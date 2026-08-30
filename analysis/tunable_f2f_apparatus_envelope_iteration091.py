"""RQIR Iteration 091 — tunable dual-mode f,2f apparatus design envelope.

This is an engineering/design-envelope calculation, not an apparatus forecast.
It combines the robust two-band science law (Iterations 085–087), seven-layer
calibration wall-clock law (088), and source/duty closure (089) in one common
physical Fisher-rate scale R0.
"""

from __future__ import annotations

import math
import random


def two_band_coefficient(a2: float, a4: float, rho: float) -> float:
    """Return s such that R_beta = R0*s when r2=R0*a2, r4=R0*a4."""
    if a2 <= 0 or a4 <= 0:
        raise ValueError("band coefficients must be positive")
    if not (-1.0 < rho < 1.0):
        raise ValueError("ordinary covariance requires |rho|<1")
    return 4.0 * a2 * a4 / (a2 + a4 + 2.0 * rho * math.sqrt(a2 * a4))


def detector_calibration_coefficient(
    z: float,
    gamma: float,
    a2: float,
    a4: float,
    rho_hi: float,
    k_cal: list[float],
) -> float:
    """A in T_pre-duty = A/R0 + C_src/R_src."""
    if any(k <= 0 for k in k_cal):
        raise ValueError("all robust calibration coefficients must be positive")
    s = two_band_coefficient(a2, a4, rho_hi)
    return z * z / s + gamma * sum(1.0 / k for k in k_cal)


def source_rate_floor(t_cap: float, c_src: float, duty_upper: float) -> float:
    """Strict source-rate feasibility floor in wall-clock Fisher/s."""
    if not (0 <= duty_upper < 1):
        raise ValueError("duty_upper must lie in [0,1)")
    m = 1.0 / (1.0 - duty_upper)
    return m * c_src / t_cap


def minimum_R0(
    t_cap: float,
    A: float,
    c_src: float,
    r_src: float,
    duty_upper: float,
) -> float:
    """Minimum common detector/calibration Fisher scale R0.

    T_upper = m*(A/R0 + C_src/R_src) <= T_cap.
    Returns +inf when the source channel alone consumes the full time cap.
    """
    m = 1.0 / (1.0 - duty_upper)
    remaining = t_cap - m * c_src / r_src
    if remaining <= 0:
        return math.inf
    return m * A / remaining


def total_time_upper(R0: float, A: float, c_src: float, r_src: float, duty_upper: float) -> float:
    m = 1.0 / (1.0 - duty_upper)
    return m * (A / R0 + c_src / r_src)


def dominance_threshold_R0(
    A_i: float,
    A_k: float,
    c_i: float,
    c_k: float,
    rsrc_i: float,
    rsrc_k: float,
) -> float:
    """Common-duty common-R0 crossing scale for T_i=T_k.

    Solves (A_i-A_k)/R0 = C_k/Rsrc_k - C_i/Rsrc_i.
    Positive finite output exists only when numerator and denominator have the
    same sign. Otherwise there is no positive crossing in this 1-D slice.
    """
    num = A_i - A_k
    den = c_k / rsrc_k - c_i / rsrc_i
    if den == 0 or num / den <= 0:
        return math.inf
    return num / den


def main() -> None:
    # Deterministic algebraic regressions.
    assert abs(two_band_coefficient(1.0, 1.0, 0.0) - 2.0) < 1e-14
    assert abs(two_band_coefficient(1.0, 1.0, 0.5) - (2.0 / 1.5)) < 1e-14

    # Common benchmark retained throughout the late resource front.
    z = 5.0
    c_src = 225.0
    t7 = 7.0 * 86400.0
    duty = 0.05

    # Transparent normalized design slice only: k_j=1 and equal raw band
    # coefficients. This is NOT a hardware forecast.
    k = [1.0] * 7
    gamma009 = 1.830264703e6
    gamma014 = 5.6776851e6
    A009 = detector_calibration_coefficient(z, gamma009, 1.0, 1.0, 0.0, k)
    A014 = detector_calibration_coefficient(z, gamma014, 1.0, 1.0, 0.0, k)

    floor = source_rate_floor(t7, c_src, duty)
    assert math.isinf(minimum_R0(t7, A009, c_src, floor, duty))

    # At ten times the source floor, source metrology consumes exactly 10% of
    # the time cap after duty inflation, leaving 90% for science+calibration.
    rsrc = 10.0 * floor
    R009 = minimum_R0(t7, A009, c_src, rsrc, duty)
    R014 = minimum_R0(t7, A014, c_src, rsrc, duty)
    assert abs(total_time_upper(R009, A009, c_src, rsrc, duty) - t7) < 1e-7
    assert abs(total_time_upper(R014, A014, c_src, rsrc, duty) - t7) < 1e-7

    # Shared-kernel Toy014/Toy009 regression from Iteration 074.
    qs = 3.53338589945
    qc = 3.48482822888
    qp = 0.67054046
    intercept = (qs - 1.0) / (1.0 - qp)
    slope = (qc - 1.0) / (1.0 - qp)
    assert abs(intercept - 7.6895205385) < 1e-9
    assert abs(slope - 7.5421347000) < 1e-9

    # Random regression: the analytic R0_min saturates the requested cap.
    rng = random.Random(20260830091)
    worst = 0.0
    for _ in range(1000):
        a2 = 10 ** rng.uniform(-1.0, 1.0)
        a4 = 10 ** rng.uniform(-1.0, 1.0)
        rho = rng.uniform(-0.8, 0.8)
        gamma = 10 ** rng.uniform(3.0, 7.0)
        ks = [10 ** rng.uniform(-1.0, 1.0) for _ in range(7)]
        cap = 10 ** rng.uniform(4.0, 7.0)
        d = rng.uniform(0.0, 0.2)
        C = 10 ** rng.uniform(0.0, 3.0)
        floor_i = source_rate_floor(cap, C, d)
        src = floor_i * rng.uniform(1.05, 20.0)
        A = detector_calibration_coefficient(5.0, gamma, a2, a4, rho, ks)
        R0 = minimum_R0(cap, A, C, src, d)
        err = abs(total_time_upper(R0, A, C, src, d) / cap - 1.0)
        worst = max(worst, err)
    assert worst < 1e-12

    print("RQIR Iteration 091 PASS")
    print(f"7-day, d=5% source feasibility floor = {floor:.12e} s^-1")
    print(f"normalized-slice A009 = {A009:.9e}")
    print(f"normalized-slice A014 = {A014:.9e}")
    print(f"at Rsrc=10x floor: R0_min(009) = {R009:.9e} s^-1")
    print(f"at Rsrc=10x floor: R0_min(014) = {R014:.9e} s^-1")
    print(f"shared-kernel Toy014/Toy009 boundary y > {intercept:.10f} + {slope:.10f} x")
    print(f"max random saturation relative error = {worst:.3e}")


if __name__ == "__main__":
    main()
