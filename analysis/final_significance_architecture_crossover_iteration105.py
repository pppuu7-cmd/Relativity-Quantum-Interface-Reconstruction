#!/usr/bin/env python3
"""RQIR Iteration 105 — final-significance Toy009/Toy014 rate crossover.

Algebraic certificate in compressed physical rates. Repository Toy014/Toy009
ratios are used only as regression slices unless a common apparatus supplies the
full detector+calibration effective-rate ratio.
"""
from math import sqrt, isclose


def final_rate(Rd,Ra):
    assert Rd>0 and Ra>0
    return 1.0/(1.0/sqrt(Rd)+1.0/sqrt(Ra))**2


def rate_ratio(u,v,z,delta=1.0):
    """Duty-adjusted Q14/Q09.

    u=Rd14/Rd09, v=Ra14/Ra09, z=Ra09/Rd09,
    delta=(1-d14)/(1-d09).
    """
    assert u>0 and v>0 and z>0 and delta>0
    num=1.0+1.0/sqrt(z)
    den=1.0/sqrt(u)+1.0/sqrt(v*z)
    return delta*(num/den)**2


def crossover_z(u,v,delta=1.0,tol=1e-14):
    """Return positive finite z crossing if it exists, else None."""
    sd=sqrt(delta); A=1.0/sqrt(u); B=1.0/sqrt(v)
    den=sd-B
    num=A-sd
    if abs(den)<tol:
        return None
    w=num/den
    if w<=0:
        return None
    return 1.0/(w*w)


def monotone_source_direction(u,v):
    """Sign of d sqrt(rate_ratio)/d w, w=1/sqrt(z)."""
    A=1.0/sqrt(u); B=1.0/sqrt(v)
    if abs(A-B)<1e-14: return 0
    return 1 if A>B else -1


def main():
    # Direct compression regression.
    Rd9=2.0; Ra9=0.5
    u=0.4; v=2.0
    Rd14=u*Rd9; Ra14=v*Ra9
    z=Ra9/Rd9
    direct=final_rate(Rd14,Ra14)/final_rate(Rd9,Ra9)
    assert isclose(direct,rate_ratio(u,v,z),rel_tol=1e-14)

    # Repository shared-kernel SCIENCE-ONLY regression slice.
    # This u is not yet the full physical detector+7cal RESOURCE-057 rate ratio.
    u_reg=0.2830146574583767  # 1/q_s Toy014/Toy009
    v_reg=1.4913343179877905  # zero-reset Ramsey source-rate ratio
    zc=crossover_z(u_reg,v_reg,1.0)
    assert zc is not None
    assert isclose(zc,0.042393961570158255,rel_tol=2e-14)
    assert isclose(rate_ratio(u_reg,v_reg,zc),1.0,rel_tol=3e-14)
    assert rate_ratio(u_reg,v_reg,0.5*zc)>1.0
    assert rate_ratio(u_reg,v_reg,2.0*zc)<1.0

    # Source-dominated systems favor the architecture with relatively better source rate
    # exactly when v>u.
    assert monotone_source_direction(u_reg,v_reg)==1
    assert monotone_source_direction(2.0,0.5)==-1
    assert monotone_source_direction(1.0,1.0)==0

    # Duty loss shifts the crossover toward a more source-dominated baseline.
    delta=(1.0-0.08)/(1.0-0.02)
    zc_duty=crossover_z(u_reg,v_reg,delta)
    assert zc_duty is not None
    assert isclose(zc_duty,0.027135455186203732,rel_tol=2e-14)
    assert zc_duty<zc

    # Final target scaling: architecture ranking is independent of Z if all rates
    # are local-linear and duty is multiplicative, because T=Z^2/Q.
    for Z in (3.0,5.0,8.0):
        T9=Z*Z/final_rate(Rd9,Ra9)
        T14=Z*Z/final_rate(Rd14,Ra14)
        assert isclose(T14/T9,1.0/direct,rel_tol=2e-14)

    print('PASS Iteration 105 final-significance architecture crossover')
    print('shared-kernel science-only regression u,v =',u_reg,v_reg)
    print('equal-duty crossover z=Ra09/Rd09 =',zc)
    print('with d09=0.02,d14=0.08 crossover z =',zc_duty)
    print('source-dominated direction sign =',monotone_source_direction(u_reg,v_reg))


if __name__=='__main__':
    main()
