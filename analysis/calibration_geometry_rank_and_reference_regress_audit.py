"""RQIR Paper III — calibration-geometry rank and reference-regress audit.

This audit extracts a model-independent apparatus design criterion from the
physical atom-interferometer example.

Suppose each independently measurable calibration channel c has, after
profiling additive nuisances/covariance, scalar Fisher weight I_c > 0 and a
fractional sensitivity vector e_c to m common calibration parameters. Then

    F_cal = sum_c I_c e_c e_c^T = E^T W E,

so

    rank(F_cal) = rank(span{e_c : I_c > 0}).

For two calibration parameters e_c=(p_c,q_c),

    det(F_cal)
      = sum_{i<j} I_i I_j (p_i q_j - q_i p_j)^2.

Thus merely adding more channels is insufficient: their sensitivity vectors
must span the calibration-parameter space. Near-collinear channels are
formally identifiable but ill-conditioned, so rank alone is not a sufficient
resource-closure metric.

The audit also proves a calibration-regress no-go for an injected reference.
If

    mu_j = K_j (1+gamma) [theta + alpha q_j]

and the reference amplitude alpha is itself unknown, then at gamma=0

    d_mu/d_gamma = theta d_mu/d_theta + alpha d_mu/d_alpha.

The gain gamma is therefore exactly non-identifiable jointly with theta and an
unconstrained reference amplitude, even when q_j is modulated and after any
linear nuisance/covariance projection. A reference only closes the gain if its
amplitude is independently calibrated, constrained by a prior, or linked to
another calibration channel with independent sensitivity geometry.
"""
from __future__ import annotations

import math
import numpy as np


def calibration_fisher(
    sensitivities: np.ndarray,
    information: np.ndarray,
    prior_precision: np.ndarray | None = None,
) -> np.ndarray:
    E = np.asarray(sensitivities, dtype=float)
    I = np.asarray(information, dtype=float)
    if E.ndim != 2:
        raise ValueError("sensitivities must be a channels x parameters matrix")
    if I.shape != (E.shape[0],):
        raise ValueError("information must have one value per channel")
    if np.any(I < 0.0):
        raise ValueError("information weights must be non-negative")
    F = E.T @ np.diag(I) @ E
    if prior_precision is not None:
        P = np.asarray(prior_precision, dtype=float)
        if P.shape != F.shape:
            raise ValueError("prior_precision has wrong shape")
        F = F + P
    return F


def determinant_pair_sum_2d(sensitivities: np.ndarray, information: np.ndarray) -> float:
    E = np.asarray(sensitivities, dtype=float)
    I = np.asarray(information, dtype=float)
    if E.ndim != 2 or E.shape[1] != 2:
        raise ValueError("requires 2D calibration sensitivity vectors")
    total = 0.0
    for i in range(E.shape[0]):
        for j in range(i + 1, E.shape[0]):
            cross = E[i, 0] * E[j, 1] - E[i, 1] * E[j, 0]
            total += I[i] * I[j] * cross**2
    return float(total)


def normalized_separation(e1: np.ndarray, e2: np.ndarray) -> float:
    """Absolute sine of the angle between two calibration sensitivity vectors."""
    a = np.asarray(e1, dtype=float)
    b = np.asarray(e2, dtype=float)
    if a.shape != (2,) or b.shape != (2,):
        raise ValueError("requires two 2D vectors")
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0.0:
        raise ValueError("zero sensitivity vector")
    return abs(float(a[0] * b[1] - a[1] * b[0])) / denom


def nuisance_projector(cov: np.ndarray, nuisance: np.ndarray) -> np.ndarray:
    Cinv = np.linalg.inv(cov)
    normal = nuisance.T @ Cinv @ nuisance
    return Cinv - Cinv @ nuisance @ np.linalg.solve(normal, nuisance.T @ Cinv)


def reference_columns(
    K: np.ndarray,
    q: np.ndarray,
    theta: float,
    alpha: float,
) -> np.ndarray:
    """Columns [theta, gamma_gain, alpha_reference] at gamma=0."""
    dtheta = K
    dalpha = K * q
    dgamma = K * (theta + alpha * q)
    return np.column_stack([dtheta, dgamma, dalpha])


