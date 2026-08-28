"""RQIR Toy Model 005 reproducibility search.

Searches real-symmetric five-level source operators B for two states
rho± = I/d ± eps*Delta satisfying:
  Tr Delta = 0,
  Tr Delta H = 0,
  Tr Delta B(t) = 0 for all t,
  Tr Delta {B(t),B(0)}/2 = 0 for all t,
while the commutator component remains nonzero.

The positive B is then diagonalized and interpreted as a one-particle
Newtonian potential channel with site distances r_a = L/b_a.

This is exploratory finite-mode weak-field code, not a covariant gravity
simulation.
"""

from __future__ import annotations

import numpy as np


def herm_vec(a: np.ndarray) -> np.ndarray:
    d = a.shape[0]
    out = [a[i, i].real for i in range(d)]
    for i in range(d):
        for j in range(i + 1, d):
            out.extend([np.sqrt(2.0) * a[i, j].real,
                        np.sqrt(2.0) * a[i, j].imag])
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


def frequency_components(b: np.ndarray, energies: np.ndarray) -> dict[int, np.ndarray]:
    d = len(energies)
    result: dict[int, np.ndarray] = {}
    for i in range(d):
        for j in range(d):
            w = int(round(float(energies[i] - energies[j])))
            result.setdefault(w, np.zeros((d, d), dtype=complex))[i, j] = b[i, j]
    return result


def hermitian_time_components(xw: dict[int, np.ndarray]):
    ops = []
    if 0 in xw:
        x0 = (xw[0] + xw[0].conj().T) / 2.0
        ops.append((0, "const", x0))
    for w in sorted(k for k in xw if k > 0):
        xp = xw[w]
        xm = xw.get(-w, np.zeros_like(xp))
        c = (xp + xm)
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

    _, singular, vh = np.linalg.svd(m, full_matrices=True)
    rank = int(np.sum(singular > tol))
    row_basis = vh[:rank]

    best = None
    for w, trig, op in comm_ops:
        v = herm_vec(op)
        residual = v - (v @ row_basis.T) @ row_basis
        norm = float(np.linalg.norm(residual))
        if best is None or norm > best[0]:
            best = (norm, w, trig, residual)
    return rank, best


def search_real_symmetric(d: int = 5, trials: int = 3000, seed: int = 105):
    rng = np.random.default_rng(seed)
    for trial in range(trials):
        energies = np.sort(
            rng.choice(np.arange(-7, 8), size=d, replace=False)
        ).astype(float)
        x = rng.normal(size=(d, d))
        b = (x + x.T) / 2.0
        rank, best = analyze_pair(energies, b)
        if best is not None and best[0] > 1e-7:
            return trial, energies, b, rank, best
    raise RuntimeError("No witness found in requested scan")


def build_states(energies, b, residual, eps=0.08):
    d = len(energies)
    delta = mat_from_herm_vec(residual, d)
    delta /= np.max(np.abs(np.linalg.eigvalsh(delta)))

    h = np.diag(energies).astype(complex)
    h += (-np.min(energies) + 1.0) * np.eye(d)

    b = b.astype(complex)
    b += (-np.min(np.linalg.eigvalsh(b)) + 1.0) * np.eye(d)

    rho_plus = np.eye(d) / d + eps * delta
    rho_minus = np.eye(d) / d - eps * delta
    return h, b, delta, rho_plus, rho_minus


def evolve_diagonal_h(h, b, t):
    e = np.diag(h).real
    return b * np.exp(1j * (e[:, None] - e[None, :]) * t)


def mean(rho, x):
    return np.trace(rho @ x)


def noise(rho, bt, b0):
    mt = mean(rho, bt)
    m0 = mean(rho, b0)
    dt = bt - mt * np.eye(bt.shape[0])
    d0 = b0 - m0 * np.eye(bt.shape[0])
    return np.real(np.trace(rho @ ((dt @ d0 + d0 @ dt) / 2.0)))


def comm_kernel(rho, bt, b0):
    return np.real(np.trace(rho @ ((bt @ b0 - b0 @ bt) / (2j))))


def main():
    trial, energies, b0, rank, best = search_real_symmetric()
    h, b, delta, rp, rm = build_states(energies, b0, best[3])

    print("trial:", trial)
    print("raw energies:", energies)
    print("constraint rank:", rank)
    print("commutator residual norm:", best[0])
    print("commutator Fourier component:", best[1], best[2])

    np.set_printoptions(precision=5, suppress=True)
    print("H=\n", h.real)
    print("B=\n", b.real)
    print("Delta=\n", delta.real)
    print("eig(B):", np.linalg.eigvalsh(b))
    print("eig(rho+):", np.linalg.eigvalsh(rp))
    print("eig(rho-):", np.linalg.eigvalsh(rm))
    print("mean energies:", np.trace(rp @ h).real, np.trace(rm @ h).real)

    # Dense verification over the common 2*pi period.
    ts = np.linspace(0.0, 2.0 * np.pi, 5001)
    mean_diff = []
    noise_diff = []
    response = []
    for t in ts:
        bt = evolve_diagonal_h(h, b, t)
        mean_diff.append(abs(mean(rp, bt) - mean(rm, bt)))
        noise_diff.append(abs(noise(rp, bt, b) - noise(rm, bt, b)))
        dp = comm_kernel(rp, bt, b)
        dm = comm_kernel(rm, bt, b)
        response.append((abs(dp - dm), dp, dm))

    k = int(np.argmax([x[0] for x in response]))
    tstar = ts[k]
    bt = evolve_diagonal_h(h, b, tstar)
    print("max mean difference:", max(mean_diff))
    print("max noise difference:", max(noise_diff))
    print("t*:", tstar)
    print("common mean at t*:", mean(rp, bt).real, mean(rm, bt).real)
    print("common N at t*:", noise(rp, bt, b), noise(rm, bt, b))
    print("D at t*:", comm_kernel(rp, bt, b), comm_kernel(rm, bt, b))

    # Newtonian site embedding B = V diag(b_a) V^T.
    vals, v = np.linalg.eigh(b.real)
    h_site = v.T @ h.real @ v
    rp_site = v.T @ rp @ v
    rm_site = v.T @ rm @ v

    # Set the closest site to 1 arbitrary length unit.
    L = vals.max()
    distances = L / vals
    print("B eigenvalues / potential weights:", vals)
    print("site distances with nearest=1:", distances)
    print("H_site=\n", h_site)
    print("local population difference at t=0:",
          np.real(np.diag(rp_site - rm_site)))


if __name__ == "__main__":
    main()
