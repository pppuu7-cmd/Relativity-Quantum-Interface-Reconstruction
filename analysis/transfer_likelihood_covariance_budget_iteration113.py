#!/usr/bin/env python3
"""RQIR Iteration 113 — likelihood-derived complex-transfer covariance budget.

This script verifies:
1. the exact Schur/LMI retention condition for a scalar science parameter beta;
2. the canonical rank-one science-coupled transfer calibration certificate;
3. NG-005/source-amplitude scalar recovery;
4. the final-5-sigma fixed-retention bookkeeping correction;
5. reduction of multivariate gain/phase recertification to the likelihood-derived
   science-coupled transfer mode.

No apparatus numbers are asserted.
"""

from __future__ import annotations

import math
import numpy as np


def _sym(a: np.ndarray) -> np.ndarray:
    return 0.5 * (a + a.T)


def profile_fisher(F0: float, b: np.ndarray, G: np.ndarray, C: np.ndarray) -> float:
    """Profile transfer nuisance g after all other nuisances are already profiled."""
    b = np.asarray(b, dtype=float)
    G = _sym(np.asarray(G, dtype=float))
    C = _sym(np.asarray(C, dtype=float))
    return float(F0 - b @ np.linalg.solve(G + C, b))


def targeted_rank1_certificate(F0: float, b: np.ndarray, G: np.ndarray, q: float):
    """Canonical rank-one calibration reaching retained fraction q of F0.

    Returns B=b^T G^-1 b, raw loss fraction ell0=B/F0, kappa, C*=kappa a a^T,
    and the normalized science-coupled transfer coordinate a=b/sqrt(B).
    """
    if not (0.0 < q < 1.0):
        raise ValueError("q must lie in (0,1)")
    b = np.asarray(b, dtype=float)
    G = _sym(np.asarray(G, dtype=float))
    B = float(b @ np.linalg.solve(G, b))
    if B < -1e-12 or B > F0 * (1.0 + 1e-10):
        raise ValueError("invalid PSD Fisher block: require 0 <= B <= F0")
    if B <= 1e-15:
        return B, 0.0, 0.0, np.zeros_like(G), np.zeros_like(b)

    ell0 = B / F0
    free_retention = 1.0 - ell0
    a = b / math.sqrt(B)
    if q <= free_retention + 1e-14:
        return B, ell0, 0.0, np.zeros_like(G), a

    kappa = ell0 / (1.0 - q) - 1.0
    Cstar = kappa * np.outer(a, a)
    return B, ell0, kappa, Cstar, a


def effective_reference_rate(a: np.ndarray, F_ref: np.ndarray) -> float:
    """Fisher rate for the linear functional eta=a^T g with other g directions free."""
    a = np.asarray(a, dtype=float)
    F_ref = _sym(np.asarray(F_ref, dtype=float))
    return float(1.0 / (a @ np.linalg.solve(F_ref, a)))


