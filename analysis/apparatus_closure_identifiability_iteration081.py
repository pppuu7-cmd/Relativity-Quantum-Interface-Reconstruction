"""RQIR Iteration 081 — apparatus-closure identifiability audit.

Demonstrates which absolute scale freedoms remain after the Iteration-077/080
rate certificates when detector PSD normalization and source-metrology rate are
not supplied by one declared apparatus.

No hardware performance values are assumed.
"""
from __future__ import annotations

import math

Z = 5.0
C_PREP = 225.0
GAMMA_009 = 1.830264703e6


def total_time(R_beta, R_cal, R_src, gamma=GAMMA_009, duty=0.0):
    """Seven equal-rate calibration layers, for a transparent scale audit."""
    m = 1.0 / (1.0 - duty)
    return m * (Z**2 / R_beta + 7.0 * gamma / R_cal + C_PREP / R_src)


def x_ratio(R_beta, R_cal, gamma=GAMMA_009):
    return gamma * R_beta / Z**2 * 7.0 / R_cal


def y_ratio(R_beta, R_src):
    return C_PREP * R_beta / (Z**2 * R_src)


def main():
    # Arbitrary reference rates are used only to prove scaling identities.
    # They are not apparatus forecasts.
    Rb0, Rc0, Rs0 = 2.0, 5.0, 7.0
    T0 = total_time(Rb0, Rc0, Rs0)
    x0, y0 = x_ratio(Rb0, Rc0), y_ratio(Rb0, Rs0)

    # Detector PSD normalization freedom: S -> lambda S makes all matched-filter
    # detector/calibration Fisher rates -> rates/lambda when transfer is fixed.
    # x is invariant, while absolute science+calibration time scales with lambda.
    for lam in [0.1, 1.0, 10.0, 100.0]:
        Rb = Rb0 / lam
        Rc = Rc0 / lam
        assert math.isclose(x_ratio(Rb, Rc), x0, rel_tol=1e-14, abs_tol=1e-14)
        detector_payload = Z**2 / Rb + 7.0 * GAMMA_009 / Rc
        detector_payload0 = Z**2 / Rb0 + 7.0 * GAMMA_009 / Rc0
        assert math.isclose(detector_payload / detector_payload0, lam, rel_tol=1e-14)

    # Source-rate freedom is independent of detector PSD unless a physical
    # source-metrology model supplies the coupling/reset/visibility.
    # Therefore y can be made arbitrarily large/small by changing R_src.
    ys = []
    for mu in [0.01, 0.1, 1.0, 10.0, 100.0]:
        ys.append(y_ratio(Rb0, Rs0 * mu))
    assert all(ys[i] > ys[i + 1] for i in range(len(ys) - 1))
    assert math.isclose(ys[0] / ys[-1], 1.0e4, rel_tol=1e-14)

    # A common scale applied to ALL three Fisher rates leaves x and y unchanged
    # but rescales the entire wall clock inversely. Hence (x,y,d) alone cannot
    # set absolute seconds without one absolute Fisher-rate normalization.
    for k in [0.2, 2.0, 20.0]:
        Tk = total_time(k * Rb0, k * Rc0, k * Rs0)
        assert math.isclose(Tk, T0 / k, rel_tol=1e-14)
        assert math.isclose(x_ratio(k * Rb0, k * Rc0), x0, rel_tol=1e-14)
        assert math.isclose(y_ratio(k * Rb0, k * Rs0), y0, rel_tol=1e-14)

    # Ramsey source-metrology zero-reset coefficient from the mature Toy009
    # front: R_src = coeff * p * Omega_E in that special limit. Without an
    # apparatus value of p*Omega_E (and with reset/visibility in the general
    # case), the absolute source Fisher rate is not fixed.
    coeff_ramsey_009 = 0.0025234392
    for pOmega in [1e-3, 1.0, 1e3]:
        rate = coeff_ramsey_009 * pOmega
        assert rate > 0.0

    print("reference x:", x0)
    print("reference y:", y0)
    print("PSD-scale invariance of x: PASS")
    print("absolute detector payload scale degeneracy: PASS")
    print("independent source-rate freedom: PASS")
    print("global Fisher-rate scale leaves (x,y) fixed but changes seconds: PASS")
    print("Iteration-081 apparatus-closure identifiability audit: PASS")


if __name__ == "__main__":
    main()
