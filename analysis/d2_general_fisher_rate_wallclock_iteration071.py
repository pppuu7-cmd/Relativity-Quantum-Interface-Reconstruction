#!/usr/bin/env python3
"""RQIR Iteration 071: general D2 Fisher-rate / wall-clock closure.

No apparatus forecast is made. The script verifies the structural rate formulas and
regresses to the Iteration-070 common-PSD/common-schedule reference surface.
"""
from math import isclose

GAMMA_MEAN_009 = 1.830264703e6
S_EFF_009 = 5.7795071960e-4
Z = 5.0
N_LAYERS = 7


def science_time(R_beta: float, z: float = Z) -> float:
    return z*z/R_beta


def calibration_time(gamma: float, rates) -> float:
    return gamma*sum(1.0/r for r in rates)


def source_time(C_prep: float, R_src: float) -> float:
    return C_prep/R_src


def normalized_budget(R_beta: float, rates_cal, gamma: float,
                      C_prep: float, R_src: float, z: float = Z):
    T_sci = science_time(R_beta, z)
    T_cal = calibration_time(gamma, rates_cal)
    T_src = source_time(C_prep, R_src)
    return {
        "T_sci": T_sci,
        "T_cal": T_cal,
        "T_src": T_src,
        "x": T_cal/T_sci,
        "y": T_src/T_sci,
        "total_over_science": (T_sci+T_cal+T_src)/T_sci,
    }


def cprep_for_retained_fraction(r: float, Fraw_required: float) -> float:
    # Schur-complement amplitude-prior requirement for multiplicative beta*alpha.
    return (r/(1.0-r))*Fraw_required


def iteration070_x(rho: float, r_F: float) -> float:
    return (N_LAYERS*GAMMA_MEAN_009*S_EFF_009/Z**2
            * (1.0+abs(rho))*r_F*r_F)


def main():
    pref = N_LAYERS*GAMMA_MEAN_009*S_EFF_009/Z**2
    assert isclose(pref, 296.1847846040525, rel_tol=2e-15)

    # Regression of Iteration 070.
    for rho, expected in [(0.0, 296.1847846040525),
                          (0.5, 444.2771769060788),
                          (0.9, 562.7510907476998)]:
        assert isclose(iteration070_x(rho, 1.0), expected, rel_tol=2e-12)

    # Source-metrology bridge for r=0.90 and Z=5 => C_prep=225.
    C = cprep_for_retained_fraction(0.90, Z**2)
    assert isclose(C, 225.0, rel_tol=1e-15)

    print("RQIR Iteration 071 — general Fisher-rate wall-clock closure")
    print(f"Iteration-070 regression prefactor = {pref:.12f}")
    print("General independent-campaign formulas:")
    print("  T_sci = Z^2 / R_beta")
    print("  T_cal = gamma * sum_j (1/R_cal,j)")
    print("  T_src = C_prep / R_src")
    print("  x = gamma*R_beta/Z^2 * sum_j(1/R_cal,j)")
    print("  y = C_prep*R_beta/(Z^2*R_src)")
    print("For retained fraction r with Fraw=Z^2:")
    print("  C_prep = [r/(1-r)] Z^2, hence y = [r/(1-r)] R_beta/R_src")
    print(f"At r=0.90: C_prep={C:.12g}, y=9*R_beta/R_src")


if __name__ == "__main__":
    main()
