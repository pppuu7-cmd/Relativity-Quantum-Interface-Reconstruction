"""RQIR Toy Model 007 — finite multiprobe nullspace design verifier.

Reconstructs the exact Toy 005 real five-level source from seed 105, embeds
it as a five-site Newtonian source, applies the recorded two-probe finite
calibration, and verifies:

  rank(A) = 24 in Herm(5),
  nullity = 1,
  eta_R ~ 0.45768,
  equal target mean and equal target symmetrized self-noise,
  opposite commutator response D at the target time.

The recorded geometry/times were found by a deterministic exploratory search.
This verifier reproduces the accepted design; it does not claim global
optimality. All quantities are dimensionless until physical scales are restored.
"""

from __future__ import annotations

import numpy as np


# ---------- Hermitian operator coordinates ----------

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


# ---------- Toy 005 source reconstruction ----------

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


def reconstruct_toy005_source(seed: int = 105):
    """Reproduce the first accepted real-symmetric Toy 005 witness."""
    d = 5
    rng = np.random.default_rng(seed)
    for trial in range(3000):
        energies = np.sort(
            rng.choice(np.arange(-7, 8), size=d, replace=False)
        ).astype(float)
        x = rng.normal(size=(d, d))
        b_raw = (x + x.T) / 2.0
        rank, best = analyze_pair(energies, b_raw)
        if best is None or best[0] <= 1e-7:
            continue

        # Accepted Toy 005 witness occurs at trial 69 for seed 105.
        delta = mat_from_herm_vec(best[3], d)
        delta /= np.max(np.abs(np.linalg.eigvalsh(delta)))

        h = np.diag(energies).astype(complex)
        h += (-np.min(energies) + 1.0) * np.eye(d)

        b = b_raw.astype(complex)
        b += (-np.min(np.linalg.eigvalsh(b)) + 1.0) * np.eye(d)
        return trial, h, b, delta

    raise RuntimeError("Toy 005 source witness was not reproduced")


# ---------- Newtonian probes and kernels ----------

def evolve_diagonal_h(h: np.ndarray, op: np.ndarray, t: float) -> np.ndarray:
    e = np.diag(h).real
    return op * np.exp(1j * (e[:, None] - e[None, :]) * t)


