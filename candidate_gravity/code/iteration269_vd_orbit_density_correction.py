#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 269.

Correction of the orbit-metric density factor in the routed physical N/Q layer.

Primary same-parent convention:
  Nhat^alpha_beta = Y^{alpha gamma} N_orb_{gamma beta}
  Y^{alpha beta} = g^{alpha beta}/sqrt(|g|)  (up to the fixed overall sign)
therefore
  N_orb = Y_down Nhat,  Y_down = sqrt(|g|) g_{alpha beta}.

Iterations 258/268 used g/sqrt(|g|), which agrees at first order for TT
backgrounds but has the opposite second-order density coefficient.  This script
shows that the corrected factor restores endpoint-reversed Fourier transpose of
physical N2/Q2 while preserving exact routed inverse recursion.
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
    return g,gi,gam,dgam,ric


def nhat(amps,modes,p):
    g,gi,gam,dgam,ric=geometry(amps,modes); pc=ETA@p
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


def y_down_wrong(amps,modes):
    g=ETA.astype(complex).copy()
    for a,(_,e) in zip(amps,modes): g+=a*e
    return g/np.sqrt(abs(np.linalg.det(g)))


def norb(amps,modes,p,correct=True):
    V=y_down(amps,modes) if correct else y_down_wrong(amps,modes)
    return V@nhat(amps,modes,p)

def N0(p): return norb([],[],p)

def N1(M,x,p,h=3e-5):
    m=[M[x]]
    return (norb([h],m,p)-norb([-h],m,p))/(2*h)

def N2(M,x,y,p,h=2e-4,correct=True):
    m=[M[x],M[y]]
    f=lambda a,b:norb([a,b],m,p,correct=correct)
    return (f(h,h)-f(h,-h)-f(-h,h)+f(-h,-h))/(4*h*h)

def Q0(p): return np.linalg.inv(N0(p))
def Q1(M,x,p,h=3e-5):
    k=M[x][0]
    return -Q0(p+k)@N1(M,x,p,h)@Q0(p)

def Q2(M,x,y,p,h1=3e-5,h2=2e-4):
    kx,ky=M[x][0],M[y][0]
    core=(N1(M,x,p+ky,h1)@Q0(p+ky)@N1(M,y,p,h1)
         +N1(M,y,p+kx,h1)@Q0(p+kx)@N1(M,x,p,h1)
         -N2(M,x,y,p,h2,True))
    return Q0(p+kx+ky)@core@Q0(p)

q1={}
for x in ['s','a','b']:
    k=POS[x][0]; q=Q1(POS,x,P0)
    inv=N0(P0+k)@q+N1(POS,x,P0)@Q0(P0)
    tr=np.max(np.abs(q.T-Q1(NEG,x,P0+k)))
    q1[x]={'norm':float(np.linalg.norm(q)),'inverse_residual':float(np.max(np.abs(inv))),'endpoint_transpose_residual':float(tr)}

q2={}
for x,y in [('s','a'),('s','b'),('a','b')]:
    kx,ky=POS[x][0],POS[y][0]; K=kx+ky
    q=Q2(POS,x,y,P0)
    inv=(N0(P0+K)@q+N1(POS,x,P0+ky)@Q1(POS,y,P0)+N1(POS,y,P0+kx)@Q1(POS,x,P0)+N2(POS,x,y,P0)@Q0(P0))
    ntr=np.max(np.abs(N2(POS,x,y,P0).T-N2(NEG,x,y,P0+K)))
    qtr=np.max(np.abs(q.T-Q2(NEG,x,y,P0+K)))
    wrong_ntr=np.max(np.abs(N2(POS,x,y,P0,correct=False).T-N2(NEG,x,y,P0+K,correct=False)))
    q2[x+y]={
      'N2_norm':float(np.linalg.norm(N2(POS,x,y,P0))),
      'Q2_norm':float(np.linalg.norm(q)),
      'inverse_residual':float(np.max(np.abs(inv))),
      'mixed_leg_exchange_residual':float(np.max(np.abs(q-Q2(POS,y,x,P0)))),
      'N2_endpoint_transpose_residual':float(ntr),
      'Q2_endpoint_transpose_residual':float(qtr),
      'wrong_density_N2_endpoint_transpose_residual':float(wrong_ntr),
    }

# Single-mode second-order density sign, using the soft TT mode with tr(H^2)=1.
H=ETA@E_S
single_density={
 'tr_H2':float(np.trace(H@H)),
 'correct_Ydown_t2_coefficient':'-(tr(H^2)/4) eta',
 'superseded_wrong_coefficient':'+(tr(H^2)/4) eta'
}

result={
 'iteration':269,
 'model_readiness_percent':24,
 'primary_density_correction':{
   'Y_up':'g^{alpha beta}/sqrt(|g|) up to fixed overall sign',
   'Y_down':'sqrt(|g|) g_{alpha beta}',
   'Nhat_factorization':'Nhat=Y_up N_orb; N_orb=Y_down Nhat'
 },
 'single_mode_TT_density':single_density,
 'Q1':q1,'Q2':q2,
 'classification':'PASS_PRIMARY_AUTHORITY_ORBIT_DENSITY_CORRECTION_AND_ROUTED_N2_Q2_TRANSPOSE_RESTORATION',
 'supersedes':'Iteration 252 density representative and Iterations 258/259/268 second-order Norb/Q2 numerical values only; first-order TT deltaY, Q1, routing logic and inverse-recursion algebra remain valid',
 'guardrail':'USE_Y_UP=g^-1/sqrt|g| AND Y_DOWN=sqrt|g|*g; DO_NOT_USE_THE_INVERTED_DENSITY_FACTOR',
 'candidate_residual':False,'heavy_run_authorized':False,'next_gate':270
}
assert max(v['inverse_residual'] for v in q1.values())<1e-12
assert max(v['inverse_residual'] for v in q2.values())<1e-12
assert max(v['Q2_endpoint_transpose_residual'] for v in q2.values())<1e-6
assert min(v['wrong_density_N2_endpoint_transpose_residual'] for v in q2.values())>1e-2
print(json.dumps(result,indent=2,sort_keys=True))
