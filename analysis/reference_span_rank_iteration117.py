"""RQIR Iteration 117: rank/span certificate for same-state reference settings.

Structural Fisher-rank result only. No apparatus forecast and no new-physics claim.
"""
from __future__ import annotations

import math
import numpy as np


def fisher_from_jacobian(j: np.ndarray, w: np.ndarray | None = None) -> np.ndarray:
    if w is None:
        w = np.eye(j.shape[0])
    return j.T @ w @ j


def matrix_rank(a: np.ndarray, tol: float = 1e-10) -> int:
    return int(np.sum(np.linalg.svd(a, compute_uv=False) > tol))


def support_feasible(k: np.ndarray, h: np.ndarray, tol: float = 1e-10) -> bool:
    # For PSD matrices, range(H) subset range(K) iff null(K) subset null(H).
    ew, u = np.linalg.eigh(k)
    null = u[:, ew <= tol]
    if null.shape[1] == 0:
        return True
    return np.linalg.norm(h @ null) <= tol * max(1.0, np.linalg.norm(h))


def main() -> None:
    rng = np.random.default_rng(20260831117)

    # One four-real observation setting can contribute at most rank four.
    p = 12
    j = rng.normal(size=(4, p))
    k = fisher_from_jacobian(j)
    assert matrix_rank(k) <= 4

    # Repeating the unchanged setting scales Fisher but cannot increase rank/span.
    for nrep in (2, 10, 1000):
        assert matrix_rank(nrep * k) == matrix_rank(k)

    # A required direction placed in null(K) is infeasible at every finite exposure.
    ew, u = np.linalg.eigh(k)
    v = u[:, np.argmin(ew)]
    h_bad = np.outer(v, v)
    assert not support_feasible(k, h_bad)
    assert not support_feasible(1e9 * k, h_bad)

    # With m distinct four-real settings, rank cannot exceed 4m.
    for m in range(1, 5):
        js = [rng.normal(size=(4, p)) for _ in range(m)]
        ktot = sum(fisher_from_jacobian(x) for x in js)
        assert matrix_rank(ktot) <= min(p, 4 * m)

    # Lower bounds for independent required coordinates.
    assert math.ceil(8 / 4) == 2   # common gain + seven scalar independent layers
    assert math.ceil(15 / 4) == 4  # common gain + seven independent 2D layers

    # DESIGN-018 regression: deliberately complementary settings recover an 8D quota.
    p2 = 8
    j1 = np.zeros((4, p2))
    j2 = np.zeros((4, p2))
    j1[:, :4] = np.eye(4)
    j2[:, 4:] = np.eye(4)
    k1 = fisher_from_jacobian(j1)
    k2 = fisher_from_jacobian(j2)
    h8 = np.eye(8)
    assert not support_feasible(k1, h8)
    assert support_feasible(k1 + k2, h8)
    assert matrix_rank(k1 + k2) == 8

    # Orientation matters: two settings satisfy the dimension lower bound but may still fail.
    j3 = j1.copy()
    k3 = fisher_from_jacobian(j3)
    assert matrix_rank(k1 + k3) == 4
    assert not support_feasible(k1 + k3, h8)

    # Required-subspace singular-value certificate.
    jstack_good = np.vstack([j1, j2])
    jstack_bad = np.vstack([j1, j3])
    s_good = np.linalg.svd(jstack_good, compute_uv=False)
    s_bad = np.linalg.svd(jstack_bad, compute_uv=False)
    assert s_good.min() > 0.999999999
    assert s_bad[-1] < 1e-12

    print("single-setting Fisher rank", matrix_rank(k))
    print("8 independent required coordinates need at least", math.ceil(8/4), "settings")
    print("15 independent required coordinates need at least", math.ceil(15/4), "settings")
    print("complementary 2-setting rank", matrix_rank(k1+k2))
    print("redundant 2-setting rank", matrix_rank(k1+k3))
    print("good stacked s_min", s_good.min())
    print("bad stacked s_min", s_bad[-1])


if __name__ == "__main__":
    main()