def sym_op(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return (a @ b + b @ a) / 2.0


def comm_op(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return (a @ b - b @ a) / (2j)


def mean(rho: np.ndarray, op: np.ndarray) -> complex:
    return np.trace(rho @ op)


def centered_noise(rho: np.ndarray, a: np.ndarray, b: np.ndarray) -> float:
    d = rho.shape[0]
    da = a - mean(rho, a) * np.eye(d)
    db = b - mean(rho, b) * np.eye(d)
    return float(np.real(np.trace(rho @ sym_op(da, db))))


def comm_kernel(rho: np.ndarray, a: np.ndarray, b: np.ndarray) -> float:
    return float(np.real(np.trace(rho @ comm_op(a, b))))


def main():
    np.set_printoptions(precision=10, suppress=True)
    d = 5

    trial, h, b, _ = reconstruct_toy005_source(seed=105)
    vals, v = np.linalg.eigh(b.real)

    # Toy 005 physical site embedding.  The closest site to probe 0 is one
    # dimensionless length unit away.
    L = float(vals.max())
    x_sites = L / vals
    h_site = v.T @ h.real @ v

    def probe_operator(y: float) -> np.ndarray:
        weights = 1.0 / np.abs(x_sites - y)
        return v @ np.diag(weights) @ v.T

    # Recorded accepted Toy 007 design.
    y0 = 0.0
    y1 = -3.5955271928522547
    t_response = 3.583928899215236
    times = np.array([
        0.0,
        3.0709312960670494,
        t_response,
        3.73521464966555,
        4.18983,
        4.897032874946426,
        5.657269795944965,
    ])

    probes = [probe_operator(y0).astype(complex),
              probe_operator(y1).astype(complex)]

    rows: list[np.ndarray] = []
    labels: list[str] = []

    def add(op: np.ndarray, label: str):
        rows.append(herm_vec(op))
        labels.append(label)

    add(np.eye(d), "trace")
    add(h, "mean energy")

    # Both probe means at every declared calibration time.
    for k in (0, 1):
        for t in times:
            add(evolve_diagonal_h(h, probes[k], float(t)),
                f"M{k}(t={t:.12f})")

    # Mandatory equality of target probe-0 self-noise.
    add(sym_op(evolve_diagonal_h(h, probes[0], t_response), probes[0]),
        "S00(target,0)")

    # Additional independent symmetrized auto/cross-noise controls selected
    # in the accepted exploratory design.
    extra = [
        (0, 1, times[1]),
        (1, 1, times[5]),
        (1, 0, t_response),
        (0, 1, t_response),
        (1, 0, times[3]),
        (0, 0, times[6]),
        (0, 1, times[6]),
    ]
    for k, l, t in extra:
        add(sym_op(evolve_diagonal_h(h, probes[k], float(t)), probes[l]),
            f"S{k}{l}(t={t:.12f},0)")

    a = np.vstack(rows)
    u, singular, vh = np.linalg.svd(a, full_matrices=True)
    rank = int(np.sum(singular > 1e-10))
    nullity = d * d - rank
    assert rank == 24 and nullity == 1

    # Unique null direction and positive null-pair states.
    null_vec = vh[-1]
    null_vec /= np.linalg.norm(null_vec)
    delta0 = mat_from_herm_vec(null_vec, d)
    delta0 /= np.max(np.abs(np.linalg.eigvalsh(delta0)))

    eps = 0.08
    rho_plus = np.eye(d) / d + eps * delta0
    rho_minus = np.eye(d) / d - eps * delta0

    # Target response geometry.
    b0_t = evolve_diagonal_h(h, probes[0], t_response)
    c_response = herm_vec(comm_op(b0_t, probes[0]))
    eta_r = abs(c_response @ null_vec) / np.linalg.norm(c_response)

    # Conditioning after normalizing every calibration operator to unit HS norm.
    a_norm = a / np.linalg.norm(a, axis=1, keepdims=True)
    s_norm = np.linalg.svd(a_norm, compute_uv=False)
    s_min = float(s_norm[-1])
    condition = float(s_norm[0] / s_min)

    target_mean_plus = mean(rho_plus, b0_t).real
    target_mean_minus = mean(rho_minus, b0_t).real
    reference_mean_plus = mean(rho_plus, probes[0]).real
    reference_mean_minus = mean(rho_minus, probes[0]).real
    n_plus = centered_noise(rho_plus, b0_t, probes[0])
    n_minus = centered_noise(rho_minus, b0_t, probes[0])
    d_plus = comm_kernel(rho_plus, b0_t, probes[0])
    d_minus = comm_kernel(rho_minus, b0_t, probes[0])

    max_constraint_residual = float(
        np.max(np.abs(a @ herm_vec(delta0)))
    )

    print("Toy 005 reconstruction trial:", trial)
    print("energy eigenvalues:", np.diag(h).real)
    print("site positions:", x_sites)
    print("probe positions:", (y0, y1))
    print("calibration times:", times)
    print("target response time:", t_response)
    print("constraint rows:", len(rows))
    print("constraint rank:", rank, "/", d * d)
    print("nullity:", nullity)
    print("eta_R:", eta_r)
    print("normalized s_min:", s_min)
    print("normalized condition number:", condition)
    print("eig(rho+):", np.linalg.eigvalsh(rho_plus))
    print("eig(rho-):", np.linalg.eigvalsh(rho_minus))
    print("target mean +/-:", target_mean_plus, target_mean_minus)
    print("reference mean +/-:", reference_mean_plus, reference_mean_minus)
    print("target centered N00 +/-:", n_plus, n_minus)
    print("target D00 +/-:", d_plus, d_minus)
    print("Delta D00:", d_plus - d_minus)
    print("max equality residual:", max_constraint_residual)
    print("H_site=\n", h_site)
    print("selected sym constraints:")
    for label in labels[-8:]:
        print("  ", label)

    # Numerical regression checks for the accepted design.
    assert np.min(np.linalg.eigvalsh(rho_plus)) > 0.0
    assert np.min(np.linalg.eigvalsh(rho_minus)) > 0.0
    assert abs(eta_r - 0.45768196) < 1e-6
    assert abs(s_min - 0.0014629182) < 1e-8
    assert max_constraint_residual < 1e-12
    assert abs(target_mean_plus - target_mean_minus) < 1e-12
    assert abs(n_plus - n_minus) < 1e-12
    assert abs(d_plus - d_minus) > 1e-3


if __name__ == "__main__":
    main()
