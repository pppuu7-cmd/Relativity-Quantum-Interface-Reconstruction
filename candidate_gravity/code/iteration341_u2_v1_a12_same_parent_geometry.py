#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 341.

Physical same-parent first/second background expansion of the Vilkovisky U2
vertex A=(D R)*epsilon, using the explicit gravity V1 formula of Giacchini,
de Paula Netto & Shapiro, PRD 102, 106006 (2020), arXiv:2006.04217v4,
Eqs. (54)-(55). Frozen specialization: D=4, Lambda=0, standard linear
metric split (gamma1=1,gamma2=0), and the a=-1/2 parent used by the RQIR
minimal H/N sector.

The polynomial construction and a separate exact-geometry coordinate finite-
difference oracle are independent. This gate freezes A1/A2 only; it does not
assemble U2 until the N/Y inverse-routing bridge is separately closed.
"""
import numpy as np, itertools, json
D=4; M=2; ZERO=(0,0)
eta=np.diag([-1.,1.,1.,1.]).astype(complex)
rng=np.random.default_rng(341)
hs=[]
for _ in range(M):
    x=rng.normal(size=(D,D)); hs.append(0.08*(x+x.T)/2)
qs=[np.array([.31,-.17,.23,.11]), np.array([-.19,.29,.13,-.37])]
p=np.array([.43,-.27,.39,.21])
def deg(a): return sum(a)
def indices(nmax): return [a for n in range(nmax+1) for a in itertools.product(range(n+1),repeat=M) if sum(a)==n]
IND=indices(2)
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def decompositions(a):
    for b in IND:
        if all(b[r]<=a[r] for r in range(M)): yield b,sub(a,b)
def qsum(a): return sum((a[r]*qs[r] for r in range(M)),np.zeros(D))
B=[]
for a in range(D):
    E=np.zeros((D,D),complex); E[a,a]=1; B.append(E)
for a in range(D):
  for b in range(a+1,D):
    E=np.zeros((D,D),complex); E[a,b]=E[b,a]=1/np.sqrt(2); B.append(E)
NB=len(B)
def mat_from_cols(cols):
    out=np.zeros((NB,D),complex)
    for j,T in enumerate(cols):
        for i,F in enumerate(B): out[i,j]=np.vdot(F,T)
    return out
G={ZERO:eta.copy()}
for a in IND[1:]:
    X=np.zeros((D,D),complex)
    for r in range(M):
        if a[r]:
            b=list(a); b[r]-=1; b=tuple(b); X+=hs[r]@G[b]
    G[a]=-eta@X
Gam={ZERO:np.zeros((D,D,D),complex)}
for a in IND[1:]:
    X=np.zeros((D,D,D),complex)
    for r in range(M):
      if a[r]:
        b=list(a); b[r]-=1; b=tuple(b); h,q=hs[r],qs[r]
        for x,m,v,s in itertools.product(range(D),repeat=4):
          X[x,m,v]+=0.5*G[b][x,s]*(1j*q[m]*h[s,v]+1j*q[v]*h[s,m]-1j*q[s]*h[m,v])
    Gam[a]=X
Riem={}
for a in IND:
    Q=qsum(a); R=np.zeros((D,D,D,D),complex)
    for A,b,mu,nu in itertools.product(range(D),repeat=4):
        R[A,b,mu,nu]+=1j*Q[mu]*Gam[a][A,nu,b]-1j*Q[nu]*Gam[a][A,mu,b]
        for u,v in decompositions(a):
            if deg(u)==0 or deg(v)==0: continue
            for rho in range(D): R[A,b,mu,nu]+=Gam[u][A,mu,rho]*Gam[v][rho,nu,b]-Gam[u][A,nu,rho]*Gam[v][rho,mu,b]
    Riem[a]=R
Ric={a:np.einsum('aban->bn',Riem[a]) for a in IND}
RicUp={}; Rsc={}; Rmix={}
for a in IND:
    ru=np.zeros((D,D),complex); rs=0j; rm=np.zeros((D,D),complex)
    for u,b in decompositions(a):
        rs += np.einsum('mn,mn->',G[u],Ric[b])
        rm += np.einsum('mr,rg->mg',G[u],Ric[b])
        for v,w in decompositions(b): ru += np.einsum('ma,nb,ab->mn',G[u],G[v],Ric[w])
    RicUp[a]=ru; Rsc[a]=rs; Rmix[a]=rm
nRicUp={}; nRsc={}
for a in IND:
    Q=qsum(a); nr=np.zeros((D,D,D),complex)
    for gam in range(D):
        nr[gam]=1j*Q[gam]*RicUp[a]
        for u,v in decompositions(a):
            if deg(u)==0: continue
            for mu in range(D):
                for nu in range(D):
                    for rho in range(D): nr[gam,mu,nu]+=Gam[u][mu,gam,rho]*RicUp[v][rho,nu]+Gam[u][nu,gam,rho]*RicUp[v][mu,rho]
    nRicUp[a]=nr; nRsc[a]=1j*Q*Rsc[a]
Dg={}
for a in IND:
    Dg[a]=[1j*p[lam]*np.eye(D,dtype=complex) if a==ZERO else Gam[a][:,lam,:].copy() for lam in range(D)]
DgUp={}
for a in IND:
    arr=[]
    for nu in range(D):
        X=np.zeros((D,D),complex)
        for u,v in decompositions(a):
            for lam in range(D): X += G[u][nu,lam]*Dg[v][lam]
        arr.append(X)
    DgUp[a]=arr
Div={}
for a in IND:
    row=np.zeros(D,complex)
    for gam in range(D): row += Dg[a][gam][gam,:]
    Div[a]=row
Acoef={}
for a in IND:
  cols=[]
  for rhoin in range(D):
    T=np.zeros((D,D),complex)
    for u,v in decompositions(a):
      for mu in range(D):
       for nu in range(D):
        T[mu,nu]+=0.5*sum(Rmix[u][mu,g]*DgUp[v][nu][g,rhoin]+Rmix[u][nu,g]*DgUp[v][mu][g,rhoin] for g in range(D))
        T[mu,nu]+=-0.5*sum(RicUp[u][nu,l]*Dg[v][l][mu,rhoin]+RicUp[u][mu,l]*Dg[v][l][nu,rhoin] for l in range(D))
        T[mu,nu]+=0.5*RicUp[u][mu,nu]*Div[v][rhoin]
        T[mu,nu]+=0.25*Rsc[u]*(DgUp[v][nu][mu,rhoin]+DgUp[v][mu][nu,rhoin])
    T+=nRicUp[a][rhoin]
    for u,b in decompositions(a):
      for v,w in decompositions(b):
       scalar5=sum(Rmix[v][l,g]*Dg[w][l][g,rhoin] for l in range(D) for g in range(D))
       for mu in range(D):
        for nu in range(D):
         T[mu,nu]+=-0.5*G[u][mu,nu]*scalar5
         T[mu,nu]+=-0.25*G[u][mu,nu]*Rsc[v]*Div[w][rhoin]
    for u,v in decompositions(a):
      for mu in range(D):
       for nu in range(D): T[mu,nu]+=-0.5*G[u][mu,nu]*nRsc[v][rhoin]
    cols.append(T)
  Acoef[a]=mat_from_cols(cols)
def geom_x(t,x):
  t=np.asarray(t,float); x=np.asarray(x,float)
  g=eta.copy(); dg=np.zeros((D,D,D),complex); d2g=np.zeros((D,D,D,D),complex)
  for r in range(M):
    phase=np.exp(1j*np.dot(qs[r],x)); amp=t[r]*phase
    g+=amp*hs[r]
    for l in range(D): dg[l]+=1j*qs[r][l]*amp*hs[r]
    for l in range(D):
      for s in range(D): d2g[l,s]+=-qs[r][l]*qs[r][s]*amp*hs[r]
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
  ric=np.einsum('aban->bn',Rm); rup=np.einsum('ma,nb,ab->mn',gi,gi,ric); rsc=np.einsum('mn,mn->',gi,ric); rmix=np.einsum('mr,rg->mg',gi,ric)
  return gi,Ga,rup,rsc,rmix
def direct_fd(t):
  gi,Ga,rup,rsc,rmix=geom_x(t,np.zeros(D))
  hx=2e-5; drup=np.zeros((D,D,D),complex); drsc=np.zeros(D,complex)
  for k in range(D):
    xp=np.zeros(D); xm=np.zeros(D); xp[k]=hx; xm[k]=-hx
    gp=geom_x(t,xp); gm=geom_x(t,xm)
    drup[k]=(gp[2]-gm[2])/(2*hx); drsc[k]=(gp[3]-gm[3])/(2*hx)
  nrup=np.zeros((D,D,D),complex)
  for k in range(D):
    nrup[k]=drup[k]
    for mu in range(D):
      for nu in range(D):
        for r in range(D): nrup[k,mu,nu]+=Ga[mu,k,r]*rup[r,nu]+Ga[nu,k,r]*rup[mu,r]
  dgl=[1j*p[l]*np.eye(D)+Ga[:,l,:] for l in range(D)]
  dgu=[sum(gi[nu,l]*dgl[l] for l in range(D)) for nu in range(D)]
  div=sum((dgl[gam][gam,:] for gam in range(D)),np.zeros(D,complex))
  cols=[]
  for rin in range(D):
    T=np.zeros((D,D),complex)
    for mu in range(D):
      for nu in range(D):
        T[mu,nu]+=0.5*sum(rmix[mu,gam]*dgu[nu][gam,rin]+rmix[nu,gam]*dgu[mu][gam,rin] for gam in range(D))
        T[mu,nu]+=-0.5*sum(rup[nu,l]*dgl[l][mu,rin]+rup[mu,l]*dgl[l][nu,rin] for l in range(D))
        T[mu,nu]+=nrup[rin,mu,nu]+0.5*rup[mu,nu]*div[rin]
        T[mu,nu]+=-0.5*gi[mu,nu]*sum(rmix[l,gam]*dgl[l][gam,rin] for l in range(D) for gam in range(D))
        T[mu,nu]+=0.25*rsc*(dgu[nu][mu,rin]+dgu[mu][nu,rin])
        T[mu,nu]+=-0.5*gi[mu,nu]*drsc[rin]-0.25*gi[mu,nu]*rsc*div[rin]
    cols.append(T)
  return mat_from_cols(cols)
FIT=[a for n in range(4) for a in itertools.product(range(n+1),repeat=M) if sum(a)==n]
us=[-1.,-.5,0.,.5,1.]; samples=list(itertools.product(us,repeat=M)); scale=8e-4
V=np.array([[np.prod([u[r]**a[r] for r in range(M)]) for a in FIT] for u in samples],float)
vals=np.stack([direct_fd(scale*np.array(u)) for u in samples])
coef=np.linalg.lstsq(V,vals.reshape(len(samples),-1),rcond=None)[0].reshape(len(FIT),NB,D)
fi={a:i for i,a in enumerate(FIT)}
errs={a:float(np.max(np.abs(coef[fi[a]]/scale**deg(a)-Acoef[a]))) for a in IND}
first=[a for a in IND if deg(a)==1]; second=[a for a in IND if deg(a)==2]
max1=max(errs[a] for a in first); max2=max(errs[a] for a in second)
a0=float(np.max(np.abs(Acoef[ZERO])))
norm1=max(float(np.max(np.abs(Acoef[a]))) for a in first); norm2=max(float(np.max(np.abs(Acoef[a]))) for a in second)
thresholds={'A0_abs_max':1e-12,'A1_oracle_abs_max':1e-9,'A2_oracle_abs_max':2e-7}
passed=(a0<=thresholds['A0_abs_max'] and max1<=thresholds['A1_oracle_abs_max'] and max2<=thresholds['A2_oracle_abs_max'] and norm1>1e-12 and norm2>1e-12)
result={'iteration':341,'model_readiness_percent':24,'scientific_gate_pass':bool(passed),'classification':('PASS_U2_PHYSICAL_SAME_PARENT_V1_A1_A2_BACKGROUND_KERNELS_EQ55_EXACT_GEOMETRY_ORACLE__NY_ROUTING_REMAINS_BLOCKED' if passed else 'FAIL_U2_V1_A1_A2_BACKGROUND_KERNEL_ORACLE'),'candidate_residual':False,'primary_authority':'Giacchini-de Paula Netto-Shapiro 2020 arXiv:2006.04217v4 Eqs.54-55','specialization':{'D':4,'Lambda':0,'a':'-1/2','gamma1':1,'gamma2':0,'metric_split':'g=eta+h','background_modes':2,'ghost_test_momentum':p.tolist()},'orientation':{'A':'field x ghost (10x4)','V1_L':'A.T (4x10)','V1_R':'A (10x4)','u2_sign_bridge':'Hinv_VD=-K^{-1} from Iteration340'},'background_coefficients':{'A0_max_abs':a0,'A1_mode_count':len(first),'A2_partition_count':len(second),'max_abs_A1_kernel':norm1,'max_abs_A2_kernel':norm2,'A1_oracle_max_abs_error':max1,'A2_oracle_max_abs_error':max2,'per_multiindex_oracle_max_abs_error':{str(a):errs[a] for a in IND},'thresholds':thresholds},'oracle':{'type':'exact geometry plus coordinate finite differences for nabla Ricci and independent amplitude fit','coordinate_fd_step':2e-5,'amplitude_fit_scale':scale},'status':{'physical_A1_A2':'FROZEN_EXECUTABLE' if passed else 'FAIL_PRESERVE','N_Y_inverse_routing':'BLOCKED_SEPARATE_GATE','physical_TrU2_numerator':'BLOCKED_UNTIL_NY_ROUTING'},'guardrails':['NO_U2_ASSEMBLY_BEFORE_NY_ROUTING','ITERATION340_AT_A_ORIENTATION_AND_HINV_MINUS_SIGN_BINDING','UNSUPPORTED_IS_BLOCKED_NOT_ZERO_FILLED','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],'next_gate':'close same-parent N/Y inverse-routing bridge in the a=-1/2 minimal ghost convention, using Eq57 and the already-frozen ghost operator; then assemble first-background-order Tr U2 with A.T/A and Hinv_VD=-K^-1'}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
