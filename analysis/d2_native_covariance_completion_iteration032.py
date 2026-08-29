"""RQIR Iteration 032: fully native D2 covariance/calibration completion audit.

Motivation
----------
Iteration 026 called one branch `native_replace`, but only the 14 mean rows were
replaced by force-gradient observables; its 8 covariance/noise rows were still
built from the old potential operator family. Iterations 030-031 then showed
that D2 physical observables must be transformed consistently (finite-reference
potential differences rather than undeclared absolute potentials).

This iteration therefore asks two consistency questions on the same corrected
hard trace+energy constrained Toy009/Iteration-011 source space:

1. What happens if BOTH D2 mean and covariance calibration rows are genuinely
   force-native?
2. If relational-potential and force observables are used complementarily, how
   much detector-level Fisher is recovered when their covariance information is
   also supplied consistently?

The script does not assign SI covariance rates. Row weights GM/GC remain the
corrected Iteration-015 local benchmark. The purpose is to expose observable-
family consistency and identify which covariance rows are most informative
before wall-clock rates are attached.
"""
from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path
import numpy as np

TARGET = 0.90


def load(name: str, filename: str):
    path = Path(__file__).resolve().parent / filename
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def operator_rows(i26, ops):
    """Return row-normalized 14 mean + 8 covariance rows for two operators."""
    means = []
    for k in (0, 1):
        for t in i26.TIMES:
            means.append(i26.herm_vec(i26.evolve(ops[k], float(t))))

    cov = [i26.herm_vec(i26.sym(i26.evolve(ops[0], i26.TR), ops[0]))]
    extra = [
        (0, 1, i26.TIMES[1]),
        (1, 1, i26.TIMES[5]),
        (1, 0, i26.TR),
        (0, 1, i26.TR),
        (1, 0, i26.TIMES[3]),
        (0, 0, i26.TIMES[6]),
        (0, 1, i26.TIMES[6]),
    ]
    for k, l, t in extra:
        cov.append(i26.herm_vec(i26.sym(i26.evolve(ops[k], float(t)), ops[l])))

    means = np.vstack(means)
    cov = np.vstack(cov)
    means /= np.linalg.norm(means, axis=1, keepdims=True)
    cov /= np.linalg.norm(cov, axis=1, keepdims=True)
    return means, cov


def fisher_profile(i26, pack, mean_rows, cov_rows, c_a=0.0, scale=1.0):
    A, labels, G, theta0, B, s, Z, Zu, _sv = pack
    M = np.vstack([mean_rows, cov_rows])
    W = np.r_[np.full(len(mean_rows), i26.GM), np.full(len(cov_rows), i26.GC)] * scale

    # params = beta, fractional amplitude of fixed Toy009 hidden state,
    # and 22 source nuisances orthogonal to that state.
    Jd = np.column_stack([s, s, B @ Zu])
    F = Jd.T @ Jd
    Jc = np.column_stack([M @ theta0, M @ Zu])
    F[1:, 1:] += Jc.T @ (W[:, None] * Jc)
    F[1, 1] += c_a

    N = F[1:, 1:]
    c = F[0, 1:]
    fb = float(F[0, 0] - c @ np.linalg.pinv(N, rcond=1e-13) @ c)

    MR = M @ Z
    _u, ss, vh = np.linalg.svd(MR, full_matrices=True)
    rank = int(np.sum(ss > 1e-12))
    overlap = np.nan
    alignment = np.nan
    if rank < Z.shape[1]:
        znull = Z @ vh[-1]
        znull /= np.linalg.norm(znull)
        old = theta0 / np.linalg.norm(theta0)
        bz = B @ znull
        overlap = float(abs(znull @ old))
        alignment = float(abs(s @ bz) / np.linalg.norm(bz))
    return fb, rank, float(ss[-1]), overlap, alignment


def min_ca(i26, pack, mean_rows, cov_rows, scale=1.0, target=TARGET):
    f = lambda ca: fisher_profile(i26, pack, mean_rows, cov_rows, ca, scale)[0]
    if f(0.0) >= target:
        return 0.0
    if f(1e8) < target:
        return np.inf
    lo, hi = 0.0, 1.0
    while f(hi) < target:
        hi *= 10.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if f(mid) >= target:
            hi = mid
        else:
            lo = mid
    return hi


def min_lambda_no_prep(i26, pack, mean_rows, cov_rows, target=TARGET):
    f = lambda lam: fisher_profile(i26, pack, mean_rows, cov_rows, 0.0, lam)[0]
    lo, hi = 1e-5, 1.0
    while f(hi) < target and hi < 1e5:
        hi *= 2.0
    if f(hi) < target:
        return np.inf
    for _ in range(100):
        mid = np.sqrt(lo * hi)
        if f(mid) >= target:
            hi = mid
        else:
            lo = mid
    return hi


def min_lambda_strong_prep(i26, pack, mean_rows, cov_rows, target=TARGET):
    f = lambda lam: fisher_profile(i26, pack, mean_rows, cov_rows, 1e8, lam)[0]
    lo, hi = 1e-6, 10.0
    if f(hi) < target:
        return np.inf
    for _ in range(100):
        mid = np.sqrt(lo * hi)
        if f(mid) >= target:
            hi = mid
        else:
            lo = mid
    return hi


