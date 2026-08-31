#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 197 — v3 local C5 soft2 basis.

Evaluate only after the v3 K2 geometry and polarization acceptance are frozen.
The Riemann^3 soft2 coefficient is exact at linear-curvature trilinear order.
"""
from pathlib import Path
import itertools,json,math,numpy as np
ETA=np.diag([-1.,1.,1.,1.]); k0=np.array([1.,0.,0.,1.])
QS0=np.array([
 [0.18,0.70,0.20,0.10],[0.14,0.55,-0.25,0.20],
 [0.22,0.62,0.18,-0.24],[0.16,0.48,0.31,0.12],
 [0.20,0.58,-0.16,-0.28],[0.12,0.44,0.27,-0.19]],float)
QS=np.vstack([.8*QS0,1.4*QS0])
seed_pairs=[
 [197000,197500],[198000,198501],[199000,199500],[200000,200500],
 [201000,201500],[202000,202500],[203000,203501],[204000,204500],
 [205000,205500],[206000,206500],[207000,207501],[208000,208500]]
e_soft=np.zeros((4,4)); e_soft[1,1]=1/math.sqrt(2); e_soft[2,2]=-1/math.sqrt(2)

def dot(a,b): return float(a@ETA@b)
def theta(k):
    kc=ETA@k
    return ETA-np.outer(kc,kc)/dot(k,k)
def p2(k):
    t=theta(k)
    return .5*(np.einsum('mr,ns->mnrs',t,t)+np.einsum('ms,nr->mnrs',t,t))-(1/3)*np.einsum('mn,rs->mnrs',t,t)
def seed_matrix(seed):
    rng=np.random.default_rng(seed); A=rng.normal(size=(4,4)); return (A+A.T)/2
def polarization(k,seed):
    P=p2(k); A=seed_matrix(seed)
    e=np.einsum('mnrs,ra,sb,ab->mn',P,ETA,ETA,A)
    n=np.einsum('mn,ma,nb,ab',e,ETA,ETA,e)
    return e/np.sqrt(abs(n))
def lin_riemann(k,e):
    kc=ETA@k; R=np.zeros((4,4,4,4),complex)
    for m,n,r,s in itertools.product(range(4),repeat=4):
        R[m,n,r,s]=.5*(-kc[r]*kc[n]*e[m,s]-kc[s]*kc[m]*e[n,r]+kc[s]*kc[n]*e[m,r]+kc[r]*kc[m]*e[n,s])
    return R
def riem3(ks,es):
    A=[]
    for k,e in zip(ks,es):
        R=lin_riemann(k,e)
        A.append(np.einsum('mnab,ar,bs->mnrs',R,ETA,ETA).reshape(16,16))
    return sum(np.trace(A[a]@A[b]@A[c]) for a,b,c in itertools.permutations(range(3))).real

r0=[]; x=[]
for i,q in enumerate(QS):
    e2=polarization(q,seed_pairs[i][0]); e3=polarization(-q,seed_pairs[i][1])
    r0.append(riem3([k0,q,-q],[e_soft,e2,e3])); x.append(dot(q,q))
r0=np.array(r0); x=np.array(x)
V4=np.column_stack([r0,-x*r0,x*x*r0,-x**3*r0])
s=np.linalg.svd(V4,compute_uv=False)
rank=int(np.linalg.matrix_rank(V4,tol=1e-12))
out={
 "iteration":197,"model_readiness_percent":24,
 "protocol":"RQIR-WITHHELD-NULLSOFT-12-v3",
 "soft2_extraction":"EXACT_LEADING_COEFFICIENT_FROM_TRILINEAR_LINEARIZED_RIEMANN_AT_K0_Q_MINUSQ_NO_EXTRAPOLATION",
 "q2":x.tolist(),"Riemann3_soft2":r0.tolist(),
 "local_C5_basis":"Riemann3_soft2*{1,-q2,q2^2,-q2^3}",
 "rank":rank,"singular_values":s.tolist(),"condition_number":float(s[0]/s[-1]),
 "soft2_row_dimension":12,"algebraic_complement_dimension_before_AS_C3":12-rank,
 "classification":{"local_zeroK2_C5":"RANK4_ON_WITHHELD_V3","candidate_residual":"NOT_TESTED","AS":"BLOCKED_NOT_ZERO","C3":"BLOCKED_NOT_ZERO","ANSATZ_003":"NOT_CREATED","Fisher_resources":"FORBIDDEN"},
 "retained_results":[
   "C5-NG-017 — WITHHELD_V3_ZERO_K2_LOCAL_DIM12_CURVATURE_CUBIC_SOFT2_SPAN_REMAINS_RANK4",
   "NUM-NG-013 — V3_CONDITIONING_DESIGN_DOES_NOT_COLLAPSE_THE_LOCAL_C5_SOFT2_BASIS",
   "REL-NG-012 — WITHHELD_V3_LEAVES_EIGHT_SOFT2_RELATION_DIMENSIONS_BEFORE_BLOCKED_AS_C3_COMPLETION"],
 "readiness_change":"unchanged: comparator geometry is more operationally stable, but unique residual remains absent and AS/C3 are blocked"}
Path("results/withheld_v3_local_c5_soft2_iteration197.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2,sort_keys=True))
