#!/usr/bin/env python3
"""RQIR Iteration 109 — control recertification Fisher envelope.

Derives the optimal trade between reference-estimation variance and Brownian
control drift for a scalar nuisance coordinate. Repository timing tolerances are
used as physical regression anchors; additive/geometry/gain coordinates remain
conditional until a common apparatus transduction is supplied.
"""
from math import isclose

# Physical timing tolerances retained in repository (microseconds).
SIG_T9_US = 9.190010830110957
SIG_T14_US = 3.97715

# Normalized additive tolerances retained only as conditional regression slices.
SIG_M9 = 7.39167814e-5
SIG_M14 = 4.19676208e-5
SIG_C9 = 1.30174869e-4
SIG_C14 = 6.06486956e-5


def optimized_reference(target_sigma, drift_D, R_ref, floor_sigma=0.0):
    """Minimum pure-dead reference overhead/live ratio for Brownian drift.

    Repository cadence convention: drift variance growth = D*t/2.
    A reference measured for time t_ref has variance 1/(R_ref*t_ref).
    Let S=target_sigma^2-floor_sigma^2>0. Optimizing the split between reference
    variance and allowed drift variance gives sigma_ref^2=S/2,
    t_ref=2/(R_ref*S), tau_live=S/D, and r_min=2D/(R_ref*S^2).
    """
    S = target_sigma*target_sigma - floor_sigma*floor_sigma
    assert S > 0 and drift_D > 0 and R_ref > 0
    sigma_ref2 = 0.5*S
    t_ref = 2.0/(R_ref*S)
    tau_live = S/drift_D
    r = t_ref/tau_live
    return sigma_ref2, t_ref, tau_live, r


def required_reference_rate(target_sigma, drift_D, r_max, floor_sigma=0.0):
    """Minimum Fisher rate needed to keep optimized overhead/live <= r_max."""
    S = target_sigma*target_sigma - floor_sigma*floor_sigma
    assert S > 0 and drift_D > 0 and r_max > 0
    return 2.0*drift_D/(r_max*S*S)


def same_coordinate_rate_ratio(sig9, sig14, floor9=0.0, floor14=0.0):
    """R_ref,14/R_ref,09 for equal drift D and equal overhead target.

    Only valid when sigmas refer to the same physical coordinate and Fisher
    normalization. Timing in seconds satisfies this; normalized additive rows do
    not yet, so those uses are explicitly conditional.
    """
    S9=sig9*sig9-floor9*floor9
    S14=sig14*sig14-floor14*floor14
    assert S9>0 and S14>0
    return (S9/S14)**2


def main():
    # Analytic optimum regression against direct split scan.
    sig=3.0; D=0.7; R=5.0
    sref2,tref,tau,r=optimized_reference(sig,D,R)
    assert isclose(sref2,4.5,rel_tol=1e-14)
    assert isclose(tref,2/(R*9),rel_tol=1e-14)
    assert isclose(tau,9/D,rel_tol=1e-14)
    assert isclose(r,2*D/(R*9**2),rel_tol=1e-14)

    # Physical timing comparison: same coordinate (microseconds), same D and
    # reference Fisher normalization. Units cancel in the ratio.
    rt=same_coordinate_rate_ratio(SIG_T9_US,SIG_T14_US)
    assert 28.50 < rt < 28.52

    # Conditional normalized-coordinate regressions only.
    rm=same_coordinate_rate_ratio(SIG_M9,SIG_M14)
    rc=same_coordinate_rate_ratio(SIG_C9,SIG_C14)
    assert 9.62 < rm < 9.63
    assert 21.22 < rc < 21.23

    # A floor can make the rate demand diverge as floor -> target.
    r0=required_reference_rate(1.0,1.0,0.01,0.0)
    r9=required_reference_rate(1.0,1.0,0.01,0.9)
    assert r9 > r0

    print('PASS Iteration 109 control recertification Fisher envelope')
    print('optimal reference variance fraction = 0.5 of available variance budget')
    print('timing Rref14/Rref09 same-D,same-overhead =',rt)
    print('conditional normalized additive mean/cov ratios =',rm,rc)
    print('example floor rate amplification =',r9/r0)

if __name__=='__main__':
    main()