def reference_regress_assertions() -> None:
    n = 96
    j = np.arange(n)
    K = np.where(j % 2 == 0, 1.0, -1.0) * np.where((j // 4) % 2 == 0, 1.0, 2.0)
    q = np.where((j // 8) % 2 == 0, 1.0, -1.0)
    theta = 0.23
    alpha = 0.41

    J = reference_columns(K, q, theta, alpha)

    # Exact algebraic dependence before projection.
    assert np.allclose(J[:, 1], theta * J[:, 0] + alpha * J[:, 2], rtol=0.0, atol=1e-14)
    assert np.linalg.matrix_rank(J, tol=1e-10) == 2

    # The same dependence survives simultaneous offset/linear/quadratic drift
    # profiling and correlated covariance weighting.
    t = np.linspace(-1.0, 1.0, n)
    nuisance = np.column_stack([np.ones(n), t, t**2])
    for rho in [0.0, 0.5, 0.9]:
        idx = np.arange(n)
        cov = rho ** np.abs(idx[:, None] - idx[None, :])
        P = nuisance_projector(cov, nuisance)
        F = J.T @ P @ J
        assert np.linalg.matrix_rank(F, tol=1e-9) == 2

        # If alpha is known, only [theta,gamma] remain and modulation makes them
        # independently identifiable.
        J_known = J[:, :2]
        F_known = J_known.T @ P @ J_known
        assert np.linalg.matrix_rank(F_known, tol=1e-9) == 2


def geometry_assertions() -> None:
    # Atom-interferometer leading exponent vectors:
    # acceleration-like k*T^2 and recoil-like k^2*T.
    E = np.array([[1.0, 2.0], [2.0, 1.0]])
    I = np.array([1.0, 1.0])
    F = calibration_fisher(E, I)
    assert np.linalg.matrix_rank(F, tol=1e-12) == 2
    assert math.isclose(np.linalg.det(F), 9.0, rel_tol=1e-12)
    assert math.isclose(
        np.linalg.det(F), determinant_pair_sum_2d(E, I), rel_tol=1e-12
    )
    assert math.isclose(normalized_separation(E[0], E[1]), 3.0 / 5.0, rel_tol=1e-14)

    # Equal-information acceleration+recoil geometry has eigenvalues 1 and 9.
    eig = np.linalg.eigvalsh(F)
    assert np.allclose(eig, [1.0, 9.0], rtol=1e-14, atol=1e-14)
    assert math.isclose(np.linalg.cond(F), 9.0, rel_tol=1e-12)

    # Extra channels with identical exponent ratio add information but not rank.
    same = np.array([[1.0, 2.0], [2.0, 4.0], [-0.5, -1.0]])
    F_same = calibration_fisher(same, np.array([1.0, 3.0, 5.0]))
    assert np.linalg.matrix_rank(F_same, tol=1e-12) == 1
    assert math.isclose(determinant_pair_sum_2d(same, np.ones(3)), 0.0, abs_tol=1e-14)

    # Cauchy-Binet pair-sum identity for multiple non-collinear channels.
    multi = np.array([[1.0, 2.0], [2.0, 1.0], [1.0, -1.0], [3.0, 0.5]])
    weights = np.array([0.7, 2.0, 0.4, 1.3])
    F_multi = calibration_fisher(multi, weights)
    assert math.isclose(
        np.linalg.det(F_multi),
        determinant_pair_sum_2d(multi, weights),
        rel_tol=1e-12,
        abs_tol=1e-12,
    )

    # Near-collinear channels are full rank but progressively ill-conditioned.
    condition_numbers = []
    determinants = []
    for eps in [0.5, 0.1, 0.02, 0.005]:
        near = np.array([[1.0, 2.0], [1.0 + eps, 2.0]])
        F_near = calibration_fisher(near, np.ones(2))
        assert np.linalg.matrix_rank(F_near, tol=1e-14) == 2
        determinants.append(float(np.linalg.det(F_near)))
        condition_numbers.append(float(np.linalg.cond(F_near)))
    assert all(determinants[i] > determinants[i + 1] for i in range(len(determinants) - 1))
    assert all(condition_numbers[i] < condition_numbers[i + 1] for i in range(len(condition_numbers) - 1))

    # A prior can make a rank-deficient Fisher invertible, but that is prior-
    # assisted closure rather than apparatus self-calibration.
    singular = calibration_fisher(np.array([[1.0, 2.0]]), np.array([10.0]))
    assert np.linalg.matrix_rank(singular, tol=1e-12) == 1
    regularized = calibration_fisher(
        np.array([[1.0, 2.0]]),
        np.array([10.0]),
        prior_precision=np.diag([0.0, 1.0]),
    )
    assert np.linalg.matrix_rank(regularized, tol=1e-12) == 2


def print_audit() -> None:
    accel = np.array([1.0, 2.0])
    recoil = np.array([2.0, 1.0])
    F = calibration_fisher(np.vstack([accel, recoil]), np.ones(2))
    print("RQIR calibration-geometry rank audit")
    print("rank(F_cal) = rank(span of positive-information sensitivity vectors): PASS")
    print("2D determinant pair-sum / Cauchy-Binet identity: PASS")
    print(f"acceleration/recoil normalized separation |sin alpha| = {normalized_separation(accel, recoil):.6f}")
    print(f"equal-information acceleration+recoil condition number = {np.linalg.cond(F):.6f}")
    print("same-ratio extra channels: RANK-DEFICIENT")
    print("near-collinear channels: FULL-RANK BUT ILL-CONDITIONED")
    print("unknown injected-reference amplitude: CALIBRATION REGRESS / NON_IDENTIFIABLE")
    print("known modulated-reference amplitude: COMBINED-GAIN IDENTIFIABLE")
    print("prior-restored rank: PRIOR-ASSISTED, NOT SELF-CALIBRATING")
    print("RQIR calibration geometry audit: PASS WITH EXPLICIT FAILURE DOMAINS")


def main() -> None:
    geometry_assertions()
    reference_regress_assertions()
    print_audit()


if __name__ == "__main__":
    main()
