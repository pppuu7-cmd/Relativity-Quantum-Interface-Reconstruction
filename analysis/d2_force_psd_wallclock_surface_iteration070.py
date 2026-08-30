#!/usr/bin/env python3
"""RQIR Iteration 070: physical force-PSD wall-clock surface.

This script closes the next detector-resource gate after Iteration 069 without
pretending to forecast a specific laboratory apparatus. It uses a declared
white equivalent-force PSD benchmark for a same-time dual-probe layer and
expresses the result through the physical ratio r_F = F_sci/F_cal.

For a rectangular force template of duration T and one-sided white force PSD
S_F=A_F^2, matched-filter Fisher for one scalar channel is
    I = 2 F^2 T / S_F.
For a symmetric two-channel covariance C=[[1,rho],[rho,1]], the worst-mode
calibration Fisher is divided by (1+|rho|).

If science and calibration use the same cycle schedule / acceptance / PSD,
these common factors cancel from x=T_cal/T_sci, giving
    x = 7*gamma_mean*S_eff/Z^2 * (1+|rho|) * r_F^2.
This is a transparent benchmark surface, not an apparatus forecast.
"""

from math import sqrt

GAMMA_MEAN_009 = 1.830264703e6
S_EFF_009 = 5.7795071960e-4
Z = 5.0

# Iteration-066 Toy013-vs-Toy009 total-time boundary:
# x > A + B y, y=T_src009/T_sci009
A_BOUND = 25.8350584
B_BOUND = 376.305592


def x_ratio(r_f: float, rho: float) -> float:
    return (
        7.0
        * GAMMA_MEAN_009
        * S_EFF_009
        / Z**2
        * (1.0 + abs(rho))
        * r_f**2
    )


def y_critical(r_f: float, rho: float) -> float:
    """Largest y for which Toy013 can beat Toy009 at this benchmark x."""
    return (x_ratio(r_f, rho) - A_BOUND) / B_BOUND


def r_f_critical(y: float, rho: float) -> float:
    prefactor = 7.0 * GAMMA_MEAN_009 * S_EFF_009 / Z**2 * (1.0 + abs(rho))
    return sqrt((A_BOUND + B_BOUND * y) / prefactor)


def main() -> None:
    base = 7.0 * GAMMA_MEAN_009 * S_EFF_009 / Z**2
    print(f"base_x_prefactor_rho0_rF1 = {base:.12f}")

    for rho in (0.0, 0.5, 0.9):
        x = x_ratio(1.0, rho)
        yc = y_critical(1.0, rho)
        print(f"rho={rho:.1f} x(rF=1)={x:.12f} ycrit={yc:.12f}")

    for y in (0.0, 0.1, 1.0):
        vals = [r_f_critical(y, rho) for rho in (0.0, 0.5, 0.9)]
        print(
            f"y={y:.1f} rFcrit(rho=0,0.5,0.9)="
            + ",".join(f"{v:.12f}" for v in vals)
        )

    # Exact regression checks against hand-derived values.
    assert abs(base - 296.1847846040525) < 1e-9
    assert abs(y_critical(1.0, 0.0) - 0.7184313280256874) < 1e-9
    assert abs(y_critical(1.0, 0.5) - 1.111974223614723) < 1e-9
    assert abs(y_critical(1.0, 0.9) - 1.4268085400859514) < 1e-9


if __name__ == "__main__":
    main()
