#!/usr/bin/env python3
"""Paper III sidecar — differential atom-interferometer likelihood contract.

Purpose
-------
Connect the existing D1 binary-fringe normalization to a two-interferometer,
common-mode-noise likelihood without claiming a hardware forecast.

The regression checks:
  * exact Bernoulli fringe Fisher I_phi=C^2 at quadrature (Iteration-019 link);
  * common-mode correlated phase noise is suppressed by a differential signal;
  * separate phase offsets and linear/quadratic drifts can be profiled jointly;
  * a common multiplicative scale remains exactly degenerate with the absolute
    RQIR amplitude even after differential common-mode rejection;
  * a finite scale prior restores identifiability and produces the same hard
    calibration floor as the single-channel sidecar.

All phase/noise coordinates are SI-compatible radians/radian^2. Numerical noise
levels are synthetic stress-test values, not a named-apparatus forecast.
"""
from __future__ import annotations

import math
import numpy as np

CONTRAST = 0.66
SIGMA_INDEPENDENT_RAD = 1.0e-3
SIGMA_COMMON_RAD = 3.0e-3
RHO_COMMON = 0.95
SIGNAL_PHASE_RAD = 1.0e-3
SCALE_PRIOR_SIGMA = 0.02
THETA0 = 1.0


def bernoulli_fringe_fisher(contrast: float, phase: float) -> float:
    """Fisher information for phase in p=(1+C cos phi)/2."""
    p = 0.5 * (1.0 + contrast * math.cos(phase))
    dp = -0.5 * contrast * math.sin(phase)
    return dp * dp / (p * (1.0 - p))


def red_corr(n: int, rho: float) -> np.ndarray:
    i = np.arange(n)
    return rho ** np.abs(i[:, None] - i[None, :])


def nuisance_basis(n: int) -> np.ndarray:
    t = np.linspace(-1.0, 1.0, n)
    t2 = t * t - np.mean(t * t)
    return np.column_stack([np.ones(n), t, t2])


def profiled_q(g: np.ndarray, sigma: np.ndarray, b: np.ndarray) -> float:
    wg = np.linalg.solve(sigma, g)
    wb = np.linalg.solve(sigma, b)
    return float(g @ wg - (g @ wb) @ np.linalg.solve(b.T @ wb, b.T @ wg))


def single_channel(n: int):
    h = (-1.0) ** np.arange(n)
    r = red_corr(n, RHO_COMMON)
    sigma = (SIGMA_INDEPENDENT_RAD**2 * np.eye(n) +
             SIGMA_COMMON_RAD**2 * r)
    g = SIGNAL_PHASE_RAD * h
    b = nuisance_basis(n)
    return g, sigma, b, profiled_q(g, sigma, b)


def differential_channels(n: int):
    """Two simultaneous AIs with opposite science response and shared phase noise."""
    h = (-1.0) ** np.arange(n)
    r = red_corr(n, RHO_COMMON)
    s0 = SIGMA_INDEPENDENT_RAD**2 * np.eye(n) + SIGMA_COMMON_RAD**2 * r
    cross = SIGMA_COMMON_RAD**2 * r
    sigma = np.block([[s0, cross], [cross, s0]])

    # Opposite differential science response; common environmental phase is in Sigma.
    g = np.concatenate([SIGNAL_PHASE_RAD * h, -SIGNAL_PHASE_RAD * h])

    # Separate offset + linear + quadratic drift for each AI.
    b0 = nuisance_basis(n)
    z = np.zeros_like(b0)
    b = np.block([[b0, z], [z, b0]])
    q = profiled_q(g, sigma, b)
    return g, sigma, b, q


def full_fisher(n: int, scale_prior_sigma: float | None = None) -> np.ndarray:
    g, sigma, b, _ = differential_channels(n)
    # params [theta, kappa, nuisances...]; mu=(1+kappa)*theta*g+B eta
    jac = np.column_stack([g, THETA0 * g, b])
    fisher = jac.T @ np.linalg.solve(sigma, jac)
    if scale_prior_sigma is not None:
        fisher[1, 1] += 1.0 / scale_prior_sigma**2
    return fisher


def profiled_theta_information(f: np.ndarray) -> float:
    v = f[0, 1:]
    n = f[1:, 1:]
    return float(f[0, 0] - v @ np.linalg.solve(n, v.T))


def main() -> None:
    # Exact link to Iteration-019's local binary-fringe statement.
    i_quad = bernoulli_fringe_fisher(CONTRAST, math.pi / 2.0)
    assert math.isclose(i_quad, CONTRAST**2, rel_tol=0.0, abs_tol=1e-15)

    n = 64
    _, _, _, q_single = single_channel(n)
    _, _, _, q_diff = differential_channels(n)
    common_mode_gain = q_diff / q_single
    assert common_mode_gain > 1.0

    # Science-only target/scale degeneracy survives differential rejection.
    f0 = full_fisher(n, None)
    assert np.allclose(f0[:, 0], f0[:, 1], rtol=1e-12, atol=1e-12)
    assert np.linalg.matrix_rank(f0, tol=1e-8) == f0.shape[0] - 1

    # With a scale prior, the exact calibration-floor identity survives all
    # additive nuisance and the full common-mode covariance.
    fp = full_fisher(n, SCALE_PRIOR_SIGMA)
    fprof = profiled_theta_information(fp)
    analytic = q_diff / (1.0 + q_diff * SCALE_PRIOR_SIGMA**2)
    assert math.isclose(fprof, analytic, rel_tol=1e-10, abs_tol=1e-10)
    sigma_theta = 1.0 / math.sqrt(fprof)
    sigma_expected = math.sqrt(1.0 / q_diff + SCALE_PRIOR_SIGMA**2)
    assert math.isclose(sigma_theta, sigma_expected, rel_tol=1e-10, abs_tol=1e-10)

    print("Paper III differential atom-interferometer likelihood contract: PASS")
    print(f"Bernoulli fringe I_phi at quadrature = {i_quad:.12g} = C^2")
    print(f"single-channel profiled q            = {q_single:.12g}")
    print(f"differential profiled q              = {q_diff:.12g}")
    print(f"common-mode rejection information gain = {common_mode_gain:.12g}")
    print("science-only theta/common-scale      = NON_IDENTIFIABLE")
    print(f"theta sigma with 2% scale prior      = {sigma_theta:.12g}")
    print("classification: differential rejection helps correlated phase noise,"
          " but does not self-calibrate a free common multiplicative scale")


if __name__ == "__main__":
    main()
