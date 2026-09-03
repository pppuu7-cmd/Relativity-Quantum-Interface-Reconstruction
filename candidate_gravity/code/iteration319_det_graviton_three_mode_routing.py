#!/usr/bin/env python3
"""RQIR Iteration 319: physical graviton H1/H2/H3 multimode routing gate.

Expands the Iteration-318 frozen minimal tensor Laplace operator H=-(Box+Pi)
on a fixed 10-component symmetric contravariant tensor basis through total cubic
background order for three non-collinear Fourier modes. The polynomial-routing
implementation is checked against a separate direct exact-geometry oracle and
multivariate degree-4 fit. No missing kernel is zero-filled.
"""
from __future__ import annotations
import itertools, json, numpy as np
D=4; M=3; ZERO=(0,0,0)
eta=np.diag([-1.,1.,1.,1.]).astype(complex)
rng=np.random.default_rng(319)
hs=[]
for _ in range(M):
    x=rng.normal(size=(D,D)); hs.append(0.12*(x+x.T)/2)
qs=[np.array([.27,-.19,.31,.11]),np.array([-.13,.37,.17,-.29]),np.array([.22,.08,-.34,.41])]
p=np.array([.61,-.33,.24,.52])
def deg(a): return sum(a)
def indices(nmax): return [a for n in range(nmax+1) for a in itertools.product(range(n+1),repeat=M) if sum(a)==n]
IND=indices(3)
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def decompositions(a):
    for b in IND:
        if all(b[r]<=a[r] for r in range(M)): yield b,sub(a,b)
def qsum(a): return sum((a[r]*qs[r] for r in range(M)),np.zeros(D))
B=[]; labels=[]
for a in range(D):
    E=np.zeros((D,D),complex); E[a,a]=1; B.append(E); labels.append((a,a))
for a in range(D):
  for b in range(a+1,D):
    E=np.zeros((D,D),complex); E[a,b]=E[b,a]=1/np.sqrt(2); B.append(E); labels.append((a,b))
NB=len(B)
def mat_from_action(action):
    out=np.zeros((NB,NB),complex)
    for j,E in enumerate(B):
        Y=action(E)
        for i,F in enumerate(B): out[i,j]=np.vdot(F,Y)
    return out
G={ZERO:eta.copy()}
for a in IND[1:]:
    X=np.zeros((D,D),complex)
    for r in range(M):
        if a[r]:
            b=list(a); b[r]-=1; b=tuple(b); X+=hs[r]@G[b]
    G[a]=-eta@X
gcoef={a:np.zeros((D,D),complex) for a in IND}; gcoef[ZERO]=eta.copy()
for r in range(M):
    a=tuple(1 if j==r else 0 for j in range(M)); gcoef[a]=hs[r].astype(complex)
Gam={ZERO:np.zeros((D,D,D),complex)}
for a in IND[1:]:
    A=np.zeros((D,D,D),complex)
    for r in range(M):
      if a[r]:
        b=list(a); b[r]-=1; b=tuple(b); h,q=hs[r],qs[r]
        for x,m,v,s in itertools.product(range(D),repeat=4):
          A[x,m,v]+=0.5*G[b][x,s]*(1j*q[m]*h[s,v]+1j*q[v]*h[s,m]-1j*q[s]*h[m,v])
    Gam[a]=A
Riem={}
for a in IND:
    Q=qsum(a); R=np.zeros((D,D,D,D),complex)
    for A,b,mu,nu in itertools.product(range(D),repeat=4):
        R[A,b,mu,nu]+=1j*Q[mu]*Gam[a][A,nu,b]-1j*Q[nu]*Gam[a][A,mu,b]
        for u,v in decompositions(a):
            if deg(u)==0 or deg(v)==0: continue
            for rho in range(D):
                R[A,b,mu,nu]+=Gam[u][A,mu,rho]*Gam[v][rho,nu,b]-Gam[u][A,nu,rho]*Gam[v][rho,mu,b]
    Riem[a]=R
Ric={a:np.einsum('aban->bn',Riem[a]) for a in IND}
Rsc={}; RicUp={}
for a in IND:
    rs=0j; ru=np.zeros((D,D),complex)
    for u,v in decompositions(a): rs+=np.einsum('mn,mn->',G[u],Ric[v])
    for u,b in decompositions(a):
      for v,w in decompositions(b): ru+=np.einsum('ma,nb,ab->mn',G[u],G[v],Ric[w])
    Rsc[a]=rs; RicUp[a]=ru
Rmix2={}
for a in IND:
    X=np.zeros((D,D,D,D),complex)
    for u,v in decompositions(a): X+=np.einsum('nr,marb->manb',G[u],Riem[v])
    Rmix2[a]=X
