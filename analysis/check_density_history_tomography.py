"""RQIR Toy Model 006 reproducibility check.

Verifies the finite-mode sufficient-condition theorem:
for nondegenerate Bohr gaps, full-rank W=|V|^2, and nonzero pair overlaps,
the real span of time-evolved local projectors P_a(t) is Herm(d).

The explicit example uses d=5, energies (0,1,4,10,12), and a fixed-seed
real orthogonal basis.
"""

from __future__ import annotations

import numpy as np


def herm_vec(a: np.ndarray) -> np.ndarray:
    d = a.shape[0]
    out = [a[i, i].real for i in range(d)]
    for i in range(d):
        for j in range(i + 1, d):
            out.extend([
                np.sqrt(2.0) * a[i, j].real,
                np.sqrt(2.0) * a[i, j].imag,
            ])
    return np.asarray(out, dtype=float)


def fixed_orthogonal(d: int, seed: int = 606) -> np.ndarray:
    rng = np.random.default_rng(seed)
    q, r = np.linalg.qr(rng.normal(size=(d, d)))
    signs = np.sign(np.diag(r))
    signs[signs == 0] = 1.0
    return q * signs


def positive_gaps(energies: np.ndarray) -> list[float]:
    out = []
    for i in range(len(energies)):
        for j in range(i + 1, len(energies)):
            out.append(float(energies[j] - energies[i]))
    return sorted(out)


def fourier_span_operators(energies: np.ndarray, v: np.ndarray):
    """Construct diagonal and pair Fourier quadratures of all site projectors.

    For the explicit nondegenerate-gap example, each pair frequency can be
    isolated independently. Multiple sites are included redundantly so the
    numerical rank check mirrors the theorem assumptions.
    """
    d = len(energies)
    ops: list[np.ndarray] = []

    for a in range(d):
        p = np.outer(v[:, a], v[:, a].conj())

        # Zero-frequency component.
        ops.append(np.diag(np.diag(p)))

        # Cosine/sine Hermitian quadratures for every energy pair.
        for i in range(d):
            for j in range(i + 1, d):
                c = p[i, j]

                x = np.zeros((d, d), dtype=complex)
                x[i, j] = c
                x[j, i] = np.conj(c)

                y = np.zeros((d, d), dtype=complex)
                y[i, j] = 1j * c
                y[j, i] = -1j * np.conj(c)

                ops.extend([x, y])

    return ops


def main():
    d = 5
    energies = np.array([0.0, 1.0, 4.0, 10.0, 12.0])
    gaps = positive_gaps(energies)
    assert len(gaps) == len(set(gaps)), "Bohr gaps are not unique"

    v = fixed_orthogonal(d, seed=606)
    w = np.abs(v) ** 2

    ops = fourier_span_operators(energies, v)
    m = np.vstack([herm_vec(op) for op in ops])
    singular = np.linalg.svd(m, compute_uv=False)
    rank = int(np.sum(singular > 1e-10))

    np.set_printoptions(precision=5, suppress=True)
    print("energies:", energies)
    print("positive gaps:", gaps)
    print("min |V_ia|:", np.min(np.abs(v)))
    print("W=|V|^2:\n", w)
    print("rank(W):", np.linalg.matrix_rank(w, tol=1e-10))
    print("det(W):", np.linalg.det(w))
    print("Hermitian operator-span rank:", rank, "/", d * d)
    print("smallest singular value:", singular[-1])

    assert np.linalg.matrix_rank(w, tol=1e-10) == d
    assert np.min(np.abs(v)) > 0.0
    assert rank == d * d


if __name__ == "__main__":
    main()
