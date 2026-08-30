#!/usr/bin/env python3
"""RQIR Iteration 107 — recertification-constrained campaign scheduling.

Deterministic algebra/regression only.  Timing numbers reproduced from the
retained Toy014 control benchmark are not apparatus forecasts.
"""
from __future__ import annotations

import math
import numpy as np


def profiled(J):
    J=np.asarray(J,float)
    a=float(J[0,0]); b=J[0,1:]; N=J[1:,1:]
    if len(b)==0:
        return a
    return float(a-b@np.linalg.solve(N,b))


def constrained_three_campaign(Js, Jc, Jr, ell_ref=0.0, n=801):
    """Grid regression over x_s+x_c+x_r=1, x_r>=ell_ref."""
    best=(-math.inf,None)
    for xr in np.linspace(ell_ref,1.0,n):
        rem=1.0-xr
        for xs in np.linspace(0.0,rem,n):
            xc=rem-xs
            f=profiled(xs*Js+xc*Jc+xr*Jr)
            if f>best[0]:
                best=(f,(float(xs),float(xc),float(xr)))
    return best


def pure_dead_reference_wallclock(Ftarget, Rlive, tau_live, t_ref):
    """Exact finite-campaign periodic-reference staircase.

    Convention: one reference block is required for every at-most tau_live of
    informative exposure, including the first interval.
    """
    assert Ftarget>0 and Rlive>0 and tau_live>0 and t_ref>=0
    L=Ftarget/Rlive
    n=max(1,math.ceil(L/tau_live))
    T=L+n*t_ref
    return L,n,T,Ftarget/T


def asymptotic_live_fraction(tau_live,t_ref):
    return tau_live/(tau_live+t_ref)


def main():
    # Science is exactly degenerate with one nuisance unless calibration exists.
    Js=np.array([[4.0,2.0],[2.0,1.0]])
    Jc=np.array([[0.0,0.0],[0.0,16.0]])
    # Mandatory reference also calibrates the nuisance, but more slowly.
    Jr=np.array([[0.0,0.0],[0.0,1.0]])

    f0,x0=constrained_three_campaign(Js,Jc,Jr,0.0,401)
    f10,x10=constrained_three_campaign(Js,Jc,Jr,0.10,401)
    assert x0[2] < 1e-15
    assert abs(x10[2]-0.10) < 1e-15
    assert f10 < f0
    assert 2.54 < f0 < 2.58
    assert 2.30 < f10 < 2.34

    # The feasible lower-bound constraint is linear and does not break
    # concavity of profiled Fisher over the campaign simplex.
    rng=np.random.default_rng(20260830107)
    for _ in range(200):
        x=rng.dirichlet(np.ones(3)); y=rng.dirichlet(np.ones(3)); lam=rng.random()
        Jx=x[0]*Js+x[1]*Jc+x[2]*Jr
        Jy=y[0]*Js+y[1]*Jc+y[2]*Jr
        Jm=lam*Jx+(1-lam)*Jy
        assert profiled(Jm)+1e-12 >= lam*profiled(Jx)+(1-lam)*profiled(Jy)

    # RESOURCE-065 finite periodic-reference regression.
    Ftarget=25.0; Rlive=0.1; tau=100.0; tref=2.0
    L,n,T,Q=pure_dead_reference_wallclock(Ftarget,Rlive,tau,tref)
    assert L==250.0 and n==3 and T==256.0
    assert abs(Q-25.0/256.0)<1e-15
    q_asym=Rlive*asymptotic_live_fraction(tau,tref)
    assert Q < Rlive and abs(q_asym-0.09803921568627451)<1e-15

    # Retained Toy014 timing-reference benchmark, explicitly illustrative.
    tref014=0.889
    tau_slow=0.2812*3600.0
    tau_fast=0.02812*3600.0
    d_slow=tref014/(tau_slow+tref014)
    d_fast=tref014/(tau_fast+tref014)
    assert abs(d_slow-0.0008774102875122507)<1e-15
    assert abs(d_fast-0.008705359328639556)<1e-15

    print('PASS Iteration 107 recertification-constrained schedule')
    print('unconstrained synthetic rate/fractions =',f0,x0)
    print('10% mandatory-reference rate/fractions =',f10,x10)
    print('finite cadence L,n,T,Q =',L,n,T,Q)
    print('asymptotic live-rate =',q_asym)
    print('Toy014 illustrative timing-reference duties =',d_slow,d_fast)


if __name__=='__main__':
    main()
