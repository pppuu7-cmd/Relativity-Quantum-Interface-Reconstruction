"""RQIR Iteration 034: physical-coordinate and centered-covariance Fisher audit.

Two resource-layer coordinate issues are corrected before attaching further
physical D2 covariance rates:

1. Iteration 020 computed QFI for the physical single-branch amplitude
       rho(a) = I/D + a Delta0
   at a=EPS=0.08, whereas Iterations 026+ use a *fractional* hidden-amplitude
   nuisance alpha with a = EPS * alpha. Fisher information must transform with
   the parameter Jacobian: F_alpha = EPS**2 F_a.

2. Exact Toy009/Toy010 covariance equality could be represented by raw
   symmetrized second-moment rows because all relevant mean differences were
   constrained exactly. In a noisy Fisher model, the physical symmetrized
   noise kernel is centered. For a symmetric state pair about rho0=I/D,

     Delta N_AB = Tr[Delta rho ( sym(A,B) - <A>0 B - <B>0 A )],

   up to an identity term annihilated by trace-zero perturbations.

The exact nullspace is unchanged because the centered-row correction is a
linear combination of already-declared mean rows. The finite-noise Fisher
geometry and resource weights do change.
"""
from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path
import numpy as np

TARGET = 0.90
N_MEAN = 14
N_COV = 8


