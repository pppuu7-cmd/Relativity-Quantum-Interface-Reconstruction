"""RQIR Iteration 037: phase-referenced Gaussian covariance-only Fisher bound.

For a real m-dimensional detector-output vector y~N(mu,Sigma(alpha)) with
alpha entering only through an affine covariance

    Sigma(alpha)=Sigma0 + alpha Sigma1,

and with the model required to remain positive definite for alpha in [-1,1],
this script verifies the universal single-shot bound

    I_alpha = 1/2 Tr[(Sigma0^{-1} Sigma1)^2] < m/2.

The result is apparatus-neutral and applies after alpha-independent imprecision
or backaction noise has been included in Sigma0. It does not apply when means,
diagonal variances, transfer functions or backaction themselves carry alpha in
a non-affine way, or when the physical alpha domain is smaller than [-1,1].
"""
from __future__ import annotations
import math
import numpy as np

FIRST4_PRODUCT = 4.4502e4  # Iteration 035, rounded documented threshold.
FIFTH_PRODUCT = 1.0012e6


def covariance_fisher(sigma0: np.ndarray, sigma1: np.ndarray) -> float:
    inv = np.linalg.inv(sigma0)
    return 0.5 * float(np.trace(inv @ sigma1 @ inv @ sigma1))


def whitened_eigs(sigma0: np.ndarray, sigma1: np.ndarray) -> np.ndarray:
    w, v = np.linalg.eigh(sigma0)
    if np.min(w) <= 0:
        raise ValueError("Sigma0 must be positive definite")
    h = v @ np.diag(1.0 / np.sqrt(w)) @ v.T
    a = h @ sigma1 @ h
    return np.linalg.eigvalsh((a + a.T) / 2.0)


def positivity_full_alpha(sigma0: np.ndarray, sigma1: np.ndarray) -> bool:
    return (np.min(np.linalg.eigvalsh(sigma0 + sigma1)) > 0 and
            np.min(np.linalg.eigvalsh(sigma0 - sigma1)) > 0)


def max_shot_fisher_bound(m: int) -> float:
    return 0.5 * m


def min_cycle_ratio(product: float, m: int, efficiency_ratio: float = 1.0) -> float:
    """Necessary tP/tC ratio using Ishot < m/2."""
    if efficiency_ratio <= 0:
        raise ValueError("efficiency_ratio must be positive")
    return product / (efficiency_ratio * max_shot_fisher_bound(m))


def main() -> None:
    # Explicit 2D near-saturating example: eigenvalues of the whitened
    # covariance derivative are +/-0.999, so positivity holds at alpha=+/-1
    # and Ishot approaches the m/2=1 bound from below.
    s0 = np.eye(2)
    s1 = np.diag([0.999, -0.999])
    assert positivity_full_alpha(s0, s1)
    eig = whitened_eigs(s0, s1)
    fish = covariance_fisher(s0, s1)
    print("whitened derivative eigenvalues", eig)
    print("Ishot", fish, "bound", max_shot_fisher_bound(2))
    assert np.max(np.abs(eig)) < 1.0
    assert abs(fish - 0.998001) < 1e-12
    assert fish < 1.0

    # Scalar variance-only special case: |dV/dalpha|<V over full alpha range,
    # hence Ishot=0.5(d ln V/dalpha)^2 < 0.5.
    scalar = covariance_fisher(np.array([[1.0]]), np.array([[0.999]]))
    assert abs(scalar - 0.5 * 0.999**2) < 1e-12
    assert scalar < 0.5

    # Necessary cycle-rate ratios for the current first-four and fifth-row
    # preparation-substitution products at equal acceptance/efficiency.
    r2 = min_cycle_ratio(FIRST4_PRODUCT, 2)
    r8 = min_cycle_ratio(FIRST4_PRODUCT, 8)
    r2_5 = min_cycle_ratio(FIFTH_PRODUCT, 2)
    print("first4 necessary tP/tC, m=2", r2)
    print("first4 necessary tP/tC, m=8", r8)
    print("fifth necessary tP/tC, m=2", r2_5)
    assert abs(r2 - 44502.0) < 1e-9
    assert abs(r8 - 11125.5) < 1e-9
    assert abs(r2_5 - 1001200.0) < 1e-6

    # Transparent m=2 cycle-time ceilings if source metrology takes tP.
    for tp in (1.0, 100.0, 1.0e4):
        tc_max = tp / r2
        print(f"tP={tp:g}s -> necessary tC<{tc_max:.12g}s")

    # Random regression: for positive affine families on [-1,1], Fisher stays
    # below m/2. Deterministic seed.
    rng = np.random.default_rng(20260829)
    for m in (2, 3, 5, 8):
        for _ in range(200):
            q, _ = np.linalg.qr(rng.normal(size=(m, m)))
            lam = rng.uniform(-0.999, 0.999, size=m)
            s0 = np.eye(m)
            s1 = q @ np.diag(lam) @ q.T
            assert positivity_full_alpha(s0, s1)
            f = covariance_fisher(s0, s1)
            assert f < max_shot_fisher_bound(m) + 1e-12


if __name__ == "__main__":
    main()
