#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 417.

Current-provider re-audit of the original null-soft Tr(U1^2) singleton-soft V2
pruning on the exact Iteration-295/307 s=0.016 row.

The physical U1 provider is the same finite-amplitude A=R.(D R).E construction
used by Iteration270 and the direct timelike family reconstruction Iteration295.
Because a central first derivative has O(h^2) error, the singleton-soft V2[s]
coefficient is evaluated at three predetermined h values and Richardson
extrapolated to h->0 before deciding whether the exact E^(1)[h_s]=0 rule is
numerically represented by the current provider. Mixed V2[s,a], V2[s,b] are
separately required to remain nonzero and stable enough to forbid over-pruning.

No cut integration or Tr(U1^2) sum is performed.
"""
from __future__ import annotations
import importlib.util, json
from pathlib import Path
import numpy as np

ITERATION=417
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('i273',ROOT/'iteration273_closed_kinematics_physical_b3.py')
i273=importlib.util.module_from_spec(spec); spec.loader.exec_module(i273)
m=i273.m
ETA=m.ETA; KS=m.K_S.copy(); ES=m.E_S.copy(); S=0.016
a0=(.46+S)/.2
KA=np.array([a0,.6,.3,a0-.1]); KB=-(KS+KA)
M={'s':(KS,ES),'a':(KA,m.tt_pol(KA,[.2,-.5,.7])),'b':(KB,m.tt_pol(KB,[.8,.1,.3]))}
PROBES=[np.array([.43,-.27,.39,.21]),np.array([.61,.19,-.31,.47])]
H1=(2e-4,1e-4,5e-5)
H2=(5e-4,2.5e-4)
SOFT_EXTRAP_ABS_MAX=1e-9
SOFT_RICHARDSON_DIFF_ABS_MAX=1e-8
MIXED_NORM_MIN=1e-8
MIXED_STEP_REL_MAX=2e-3
KIN_TOL=2e-13

def mdot(x,y): return float(np.asarray(x)@ETA@np.asarray(y))
kin={'s':S,'ks2':mdot(KS,KS),'ka2':mdot(KA,KA),'kb2':mdot(KB,KB),
     'ks_dot_ka':mdot(KS,KA),'closure_max_abs':float(np.max(np.abs(KS+KA+KB)))}
kin_ok=bool(abs(kin['ks2'])<=KIN_TOL and abs(kin['ka2']+0.016)<=KIN_TOL and
            abs(kin['kb2']+0.216)<=KIN_TOL and abs(kin['ks_dot_ka']+0.1)<=KIN_TOL and kin['closure_max_abs']<=KIN_TOL)
if not kin_ok: raise RuntimeError(('nullsoft_row_drift',kin))

rows=[]
for p in PROBES:
    soft=[m.Acoef(M,['s'],p,h) for h in H1]
    ext_coarse=(4.0*soft[1]-soft[0])/3.0
    ext_fine=(4.0*soft[2]-soft[1])/3.0
    soft_ext=float(np.max(np.abs(ext_fine)))
    soft_rich=float(np.max(np.abs(ext_fine-ext_coarse)))
    hard_a=float(np.max(np.abs(m.Asub(M,('a',),p,h1=H1[1]))))
    hard_b=float(np.max(np.abs(m.Asub(M,('b',),p,h1=H1[1]))))
    mixed={}
    for pair in (('s','a'),('s','b')):
        coarse=m.Asub(M,pair,p,h2=H2[0]); fine=m.Asub(M,pair,p,h2=H2[1])
        scale=max(1.0,float(np.max(np.abs(coarse))),float(np.max(np.abs(fine))))
        mixed[''.join(pair)]={'coarse_norm':float(np.max(np.abs(coarse))),
                              'fine_norm':float(np.max(np.abs(fine))),
                              'scaled_step_difference':float(np.max(np.abs(fine-coarse))/scale)}
    rows.append({'loop_probe':p.tolist(),
                 'soft_A1_raw_norms':[float(np.max(np.abs(x))) for x in soft],
                 'soft_A1_richardson_extrapolated_abs':soft_ext,
                 'soft_A1_successive_richardson_abs_difference':soft_rich,
                 'hard_A1_norms':{'a':hard_a,'b':hard_b},'mixed_A2':mixed})

all_finite=all(np.isfinite(v) for r in rows for v in (
    r['soft_A1_richardson_extrapolated_abs'],r['soft_A1_successive_richardson_abs_difference'],
    r['hard_A1_norms']['a'],r['hard_A1_norms']['b'],
    r['mixed_A2']['sa']['coarse_norm'],r['mixed_A2']['sa']['fine_norm'],r['mixed_A2']['sa']['scaled_step_difference'],
    r['mixed_A2']['sb']['coarse_norm'],r['mixed_A2']['sb']['fine_norm'],r['mixed_A2']['sb']['scaled_step_difference']))
max_soft_ext=max(r['soft_A1_richardson_extrapolated_abs'] for r in rows)
max_soft_rich=max(r['soft_A1_successive_richardson_abs_difference'] for r in rows)
min_hard=min(min(r['hard_A1_norms'].values()) for r in rows)
min_mixed=min(min(r['mixed_A2'][x]['fine_norm'] for x in ('sa','sb')) for r in rows)
max_mixed_step=max(max(r['mixed_A2'][x]['scaled_step_difference'] for x in ('sa','sb')) for r in rows)
soft_zero=bool(max_soft_ext<=SOFT_EXTRAP_ABS_MAX and max_soft_rich<=SOFT_RICHARDSON_DIFF_ABS_MAX)
mixed_retained=bool(min_hard>MIXED_NORM_MIN and min_mixed>MIXED_NORM_MIN and max_mixed_step<=MIXED_STEP_REL_MAX)
execution_valid=bool(kin_ok and all_finite)
pruning_repromoted=bool(execution_valid and soft_zero and mixed_retained)
classification=(
 'PASS_TRU1SQ_ORIGINAL_NULLSOFT_CURRENT_PHYSICAL_V2_REAUDIT__26_SINGLETON_SOFT_KILLS_REPROMOTED__16_ORDERED_8_CYCLIC_SURVIVORS' if pruning_repromoted else
 'PASS_TRU1SQ_ORIGINAL_NULLSOFT_CURRENT_PHYSICAL_V2_REAUDIT__PRUNING_NOT_REPROMOTED' if execution_valid else
 'FAIL_TRU1SQ_ORIGINAL_NULLSOFT_CURRENT_PHYSICAL_V2_REAUDIT_EXECUTION'
)
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
 'classification':classification,'original_nullsoft_row':kin,
 'physical_provider':'Iteration270/273 finite-amplitude Asub=A=R.(D R).E used by Iteration295 direct timelike row',
 'probe_results':rows,
 'observed':{'max_soft_A1_richardson_extrapolated_abs':max_soft_ext,
             'max_soft_A1_successive_richardson_abs_difference':max_soft_rich,
             'min_hard_A1_norm':min_hard,'min_mixed_soft_hard_A2_norm':min_mixed,
             'max_mixed_A2_scaled_step_difference':max_mixed_step,
             'singleton_soft_zero_preserved':soft_zero,'mixed_soft_hard_retained':mixed_retained},
 'thresholds':{'soft_extrapolated_abs_max':SOFT_EXTRAP_ABS_MAX,'soft_successive_richardson_abs_difference_max':SOFT_RICHARDSON_DIFF_ABS_MAX,
               'mixed_or_hard_norm_min':MIXED_NORM_MIN,'mixed_step_scaled_difference_max':MIXED_STEP_REL_MAX,'kinematic_abs_max':KIN_TOL,
               'singleton_steps':list(H1),'mixed_steps':list(H2)},
 'placement_authority':{'raw_TrU1sq_ordered_placements':42,'historical_singleton_soft_killed':26,
                        'historical_surviving_ordered':16,'historical_surviving_cyclic':8,
                        'current_physical_nullsoft_pruning_repromoted':pruning_repromoted},
 'scope':'ORIGINAL_NULLSOFT_CURRENT_PHYSICAL_V2_PRUNING_REAUDIT_ONLY__NO_CUT_INTEGRATION__NO_U2_CLAIM',
 'guardrails':['MIXED_SOFT_HARD_V2_SECOND_ORDER_MUST_NOT_BE_ZERO_FILLED','TWO_INDEPENDENT_LOOP_MOMENTA',
               'RICHARDSON_USED_ONLY_TO_TEST_THE_SINGLETON_SOFT_ZERO','NO_TIMELIKE_TO_NULL_EXTRAPOLATION',
               'NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('if pruning re-promoted and Iteration416 U2 V1 re-audit also passes, freeze the current-provider original-nullsoft e2 workload as 12 U2 routes plus 8 cyclic TrU1sq classes and classify their physical denominator/cut topology before any integration' if pruning_repromoted else
              'preserve all 42 ordered TrU1sq placements on original null-soft physical routing and diagnose only the failed provider zero/mixed condition')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid: raise SystemExit(2)
