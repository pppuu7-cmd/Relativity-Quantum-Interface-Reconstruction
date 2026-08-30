#!/usr/bin/env python3
"""RQIR Iteration 101 — same-state temporal f,2f calibration protocol.

Deterministic Paper-III engineering certificate.  It derives finite-window
cross-band covariance, robust rho/gain targets, and block-count requirements.
Numerical examples are protocol regressions, not apparatus forecasts.
"""
from __future__ import annotations

import math
import numpy as np


def rect_overlap(delta_f: float, T: float) -> complex:
    """Normalized white-noise covariance overlap of rectangular demodulators.

    (1/T) integral_0^T exp[-i 2 pi delta_f t] dt
      = exp[-i pi delta_f T] sinc(delta_f T),
    where numpy.sinc(x)=sin(pi x)/(pi x).
    """
    x = float(delta_f) * float(T)
    return np.exp(-1j * math.pi * x) * np.sinc(x)


def ar1_dft_correlation(N: int, a: float, k1: int, k2: int) -> complex:
    """Correlation of two DFT coefficients for a finite stationary AR(1) block."""
    assert N > 4 and 0 <= a < 1 and 0 < k1 < k2 < N // 2
    idx = np.arange(N)
    C = a ** np.abs(idx[:, None] - idx[None, :])
    t = np.arange(N)
    u1 = np.exp(-2j * np.pi * k1 * t / N) / math.sqrt(N)
    u2 = np.exp(-2j * np.pi * k2 * t / N) / math.sqrt(N)
    c12 = np.vdot(u1, C @ u2)
    v1 = float(np.real(np.vdot(u1, C @ u1)))
    v2 = float(np.real(np.vdot(u2, C @ u2)))
    return c12 / math.sqrt(v1 * v2)


def two_band_rate(r2: float, r4: float, rho: float) -> float:
    assert r2 > 0 and r4 > 0 and abs(rho) < 1
    return 4.0 * r2 * r4 / (r2 + r4 + 2.0 * rho * math.sqrt(r2 * r4))


def rho_upper_for_retention(r2: float, r4: float, rho0: float, q: float) -> float:
    """Largest rho_hi that retains fraction q of nominal two-band rate."""
    assert r2 > 0 and r4 > 0 and -1 < rho0 < 1 and 0 < q <= 1
    root = math.sqrt(r2 * r4)
    D0 = r2 + r4 + 2.0 * rho0 * root
    return (D0 / q - (r2 + r4)) / (2.0 * root)


def common_gain_error_for_retention(q: float) -> float:
    """Worst common fractional transfer-amplitude error for rate retention q.

    If both raw rates are conservatively scaled by (1-eps)^2 then R_beta has
    the same common scaling.
    """
    assert 0 < q <= 1
    return 1.0 - math.sqrt(q)


def blocks_for_rho_upper(rho0: float, rho_hi: float, z: float = 1.96) -> int:
    """Gaussian independent-block lower bound with marginal variances profiled.

    Per real bivariate Gaussian block the profiled Fisher for correlation is
    I_rho = 1/(1-rho^2)^2, hence sigma_rho=(1-rho^2)/sqrt(N).
    """
    assert -1 < rho0 < rho_hi < 1 and z > 0
    gap = rho_hi - rho0
    n = (z * (1.0 - rho0 * rho0) / gap) ** 2
    return int(math.ceil(n))


def injection_information_target(q: float, z: float = 1.96) -> float:
    """Required N*SNR_inj^2 for transfer-amplitude calibration.

    Parameter is fractional/log transfer amplitude with one-block Fisher equal
    to the declared injection SNR^2 in the matched calibration quadrature.
    """
    eps = common_gain_error_for_retention(q)
    assert eps > 0 and z > 0
    return (z / eps) ** 2


def blocks_for_injection_snr(q: float, snr_per_block: float, z: float = 1.96) -> int:
    assert snr_per_block > 0
    return int(math.ceil(injection_information_target(q, z) / (snr_per_block ** 2)))


def main():
    # DESIGN-011: exact white-noise orthogonality on an integer-cycle window.
    f = 100.0
    for M in (1, 2, 7, 100):
        T = M / f
        # separation between f and 2f is exactly f
        assert abs(rect_overlap(f, T)) < 2e-14

    # NG-054: orthogonal Fourier tones do not imply zero finite-block
    # correlation for colored stationary noise.
    c_white = ar1_dft_correlation(64, 0.0, 3, 6)
    c_col = ar1_dft_correlation(64, 0.8, 3, 6)
    assert abs(c_white) < 1e-12
    assert abs(c_col) > 0.03

    # RESOURCE-054/055 benchmark: balanced bands, nominal rho=0, retain 90%.
    q = 0.90
    rho_hi = rho_upper_for_retention(1.0, 1.0, 0.0, q)
    assert math.isclose(rho_hi, 1.0 / 9.0, rel_tol=1e-14)
    assert math.isclose(two_band_rate(1.0, 1.0, rho_hi) /
                        two_band_rate(1.0, 1.0, 0.0), q, rel_tol=1e-14)

    N_rho = blocks_for_rho_upper(0.0, rho_hi, 1.96)
    assert N_rho == 312

    eps_g = common_gain_error_for_retention(q)
    assert math.isclose(eps_g, 0.05131670194948623, rel_tol=1e-14)
    Iinj = injection_information_target(q, 1.96)
    assert 1458.7 < Iinj < 1458.9
    assert blocks_for_injection_snr(q, 10.0, 1.96) == 15
    assert blocks_for_injection_snr(q, 5.0, 1.96) == 59

    # Gosling's 3.3 ms block is used only as an external scale anchor: if an
    # RQIR-compatible protocol truly supplied independent Gaussian blocks, the
    # rho-only lower-bound integration corresponding to N=312 would be ~1.03 s.
    illustrative_block_s = 3.3e-3
    illustrative_time = N_rho * illustrative_block_s
    assert math.isclose(illustrative_time, 1.0296, rel_tol=1e-14)

    print('PASS Iteration 101 same-state f,2f calibration protocol')
    print('colored finite-block |corr| =', abs(c_col))
    print('90% balanced-rate rho upper =', rho_hi)
    print('95% rho block lower bound =', N_rho)
    print('90% common transfer amplitude error =', eps_g)
    print('95% required N*SNR_inj^2 =', Iinj)
    print('blocks at injection SNR 10 / 5 =',
          blocks_for_injection_snr(q, 10.0), blocks_for_injection_snr(q, 5.0))
    print('3.3 ms illustrative rho time [s] =', illustrative_time)


if __name__ == '__main__':
    main()
