"""RQIR Toy Model 008 — reproducible soft-nullspace design scan.

Reconstructs the Toy 005 five-level Newtonian source and scans two-probe,
finite-time calibration designs.  For each random geometry/time proposal, a
greedy selector adds independent symmetrized-kernel controls and records the
best score at ranks 20..24.

Score used in this exploratory scan:
    score = eta_R * sqrt(s_min)
where eta_R is the fraction of the target response operator outside the
calibration row span and s_min is the smallest nonzero singular value after
normalizing every calibration row to unit Hilbert-Schmidt norm.

This is a deterministic design scan, not a proof of global optimality and not
a final statistical objective.  The Fisher/likelihood replacement is derived
in docs/STATISTICAL_IDENTIFIABILITY.md.
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
    result: dict[int, np.ndarray] = {}
    d = len(energies)
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
    d = 5
    rng = np.random.default_rng(seed)
    for trial in range(3000):
        energies = np.sort(rng.choice(np.arange(-7, 8), size=d, replace=False)).astype(float)
        x = rng.normal(size=(d, d))
        b_raw = (x + x.T) / 2.0
        _, best = analyze_pair(energies, b_raw)
        if best is None or best[0] <= 1e-7:
            continue
        h = np.diag(energies).astype(complex)
        h += (-np.min(energies) + 1.0) * np.eye(d)
        b = b_raw.astype(complex)
        b += (-np.min(np.linalg.eigvalsh(b)) + 1.0) * np.eye(d)
        return trial, h, b
    raise RuntimeError("Toy 005 source witness was not reproduced")


def evolve(h: np.ndarray, op: np.ndarray, t: float) -> np.ndarray:
    e = np.diag(h).real
    return op * np.exp(1j * (e[:, None] - e[None, :]) * t)


def sym_op(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return (a @ b + b @ a) / 2.0


def comm_op(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return (a @ b - b @ a) / (2j)


def metrics(a: np.ndarray, cvec: np.ndarray, tol: float = 1e-10):
    a_norm = a / np.linalg.norm(a, axis=1, keepdims=True)
    _, singular, vh = np.linalg.svd(a_norm, full_matrices=True)
    rank = int(np.sum(singular > tol))
    row_basis = vh[:rank]
    residual = cvec - (cvec @ row_basis.T) @ row_basis
    eta = float(np.linalg.norm(residual) / np.linalg.norm(cvec))
    nonzero = singular[singular > tol]
    s_min = float(nonzero[-1])
    condition = float(nonzero[0] / nonzero[-1])
    return rank, 25 - rank, eta, s_min, condition


def greedy_chain(h, probe_operator, y1, t_response, times, max_rank=24):
    probes = [probe_operator(0.0), probe_operator(y1)]
    rows = [herm_vec(np.eye(5)), herm_vec(h)]
    labels = ["trace", "H"]

    for k in range(2):
        for t in times:
            rows.append(herm_vec(evolve(h, probes[k], float(t))))
            labels.append(f"M{k}@{t:.6f}")

    rows.append(herm_vec(sym_op(evolve(h, probes[0], t_response), probes[0])))
    labels.append("S00_target")

    cvec = herm_vec(comm_op(evolve(h, probes[0], t_response), probes[0]))
    a = np.vstack(rows)
    rank = int(np.linalg.matrix_rank(a, tol=1e-10))
    if rank > max_rank:
        return {}

    pool = []
    for t in times:
        for k in range(2):
            for l in range(2):
                if k == 0 and l == 0 and abs(t - t_response) < 1e-10:
                    continue
                vec = herm_vec(sym_op(evolve(h, probes[k], float(t)), probes[l]))
                pool.append((vec, f"S{k}{l}@{t:.6f}"))

    records = {}
    m0 = metrics(a, cvec)
    if m0[0] in (20, 21, 22, 23, 24):
        records[m0[0]] = (m0, list(labels), y1, t_response, times.copy())

    while rank < max_rank:
        best = None
        for idx, (vec, label) in enumerate(pool):
            at = np.vstack([a, vec])
            m = metrics(at, cvec)
            if m[0] != rank + 1:
                continue
            score = m[2] * np.sqrt(m[3])
            if best is None or score > best[0]:
                best = (score, idx, vec, label, m)
        if best is None:
            break
        _, idx, vec, label, m = best
        a = np.vstack([a, vec])
        labels.append(label)
        pool.pop(idx)
        rank = m[0]
        if rank in (20, 21, 22, 23, 24):
            records[rank] = (m, list(labels), y1, t_response, times.copy())
    return records


def main():
    trial, h, b = reconstruct_toy005_source(seed=105)
    vals, v = np.linalg.eigh(b.real)
    length_scale = float(vals.max())
    x_sites = length_scale / vals

    def probe_operator(y: float) -> np.ndarray:
        weights = 1.0 / np.abs(x_sites - y)
        return (v @ np.diag(weights) @ v.T).astype(complex)

    rng = np.random.default_rng(2026082902)
    best_by_rank = {}
    n_designs = 300

    for _ in range(n_designs):
        y1 = float(rng.uniform(-8.0, -0.3))
        t_response = float(rng.uniform(0.3, 2.0 * np.pi - 0.2))
        other = np.sort(rng.uniform(0.15, 2.0 * np.pi - 0.1, size=4))
        times = np.unique(np.round(np.array([0.0, t_response, *other]), 12))
        if len(times) != 6:
            continue

        records = greedy_chain(h, probe_operator, y1, t_response, times)
        for rank, data in records.items():
            m = data[0]
            score = m[2] * np.sqrt(m[3])
            old = best_by_rank.get(rank)
            if old is None or score > old[0]:
                best_by_rank[rank] = (score, data)

    print("Toy 005 reconstruction trial:", trial)
    print("site positions:", x_sites)
    print("scan designs:", n_designs)
    print("rank nullity eta_R s_min condition score y1 t_response")
    for rank in sorted(best_by_rank):
        score, data = best_by_rank[rank]
        m, labels, y1, t_response, times = data
        print(
            rank,
            m[1],
            f"{m[2]:.12f}",
            f"{m[3]:.12g}",
            f"{m[4]:.9f}",
            f"{score:.12f}",
            f"{y1:.12f}",
            f"{t_response:.12f}",
        )
        print(" times:", np.array2string(times, precision=8))
        print(" added tail:", labels[-8:])

    expected = {
        20: (0.6968013783829194, 0.005684684380676806),
        21: (0.6775211295000244, 0.005436955333154186),
        22: (0.6389914417083342, 0.0024818582028525685),
        23: (0.6076291264668624, 0.0013892350819041186),
        24: (0.4738498501742753, 0.0015638774318377999),
    }
    for rank, (eta_ref, smin_ref) in expected.items():
        m = best_by_rank[rank][1][0]
        assert abs(m[2] - eta_ref) < 1e-10
        assert abs(m[3] - smin_ref) < 1e-10


if __name__ == "__main__":
    main()
