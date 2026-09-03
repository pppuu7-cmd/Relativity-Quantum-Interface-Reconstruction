#!/usr/bin/env python3
"""RQIR Iteration 320: first physical determinant e=0,c<=3 integrand coefficient.

Uses the validated Iteration-319 graviton expansion as the common three-mode
background fixture, reconstructs the ghost N coefficients on exactly that same
fixture, independently validates ghost routing against exact geometry, then
assembles the [t1 t2 t3] coefficient of 1/2 Tr log H - Tr log N using the
Iteration-312 frozen cubic logdet topology. This is an integrand-level routed
coefficient, not a loop-integrated observable and not a comparator residual.
"""
from __future__ import annotations
import contextlib, io, itertools, json, runpy, numpy as np
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    g=runpy.run_path('candidate_gravity/code/iteration319_det_graviton_three_mode_routing.py')
D,M,ZERO=g['D'],g['M'],g['ZERO']; eta=g['eta']; hs=g['hs']; qs=g['qs']; p=g['p']; IND=g['IND']; G=g['G']; Gam=g['Gam']; Ric=g['Ric']; H=g['H']
deg=g['deg']; decompositions=g['decompositions']; qsum=g['qsum']
# Ghost N = Box_vector + R^a_b on the exact same background/routing fixture.
Rm={}
for a in IND:
    X=np.zeros((D,D),complex)
    for b,c in decompositions(a): X+=G[b]@Ric[c]
    Rm[a]=X
D1={}
for a in IND:
    D1[a]=[1j*p[nu]*np.eye(D) if a==ZERO else Gam[a][:,nu,:].copy() for nu in range(D)]
S={}
for a in IND:
    kout=p+qsum(a); aa=[[None]*D for _ in range(D)]
    for mu in range(D):
      for nu in range(D):
        X=1j*kout[mu]*D1[a][nu]
        for b,c in decompositions(a):
          if deg(b)==0: continue
          X+=Gam[b][:,mu,:]@D1[c][nu]
          for rho in range(D): X-=Gam[b][rho,mu,nu]*D1[c][rho]
        aa[mu][nu]=X
    S[a]=aa
N={}
for a in IND:
    X=np.zeros((D,D),complex)
    for b,c in decompositions(a):
      for mu in range(D):
       for nu in range(D): X+=G[b][mu,nu]*S[c][mu][nu]
    N[a]=X+Rm[a]
# Independent exact-geometry ghost oracle, same hs/qs/p.
def ghost_direct(t):
    g0=eta.copy(); dg=np.zeros((D,D,D),complex); d2g=np.zeros((D,D,D,D),complex)
    for r in range(M):
      g0+=t[r]*hs[r]
      for l in range(D): dg[l]+=1j*qs[r][l]*t[r]*hs[r]
      for l in range(D):
       for s in range(D): d2g[l,s]+=-qs[r][l]*qs[r][s]*t[r]*hs[r]
    gi=np.linalg.inv(g0); dgi=np.array([-gi@dg[l]@gi for l in range(D)])
    Ga=np.zeros((D,D,D),complex); dGa=np.zeros((D,D,D,D),complex)
    for A,m,n,s in itertools.product(range(D),repeat=4): Ga[A,m,n]+=0.5*gi[A,s]*(dg[m,s,n]+dg[n,s,m]-dg[s,m,n])
    for l,A,m,n,s in itertools.product(range(D),repeat=5):
      B=dg[m,s,n]+dg[n,s,m]-dg[s,m,n]; dB=d2g[l,m,s,n]+d2g[l,n,s,m]-d2g[l,s,m,n]
      dGa[l,A,m,n]+=0.5*(dgi[l,A,s]*B+gi[A,s]*dB)
    Ric0=np.zeros((D,D),complex)
    for m,n,A in itertools.product(range(D),repeat=3):
      Ric0[m,n]+=dGa[A,A,m,n]-dGa[n,A,m,A]
      for l in range(D): Ric0[m,n]+=Ga[A,A,l]*Ga[l,m,n]-Ga[A,n,l]*Ga[l,m,A]
    Rmix=gi@Ric0; out=np.zeros((D,D),complex)
    for mu in range(D):
      for nu in range(D):
        X=-(p[mu]*p[nu])*np.eye(D)+dGa[mu,:,nu,:]+1j*p[nu]*Ga[:,mu,:]+1j*p[mu]*Ga[:,nu,:]+Ga[:,mu,:]@Ga[:,nu,:]
        for rho in range(D): X-=Ga[rho,mu,nu]*(1j*p[rho]*np.eye(D)+Ga[:,rho,:])
        out+=gi[mu,nu]*X
    return out+Rmix
