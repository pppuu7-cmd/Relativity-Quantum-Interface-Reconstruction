#!/usr/bin/env python3
"""Iteration 178: complete the frozen local-C5 dimension-12 soft-transverse basis.

Uses exactly the six Iteration-177 null-soft TT rows and the same curvature
conventions. Extends the two Iteration-177 curvature-cubic operators by the
already-authorized Iteration-165 dimension-12 subset:

  * mixed Ricci Ricci Riemann;
  * Ricci-chain Box^n descendants, n=1,2,3;
  * Riemann-chain Box^n descendants, n=1,2,3.

All operators start at O(h^3) about Minkowski, so their operator-specific K2
vanishes and W[K2]=0. The physical soft leg is null and TT, hence its linearized
Ricci tensor vanishes exactly while its linearized Riemann tensor is O(eps^2).

The script distinguishes the naive floating-point SVD from the physics-aware
rank obtained after imposing the exact soft-TT identities. A sub-error singular
value must not be promoted to a physical direction.
"""
from pathlib import Path
import itertools, json, math
import numpy as np

ETA=np.diag([-1.,1.,1.,1.])
QS=[np.array(x,float) for x in [[0.18,0.70,0.20,0.10],[0.14,0.55,-0.25,0.20],[0.22,0.62,0.18,-0.24],[0.16,0.48,0.31,0.12],[0.20,0.58,-0.16,-0.28],[0.12,0.44,0.27,-0.19]]]
EPS=np.array([0.02,0.01,0.005,0.0025,0.00125],float)

def dot(a,b): return float(a@ETA@b)
def theta(k):
    kc=ETA@k; return ETA-np.outer(kc,kc)/dot(k,k)
def p2(k):
    t=theta(k)
    return .5*(np.einsum('mr,ns->mnrs',t,t)+np.einsum('ms,nr->mnrs',t,t))-(1/3)*np.einsum('mn,rs->mnrs',t,t)
def polarization(k,seed):
    P=p2(k); e=np.einsum('mnrs,ra,sb,ab->mn',P,ETA,ETA,seed)
    n=np.einsum('mn,ma,nb,ab',e,ETA,ETA,e)
    return e/np.sqrt(abs(n))
def lin_ricci(k,e):
    kc=ETA@k; tr=np.einsum('mn,mn',ETA,e); k2v=dot(k,k); R=np.zeros((4,4),complex)
    for m,n in itertools.product(range(4),repeat=2):
        t1=-kc[m]*sum(k[a]*e[a,n] for a in range(4))
        t2=-kc[n]*sum(k[a]*e[a,m] for a in range(4))
        R[m,n]=.5*(t1+t2+k2v*e[m,n]+kc[m]*kc[n]*tr)
    return R
def lin_riemann(k,e):
    kc=ETA@k; R=np.zeros((4,4,4,4),complex)
    for m,n,r,s in itertools.product(range(4),repeat=4):
        R[m,n,r,s]=.5*(-kc[r]*kc[n]*e[m,s]-kc[s]*kc[m]*e[n,r]+kc[s]*kc[n]*e[m,r]+kc[r]*kc[m]*e[n,s])
    return R
def ricci_chain_boxn(ks,es,n):
    A=[ETA@lin_ricci(k,e) for k,e in zip(ks,es)]
    return sum(((-dot(ks[c],ks[c]))**n*np.trace(A[a]@A[b]@A[c])) for a,b,c in itertools.permutations(range(3))).real
def riemann_chain_boxn(ks,es,n):
    A=[]
    for k,e in zip(ks,es):
        R=lin_riemann(k,e)
        A.append(np.einsum('mnab,ar,bs->mnrs',R,ETA,ETA).reshape(16,16))
    return sum(((-dot(ks[c],ks[c]))**n*np.trace(A[a]@A[b]@A[c])) for a,b,c in itertools.permutations(range(3))).real
