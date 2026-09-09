"""RQIR apparatus joint-nuisance/covariance closure audit.

Purpose
-------
Close the statistical identifiability gap left explicit by the earlier
apparatus-certificate / specification / identifiability audits.  This file is a
model-agnostic Fisher audit, not a hardware forecast: no apparatus performance
numbers are assumed.

The science channel is linearised as

    mu = phi0 + theta * (1 + kappa) * g(t) + d1*t + d2*t**2,

where theta is the RQIR science amplitude, kappa a multiplicative scale-factor
uncertainty, phi0 a phase offset, and d1,d2 polynomial drift nuisances.
Time-correlated noise is represented by an AR(1) covariance only as a clean
positive-definite stress-test family.

Main structural result
----------------------
At kappa=0, dmu/dtheta = g and dmu/dkappa = theta*g.  Hence an unconstrained
scale factor is exactly collinear with the absolute science amplitude.  No
increase in sample count can remove this rank defect.  If kappa has an
independent Gaussian prior sigma_kappa, then after profiling offset/drifts and
all covariance structure,

    Var(theta) = 1/A + theta**2 * sigma_kappa**2,

where A is the nuisance-profiled statistical Fisher information for the signal
shape g.  The second term is therefore a calibration floor, not a numerical
artifact.

The correlated-noise stress test also shows why a scalar 'correlation penalty'
is insufficient: the same AR(1) correlation can hurt a slowly varying signal
while helping a reversal/alternating signal, because closure depends on spectral
alignment between the signal and the covariance eigenmodes.
"""
from __future__ import annotations

import math
import numpy as np


def ar1_covariance(n: int, rho: float, sigma: float = 1.0) -> np.ndarray:
    if not (-1.0 < rho < 1.0):
        raise ValueError("rho must satisfy |rho| < 1")
    idx = np.arange(n)
    return sigma**2 * rho ** np.abs(idx[:, None] - idx[None, :])


def signal_shape(n: int, kind: str) -> tuple[np.ndarray, np.ndarray]:
    t = np.linspace(-1.0, 1.0, n)
    if kind == "alternating":
        # Reversal-like high-frequency channel.
        g = np.where(np.arange(n) % 2 == 0, 1.0, -1.0)
    elif kind == "slow_sine":
        # Two cycles across the observation window: deliberately overlaps the
        # low-frequency region where positive AR(1) correlations are strongest.
        g = np.sin(4.0 * math.pi * np.arange(n) / n)
    else:
        raise ValueError(f"unknown signal kind: {kind}")
    return t, g


def profiled_signal_information(n: int, rho: float, kind: str) -> float:
    """Fisher information A after profiling phase offset + linear/quadratic drift."""
    t, g = signal_shape(n, kind)
    cov = ar1_covariance(n, rho)
    cinv = np.linalg.inv(cov)
    nuisance = np.column_stack([np.ones(n), t, t**2])

    f_nn = nuisance.T @ cinv @ nuisance
    f_gn = g @ cinv @ nuisance
    a_raw = float(g @ cinv @ g)
    a = a_raw - float(f_gn @ np.linalg.solve(f_nn, f_gn.T))
    if not a > 0.0:
        raise AssertionError("profiled signal information must remain positive")
    return a


def full_fisher(
    n: int,
    rho: float,
    kind: str,
    theta: float = 1.0,
    sigma_kappa: float | None = None,
) -> np.ndarray:
    """Joint Fisher for [theta, kappa, phi0, d1, d2]."""
    t, g = signal_shape(n, kind)
    cinv = np.linalg.inv(ar1_covariance(n, rho))

    # Linearise at kappa = 0.
    jac = np.column_stack([g, theta * g, np.ones(n), t, t**2])
    fisher = jac.T @ cinv @ jac
    if sigma_kappa is not None:
        if sigma_kappa <= 0.0:
            raise ValueError("sigma_kappa must be positive")
        fisher[1, 1] += 1.0 / sigma_kappa**2
    return fisher


def theta_sigma(
    n: int,
    rho: float,
    kind: str,
    sigma_kappa: float,
    theta: float = 1.0,
) -> float:
    fisher = full_fisher(n, rho, kind, theta=theta, sigma_kappa=sigma_kappa)
    covariance = np.linalg.inv(fisher)
    return math.sqrt(float(covariance[0, 0]))


