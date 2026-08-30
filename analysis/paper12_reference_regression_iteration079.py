"""RQIR Iteration 079 — reference-likelihood regression certificate.

This file is intentionally source-agnostic. It verifies algebraic invariants that
all Paper-II detector likelihoods must satisfy before architecture-specific
resource calculations are credited.

It does not claim experimental readiness or new physics.
"""
from __future__ import annotations

import math
import numpy as np


def profiled_fisher(s, J, prior=None, rcond=1e-14):
    """Whitened Gaussian Fisher for beta after profiling nuisance columns J."""
    s = np.asarray(s, dtype=float).reshape(-1)
    J = np.asarray(J, dtype=float)
    if J.ndim == 1:
        J = J[:, None]
    if J.shape[1] == 0:
        return float(s @ s)

    f_bb = float(s @ s)
    f_bt = s @ J
    f_tt = J.T @ J
    if prior is not None:
        f_tt = f_tt + np.asarray(prior, dtype=float)
    return float(f_bb - f_bt @ np.linalg.pinv(f_tt, rcond=rcond) @ f_bt.T)


def main():
    rng = np.random.default_rng(20260830)

    # 1. Schur complement equals orthogonal projection residual with no prior.
    s = rng.normal(size=8)
    J = rng.normal(size=(8, 3))
    f_schur = profiled_fisher(s, J)
    projector = J @ np.linalg.pinv(J)
    f_projection = float(np.linalg.norm((np.eye(len(s)) - projector) @ s) ** 2)
    assert abs(f_schur - f_projection) < 1e-12

    # 2. Invariance under any invertible nuisance reparameterization.
    M = rng.normal(size=(3, 3))
    while abs(np.linalg.det(M)) < 0.2:
        M = rng.normal(size=(3, 3))
    P = np.diag([0.2, 0.7, 1.3])
    f_original = profiled_fisher(s, J, P)
    f_reparam = profiled_fisher(s, J @ M, M.T @ P @ M)
    assert abs(f_original - f_reparam) < 1e-12

    # 3. Adding positive-semidefinite nuisance information cannot reduce F_beta.
    Q = rng.normal(size=(3, 3))
    extra = Q.T @ Q
    f_weak = profiled_fisher(s, J, P)
    f_strong = profiled_fisher(s, J, P + extra)
    assert f_strong + 1e-12 >= f_weak

    # 4. NG-005 exact source-amplitude obstruction and finite-preparation law.
    s0 = np.array([1.0, 0.0])  # normalized raw science Fisher S=1
    for C_a in [0.0, 1.0, 4.0, 9.0, 19.0, 99.0]:
        f = profiled_fisher(s0, s0[:, None], np.array([[C_a]]))
        expected = 0.0 if C_a == 0 else C_a / (1.0 + C_a)
        assert abs(f - expected) < 1e-12

    # 5. NG-006 structural form: more exposure cannot break an exactly aligned,
    # unconstrained control nuisance.
    for exposure in [1.0, 2.0, 10.0, 100.0, 1e6]:
        scale = math.sqrt(exposure)
        f = profiled_fisher(scale * s0, (scale * s0)[:, None])
        assert abs(f) < 1e-10

    # 6. Two-band spectral-tilt profiling identity used by the physical D2 front.
    g2, g4 = 0.3, 0.7
    g = np.array([g2, g4])
    tilt = np.array([g2, -g4])
    f_tilt = profiled_fisher(g, tilt[:, None])
    s_eff = 4.0 * g2**2 * g4**2 / (g2**2 + g4**2)
    assert abs(f_tilt - s_eff) < 1e-12

    # 7. NUM-001 counterexample: threshold deletion of a weak nuisance direction
    # can falsely turn exact degeneracy into unit Fisher.
    eps = 1e-8
    science = np.array([1.0, 0.0])
    nuisance = np.array([[eps], [0.0]])
    f_true = profiled_fisher(science, nuisance, rcond=1e-30)
    f_tt = float((nuisance.T @ nuisance)[0, 0])
    f_bt = float(science @ nuisance[:, 0])
    threshold = 1e-12
    f_bad = 1.0 - (f_bt * f_bt / f_tt if f_tt > threshold else 0.0)
    assert abs(f_true) < 1e-12
    assert abs(f_bad - 1.0) < 1e-12

    print("projection identity:", f_schur, f_projection)
    print("reparameterization invariant:", f_original, f_reparam)
    print("monotonicity:", f_weak, "->", f_strong)
    print("NG-005 C_a=9:", profiled_fisher(s0, s0[:, None], np.array([[9.0]])))
    print("two-band tilt F:", f_tilt, "S_eff:", s_eff)
    print("threshold counterexample true/bad:", f_true, f_bad)
    print("Paper-II reference-likelihood regression certificate: PASS")


if __name__ == "__main__":
    main()