def load(name: str, filename: str):
    path = Path(__file__).resolve().parent / filename
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def centered_sym_derivative(i26, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Linear row for a centered symmetrized covariance about rho0=I/D.

    An additive identity term <A>0<B>0 I is unnecessary on the exact
    trace-zero tangent space and is omitted.
    """
    rho0 = np.eye(i26.D) / i26.D
    ma = np.trace(rho0 @ a)
    mb = np.trace(rho0 @ b)
    return i26.sym(a, b) - mb * a - ma * b


def operator_rows(i26, ops, centered: bool):
    means = []
    for k in (0, 1):
        for t in i26.TIMES:
            means.append(i26.herm_vec(i26.evolve(ops[k], float(t))))

    f = (lambda a, b: centered_sym_derivative(i26, a, b)) if centered else i26.sym
    cov = [i26.herm_vec(f(i26.evolve(ops[0], i26.TR), ops[0]))]
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
        cov.append(i26.herm_vec(f(i26.evolve(ops[k], float(t)), ops[l])))

    means = np.vstack(means)
    cov = np.vstack(cov)
    means /= np.linalg.norm(means, axis=1, keepdims=True)
    cov /= np.linalg.norm(cov, axis=1, keepdims=True)
    return means, cov


def d1_detector(i26, pack):
    _A, _labels, _G, theta0, _B2, _s2, _Z, Zu, _sv = pack
    p0 = i26.probe(0.0)
    B = np.zeros((4, i26.D * i26.D), float)
    for j in range(i26.D * i26.D):
        e = np.zeros(i26.D * i26.D)
        e[j] = 1.0
        op = i26.mat(e)
        h2 = i26.harmonic(op, p0, p0, 2)
        h4 = i26.harmonic(op, p0, p0, 4)
        B[:, j] = [h2.real, h2.imag, h4.real, h4.imag]
    s = B @ theta0
    B /= np.linalg.norm(s)
    s = B @ theta0
    return s, B @ Zu


def group_grams(Zu, mean_rows, cov_rows):
    am = mean_rows @ Zu
    av = cov_rows @ Zu
    return am.T @ am, av.T @ av


def profiled_known_amplitude(s, bu, mm, mc, gm: float, gc: float) -> float:
    fuu = bu.T @ bu + gm * mm + gc * mc
    cross = s @ bu
    return float(s @ s - cross @ np.linalg.solve(fuu, cross))


def required_cov(s, bu, mm, mc, gm: float, target: float = TARGET) -> float:
    lo, hi = 1e1, 1e12
    if profiled_known_amplitude(s, bu, mm, mc, gm, hi) < target:
        return np.inf
    for _ in range(55):
        mid = np.sqrt(lo * hi)
        if profiled_known_amplitude(s, bu, mm, mc, gm, mid) >= target:
            hi = mid
        else:
            lo = mid
    return hi


def uniform_threshold(s, bu, mm, mc, target: float = TARGET) -> float:
    lo, hi = 1e2, 1e12
    for _ in range(55):
        mid = np.sqrt(lo * hi)
        if profiled_known_amplitude(s, bu, mm, mc, mid, mid) >= target:
            hi = mid
        else:
            lo = mid
    return hi


def optimize_groups(s, bu, Zu, mean_rows, cov_rows, target: float = TARGET):
    mm, mc = group_grams(Zu, mean_rows, cov_rows)
    gu = uniform_threshold(s, bu, mm, mc, target)
    best = ((N_MEAN + N_COV) * gu, gu, gu)
    # Keep the deterministic 900-point scan convention of Iteration 015.
    for gm in np.logspace(4, 10, 900):
        gc = required_cov(s, bu, mm, mc, float(gm), target)
        if np.isfinite(gc):
            cost = N_MEAN * gm + N_COV * gc
            if cost < best[0]:
                best = (float(cost), float(gm), float(gc))
    return gu, best, (N_MEAN + N_COV) * gu / best[0]


def fisher_profile(i26, pack, mean_rows, cov_rows, gm, gc, c_alpha=0.0, scale=1.0):
    _A, _labels, _G, theta0, B, s, Z, Zu, _sv = pack
    M = np.vstack([mean_rows, cov_rows])
    W = np.r_[np.full(len(mean_rows), gm), np.full(len(cov_rows), gc)] * scale
    # beta, fractional hidden amplitude alpha, 22 orthogonal nuisances.
    Jd = np.column_stack([s, s, B @ Zu])
    F = Jd.T @ Jd
    Jc = np.column_stack([M @ theta0, M @ Zu])
    F[1:, 1:] += Jc.T @ (W[:, None] * Jc)
    F[1, 1] += c_alpha
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


def min_calpha(i26, pack, mean_rows, cov_rows, gm, gc, scale=1.0, target=TARGET):
    f = lambda ca: fisher_profile(i26, pack, mean_rows, cov_rows, gm, gc, ca, scale)[0]
    if f(0.0) >= target:
        return 0.0
    if f(1e10) < target:
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


def min_lambda_no_prep(i26, pack, mean_rows, cov_rows, gm, gc, target=TARGET):
    f = lambda lam: fisher_profile(i26, pack, mean_rows, cov_rows, gm, gc, 0.0, lam)[0]
    lo, hi = 1e-6, 1.0
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


def min_lambda_strong_prep(i26, pack, mean_rows, cov_rows, gm, gc, target=TARGET):
    f = lambda lam: fisher_profile(i26, pack, mean_rows, cov_rows, gm, gc, 1e10, lam)[0]
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


def main():
    i26 = load("rqir_i26", "d2_calibration_branch_fisher_iteration026.py")
    i20 = load("rqir_i20", "source_preparation_qfi_iteration020.py")
    pack = i26.build()
    A, labels, _G, theta0, B2, s2, Z, Zu, _sv = pack

    pot_ops = [i26.probe(0.0), i26.probe(i26.Y1)]
    pm_raw, pc_raw = operator_rows(i26, pot_ops, centered=False)
    pm_ctr, pc_ctr = operator_rows(i26, pot_ops, centered=True)

    # Exact-null geometry is preserved by centering because the correction is
    # in the span of the already-present mean rows.
    fixed = np.vstack([i26.herm_vec(np.eye(i26.D)), i26.herm_vec(i26.H)])
    fixed /= np.linalg.norm(fixed, axis=1, keepdims=True)
    AR = np.vstack([fixed, pm_raw, pc_raw])
    AC = np.vstack([fixed, pm_ctr, pc_ctr])
    _ur, sr, vhr = np.linalg.svd(AR, full_matrices=True)
    _uc, sc, vhc = np.linalg.svd(AC, full_matrices=True)
    nr = vhr[-1] / np.linalg.norm(vhr[-1])
    nc = vhc[-1] / np.linalg.norm(vhc[-1])
    print("raw/centered rank", np.linalg.matrix_rank(AR, 1e-12), np.linalg.matrix_rank(AC, 1e-12))
    print("raw/centered null overlap", abs(nr @ nc))
    print("raw/centered normalized smin", sr[-1], sc[-1])

    # Recompute the hard-constrained 90% row-weight benchmark for centered N.
    d1_s, d1_bu = d1_detector(i26, pack)
    d2_bu = B2 @ Zu
    d1 = optimize_groups(d1_s, d1_bu, Zu, pm_ctr, pc_ctr)
    d2 = optimize_groups(s2, d2_bu, Zu, pm_ctr, pc_ctr)
    print("centered D1 uniform,opt,gain", d1)
    print("centered D2 uniform,opt,gain", d2)
    _cost1, gm1, gc1 = d1[1]
    _cost2, gm2, gc2 = d2[1]

    # Fisher-coordinate correction for source preparation.
    fq_a = i20.amplitude_qfi(i26.EPS)
    fq_alpha = i26.EPS**2 * fq_a
    print("FQ_a per accepted single-branch copy", fq_a)
    print("FQ_alpha=EPS^2 FQ_a", fq_alpha)
    for detector_info in (1.0, 25.0):
        c90 = detector_info * TARGET / (1.0 - TARGET)
        n_single = c90 / fq_alpha
        n_pair = c90 / (2.0 * fq_alpha)
        print("S_D", detector_info, "C_alpha90", c90,
              "single-branch copies", n_single, "plus/minus pair equivalents", n_pair)

    # Current D2 branches after using centered covariance and the new D2
    # normalized 90% benchmark weights.
    force_ops = [i26.grad_probe(0.0), i26.grad_probe(i26.Y1)]
    fm, fc = operator_rows(i26, force_ops, centered=True)
    f_native = fisher_profile(i26, pack, fm, fc, gm2, gc2)
    ca_native = min_calpha(i26, pack, fm, fc, gm2, gc2)
    lam_native = min_lambda_strong_prep(i26, pack, fm, fc, gm2, gc2)
    print("centered fully-force-native", f_native, "C_alpha90", ca_native,
          "lambda90 strong prep", lam_native)

    # Finite-reference centered complementary branch at y_ref=-4.
    yref = -4.0
    rel_ops = [i26.probe(0.0) - i26.probe(yref),
               i26.probe(i26.Y1) - i26.probe(yref)]
    rm, rc = operator_rows(i26, rel_ops, centered=True)
    means = np.vstack([rm, fm])

    subset = {}
    for k in range(9):
        best = (-np.inf, (), np.inf, np.inf)
        for inds in itertools.combinations(range(len(fc)), k):
            cov = np.vstack([rc] + [fc[j][None, :] for j in inds]) if inds else rc
            fb = fisher_profile(i26, pack, means, cov, gm2, gc2)[0]
            if fb > best[0]:
                ca = min_calpha(i26, pack, means, cov, gm2, gc2)
                lam = min_lambda_no_prep(i26, pack, means, cov, gm2, gc2)
                best = (fb, inds, ca, lam)
        subset[k] = best
        print("centered subset", k, best)

    # Updated preparation/covariance substitution thresholds at lambda=1.
    d_first4 = subset[0][2] - subset[4][2]
    d_fifth = subset[4][2] - subset[5][2]
    th_first4 = 4.0 * gc2 / d_first4
    th_fifth = gc2 / d_fifth
    print("centered DeltaC first4/fifth", d_first4, d_fifth)
    print("centered qcov/RP break-even first4/fifth", th_first4, th_fifth)

    # Regression guards.
    assert np.linalg.matrix_rank(AR, 1e-12) == 24
    assert np.linalg.matrix_rank(AC, 1e-12) == 24
    assert abs(abs(nr @ nc) - 1.0) < 2e-12
    assert abs(sr[-1] - 0.001999540405542146) < 2e-12
    assert abs(sc[-1] - 0.0021038060838062403) < 2e-12

    assert 1.25e6 < gm1 < 1.28e6 and 0.60e6 < gc1 < 0.64e6
    assert 1.81e6 < gm2 < 1.85e6 and 0.57e6 < gc2 < 0.61e6
    assert abs(fq_a - 13.27068619) < 3e-7
    assert abs(fq_alpha - 0.0849323916) < 3e-9
    assert 105.8 < 9.0 / fq_alpha < 106.1
    assert 2648.0 < 225.0 / fq_alpha < 2651.0

    assert f_native[1] == 22
    assert 0.0194 < f_native[0] < 0.0197
    assert 7.6 < ca_native < 7.9
    assert 0.09 < lam_native < 0.11

    assert subset[4][1] == (0, 1, 3, 7)
    assert 0.8993 < subset[4][0] < 0.8997
    assert 0.04 < subset[4][2] < 0.06
    assert subset[5][1] == (0, 1, 3, 6, 7)
    assert subset[5][2] == 0.0
    assert 5.1e5 < th_first4 < 5.4e5
    assert 1.1e7 < th_fifth < 1.3e7


if __name__ == "__main__":
    main()