def classify_resource_closure(
    n: int,
    rho: float,
    kind: str,
    sigma_kappa: float | None,
    target_sigma: float,
    theta: float = 1.0,
) -> str:
    """Classify an illustrative precision target without treating it as hardware input."""
    if sigma_kappa is None:
        return "NON_IDENTIFIABLE"

    calibration_floor = abs(theta) * sigma_kappa
    if calibration_floor >= target_sigma:
        return "CALIBRATION_LIMITED"

    sigma = theta_sigma(n, rho, kind, sigma_kappa, theta=theta)
    return "RESOURCE_CLOSED" if sigma <= target_sigma else "STATISTICALLY_LIMITED"


def structural_assertions() -> None:
    theta = 1.37
    n = 128
    rho = 0.7
    kind = "slow_sine"

    # Exact amplitude/scale collinearity without a scale prior.
    f_free = full_fisher(n, rho, kind, theta=theta, sigma_kappa=None)
    assert np.linalg.matrix_rank(f_free, tol=1e-9) < f_free.shape[0]

    # The calibration-floor identity must survive simultaneous profiling of
    # phase offset, drifts, and correlated covariance.
    a = profiled_signal_information(n, rho, kind)
    for sigma_kappa in [0.1, 0.03, 0.01, 0.003]:
        sigma_num = theta_sigma(n, rho, kind, sigma_kappa, theta=theta)
        sigma_exact = math.sqrt(1.0 / a + theta**2 * sigma_kappa**2)
        assert math.isclose(sigma_num, sigma_exact, rel_tol=1e-10, abs_tol=1e-12)


def covariance_geometry_assertions() -> None:
    # Positive AR(1) correlation is not universally a sensitivity penalty.
    # It hurts the slowly-varying channel but can help an alternating/reversal
    # channel relative to unit-marginal white noise, because their spectra differ.
    n = 256
    a_alt_white = profiled_signal_information(n, 0.0, "alternating")
    a_alt_corr = profiled_signal_information(n, 0.9, "alternating")
    a_slow_white = profiled_signal_information(n, 0.0, "slow_sine")
    a_slow_corr = profiled_signal_information(n, 0.9, "slow_sine")

    assert a_alt_corr > a_alt_white
    assert a_slow_corr < a_slow_white


def print_audit_table() -> None:
    print("RQIR joint nuisance/covariance audit")
    print("columns: N rho shape A_profile sigma_stat sigma_theta(k=0.03) class@target=0.05")
    for n in [64, 128, 256, 512]:
        for rho in [0.0, 0.5, 0.9]:
            for kind in ["alternating", "slow_sine"]:
                a = profiled_signal_information(n, rho, kind)
                sigma_stat = 1.0 / math.sqrt(a)
                sigma = theta_sigma(n, rho, kind, sigma_kappa=0.03)
                cls = classify_resource_closure(
                    n, rho, kind, sigma_kappa=0.03, target_sigma=0.05
                )
                print(
                    f"{n:4d} {rho:3.1f} {kind:11s} "
                    f"{a:12.6f} {sigma_stat:10.6f} {sigma:10.6f} {cls}"
                )

    # Demonstrate all three failure/closure classes with an illustrative target.
    target = 0.05
    assert classify_resource_closure(512, 0.0, "alternating", None, target) == "NON_IDENTIFIABLE"
    assert classify_resource_closure(512, 0.0, "alternating", 0.10, target) == "CALIBRATION_LIMITED"
    assert classify_resource_closure(64, 0.9, "slow_sine", 0.01, target) == "STATISTICALLY_LIMITED"
    assert classify_resource_closure(512, 0.9, "alternating", 0.01, target) == "RESOURCE_CLOSED"


def main() -> None:
    structural_assertions()
    covariance_geometry_assertions()
    print_audit_table()
    print("unconstrained scale-factor identifiability: FAIL (structural, expected)")
    print("finite scale-prior calibration-floor identity: PASS")
    print("phase/linear/quadratic drift simultaneous profiling: PASS")
    print("correlated-covariance spectral-geometry audit: PASS")
    print("resource-closure regime classifier: PASS")
    print("RQIR apparatus joint nuisance/covariance audit: PASS WITH EXPLICIT FAILURE DOMAIN")


if __name__ == "__main__":
    main()
