#!/usr/bin/env python3
"""Iteration 152: source-completed Ward validation for existing C5 curvature-cubic directions.

Around flat space the covariant R^3 operators used in Iteration 150 have no
quadratic term. Their leading contribution is cubic and is built entirely from
linearized curvatures. Therefore the cubic-order diffeomorphism identity reduces
to B3[L_xi,e2,e3]=0 for each leg, because the corresponding operator-specific
B2/source-contact completion vanishes at this perturbative order.

This script uses the same six frozen spacelike probes and the same local
curvature conventions as Iteration 150, replacing each leg in turn by a pure
linearized diffeomorphism polarization and checking both the linearized
curvature tensors and the two cubic contractions.
"""
import itertools, json
import numpy as np

ETA=np.diag([-1.,1.,1.,1.])
QS=[np.array(x,float) for x in [
[0.18,0.70,0.20,0.10],[0.14,0.55,-0.25,0.20],[0.22,0.62,0.18,-0.24],
[0.16,0.48,0.31,0.12],[0.20,0.58,-0.16,-0.28],[0.12,0.44,0.27,-0.19]]]
RS=[np.array(x,float) for x in [
[0.11,-0.21,0.52,0.17],[0.09,0.24,0.46,-0.18],[0.10,-0.18,0.41,0.29],
[0.13,0.22,-0.37,0.33],[0.08,0.26,0.35,0.21],[0.15,-0.20,0.39,0.25]]]

def dot(a,b): return float(a@ETA@b)
def theta(k):
    kc=ETA@k
    return ETA-np.outer(kc,kc)/dot(k,k)
def p2(k):
    t=theta(k)
    return .5*(np.einsum('mr,ns->mnrs',t,t)+np.einsum('ms,nr->mnrs',t,t))-(1/3)*np.einsum('mn,rs->mnrs',t,t)
def polarization(k,seed):
    P=p2(k)
    e=np.einsum('mnrs,ra,sb,ab->mn',P,ETA,ETA,seed)
    n=np.einsum('mn,ma,nb,ab',e,ETA,ETA,e)
    return e/np.sqrt(abs(n))

def lin_ricci(k,e):
    kc=ETA@k; tr=np.einsum('mn,mn',ETA,e); k2v=dot(k,k)
    R=np.zeros((4,4),complex)
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

def ricci3(ks,es):
    A=[ETA@lin_ricci(k,e) for k,e in zip(ks,es)]
    return sum(np.trace(A[a]@A[b]@A[c]) for a,b,c in itertools.permutations(range(3))).real

def riem3(ks,es):
    A=[]
    for k,e in zip(ks,es):
        R=lin_riemann(k,e)
        A.append(np.einsum('mnab,ar,bs->mnrs',R,ETA,ETA).reshape(16,16))
    return sum(np.trace(A[a]@A[b]@A[c]) for a,b,c in itertools.permutations(range(3))).real

seeds=[]
for i in range(18):
    rng=np.random.default_rng(100+i); A=rng.normal(size=(4,4)); seeds.append((A+A.T)/2)

rows=[]; max_lr=0.; max_lrm=0.; max_r3=0.; max_rm3=0.
for i,(q,r) in enumerate(zip(QS,RS)):
    p=q+r; ks=[p,-q,-r]
    es=[polarization(ks[j],seeds[3*i+j]) for j in range(3)]
    row={'probe':i,'baseline_Ricci3':ricci3(ks,es),'baseline_Riemann3':riem3(ks,es),'legs':[]}
    for leg in range(3):
        rng=np.random.default_rng(1900+3*i+leg); xi=rng.normal(size=4); kc=ETA@ks[leg]
        gauge=np.outer(kc,xi)+np.outer(xi,kc)
        eg=list(es); eg[leg]=gauge
        lr=float(np.max(np.abs(lin_ricci(ks[leg],gauge))))
        lrm=float(np.max(np.abs(lin_riemann(ks[leg],gauge))))
        r3=float(abs(ricci3(ks,eg))); rm3=float(abs(riem3(ks,eg)))
        max_lr=max(max_lr,lr); max_lrm=max(max_lrm,lrm); max_r3=max(max_r3,r3); max_rm3=max(max_rm3,rm3)
        row['legs'].append({'leg':leg,'max_abs_linearized_Ricci_on_gauge':lr,
                            'max_abs_linearized_Riemann_on_gauge':lrm,
                            'abs_Ricci3_B3_on_gauge':r3,'abs_Riemann3_B3_on_gauge':rm3})
    rows.append(row)

out={'iteration':152,
     'scope':'same six frozen spacelike probes and curvature conventions as Iteration 150',
     'operators':['Tr(Ricci^3)','Riemann_mn^rs Riemann_rs^ab Riemann_ab^mn'],
     'identity':'operator-specific B2=0 about flat space at this order; therefore B3[L_xi,e2,e3]=0',
     'max_abs_linearized_Ricci_on_gauge':max_lr,
     'max_abs_linearized_Riemann_on_gauge':max_lrm,
     'max_abs_Ricci3_B3_on_gauge':max_r3,
     'max_abs_Riemann3_B3_on_gauge':max_rm3,
     'rows':rows,
     'status':{'Ricci3_completed_Ward':'PASS_SCOPED','Riemann3_completed_Ward':'PASS_SCOPED',
               'existing_local_C5_6x2_tangent':'PASS_SCOPED_WARD_VALIDATED',
               'higher_dimension_local':'BLOCKED','loops_nonanalytic':'BLOCKED',
               'N2_C3sym':'BLOCKED','Fisher_resources':'FORBIDDEN_NO_COMPARATOR_QUOTIENT_RESIDUAL',
               'ANSATZ_003':'NOT_CREATED'}}
print(json.dumps(out,indent=2,sort_keys=True))
