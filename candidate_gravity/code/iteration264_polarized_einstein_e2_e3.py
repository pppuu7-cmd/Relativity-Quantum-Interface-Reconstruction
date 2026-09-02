#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 264.

Construct physical multilinear Einstein-EOM coefficients E2[x,y] and
E3[s,a,b] by centered mixed derivatives of the exact Einstein tensor for
three distinct TT Fourier perturbations on Minkowski space.

This is a scoped same-parent vertex certificate. It is not a C5 comparator
coordinate and not a Candidate Gravity residual.
"""
import itertools, json
import numpy as np

ETA=np.diag([-1.,1.,1.,1.])
K_S=np.array([1.,0.,0.,1.])
E_S=np.zeros((4,4)); E_S[1,1]=1/np.sqrt(2); E_S[2,2]=-1/np.sqrt(2)

def tt_pol(k,seed):
    q=k[1:]; u=np.array(seed,dtype=float)
    u-=q*np.dot(u,q)/np.dot(q,q); u/=np.linalg.norm(u)
    v=np.cross(q,u); v/=np.linalg.norm(v)
    e=np.zeros((4,4)); e[1:,1:]=(np.outer(u,u)-np.outer(v,v))/np.sqrt(2)
    return e

K_A=np.array([.25,.6,.3,.15]); E_A=tt_pol(K_A,[.2,-.5,.7])
K_B=np.array([-.15,.2,.55,-.35]); E_B=tt_pol(K_B,[.8,.1,.3])
MODES=[(K_S,E_S),(K_A,E_A),(K_B,E_B)]

def einstein(amps,modes):
    g=ETA.astype(complex).copy()
    for a,(_,e) in zip(amps,modes): g+=a*e
    gi=np.linalg.inv(g); covk=[ETA@k for k,_ in modes]
    dg=np.zeros((4,4,4),complex); ddg=np.zeros((4,4,4,4),complex)
    for mu in range(4):
        for a,(_,e),kc in zip(amps,modes,covk): dg[mu]+=1j*kc[mu]*a*e
        for nu in range(4):
            for a,(_,e),kc in zip(amps,modes,covk): ddg[mu,nu]+=-kc[mu]*kc[nu]*a*e
    dgi=np.array([-gi@dg[l]@gi for l in range(4)])
    gam=np.zeros((4,4,4),complex); dgam=np.zeros((4,4,4,4),complex)
    for r,m,n in itertools.product(range(4),repeat=3):
        A=[dg[m,s,n]+dg[n,s,m]-dg[s,m,n] for s in range(4)]
        gam[r,m,n]=.5*sum(gi[r,s]*A[s] for s in range(4))
        for l in range(4):
            dgam[l,r,m,n]=.5*sum(dgi[l,r,s]*A[s]+gi[r,s]*(ddg[l,m,s,n]+ddg[l,n,s,m]-ddg[l,s,m,n]) for s in range(4))
    ric=np.zeros((4,4),complex)
    for m,n in itertools.product(range(4),repeat=2):
        z=0j
        for r in range(4):
            z+=dgam[r,r,m,n]-dgam[n,r,m,r]
            for l in range(4): z+=gam[r,r,l]*gam[l,m,n]-gam[r,n,l]*gam[l,m,r]
        ric[m,n]=z
    return ric-.5*g*np.sum(gi*ric)

def mixed(modes,h):
    n=len(modes); out=np.zeros((4,4),complex)
    for sig in itertools.product([-1,1],repeat=n):
        out+=np.prod(sig)*einstein([s*h for s in sig],modes)
    return out/(2*h)**n

def first(mode,h): return (einstein([h],[mode])-einstein([-h],[mode]))/(2*h)

steps=[1e-2,3e-3,1e-3,3e-4]
rows=[]
for h in steps:
    e2sa=mixed([MODES[0],MODES[1]],h); e2sb=mixed([MODES[0],MODES[2]],h)
    e2ab=mixed([MODES[1],MODES[2]],h); e3=mixed(MODES,h)
    perm=max(np.max(np.abs(mixed([MODES[i] for i in p],h)-e3)) for p in itertools.permutations(range(3)))
    rows.append({"step":h,"e2_sa_fro":float(np.linalg.norm(e2sa)),"e2_sa_max":float(np.max(np.abs(e2sa))),"e2_sb_fro":float(np.linalg.norm(e2sb)),"e2_sb_max":float(np.max(np.abs(e2sb))),"e2_ab_fro":float(np.linalg.norm(e2ab)),"e2_ab_max":float(np.max(np.abs(e2ab))),"e3_sab_fro":float(np.linalg.norm(e3)),"e3_sab_max":float(np.max(np.abs(e3))),"e3_leg_permutation_residual":float(perm),"e3_output_symmetry_residual":float(np.max(np.abs(e3-e3.T)))})

h=3e-4; e1s=first(MODES[0],h)
result={"iteration":264,"model_readiness_percent":24,"soft_k2":float(K_S@ETA@K_S),"hard_a_k2":float(K_A@ETA@K_A),"hard_b_k2":float(K_B@ETA@K_B),"soft_E1_fro":float(np.linalg.norm(e1s)),"soft_E1_max":float(np.max(np.abs(e1s))),"rows":rows,"classification":"PASS_SCOPED_POLARIZED_EINSTEIN_E2_E3_NONZERO_AND_SYMMETRIC","guardrail":"DO_NOT_ZERO_E2_OR_E3_FROM_E1_SOFT_ZERO","candidate_residual":False}
assert abs(result["soft_k2"])<1e-14
assert result["soft_E1_max"]<1e-12
assert rows[-1]["e2_sa_fro"]>.7 and rows[-1]["e3_sab_fro"]>.5
assert rows[-1]["e3_leg_permutation_residual"]<1e-7
assert rows[-1]["e3_output_symmetry_residual"]<1e-7
print(json.dumps(result,indent=2,sort_keys=True))
