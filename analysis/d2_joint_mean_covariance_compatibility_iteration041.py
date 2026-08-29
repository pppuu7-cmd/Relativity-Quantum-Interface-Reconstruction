"""RQIR Iteration 041: joint D2 mean+covariance trajectory compatibility audit.

Checks whether the current 14 force-mean calibration observables and the
best-four centered covariance endpoints can legitimately be treated as
information obtained from one disturbance-free source trajectory.

The audit is deliberately apparatus-neutral:
- reconstructs the accepted Toy009 / Iteration-011 force operators;
- evaluates pairwise operator commutators;
- identifies maximal same-time commuting groups;
- combines the Iteration-040 covariance-cycle lower bound with the current
  centered mean/control Fisher targets to obtain the *optimistic* per-cycle
  standardized information that a shared-output detector would need.

No claim is made that a physical continuous detector saturates these bounds.
If sequential noncommuting observables are monitored on the same source copy,
measurement backaction must be included explicitly.
"""
from __future__ import annotations

import math
import numpy as np

D = 5
E = np.array([1., 2., 3., 4., 6.])
H = np.diag(E).astype(complex)
EPS = 0.08
Y1 = -3.7766873836695947
TIMES = np.array([0., 3.09855988, 3.45849306, 2.93830159,
                  4.13016958, 4.84480925, 4.99085067])
TR = float(TIMES[2])

# Current centered Iteration-034/036 targets.
GAMMA_MEAN_D2 = 1.830265e6
SIGMA_TAU_D2 = 5.77425e-3
SIGMA_BMEAN_D2 = 7.39168e-5
SIGMA_BCOV_D2 = 1.30175e-4

# Iteration-040 accepted-cycle lower bound for best4 covariance graph.
N_BEST4_COV = 1.180254e6


def source_geometry():
    rng = np.random.default_rng(314159)
    for _ in range(812):
        x = rng.normal(size=(D, D))
        braw = (x + x.T) / 2.0
    ev = np.linalg.eigvalsh(braw)
    bpos = braw + (-ev.min() + 1.0) * np.eye(D)
    vals, v = np.linalg.eigh(bpos)
    return vals, v, float(vals.max())


VALS, V, SCALE = source_geometry()


def evolve(a: np.ndarray, t: float) -> np.ndarray:
    return a * np.exp(1j * (E[:, None] - E[None, :]) * t)


def grad_probe(y: float) -> np.ndarray:
    r = SCALE / VALS - y
    return (V @ np.diag(1.0 / r**2) @ V.T).astype(complex)


def comm_norm(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm(a @ b - b @ a, ord="fro"))


def force_mean_operators():
    labels = []
    ops = []
    for k, y in ((0, 0.0), (1, Y1)):
        g = grad_probe(y)
        for j, t in enumerate(TIMES):
            labels.append(f"G{k}@T{j}")
            ops.append(evolve(g, float(t)))
    return labels, ops


def best4_endpoint_operators():
    # Iteration-040 best4 rows (0,1,3,7) use six unique endpoints:
    # row0 G0(TR)-G0(0), row1 G0(T1)-G1(0),
    # row3 G1(TR)-G0(0), row7 G0(T6)-G1(0).
    specs = [
        ("G0@0", 0, 0.0),
        ("G1@0", 1, 0.0),
        ("G0@TR", 0, TR),
        ("G1@TR", 1, TR),
        ("G0@T1", 0, float(TIMES[1])),
        ("G0@T6", 0, float(TIMES[6])),
    ]
    out = []
    for label, k, t in specs:
        g = grad_probe(0.0 if k == 0 else Y1)
        out.append((label, t, evolve(g, t)))
    return out


def per_cycle_requirement(total_information: float, ncycles: float) -> tuple[float, float]:
    i = total_information / ncycles
    return i, math.sqrt(i)


