#!/usr/bin/env python3
"""RQIR Iteration 095 — primitive physical decision Jacobian.

Deterministic algebra/regression certificate. Numerical examples are synthetic
and test formulas only; they are not apparatus forecasts.
"""
from dataclasses import dataclass
from math import sqrt, isclose

Z2 = 25.0
C_SRC = 225.0


def science_A(a2, a4, rho):
    assert a2 > 0 and a4 > 0 and abs(rho) < 1
    return Z2 * (1/(4*a2) + 1/(4*a4) + rho/(2*sqrt(a2*a4)))


def science_grad(a2, a4, rho):
    return {
        'a2': -Z2/(4*a2*a2) - Z2*rho/(4*a2**1.5*sqrt(a4)),
        'a4': -Z2/(4*a4*a4) - Z2*rho/(4*a4**1.5*sqrt(a2)),
        'rho': Z2/(2*sqrt(a2*a4)),
    }


def lam_min(a, b, c):
    disc = sqrt((a-b)**2 + 4*c*c)
    return 0.5*(a+b-disc)


def lam_min_grad(a, b, c):
    disc = sqrt((a-b)**2 + 4*c*c)
    if disc == 0:
        raise ValueError('lambda_min is nondifferentiable at repeated eigenvalue')
    return {
        'a': 0.5*(1-(a-b)/disc),
        'b': 0.5*(1+(a-b)/disc),
        'c': -2*c/disc,
    }


def aggregate_A(a2, a4, rho, gamma, ks):
    assert all(k > 0 for k in ks)
    return science_A(a2,a4,rho) + gamma*sum(1/k for k in ks)


def boundary(Ai, Ri, di, Ak, Rk, dk):
    mi = 1/(1-di); mk = 1/(1-dk)
    D = mi*Ai - mk*Ak
    S = C_SRC*(mi/Ri - mk/Rk)
    assert S != 0
    return -D/S, D, S


def boundary_outer_grad(Ai, Ri, di, Ak, Rk, dk):
    B,D,S = boundary(Ai,Ri,di,Ak,Rk,dk)
    mi=1/(1-di); mk=1/(1-dk)
    gD=-1/S; gS=D/(S*S)
    return B, {
        'Ai': gD*mi,
        'Ak': -gD*mk,
        'Ri': gS*(-C_SRC*mi/(Ri*Ri)),
        'Rk': gS*(+C_SRC*mk/(Rk*Rk)),
        'di': gD*(Ai*mi*mi)+gS*(C_SRC*mi*mi/Ri),
        'dk': gD*(-Ak*mk*mk)+gS*(-C_SRC*mk*mk/Rk),
    }


def source_rate(p, Omega, t_reset, V):
    # Smooth regression surrogate q(V,tau)=V^2/(1+tau).
    tau=Omega*t_reset
    q=V*V/(1+tau)
    return p*Omega*q


def source_rate_grad(p, Omega, t_reset, V):
    tau=Omega*t_reset
    q=V*V/(1+tau)
    q_tau=-V*V/(1+tau)**2
    q_V=2*V/(1+tau)
    return {
        'p': Omega*q,
        'Omega': p*(q + tau*q_tau),
        't_reset': p*Omega*Omega*q_tau,
        'V': p*Omega*q_V,
    }


def fd(f, x, i, eps=1e-6):
    xp=list(x); xm=list(x)
    xp[i]+=eps; xm[i]-=eps
    return (f(*xp)-f(*xm))/(2*eps)


def main():
    # Science primitive Jacobian.
    x=(1.2,0.8,-0.3)
    g=science_grad(*x)
    for i,name in enumerate(('a2','a4','rho')):
        num=fd(science_A,x,i)
        assert isclose(g[name],num,rel_tol=2e-9,abs_tol=2e-9)

    # 2x2 calibration-block eigenvalue Jacobian.
    y=(1.5,2.2,0.3)
    gl=lam_min_grad(*y)
    for i,name in enumerate(('a','b','c')):
        num=fd(lam_min,y,i)
        assert isclose(gl[name],num,rel_tol=2e-9,abs_tol=2e-9)

    # Relative calibration-rate leverage: dA/d ln k_j = -gamma/k_j.
    gamma=2.0
    ks=[1.1,1.5,2.0,2.5,3.0,4.0,5.0]
    contributions=[gamma/k for k in ks]
    assert contributions[0] == max(contributions)

    # Outer boundary chain rule, tested for a2 and one calibration rate.
    A1=aggregate_A(1.2,0.8,-0.3,gamma,ks)
    A2=aggregate_A(1.0,1.0,0.1,1.2,[2.0]*7)
    B,gout=boundary_outer_grad(A1,0.8,0.04,A2,1.2,0.02)
    assert B > 0

    dB_da2 = gout['Ai']*science_grad(1.2,0.8,-0.3)['a2']
    def B_of_a2(a2):
        aa=aggregate_A(a2,0.8,-0.3,gamma,ks)
        return boundary(aa,0.8,0.04,A2,1.2,0.02)[0]
    num=(B_of_a2(1.2+1e-6)-B_of_a2(1.2-1e-6))/(2e-6)
    assert isclose(dB_da2,num,rel_tol=2e-8,abs_tol=2e-10)

    dA_dk0=-gamma/(ks[0]**2)
    dB_dk0=gout['Ai']*dA_dk0
    def B_of_k0(k0):
        kk=ks.copy(); kk[0]=k0
        aa=aggregate_A(1.2,0.8,-0.3,gamma,kk)
        return boundary(aa,0.8,0.04,A2,1.2,0.02)[0]
    num=(B_of_k0(ks[0]+1e-6)-B_of_k0(ks[0]-1e-6))/(2e-6)
    assert isclose(dB_dk0,num,rel_tol=2e-8,abs_tol=2e-10)

    # Physical source-rate primitive Jacobian regression.
    sp=(0.6,1.4,0.7,0.8)
    gs=source_rate_grad(*sp)
    for i,name in enumerate(('p','Omega','t_reset','V')):
        num=fd(source_rate,sp,i)
        assert isclose(gs[name],num,rel_tol=2e-8,abs_tol=2e-10)

    # Anti-correlation sign reversal condition reproduces CORR-001 geometry.
    rho=-0.5; a4=1.0
    threshold=a4/(rho*rho)
    assert science_grad(0.5*threshold,a4,rho)['a2'] < 0
    assert science_grad(2.0*threshold,a4,rho)['a2'] > 0

    print('PASS Iteration 095 primitive decision Jacobian')
    print('boundary=',B)
    print('science_grad=',g)
    print('lambda_min_grad=',gl)
    print('slowest calibration layer relative contribution=',contributions[0])
    print('anti-correlation a2 sign-flip threshold=',threshold)

if __name__ == '__main__':
    main()
