"""RQIR Iteration 121: physical rate-level detector bracket.

Combines science/common-gain transfer with seven mean calibration layers and
four-matching vs eight-separate covariance covers.  Symbolic/resource algebra;
no apparatus forecast and no new-physics claim.
"""
from __future__ import annotations

import math
import numpy as np


def dt_time(f_target: float, r_s: float, r_c: float) -> float:
    if min(f_target, r_s, r_c) <= 0:
        raise ValueError("positive target/rates required")
    return f_target * (1.0 / math.sqrt(r_s) + 1.0 / math.sqrt(r_c)) ** 2


def calibration_times(gm: float, mean_rates, gc: float, match_rates, sep_rates):
    mean_rates = np.asarray(mean_rates, float)
    match_rates = np.asarray(match_rates, float)
    sep_rates = np.asarray(sep_rates, float)
    if mean_rates.shape != (7,) or match_rates.shape != (4,) or sep_rates.shape != (8,):
        raise ValueError("expected 7 mean, 4 matching, 8 separate covariance rates")
    if np.min(mean_rates) <= 0 or np.min(match_rates) <= 0 or np.min(sep_rates) <= 0:
        raise ValueError("rates must be positive")
    tm = gm * float(np.sum(1.0 / mean_rates))
    tc_match = gc * float(np.sum(1.0 / match_rates))
    tc_sep = gc * float(np.sum(1.0 / sep_rates))
    return tm, tc_match, tc_sep


def detector_bounds(f_target: float, r_s: float, r_c: float,
                    gm: float, mean_rates, gc: float, match_rates, sep_rates):
    tdt = dt_time(f_target, r_s, r_c)
    tm, tcm, tcs = calibration_times(gm, mean_rates, gc, match_rates, sep_rates)
    # Absolute perfect-sharing lower bound, then two non-overlap branches.
    lower = max(tdt, tm, tcm)
    matching_no_share = tdt + tm + tcm
    conservative = tdt + tm + tcs
    assert lower <= matching_no_share <= conservative
    return lower, matching_no_share, conservative


def u_interval(bounds09, bounds14):
    l9, _m9, u9 = bounds09
    l14, _m14, u14 = bounds14
    # u=R_D14/R_D09=T09/T14 at fixed final Fisher target.
    return l9 / u14, u9 / l14


def main() -> None:
    # Regression with deliberately dimensionless positive rates.
    f = 25.0
    s14 = 0.2830146574583767
    b9 = detector_bounds(
        f, 1.0, 1.0,
        1.830264703e6, np.full(7, 9.0),
        5.901272925e5, np.ones(4), np.ones(8),
    )
    b14 = detector_bounds(
        f, s14, 1.0,
        5.6776851e6, np.full(7, 9.0),
        2.7186736e6, np.ones(4), np.ones(8),
    )
    ui = u_interval(b9, b14)
    print("Toy009 regression bounds", b9)
    print("Toy014 regression bounds", b14)
    print("u interval", ui)
    assert 0 < ui[0] <= ui[1]

    # Exact homogeneous scaling: multiplying every detector-side rate by k
    # divides every time bound by k and leaves the architecture ratio interval unchanged.
    k = 17.0
    b9k = detector_bounds(
        f, k, k,
        1.830264703e6, np.full(7, 9.0 * k),
        5.901272925e5, np.ones(4) * k, np.ones(8) * k,
    )
    b14k = detector_bounds(
        f, s14 * k, k,
        5.6776851e6, np.full(7, 9.0 * k),
        2.7186736e6, np.ones(4) * k, np.ones(8) * k,
    )
    for a, b in zip(b9k, b9):
        assert abs(a - b / k) / max(1.0, abs(b/k)) < 1e-12
    for a, b in zip(b14k, b14):
        assert abs(a - b / k) / max(1.0, abs(b/k)) < 1e-12
    ui_k = u_interval(b9k, b14k)
    assert max(abs(ui_k[i]-ui[i]) for i in range(2)) < 1e-12

    # NG-030-style decision guard.
    if ui[0] > 1.0:
        decision = "Toy014 detector-side robust advantage"
    elif ui[1] < 1.0:
        decision = "Toy014 detector-side robust disadvantage"
    else:
        decision = "detector-side unresolved"
    print("decision", decision)


if __name__ == "__main__":
    main()
