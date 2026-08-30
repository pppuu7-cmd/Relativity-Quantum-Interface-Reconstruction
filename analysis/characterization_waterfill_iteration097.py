#!/usr/bin/env python3
"""RQIR Iteration 097 — optimal Fisher-limited characterization allocation.

The Iteration-094 leverage box is synthetic and used only as a deterministic
regression.  The water-filling law is general for the declared local separable
model W ~= const + sum_i c_i/sqrt(I_i0+R_i t_i).
"""
from math import isclose

LEVERAGE = {
    "14.Rsrc": 0.5191102104601385,
    "09.Rsrc": 0.4273712599258450,
    "14.A": 0.18109516727283034,
    "14.duty": 0.15899646329385492,
    "09.duty": 0.10243207461665434,
    "09.A": 0.035279501184403525,
}


def objective(channels, allocation):
    return sum(
        c / (I0 + R*allocation.get(name, 0.0))**0.5
        for name,c,R,I0 in channels
    )


def marginal(c, R, I):
    return c*R/(2.0*I**1.5)


def optimal_allocation(channels, total_time):
    """Exact KKT solution for no-floor independent Fisher accumulation."""
    assert total_time >= 0.0
    for _,c,R,I0 in channels:
        assert c > 0.0 and R > 0.0 and I0 > 0.0
    if total_time == 0.0:
        return 0.0, {name:0.0 for name,_,_,_ in channels}

    # t_i(lambda)=max(0,[ (c_i R_i/(2 lambda))^(2/3)-I_i0]/R_i ).
    def tsum(lam):
        out=0.0
        for _,c,R,I0 in channels:
            target=(c*R/(2.0*lam))**(2.0/3.0)
            out += max(0.0, (target-I0)/R)
        return out

    hi=max(marginal(c,R,I0) for _,c,R,I0 in channels)
    lo=0.0
    for _ in range(250):
        mid=0.5*(lo+hi)
        if mid == 0.0:
            mid=1e-300
        if tsum(mid) > total_time:
            lo=mid
        else:
            hi=mid
    lam=hi
    allocation={}
    for name,c,R,I0 in channels:
        target=(c*R/(2.0*lam))**(2.0/3.0)
        allocation[name]=max(0.0, (target-I0)/R)
    return lam, allocation


def main():
    # Normalize current h=1 and W=1 only for the regression, so c_i=Lambda_i
    # and I0=1. Equal characterization Fisher rates are not an apparatus claim.
    channels=[(name,lam,1.0,1.0) for name,lam in LEVERAGE.items()]

    lam01,a01=optimal_allocation(channels,0.1)
    assert isclose(sum(a01.values()),0.1,rel_tol=0,abs_tol=3e-14)
    assert a01["14.Rsrc"] > 0.099999999 and all(
        a01[k] < 1e-13 for k in a01 if k != "14.Rsrc"
    )

    lam1,a1=optimal_allocation(channels,1.0)
    assert isclose(sum(a1.values()),1.0,rel_tol=0,abs_tol=3e-13)
    assert a1["14.Rsrc"] > 0 and a1["09.Rsrc"] > 0
    assert all(a1[k] < 1e-12 for k in ("14.A","14.duty","09.duty","09.A"))

    lam3,a3=optimal_allocation(channels,3.0)
    assert isclose(sum(a3.values()),3.0,rel_tol=0,abs_tol=3e-12)
    assert a3["14.A"] > 0 and a3["14.duty"] > 0

    # KKT: every active channel has equal final marginal value lambda;
    # inactive channels have initial marginal <= lambda.
    for name,c,R,I0 in channels:
        t=a3[name]
        m=marginal(c,R,I0+R*t)
        if t > 1e-10:
            assert isclose(m,lam3,rel_tol=2e-12,abs_tol=2e-12)
        else:
            assert m <= lam3 + 2e-12

    # The optimum beats equal-time allocation for the same total budget.
    equal={name:3.0/len(channels) for name,_,_,_ in channels}
    assert objective(channels,a3) < objective(channels,equal)

    print("PASS Iteration 097 characterization water-filling")
    print("T=0.1 allocation",a01)
    print("T=1 allocation",a1)
    print("T=3 allocation",a3)
    print("KKT lambda(T=3)",lam3)
    print("objective optimum/equal",objective(channels,a3),objective(channels,equal))


if __name__ == "__main__":
    main()
