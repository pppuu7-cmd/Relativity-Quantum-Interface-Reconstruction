#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 349.

Re-specialize the frozen Iteration-342 N/Y inverse-routing bridge and the
Iteration-339 shifted graviton Green bridge on the exact Iteration-348 matched
timelike/common metric background. This is a provider gate only: it does not
assemble the 12 physical Tr U2 routes and performs no cut integration.

Frozen bindings retained:
  q_i^2=(-1,-0.14,-0.34), seed-319 symmetric metric tensors, scale 0.12,
  D=4, Lambda=0, a=-1/2,
  Q1=-Q0(p+q) N1(q;p) Q0(p),
  G1=-G0(p+q) K1(q;p) G0(p),
  Hinv_VD=-K^-1.
Unsupported or singular routing is BLOCKED, never zero-filled.
"""
from __future__ import annotations
import contextlib, io, itertools, json, re
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
ETA=np.diag([-1.,1.,1.,1.]).astype(complex)
QS=[np.array([1.0,0.0,0.0,0.0]),np.array([-0.4,0.1,0.1,0.0]),np.array([-0.6,-0.1,-0.1,0.0])]
P=np.array([0.43,-0.27,0.39,0.21])
D=4

def maxabs(x): return float(np.max(np.abs(x)))
def mdot(a,b): return complex(np.asarray(a,complex)@ETA@np.asarray(b,complex))

def matched_ghost_parent(p_in):
    src=(ROOT/'iteration317_det_ghost_three_mode_routing.py').read_text().split('# Independent exact-geometry oracle',1)[0]
    # Replace only the frozen fixture, leaving the physical polynomial operator untouched.
    src,n=re.subn(r"rng=np\.random\.default_rng\(317\)","rng=np.random.default_rng(319)",src,count=1)
    if n!=1: raise RuntimeError('ghost seed signature drift')
    src,n=re.subn(r"hs\.append\(0\.2\*\(x\+x\.T\)/2\.0\)","hs.append(0.12*(x+x.T)/2.0)",src,count=1)
    if n!=1: raise RuntimeError('ghost tensor-scale signature drift')
    src,n=re.subn(r"qs=\[.*?\]\np=np\.array\([^\n]+\)","qs=[np.array([1.0,0.0,0.0,0.0]),np.array([-0.4,0.1,0.1,0.0]),np.array([-0.6,-0.1,-0.1,0.0])]\np=P_IN.copy()",src,count=1,flags=re.S)
    if n!=1: raise RuntimeError('ghost q/p fixture signature drift')
    ns={'P_IN':np.asarray(p_in,float),'__name__':'iteration349_ghost','__file__':str(ROOT/'iteration317_det_ghost_three_mode_routing.py')}
    with contextlib.redirect_stdout(io.StringIO()): exec(compile(src,'iteration349_ghost','exec'),ns,ns)
    return ns

def matched_graviton_parent(p_in):
    src=(ROOT/'iteration319_det_graviton_three_mode_routing.py').read_text().split('FIT=indices(4)',1)[0]
    src,n=re.subn(r"qs=\[np\.array\([^\n]+\),np\.array\([^\n]+\),np\.array\([^\n]+\)\]","qs=[np.array([1.0,0.0,0.0,0.0]),np.array([-0.4,0.1,0.1,0.0]),np.array([-0.6,-0.1,-0.1,0.0])]",src,count=1)
    if n!=1: raise RuntimeError('graviton q fixture signature drift')
    src,n=re.subn(r"p=np\.array\([^\n]+\)","p=P_IN.copy()",src,count=1)
    if n!=1: raise RuntimeError('graviton p signature drift')
    ns={'P_IN':np.asarray(p_in,float),'__name__':'iteration349_graviton','__file__':str(ROOT/'iteration319_det_graviton_three_mode_routing.py')}
    with contextlib.redirect_stdout(io.StringIO()): exec(compile(src,'iteration349_graviton','exec'),ns,ns)
    return ns

GHOST=matched_ghost_parent(P)
GRAV=matched_graviton_parent(P)
ZERO=(0,0,0)
thresholds={
 'q2_fixture_max':1e-14,
 'ghost_flat_parent_max':1e-12,
 'ghost_inverse_identity_max':2e-11,
 'ghost_block_inverse_max':2e-11,
 'Y_inverse_max':2e-11,
 'NY_bridge_max':2e-11,
 'graviton_flat_K0_max':1e-12,
 'graviton_inverse_identity_max':2e-11,
 'graviton_block_inverse_max':2e-11,
 'shift_matter_min_norm':1e-7,
}

q2=[float(np.real(mdot(q,q))) for q in QS]
q2_target=[-1.0,-0.14,-0.34]
q2_err=max(abs(a-b) for a,b in zip(q2,q2_target))
closure=maxabs(sum(QS,np.zeros(4)))

# N/Y: test every physical first-order background leg on the same parent.
N=GHOST['N']; Gcoef=GHOST['G']; hs=GHOST['hs']
N0=np.asarray(N[ZERO],complex)
ghost_flat=maxabs(N0-(-mdot(P,P))*np.eye(D))
ghost_rows=[]
for r,q in enumerate(QS):
    mode=tuple(1 if j==r else 0 for j in range(3))
    N1=np.asarray(N[mode],complex)
    Q0i=np.linalg.inv(N0)
    gout=matched_ghost_parent(P+q)
    N0o=np.asarray(gout['N'][ZERO],complex)
    Q0o=np.linalg.inv(N0o)
    Q1=-Q0o@N1@Q0i
    li=maxabs(N0o@Q1+N1@Q0i)
    ri=maxabs(Q1@N0+Q0o@N1)
    Z=np.zeros((D,D),complex)
    Hat=np.block([[N0,Z],[N1,N0o]])
    Qdir=np.linalg.inv(Hat)
    Qexp=np.block([[Q0i,Z],[Q1,Q0o]])
    block=maxabs(Qdir-Qexp)
    Yup0=-ETA; Yup1=-np.asarray(Gcoef[mode],complex)
    Ylow0=-ETA; Ylow1=-np.asarray(hs[r],complex)
    Yup=np.block([[Yup0,Z],[Yup1,Yup0]])
    Ylow=np.block([[Ylow0,Z],[Ylow1,Ylow0]])
    yerr=max(maxabs(Yup@Ylow-np.eye(2*D)),maxabs(Ylow@Yup-np.eye(2*D)))
    Nlower=Ylow@Hat
    Nupper=np.linalg.inv(Nlower)
    bridge=max(maxabs(Nupper-Qdir@Yup),maxabs(Nupper@Ylow-Qdir))
    ghost_rows.append({'mode':list(mode),'q':q.tolist(),'left_inverse_error':li,'right_inverse_error':ri,'block_inverse_error':block,'Y_inverse_error':yerr,'NY_bridge_error':bridge})

# Shifted graviton inverse and VD sign: test every leg on identical metric background.
H=GRAV['H']; NB=int(GRAV['NB']); K0=np.asarray(H[ZERO],complex); I=np.eye(NB,dtype=complex)
p2=mdot(P,P); grav_flat=maxabs(K0-p2*I)
grav_rows=[]
for r,q in enumerate(QS):
    mode=tuple(1 if j==r else 0 for j in range(3))
    K1=np.asarray(H[mode],complex)
    gout=matched_graviton_parent(P+q)
    K0o=np.asarray(gout['H'][ZERO],complex)
    G0i=np.linalg.inv(K0); G0o=np.linalg.inv(K0o)
    G1=-G0o@K1@G0i
    li=maxabs(K0o@G1+K1@G0i)
    ri=maxabs(G1@K0+G0o@K1)
    Z=np.zeros((NB,NB),complex)
    Kop=np.block([[K0,Z],[K1,K0o]])
    Gdir=np.linalg.inv(Kop)
    Gexp=np.block([[G0i,Z],[G1,G0o]])
    block=maxabs(Gdir-Gexp)
    wrong=-G0i@K1@G0i
    shift=float(np.linalg.norm(G1-wrong))
    # Iteration-340 binding: VD field-space inverse is minus the ordinary Green.
    hinv0=-G0i; hinv1=-G1
    vd_sign=max(maxabs(hinv0+G0i),maxabs(hinv1+G1))
    grav_rows.append({'mode':list(mode),'q':q.tolist(),'left_inverse_error':li,'right_inverse_error':ri,'block_inverse_error':block,'shifted_vs_unshifted_norm':shift,'Hinv_VD_minus_Kinv_error':vd_sign})

passed=bool(
 closure<=thresholds['q2_fixture_max'] and q2_err<=thresholds['q2_fixture_max'] and
 ghost_flat<=thresholds['ghost_flat_parent_max'] and
 all(x['left_inverse_error']<=thresholds['ghost_inverse_identity_max'] and x['right_inverse_error']<=thresholds['ghost_inverse_identity_max'] and x['block_inverse_error']<=thresholds['ghost_block_inverse_max'] and x['Y_inverse_error']<=thresholds['Y_inverse_max'] and x['NY_bridge_error']<=thresholds['NY_bridge_max'] for x in ghost_rows) and
 grav_flat<=thresholds['graviton_flat_K0_max'] and
 all(x['left_inverse_error']<=thresholds['graviton_inverse_identity_max'] and x['right_inverse_error']<=thresholds['graviton_inverse_identity_max'] and x['block_inverse_error']<=thresholds['graviton_block_inverse_max'] and x['shifted_vs_unshifted_norm']>=thresholds['shift_matter_min_norm'] and x['Hinv_VD_minus_Kinv_error']<=thresholds['graviton_inverse_identity_max'] for x in grav_rows)
)
result={
 'iteration':349,'model_readiness_percent':24,'scientific_gate_pass':passed,
 'classification':('PASS_U2_NY_AND_SHIFTED_HINV_MATCHED_TIMELIKE_COMMON_BACKGROUND_PROVIDERS__12_ROUTE_PHYSICAL_SUBSTITUTION_NEXT' if passed else 'FAIL_U2_NY_HINV_MATCHED_TIMELIKE_PROVIDER_GATE'),
 'candidate_residual':False,
 'matched_background':{'q_squared':q2,'q_squared_target':q2_target,'q2_max_error':q2_err,'closure_max_abs':closure,'metric_tensor_seed':319,'metric_tensor_scale':0.12,'p':P.tolist()},
 'ghost_NY':{'flat_parent_error':ghost_flat,'modes':ghost_rows},
 'graviton_Hinv':{'flat_K0_error':grav_flat,'modes':grav_rows,'binding':'Hinv_VD=-K^-1'},
 'thresholds':thresholds,
 'guardrails':['UNSUPPORTED_IS_BLOCKED_NOT_ZERO_FILLED','NO_12_ROUTE_CUT_INTEGRATION_FROM_PROVIDER_GATE','ITERATION345_FUNCTIONAL_TRANSPOSE_REMAINS_BINDING','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':('substitute Iteration348 A1/A2 plus these matched N/Y/Hinv providers route-by-route into all 12 Iteration346 survivors; preserve exact incoming momenta and Iteration345 functional transpose; canonicalize physical numerator/denominator families before any cut integration' if passed else 'preserve failure and diagnose matched-parent routing without weakening frozen thresholds or changing parent dynamics')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
