#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 416.

Current-provider re-audit of the original null-soft U2 pruning.

Historical Iteration 308 killed 18/30 cubic U2 placements because a singleton
null-soft external mode on either V1 factor vanishes through the linear EOM.
Iteration 350 later proved only that this pruning cannot be transported to the
separate generic timelike fixture.  This gate returns to the ORIGINAL frozen
s=0.016 row of Iterations 295/307 and evaluates the final physical same-parent
V1 A=(D R)*epsilon provider of Iteration 341 on exactly that null-TT soft mode.

No cut integration is performed.  We test two independent ghost-loop momenta.
The singleton soft first-background coefficient must vanish at the frozen exact
zero threshold, while the mixed soft-hard second-background coefficients must
remain nonzero; otherwise the old 12-survivor U2 pruning is not re-promoted.
"""
from __future__ import annotations
import contextlib, importlib.util, io, json, re
from pathlib import Path
import numpy as np

ITERATION=416
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration341_u2_v1_a12_same_parent_geometry.py'
SRC=PARENT.read_text().split('def geom_x',1)[0]

OLD=(r"D=4; M=2; ZERO=\(0,0\)\neta=np\.diag\(\[-1\.,1\.,1\.,1\.\]\)\.astype\(complex\)\nrng=np\.random\.default_rng\(341\)\nhs=\[\]\n"
     r"for _ in range\(M\):\n    x=rng\.normal\(size=\(D,D\)\); hs\.append\(0\.08\*\(x\+x\.T\)/2\)\n"
     r"qs=\[np\.array\(\[\.31,-\.17,\.23,\.11\]\), np\.array\(\[-\.19,\.29,\.13,-\.37\]\)\]\n"
     r"p=np\.array\(\[\.43,-\.27,\.39,\.21\]\)")

PROBES=[np.array([.43,-.27,.39,.21]),np.array([.61,.19,-.31,.47])]
SOFT_ZERO_ABS_MAX=1e-12
MIXED_NONZERO_ABS_MIN=1e-12
KIN_TOL=2e-13

# Exact original row constructor, copied in provenance from Iteration 295.
spec=importlib.util.spec_from_file_location('i273',ROOT/'iteration273_closed_kinematics_physical_b3.py')
i273=importlib.util.module_from_spec(spec); spec.loader.exec_module(i273)
mm=i273.m
ETA=mm.ETA; KS=mm.K_S.copy(); ES=mm.E_S.copy(); S=0.016
a0=(.46+S)/.2
KA=np.array([a0,.6,.3,a0-.1]); KB=-(KS+KA)
HA=mm.tt_pol(KA,[.2,-.5,.7]); HB=mm.tt_pol(KB,[.8,.1,.3])


def mdot(x,y): return float(np.asarray(x)@ETA@np.asarray(y))
kin={'s':S,'ks2':mdot(KS,KS),'ka2':mdot(KA,KA),'kb2':mdot(KB,KB),
     'ks_dot_ka':mdot(KS,KA),'closure_max_abs':float(np.max(np.abs(KS+KA+KB)))}
kin_ok=bool(abs(kin['ks2'])<=KIN_TOL and abs(kin['ka2']+0.016)<=KIN_TOL and
            abs(kin['kb2']+0.216)<=KIN_TOL and abs(kin['ks_dot_ka']+0.1)<=KIN_TOL and
            kin['closure_max_abs']<=KIN_TOL)
if not kin_ok: raise RuntimeError(('nullsoft_row_drift',kin))


def provider_at(probe):
    new=f"""D=4; M=3; ZERO=(0,0,0)
