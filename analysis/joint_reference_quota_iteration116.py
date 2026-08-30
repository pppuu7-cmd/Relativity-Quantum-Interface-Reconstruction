"""RQIR Iteration 116: non-double-counted joint-reference quota scheduler.

Algebraic/resource result only. No apparatus forecast and no new-physics claim.
"""
from __future__ import annotations

import numpy as np


def invsqrt_spd(a: np.ndarray) -> np.ndarray:
    w, u = np.linalg.eigh(a)
    if np.min(w) <= 0:
        raise ValueError("matrix must be positive definite")
    return u @ np.diag(1.0 / np.sqrt(w)) @ u.T


def joint_time(k_rate: np.ndarray, h_req: np.ndarray) -> float:
    """Minimum T such that T*K_rate >= H_req in Loewner order."""
    z = invsqrt_spd(k_rate)
    return float(np.linalg.eigvalsh(z @ h_req @ z).max())


def main() -> None:
    # RESOURCE-082: diagonal case reduces to the largest individual burden.
    rates = np.array([2.0, 4.0, 8.0, 5.0, 10.0, 3.0, 6.0, 9.0])
    burdens = np.array([1.0, 3.0, 4.0, 2.0, 5.0, 1.5, 4.0, 3.0])
    k = np.diag(rates)
    h = np.diag(burdens)
    t_joint = joint_time(k, h)
    ratios = burdens / rates
    assert abs(t_joint - np.max(ratios)) < 1e-13

    # RESOURCE-084: dedicated sequential campaigns sum the same burdens.
    t_separate = float(np.sum(ratios))
    assert t_separate >= t_joint
    assert t_separate / t_joint <= len(ratios) + 1e-13

    # Equal burdens saturate the n-fold upper saving for n simultaneous quotas.
    k8 = np.eye(8)
    h8 = np.eye(8)
    assert abs(joint_time(k8, h8) - 1.0) < 1e-13
    assert abs(8.0 / joint_time(k8, h8) - 8.0) < 1e-13

    # NG-073: diagonal rates alone are not enough when the shared Fisher is correlated.
    rho = 0.8
    kcorr = np.array([[1.0, rho], [rho, 1.0]])
    hcorr = np.eye(2)
    tcorr = joint_time(kcorr, hcorr)
    assert abs(tcorr - 5.0) < 1e-12

    # Coordinate invariance under nonsingular congruence transformations.
    rng = np.random.default_rng(20260831116)
    max_rel = 0.0
    for _ in range(500):
        a = rng.normal(size=(5, 5))
        k0 = a.T @ a + 0.8 * np.eye(5)
        b = rng.normal(size=(5, 5))
        h0 = b.T @ b + 0.2 * np.eye(5)
        t0 = joint_time(k0, h0)

        s = rng.normal(size=(5, 5))
        while abs(np.linalg.det(s)) < 0.2:
            s = rng.normal(size=(5, 5))
        t1 = joint_time(s.T @ k0 @ s, s.T @ h0 @ s)
        max_rel = max(max_rel, abs(t1 - t0) / t0)
    assert max_rel < 2e-9

    # More Fisher cannot increase the minimum quota time.
    for _ in range(200):
        a = rng.normal(size=(4, 4))
        k0 = a.T @ a + np.eye(4)
        h0 = np.eye(4)
        d = rng.normal(size=(4, 4))
        k1 = k0 + d.T @ d
        assert joint_time(k1, h0) <= joint_time(k0, h0) + 1e-11

    print("diagonal burdens", ratios)
    print("joint time", t_joint)
    print("separate time", t_separate)
    print("separate/joint", t_separate / t_joint)
    print("8-way ideal simultaneous saving", 8.0)
    print("correlated two-coordinate time", tcorr)
    print("coordinate-invariance max relative error", max_rel)


if __name__ == "__main__":
    main()
