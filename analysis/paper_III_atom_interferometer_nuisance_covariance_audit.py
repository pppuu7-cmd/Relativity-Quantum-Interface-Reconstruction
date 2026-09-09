#!/usr/bin/env python3
"""Paper III sidecar — atom-interferometer nuisance/covariance closure audit.

This audit is intentionally separate from the authoritative Candidate-Gravity
iteration chain. It tests a generic atom-interferometer-like phase channel
with

    mu = phi0 + (1+kappa)*theta*g + d1*t + d2*t^2

under a full correlated covariance matrix. The target amplitude is theta;
kappa is a multiplicative apparatus scale error. Offset and polynomial drift
are profiled simultaneously.

The script demonstrates four structural facts:
  1. theta and kappa are exactly non-identifiable from science data alone;
  2. adding more science configurations with the same multiplicative scale
     does not remove that degeneracy;
  3. a finite scale prior produces the analytic calibration floor
         Var(theta) = 1/q + sigma_kappa^2  (theta=1);
  4. an independent known-reference calibration channel restores finite
     scale information, while lock-in modulation protects q against red noise
     and slow drift.

Numbers below are synthetic dimensionless audit coordinates, not a forecast
for any named apparatus.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

SIGMA_W = 0.35
SIGMA_C = 1.0
RHO = 0.92
THETA0 = 1.0
KAPPA0 = 0.0
SCALE_PRIOR_SIGMA = 0.02
CAL_REFERENCE_AMPLITUDE = 5.0


@dataclass(frozen=True)
class ProfileResult:
    n: int
    q_slow: float
    q_lockin: float
    lockin_gain: float
    sigma_stat_lockin: float
    sigma_total_scale_prior: float


def covariance(n: int) -> np.ndarray:
    """White + exponentially correlated component."""
    i = np.arange(n)
    return SIGMA_W**2 * np.eye(n) + SIGMA_C**2 * RHO ** np.abs(i[:, None] - i[None, :])


def nuisance_basis(n: int) -> tuple[np.ndarray, np.ndarray]:
    """Phase offset + linear drift + centered quadratic drift."""
    t = np.linspace(-1.0, 1.0, n)
    t2 = t * t - np.mean(t * t)
    return np.column_stack([np.ones(n), t, t2]), t


def signal(n: int, kind: str) -> np.ndarray:
    _, t = nuisance_basis(n)
    if kind == "slow":
        return np.sin(np.pi * t)
    if kind == "lockin":
        return (-1.0) ** np.arange(n)
    raise ValueError(kind)


def profiled_signal_information(g: np.ndarray, sigma: np.ndarray, basis: np.ndarray) -> float:
    """q = g^T Sigma^-1 P_perp g, profiling all additive nuisance columns."""
    solved = np.linalg.solve(sigma, np.column_stack([g, basis]))
    wg = solved[:, 0]
    wb = solved[:, 1:]
    btwb = basis.T @ wb
    correction = (g @ wb) @ np.linalg.solve(btwb, basis.T @ wg)
    q = float(g @ wg - correction)
    assert q > 0.0
    return q


def science_fisher(n: int, kind: str = "lockin", scale_prior_sigma: float | None = None) -> np.ndarray:
    sigma = covariance(n)
    basis, _ = nuisance_basis(n)
    g = signal(n, kind)
    # [theta, kappa, phi0, d1, d2]
    jac = np.column_stack([(1.0 + KAPPA0) * g, THETA0 * g, basis])
    solved = np.linalg.solve(sigma, jac)
    fisher = jac.T @ solved
    if scale_prior_sigma is not None:
        fisher[1, 1] += 1.0 / scale_prior_sigma**2
    return fisher


def profiled_theta_information(fisher: np.ndarray) -> float:
    """Schur complement for theta after profiling every nuisance parameter."""
    ftt = float(fisher[0, 0])
    ftn = fisher[0, 1:]
    fnn = fisher[1:, 1:]
    return float(ftt - ftn @ np.linalg.solve(fnn, ftn.T))


def two_configuration_fisher(n: int) -> np.ndarray:
    """Two science configurations sharing one theta and one unknown kappa.

    Each configuration gets its own offset and drift basis. The target and
    scale columns remain proportional globally, so the scale degeneracy is
    exact even though the signal shapes differ.
    """
    sigma1 = covariance(n)
    sigma2 = covariance(n)
    b1, _ = nuisance_basis(n)
    b2, _ = nuisance_basis(n)
    g1 = signal(n, "slow")
    g2 = signal(n, "lockin")

    zeros = np.zeros_like(b1)
    # params = theta, kappa, nuisance_cfg1(3), nuisance_cfg2(3)
    j1 = np.column_stack([g1, THETA0 * g1, b1, zeros])
    j2 = np.column_stack([g2, THETA0 * g2, zeros, b2])
    jac = np.vstack([j1, j2])

    sigma = np.block(
        [[sigma1, np.zeros_like(sigma1)], [np.zeros_like(sigma2), sigma2]]
    )
    return jac.T @ np.linalg.solve(sigma, jac)


def audit_grid() -> list[ProfileResult]:
    out: list[ProfileResult] = []
    p = 1.0 / SCALE_PRIOR_SIGMA**2
    for n in (64, 128, 256, 512):
        sigma = covariance(n)
        basis, _ = nuisance_basis(n)
        q_slow = profiled_signal_information(signal(n, "slow"), sigma, basis)
        q_lock = profiled_signal_information(signal(n, "lockin"), sigma, basis)
        sigma_stat = 1.0 / math.sqrt(q_lock)
        sigma_total = math.sqrt(1.0 / q_lock + 1.0 / p)
        out.append(
            ProfileResult(
                n=n,
                q_slow=q_slow,
                q_lockin=q_lock,
                lockin_gain=q_lock / q_slow,
                sigma_stat_lockin=sigma_stat,
                sigma_total_scale_prior=sigma_total,
            )
        )
    return out


def main() -> None:
    # Gate A: science-only target/scale degeneracy.
    f0 = science_fisher(128, "lockin", None)
    evals = np.linalg.eigvalsh(f0)
    rank = np.linalg.matrix_rank(f0, tol=1e-9)
    assert rank == f0.shape[0] - 1
    assert abs(evals[0]) < 1e-9 * evals[-1]
    assert np.allclose(f0[:, 0], f0[:, 1], rtol=1e-12, atol=1e-12)

    # Gate B: changing science configuration does not self-calibrate a common
    # multiplicative scale.
    f2 = two_configuration_fisher(64)
    rank2 = np.linalg.matrix_rank(f2, tol=1e-9)
    assert rank2 == f2.shape[0] - 1
    assert np.allclose(f2[:, 0], f2[:, 1], rtol=1e-12, atol=1e-12)

    # Gate C: finite scale prior matches the closed-form calibration floor.
    n = 128
    sigma = covariance(n)
    basis, _ = nuisance_basis(n)
    q = profiled_signal_information(signal(n, "lockin"), sigma, basis)
    fp = science_fisher(n, "lockin", SCALE_PRIOR_SIGMA)
    fprof = profiled_theta_information(fp)
    analytic = q / (1.0 + q * SCALE_PRIOR_SIGMA**2)
    assert math.isclose(fprof, analytic, rel_tol=1e-10, abs_tol=1e-10)
    var_numeric = 1.0 / fprof
    var_analytic = 1.0 / q + SCALE_PRIOR_SIGMA**2
    assert math.isclose(var_numeric, var_analytic, rel_tol=1e-10, abs_tol=1e-10)

    # Gate D: red-noise/drift overlap strongly favors lock-in modulation in this
    # synthetic covariance model.
    grid = audit_grid()
    assert all(r.lockin_gain > 100.0 for r in grid)

    # Gate E: resource closure has a hard calibration floor. With a 2% scale
    # prior, a 1% or 2% target precision is impossible from science shots alone.
    assert SCALE_PRIOR_SIGMA >= 0.01
    assert SCALE_PRIOR_SIGMA >= 0.02
    assert grid[-1].sigma_total_scale_prior < 0.03
    assert grid[-1].sigma_total_scale_prior > SCALE_PRIOR_SIGMA

    # Gate F: independent known-reference calibration breaks the degeneracy.
    # A_ref*g has d/dkappa = A_ref*g but no theta derivative.
    q_science = grid[-1].q_lockin
    q_cal = CAL_REFERENCE_AMPLITUDE**2 * q_science
    p_eff = 1.0 / SCALE_PRIOR_SIGMA**2 + q_cal
    sigma_scale_eff = 1.0 / math.sqrt(p_eff)
    sigma_theta_with_cal = math.sqrt(1.0 / q_science + 1.0 / p_eff)
    assert sigma_scale_eff < SCALE_PRIOR_SIGMA
    assert sigma_theta_with_cal < 0.02

    print("Paper III nuisance/covariance sidecar audit")
    print("science-only theta/kappa identifiability: NON_IDENTIFIABLE")
    print("two science configurations, same scale: NON_IDENTIFIABLE")
    print("finite scale prior calibration-floor identity: PASS")
    print("correlated-noise + offset/drift simultaneous profiling: PASS")
    print("independent known-reference scale calibration: IDENTIFIABLE")
    print()
    for r in grid:
        print(
            f"N={r.n:4d} "
            f"q_slow={r.q_slow:10.6f} "
            f"q_lockin={r.q_lockin:10.6f} "
            f"gain={r.lockin_gain:9.3f} "
            f"sigma_stat={r.sigma_stat_lockin:.6f} "
            f"sigma_with_2pct_scale={r.sigma_total_scale_prior:.6f}"
        )
    print()
    print(f"N=512 effective scale sigma after known-reference calibration: {sigma_scale_eff:.6f}")
    print(f"N=512 theta sigma after known-reference calibration: {sigma_theta_with_cal:.6f}")
    print("classification N=512, science only + 2% prior: CALIBRATION_LIMITED")
    print("classification target precision <=2%, science only: NO_FINITE_RESOURCE_CLOSURE")
    print("classification target precision 3%, N=512: FINITE_RESOURCE_CLOSURE")
    print("Paper III nuisance/covariance structural gate: PASS_WITH_CALIBRATION_REQUIREMENT")


if __name__ == "__main__":
    main()
