"""Paper III Eq. (1) adapter to the frozen RQIR nuisance profiler.

This module does not introduce a second profiling algorithm.  It maps the
resource-law representation

    I_beta(e; Lambda) = min_a [sum_k e_k ||s_k - J_k a||^2 + a^T Lambda a]

to the Fisher block matrix consumed by the pre-existing RQIR
``profiled_beta_information`` implementation in ``protocol002_profiled_fisher``.

The adapter therefore lets heterogeneous sensing architectures provide only
architecture-specific response blocks ``s_k``, nuisance Jacobians ``J_k``,
resource allocations ``e_k`` and prior/calibration precision ``Lambda`` while
reusing the same nuisance-profiling machinery.
"""
from __future__ import annotations

import numpy as np

from protocol002_profiled_fisher import profiled_beta_information


def resource_fisher_matrix(
    allocation: np.ndarray,
    signal: np.ndarray,
    nuisance_jacobian: np.ndarray,
    calibration_precision: np.ndarray,
) -> np.ndarray:
    """Build the Fisher matrix corresponding exactly to Paper III Eq. (1).

    ``signal`` may be shape ``(K,)`` for scalar readout per setting or
    ``(K, D)`` for a D-component whitened readout.  ``nuisance_jacobian`` must
    then be ``(K, P)`` or ``(K, D, P)`` respectively.  ``allocation`` is the
    non-negative exposure/resource assigned to each of the K settings and
    ``calibration_precision`` is the positive-semidefinite P x P nuisance
    precision supplied by independent calibration/prior information.
    """
    e = np.asarray(allocation, dtype=float)
    s = np.asarray(signal, dtype=float)
    j = np.asarray(nuisance_jacobian, dtype=float)
    lam = np.asarray(calibration_precision, dtype=float)

    if e.ndim != 1 or e.size == 0:
        raise ValueError("allocation must be a non-empty 1D array")
    if not np.all(np.isfinite(e)) or np.any(e < 0.0):
        raise ValueError("allocation must be finite and non-negative")

    if s.ndim == 1:
        s = s[:, None]
    if s.ndim != 2 or s.shape[0] != e.size:
        raise ValueError("signal must have shape (K,) or (K,D)")

    if j.ndim == 2:
        if s.shape[1] != 1:
            raise ValueError("2D nuisance_jacobian is valid only for scalar readout")
        j = j[:, None, :]
    if j.ndim != 3 or j.shape[:2] != s.shape:
        raise ValueError("nuisance_jacobian must have shape (K,P) or (K,D,P)")

    p = j.shape[2]
    if lam.shape != (p, p):
        raise ValueError("calibration_precision must have shape (P,P)")
    if not np.all(np.isfinite(lam)) or not np.allclose(lam, lam.T, atol=1e-12, rtol=0.0):
        raise ValueError("calibration_precision must be finite and symmetric")
    if np.min(np.linalg.eigvalsh(lam)) < -1e-12:
        raise ValueError("calibration_precision must be positive semidefinite")

    root_e = np.sqrt(e)
    ds = (root_e[:, None] * s).reshape(-1)
    dj = (root_e[:, None, None] * j).reshape(-1, p)
    derivatives = np.column_stack([ds, dj])
    fisher = derivatives.T @ derivatives
    fisher[1:, 1:] += lam
    return fisher


def profiled_resource_information(
    allocation: np.ndarray,
    signal: np.ndarray,
    nuisance_jacobian: np.ndarray,
    calibration_precision: np.ndarray,
) -> float:
    """Evaluate Paper III Eq. (1) using the existing RQIR Schur profiler."""
    fisher = resource_fisher_matrix(
        allocation, signal, nuisance_jacobian, calibration_precision
    )
    return profiled_beta_information(fisher)


def structural_regression() -> None:
    """Small exact guard for the adapter-to-profiler mapping."""
    e = np.array([0.5, 0.5])
    s = np.array([1.0, 1.0])
    j = np.ones((2, 1))
    lam = np.array([[1.0]])
    value = profiled_resource_information(e, s, j, lam)
    # min_a (1-a)^2 + a^2 = 1/2.
    assert abs(value - 0.5) < 1e-12


if __name__ == "__main__":
    structural_regression()
    print("Paper III resource-law adapter: PASS")