def best_force_cov_subset(i26, pack, rel_mean, rel_cov, force_mean, force_cov, k):
    best = (-np.inf, ())
    for inds in itertools.combinations(range(len(force_cov)), k):
        cov = np.vstack([rel_cov] + [force_cov[j][None, :] for j in inds]) if inds else rel_cov
        fb = fisher_profile(i26, pack, np.vstack([rel_mean, force_mean]), cov)[0]
        if fb > best[0]:
            best = (fb, inds)
    return best


def main():
    i26 = load("rqir_i26", "d2_calibration_branch_fisher_iteration026.py")
    i30 = load("rqir_i30", "d2_finite_reference_potential_iteration030.py")
    pack = i26.build()
    A, labels, G, theta0, B, s, Z, Zu, _sv = pack
    im = np.where(labels == "mean")[0]
    ic = np.where(labels == "cov")[0]

    force_mean, force_cov = operator_rows(i26, [i26.grad_probe(0.0), i26.grad_probe(i26.Y1)])
    assert np.max(np.abs(force_mean - G)) < 1e-14

    # 1. Fully native force branch: force mean + force covariance.
    f_native = fisher_profile(i26, pack, force_mean, force_cov)
    ca_native = min_ca(i26, pack, force_mean, force_cov)
    lam_native = min_lambda_strong_prep(i26, pack, force_mean, force_cov)
    print("fully-native force mean+cov")
    print("  Fbeta(Ca=0,lambda=1)=", f_native[0])
    print("  hard rank=", f_native[1], "/23")
    print("  old-null overlap=", f_native[3])
    print("  detector alignment=", f_native[4])
    print("  Ca90(lambda=1)=", ca_native)
    print("  lambda90(strong prep)=", lam_native)

    # 2. Relational-potential + force complementary branch.
    refs = [-4.0, -5.0, -7.5, -10.0, -20.0, -50.0, -100.0, -1000.0]
    for yr in refs:
        R = i30.calibration_matrix(float(yr))
        rel_mean, rel_cov = R[im], R[ic]
        means = np.vstack([rel_mean, force_mean])

        # Previous relational augmented analogue: relational covariance only.
        f_relcov = fisher_profile(i26, pack, means, rel_cov)
        # Fully complementary covariance: relational + force covariance.
        both_cov = np.vstack([rel_cov, force_cov])
        f_both = fisher_profile(i26, pack, means, both_cov)
        ca_both = min_ca(i26, pack, means, both_cov)
        lam_both = min_lambda_no_prep(i26, pack, means, both_cov)
        print(
            f"yref={yr:8.1f} relcov_F={f_relcov[0]:.12g} bothcov_F={f_both[0]:.12g} "
            f"rank={f_both[1]}/23 Ca90={ca_both:.12g} lambda90_Ca0={lam_both:.12g}"
        )

    # 3. Row-value audit at the most favorable tested finite reference.
    yr = -4.0
    R = i30.calibration_matrix(yr)
    rel_mean, rel_cov = R[im], R[ic]
    means = np.vstack([rel_mean, force_mean])
    print("\nbest force-cov subsets at yref=-4")
    subset_results = []
    for k in range(0, 9):
        fb, inds = best_force_cov_subset(i26, pack, rel_mean, rel_cov, force_mean, force_cov, k)
        cov = np.vstack([rel_cov] + [force_cov[j][None, :] for j in inds]) if inds else rel_cov
        ca = min_ca(i26, pack, means, cov)
        subset_results.append((k, inds, fb, ca))
        print(f"  k={k} inds={inds} Fbeta={fb:.12g} Ca90={ca:.12g}")

    # Regression guards defining Iteration 032.
    assert f_native[1] == 22
    assert abs(f_native[0] - 0.019445034221592716) < 2e-12
    assert abs(f_native[3] - 0.9500334630595046) < 2e-12
    assert abs(f_native[4] - 0.9900396136066448) < 2e-12
    assert abs(ca_native - 8.294643879994588) < 2e-9
    assert abs(lam_native - 0.1537665234336622) < 2e-8

    R4 = i30.calibration_matrix(-4.0)
    m4 = np.vstack([R4[im], force_mean])
    c4 = np.vstack([R4[ic], force_cov])
    f4 = fisher_profile(i26, pack, m4, c4)
    assert f4[1] == 23
    assert abs(f4[0] - 0.8994327256877968) < 2e-12
    assert abs(min_ca(i26, pack, m4, c4) - 0.06708337269483168) < 2e-9
    assert abs(min_lambda_no_prep(i26, pack, m4, c4) - 1.0063171891975229) < 2e-8

    k4 = subset_results[4]
    assert k4[1] == (0, 1, 3, 7)
    assert abs(k4[2] - 0.8948571599212516) < 2e-12
    assert abs(k4[3] - 0.5889578884945835) < 2e-9


if __name__ == "__main__":
    main()
