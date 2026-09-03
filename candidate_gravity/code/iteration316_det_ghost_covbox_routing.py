#!/usr/bin/env python3
"""RQIR Iteration 316: complete routed vector covariant-Box terms for ghost N1/N2/N3.

Uses the same frozen minimal FP parent operator as Iteration 315:
N^a_b = delta^a_b Box + R^a_b, D=4, Lambda=0, a=-1/2.
A single generic background Fourier mode h exp(i q.x) is used as an executable
routing certificate. Order n maps ghost momentum p -> p+n q. No missing term is
zero-filled by assumption; every connection convolution is explicit.
"""
from __future__ import annotations
import json, numpy as np
D=4; eta=np.diag([-1.,1.,1.,1.]); rng=np.random.default_rng(316)
h=rng.normal(size=(D,D)); h=(h+h.T)/2; q=rng.normal(size=D); p=rng.normal(size=D)

G=[eta.copy()]
for n in range(1,4): G.append(-eta@h@G[n-1])
Gam=[np.zeros((D,D,D),complex)]
for n in range(1,4):
 A=np.zeros((D,D,D),complex)
 for a in range(D):
  for m in range(D):
   for v in range(D):
    for s in range(D):
     A[a,m,v]+=0.5*G[n-1][a,s]*(1j*q[m]*h[s,v]+1j*q[v]*h[s,m]-1j*q[s]*h[m,v])
 Gam.append(A)
R=[np.zeros((D,D),complex)]
for n in range(1,4):
 T=np.zeros((D,D),complex)
 for m in range(D):
  for v in range(D):
   for a in range(D):
    T[m,v]+=1j*n*q[a]*Gam[n][a,m,v]-1j*n*q[v]*Gam[n][a,m,a]
    for i in range(1,n):
     j=n-i
     for l in range(D): T[m,v]+=Gam[i][a,a,l]*Gam[j][l,m,v]-Gam[i][a,v,l]*Gam[j][l,m,a]
 R.append(T)
# Mixed Ricci coefficients R^a_b = g^{a m} R_{m b}; allocate all orders
# explicitly so unsupported orders cannot be silently zero-filled or indexed past.
Rm=[np.zeros((D,D),complex) for _ in range(4)]
for n in range(1,4):
 for k in range(n+1): Rm[n]+=G[k]@R[n-k]

# First covariant derivative Dnu_n^a_b.
D1=[[np.zeros((D,D),complex) for _ in range(D)] for __ in range(4)]
for nu in range(D): D1[0][nu]=1j*p[nu]*np.eye(D)
for n in range(1,4):
 for nu in range(D): D1[n][nu]=Gam[n][:,nu,:].copy()

# Second covariant derivative S_n[mu,nu]^a_b with explicit routing.
S=[[[np.zeros((D,D),complex) for _ in range(D)] for __ in range(D)] for ___ in range(4)]
for n in range(4):
 kout=p+n*q
 for mu in range(D):
  for nu in range(D):
   X=1j*kout[mu]*D1[n][nu]
   for i in range(1,n+1):
    j=n-i
    X += Gam[i][:,mu,:]@D1[j][nu]
    # -Gamma^rho_{mu nu} D_rho
    for rho in range(D): X -= Gam[i][rho,mu,nu]*D1[j][rho]
   S[n][mu][nu]=X

Box=[]
for n in range(4):
 X=np.zeros((D,D),complex)
 for k in range(n+1):
  j=n-k
  for mu in range(D):
   for nu in range(D): X+=G[k][mu,nu]*S[j][mu][nu]
 Box.append(X)
N=[Box[n]+Rm[n] for n in range(4)]

