"""RQIR Protocol 002B — physical scaling calculator.

Converts the normalized Toy 007/Protocol 002 two-harmonic response into a
simple matter-wave phase readout model.

Assumptions of this first scaling layer:
  * response difference after a weak pump is Delta B_n = 2 alpha H_n;
  * Newtonian potential is Phi = -(G m_s/L0) B;
  * the probe phase response uses one common effective interaction time T_D
    for n=2 and n=4;
  * equal phase-noise standard deviation sigma_phi per complex-harmonic
    quadrature;
  * static mean-potential calibration can use comparable interaction time.

These assumptions are deliberately idealized.  Frequency-dependent detector
transfer and colored covariance belong in Protocol 002C.
"""

from __future__ import annotations

import numpy as np

G = 6.67430e-11
HBAR = 1.054571817e-34

H2 = complex(-0.0002718331363764142, -0.007661385084133181)
H4 = complex(+0.0012094280337234182, -0.009061081550557511)
H24 = float(np.sqrt(abs(H2) ** 2 + abs(H4) ** 2))
KAPPA = float((abs(H4) ** 2 - abs(H2) ** 2) / (abs(H4) ** 2 + abs(H2) ** 2))
TILT_EFF = float(1.0 - KAPPA**2)
B_STATIC = 0.621539


def gamma_g(m_source: float, m_probe: float, t_det: float, length: float) -> float:
    return G * m_source * m_probe * t_det / (HBAR * length)


def response_snr(gamma: float, alpha: float, sigma_phi: float) -> float:
    return 2.0 * abs(alpha) * gamma * H24 / sigma_phi


def calibration_snr(gamma: float, sigma_cal: float) -> float:
    return gamma * B_STATIC / sigma_cal


def profile_info(rho_r: float, rho_c: float) -> float:
    s_eff = rho_r**2 * TILT_EFF
    c = rho_c**2
    return s_eff * c / (s_eff + c)


def strong_cal_gamma_required(z_target: float, alpha: float, sigma_phi: float) -> float:
    return z_target * sigma_phi / (2.0 * abs(alpha) * H24 * np.sqrt(TILT_EFF))


def mass_product_from_gamma(gamma: float, length: float, t_det: float) -> float:
    return gamma * HBAR * length / (G * t_det)


def main():
    alpha = 0.1
    length = 10e-6
    t_det = 1.0
    z_target = 5.0

    print("H24:", H24)
    print("kappa:", KAPPA)
    print("1-kappa^2:", TILT_EFF)
    print("static B0:", B_STATIC)
    print("rho_C/rho_R for equal phase noise and alpha=0.1:",
          B_STATIC / (2.0 * alpha * H24))

    print("\nsigma_phi gamma_req mass_product equal_mass")
    for sigma_phi in (1e-3, 1e-4, 1e-5, 1e-6):
        gamma_req = strong_cal_gamma_required(z_target, alpha, sigma_phi)
        product = mass_product_from_gamma(gamma_req, length, t_det)
        equal_mass = np.sqrt(product)
        print(sigma_phi, gamma_req, product, equal_mass)

    # Regression values for the benchmark stated in the document.
    gamma_req = strong_cal_gamma_required(5.0, 0.1, 1e-3)
    product = mass_product_from_gamma(gamma_req, 10e-6, 1.0)
    equal_mass = np.sqrt(product)
    assert abs(gamma_req - 2.1280081146) < 1e-9
    assert abs(product - 3.3623561782e-29) < 1e-39
    assert abs(equal_mass - 5.7985827391e-15) < 1e-24


if __name__ == "__main__":
    main()
