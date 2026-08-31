#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 199.

Evaluate the zero-K2 local C5 curvature-cubic soft2 basis on the prospectively
frozen v3 K2 geometry and Iteration-198 polarization seeds.  Compare its
conditioning with withheld-v2.  This is a comparator-only evaluation; no
candidate target is used.
"""
from pathlib import Path
import itertools,json,math,numpy as np
ETA=np.diag([-1.,1.,1.,1.]); k0=np.array([1.,0.,0.,1.])
QS0=np.array([[0.18,0.70,0.20,0.10],[0.14,0.55,-0.25,0.20],[0.22,0.62,0.18,-0.24],[0.16,0.48,0.31,0.12],[0.20,0.58,-0.16,-0.28],[0.12,0.44,0.27,-0.19]],float)
QS=np.vstack([.80*QS0,1.40*QS0])
seed_pairs=[[198000,198501],[199000,199501],[200000,200500],[201000,201500],[202000,202500],[203000,203500],[204000,204500],[205000,205500],[206000,206500],[207000,207501],[208000,208500],[209000,209501]]
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
V4=np.column_stack([r0,-x*r0,x*x*r0,-x**3*r0])
s=np.linalg.svd(V4,compute_uv=False)
sn=np.linalg.svd(V4/np.linalg.norm(V4,axis=0),compute_uv=False)

# Frozen Iteration-194 v2 comparator reference.
x2=np.array([0.2855249999999999,0.21678750000000005,0.23962499999999995,0.17735625,0.22522499999999995,0.16211250000000002,0.793125,0.6021875,0.665625,0.49265624999999996,0.625625,0.45031250000000006])
r02=np.array([0.09062678834951932,0.16803920764664712,-0.09789544062570427,-0.005916118520839153,-0.029039631761568437,-0.07238006200957146,-0.06610818516517986,0.38320932719734235,0.029971342547624725,0.45560116033401604,0.6591802274467985,-0.18125066515442065])
V2=np.column_stack([r02,-x2*r02,x2*x2*r02,-x2**3*r02])
s2=np.linalg.svd(V2,compute_uv=False)
sn2=np.linalg.svd(V2/np.linalg.norm(V2,axis=0),compute_uv=False)

out={
 'iteration':199,'model_readiness_percent':24,
 'protocol':'RQIR-WITHHELD-NULLSOFT-12-v3',
 'soft2_extraction':'EXACT_LEADING_COEFFICIENT_FROM_TRILINEAR_LINEARIZED_RIEMANN_AT_K0_Q_MINUSQ_NO_EXTRAPOLATION',
 'q2':x.tolist(),'Riemann3_soft2':r0.tolist(),
 'local_C5_basis':'Riemann3_soft2*{1,-q2,q2^2,-q2^3}',
 'rank':int(np.linalg.matrix_rank(V4,tol=1e-12)),
 'singular_values':s.tolist(),'condition_number':float(s[0]/s[-1]),
 'column_normalized_singular_values':sn.tolist(),
 'column_normalized_condition_number':float(sn[0]/sn[-1]),
 'soft2_row_dimension':12,
 'algebraic_complement_dimension_before_AS_C3':int(12-np.linalg.matrix_rank(V4,tol=1e-12)),
 'comparison_to_v2':{
   'v2_raw_condition_number':float(s2[0]/s2[-1]),
   'v3_over_v2_raw_condition_factor':float((s[0]/s[-1])/(s2[0]/s2[-1])),
   'v2_column_normalized_condition_number':float(sn2[0]/sn2[-1]),
   'v3_over_v2_column_normalized_condition_factor':float((sn[0]/sn[-1])/(sn2[0]/sn2[-1]))},
 'classification':{
   'local_zeroK2_C5':'RANK4_ON_WITHHELD_V3',
   'hard_K2_conditioning':'BETTER_THAN_V2',
   'conditional_soft2_conditioning':'WORSE_THAN_V2',
   'global_protocol_preference':'NONE_TRADEOFF_REQUIRES_MULTI_OBJECTIVE_DESIGN',
   'candidate_residual':'NOT_TESTED','AS':'BLOCKED_NOT_ZERO','C3':'BLOCKED_NOT_ZERO',
   'ANSATZ_003':'NOT_CREATED','Fisher_resources':'FORBIDDEN'},
 'retained_results':[
   'C5-NG-017 — WITHHELD_V3_ZERO_K2_LOCAL_C5_SOFT2_SPAN_REMAINS_RANK4',
   'NUM-NG-013 — HARD_K2_CONDITIONING_IMPROVEMENT_CAN_WORSEN_CONDITIONAL_SOFT2_CONDITIONING',
   'PROTO-NG-006 — V2_AND_V3_FORM_A_CONDITIONING_TRADEOFF_NOT_A_TOTAL_ORDER',
   'NG-FUNNEL-053 — PROSPECTIVE_PROTOCOL_DESIGN_MUST_CONTROL_THE_FULL_JOINT_QUOTIENT_NOT_ONE_BLOCK_IN_ISOLATION'],
 'readiness_change':'unchanged: v3 reveals a hard-vs-soft conditioning tradeoff; AS/C3 remain blocked and no candidate residual exists.'}
Path('results/withheld_v3_local_c5_soft2_iteration199.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