eta=np.diag([-1.,1.,1.,1.]).astype(complex)
hs=[np.array({ES.tolist()},complex),np.array({HA.tolist()},complex),np.array({HB.tolist()},complex)]
qs=[np.array({KS.tolist()},float),np.array({KA.tolist()},float),np.array({KB.tolist()},float)]
p=np.array({np.asarray(probe,float).tolist()},float)"""
    src,n=re.subn(OLD,new,SRC,count=1)
    if n!=1: raise RuntimeError(('iteration341_fixture_signature_drift',n))
    ns={'__name__':'iteration416_nullsoft_v1_provider','__file__':str(PARENT)}
    with contextlib.redirect_stdout(io.StringIO()): exec(compile(src,str(PARENT),'exec'),ns,ns)
    A=ns['Acoef']
    keys={'soft_A1':(1,0,0),'hard_a_A1':(0,1,0),'hard_b_A1':(0,0,1),
          'soft_a_A2':(1,1,0),'soft_b_A2':(1,0,1),'hard_ab_A2':(0,1,1)}
    return {name:float(np.max(np.abs(A[k]))) for name,k in keys.items()}

rows=[]
for p in PROBES:
    norms=provider_at(p)
    rows.append({'ghost_loop_probe':p.tolist(),'max_abs_V1_coefficients':norms})

max_soft=max(r['max_abs_V1_coefficients']['soft_A1'] for r in rows)
min_mixed=min(r['max_abs_V1_coefficients']['soft_a_A2'] for r in rows for _ in [0])
min_mixed=min(min_mixed,min(r['max_abs_V1_coefficients']['soft_b_A2'] for r in rows))
min_hard=min(min(r['max_abs_V1_coefficients']['hard_a_A1'],r['max_abs_V1_coefficients']['hard_b_A1']) for r in rows)
all_finite=all(np.isfinite(x) for r in rows for x in r['max_abs_V1_coefficients'].values())
soft_zero=bool(max_soft<=SOFT_ZERO_ABS_MAX)
mixed_retained=bool(min_mixed>MIXED_NONZERO_ABS_MIN and min_hard>MIXED_NONZERO_ABS_MIN)
execution_valid=bool(kin_ok and all_finite)
pruning_repromoted=bool(execution_valid and soft_zero and mixed_retained)
classification=(
 'PASS_U2_ORIGINAL_NULLSOFT_CURRENT_PHYSICAL_V1_REAUDIT__18_SINGLETON_SOFT_KILLS_REPROMOTED__12_SURVIVORS' if pruning_repromoted else
 'PASS_U2_ORIGINAL_NULLSOFT_CURRENT_PHYSICAL_V1_REAUDIT__PRUNING_NOT_REPROMOTED' if execution_valid else
 'FAIL_U2_ORIGINAL_NULLSOFT_CURRENT_PHYSICAL_V1_REAUDIT_EXECUTION'
)
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
 'classification':classification,
 'original_nullsoft_row':kin,
 'physical_provider':'Iteration341 same-parent V1 A=(D R)*epsilon, specialized to exact Iteration295/307 external modes',
 'probe_results':rows,
 'observed':{'max_singleton_soft_A1_abs':max_soft,'min_mixed_soft_hard_A2_abs':min_mixed,'min_hard_A1_abs':min_hard,
             'singleton_soft_zero_preserved':soft_zero,'mixed_soft_hard_retained':mixed_retained},
 'thresholds':{'singleton_soft_A1_abs_max':SOFT_ZERO_ABS_MAX,'mixed_or_hard_nonzero_abs_min':MIXED_NONZERO_ABS_MIN,'kinematic_abs_max':KIN_TOL},
 'route_authority':{'raw_U2_cubic_placements':30,'historical_singleton_soft_killed':18,
                    'historical_survivors':12,'current_physical_nullsoft_pruning_repromoted':pruning_repromoted,
                    'timelike_rebase_pruning_reusable':False},
 'scope':'ORIGINAL_NULLSOFT_PHYSICAL_V1_PRUNING_REAUDIT_ONLY__NO_CUT_INTEGRATION__NO_TRU1SQ_CLAIM',
 'guardrails':['ITERATION350_TIMELIKE_NEGATIVE_RESULT_REMAINS_VALID_ONLY_FOR_TIMELIKE_REBASE',
               'MIXED_SOFT_HARD_A2_MUST_NOT_BE_ZERO_FILLED','TWO_INDEPENDENT_GHOST_MOMENTA',
               'NO_TIMELIKE_TO_NULL_EXTRAPOLATION','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('if pruning re-promoted, independently re-audit the TrU1sq singleton-soft V2 zero with the current U1 physical provider on the same original row; only then freeze the reduced 12-U2 plus 8-cyclic-TrU1sq null-soft e2 workload' if pruning_repromoted else
              'preserve all 30 U2 placements for original null-soft physical routing and diagnose only the failed current-provider zero/mixed condition')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid: raise SystemExit(2)
