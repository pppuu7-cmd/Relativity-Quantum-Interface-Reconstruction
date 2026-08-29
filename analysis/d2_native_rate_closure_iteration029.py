"""RQIR Iteration 029: native-rate closure for the D2 resource phase diagram.

This script converts apparatus-level Fisher rates into the dimensionless
coordinates used in Iteration 028 without assuming equal calibration rates.

Definitions
-----------
q_pot   : Fisher rate [1/s] for one normalized potential-mean calibration row
q_force : Fisher rate [1/s] for one normalized force-gradient calibration row
q_cov   : Fisher rate [1/s] for one normalized covariance/log-PSD row
R_P     : independent source-preparation Fisher rate [1/s]

The corrected D2 row weights are GM=2.414e6 for each of 14 mean rows and
GC=0.929e6 for each of 8 covariance rows. Therefore

K_pot   = 14 GM / q_pot
K_force = 14 GM / q_force
K_cov   =  8 GC / q_cov

and the Iteration-028 coordinates become

x = K_force/K_pot = q_pot/q_force
y = K_cov/K_pot   = (8 GC)/(14 GM) * q_pot/q_cov
z = R_P K_pot     = 14 GM * R_P/q_pot.

No hardware sensitivity is asserted here. The point is to expose exactly which
native rate ratios must be supplied by one internally consistent D2 apparatus.
"""
from __future__ import annotations

GM = 2.414e6
GC = 0.929e6
N_MEAN = 14
N_COV = 8
FQ_A008 = 13.2707


def phase_coordinates(q_pot: float, q_force: float, q_cov: float, R_P: float):
    if min(q_pot, q_force, q_cov, R_P) <= 0:
        raise ValueError("all Fisher rates must be positive")
    K_pot = N_MEAN * GM / q_pot
    K_force = N_MEAN * GM / q_force
    K_cov = N_COV * GC / q_cov
    x = K_force / K_pot
    y = K_cov / K_pot
    z = R_P * K_pot
    return {
        "K_pot_s": K_pot,
        "K_force_s": K_force,
        "K_cov_s": K_cov,
        "x": x,
        "y": y,
        "z": z,
    }


def preparation_rate(p_accept: float, eta_qfi: float, cycle_s: float,
                     fq: float = FQ_A008) -> float:
    if not (0 < p_accept <= 1 and 0 < eta_qfi <= 1 and cycle_s > 0 and fq > 0):
        raise ValueError("invalid preparation parameters")
    return p_accept * eta_qfi * fq / cycle_s


def main():
    coeff_y = N_COV * GC / (N_MEAN * GM)
    coeff_z = N_MEAN * GM
    print("native-rate closure")
    print(f"y coefficient = {coeff_y:.12g}")
    print(f"z coefficient = {coeff_z:.12g}")
    print(f"z=1 occurs at R_P/q_pot = {1/coeff_z:.12g}")
    print(f"y=1 occurs at q_cov/q_pot = {coeff_y:.12g}")

    # Representative rate-ratio regimes. q_pot=1 merely fixes the time unit;
    # only ratios matter for x,y,z.
    cases = {
        "force-fast_prep-slow": (1.0, 10.0, 10.0, 1e-8),
        "force-fast_prep-fast": (1.0, 10.0, 10.0, 1e-6),
        "force-slow_prep-fast": (1.0, 0.1, 10.0, 1e-6),
        "equal-mean_broad-cov": (1.0, 1.0, 100.0, 1e-7),
    }
    for name, pars in cases.items():
        out = phase_coordinates(*pars)
        print(name, "x={x:.6g} y={y:.6g} z={z:.6g}".format(**out))

    # Regression guards for exact algebraic mapping.
    o = phase_coordinates(2.0, 4.0, 8.0, 3.0)
    assert abs(o["x"] - 0.5) < 1e-15
    assert abs(o["y"] - coeff_y * 0.25) < 1e-15
    assert abs(o["z"] - coeff_z * 1.5) < 1e-8


if __name__ == "__main__":
    main()
