#!/usr/bin/env python3
"""Iteration 177: action-level C5 Ward-subtracted soft-transverse columns.

Reuses the covariant parent operators of Iteration 150, not their finite-response
numbers. The soft leg is the physical null TT graviton fixed by Iteration 175:
k_soft = eps*(1,0,0,1), e_soft = plus polarization. Six target-independent
hard rows reuse the six Iteration-150 q momenta. Exact momentum conservation is
k1+k2+k3=0 with k2=q_i and k3=-q_i-k1.

Both curvature-cubic operators start at cubic order around Minkowski, so their
quadratic kernel vanishes and W[K2]=0 for these directions. Their cubic terms
are products of linearized curvatures and are separately gauge invariant.
For a null TT soft graviton R^(1)_mn=0 analytically, hence Tr(Ricci^3) has an
exact zero B_T column in this protocol; cyclic Riemann^3 is extrapolated from
the eps^2 coefficient.
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
    t=theta(k); return .5*(np.einsum('mr,ns->mnrs',t,t)+np.einsum('ms,nr->mnrs',t,t))-(1/3)*np.einsum('mn,rs->mnrs',t,t)
def polarization(k,seed):
    P=p2(k); e=np.einsum('mnrs,ra,sb,ab->mn',P,ETA,ETA,seed); n=np.einsum('mn,ma,nb,ab',e,ETA,ETA,e); return e/np.sqrt(abs(n))
def lin_ricci(k,e):
    kc=ETA@k; tr=np.einsum('mn,mn',ETA,e); k2v=dot(k,k); R=np.zeros((4,4),complex)
    for m,n in itertools.product(range(4),repeat=2):
        t1=-kc[m]*sum(k[a]*e[a,n] for a in range(4)); t2=-kc[n]*sum(k[a]*e[a,m] for a in range(4)); R[m,n]=.5*(t1+t2+k2v*e[m,n]+kc[m]*kc[n]*tr)
    return R
def lin_riemann(k,e):
    kc=ETA@k; R=np.zeros((4,4,4,4),complex)
    for m,n,r,s in itertools.product(range(4),repeat=4):
        R[m,n,r,s]=.5*(-kc[r]*kc[n]*e[m,s]-kc[s]*kc[m]*e[n,r]+kc[s]*kc[n]*e[m,r]+kc[r]*kc[m]*e[n,s])
    return R
def ricci3(ks,es):
    A=[ETA@lin_ricci(k,e) for k,e in zip(ks,es)]; return sum(np.trace(A[a]@A[b]@A[c]) for a,b,c in itertools.permutations(range(3))).real
def riem3(ks,es):
    A=[]
    for k,e in zip(ks,es):
        R=lin_riemann(k,e); A.append(np.einsum('mnab,ar,bs->mnrs',R,ETA,ETA).reshape(16,16))
    return sum(np.trace(A[a]@A[b]@A[c]) for a,b,c in itertools.permutations(range(3))).real
k0=np.array([1.,0.,0.,1.]); e_soft=np.zeros((4,4),float); e_soft[1,1]=1/math.sqrt(2); e_soft[2,2]=-1/math.sqrt(2)
soft_ricci_norm=float(np.linalg.norm(lin_ricci(k0,e_soft))); soft_riemann_norm=float(np.linalg.norm(lin_riemann(k0,e_soft)))
seeds=[]
for i in range(12):
    rng=np.random.default_rng(17700+i); A=rng.normal(size=(4,4)); seeds.append((A+A.T)/2)
rows=[]; riem_coeff=[]; fit_discrep=[]; max_gauge=0.0
for i,q in enumerate(QS):
    e2=polarization(q,seeds[2*i]); y_ricci=[]; y_riem=[]
    for eps in EPS:
        k1=eps*k0; k2=q; k3=-q-k1; e3=polarization(k3,seeds[2*i+1]); ks=[k1,k2,k3]; es=[e_soft,e2,e3]
        y_ricci.append(ricci3(ks,es)/(eps**2)); y_riem.append(riem3(ks,es)/(eps**2))
        xi=np.array([0.31,-0.27,0.19,0.41]); kc=ETA@k1; eg=np.outer(kc,xi)+np.outer(xi,kc)
        max_gauge=max(max_gauge,abs(ricci3(ks,[eg,e2,e3])),abs(riem3(ks,[eg,e2,e3])))
    c2=float(np.polyfit(EPS[-4:],np.array(y_riem)[-4:],2)[-1]); c3=float(np.polyfit(EPS,np.array(y_riem),3)[-1]); riem_coeff.append(c3); fit_discrep.append(abs(c3-c2))
    rows.append({'row':i,'q':q.tolist(),'eps':EPS.tolist(),'Ricci3_over_eps2_raw':[float(x) for x in y_ricci],'Riemann3_over_eps2_raw':[float(x) for x in y_riem],'Ricci3_B_T':0.0,'Riemann3_B_T':c3,'Riemann3_fit_discrepancy':abs(c3-c2)})
V=np.column_stack([np.zeros(6),np.array(riem_coeff)]); s=np.linalg.svd(V,compute_uv=False); rank=int(np.linalg.matrix_rank(V))
out={'iteration':177,'scope':'six target-independent null-soft TT Ward-subtracted amputated C5 rows','soft_family':'k1=eps*(1,0,0,1), k2=q_i, k3=-q_i-k1','ward_subtraction':'W[K2]=0 exactly for these curvature-cubic directions because their quadratic expansion around Minkowski vanishes','soft_ricci_norm_at_unit_k0':soft_ricci_norm,'soft_riemann_norm_at_unit_k0':soft_riemann_norm,'analytic_result':'For null TT soft leg, Rmn^(1)=0, so Tr(Ricci^3) B_T is exactly zero in this protocol','rows':rows,'V_C5_B_T':V.tolist(),'rank':rank,'n_columns':2,'singular_values':s.tolist(),'nonzero_column_norm':float(np.linalg.norm(riem_coeff)),'max_extrapolation_discrepancy':float(max(fit_discrep)),'max_soft_gauge_replacement_abs':float(max_gauge),'classification':{'Ricci3_B_T':'EXACT_PROTOCOL_ZERO_FROM_NULL_TT_SOFT_RICCI','Riemann3_B_T':'NONZERO_PASS_SCOPED','two_operator_rank':'1/2_REGIME_SPECIFIC_NON_IDENTIFIABILITY','novelty_certificate':'NONE_COMPARATOR_INCOMPLETE','ANSATZ_003':'NOT_CREATED','Fisher_resources':'FORBIDDEN'},'retained_results':['C5-NG-008 — NULL_TT_SOFT_PROTOCOL_ANNIHILATES_RICCI_CUBED_B_T_BUT_NOT_CYCLIC_RIEMANN_CUBED','SOFT-NG-004 — FIRST_ACTION_LEVEL_LOCAL_C5_B_T_BASIS_HAS_RANK_ONE_ON_SIX_NULL_SOFT_TT_ROWS','NG-FUNNEL-037 — PROTOCOL_ZERO_FROM_ONSHELL_SOFT_RICCI_IS_REGIME_SPECIFIC_NOT_OPERATOR_ABSENCE'],'model_readiness_percent':24,'readiness_change':'unchanged: first physical C5 B_T column is instantiated, but fixed C4/nonlocal/AS/C3 transverse quotient and any robust candidate residual are still missing'}
Path('results/c5_soft_transverse_columns_iteration177.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8'); print(json.dumps(out,indent=2,sort_keys=True))
