"""RQIR Iteration 048: explicit energy-basis source-metrology D2 phase diagram.

Iteration 047 supplied a concrete independent source-metrology channel with
fractional-amplitude Fisher per accepted plus-branch copy

    F_E_alpha = 0.00939188436411534.

Use the centered y_ref=-4, lambda=1 branch requirements already established:

    no added force-cov rows: C_alpha*=4.55511
    best4 force-cov rows:    C_alpha*=0.0500614386
    best5 force-cov rows:    C_alpha*=0

and covariance accepted-trajectory lower bounds from Iteration 040:

    best4 N4=1.180254e6
    best5 N5=2.135099543679e6.

Define the physical relative cycle-cost coordinate

    x_E = (p_C eta_C)/(p_E eta_E) * t_E/t_C,

so all wall times can be expressed in units t_C/(p_C eta_C):

    tau0 = N_E0 * x_E
    tau4 = N4 + N_E4 * x_E
    tau5 = N5.

This script derives the exact branch crossovers and the transparent 100-Hz
cycle-time thresholds. Common mean-calibration/control costs are omitted because
they are shared by the three compared branches; this is a local branch-choice
phase diagram, not the total experiment wall time.
"""
from __future__ import annotations

import math

F_E_ALPHA = 0.00939188436411534
C0 = 4.55511
C4 = 0.05006143859980483
N4 = 1.180254e6
N5 = 2.1350995436790087e6
TMAX = 4.99085067


def source_copies(c_alpha: float) -> float:
    return c_alpha / F_E_ALPHA


def normalized_times(x_e: float) -> tuple[float, float, float]:
    n0 = source_copies(C0)
    n4e = source_copies(C4)
    return n0 * x_e, N4 + n4e * x_e, N5


def branch_crossovers() -> tuple[float, float, float]:
    n0 = source_copies(C0)
    n4e = source_copies(C4)
    x04 = N4 / (n0 - n4e)
    x45 = (N5 - N4) / n4e
    x05 = N5 / n0
    return x04, x45, x05


def covariance_cycle_seconds(gap_hz: float, dead_s: float = 0.0) -> float:
    return TMAX / (2.0 * math.pi * gap_hz) + dead_s


def main() -> None:
    n0 = source_copies(C0)
    n4e = source_copies(C4)
    x04, x45, x05 = branch_crossovers()

    print("energy-basis copies no-force-cov", n0)
    print("energy-basis copies best4 residual", n4e)
    print("x_E crossovers 0-4,4-5,0-5", x04, x45, x05)

    assert abs(n0 - 485.00490672609175) < 2e-9
    assert abs(n4e - 5.330286943382775) < 2e-9
    assert abs(x04 - 2460.5304331812495) < 2e-9
    assert abs(x45 - 179135.8615063662) < 2e-7
    assert abs(x05 - 4402.2225632550435) < 2e-9

    # Verify actual lower-envelope branch ordering.
    for x, winner in [
        (100.0, 0),
        (x04 * 0.999, 0),
        (x04 * 1.001, 4),
        (1.0e4, 4),
        (x45 * 0.999, 4),
        (x45 * 1.001, 5),
        (1.0e6, 5),
    ]:
        t = normalized_times(x)
        got = (0, 4, 5)[min(range(3), key=lambda k: t[k])]
        print("x_E", x, "times", t, "winner", got)
        assert got == winner

    # Transparent equal-efficiency 100-Hz thresholds.
    for dead in (0.0, 1e-3):
        tc = covariance_cycle_seconds(100.0, dead)
        tE04 = x04 * tc
        tE45 = x45 * tc
        print("dead", dead, "tC", tc,
              "energy-cycle 0<->4 threshold s", tE04,
              "4<->5 threshold s", tE45)
        if dead == 0.0:
            assert abs(tE04 - 19.54444976653151) < 2e-12
            assert abs(tE45 - 1422.909385464864) < 2e-9
        else:
            assert abs(tE04 - 22.004980199712758) < 2e-12
            assert abs(tE45 - 1602.0452469712303) < 2e-9


if __name__ == "__main__":
    main()