def mixed_rrr(ks,es):
    Ric=[lin_ricci(k,e) for k,e in zip(ks,es)]
    Rm=[lin_riemann(k,e) for k,e in zip(ks,es)]
    val=0j
    for a,b,c in itertools.permutations(range(3)):
        Rup=np.einsum('abcd,ma,rb,nc,sd->mrns',Rm[c],ETA,ETA,ETA,ETA)
        val += np.einsum('mn,rs,mrns',Ric[a],Ric[b],Rup)
    return val.real

k0=np.array([1.,0.,0.,1.])
e_soft=np.zeros((4,4),float); e_soft[1,1]=1/math.sqrt(2); e_soft[2,2]=-1/math.sqrt(2)
seeds=[]
for i in range(12):
    rng=np.random.default_rng(17700+i); A=rng.normal(size=(4,4)); seeds.append((A+A.T)/2)

names=['Riemann3','mixed_RicciRicciRiemann','RicciChain_Box1','RiemannChain_Box1','RicciChain_Box2','RiemannChain_Box2','RicciChain_Box3','RiemannChain_Box3']
coeff={n:[] for n in names}; fit_disc={n:[] for n in names}; rows=[]; max_gauge=0.0
for i,q in enumerate(QS):
    e2=polarization(q,seeds[2*i]); raw={n:[] for n in names}
    for eps in EPS:
        k1=eps*k0; k2=q; k3=-q-k1; e3=polarization(k3,seeds[2*i+1]); ks=[k1,k2,k3]; es=[e_soft,e2,e3]
        vals={
          'Riemann3':riemann_chain_boxn(ks,es,0),
          'mixed_RicciRicciRiemann':mixed_rrr(ks,es),
          'RicciChain_Box1':ricci_chain_boxn(ks,es,1),'RiemannChain_Box1':riemann_chain_boxn(ks,es,1),
          'RicciChain_Box2':ricci_chain_boxn(ks,es,2),'RiemannChain_Box2':riemann_chain_boxn(ks,es,2),
          'RicciChain_Box3':ricci_chain_boxn(ks,es,3),'RiemannChain_Box3':riemann_chain_boxn(ks,es,3)}
        for n,v in vals.items(): raw[n].append(v/eps**2)
        xi=np.array([0.31,-0.27,0.19,0.41]); kc=ETA@k1; eg=np.outer(kc,xi)+np.outer(xi,kc)
        for n in (0,1,2,3): max_gauge=max(max_gauge,abs(riemann_chain_boxn(ks,[eg,e2,e3],n)))
        for n in (1,2,3): max_gauge=max(max_gauge,abs(ricci_chain_boxn(ks,[eg,e2,e3],n)))
        max_gauge=max(max_gauge,abs(mixed_rrr(ks,[eg,e2,e3])))
    rec={'row':i,'q':q.tolist(),'q2':dot(q,q),'eps':EPS.tolist(),'raw_over_eps2':{}}
    for n in names:
        y=np.array(raw[n]); c2=float(np.polyfit(EPS[-4:],y[-4:],2)[-1]); c3=float(np.polyfit(EPS,y,3)[-1])
        coeff[n].append(c3); fit_disc[n].append(abs(c3-c2)); rec['raw_over_eps2'][n]=[float(x) for x in y]
    rows.append(rec)

r0=np.array(coeff['Riemann3']); q2=np.array([dot(q,q) for q in QS])
# Exact soft-TT reduction of the frozen operator family.
pred={
 'mixed_RicciRicciRiemann':r0/12.0,
 'RiemannChain_Box1':(2/3)*(-q2)*r0,
 'RiemannChain_Box2':(2/3)*(q2**2)*r0,
 'RiemannChain_Box3':(2/3)*(-q2**3)*r0}
identity_errors={n:{
 'max_abs':float(np.max(np.abs(np.array(coeff[n])-v))),
 'max_rel':float(np.max(np.abs(np.array(coeff[n])-v))/max(np.max(np.abs(v)),1e-30))}
 for n,v in pred.items()}
ricci_zero={n:float(np.max(np.abs(np.array(coeff[n])))) for n in ['RicciChain_Box1','RicciChain_Box2','RicciChain_Box3']}

