#!/usr/bin/env python3
"""RQIR Iteration 111 — parameterized pure-dead control-threshold surface.

No apparatus SI rates are invented. The script converts measurable scalar control
triples (R_ref, D, sigma_floor) into optimized recertification overheads using
RESOURCE-067, composes them exactly at wall-clock level, and derives architecture
break-even / robust interval conditions for u=R_D,14/R_D,09.
"""
from math import isclose, sqrt


def usable_variance(target_sigma, floor_sigma=0.0):
    S = target_sigma*target_sigma - floor_sigma*floor_sigma
    assert S > 0
    return S


def optimized_overhead(target_sigma, drift_D, R_ref, floor_sigma=0.0):
    """RESOURCE-067 minimum pure-dead overhead/live ratio."""
    S = usable_variance(target_sigma, floor_sigma)
    assert drift_D >= 0 and R_ref > 0
    return 2.0*drift_D/(R_ref*S*S)


def total_overhead(controls):
    """Sum non-overlapping pure-dead reference overheads per unit live time."""
    return sum(optimized_overhead(**c) for c in controls)


def wall_detector_ratio(u_live, H09, H14):
    """Exact detector-rate ratio after aggregate pure-dead recertification."""
    assert u_live > 0 and H09 >= 0 and H14 >= 0
    return u_live*(1.0+H09)/(1.0+H14)


def toy14_headroom(u_live, u_req, H09, H14_other=0.0):
    """Maximum overhead/live ratio available to one Toy014 control.

    Toy014 beats the detector threshold iff h14_j < K, where
    K = u_live(1+H09)/u_req - 1 - H14_other.
    """
    assert u_live > 0 and u_req > 0 and H09 >= 0 and H14_other >= 0
    return u_live*(1.0+H09)/u_req - 1.0 - H14_other


def required_toy14_reference_rate(target_sigma, drift_D, K, floor_sigma=0.0):
    """Minimum R_ref for one Toy014 control to fit inside decision headroom K."""
    S = usable_variance(target_sigma, floor_sigma)
    assert drift_D >= 0 and K > 0
    return 2.0*drift_D/(K*S*S)


def max_floor_variance(target_sigma, drift_D, R_ref, K):
    """Largest sigma_floor^2 compatible with a decision headroom K.

    From 2D/[R S^2] <= K => S >= sqrt(2D/(R K)).
    Returns sigma_floor,max^2. A negative value means no floor is admissible:
    even sigma_floor=0 cannot meet the threshold.
    """
    assert target_sigma > 0 and drift_D >= 0 and R_ref > 0 and K > 0
    required_S = sqrt(2.0*drift_D/(R_ref*K))
    return target_sigma*target_sigma - required_S


def robust_box_certificate(uL, uU, H09L, H09U, H14L, H14U, u_req):
    """Exact monotone interval certificate for independent boxes.

    lower = worst Toy014 wall ratio; upper = best Toy014 wall ratio.
    guaranteed=True means Toy014 wins everywhere in the box.
    impossible=True means Toy014 cannot win anywhere in the box.
    Otherwise the architecture is unresolved by the current box.
    """
    assert 0 < uL <= uU and 0 <= H09L <= H09U and 0 <= H14L <= H14U
    assert u_req > 0
    lower = wall_detector_ratio(uL,H09L,H14U)
    upper = wall_detector_ratio(uU,H09U,H14L)
    return lower, upper, lower > u_req, upper <= u_req


def main():
    # Exact composition regression: two controls with overheads .01 and .02.
    # Build those values from direct scalar inputs (sigma=1, D=h*R/2).
    c1=dict(target_sigma=1.0, drift_D=0.005, R_ref=1.0, floor_sigma=0.0)
    c2=dict(target_sigma=1.0, drift_D=0.010, R_ref=1.0, floor_sigma=0.0)
    H=total_overhead([c1,c2])
    assert isclose(H,0.03,rel_tol=1e-14)
    assert isclose(wall_detector_ratio(0.8,0.01,0.03),0.8*1.01/1.03,rel_tol=1e-14)

    # Decision-headroom regression.
    K=toy14_headroom(u_live=0.9,u_req=0.8,H09=0.01,H14_other=0.02)
    assert isclose(K,0.11625,rel_tol=1e-14)
    R=required_toy14_reference_rate(1.0,0.005,K)
    assert isclose(optimized_overhead(1.0,0.005,R),K,rel_tol=1e-12)

    # Floor boundary: at returned floor variance the overhead is exactly K.
    f2=max_floor_variance(1.0,0.005,R,K)
    assert abs(f2) < 1e-12  # this regression used the zero-floor threshold rate

    # Robust interval classification.
    lower,upper,guaranteed,impossible=robust_box_certificate(
        uL=0.90,uU=1.10,H09L=0.01,H09U=0.03,H14L=0.02,H14U=0.08,u_req=0.80)
    assert guaranteed and not impossible and lower > 0.80

    lower2,upper2,guaranteed2,impossible2=robust_box_certificate(
        uL=0.40,uU=0.50,H09L=0.0,H09U=0.01,H14L=0.0,H14U=0.02,u_req=0.80)
    assert impossible2 and not guaranteed2 and upper2 <= 0.80

    print('PASS Iteration 111 control-threshold surface')
    print('aggregate overhead H =',H)
    print('Toy014 example decision headroom K =',K)
    print('example threshold R_ref =',R)
    print('robust box 1 lower/upper =',lower,upper,'guaranteed=',guaranteed)
    print('robust box 2 lower/upper =',lower2,upper2,'impossible=',impossible2)


if __name__ == '__main__':
    main()
