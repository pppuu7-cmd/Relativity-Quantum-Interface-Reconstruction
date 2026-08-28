"""RQIR Protocol 002 — two-harmonic profiled Fisher calculation.

Uses the accepted Toy 007 response harmonic coefficients at n=2 and n=4.
The minimal detector model has:

  beta : interface ordered-response transfer amplitude (parameter of interest)
  g    : common gravitational/detector amplitude nuisance, calibrated by an
         independent static mean-potential channel
  q    : antisymmetric relative spectral-tilt nuisance between harmonics
         (weights -1 for n=2, +1 for n=4)
  tau  : timing/phase-offset nuisance

Response data are the real and imaginary quadratures of both harmonics with
circular white Gaussian noise.  A separate scalar calibration datum constrains
g.  The script evaluates the exact local Fisher matrix and verifies the closed
form

  F_beta|nuis = S_eff C / (S_eff + C)
  S_eff = S (1-kappa^2)
  kappa = (|H4|^2-|H2|^2)/(|H4|^2+|H2|^2)

where S is the squared response SNR and C is the squared static-calibration SNR.

This is a normalized first statistical protocol, not yet an SI detector
forecast.
"""

from __future__ import annotations

import numpy as np


# Harmonic coefficients from analysis/protocol002_response_spectrum.py.
H2 = complex(-0.0002718331363764142, -0.007661385084133181)
H4 = complex(+0.0012094280337234182, -0.009061081550557511)


def c2r(z: np.ndarray) -> np.ndarray:
    """Stack complex channel amplitudes as Re,Im quadratures."""
    return np.ravel(np.column_stack([z.real, z.imag]))


def shape_parameters():
    h = np.array([H2, H4], dtype=complex)
    power = np.abs(h) ** 2
    s0 = float(np.sum(power))
    kappa = float((power[1] - power[0]) / s0)
    fractions = power / s0
    return h, s0, kappa, fractions


def fisher_matrix(rho_response: float, rho_calibration: float):
    """Return Fisher for parameters [beta, log_g, q, tau]."""
    h, s0, _, _ = shape_parameters()
    hn = h / np.sqrt(s0)
    n = np.array([2.0, 4.0])
    tilt = np.array([-1.0, +1.0])

    # Whitened response derivatives at beta=g=1, q=tau=0.
    d_beta_r = rho_response * c2r(hn)
    d_g_r = d_beta_r.copy()
    d_q_r = rho_response * c2r(tilt * hn)
    d_tau_r = rho_response * c2r(1j * n * hn)

    # Data vector: [static calibration, ReH2, ImH2, ReH4, ImH4].
    d_beta = np.r_[0.0, d_beta_r]
    d_g = np.r_[rho_calibration, d_g_r]
    d_q = np.r_[0.0, d_q_r]
    d_tau = np.r_[0.0, d_tau_r]

    j = np.column_stack([d_beta, d_g, d_q, d_tau])
    return j.T @ j


def profiled_beta_information(f: np.ndarray) -> float:
    fbb = float(f[0, 0])
    cross = f[0, 1:]
    nuisance = f[1:, 1:]
    value = fbb - cross @ np.linalg.pinv(nuisance, rcond=1e-13) @ cross
    return float(max(value, 0.0))


def closed_form(rho_response: float, rho_calibration: float) -> float:
    _, _, kappa, _ = shape_parameters()
    s = rho_response**2
    c = rho_calibration**2
    s_eff = s * (1.0 - kappa**2)
    return float(s_eff * c / (s_eff + c))


def main():
    h, s0, kappa, fractions = shape_parameters()
    print("H2:", H2, "|H2|:", abs(H2))
    print("H4:", H4, "|H4|:", abs(H4))
    print("two-harmonic norm:", np.sqrt(s0))
    print("power fractions n=2,n=4:", fractions)
    print("kappa:", kappa)
    print("1-kappa^2:", 1.0 - kappa**2)

    print("\nrho_R rho_C F_profile sqrt(F) closed_form")
    for rho_r, rho_c in [
        (1.0, 1.0),
        (3.0, 10.0),
        (10.0, 3.0),
        (10.0, 10.0),
        (10.0, 100.0),
        (100.0, 10.0),
    ]:
        f = fisher_matrix(rho_r, rho_c)
        prof = profiled_beta_information(f)
        exact = closed_form(rho_r, rho_c)
        print(rho_r, rho_c, prof, np.sqrt(prof), exact)
        assert abs(prof - exact) < 1e-9 * max(1.0, exact)

    # Single-harmonic comparison with the same unconstrained relative-tilt
    # nuisance: for one channel tilt is collinear with amplitude, so the
    # analogue has |kappa|=1 and zero effective response information.
    assert abs(kappa) < 1.0
    assert 1.0 - kappa**2 > 0.96


if __name__ == "__main__":
    main()
