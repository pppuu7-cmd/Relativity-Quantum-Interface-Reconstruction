#!/usr/bin/env python3
"""RQIR Iteration 103 — full complex f,2f profile and campaign allocation.

Deterministic algebra/regression certificate. Synthetic matrices are used only
to verify the exact Fisher identities; they are not apparatus forecasts.
"""
from math import sqrt, isclose
import numpy as np


def profile_fisher(J):
    J=np.asarray(J,float)
    a=float(J[0,0]); b=J[0,1:]; N=J[1:,1:]
    q=np.linalg.solve(N,b)
    return float(a-b@q)


def efficient_direction(J):
    J=np.asarray(J,float)
    b=J[0,1:]; N=J[1:,1:]
    q=np.linalg.solve(N,b)
    return np.r_[1.0,-q]


def marginal_profile_rate(J,Jk):
    w=efficient_direction(J)
    return float(w@Jk@w)


def total_matrix(fractions,campaigns):
    return sum(float(x)*J for x,J in zip(fractions,campaigns))


def symmetric_gain_campaigns(m=8,c=8.0):
    """Science observes m channels beta+g_i; each calibration measures one g_i."""
    Js=np.zeros((m+1,m+1))
    Js[0,0]=m
    Js[0,1:]=1.0; Js[1:,0]=1.0
    Js[1:,1:]=np.eye(m)
    out=[Js]
    for i in range(m):
        K=np.zeros_like(Js); K[1+i,1+i]=c
        out.append(K)
    return out


def symmetric_optimum(m,c):
    d=sqrt(c/m)
    x_s=d/(1+d)
    x_each=1.0/(m*(1+d))
    fmax=c/(1+d)**2
    return x_s,x_each,fmax


def full_complex_regression():
    # Four real science components = Re/Im at f and 2f.
    s=np.array([1.0,0.2,0.8,-0.4])
    a2=np.array([s[0],s[1],0.0,0.0])
    p2=np.array([-s[1],s[0],0.0,0.0])
    a4=np.array([0.0,0.0,s[2],s[3]])
    p4=np.array([0.0,0.0,-s[3],s[2]])
    tilt=np.array([s[0],s[1],-s[2],-s[3]])

    W=np.array([
        [1.30,0.22,0.10,-0.04],
        [0.22,0.90,0.03,0.08],
        [0.10,0.03,1.10,-0.18],
        [-0.04,0.08,-0.18,1.00],
    ])
    assert np.linalg.eigvalsh(W).min()>0

    # Parameter order: beta, amp2, phase2, amp4, phase4, tilt.
    H=np.column_stack([s,a2,p2,a4,p4,tilt])
    Js=H.T@W@H

    # With free independent complex gains, beta is unidentifiable.
    a=float(Js[0,0]); b=Js[0,1:]; N=Js[1:,1:]
    ffree=float(a-b@np.linalg.pinv(N,rcond=1e-12)@b)
    assert abs(ffree)<2e-12

    # Same-state transfer injection constrains amplitude+phase gain coordinates.
    K=np.zeros((5,5))
    K[:4,:4]=np.diag([5.0,3.0,4.0,2.0])
    Jc=Js.copy(); Jc[1:,1:]+=K
    fcal=profile_fisher(Jc)
    assert fcal>1.9

    # Phase is Euclidean-orthogonal to amplitude for isotropic quadrature noise,
    # but not automatically Fisher-orthogonal under a general precision matrix.
    assert abs(s@np.eye(4)@p2)<1e-14
    assert abs(s@np.eye(4)@p4)<1e-14
    phase2_coupling=float(s@W@p2)
    phase4_coupling=float(s@W@p4)
    assert abs(phase2_coupling)>0.10
    assert abs(phase4_coupling)>0.03-1e-12
    return ffree,fcal,phase2_coupling,phase4_coupling


def main():
    # General derivative identity dF/dt_k = w^T J_k w.
    campaigns=symmetric_gain_campaigns(m=8,c=8.0)
    xs,xe,fmax=symmetric_optimum(8,8.0)
    frac=np.array([xs]+[xe]*8)
    J=total_matrix(frac,campaigns)
    F=profile_fisher(J)
    assert isclose(frac.sum(),1.0,rel_tol=0,abs_tol=1e-15)
    assert isclose(F,fmax,rel_tol=1e-13,abs_tol=1e-13)

    # KKT: every active campaign has the same marginal profiled Fisher rate.
    marg=np.array([marginal_profile_rate(J,K) for K in campaigns])
    assert np.max(np.abs(marg-F))<2e-12

    # Finite-difference derivative check for one campaign.
    eps=1e-7
    k=3
    Jp=J+eps*campaigns[k]
    Jm=J-eps*campaigns[k]
    fd=(profile_fisher(Jp)-profile_fisher(Jm))/(2*eps)
    assert isclose(fd,marg[k],rel_tol=2e-8,abs_tol=2e-9)

    # Positive homogeneity: target Fisher is obtained by scaling total time.
    Z2=25.0
    Tmin=Z2/F
    assert isclose(profile_fisher(Tmin*J),Z2,rel_tol=2e-13)
    assert isclose(Tmin,12.5,rel_tol=1e-14)

    # Concavity regression on two feasible positive allocations.
    x=np.array([0.40]+[0.60/8]*8)
    y=np.array([0.65]+[0.35/8]*8)
    lam=0.37
    Fx=profile_fisher(total_matrix(x,campaigns))
    Fy=profile_fisher(total_matrix(y,campaigns))
    Fm=profile_fisher(total_matrix(lam*x+(1-lam)*y,campaigns))
    assert Fm+1e-13>=lam*Fx+(1-lam)*Fy

    ffree,fcal,p2,p4=full_complex_regression()

    print('PASS Iteration 103 full complex campaign allocation')
    print('symmetric optimum fractions science/each-cal =',xs,xe)
    print('optimized profiled Fisher rate =',F,'Z=5 total time units =',Tmin)
    print('KKT marginal rates =',marg)
    print('full-complex free-gain Fisher =',ffree,'with transfer calibration =',fcal)
    print('phase couplings under non-isotropic W =',p2,p4)


if __name__=='__main__':
    main()
