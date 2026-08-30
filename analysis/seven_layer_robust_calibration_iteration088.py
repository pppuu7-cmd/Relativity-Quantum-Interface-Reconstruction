#!/usr/bin/env python3
"""RQIR Iteration 088 — uncertainty-safe seven-layer calibration certificate.

Deterministic regression only. No apparatus forecast.
"""
from __future__ import annotations
import itertools
import math
import random


def lambda_min_2x2(a: float, b: float, c: float) -> float:
    """Smallest eigenvalue of [[a,c],[c,b]]."""
    return 0.5 * (a + b - math.sqrt((a - b) ** 2 + 4.0 * c * c))


def robust_box_lambda_min(a_rng, b_rng, c_rng):
    """Exact lower envelope over a PSD-safe independent entry box.

    lambda_min is concave on symmetric matrices, so a minimum over a box is
    attained at a vertex. We explicitly evaluate all eight vertices.
    """
    vals = []
    for a, b, c in itertools.product(a_rng, b_rng, c_rng):
        vals.append(((a, b, c), lambda_min_2x2(a, b, c)))
    worst = min(vals, key=lambda z: z[1])
    return worst, vals


def layer_rate_lower(a_rng, b_rng, c_rng, p_rng, tcyc_rng):
    (corner, i_lo), vals = robust_box_lambda_min(a_rng, b_rng, c_rng)
    if min(v for _, v in vals) <= 0:
        raise ValueError("entry box is not PSD-safe; positive rate cannot be certified")
    p_lo = min(p_rng)
    t_hi = max(tcyc_rng)
    return p_lo * i_lo / t_hi, i_lo, corner


def harmonic_mean_lower(rate_lowers):
    return len(rate_lowers) / sum(1.0 / r for r in rate_lowers)


def calibration_time_upper(gamma, rate_lowers):
    return gamma * sum(1.0 / r for r in rate_lowers)


def accepted_cycles_upper(gamma, info_per_accepted_lower):
    return gamma / info_per_accepted_lower


def expected_attempts_upper(gamma, info_per_accepted_lower, p_lower):
    return gamma / (info_per_accepted_lower * p_lower)


# Transparent synthetic regression boxes. They are dimensionless/per-cycle
# examples and must not be interpreted as detector measurements.
LAYERS = [
    ((7.2, 8.8), (8.1, 9.9), (-1.2, -0.8), (0.45, 0.55), (0.0085, 0.0095)),
    ((8.0,10.0), (7.5, 9.5), (-0.6, -0.2), (0.48, 0.58), (0.0080, 0.0090)),
    ((6.5, 7.5), (7.0, 8.0), ( 0.2,  0.6), (0.50, 0.60), (0.0075, 0.0085)),
    ((9.0,11.0), (8.0,10.0), ( 1.0,  1.5), (0.42, 0.52), (0.0090, 0.0100)),
    ((7.0, 8.0), (6.8, 7.8), (-0.4,  0.1), (0.46, 0.56), (0.0082, 0.0092)),
    ((8.5, 9.5), (9.0,10.0), ( 0.5,  1.0), (0.44, 0.54), (0.0088, 0.0098)),
    ((6.8, 7.8), (8.2, 9.2), (-1.0, -0.5), (0.49, 0.59), (0.0078, 0.0088)),
]


def main():
    rate_lowers = []
    info_lowers = []
    for j, (ar, br, cr, pr, tr) in enumerate(LAYERS, start=1):
        rate, info, corner = layer_rate_lower(ar, br, cr, pr, tr)
        rate_lowers.append(rate)
        info_lowers.append(info)
        print(f"layer {j}: lambda_min_lower={info:.15g}, rate_lower={rate:.15g} 1/s, corner={corner}")

    h_lo = harmonic_mean_lower(rate_lowers)
    print(f"H_cal_lower={h_lo:.15g} 1/s")

    # Numerical identity: gamma sum 1/R_j == 7 gamma/H_cal.
    for gamma in (1.0, 1.6292582380236194e6, 5.6776851e6):
        t1 = calibration_time_upper(gamma, rate_lowers)
        t2 = 7.0 * gamma / h_lo
        assert math.isclose(t1, t2, rel_tol=2e-15, abs_tol=1e-12)
        print(f"gamma={gamma:.15g}: T_cal_upper={t1:.15g} s")

    # Accepted-cycle/attempt bridge for layer 1.
    gamma_test = 1000.0
    p1_lo = LAYERS[0][3][0]
    n_acc = accepted_cycles_upper(gamma_test, info_lowers[0])
    n_try = expected_attempts_upper(gamma_test, info_lowers[0], p1_lo)
    assert n_try >= n_acc
    print(f"layer1 gamma=1000: accepted_cycles_upper={n_acc:.15g}, expected_attempts_upper={n_try:.15g}")

    # Concavity/corner regression: random interior matrices must never have
    # lambda_min below the eight-corner bound for PSD-safe boxes.
    rng = random.Random(20260830088)
    for _ in range(200):
        # Construct a comfortably PSD-safe box.
        a0 = rng.uniform(2.0, 10.0)
        b0 = rng.uniform(2.0, 10.0)
        da = rng.uniform(0.01, 0.2) * min(a0, b0)
        db = rng.uniform(0.01, 0.2) * min(a0, b0)
        cmax_safe = 0.45 * math.sqrt((a0-da) * (b0-db))
        c0 = rng.uniform(-0.5, 0.5) * cmax_safe
        dc = rng.uniform(0.01, 0.25) * cmax_safe
        ar = (a0-da, a0+da)
        br = (b0-db, b0+db)
        cr = (c0-dc, c0+dc)
        (corner, lo), vals = robust_box_lambda_min(ar, br, cr)
        if min(v for _, v in vals) <= 0:
            continue
        for _ in range(2000):
            a = rng.uniform(*ar); b = rng.uniform(*br); c = rng.uniform(*cr)
            assert lambda_min_2x2(a,b,c) >= lo - 2e-12

    # Non-PSD-safe box must fail certification.
    try:
        layer_rate_lower((1.0,1.1),(1.0,1.1),(1.2,1.3),(0.5,0.6),(0.01,0.02))
    except ValueError:
        pass
    else:
        raise AssertionError("expected non-PSD-safe box to fail")

    print("PASS")


if __name__ == "__main__":
    main()