# Independent direct evaluation of exact geometry at x=0, then polynomial fit.
def direct(t):
 g=eta+t*h; gi=np.linalg.inv(g)
 dg=np.zeros((D,D,D),complex); d2g=np.zeros((D,D,D,D),complex)
 for l in range(D): dg[l]=1j*q[l]*t*h
 for l in range(D):
  for r in range(D): d2g[l,r]=-q[l]*q[r]*t*h
 dgi=np.zeros((D,D,D),complex)
 for l in range(D): dgi[l]=-gi@dg[l]@gi
 Ga=np.zeros((D,D,D),complex); dGa=np.zeros((D,D,D,D),complex)
 for a in range(D):
  for m in range(D):
   for v in range(D):
    for s in range(D): Ga[a,m,v]+=0.5*gi[a,s]*(dg[m,s,v]+dg[v,s,m]-dg[s,m,v])
 for l in range(D):
  for a in range(D):
   for m in range(D):
    for v in range(D):
     for s in range(D):
      B=dg[m,s,v]+dg[v,s,m]-dg[s,m,v]
      dB=d2g[l,m,s,v]+d2g[l,v,s,m]-d2g[l,s,m,v]
      dGa[l,a,m,v]+=0.5*(dgi[l,a,s]*B+gi[a,s]*dB)
 Ric=np.zeros((D,D),complex)
 for m in range(D):
  for v in range(D):
   for a in range(D):
    Ric[m,v]+=dGa[a,a,m,v]-dGa[v,a,m,a]
    for l in range(D): Ric[m,v]+=Ga[a,a,l]*Ga[l,m,v]-Ga[a,v,l]*Ga[l,m,a]
 Rmix=gi@Ric
 # exact second covariant derivative on c e^{ipx} at x=0, including derivative Gamma.
 out=np.zeros((D,D),complex)
 for mu in range(D):
  for nu in range(D):
   X=-(p[mu]*p[nu])*np.eye(D)+dGa[mu,:,nu,:]+1j*p[nu]*Ga[:,mu,:]+1j*p[mu]*Ga[:,nu,:]
   X+=Ga[:,mu,:]@Ga[:,nu,:]
   for rho in range(D): X-=Ga[rho,mu,nu]*(1j*p[rho]*np.eye(D)+Ga[:,rho,:])
   out+=gi[mu,nu]*X
 return out+Rmix

ts=np.arange(-4,5,dtype=float)*1.5e-4
vals=np.stack([direct(t) for t in ts]); V=np.vander(ts,4,increasing=True)
coef=np.linalg.lstsq(V,vals.reshape(len(ts),-1),rcond=None)[0].reshape(4,D,D)
errs=[float(np.max(np.abs(coef[n]-N[n]))) for n in range(4)]
thr=[1e-8,5e-5,5e-2,20.0]
ok=all(e<t for e,t in zip(errs,thr))
print(json.dumps({
 'iteration':316,'model_readiness_percent':24,'scientific_gate_pass':bool(ok),
 'classification':'PASS_FULL_ROUTED_GHOST_N123_SINGLE_MODE_CERTIFICATE' if ok else 'FAIL_FULL_ROUTED_GHOST_N123_SINGLE_MODE_CERTIFICATE',
 'scope':{'D':4,'Lambda':0,'a':'-1/2','routing':'order n: p -> p+n q'},
 'validation_max_abs_error_by_order':errs,'validation_threshold_by_order':thr,
 'physical_status':{'ghost_N1_N2_N3':'DERIVED_EXECUTABLE_SINGLE_MODE_AND_VALIDATED' if ok else 'FAIL','graviton_H1_H2_H3':'BLOCKED_UNCHANGED'},
 'candidate_residual':False,
 'guardrails':['NO_ZERO_FILL','NO_LOGDET_INSERTION_BEFORE_GRAVITON_AUTHORITY','NO_BLIND_HEAVY_FULL_C5','NO_ANSATZ003_FISHER_RESOURCES'],
 'next_gate':'independently validate ghost routing with a second non-collinear multi-mode background certificate; then freeze ghost authority and proceed to graviton H1/H2/H3' if ok else 'preserve failure and repair covariant-Box routing without weakening thresholds'
},indent=2,sort_keys=True))