Pi={}
for a in IND:
  def act(T,a=a):
    Y=2*np.einsum('manb,ab->mn',Rmix2[a],T)
    tmp=np.zeros((D,D,D,D),complex)
    for u,v in decompositions(a): tmp+=np.einsum('mn,ab->mnab',G[u],Ric[v])
    Y+=-0.5*np.einsum('mnab,ab->mn',tmp,T)
    tmp=np.zeros((D,D,D,D),complex)
    for u,v in decompositions(a): tmp+=np.einsum('ab,mn->mnab',gcoef[u],RicUp[v])
    Y+=-0.5*np.einsum('mnab,ab->mn',tmp,T)
    tmp=np.zeros((D,D,D,D),complex)
    for u,b in decompositions(a):
      for v,w in decompositions(b): tmp+=np.einsum('mn,ab->mnab',G[u],gcoef[v])*Rsc[w]
    Y+=0.25*np.einsum('mnab,ab->mn',tmp,T)
    Y+=-0.5*Rsc[a]*T
    return Y
  Pi[a]=mat_from_action(act)
D1={}
for a in IND:
  arr=[]
  for nu in range(D):
    def act(T,a=a,nu=nu):
      if a==ZERO: return 1j*p[nu]*T
      Ga=Gam[a]
      return np.einsum('ar,rb->ab',Ga[:,nu,:],T)+np.einsum('br,ar->ab',Ga[:,nu,:],T)
    arr.append(mat_from_action(act))
  D1[a]=arr
S={}
for a in IND:
  kout=p+qsum(a); aa=[[None]*D for _ in range(D)]
  for mu in range(D):
    for nu in range(D):
      X=1j*kout[mu]*D1[a][nu]
      for u,v in decompositions(a):
        if deg(u)==0: continue
        Gu=Gam[u]
        def upper_conn(Y,Gu=Gu,mu=mu):
          return np.einsum('ar,rb->ab',Gu[:,mu,:],Y)+np.einsum('br,ar->ab',Gu[:,mu,:],Y)
        X+=mat_from_action(upper_conn)@D1[v][nu]
        for rho in range(D): X-=Gu[rho,mu,nu]*D1[v][rho]
      aa[mu][nu]=X
  S[a]=aa
Box={}; H={}
for a in IND:
  X=np.zeros((NB,NB),complex)
  for u,v in decompositions(a):
    for mu in range(D):
      for nu in range(D): X+=G[u][mu,nu]*S[v][mu][nu]
  Box[a]=X; H[a]=-(X+Pi[a])
def direct(t):
  g=eta.copy(); dg=np.zeros((D,D,D),complex); d2g=np.zeros((D,D,D,D),complex)
  for r in range(M):
    g+=t[r]*hs[r]
    for l in range(D): dg[l]+=1j*qs[r][l]*t[r]*hs[r]
    for l in range(D):
      for s in range(D): d2g[l,s]+=-qs[r][l]*qs[r][s]*t[r]*hs[r]
  gi=np.linalg.inv(g); dgi=np.zeros((D,D,D),complex)
  for l in range(D): dgi[l]=-gi@dg[l]@gi
  Ga=np.zeros((D,D,D),complex); dGa=np.zeros((D,D,D,D),complex)
  for A,m,n,s in itertools.product(range(D),repeat=4): Ga[A,m,n]+=0.5*gi[A,s]*(dg[m,s,n]+dg[n,s,m]-dg[s,m,n])
  for l,A,m,n,s in itertools.product(range(D),repeat=5):
    bb=dg[m,s,n]+dg[n,s,m]-dg[s,m,n]; db=d2g[l,m,s,n]+d2g[l,n,s,m]-d2g[l,s,m,n]
    dGa[l,A,m,n]+=0.5*(dgi[l,A,s]*bb+gi[A,s]*db)
  Rm=np.zeros((D,D,D,D),complex)
  for A,b,mu,nu in itertools.product(range(D),repeat=4):
    Rm[A,b,mu,nu]=dGa[mu,A,nu,b]-dGa[nu,A,mu,b]
    for rho in range(D): Rm[A,b,mu,nu]+=Ga[A,mu,rho]*Ga[rho,nu,b]-Ga[A,nu,rho]*Ga[rho,mu,b]
  Ric=np.einsum('aban->bn',Rm); Rscalar=np.einsum('mn,mn->',gi,Ric); Ricup=np.einsum('ma,nb,ab->mn',gi,gi,Ric); Rmix=np.einsum('nr,marb->manb',gi,Rm)
  def op(T):
    Dv=[]
    for nu in range(D): Dv.append(1j*p[nu]*T+np.einsum('ar,rb->ab',Ga[:,nu,:],T)+np.einsum('br,ar->ab',Ga[:,nu,:],T))
    box=np.zeros((D,D),complex)
    for mu in range(D):
      for nu in range(D):
        partial=-p[mu]*p[nu]*T
        partial+=1j*p[mu]*(np.einsum('ar,rb->ab',Ga[:,nu,:],T)+np.einsum('br,ar->ab',Ga[:,nu,:],T))
        partial+=np.einsum('ar,rb->ab',dGa[mu,:,nu,:],T)+np.einsum('br,ar->ab',dGa[mu,:,nu,:],T)
        sec=partial+np.einsum('ar,rb->ab',Ga[:,mu,:],Dv[nu])+np.einsum('br,ar->ab',Ga[:,mu,:],Dv[nu])
        for rho in range(D): sec-=Ga[rho,mu,nu]*Dv[rho]
        box+=gi[mu,nu]*sec
    pi=2*np.einsum('manb,ab->mn',Rmix,T)
    pi+=-0.5*gi*np.einsum('ab,ab->',Ric,T)-0.5*Ricup*np.einsum('ab,ab->',g,T)
    pi+=0.25*gi*Rscalar*np.einsum('ab,ab->',g,T)-0.5*Rscalar*T
    return -(box+pi)
  return mat_from_action(op)
