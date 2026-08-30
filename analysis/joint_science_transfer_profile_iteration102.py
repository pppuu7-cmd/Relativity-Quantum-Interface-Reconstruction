#!/usr/bin/env python3
"""RQIR Iteration 102 — joint science + injected-transfer profile.

Exact local Gaussian Fisher algebra for a two-band science likelihood with
multiplicative transfer-gain nuisances constrained by an independent injected
calibration campaign. Numerical examples are regression checks, not forecasts.
"""
from __future__ import annotations

import math
import numpy as np


def profiled_beta_transfer(s, W, D, C):
    """F_beta after profiling transfer nuisances.

    W is the science precision/Fisher metric including science exposure,
    D maps transfer nuisance coordinates into the science mean, and C is the
    independent injected-calibration Fisher matrix for those nuisances.
    """
    s=np.asarray(s,float)
    W=np.asarray(W,float)
    D=np.asarray(D,float)
    C=np.asarray(C,float)
    A=float(s @ W @ s)
    b=s @ W @ D
    G=D.T @ W @ D + C
    return float(A - b @ np.linalg.solve(G,b.T))


def balanced_profiled_fisher(r, c, T_sci, T_cal, rho):
    """Symmetric two-band slice with per-band raw rate r and gain-cal rate c."""
    assert r>0 and c>0 and T_sci>0 and T_cal>0 and abs(rho)<1
    return 2*c*r*T_cal*T_sci/(c*T_cal*(1+rho)+r*T_sci)


def effective_rates(r,c,rho):
    # Perfect-transfer science rate and common transfer-calibration rate.
    return 2*r/(1+rho), 2*c


def optimal_times_for_target(Fstar,r,c,rho):
    """Minimum separate science+calibration wall time in balanced slice."""
    assert Fstar>0
    Rs,Rc=effective_rates(r,c,rho)
    total=Fstar*(1/math.sqrt(Rs)+1/math.sqrt(Rc))**2
    ratio=math.sqrt(Rc/Rs)  # T_sci/T_cal
    Tcal=total/(1+ratio)
    Tsci=total-Tcal
    return Tsci,Tcal,total,Rs,Rc


def overhead_factor(Rs,Rc):
    """Total-time penalty relative to perfect transfer calibration."""
    assert Rs>0 and Rc>0
    return (1+math.sqrt(Rs/Rc))**2


def required_cal_rate_ratio(max_overhead_factor):
    """Minimum Rc/Rs to keep total penalty <= requested factor (>1)."""
    p=max_overhead_factor
    assert p>1
    return 1/(math.sqrt(p)-1)**2


def main():
    # General matrix structural gate: with two free per-band gains and no
    # independent calibration, the common amplitude direction is absorbed.
    rho=0.2
    Sigma=np.array([[1.0,rho],[rho,1.0]])
    W=np.linalg.inv(Sigma)
    s=np.array([1.0,1.0])
    D=np.eye(2)
    f0=profiled_beta_transfer(s,W,D,np.zeros((2,2)))
    assert abs(f0)<2e-14
    fstrong=profiled_beta_transfer(s,W,D,1e12*np.eye(2))
    fraw=float(s@W@s)
    assert math.isclose(fstrong,fraw,rel_tol=2e-12)

    # Exact balanced closed form against the general matrix formula.
    r=3.0; c=5.0; Ts=7.0; Tc=11.0; rho=-0.25
    Wscience=(r*Ts/(1-rho*rho))*np.array([[1,-rho],[-rho,1]])
    C=c*Tc*np.eye(2)
    fm=profiled_beta_transfer(np.ones(2),Wscience,np.eye(2),C)
    fc=balanced_profiled_fisher(r,c,Ts,Tc,rho)
    assert math.isclose(fm,fc,rel_tol=2e-14)

    # Harmonic form: 1/F = 1/(Rs Ts)+1/(Rc Tc).
    Rs,Rc=effective_rates(r,c,rho)
    assert math.isclose(1/fc,1/(Rs*Ts)+1/(Rc*Tc),rel_tol=2e-14)

    # Exact wall-clock optimum and numerical scan regression.
    Fstar=25.0
    Ts_opt,Tc_opt,Ttot,Rs,Rc=optimal_times_for_target(Fstar,r,c,rho)
    assert math.isclose(balanced_profiled_fisher(r,c,Ts_opt,Tc_opt,rho),Fstar,rel_tol=2e-14)
    assert math.isclose(Ts_opt/Tc_opt,math.sqrt(Rc/Rs),rel_tol=2e-14)

    # Scan along the exact constraint to verify the analytic minimum.
    vals=[]
    for Ts_try in np.geomspace(Fstar/Rs*1.0001, 1e4, 20000):
        rem=1/Fstar-1/(Rs*Ts_try)
        if rem>0:
            Tc_try=1/(Rc*rem)
            vals.append(Ts_try+Tc_try)
    assert min(vals) >= Ttot*(1-2e-7)

    # Practical calibration-speed thresholds.
    q10=required_cal_rate_ratio(1.10)
    q25=required_cal_rate_ratio(1.25)
    q2=required_cal_rate_ratio(2.0)
    assert 419<q10<421
    assert 71<q25<73
    assert 5.82<q2<5.84

    print('PASS Iteration 102 joint science-transfer profile')
    print('free-gain profiled Fisher =',f0)
    print('balanced Fisher =',fc)
    print('effective Rs,Rc =',Rs,Rc)
    print('optimal Ts,Tc,total =',Ts_opt,Tc_opt,Ttot)
    print('Rc/Rs for <=10%,25%,2x total penalty =',q10,q25,q2)


if __name__=='__main__':
    main()
