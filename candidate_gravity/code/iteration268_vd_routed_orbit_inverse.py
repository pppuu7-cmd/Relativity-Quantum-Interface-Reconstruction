#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 268.

Physical routed orbit-metric / inverse-resolvent kernel certificate.

This implements the Iteration-267 condensed-index Fourier rule for the orbit
metric itself.  For a background Fourier insertion x, N1[x] maps p to p+k_x.
For a mixed insertion [x,y], N2[x,y] maps p to p+k_x+k_y.  The inverse kernels
must therefore use Q0 at the actual routed endpoint/intermediate momenta:

 Q1[x](p) = -Q0(p+k_x) N1[x](p) Q0(p)

 Q2[x,y](p) = Q0(p+k_x+k_y) [
      N1[x](p+k_y) Q0(p+k_y) N1[y](p)
    + N1[y](p+k_x) Q0(p+k_x) N1[x](p)
    - N2[x,y](p)
 ] Q0(p).

The physical N kernels are extracted from the same finite-amplitude curved
minimal ghost operator and orbit-metric factorization used in Iterations
251/252/258, generalized to the three frozen physical TT modes from Iteration
264.  No loop integration is performed.
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
MODES={'s':(K_S,E_S),'a':(K_A,E_A),'b':(K_B,E_B)}


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


def V(amps,modes):
    g=ETA.astype(complex).copy()
    for a,(_,e) in zip(amps,modes): g+=a*e
    return g/np.sqrt(abs(np.linalg.det(g)))


def norb(amps,modes,p): return V(amps,modes)@nhat(amps,modes,p)
def N0(p): return norb([],[],p)

def N1(x,p,h):
    m=[MODES[x]]
    return (norb([h],m,p)-norb([-h],m,p))/(2*h)

def N2(x,y,p,h):
    m=[MODES[x],MODES[y]]
    return (norb([h,h],m,p)-norb([h,-h],m,p)-norb([-h,h],m,p)+norb([-h,-h],m,p))/(4*h*h)

def Q0(p): return np.linalg.inv(N0(p))

def Q1(x,p,h):
    k=MODES[x][0]
    return -Q0(p+k)@N1(x,p,h)@Q0(p)

def Q2(x,y,p,h1,h2):
    kx,ky=MODES[x][0],MODES[y][0]
    core=(N1(x,p+ky,h1)@Q0(p+ky)@N1(y,p,h1)
         +N1(y,p+kx,h1)@Q0(p+kx)@N1(x,p,h1)
         -N2(x,y,p,h2))
    return Q0(p+kx+ky)@core@Q0(p)

h1=3e-5; h2=5e-4
q1_rows={}
for x in ['s','a','b']:
    k=MODES[x][0]; q1=Q1(x,P0,h1)
    r=N0(P0+k)@q1+N1(x,P0,h1)@Q0(P0)
    wrong=-Q0(P0)@N1(x,P0,h1)@Q0(P0)
    wrong_r=N0(P0+k)@wrong+N1(x,P0,h1)@Q0(P0)
    q1_rows[x]={
      'Q1_fro':float(np.linalg.norm(q1)),
      'inverse_residual_max':float(np.max(np.abs(r))),
      'wrong_same_routing_residual_max':float(np.max(np.abs(wrong_r))),
    }

q2_rows={}
for x,y in [('s','a'),('s','b'),('a','b')]:
    kx,ky=MODES[x][0],MODES[y][0]; q2=Q2(x,y,P0,h1,h2)
    r=(N0(P0+kx+ky)@q2
       +N1(x,P0+ky,h1)@Q1(y,P0,h1)
       +N1(y,P0+kx,h1)@Q1(x,P0,h1)
       +N2(x,y,P0,h2)@Q0(P0))
    q2_rows[x+y]={
      'N2_fro':float(np.linalg.norm(N2(x,y,P0,h2))),
      'Q2_fro':float(np.linalg.norm(q2)),
      'mixed_leg_exchange_max':float(np.max(np.abs(q2-Q2(y,x,P0,h1,h2)))),
      'inverse_residual_max':float(np.max(np.abs(r))),
    }

result={
 'iteration':268,
 'model_readiness_percent':24,
 'loop_momentum':P0.tolist(),
 'fd_steps':{'N1':h1,'N2_mixed':h2},
 'Q1':q1_rows,'Q2':q2_rows,
 'routing_rules':{
   'Q1':'Q1[x](p)=-Q0(p+k_x) N1[x](p) Q0(p)',
   'Q2':'Q0(p+kx+ky)[N1[x](p+ky)Q0(p+ky)N1[y](p)+N1[y](p+kx)Q0(p+kx)N1[x](p)-N2[x,y](p)]Q0(p)'
 },
 'classification':'PASS_SCOPED_PHYSICAL_ROUTED_N1_N2_Q1_Q2_KERNEL_LAYER',
 'guardrail':'Q0 MUST BE EVALUATED AT EACH ROUTED ENDPOINT/INTERMEDIATE MOMENTUM; SAME-p RESOLVENT INSERTION IS FALSE',
 'candidate_residual':False,
 'heavy_run_authorized':False,
 'next_gate':269,
}
assert max(v['inverse_residual_max'] for v in q1_rows.values())<1e-12
assert max(v['inverse_residual_max'] for v in q2_rows.values())<1e-12
assert min(v['wrong_same_routing_residual_max'] for v in q1_rows.values())>0.2
assert min(v['Q2_fro'] for v in q2_rows.values())>1.0
print(json.dumps(result,indent=2,sort_keys=True))
