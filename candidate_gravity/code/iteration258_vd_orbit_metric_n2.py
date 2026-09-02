#!/usr/bin/env python3
"""RQIR Iteration 258: physical same-parent second-order orbit-metric coefficient N2.

Frozen convention: D=4, Lambda=0, a=-1/2, eta=(-,+,+,+), linear covariant-metric split.
Uses the exact Iteration-252 factorization Nhat = W N_orb, hence N_orb = V Nhat with V=W^-1.
For a TT background g=eta+t eps exp(i q.x), V=(sqrt|g| g^-1)^-1=g/sqrt|g|.
The code evaluates the full minimal vector operator Nhat^alpha_beta=delta^alpha_beta Box+R^alpha_beta
on a finite-amplitude TT plane wave, extracts Nhat0,Nhat1,Nhat2 and directly verifies the second-order
coefficient identity N_orb,2 = V0 Nhat2 + V1 Nhat1 + V2 Nhat0.
"""
import json
import numpy as np

ETA=np.diag([-1.0,1.0,1.0,1.0])
K=np.array([0.2,0.6,0.3,0.1])
P=np.array([0.7,-0.4,0.5,0.9])
q=K[1:]
u=np.array([q[1],-q[0],0.0]); u/=np.linalg.norm(u)
v=np.cross(q,u); v/=np.linalg.norm(v)
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

N0=nhat(0.0); O0=norb(0.0)
H=ETA@EPS; trH2=float(np.trace(H@H))
V0=ETA.copy(); V1=EPS.copy(); V2=0.25*trH2*ETA
rows=[]
for h in [1e-2,3e-3,1e-3,3e-4,1e-4]:
    hp,hm=nhat(h),nhat(-h)
    H1=(hp-hm)/(2*h)
    H2=(hp+hm-2*N0)/(2*h*h)
    O2direct=(norb(h)+norb(-h)-2*O0)/(2*h*h)
    O2assembled=V0@H2+V1@H1+V2@N0
    rows.append({"step":h,"max_abs_Norb2_direct_minus_assembled":float(np.max(np.abs(O2direct-O2assembled))),"Norb2_frobenius_norm":float(np.linalg.norm(O2direct)),"Nhat2_frobenius_norm":float(np.linalg.norm(H2))})

result={
 "iteration":258,
 "model_readiness_percent":24,
 "frozen_convention":{"D":4,"Lambda":0,"deWitt_a":-0.5,"signature":"-+++","split":"g=eta+t eps exp(i q.x)","factorization":"Nhat=W N_orb; Q=N_orb^-1"},
 "tt_checks":{"trace":float(np.sum(ETA*EPS)),"transversality_max":float(np.max(np.abs((ETA@K)@EPS))),"tr_H2":trH2},
 "analytic_weight_inverse_coefficients":{"V0":"eta","V1":"eps","V2":"(tr(H^2)/4) eta"},
 "exact_second_order_identity":"Norb2 = V0*Nhat2 + V1*Nhat1 + V2*Nhat0",
 "finite_difference_validation":rows,
 "classification":"PASS_SCOPED_PHYSICAL_ORBIT_METRIC_N2_CONSTRUCTION_AND_DIRECT_VALIDATION",
 "guardrail":"NO_INDEPENDENT_NORB2_OR_Q2_ANSATZ; Q2 must follow Q0*N1*Q0*N1*Q0-Q0*N2*Q0",
 "candidate_residual":False,"heavy_run_authorized":False,"next_gate":259
}
assert abs(result["tt_checks"]["trace"])<1e-14
assert result["tt_checks"]["transversality_max"]<1e-14
assert rows[-1]["Norb2_frobenius_norm"]>1.0
assert rows[-1]["max_abs_Norb2_direct_minus_assembled"]<5e-8
print(json.dumps(result,indent=2,sort_keys=True))
