#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 270.

Explicit physical routed null-soft B3=[U1 W]_3 nonzero certificate.

Uses the corrected Iteration-269 orbit density Y_down=sqrt(|g|) g, exact routed
Q0/Q1/Q2 convolution recursion, and a direct finite-amplitude realization of
A=R.(D R).E in the same D=4, Lambda=0, a=-1/2 linear metric split.

The direct A construction uses:
- physical TT Fourier backgrounds s,a,b;
- affine diffeomorphism generator R=L_xi g;
- configuration-space Christoffel Gamma(g) with c1=-1,c2=1/4,c3=1/4,c4=-1/8;
- Einstein-action covector sqrt(|g|) G^{mu nu};
- explicit bra/input orbit momenta r_L=-(p+K_M), r_R=p for each A_M kernel.

No loop integration, tensor reduction or source projection is performed.
"""
import itertools, json
import numpy as np

ETA=np.diag([-1.,1.,1.,1.])
P0=np.array([.7,-.4,.5,.9])
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
POS={'s':(K_S,E_S),'a':(K_A,E_A),'b':(K_B,E_B)}
NEG={x:(-k,e) for x,(k,e) in POS.items()}
LEGS=('s','a','b')


def symdelta(mu,nu,r,s):
    return .5*((mu==r and nu==s)+(mu==s and nu==r))

def gamma_tensor(g):
    gi=np.linalg.inv(g); T=np.zeros((4,4,4,4,4,4),complex)
    c1,c2,c3,c4=-1.,.25,.25,-.125
    def P(mu,nu,al,be): return .5*(gi[mu,al]*gi[nu,be]+gi[mu,be]*gi[nu,al])
    for r,s,mu,nu,al,be in itertools.product(range(4),repeat=6):
      S=.25*(symdelta(mu,al,r,s)*gi[nu,be]+symdelta(nu,al,r,s)*gi[mu,be]+symdelta(mu,be,r,s)*gi[nu,al]+symdelta(nu,be,r,s)*gi[mu,al])
      T[r,s,mu,nu,al,be]=c1*S+c2*(symdelta(mu,nu,r,s)*gi[al,be]+symdelta(al,be,r,s)*gi[mu,nu])+c3*P(mu,nu,al,be)*g[r,s]+c4*gi[mu,nu]*gi[al,be]*g[r,s]
    return T


def geometry(amps,modes):
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
    return g,gi,dg,ddg,gam,dgam,ric


def nhat(amps,modes,p):
    g,gi,dg,ddg,gam,dgam,ric=geometry(amps,modes); pc=ETA@p
    out=np.zeros((4,4),complex); ricm=gi@ric
    for beta in range(4):
      pol=np.zeros(4); pol[beta]=1.; lap=np.zeros(4,complex)
      for mu,nu,a in itertools.product(range(4),repeat=3):
       term=-(pc[mu]*pc[nu])*pol[a]
       term+=sum(dgam[mu,a,nu,r]*pol[r] for r in range(4))
       term+=sum(gam[a,nu,r]*(1j*pc[mu])*pol[r] for r in range(4))
       term+=sum(gam[a,mu,s]*((1j*pc[nu])*pol[s]+sum(gam[s,nu,r]*pol[r] for r in range(4))) for s in range(4))
       term-=sum(gam[s,mu,nu]*((1j*pc[s])*pol[a]+sum(gam[a,s,r]*pol[r] for r in range(4))) for s in range(4))
       lap[a]+=gi[mu,nu]*term
      out[:,beta]=lap+ricm@pol
    return out


def y_down(amps,modes):
    g=ETA.astype(complex).copy()
    for a,(_,e) in zip(amps,modes): g+=a*e
    return np.sqrt(abs(np.linalg.det(g)))*g

def norb(amps,modes,p): return y_down(amps,modes)@nhat(amps,modes,p)
def N0(p): return norb([],[],p)
def Q0(p): return np.linalg.inv(N0(p))

def N1(M,x,p,h=3e-5):
    m=[M[x]]
    return (norb([h],m,p)-norb([-h],m,p))/(2*h)

def N2(M,x,y,p,h=2e-4):
    m=[M[x],M[y]]
    f=lambda a,b:norb([a,b],m,p)
    return (f(h,h)-f(h,-h)-f(-h,h)+f(-h,-h))/(4*h*h)

def Q1(M,x,p,h=3e-5):
    k=M[x][0]
    return -Q0(p+k)@N1(M,x,p,h)@Q0(p)

def Q2(M,x,y,p,h1=3e-5,h2=2e-4):
    kx,ky=M[x][0],M[y][0]
    core=N1(M,x,p+ky,h1)@Q0(p+ky)@N1(M,y,p,h1)+N1(M,y,p+kx,h1)@Q0(p+kx)@N1(M,x,p,h1)-N2(M,x,y,p,h2)
    return Q0(p+kx+ky)@core@Q0(p)


def R_and_dR(c,rvec,g,dg,ddg):
    rc=ETA@rvec; R=np.zeros((4,4),complex)
    for mu,nu in itertools.product(range(4),repeat=2):
      R[mu,nu]=sum(c[rho]*dg[rho,mu,nu] for rho in range(4))+1j*rc[mu]*sum(g[rho,nu]*c[rho] for rho in range(4))+1j*rc[nu]*sum(g[mu,rho]*c[rho] for rho in range(4))
    dR=np.zeros((4,4,4),complex)
    for lam,mu,nu in itertools.product(range(4),repeat=3):
      dR[lam,mu,nu]=1j*rc[lam]*R[mu,nu]+sum(c[rho]*ddg[lam,rho,mu,nu] for rho in range(4))+1j*rc[mu]*sum(dg[lam,rho,nu]*c[rho] for rho in range(4))+1j*rc[nu]*sum(dg[lam,mu,rho]*c[rho] for rho in range(4))
    return R,dR


def lie_on_tensor(c,rvec,T,dT):
    rc=ETA@rvec; out=np.zeros((4,4),complex)
    for mu,nu in itertools.product(range(4),repeat=2):
      out[mu,nu]=sum(c[rho]*dT[rho,mu,nu] for rho in range(4))+1j*rc[mu]*sum(T[rho,nu]*c[rho] for rho in range(4))+1j*rc[nu]*sum(T[mu,rho]*c[rho] for rho in range(4))
    return out


def action_covector(g,gi,ric):
    Rsc=np.sum(gi*ric); Ein=ric-.5*g*Rsc
    return np.sqrt(abs(np.linalg.det(g)))*(gi@Ein@gi)


def A_finite(amps,modes,p,total_shift):
    g,gi,dg,ddg,gam,dgam,ric=geometry(amps,modes)
    E=action_covector(g,gi,ric); GT=gamma_tensor(g)
    rR=p; rL=-(p+total_shift); eye=np.eye(4)
    RL=[]; dRL=[]; RR=[]
    for a in range(4):
      rl,drl=R_and_dR(eye[a],rL,g,dg,ddg); rr,_=R_and_dR(eye[a],rR,g,dg,ddg)
      RL.append(rl); dRL.append(drl); RR.append(rr)
    A=np.zeros((4,4),complex)
    for al,be in itertools.product(range(4),repeat=2):
      directional=lie_on_tensor(eye[be],rR,RL[al],dRL[al])
      connection=np.einsum('rsmnab,mn,ab->rs',GT,RL[al],RR[be])
      A[al,be]=np.sum((directional+connection)*E)
    return A


def ksum(M,legs): return sum((M[x][0] for x in legs),np.zeros(4))

def Acoef(M,legs,p,h):
    modes=[M[x] for x in legs]; K=ksum(M,legs); out=np.zeros((4,4),complex)
    for sig in itertools.product([-1,1],repeat=len(legs)):
      out+=np.prod(sig)*A_finite([s*h for s in sig],modes,p,K)
    return out/(2*h)**len(legs)

def Asub(M,legs,p,h1=1e-4,h2=5e-4,h3=1e-3):
    return Acoef(M,list(legs),p,{1:h1,2:h2,3:h3}[len(legs)])

def Qsub(M,legs,p):
    if len(legs)==0:return Q0(p)
    if len(legs)==1:return Q1(M,legs[0],p)
    if len(legs)==2:return Q2(M,legs[0],legs[1],p)
    raise ValueError('Q3 is not required because A0=0')

def term(M,L,Md,R,p,h1=1e-4,h2=5e-4,h3=1e-3):
    kR=ksum(M,R); kM=ksum(M,Md)
    return Qsub(M,L,p+kR+kM)@Asub(M,Md,p+kR,h1,h2,h3)@Qsub(M,R,p)

# A-layer certificates.
Achecks={}
for x in LEGS:
    Ap=Asub(POS,(x,),P0); k=POS[x][0]; An=Asub(NEG,(x,),P0+k)
    Achecks['A1_'+x]={'norm':float(np.linalg.norm(Ap)),'endpoint_transpose_residual':float(np.max(np.abs(Ap.T-An)))}
for x,y in [('s','a'),('s','b'),('a','b')]:
    Ap=Asub(POS,(x,y),P0); K=POS[x][0]+POS[y][0]; An=Asub(NEG,(x,y),P0+K)
    Achecks['A2_'+x+y]={'norm':float(np.linalg.norm(Ap)),'endpoint_transpose_residual':float(np.max(np.abs(Ap.T-An)))}
A3=Asub(POS,LEGS,P0); KT=ksum(POS,LEGS); A3n=Asub(NEG,LEGS,P0+KT)
Achecks['A3_sab']={'norm':float(np.linalg.norm(A3)),'endpoint_transpose_residual':float(np.max(np.abs(A3.T-A3n)))}
Achecks['A3_permutation_residual']=float(max(np.max(np.abs(Asub(POS,p,P0)-A3)) for p in itertools.permutations(LEGS)))

# Enumerate 19 generic Leibniz partitions; null-soft A1[s]=0 removes four.
parts=[]; B19=np.zeros((4,4),complex); B15=np.zeros((4,4),complex)
for assign in itertools.product('LMR',repeat=3):
    L=tuple(LEGS[i] for i,a in enumerate(assign) if a=='L')
    Md=tuple(LEGS[i] for i,a in enumerate(assign) if a=='M')
    R=tuple(LEGS[i] for i,a in enumerate(assign) if a=='R')
    if not Md: continue
    T=term(POS,L,Md,R,P0); B19+=T
    soft_zero=(Md==('s',))
    if not soft_zero:B15+=T
    parts.append({'L':L,'A':Md,'R':R,'norm':float(np.linalg.norm(T)),'soft_A1_zero_class':soft_zero})

# Eight exact transpose representatives from Iteration 266.
REPS=[
 ((),('s','a','b'),()),
 (('s',),('a','b'),()),
 (('a',),('s','b'),()),
 (('b',),('s','a'),()),
 (('s','b'),('a',),()),
 (('s','a'),('b',),()),
 (('s',),('a',),('b',)),
 (('s',),('b',),('a',)),
]
rep_rows=[]; Brep=np.zeros((4,4),complex)
for i,(L,Md,R) in enumerate(REPS):
    X=term(POS,L,Md,R,P0)
    if i==0:
      Xneg=term(NEG,L,Md,R,P0+KT); pair=None; Brep+=X
    else:
      pair=(R,Md,L); Xneg=term(NEG,*pair,P0+KT); Xpair=term(POS,*pair,P0); Brep+=X+Xpair
    rep_rows.append({'class':i+1,'L':L,'A':Md,'R':R,'representative_norm':float(np.linalg.norm(X)),'endpoint_transpose_residual':float(np.max(np.abs(X.T-Xneg))),'partner_norm':None if pair is None else float(np.linalg.norm(Xpair))})

# Full endpoint reversal and step stability.
B15neg=np.zeros((4,4),complex)
for assign in itertools.product('LMR',repeat=3):
    L=tuple(LEGS[i] for i,a in enumerate(assign) if a=='L')
    Md=tuple(LEGS[i] for i,a in enumerate(assign) if a=='M')
    R=tuple(LEGS[i] for i,a in enumerate(assign) if a=='R')
    if not Md or Md==('s',): continue
    B15neg+=term(NEG,L,Md,R,P0+KT)

stability=[]
for h2,h3 in [(1e-3,2e-3),(7e-4,1.5e-3),(5e-4,1e-3),(3e-4,8e-4)]:
    B=np.zeros((4,4),complex)
    for assign in itertools.product('LMR',repeat=3):
      L=tuple(LEGS[i] for i,a in enumerate(assign) if a=='L')
      Md=tuple(LEGS[i] for i,a in enumerate(assign) if a=='M')
      R=tuple(LEGS[i] for i,a in enumerate(assign) if a=='R')
      if not Md or Md==('s',):continue
      B+=term(POS,L,Md,R,P0,1e-4,h2,h3)
    stability.append({'h_A2':h2,'h_A3':h3,'B15_fro':float(np.linalg.norm(B)),'B15_max':float(np.max(np.abs(B)))})

result={
 'iteration':270,'model_readiness_percent':24,
 'A_layer':Achecks,
 'generic_partition_count':len(parts),'surviving_nullsoft_partition_count':sum(not p['soft_A1_zero_class'] for p in parts),
 'soft_A1_four_term_B19_minus_B15_fro':float(np.linalg.norm(B19-B15)),
 'soft_A1_four_term_B19_minus_B15_max':float(np.max(np.abs(B19-B15))),
 'representatives':rep_rows,
 'max_representative_endpoint_transpose_residual':float(max(r['endpoint_transpose_residual'] for r in rep_rows)),
 'B15_fro':float(np.linalg.norm(B15)),'B15_max':float(np.max(np.abs(B15))),
 'B15_endpoint_transpose_residual':float(np.max(np.abs(B15.T-B15neg))),
 'B15_8class_reconstruction_residual':float(np.max(np.abs(B15-Brep))),
 'step_stability':stability,
 'classification':'PASS_SCOPED_PHYSICAL_ROUTED_NULLSOFT_B3_EXPLICIT_NONZERO_AND_TRANSPOSE_VALIDATED',
 'guardrail':'NONZERO_B3 IS A C5 NUMERATOR CERTIFICATE ONLY; DO NOT PROMOTE TO FINAL COMPARATOR OR CANDIDATE RESIDUAL BEFORE TENSOR REDUCTION_SOURCE_COMPLETION_AND_HARD_CHANNEL_PROJECTION',
 'candidate_residual':False,'tensor_reduction_now_authorized':True,'heavy_full_C5_run_authorized':False,'next_gate':271
}
assert result['generic_partition_count']==19 and result['surviving_nullsoft_partition_count']==15
assert Achecks['A1_s']['norm']<2e-8 and Achecks['A1_a']['norm']>.3 and Achecks['A1_b']['norm']>.4
assert result['B15_fro']>2.0 and result['B15_max']>1.0
assert result['max_representative_endpoint_transpose_residual']<1e-6
assert result['B15_endpoint_transpose_residual']<1e-6
assert result['B15_8class_reconstruction_residual']<1e-12
print(json.dumps(result,indent=2,sort_keys=True))