# Fit ghost direct oracle through total degree 4.
def indices(nmax): return [a for n in range(nmax+1) for a in itertools.product(range(n+1),repeat=M) if sum(a)==n]
FIT=indices(4); scale=3e-4; us=[-1.,-.5,0.,.5,1.]; samples=list(itertools.product(us,repeat=M))
V=np.array([[np.prod([u[r]**a[r] for r in range(M)]) for a in FIT] for u in samples],float)
vals=np.stack([ghost_direct(scale*np.array(u)) for u in samples])
coef=np.linalg.lstsq(V,vals.reshape(len(samples),-1),rcond=None)[0].reshape(len(FIT),D,D); fi={a:i for i,a in enumerate(FIT)}
fitN={a:coef[fi[a]]/scale**deg(a) for a in IND}; err={a:float(np.max(np.abs(fitN[a]-N[a]))) for a in IND}; maxdeg={n:max(err[a] for a in IND if deg(a)==n) for n in range(4)}
thr={0:1e-9,1:1e-7,2:1e-5,3:1e-3}
TARGET=(1,1,1)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def cubic_coeff(K):
    K0i=np.linalg.inv(K[ZERO]); A={a:K0i@K[a] for a in IND if a!=ZERO}
    c=np.trace(A[TARGET]); pair=0j; triple=0j
    nz=list(A)
    for a in nz:
      for b in nz:
        if add(a,b)==TARGET: pair+=np.trace(A[a]@A[b])
    for a in nz:
      for b in nz:
       for c0 in nz:
        if add(add(a,b),c0)==TARGET: triple+=np.trace(A[a]@A[b]@A[c0])
    return c-0.5*pair+triple/3, pair, triple
cH,pH,tH=cubic_coeff(H); cN,pN,tN=cubic_coeff(N); ceff=0.5*cH-cN
finite=all(np.isfinite([cH.real,cH.imag,cN.real,cN.imag,ceff.real,ceff.imag]))
ok=finite and all(maxdeg[n]<thr[n] for n in range(4)) and abs(ceff)>1e-10
result={'iteration':320,'model_readiness_percent':24,'scientific_gate_pass':bool(ok),'classification':('PASS_FIRST_PHYSICAL_DETERMINANT_E0C3_SHARED_BACKGROUND_INTEGRAND_COEFFICIENT' if ok else 'FAIL_FIRST_PHYSICAL_DETERMINANT_E0C3_SHARED_BACKGROUND_INTEGRAND_COEFFICIENT'),'candidate_residual':False,'parent_authority':{'graviton_iteration':319,'graviton_run':33722207947,'graviton_artifact':9880621340,'graviton_result_sha256':'517adcb91f53f5758adf9af01c8b68a21c0a645627241639312b66a01e659671','ghost_iteration':317,'logdet_topology_iteration':312},'scope':{'D':4,'Lambda':0,'a':'-1/2','common_three_mode_fixture':True,'coefficient_multiindex':[1,1,1],'effective_determinant':'1/2 Tr log H - Tr log N','status':'integrand_level_not_loop_integrated'},'ghost_common_fixture_validation_max_abs_error_by_degree':{str(k):v for k,v in maxdeg.items()},'ghost_validation_threshold_by_degree':{str(k):v for k,v in thr.items()},'coefficients':{'graviton_cubic_111':{'real':float(cH.real),'imag':float(cH.imag)},'ghost_cubic_111':{'real':float(cN.real),'imag':float(cN.imag)},'effective_halfH_minus_N_cubic_111':{'real':float(ceff.real),'imag':float(ceff.imag)}},'guardrails':['NOT_A_COMPARATOR_RESIDUAL','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5','UNSUPPORTED_IS_BLOCKED_NOT_ZERO_FILLED'],'next_gate':('derive/reduce the common-fixture determinant coefficient into loop-denominator families and classify pole/cut origin before any source/Born subtraction' if ok else 'preserve FAIL and repair common-fixture routing without weakening thresholds')}
print(json.dumps(result,indent=2,sort_keys=True))
if not ok: raise SystemExit(2)
