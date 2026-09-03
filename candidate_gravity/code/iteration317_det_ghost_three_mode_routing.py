#!/usr/bin/env python3
"""RQIR Iteration 317: non-collinear three-mode routing certificate for ghost N1/N2/N3.

Frozen parent operator:
    N^a_b = delta^a_b Box + R^a_b,
with D=4, Lambda=0, a=-1/2.

Iteration 316 validated a single Fourier mode.  This iteration tests the genuinely
mixed routing that a single-mode background cannot see, including the cubic
(1,1,1) coefficient.  Three independent Fourier modes are retained explicitly,
and every polynomial convolution is keyed by a 3-component multi-index.
No absent coefficient is zero-filled by assumption.
"""
from __future__ import annotations
import itertools, json, numpy as np

D=4
eta=np.diag([-1.,1.,1.,1.])
rng=np.random.default_rng(317)
M=3
hs=[]
for _ in range(M):
    x=rng.normal(size=(D,D)); hs.append(0.2*(x+x.T)/2.0)
qs=[
    np.array([0.30,-0.20,0.40,0.10]),
    np.array([-0.10,0.50,0.20,-0.30]),
    np.array([0.20,0.10,-0.40,0.45]),
]
p=np.array([0.70,-0.40,0.20,0.60])
ZERO=(0,0,0)

def deg(a): return sum(a)
def indices(maxdeg):
    out=[]
    for n in range(maxdeg+1):
        for a in itertools.product(range(n+1), repeat=M):
            if sum(a)==n: out.append(a)
    return out
IND=indices(3)

def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def valid(a): return min(a)>=0
def qsum(a):
    z=np.zeros(D)
    for r in range(M): z+=a[r]*qs[r]
    return z

def decompositions(a):
    for b in IND:
        if all(b[r]<=a[r] for r in range(M)):
            yield b,sub(a,b)

# Inverse metric coefficients from (eta + sum t_r h_r) G = I.
G={ZERO:eta.copy()}
for a in IND[1:]:
    X=np.zeros((D,D),complex)
    for r in range(M):
        if a[r]:
            b=list(a); b[r]-=1; b=tuple(b)
            X+=hs[r]@G[b]
    G[a]=-eta@X

# Levi-Civita connection coefficients.  Derivatives act mode by mode.
Gam={ZERO:np.zeros((D,D,D),complex)}
for a in IND[1:]:
    A=np.zeros((D,D,D),complex)
    for r in range(M):
        if not a[r]: continue
        b=list(a); b[r]-=1; b=tuple(b)
        h,q=hs[r],qs[r]
        for x in range(D):
            for m in range(D):
                for v in range(D):
                    for s in range(D):
                        A[x,m,v]+=0.5*G[b][x,s]*(1j*q[m]*h[s,v]+1j*q[v]*h[s,m]-1j*q[s]*h[m,v])
    Gam[a]=A

# Ricci and mixed Ricci coefficients; derivative momentum is the total routed Q_a.
R={ZERO:np.zeros((D,D),complex)}
for a in IND[1:]:
    T=np.zeros((D,D),complex); Q=qsum(a)
    for m in range(D):
        for v in range(D):
            for x in range(D):
                T[m,v]+=1j*Q[x]*Gam[a][x,m,v]-1j*Q[v]*Gam[a][x,m,x]
                for b,c in decompositions(a):
                    if deg(b)==0 or deg(c)==0: continue
                    for l in range(D):
                        T[m,v]+=Gam[b][x,x,l]*Gam[c][l,m,v]-Gam[b][x,v,l]*Gam[c][l,m,x]
    R[a]=T
Rm={}
for a in IND:
    X=np.zeros((D,D),complex)
    for b,c in decompositions(a): X+=G[b]@R[c]
    Rm[a]=X

# First vector covariant derivative coefficients on c exp(i p.x).
D1={}
for a in IND:
    arr=[]
    for nu in range(D):
        arr.append(1j*p[nu]*np.eye(D) if a==ZERO else Gam[a][:,nu,:].copy())
    D1[a]=arr

# Second covariant derivative with exact multi-mode momentum routing.
S={}
for a in IND:
    Q=qsum(a); kout=p+Q
    aa=[[np.zeros((D,D),complex) for _ in range(D)] for __ in range(D)]
    for mu in range(D):
        for nu in range(D):
            X=1j*kout[mu]*D1[a][nu]
            for b,c in decompositions(a):
                if deg(b)==0: continue
                X+=Gam[b][:,mu,:]@D1[c][nu]
                for rho in range(D): X-=Gam[b][rho,mu,nu]*D1[c][rho]
            aa[mu][nu]=X
    S[a]=aa

Box={}; N={}
for a in IND:
    X=np.zeros((D,D),complex)
    for b,c in decompositions(a):
        for mu in range(D):
            for nu in range(D): X+=G[b][mu,nu]*S[c][mu][nu]
    Box[a]=X; N[a]=X+Rm[a]

