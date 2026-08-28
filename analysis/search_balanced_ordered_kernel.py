"""RQIR ordered-kernel null-pair search.

Search finite-dimensional Hermitian source algebras for two states rho± = I/d ± eps*Delta
such that:
  Tr Delta = 0,
  Tr Delta H = 0,
  Tr Delta B(t) = 0 for all t,
  Tr Delta {B(t),B(0)}/2 = 0 for all t,
but Tr Delta [B(t),B(0)]/(2i) != 0 for at least one Fourier component.

Integer energy spectra make the all-time constraints finite Fourier-span conditions.
This script is exploratory research code, not a phenomenological gravity calculation.
"""

from __future__ import annotations

import numpy as np


def herm_vec(a: np.ndarray) -> np.ndarray:
    """Real Hilbert-Schmidt vectorization of a Hermitian matrix."""
    d = a.shape[0]
    out = [a[i, i].real for i in range(d)]
    for i in range(d):
        for j in range(i + 1, d):
            out.extend([np.sqrt(2.0) * a[i, j].real, np.sqrt(2.0) * a[i, j].imag])
    return np.asarray(out, dtype=float)


def mat_from_herm_vec(v: np.ndarray, d: int) -> np.ndarray:
    a = np.zeros((d, d), dtype=complex)
    k = 0
    for i in range(d):
        a[i, i] = v[k]
        k += 1
    for i in range(d):
        for j in range(i + 1, d):
            a[i, j] = (v[k] + 1j * v[k + 1]) / np.sqrt(2.0)
            a[j, i] = np.conj(a[i, j])
            k += 2
    return a


def random_hermitian(d: int, rng: np.random.Generator) -> np.ndarray:
    x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    return (x + x.conj().T) / 2.0


def frequency_components(b: np.ndarray, energies: np.ndarray) -> dict[int, np.ndarray]:
    """Return B_w with B(t)=sum_w exp(i w t) B_w for integer energies."""
    d = len(energies)
    result: dict[int, np.ndarray] = {}
    for i in range(d):
        for j in range(d):
            w = int(round(float(energies[i] - energies[j])))
            if w not in result:
                result[w] = np.zeros((d, d), dtype=complex)
            result[w][i, j] = b[i, j]
    return result


def hermitian_time_components(xw: dict[int, np.ndarray]):
    """Hermitian constant/cos/sin operator coefficients for X(t)."""
    ops = []
    if 0 in xw:
        x0 = (xw[0] + xw[0].conj().T) / 2.0
        ops.append((0, "const", x0))
    for w in sorted(k for k in xw if k > 0):
        xp = xw[w]
        xm = xw.get(-w, np.zeros_like(xp))
        c = xp + xm
        s = 1j * (xp - xm)
        c = (c + c.conj().T) / 2.0
        s = (s + s.conj().T) / 2.0
        ops.append((w, "cos", c))
        ops.append((w, "sin", s))
    return ops


def analyze_pair(energies: np.ndarray, b: np.ndarray, tol: float = 1e-9):
    d = len(energies)
    h = np.diag(energies)
    bw = frequency_components(b, energies)

    mean_ops = hermitian_time_components(bw)
    sw = {w: (x @ b + b @ x) / 2.0 for w, x in bw.items()}
    cw = {w: (x @ b - b @ x) / (2j) for w, x in bw.items()}
    sym_ops = hermitian_time_components(sw)
    comm_ops = hermitian_time_components(cw)

    rows = [herm_vec(np.eye(d)), herm_vec(h)]
    rows += [herm_vec(op) for _, _, op in mean_ops]
    rows += [herm_vec(op) for _, _, op in sym_ops]
    m = np.vstack(rows)

    _, singular, vh = np.linalg.svd(m, full_matrices=False)
    rank = int(np.sum(singular > tol))
    row_basis = vh[:rank]

    best = None
    for w, trig, op in comm_ops:
        v = herm_vec(op)
        residual = v - (v @ row_basis.T) @ row_basis
        norm = float(np.linalg.norm(residual))
        if best is None or norm > best[0]:
            best = (norm, w, trig, residual)

    return rank, best, m


def search_dimension(d: int, trials: int, seed: int):
    rng = np.random.default_rng(seed)
    for trial in range(trials):
        energies = np.sort(rng.choice(np.arange(-6, 7), size=d, replace=False)).astype(float)
        b = random_hermitian(d, rng)
        rank, best, _ = analyze_pair(energies, b)
        if best is not None and best[0] > 1e-7:
            return trial, energies, b, rank, best
    return None


def build_states(energies, b, residual, eps=0.1):
    d = len(energies)
    delta = mat_from_herm_vec(residual, d)
    delta /= np.max(np.abs(np.linalg.eigvalsh(delta)))

    # Identity shifts preserve gaps, centered kernels and commutators.
    h = np.diag(energies)
    h += (-np.min(energies) + 1.0) * np.eye(d)
    b = b + (-np.min(np.linalg.eigvalsh(b)) + 1.0) * np.eye(d)

    rho_plus = np.eye(d) / d + eps * delta
    rho_minus = np.eye(d) / d - eps * delta
    return h, b, delta, rho_plus, rho_minus


def main():
    scans = [(2, 500, 44), (3, 1500, 45), (4, 5000, 46), (5, 500, 47)]
    for d, trials, seed in scans:
        result = search_dimension(d, trials, seed)
        if result is None:
            print(f"d={d}: no witness in {trials} trials")
            continue
        trial, energies, b, rank, best = result
        print(f"d={d}: witness at trial={trial}, rank={rank}, residual={best[0]:.6g}")
        print("energies:", energies)
        h, bp, delta, rp, rm = build_states(energies, b, best[3])
        print("eig(H):", np.linalg.eigvalsh(h))
        print("eig(B):", np.linalg.eigvalsh(bp))
        print("eig(rho+):", np.linalg.eigvalsh(rp))
        print("eig(rho-):", np.linalg.eigvalsh(rm))
        if d == 5:
            np.set_printoptions(precision=5, suppress=True)
            print("B=\n", bp)
            print("Delta=\n", delta)


if __name__ == "__main__":
    main()