def main() -> None:
    rng = np.random.default_rng(113)

    # ------------------------------------------------------------------
    # 1. Four-real-component regression with prescribed free-transfer loss.
    m = 4
    A = rng.normal(size=(m, m))
    G = A.T @ A + 0.5 * np.eye(m)
    v = rng.normal(size=m)
    F0 = 3.0
    target_loss_fraction = 0.8
    Bv = float(v @ np.linalg.solve(G, v))
    b = v * math.sqrt(target_loss_fraction * F0 / Bv)
    q = 0.90

    B, ell0, kappa, Cstar, a = targeted_rank1_certificate(F0, b, G, q)
    Fstar = profile_fisher(F0, b, G, Cstar)
    assert abs(ell0 - 0.8) < 2e-14
    assert abs(kappa - 7.0) < 2e-13
    assert abs(Fstar - q * F0) < 2e-13

    # Exact LMI/Schur equivalence at the rank-one boundary:
    # G+C >= b b^T / [(1-q)F0].
    LMI = _sym(G + Cstar - np.outer(b, b) / ((1.0 - q) * F0))
    eig = np.linalg.eigvalsh(LMI)
    assert eig.min() > -2e-12
    assert abs(eig.min()) < 2e-10

    # ------------------------------------------------------------------
    # 2. NG-005 scalar recovery: fully aligned nuisance, raw F0=25, q=0.9.
    F0_s = 25.0
    G_s = np.array([[25.0]])
    b_s = np.array([25.0])
    _, ell_s, k_s, C_s, a_s = targeted_rank1_certificate(F0_s, b_s, G_s, 0.90)
    assert abs(ell_s - 1.0) < 1e-14
    assert abs(k_s - 9.0) < 1e-14
    assert abs(C_s[0, 0] - 225.0) < 1e-12
    assert abs(profile_fisher(F0_s, b_s, G_s, C_s) - 22.5) < 1e-12
    sigma_g = 1.0 / math.sqrt(C_s[0, 0])
    assert abs(sigma_g - 1.0 / 15.0) < 1e-14

    # Final target 25 at fixed 90% retention requires raw F0=25/0.9 and C=250.
    F0_final = 25.0 / 0.90
    G_final = np.array([[F0_final]])
    b_final = np.array([F0_final])
    _, _, _, C_final, _ = targeted_rank1_certificate(F0_final, b_final, G_final, 0.90)
    assert abs(C_final[0, 0] - 250.0) < 1e-11
    assert abs(profile_fisher(F0_final, b_final, G_final, C_final) - 25.0) < 1e-11

    # ------------------------------------------------------------------
    # 3. Likelihood-derived eta recertification reduction.
    # The target rank-one Fisher C*=kappa a a^T is guaranteed whenever
    # a^T Sigma_total a <= 1/kappa, because
    # Sigma_total^-1 >= kappa a a^T iff kappa a^T Sigma_total a <= 1.
    Rm = rng.normal(size=(m, m))
    F_ref = Rm.T @ Rm + 2.0 * np.eye(m)
    Qm = rng.normal(size=(m, m))
    Q = 0.02 * (Qm.T @ Qm)

    sigma_eta_star2 = 1.0 / kappa
    # Choose a deterministic floor equal to 20% of the eta variance budget.
    floor_scale = 0.20 * sigma_eta_star2 / float(a @ a)
    Sigma_floor = floor_scale * np.eye(m)
    sigma_floor_eta2 = float(a @ Sigma_floor @ a)

    R_eta = effective_reference_rate(a, F_ref)
    D_eta = float(a @ Q @ a)
    S_eta = sigma_eta_star2 - sigma_floor_eta2
    assert S_eta > 0.0

    # RESOURCE-067 applied to the likelihood-derived eta coordinate.
    t_ref = 2.0 / (R_eta * S_eta)
    tau = S_eta / D_eta
    r_eta = 2.0 * D_eta / (R_eta * S_eta**2)

    Sigma_total = Sigma_floor + np.linalg.inv(t_ref * F_ref) + 0.5 * tau * Q
    eta_var = float(a @ Sigma_total @ a)
    assert abs(eta_var - sigma_eta_star2) < 2e-13

    C_total = np.linalg.inv(Sigma_total)
    cert = _sym(C_total - kappa * np.outer(a, a))
    assert np.linalg.eigvalsh(cert).min() > -2e-11
    assert profile_fisher(F0, b, G, C_total) >= q * F0 - 2e-11

    print("RQIR Iteration 113 regression: PASS")
    print(f"4D free-transfer loss fraction ell0 = {ell0:.12g}")
    print(f"4D target q                       = {q:.12g}")
    print(f"rank-one kappa                    = {kappa:.12g}")
    print(f"profiled F at rank-one boundary   = {Fstar:.12g}")
    print(f"LMI minimum eigenvalue            = {eig.min():.12g}")
    print(f"NG-005 scalar C(q=0.9,F0=25)      = {C_s[0,0]:.12g}")
    print(f"NG-005 scalar sigma_g             = {sigma_g:.12g}")
    print(f"final-5sigma raw F0               = {F0_final:.12g}")
    print(f"final-5sigma C at q=0.9           = {C_final[0,0]:.12g}")
    print(f"eta target variance               = {sigma_eta_star2:.12g}")
    print(f"eta effective reference rate      = {R_eta:.12g}")
    print(f"eta drift rate                    = {D_eta:.12g}")
    print(f"eta optimal pure-dead overhead    = {r_eta:.12g}")


if __name__ == "__main__":
    main()
