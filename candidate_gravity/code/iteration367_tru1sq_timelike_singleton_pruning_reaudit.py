#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 367.

Physical re-audit of the historical Iteration-310 singleton-soft pruning premise
for Tr U1^2 after the Iteration-350 timelike rebase.

Historical U1 notation (Iterations 270/291):
    B = Q V2 Q,      U1 = B Y_down.
The old null-soft fixture had the singleton V2/U1 block on the soft leg equal to
zero and Iteration 310 used that premise to reduce 42 ordered cubic placements to
16 survivors / 8 cyclic classes.

That pruning must not be transported to the current timelike fixture without a
physical check.  This gate uses the same-parent finite-geometry V2 construction
from Iteration 270, but replaces only the external fixture by the current common
background:
    q_s=(1,0,0,0), q_a=(-.4,.1,.1,0), q_b=(-.6,-.1,-.1,0),
    q_i^2=(-1,-.14,-.34), sum q_i=0,
    seed-319 symmetric metric tensors at scale .12.

Two independent derivative stencils (2-point and 5-point central) and a step scan
are used.  The old translation-closed null-soft fixture is re-evaluated as a
negative control.  This gate does not contract all 42 Tr U1^2 placements and does
not perform a cut integral.
"""
from __future__ import annotations
import contextlib, io, json, math
from pathlib import Path
import numpy as np

ITERATION=367
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration270_vd_physical_b3_nonzero.py'
src=PARENT.read_text().split('# A-layer certificates.',1)[0]
ns={'__name__':'iteration367_v2_parent','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src,str(PARENT),'exec'),ns,ns)

ETA=ns['ETA']; A_finite=ns['A_finite']; Q0=ns['Q0']; y_down=ns['y_down']; tt_pol=ns['tt_pol']
P=np.array([.43,-.27,.39,.21],float)

TIMELIKE_Q=[np.array([1.,0.,0.,0.]),np.array([-.4,.1,.1,0.]),np.array([-.6,-.1,-.1,0.])]
rng=np.random.default_rng(319)
TIMELIKE_H=[]
for _ in range(3):
    x=rng.normal(size=(4,4)); TIMELIKE_H.append(0.12*(x+x.T)/2.0)
TL={x:(TIMELIKE_Q[i],TIMELIKE_H[i]) for i,x in enumerate(('s','a','b'))}

# Historical translation-closed null-soft control from Iteration 273.
KS=ns['K_S'].copy(); KA=ns['K_A'].copy(); KB=-(KS+KA)
ES=ns['E_S'].copy(); EA=ns['E_A'].copy(); EB=tt_pol(KB,[.8,.1,.3])
NULL={'s':(KS,ES),'a':(KA,EA),'b':(KB,EB)}


def mdot(a,b):
    return float(np.real(np.asarray(a,float)@ETA@np.asarray(b,float)))


def A1_2point(M,x,p,h):
    q,e=M[x]
    fp=A_finite([h],[(q,e)],p,q)
    fm=A_finite([-h],[(q,e)],p,q)
    return (fp-fm)/(2.0*h)


def A1_5point(M,x,p,h):
    q,e=M[x]
    def f(t): return A_finite([t],[(q,e)],p,q)
    return (f(-2*h)-8.0*f(-h)+8.0*f(h)-f(2*h))/(12.0*h)


def U1_from_A1(M,x,p,A1):
    q,_=M[x]
    B1=Q0(p+q)@A1@Q0(p)
    Y0=y_down([],[])
    return B1@Y0, B1

STEPS=[1.0e-4,5.0e-5,2.5e-5]
rows=[]
for label,M in [('historical_nullsoft_control',NULL),('current_timelike_common_background',TL)]:
    for x in ('s','a','b'):
        vals=[]
        for h in STEPS:
            A5=A1_5point(M,x,P,h)
            U5,B5=U1_from_A1(M,x,P,A5)
            vals.append({'h':h,'A1_fro':float(np.linalg.norm(A5)),'B1_fro':float(np.linalg.norm(B5)),'U1_1_fro':float(np.linalg.norm(U5))})
        h=STEPS[1]
        A2=A1_2point(M,x,P,h); A5=A1_5point(M,x,P,h)
        U2,_=U1_from_A1(M,x,P,A2); U5,_=U1_from_A1(M,x,P,A5)
        denom=max(float(np.linalg.norm(U5)),1e-30)
        stencil_rel=float(np.linalg.norm(U2-U5)/denom)
        unorms=np.array([v['U1_1_fro'] for v in vals],float)
        step_rel=float((unorms.max()-unorms.min())/max(unorms.max(),1e-30))
        rows.append({'fixture':label,'leg':x,'q2':mdot(M[x][0],M[x][0]),'step_scan':vals,
                     'two_vs_five_point_U1_relative_error':stencil_rel,'U1_step_relative_spread':step_rel,
                     'reference_U1_1_fro':float(np.linalg.norm(U5)),'reference_A1_fro':float(np.linalg.norm(A5))})

by={(r['fixture'],r['leg']):r for r in rows}
old_s=by[('historical_nullsoft_control','s')]
new_s=by[('current_timelike_common_background','s')]
closure=float(np.max(np.abs(sum(TIMELIKE_Q,np.zeros(4)))))
q2=[mdot(q,q) for q in TIMELIKE_Q]
q2err=max(abs(a-b) for a,b in zip(q2,[-1.0,-0.14,-0.34]))

TH={
 'fixture_closure_max':1e-14,
 'q2_fixture_max_error':1e-14,
 'historical_nullsoft_U1_max':2e-7,
 'timelike_singleton_U1_min':1e-6,
 'timelike_two_vs_five_point_relative_max':2e-4,
 'timelike_step_relative_spread_max':2e-4,
}
new_nonzero_margin=new_s['reference_U1_1_fro']/TH['timelike_singleton_U1_min']
passed=bool(
 closure<=TH['fixture_closure_max'] and q2err<=TH['q2_fixture_max_error'] and
 old_s['reference_U1_1_fro']<=TH['historical_nullsoft_U1_max'] and
 new_s['reference_U1_1_fro']>=TH['timelike_singleton_U1_min'] and
 new_s['two_vs_five_point_U1_relative_error']<=TH['timelike_two_vs_five_point_relative_max'] and
 new_s['U1_step_relative_spread']<=TH['timelike_step_relative_spread_max']
)
classification=('PASS_TRU1SQ_TIMELIKE_REBASE_INVALIDATES_OLD_SINGLETON_SOFT_PRUNING__FULL_PREPRUNING_PHYSICAL_ROUTING_REQUIRED'
                if passed else 'FAIL_TRU1SQ_TIMELIKE_SINGLETON_PRUNING_REAUDIT')
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':passed,'candidate_residual':False,
 'classification':classification,
 'current_fixture':{'q_squared':q2,'q_squared_target':[-1.0,-0.14,-0.34],'q2_max_error':q2err,
                    'momentum_closure_max_abs':closure,'metric_tensor_seed':319,'metric_tensor_scale':0.12,'loop_probe_p':P.tolist()},
 'historical_pruning_premise':{'iteration':310,'raw_ordered_placements':42,'historical_killed':26,'historical_surviving_ordered':16,'historical_cyclic_classes':8,
                               'status_on_timelike_fixture':'NOT_TRANSFERABLE_UNLESS_SINGLETON_ZERO_REPROVED'},
 'thresholds':TH,'rows':rows,
 'key_comparison':{
    'historical_nullsoft_s_U1_1_fro':old_s['reference_U1_1_fro'],
    'current_timelike_s_U1_1_fro':new_s['reference_U1_1_fro'],
    'current_timelike_s_nonzero_margin_over_frozen_min':new_nonzero_margin,
    'current_timelike_s_two_vs_five_point_relative_error':new_s['two_vs_five_point_U1_relative_error'],
    'current_timelike_s_step_relative_spread':new_s['U1_step_relative_spread'],
 },
 'scope':'SINGLETON_FIRST_ORDER_U1_PRUNING_PREMISE_ONLY__NO_FULL_TRU1SQ_CONTRACTION__NO_CUT_INTEGRAL',
 'guardrails':['SAME_PARENT_V2_GEOMETRY','CURRENT_TIMELIKE_COMMON_BACKGROUND_ONLY','OLD_8_CLASSES_NOT_PHYSICAL_IF_GATE_PASSES',
               'START_DOWNSTREAM_ROUTING_FROM_FULL_PREPRUNING_SET','NO_ZERO_FILL','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('rebuild the Tr U1^2 cubic routing on the current timelike fixture from the full pre-pruning ordered placement set, compute every physical singleton/mixed U1 block with exact routed momenta, and only then quotient by cyclic trace identities' if passed else 'preserve FAIL and diagnose same-parent V2 timelike rebase without weakening frozen thresholds')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed:
    raise SystemExit(2)
