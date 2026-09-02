#!/usr/bin/env python3
"""RQIR Iteration 259: physical same-parent Q2 from the frozen orbit metric.

Frozen convention: D=4, Lambda=0, DeWitt a=-1/2, eta=(-,+,+,+), linear covariant-metric split.
Extends Iteration 258.  No independent Q2 is introduced: Q=N_orb^-1 is differentiated directly and
compared with Q1=-Q0 N1 Q0 and Q2=Q0 N1 Q0 N1 Q0-Q0 N2 Q0.
"""
import json
import numpy as np

ETA=np.diag([-1.0,1.0,1.0,1.0])
K=np.array([0.2,0.6,0.3,0.1]); P=np.array([0.7,-0.4,0.5,0.9])
q=K[1:]; u=np.array([q[1],-q[0],0.0]); u/=np.linalg.norm(u); v=np.cross(q,u); v/=np.linalg.norm(v)
EPS=np.zeros((4,4)); EPS[1:,1:]=(np.outer(u,u)-np.outer(v,v))/np.sqrt(2)

def geometry(t):
    g=ETA+t*EPS; gi=np.linalg.inv(g); kc=ETA@K
    dg=np.zeros((4,4,4),complex); ddg=np.zeros((4,4,4,4),complex)
    for mu in range(4):
        dg[mu]=1j*kc[mu]*t*EPS
        for nu in range(4): ddg[mu,nu]=-(kc[mu]*kc[nu])*t*EPS
    dgi=np.array([-gi@dg[lam]@gi for lam in range(4)])
    gam=np.zeros((4,4,4),complex); dgam=np.zeros((4,4,4,4),complex)
    for a in range(4):
      for mu in range(4):
       for nu in range(4):
        A=[dg[mu,s,nu]+dg[nu,s,mu]-dg[s,mu,nu] for s in range(4)]
        gam[a,mu,nu]=0.5*sum(gi[a,s]*A[s] for s in range(4))
        for lam in range(4):
          dgam[lam,a,mu,nu]=0.5*sum(dgi[lam,a,s]*A[s]+gi[a,s]*(ddg[lam,mu,s,nu]+ddg[lam,nu,s,mu]-ddg[lam,s,mu,nu]) for s in range(4))
    ric=np.zeros((4,4),complex)
    for mu in range(4):
      for nu in range(4):
       for r in range(4):
        ric[mu,nu]+=dgam[r,r,mu,nu]-dgam[nu,r,mu,r]
        for ell in range(4): ric[mu,nu]+=gam[r,r,ell]*gam[ell,mu,nu]-gam[r,nu,ell]*gam[ell,mu,r]
    return g,gi,gam,dgam,ric

def nhat(t):
    g,gi,gam,dgam,ric=geometry(t); pc=ETA@P; out=np.zeros((4,4),complex); ricm=gi@ric
    for beta in range(4):
      pol=np.zeros(4); pol[beta]=1.0; lap=np.zeros(4,complex)
      for mu in range(4):
       for nu in range(4):
        for a in range(4):
         term=-(pc[mu]*pc[nu])*pol[a]
         term+=sum(dgam[mu,a,nu,r]*pol[r] for r in range(4))
         term+=sum(gam[a,nu,r]*(1j*pc[mu])*pol[r] for r in range(4))
         term+=sum(gam[a,mu,s]*((1j*pc[nu])*pol[s]+sum(gam[s,nu,r]*pol[r] for r in range(4))) for s in range(4))
         term-=sum(gam[s,mu,nu]*((1j*pc[s])*pol[a]+sum(gam[a,s,r]*pol[r] for r in range(4))) for s in range(4))
         lap[a]+=gi[mu,nu]*term
      out[:,beta]=lap+ricm@pol
    return out

def vinv_weight(t):
    g=ETA+t*EPS
    return g/np.sqrt(abs(np.linalg.det(g)))

def norb(t): return vinv_weight(t)@nhat(t)
def qphys(t): return np.linalg.inv(norb(t))

N0=norb(0.0); Q0=np.linalg.inv(N0)
rows=[]
for h in [1e-2,3e-3,1e-3,3e-4,1e-4]:
    Np,Nm=norb(h),norb(-h)
    N1=(Np-Nm)/(2*h)
    N2=(Np+Nm-2*N0)/(2*h*h)
    Q1rec=-Q0@N1@Q0
    Q2rec=Q0@N1@Q0@N1@Q0-Q0@N2@Q0
    Qp,Qm=qphys(h),qphys(-h)
    Q1direct=(Qp-Qm)/(2*h)
    Q2direct=(Qp+Qm-2*Q0)/(2*h*h)
    rows.append({
      "step":h,
      "max_abs_Q1_direct_minus_recursion":float(np.max(np.abs(Q1direct-Q1rec))),
      "max_abs_Q2_direct_minus_recursion":float(np.max(np.abs(Q2direct-Q2rec))),
      "Q2_frobenius_norm":float(np.linalg.norm(Q2direct))
    })

result={
 "iteration":259,
 "model_readiness_percent":24,
 "frozen_convention":{"D":4,"Lambda":0,"deWitt_a":-0.5,"signature":"-+++","split":"g=eta+t eps exp(i q.x)","physical_inverse":"Q=N_orb^-1"},
 "identities":{"Q1":"-Q0*N1*Q0","Q2":"Q0*N1*Q0*N1*Q0-Q0*N2*Q0"},
 "finite_difference_validation":rows,
 "classification":"PASS_SCOPED_PHYSICAL_Q2_RECURSION_AND_DIRECT_INVERSE_VALIDATION",
 "guardrail":"NO_INDEPENDENT_Q2_ANSATZ",
 "candidate_residual":False,
 "heavy_run_authorized":False,
 "next_gate":260
}
assert np.max(np.abs(N0@Q0-np.eye(4)))<1e-13
assert rows[-1]["Q2_frobenius_norm"]>1.0
assert rows[-1]["max_abs_Q1_direct_minus_recursion"]<5e-8
assert rows[-1]["max_abs_Q2_direct_minus_recursion"]<1e-7
print(json.dumps(result,indent=2,sort_keys=True))
