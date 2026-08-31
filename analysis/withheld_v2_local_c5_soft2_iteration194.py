#!/usr/bin/env python3
"""Iteration 194: zero-K2 local C5 curvature-cubic soft2 basis on the
prospectively frozen, geometry-conditioned 12-row v2 protocol.

For the cyclic Riemann^3 operator, the soft linearized Riemann is exactly
quadratic in k_soft=eps*k0.  Hence the O(eps^2) coefficient is obtained directly
by evaluating the trilinear linear-curvature contraction at (k0,q,-q), without
numerical soft extrapolation.  Iteration-178 identities then generate the local
dimension-12 span r0*{1,-q2,q2^2,-q2^3}.
"""
from pathlib import Path
import itertools,json,math,numpy as np
ETA=np.diag([-1.,1.,1.,1.]); k0=np.array([1.,0.,0.,1.])
QS0=np.array([[0.18,0.70,0.20,0.10],[0.14,0.55,-0.25,0.20],[0.22,0.62,0.18,-0.24],[0.16,0.48,0.31,0.12],[0.20,0.58,-0.16,-0.28],[0.12,0.44,0.27,-0.19]],float)
QS=np.vstack([.75*QS0,1.25*QS0])
seed_pairs=[[193000,193500],[194000,194500],[195000,195500],[196000,196500],[197000,197500],[198000,198500],[199000,199501],[200000,200500],[201000,201500],[202000,202500],[203000,203500],[204000,204500]]
e_soft=np.zeros((4,4)); e_soft[1,1]=1/math.sqrt(2); e_soft[2,2]=-1/math.sqrt(2)
def dot(a,b): return float(a@ETA@b)
def theta(k):
    kc=ETA@k; return ETA-np.outer(kc,kc)/dot(k,k)
def p2(k):
    t=theta(k); return .5*(np.einsum('mr,ns->mnrs',t,t)+np.einsum('ms,nr->mnrs',t,t))-(1/3)*np.einsum('mn,rs->mnrs',t,t)
def seed_matrix(seed):
    rng=np.random.default_rng(seed); A=rng.normal(size=(4,4)); return (A+A.T)/2
def polarization(k,seed):
    P=p2(k); A=seed_matrix(seed); e=np.einsum('mnrs,ra,sb,ab->mn',P,ETA,ETA,A)
    n=np.einsum('mn,ma,nb,ab',e,ETA,ETA,e); return e/np.sqrt(abs(n))
def lin_riemann(k,e):
    kc=ETA@k; R=np.zeros((4,4,4,4),complex)
    for m,n,r,s in itertools.product(range(4),repeat=4):
        R[m,n,r,s]=.5*(-kc[r]*kc[n]*e[m,s]-kc[s]*kc[m]*e[n,r]+kc[s]*kc[n]*e[m,r]+kc[r]*kc[m]*e[n,s])
    return R
def riem3(ks,es):
    A=[]
    for k,e in zip(ks,es):
        R=lin_riemann(k,e); A.append(np.einsum('mnab,ar,bs->mnrs',R,ETA,ETA).reshape(16,16))
    return sum(np.trace(A[a]@A[b]@A[c]) for a,b,c in itertools.permutations(range(3))).real
r0=[]; x=[]
for i,q in enumerate(QS):
    e2=polarization(q,seed_pairs[i][0]); e3=polarization(-q,seed_pairs[i][1])
    r0.append(riem3([k0,q,-q],[e_soft,e2,e3])); x.append(dot(q,q))
r0=np.array(r0); x=np.array(x)
V4=np.column_stack([r0,-x*r0,x*x*r0,-x**3*r0]); s=np.linalg.svd(V4,compute_uv=False)
out={"iteration":194,"model_readiness_percent":24,"protocol":"RQIR-WITHHELD-NULLSOFT-12-v2",
 "soft2_extraction":"EXACT_LEADING_COEFFICIENT_FROM_TRILINEAR_LINEARIZED_RIEMANN_AT_K0_Q_MINUSQ_NO_EXTRAPOLATION",
 "q2":x.tolist(),"Riemann3_soft2":r0.tolist(),"local_C5_basis":"Riemann3_soft2*{1,-q2,q2^2,-q2^3}",
 "rank":int(np.linalg.matrix_rank(V4,tol=1e-12)),"singular_values":s.tolist(),"condition_number":float(s[0]/s[-1]),
 "soft2_row_dimension":12,"algebraic_complement_dimension_before_AS_C3":int(12-np.linalg.matrix_rank(V4,tol=1e-12)),
 "classification":{"local_zeroK2_C5":"RANK4_ON_WITHHELD_V2","nonlocal_lambda_zeroK2_nuisance":"REMOVED_BY_ITERATION191_EXACT_K2_CALIBRATION","candidate_residual":"NOT_TESTED","AS":"BLOCKED_NOT_ZERO","C3":"BLOCKED_NOT_ZERO","ANSATZ_003":"NOT_CREATED","Fisher_resources":"FORBIDDEN"},
 "retained_results":["C5-NG-014 — WITHHELD_V2_ZERO_K2_LOCAL_DIM12_CURVATURE_CUBIC_SOFT2_SPAN_REMAINS_RANK4","NUM-NG-008 — EXACT_RIEMANN_SOFT2_COEFFICIENT_REMOVES_SOFT_EXTRAPOLATION_ERROR_FOR_THE_CURVATURE_CUBIC_BASE","REL-NG-009 — WITHHELD_V2_LEAVES_EIGHT_SOFT2_RELATION_DIMENSIONS_BEFORE_BLOCKED_AS_C3_COMPLETION"],
 "readiness_change":"unchanged: the prospective comparator geometry is much less saturated, but AS/C3 are blocked and no candidate residual has been tested"}
Path('results/withheld_v2_local_c5_soft2_iteration194.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