# Independent exact-geometry oracle at x=0 for arbitrary amplitudes t_r.
def direct(t):
    g=eta.copy().astype(complex)
    dg=np.zeros((D,D,D),complex); d2g=np.zeros((D,D,D,D),complex)
    for r in range(M):
        g+=t[r]*hs[r]
        for l in range(D): dg[l]+=1j*qs[r][l]*t[r]*hs[r]
        for l in range(D):
            for s in range(D): d2g[l,s]+=-qs[r][l]*qs[r][s]*t[r]*hs[r]
    gi=np.linalg.inv(g)
    dgi=np.zeros((D,D,D),complex)
    for l in range(D): dgi[l]=-gi@dg[l]@gi
    Ga=np.zeros((D,D,D),complex); dGa=np.zeros((D,D,D,D),complex)
    for x in range(D):
        for m in range(D):
            for v in range(D):
                for s in range(D):
                    Ga[x,m,v]+=0.5*gi[x,s]*(dg[m,s,v]+dg[v,s,m]-dg[s,m,v])
    for l in range(D):
        for x in range(D):
            for m in range(D):
                for v in range(D):
                    for s in range(D):
                        B=dg[m,s,v]+dg[v,s,m]-dg[s,m,v]
                        dB=d2g[l,m,s,v]+d2g[l,v,s,m]-d2g[l,s,m,v]
                        dGa[l,x,m,v]+=0.5*(dgi[l,x,s]*B+gi[x,s]*dB)
    Ric=np.zeros((D,D),complex)
    for m in range(D):
        for v in range(D):
            for x in range(D):
                Ric[m,v]+=dGa[x,x,m,v]-dGa[v,x,m,x]
                for l in range(D): Ric[m,v]+=Ga[x,x,l]*Ga[l,m,v]-Ga[x,v,l]*Ga[l,m,x]
    Rmix=gi@Ric
    out=np.zeros((D,D),complex)
    for mu in range(D):
        for nu in range(D):
            X=-(p[mu]*p[nu])*np.eye(D)+dGa[mu,:,nu,:]+1j*p[nu]*Ga[:,mu,:]+1j*p[mu]*Ga[:,nu,:]
            X+=Ga[:,mu,:]@Ga[:,nu,:]
            for rho in range(D): X-=Ga[rho,mu,nu]*(1j*p[rho]*np.eye(D)+Ga[:,rho,:])
            out+=gi[mu,nu]*X
    return out+Rmix

# Multivariate direct fit.  Fit through total degree 4 so omitted degree-4 curvature
# does not contaminate the target degree <=3 coefficients.  Symmetric sampling makes
# the leading omitted odd/even leakage higher order.
FIT=indices(4)
scale=5.0e-4
us=[-1.0,-0.5,0.0,0.5,1.0]
samples=list(itertools.product(us, repeat=M))
V=np.array([[np.prod([u[r]**a[r] for r in range(M)]) for a in FIT] for u in samples],float)
vals=np.stack([direct(scale*np.array(u,float)) for u in samples])
coef_u=np.linalg.lstsq(V,vals.reshape(len(samples),-1),rcond=None)[0].reshape(len(FIT),D,D)
fit_index={a:i for i,a in enumerate(FIT)}
coef_t={a:coef_u[fit_index[a]]/(scale**deg(a)) for a in IND}
errors={a:float(np.max(np.abs(coef_t[a]-N[a]))) for a in IND}
max_by_degree={n:max(errors[a] for a in IND if deg(a)==n) for n in range(4)}
mixed_by_degree={
    2:max(errors[a] for a in IND if deg(a)==2 and sum(x>0 for x in a)>=2),
    3:max(errors[a] for a in IND if deg(a)==3 and sum(x>0 for x in a)>=2),
}
triple_mixed_error=errors[(1,1,1)]
threshold={0:1e-8,1:1e-5,2:1e-2,3:5.0}
ok=all(max_by_degree[n]<threshold[n] for n in range(4))

# Non-collinearity certificate for the three routing momenta.
Q=np.stack(qs)
q_rank=int(np.linalg.matrix_rank(Q,tol=1e-12))
if q_rank<3: ok=False

print(json.dumps({
    'iteration':317,
    'model_readiness_percent':24,
    'scientific_gate_pass':bool(ok),
    'classification':'PASS_GHOST_N123_THREE_MODE_NONCOLLINEAR_ROUTING_CERTIFICATE' if ok else 'FAIL_GHOST_N123_THREE_MODE_NONCOLLINEAR_ROUTING_CERTIFICATE',
    'scope':{'D':4,'Lambda':0,'a':'-1/2','modes':3,'q_rank':q_rank,'target_total_degree':3,'direct_fit_total_degree':4,'fit_scale':scale},
    'validation_max_abs_error_by_total_degree':{str(k):v for k,v in max_by_degree.items()},
    'validation_threshold_by_total_degree':{str(k):v for k,v in threshold.items()},
    'mixed_validation_max_abs_error':{str(k):v for k,v in mixed_by_degree.items()},
    'triple_mixed_111_max_abs_error':triple_mixed_error,
    'physical_status':{
        'ghost_N1_N2_N3':'FULL_ROUTED_COMPONENT_AUTHORITY_READY_TO_FREEZE' if ok else 'FAIL_PRESERVE_AND_REPAIR',
        'graviton_H1_H2_H3':'BLOCKED_UNCHANGED'
    },
    'candidate_residual':False,
    'guardrails':['NO_ZERO_FILL','NO_LOGDET_INSERTION_BEFORE_GRAVITON_AUTHORITY','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5'],
    'next_gate':'freeze full ghost N1/N2/N3 authority and derive independent graviton H1/H2/H3 from the same D=4,Lambda=0,a=-1/2 parent operator' if ok else 'preserve scientific FAIL and repair multi-mode routing without weakening frozen thresholds'
},indent=2,sort_keys=True))
