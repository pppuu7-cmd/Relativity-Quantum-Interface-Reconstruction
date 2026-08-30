"""RQIR Iteration 084: simultaneous dual-band physical Fisher-rate closure.

This script derives/checks the two-band profiled science Fisher rate when both
RQIR harmonics are measured simultaneously with independent whitened band
information rates r2 and r4. It intentionally does not insert an apparatus ASD.

For P_n = r_n T and the retained antisymmetric spectral-tilt nuisance, the
profiled science information is

    F(T) = 4 P2 P4/(P2+P4) = R_2band T,
    R_2band = 4 r2 r4/(r2+r4).

The script also checks the inverse rate requirement for a target science time
and the colored-noise expression r_n = kappa_psd |DeltaF_n|^2/S_F,n.
"""
from __future__ import annotations

import math


def r_two_band(r2: float, r4: float) -> float:
    if r2 <= 0 or r4 <= 0:
        return 0.0
    return 4.0 * r2 * r4 / (r2 + r4)


def f_two_band(P2: float, P4: float) -> float:
    if P2 <= 0 or P4 <= 0:
        return 0.0
    return 4.0 * P2 * P4 / (P2 + P4)


def required_partner_rate(r2: float, R_target: float) -> float:
    """Minimum r4 at fixed r2 for R_2band >= R_target.

    Finite solution requires 4 r2 > R_target. This exposes the one-band
    bottleneck explicitly.
    """
    if r2 <= 0 or R_target <= 0 or 4.0 * r2 <= R_target:
        return math.inf
    return R_target * r2 / (4.0 * r2 - R_target)


def force_rate(delta_f: float, psd_force: float, kappa_psd: float = 1.0) -> float:
    """Band information-rate proxy with convention factor kept explicit."""
    if psd_force <= 0:
        raise ValueError("force PSD must be positive")
    return kappa_psd * delta_f * delta_f / psd_force


def main() -> None:
    # Exact time-scaling regression.
    r2, r4, T = 0.3, 0.7, 123.0
    lhs = f_two_band(r2*T, r4*T)
    rhs = r_two_band(r2, r4)*T
    assert abs(lhs-rhs) < 1e-12

    # Balanced case: profiling the antisymmetric tilt costs no information.
    r = 2.5
    assert abs(r_two_band(r, r) - 2.0*r) < 1e-14
    # Raw unprofiled total rate is r2+r4 = 2r, hence equality.

    # One useful band is insufficient.
    assert r_two_band(1.0, 0.0) == 0.0
    assert r_two_band(0.0, 1.0) == 0.0

    # Strong-band limit is controlled by the weak band: R -> 4 r_weak.
    weak = 0.2
    strong = 1e12
    assert abs(r_two_band(weak, strong)/(4*weak) - 1.0) < 1e-12

    # Inverse partner-rate law regression.
    target = 0.5
    fixed = 0.3
    partner = required_partner_rate(fixed, target)
    assert math.isfinite(partner)
    assert abs(r_two_band(fixed, partner) - target) < 1e-12
    assert math.isinf(required_partner_rate(target/4.0, target))

    # Explicit PSD scaling: common PSD multiplication by lambda rescales
    # the absolute two-band rate by 1/lambda, preserving normalized geometry.
    df2, df4 = 2.0, 3.0
    s2, s4 = 5.0, 7.0
    R0 = r_two_band(force_rate(df2, s2), force_rate(df4, s4))
    lam = 11.0
    R1 = r_two_band(force_rate(df2, lam*s2), force_rate(df4, lam*s4))
    assert abs(R1/R0 - 1.0/lam) < 1e-14

    # Example science-only target-rate floors, not apparatus forecasts.
    Z = 5.0
    for days in (1, 7, 30):
        Tcap = days*86400.0
        Rtarget = Z*Z/Tcap
        print(days, "days: required profiled science rate", Rtarget, "1/s")
        print(" balanced per-band rate", Rtarget/2.0, "1/s")

    print("PASS Iteration 084 simultaneous dual-band rate law")


if __name__ == "__main__":
    main()