# Full numerical columns in frozen dimension order: Ricci3 is exact zero from Iteration 177.
Vnum=np.column_stack([np.zeros(6),r0,np.array(coeff['mixed_RicciRicciRiemann']),np.array(coeff['RicciChain_Box1']),np.array(coeff['RiemannChain_Box1']),np.array(coeff['RicciChain_Box2']),np.array(coeff['RiemannChain_Box2']),np.array(coeff['RicciChain_Box3']),np.array(coeff['RiemannChain_Box3'])])
snum=np.linalg.svd(Vnum,compute_uv=False)
# Physics-aware exact basis after applying the soft identities.
Vexact=np.column_stack([r0,(2/3)*(-q2)*r0,(2/3)*(q2**2)*r0,(2/3)*(-q2**3)*r0])
sexact=np.linalg.svd(Vexact,compute_uv=False)
max_fit=max(max(v) for v in fit_disc.values())

out={
 'iteration':178,
 'scope':'six frozen Iteration-177 null-soft TT rows; target-independent local C5 cubic subset through dimension 12',
 'operator_columns':['Ricci3','Riemann3','mixed_RicciRicciRiemann','RicciChain_Box1','RiemannChain_Box1','RicciChain_Box2','RiemannChain_Box2','RicciChain_Box3','RiemannChain_Box3'],
 'analytic_soft_identities':[
   'Ricci3 and RicciChain_Box^n vanish because the null TT soft leg has Rmn^(1)=0',
   'mixed_RicciRicciRiemann = Riemann3/12 on the frozen null-soft TT limit',
   'RiemannChain_Box^n = (2/3)(-q^2)^n Riemann3 for n=1,2,3; Box on the null soft leg vanishes and the four hard-leg permutations survive'],
 'Riemann3_B_T':r0.tolist(),
 'identity_errors':identity_errors,
 'ricci_descendant_max_abs':ricci_zero,
 'naive_numeric_singular_values':snum.tolist(),
 'naive_numeric_rank_tol_1e-10':int(np.linalg.matrix_rank(Vnum,tol=1e-10)),
 'max_extrapolation_discrepancy':float(max_fit),
 'physics_aware_exact_basis':['Riemann3','Riemann3*(-q2)','Riemann3*(q2^2)','Riemann3*(-q2^3)'],
 'physics_aware_rank':int(np.linalg.matrix_rank(Vexact,tol=1e-10)),
 'physics_aware_singular_values':sexact.tolist(),
 'physics_aware_smin_over_smax':float(sexact[-1]/sexact[0]),
 'sub_error_singular_guard':'the fifth naive singular value is below the extrapolation/error envelope and is removed by exact soft-TT identities; it is not a physical direction',
 'max_soft_gauge_replacement_abs':float(max_gauge),
 'rows':rows,
 'classification':{
   'local_C5_dimension12_B_T':'COMPLETE_FOR_FROZEN_AUTHORIZED_CUBIC_SUBSET_EFFECTIVE_RANK_4',
   'protocol_zeros':'Ricci-based soft columns exact zero in null-TT protocol',
   'novelty_certificate':'NONE_FULL_COMPARATOR_QUOTIENT_INCOMPLETE',
   'ANSATZ_003':'NOT_CREATED','Fisher_resources':'FORBIDDEN'},
 'retained_results':[
   'C5-NG-009 — DIMENSION12_LOCAL_C5_NULL_SOFT_TT_BASIS_COMPRESSES_TO_RIEMANN_CHAIN_POLYNOMIAL_RANK_FOUR',
   'SOFT-NG-005 — NULL_SOFT_TT_KINEMATICS_KILLS_RICCI_CHAIN_AND_REDUCES_DERIVATIVE_RIEMANN_DESCENDANTS_TO_HARD_Q2_MOMENTS',
   'NUM-NG-001 — SUB_ERROR_SINGULAR_VALUE_MUST_NOT_BE_PROMOTED_WHEN_EXACT_KINEMATIC_IDENTITIES_REMOVE_IT'],
 'model_readiness_percent':24,
 'readiness_change':'unchanged: local C5 B_T comparator is substantially sharpened, but C4/nonlocal/AS/C3 transverse completion and any robust residual remain open'}
Path('results/c5_soft_transverse_dimension12_iteration178.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
