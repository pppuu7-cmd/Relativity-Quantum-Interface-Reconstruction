#!/usr/bin/env python3
"""RQIR Iteration 112 — matrix gain/phase recertification envelope.

Reproducible checks for the exact pure-dead multivariate control problem

    C_ref(t_ref) + C_drift(tau) <= S

with

    C_ref = (t_ref F_ref)^-1,
    C_drift = tau Q / 2,
    S = Sigma_target - Sigma_floor.

No apparatus numbers are asserted here. The examples are deterministic regression
problems showing scalar recovery, coordinate invariance and orientation dependence.
"""

from __future__ import annotations

import math
import numpy as np


def _sym(a: np.ndarray) -> np.ndarray:
    return 0.5 * (a + a.T)


def _inv_sqrt_spd(a: np.ndarray) -> np.ndarray:
    a = _sym(np.asarray(a, dtype=float))
    w, v = np.linalg.eigh(a)
    if np.min(w) <= 0.0:
        raise ValueError("matrix must be positive definite")
    return v @ np.diag(1.0 / np.sqrt(w)) @ v.T


def _lambda_max(a: np.ndarray) -> float:
    return float(np.max(np.linalg.eigvalsh(_sym(a))))


def fixed_cadence(F_ref: np.ndarray, Q: np.ndarray, S: np.ndarray, tau: float):
    """Minimum reference time and overhead/live ratio at fixed live cadence tau."""
    F_ref = _sym(np.asarray(F_ref, dtype=float))
    Q = _sym(np.asarray(Q, dtype=float))
    S = _sym(np.asarray(S, dtype=float))

    Sinv2 = _inv_sqrt_spd(S)
    A = _sym(Sinv2 @ np.linalg.inv(F_ref) @ Sinv2)
    B = _sym(Sinv2 @ Q @ Sinv2)

    C = _sym(np.eye(S.shape[0]) - 0.5 * tau * B)
    Cinv2 = _inv_sqrt_spd(C)
    t_ref = _lambda_max(Cinv2 @ A @ Cinv2)
    return t_ref, t_ref / tau


def optimize_recertification(
    F_ref: np.ndarray,
    Q: np.ndarray,
    S: np.ndarray,
    grid_points: int = 30000,
):
    """Exact 1-D numerical certificate for minimum pure-dead overhead/live ratio.

    The admissible interval is 0 < tau < 2/lambda_max(B), with
    B=S^-1/2 Q S^-1/2. A dense deterministic scan is sufficient for the
    regression tolerances used below and avoids an external scipy dependency.
    """
    F_ref = _sym(np.asarray(F_ref, dtype=float))
    Q = _sym(np.asarray(Q, dtype=float))
    S = _sym(np.asarray(S, dtype=float))

    Sinv2 = _inv_sqrt_spd(S)
    B = _sym(Sinv2 @ Q @ Sinv2)
    lam_b = _lambda_max(B)
    if lam_b <= 1e-15:
        return {"r_min": 0.0, "tau_star": math.inf, "t_ref_star": 0.0}

    tau_max = 2.0 / lam_b
    taus = np.linspace(tau_max * 1e-6, tau_max * (1.0 - 1e-6), grid_points)

    best_r = math.inf
    best_tau = None
    best_t = None
    for tau in taus:
        try:
            t_ref, r = fixed_cadence(F_ref, Q, S, float(tau))
        except ValueError:
            continue
        if r < best_r:
            best_r = r
            best_tau = float(tau)
            best_t = float(t_ref)

    if best_tau is None:
        raise RuntimeError("no admissible cadence found")

    return {"r_min": best_r, "tau_star": best_tau, "t_ref_star": best_t}


def main() -> None:
    # 1) Scalar recovery of RESOURCE-067.
    R = 3.7
    D = 2.3
    S_scalar = 0.8
    scalar = optimize_recertification([[R]], [[D]], [[S_scalar]], grid_points=40000)
    r_exact = 2.0 * D / (R * S_scalar**2)
    tau_exact = S_scalar / D
    t_exact = 2.0 / (R * S_scalar)

    assert abs(scalar["r_min"] / r_exact - 1.0) < 2e-4
    assert abs(scalar["tau_star"] / tau_exact - 1.0) < 2e-4
    assert abs(scalar["t_ref_star"] / t_exact - 1.0) < 2e-4

    # 2) Coordinate-invariance regression.
    F = np.array([[5.0, 1.2], [1.2, 2.0]])
    Q = np.array([[0.8, 0.25], [0.25, 0.4]])
    S = np.array([[0.7, 0.1], [0.1, 0.5]])
    base = optimize_recertification(F, Q, S, grid_points=30000)

    # y = M x. Covariances transform M Cov_x M^T and Fisher transforms M^-T F M^-1.
    M = np.array([[1.5, 0.4], [-0.2, 0.9]])
    Minv = np.linalg.inv(M)
    Fy = Minv.T @ F @ Minv
    Qy = M @ Q @ M.T
    Sy = M @ S @ M.T
    transformed = optimize_recertification(Fy, Qy, Sy, grid_points=30000)
    assert abs(transformed["r_min"] / base["r_min"] - 1.0) < 2e-10

    # 3) Same spectra, different Fisher/drift orientation.
    # Both cases have eig(F)={1,100}, eig(Q)={1,100}, S=I.
    # The only difference is whether the strongest reference-Fisher direction is
    # aligned with the fastest drift direction.
    S2 = np.eye(2)
    Q2 = np.diag([100.0, 1.0])
    F_aligned = np.diag([100.0, 1.0])
    F_misaligned = np.diag([1.0, 100.0])
    aligned = optimize_recertification(F_aligned, Q2, S2, grid_points=40000)
    misaligned = optimize_recertification(F_misaligned, Q2, S2, grid_points=40000)

    assert aligned["r_min"] < misaligned["r_min"]
    ratio = misaligned["r_min"] / aligned["r_min"]
    assert 3.8 < ratio < 4.1

    print("RQIR Iteration 112 regression: PASS")
    print(f"scalar r_min numerical = {scalar['r_min']:.12g}")
    print(f"scalar r_min analytic  = {r_exact:.12g}")
    print(f"scalar tau* numerical  = {scalar['tau_star']:.12g}")
    print(f"scalar tau* analytic   = {tau_exact:.12g}")
    print(f"matrix invariant r_min = {base['r_min']:.12g}")
    print(f"aligned r_min          = {aligned['r_min']:.12g}")
    print(f"misaligned r_min       = {misaligned['r_min']:.12g}")
    print(f"orientation penalty    = {ratio:.12g}x")


if __name__ == "__main__":
    main()
