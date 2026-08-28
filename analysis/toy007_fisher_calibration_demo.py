"""RQIR Fisher calibration demo based on the accepted Toy 007 design.

Purpose
-------
Show the distinction between:

1. exact null-pair geometry, where an added independent calibration row can
   eliminate a nonzero state-difference nullspace; and
2. statistical inference geometry, where an additional beta-blind calibration
   measurement constrains nuisance source coordinates and cannot reduce the
   profiled Fisher information for the interface parameter beta under the
   stated local-Gaussian assumptions.

This script reconstructs Toy 007, computes the accepted 24x25 normalized
calibration matrix, and studies a scalar target measurement

    y_R = beta + r^T theta + noise,

with theta the 25-dimensional Hermitian source-state nuisance coordinate.
With rank(A)=24 and response vector r having a nonzero projection on ker(A),
beta is locally unidentifiable. Adding a calibration row with nonzero overlap
with the null direction restores positive profiled information.

The numerical example is illustrative statistical geometry, not a detector
forecast.
"""

from __future__ import annotations

import numpy as np

from rank_conditioning_scan import (
    herm_vec,
    reconstruct_toy005_source,
    evolve,
    sym_op,
    comm_op,
)


def build_toy007():
    _, h, b = reconstruct_toy005_source(seed=105)
    vals, v = np.linalg.eigh(b.real)
    length_scale = float(vals.max())
    x_sites = length_scale / vals

    def probe_operator(y: float) -> np.ndarray:
        weights = 1.0 / np.abs(x_sites - y)
        return (v @ np.diag(weights) @ v.T).astype(complex)

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
    probes = [probe_operator(y0), probe_operator(y1)]

    rows = [herm_vec(np.eye(5)), herm_vec(h)]
    for k in (0, 1):
        for t in times:
            rows.append(herm_vec(evolve(h, probes[k], float(t))))

    rows.append(herm_vec(sym_op(evolve(h, probes[0], t_response), probes[0])))
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
        rows.append(herm_vec(sym_op(evolve(h, probes[k], float(t)), probes[l])))

    a = np.vstack(rows)
    a_norm = a / np.linalg.norm(a, axis=1, keepdims=True)
    response = herm_vec(comm_op(evolve(h, probes[0], t_response), probes[0]))
    r_hat = response / np.linalg.norm(response)
    return h, x_sites, probe_operator, probes, t_response, a_norm, r_hat


def profiled_information(a_white: np.ndarray, r_hat: np.ndarray) -> float:
    """Profile Fisher info for beta in y_R = beta + r^T theta + unit noise.

    Calibration rows are already whitened and have zero beta derivative.
    The target response datum has unit beta derivative and nuisance derivative
    r_hat.  Moore-Penrose inversion handles singular nuisance Fisher blocks.
    """
    f_tt = a_white.T @ a_white + np.outer(r_hat, r_hat)
    f_bt = r_hat
    f_bb = 1.0
    out = f_bb - f_bt @ np.linalg.pinv(f_tt, rcond=1e-12) @ f_bt
    # Numerical roundoff can produce a tiny negative number around zero.
    return float(max(out, 0.0))


def main():
    h, x_sites, probe_operator, probes, t_response, a_norm, r_hat = build_toy007()
    _, singular, vh = np.linalg.svd(a_norm, full_matrices=True)
    rank = int(np.sum(singular > 1e-10))
    null_vec = vh[-1]
    null_vec /= np.linalg.norm(null_vec)
    eta = abs(float(r_hat @ null_vec))

    base_info = profiled_information(a_norm, r_hat)

    # Row used in the earlier exact-rank closure observation.
    t_peak = 3.64030
    a_peak = herm_vec(evolve(h, probes[0], t_peak))
    a_peak /= np.linalg.norm(a_peak)
    overlap_peak = abs(float(a_peak @ null_vec))

    # Search a coarse physically interpretable Newtonian mean-probe grid for a
    # calibration row with stronger overlap with the old null direction.
    ys = np.concatenate([
        np.linspace(-10.0, -0.1, 120),
        np.linspace(6.0, 12.0, 60),
    ])
    ts = np.linspace(0.0, 2.0 * np.pi, 241)
    best = (0.0, None, None, None)
    for y in ys:
        p = probe_operator(float(y))
        for t in ts:
            row = herm_vec(evolve(h, p, float(t)))
            row /= np.linalg.norm(row)
            overlap = abs(float(row @ null_vec))
            if overlap > best[0]:
                best = (overlap, float(y), float(t), row)

    overlap_best, y_best, t_best, row_best = best

    print("Toy 007 calibration rank:", rank, "/ 25")
    print("response null overlap eta_R:", eta)
    print("profiled Fisher before extra calibration:", base_info)
    print("peak-time extra-row null overlap:", overlap_peak)
    print("best grid null overlap:", overlap_best)
    print("best grid y,t:", y_best, t_best)

    print("\nweight  profile_info_peak  profile_info_best")
    for weight in (1e-4, 1e-3, 1e-2, 1e-1, 1.0, 10.0, 100.0, 1000.0):
        a1 = np.vstack([a_norm, np.sqrt(weight) * a_peak])
        a2 = np.vstack([a_norm, np.sqrt(weight) * row_best])
        print(
            f"{weight:8g}",
            f"{profiled_information(a1, r_hat):.12g}",
            f"{profiled_information(a2, r_hat):.12g}",
        )

    assert rank == 24
    assert abs(eta - 0.457681964065791) < 1e-10
    assert base_info < 1e-10
    assert overlap_peak > 0.0
    assert overlap_best > 0.2
    assert profiled_information(np.vstack([a_norm, row_best]), r_hat) > 1e-6


if __name__ == "__main__":
    main()
