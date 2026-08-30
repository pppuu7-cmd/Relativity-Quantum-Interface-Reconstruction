#!/usr/bin/env python3
"""RQIR Iteration 089 — joint robust total-time and source max-min certificate.

Deterministic regression only. No apparatus forecast.
"""
from __future__ import annotations
import math


def total_time_bounds(Z2, gamma, Csrc, Rbeta_rng, Rcal_rngs, Rsrc_rng, duty_rng):
    rb_lo, rb_hi = Rbeta_rng
    rs_lo, rs_hi = Rsrc_rng
    d_lo, d_hi = duty_rng
    if not (0 < rb_lo <= rb_hi and 0 < rs_lo <= rs_hi and 0 <= d_lo <= d_hi < 1):
        raise ValueError("invalid science/source/duty interval")
    if len(Rcal_rngs) != 7:
        raise ValueError("exactly seven calibration layers required")
    for lo, hi in Rcal_rngs:
        if not (0 < lo <= hi):
            raise ValueError("invalid calibration rate interval")

    payload_hi = Z2/rb_lo + gamma*sum(1/lo for lo, _ in Rcal_rngs) + Csrc/rs_lo
    payload_lo = Z2/rb_hi + gamma*sum(1/hi for _, hi in Rcal_rngs) + Csrc/rs_hi
    T_hi = payload_hi/(1-d_hi)
    T_lo = payload_lo/(1-d_lo)
    return T_lo, T_hi


def dominance_margin(bounds_i, bounds_k):
    """Positive iff i is robustly faster than k."""
    Ti_lo, Ti_hi = bounds_i
    Tk_lo, Tk_hi = bounds_k
    return Tk_lo - Ti_hi


def robust_design_rate(designs, uncertainties, rate_fn):
    """max_q min_u R(q,u): design chosen before uncertainty realization."""
    return max(min(rate_fn(q,u) for u in uncertainties) for q in designs)


def posthoc_rate(designs, uncertainties, rate_fn):
    """min_u max_q R(q,u): optimistic if q cannot adapt freely after u is known."""
    return min(max(rate_fn(q,u) for q in designs) for u in uncertainties)


def main():
    Z2 = 25.0
    Csrc = 225.0

    # Transparent synthetic architecture intervals; regression only.
    A = total_time_bounds(
        Z2, 100.0, Csrc,
        (0.8, 1.2),
        [(80.0,120.0)]*7,
        (8.0,12.0),
        (0.01,0.03),
    )
    B = total_time_bounds(
        Z2, 100.0, Csrc,
        (0.55,0.75),
        [(150.0,190.0)]*7,
        (14.0,18.0),
        (0.02,0.04),
    )
    print("A bounds", A)
    print("B bounds", B)
    print("A faster margin", dominance_margin(A,B))
    print("B faster margin", dominance_margin(B,A))

    # Direct corner enumeration regression for A: monotonic formula must have
    # extrema at slowest/fastest rate+duty endpoints.
    candidates=[]
    for rb in (0.8,1.2):
        for rc in (80.0,120.0):
            for rs in (8.0,12.0):
                for d in (0.01,0.03):
                    t=(Z2/rb + 100.0*7.0/rc + Csrc/rs)/(1-d)
                    candidates.append(t)
    assert math.isclose(min(candidates), A[0], rel_tol=1e-14)
    assert math.isclose(max(candidates), A[1], rel_tol=1e-14)

    # RQIR-NG-039 minimax regression. Positive rate proxy with design q and
    # uncertain optimum location u. A fixed design must use max min, not min max.
    designs=[-1.0 + 2.0*k/2000.0 for k in range(2001)]
    uncertainties=[-1.0,1.0]
    rate=lambda q,u: math.exp(-(q-u)**2)
    r_rob=robust_design_rate(designs, uncertainties, rate)
    r_post=posthoc_rate(designs, uncertainties, rate)
    assert math.isclose(r_rob, math.exp(-1.0), rel_tol=1e-14)
    assert math.isclose(r_post, 1.0, rel_tol=1e-14)
    assert r_rob <= r_post
    print("source max-min robust", r_rob)
    print("source min-max posthoc", r_post)

    print("PASS")


if __name__ == "__main__":
    main()