def main() -> None:
    labels, ops = force_mean_operators()
    noncommuting = []
    commuting = []
    norms = []
    for i in range(len(ops)):
        for j in range(i + 1, len(ops)):
            c = comm_norm(ops[i], ops[j])
            norms.append(c)
            if c < 1e-12:
                commuting.append((labels[i], labels[j], c))
            else:
                noncommuting.append((labels[i], labels[j], c))

    print("14-force-mean pair count", len(norms))
    print("commuting pairs", len(commuting))
    print("noncommuting pairs", len(noncommuting))
    print("commutator median/max", np.median(norms), np.max(norms))
    print("commuting pairs", commuting)

    # Same-time G0/G1 commute because both are functions of the same source
    # position operator. Every distinct-time pair is noncommuting in this model.
    assert len(norms) == 91
    assert len(commuting) == 7
    assert len(noncommuting) == 84
    for j in range(7):
        assert comm_norm(ops[j], ops[7 + j]) < 1e-12
    for i in range(14):
        for j in range(i + 1, 14):
            if j == i + 7 and i < 7:
                continue
            assert comm_norm(ops[i], ops[j]) > 1e-12

    # Neither force observable is QND with respect to the source Hamiltonian.
    g0 = grad_probe(0.0)
    g1 = grad_probe(Y1)
    qnd0 = comm_norm(g0, H) / np.linalg.norm(g0, ord="fro")
    qnd1 = comm_norm(g1, H) / np.linalg.norm(g1, ord="fro")
    print("||[G0,H]||/||G0||", qnd0)
    print("||[G1,H]||/||G1||", qnd1)
    assert abs(qnd0 - 1.905640565091318) < 1e-12
    assert abs(qnd1 - 1.0586202280381902) < 1e-12

    # Best4 endpoint compatibility.
    ep = best4_endpoint_operators()
    ep_commuting = 0
    ep_noncommuting = 0
    for i in range(len(ep)):
        for j in range(i + 1, len(ep)):
            c = comm_norm(ep[i][2], ep[j][2])
            if c < 1e-12:
                ep_commuting += 1
            else:
                ep_noncommuting += 1
    distinct_times = len({round(x[1], 12) for x in ep})
    print("best4 endpoints", len(ep), "distinct time layers", distinct_times,
          "commuting/noncommuting pairs", ep_commuting, ep_noncommuting)
    assert len(ep) == 6
    assert distinct_times == 4
    assert ep_commuting == 2
    assert ep_noncommuting == 13

    # Optimistic shared-output requirement if the N_BEST4_COV covariance
    # trajectories could also carry the entire centered mean/control Fisher.
    i_mean, xi_mean = per_cycle_requirement(GAMMA_MEAN_D2, N_BEST4_COV)
    i_tau, xi_tau = per_cycle_requirement(1.0 / SIGMA_TAU_D2**2, N_BEST4_COV)
    i_bm, xi_bm = per_cycle_requirement(1.0 / SIGMA_BMEAN_D2**2, N_BEST4_COV)
    i_bc, xi_bc = per_cycle_requirement(1.0 / SIGMA_BCOV_D2**2, N_BEST4_COV)

    print("optimistic per-cycle standardized requirements")
    print(" mean row I,xi", i_mean, xi_mean)
    print(" timing I,xi", i_tau, xi_tau)
    print(" mean-offset reference I,xi", i_bm, xi_bm)
    print(" cov-offset reference I,xi", i_bc, xi_bc)

    assert abs(i_mean - 1.550738230923174) < 1e-12
    assert abs(xi_mean - 1.2452864051788144) < 1e-12
    assert abs(i_tau - 0.0254116785488375) < 1e-12
    assert abs(xi_tau - 0.15941040916087476) < 1e-12
    assert abs(i_bm - 155.07371983757287) < 1e-9
    assert abs(xi_bm - 12.452859905964287) < 1e-12
    assert abs(i_bc - 49.9999242444179) < 1e-9
    assert abs(xi_bc - 7.071062455134864) < 1e-12


if __name__ == "__main__":
    main()
