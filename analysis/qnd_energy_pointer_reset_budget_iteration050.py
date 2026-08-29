"""RQIR Iteration 050: reset-aware finite-strength QND energy metrology.

Extends Iteration 049 by adding an independent-source preparation/reset overhead
`t_reset` per attempted energy-metrology cycle.  With

    r = 2 sqrt(eta_E kappa_E T_E),
    delta = 4 eta_E kappa_E t_reset,

the accepted Fisher rate is

    R_E(r) = 4 p_E eta_E kappa_E F_alpha(r)/(r^2 + delta).

This script optimizes r for fixed dimensionless reset cost delta and maps the
result to the current D2 Branch0/best4/best5 Fisher-rate boundaries.
"""
from __future__ import annotations

import math
import numpy as np

import qnd_energy_pointer_fisher_iteration049 as i49

# Current centered y_ref=-4, lambda=1 requirements.
C0 = 4.55511
C4 = 0.05006143859980483
N4 = 1.180254e6
N5 = 2.1350995436790087e6
TMAX_100 = 0.00794318793930142
PC = 0.5
DEAD_C = 1e-3


def optimum_for_delta(delta: float, d: np.ndarray) -> tuple[float, float, float, float]:
    if delta < 0:
        raise ValueError("delta must be nonnegative")
    fproj = i49.projective_energy_fisher(+1.0, d)
    rstar, h = i49.golden_max(
        lambda r: i49.pointer_fisher(r, +1.0, d) / (r*r + delta),
        0.02, 10.0,
    )
    fstar = i49.pointer_fisher(rstar, +1.0, d)
    rate_coeff = 4.0 * h  # R_E = p_E eta_E kappa_E * rate_coeff
    return rstar, fstar, fstar / fproj, rate_coeff


def covariance_times() -> tuple[float, float]:
    tc = TMAX_100 + DEAD_C
    return N4 / PC * tc, N5 / PC * tc


def branch_rate_thresholds() -> tuple[float, float]:
    """Energy Fisher/s thresholds for lower-envelope branch changes."""
    t4, t5 = covariance_times()
    # Branch0 vs best4: extra source Fisher saved by best4 divided by t4.
    r04 = (C0 - C4) / t4
    # best4 vs best5: residual C4 divided by extra covariance wall time.
    r45 = C4 / (t5 - t4)
    return r04, r45


def main() -> None:
    d = i49.hidden_diagonal()
    r04, r45 = branch_rate_thresholds()
    t4, t5 = covariance_times()
    print("T4/T5 hours", t4/3600.0, t5/3600.0)
    print("energy Fisher-rate thresholds branch0-best4 / best4-best5", r04, r45)

    assert abs(t4/3600.0 - 5.86401852117) < 2e-9
    assert abs(t5/3600.0 - 10.6081091601) < 2e-9
    assert abs(r04 - 2.13403551447e-4) < 3e-15
    assert abs(r45 - 2.93121616447e-6) < 3e-17

    expected = {
        0.0: (0.86774652, 0.16576146, 0.00827009569),
        0.1: (0.98642121, 0.21160449, 0.00740844453),
        0.5: (1.26509475, 0.31997328, 0.00572283276),
        1.0: (1.47056190, 0.39776544, 0.00472500263),
        2.0: (1.72601495, 0.48844607, 0.00368532753),
        5.0: (2.16963681, 0.62542289, 0.00242039908),
        10.0: (2.58679779, 0.73098497, 0.00164522468),
        20.0: (3.03702076, 0.82024506, 0.00105444564),
        50.0: (3.65585910, 0.90438725, 0.00053618619),
    }

    for delta, exp in expected.items():
        rstar, fstar, frac, coeff = optimum_for_delta(delta, d)
        k04 = r04 / coeff  # threshold on p_E eta_E kappa_E
        k45 = r45 / coeff
        print("delta", delta, "r*", rstar, "Ffrac", frac,
              "R/(p eta kappa)", coeff,
              "p eta kappa thresholds", k04, k45)
        assert abs(rstar - exp[0]) < 4e-6
        assert abs(frac - exp[1]) < 4e-7
        assert abs(coeff - exp[2]) < 4e-10

    # Zero-reset reference from Iteration 049.
    r0, _f0, _frac0, c0 = optimum_for_delta(0.0, d)
    k04_0 = r04 / c0
    k45_0 = r45 / c0
    assert abs(k04_0 - 0.02580424212) < 3e-11
    assert abs(k45_0 - 0.0003544355804) < 3e-13
    print("zero-reset effective time scales", 1.0/k04_0, 1.0/k45_0)


if __name__ == "__main__":
    main()