FIT=indices(4); us=[-1.,-.5,0.,.5,1.]; samples=list(itertools.product(us,repeat=M)); scale=3e-4
V=np.array([[np.prod([u[r]**a[r] for r in range(M)]) for a in FIT] for u in samples],float)
vals=np.stack([direct(scale*np.array(u)) for u in samples])
coef=np.linalg.lstsq(V,vals.reshape(len(samples),-1),rcond=None)[0].reshape(len(FIT),NB,NB)
fi={a:i for i,a in enumerate(FIT)}; fitH={a:coef[fi[a]]/scale**deg(a) for a in IND}
errs={a:float(np.max(np.abs(fitH[a]-H[a]))) for a in IND}
maxdeg={n:max(errs[a] for a in IND if deg(a)==n) for n in range(4)}
q_rank=int(np.linalg.matrix_rank(np.stack(qs),tol=1e-12)); p2=complex(np.einsum('mn,m,n->',eta,p,p)); h0_flat_error=float(np.max(np.abs(H[ZERO]-p2*np.eye(NB))))
threshold={0:1e-9,1:1e-7,2:1e-5,3:1e-3}
ok=(q_rank==3 and h0_flat_error<1e-12 and all(maxdeg[n]<threshold[n] for n in range(4)) and errs[(1,1,1)]<1e-3)
result={'iteration':319,'model_readiness_percent':24,'scientific_gate_pass':bool(ok),'classification':('PASS_GRAVITON_H123_THREE_MODE_EXACT_GEOMETRY_ROUTING_CERTIFICATE' if ok else 'FAIL_GRAVITON_H123_THREE_MODE_EXACT_GEOMETRY_ROUTING_CERTIFICATE'),'scope':{'D':4,'Lambda':0,'a':'-1/2','modes':3,'q_rank':q_rank,'tensor_basis':'10-component Frobenius-orthonormal symmetric contravariant basis: diagonals then off-diagonals /sqrt(2)','target_total_degree':3,'direct_fit_total_degree':4,'fit_scale':scale},'frozen_parent':{'H':'-(I Box + Pi)','Pi':'2 R^mu_alpha^nu_beta - 1/2 g^munu R_alphabeta - 1/2 g_alphabeta R^munu + 1/4 g^munu g_alphabeta R - 1/2 delta_sym R'},'validation_max_abs_error_by_total_degree':{str(k):v for k,v in maxdeg.items()},'validation_threshold_by_total_degree':{str(k):v for k,v in threshold.items()},'triple_mixed_111_max_abs_error':errs[(1,1,1)],'flat_H0_identity_max_abs_error':h0_flat_error,'physical_status':{'graviton_H1_H2_H3':('FULL_ROUTED_COMPONENT_AUTHORITY_READY_TO_FREEZE' if ok else 'FAIL_PRESERVE_AND_REPAIR'),'ghost_N1_N2_N3':'FROZEN_FROM_ITERATION_317','connection_U2_physical':'BLOCKED_UNCHANGED'},'candidate_residual':False,'guardrails':['UNSUPPORTED_IS_BLOCKED_NOT_ZERO_FILLED','NO_RANDOM_MATRIX_SURROGATE','NO_LOGDET_INSERTION_UNLESS_THIS_GATE_PASSES','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5'],'next_gate':('freeze full physical graviton H1/H2/H3 authority, then insert frozen ghost+graviton components into Iteration-312 cubic logdet topology and compute the first physical determinant e=0,c<=3 coefficient' if ok else 'preserve scientific FAIL and repair rank-2 covariant-Box/Pi routing without weakening thresholds')}
print(json.dumps(result,indent=2,sort_keys=True))
