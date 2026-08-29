"""RQIR Iteration 036: revalidate low-rank control/systematics on the centered-noise likelihood.

Iteration 034 replaced the raw symmetrized second-moment Fisher rows by the
correct centered covariance derivative and updated the normalized D1/D2 90%
calibration weights. This script reruns the Iteration-016 low-rank systematics
logic and the Iteration-023 transparent timing-drift cadence on that corrected
basis.

The structural claim RQIR-NG-006 should survive: unconstrained calibration
systematics remain detector-degenerate even at large calibration exposure.
Numerical timing/additive priors are allowed to change.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import numpy as np

# Centered 90%-retention group weights from Iteration 034 (900-point scan).
D1_GM = 1265715.0053913328
D1_GC = 621782.9039627119
D2_GM = 1830264.702984567
D2_GC = 590127.2924902999


def load(name: str, filename: str):
    path = Path(__file__).resolve().parent / filename
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def centered_sym_derivative(i26, a, b):
    rho0 = np.eye(i26.D) / i26.D
    ma = np.trace(rho0 @ a)
    mb = np.trace(rho0 @ b)
    return i26.sym(a, b) - mb * a - ma * b


def centered_groups(i26, y1=None, dt=0.0, return_raw=False):
    if y1 is None:
        y1 = i26.Y1
    ops = [i26.probe(0.0), i26.probe(float(y1))]
    tt = i26.TIMES + dt
    tr = i26.TR + dt

    means = []
    for k in (0, 1):
        for t in tt:
            means.append(i26.herm_vec(i26.evolve(ops[k], float(t))))

    cov = [i26.herm_vec(centered_sym_derivative(i26, i26.evolve(ops[0], tr), ops[0]))]
    extra = [
        (0, 1, tt[1]),
        (1, 1, tt[5]),
        (1, 0, tr),
        (0, 1, tr),
        (1, 0, tt[3]),
        (0, 0, tt[6]),
        (0, 1, tt[6]),
    ]
    for k, l, t in extra:
        cov.append(i26.herm_vec(centered_sym_derivative(i26, i26.evolve(ops[k], float(t)), ops[l])))

    means = np.vstack(means)
    cov = np.vstack(cov)
    if return_raw:
        return means, cov
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


def drift_vectors(i26, theta0, step=1e-5):
    mp, cp = centered_groups(i26, i26.Y1 + step, 0.0)
    mm, cm = centered_groups(i26, i26.Y1 - step, 0.0)
    dy_m = (mp - mm) / (2.0 * step)
    dy_c = (cp - cm) / (2.0 * step)

    mp, cp = centered_groups(i26, i26.Y1, step)
    mm, cm = centered_groups(i26, i26.Y1, -step)
    dt_m = (mp - mm) / (2.0 * step)
    dt_c = (cp - cm) / (2.0 * step)

    vy = np.r_[dy_m @ theta0, dy_c @ theta0]
    vt = np.r_[dt_m @ theta0, dt_c @ theta0]
    return vy, vt


def conservative_sigmas(vy, vt, gm, gc, fraction=0.1):
    sm = 1.0 / np.sqrt(gm)
    sc = 1.0 / np.sqrt(gc)

    def one(col):
        return min(
            fraction * sm / np.max(np.abs(col[:14])),
            fraction * sc / np.max(np.abs(col[14:])),
        )

    return np.array([
        one(vy),
        one(vt),
        fraction * sm,
        fraction * sc,
    ])


def retained(s, bu, Azu, Vsys, gm, gc, prior_precision, scale=1.0):
    w = np.r_[np.full(14, gm * scale), np.full(8, gc * scale)]
    fuu = bu.T @ bu + Azu.T @ (w[:, None] * Azu)
    fuz = Azu.T @ (w[:, None] * Vsys)
    fzz = Vsys.T @ (w[:, None] * Vsys) + np.diag(prior_precision)
    N = np.block([[fuu, fuz], [fuz.T, fzz]])
    cross = np.concatenate([s @ bu, np.zeros(Vsys.shape[1])])
    return float(s @ s - cross @ np.linalg.solve(N, cross))


def timing_reference_block_s(target_us, i26, sigma_event_us=10.0,
                             acceptance=0.5, dead_time_s=1e-3):
    t_coh = float(np.max(i26.TIMES)) / (2.0 * np.pi * 100.0)
    t_cycle = t_coh + dead_time_s
    sigma_ref_us = target_us / 3.0
    return t_cycle / acceptance * (sigma_event_us / sigma_ref_us) ** 2


def cadence_hours(target_us, diffusion_us2_per_h, sigma_ref_fraction=1.0 / 3.0,
                  floor_us=0.0):
    sigma_ref = sigma_ref_fraction * target_us
    numerator = target_us**2 - floor_us**2 - sigma_ref**2
    if numerator <= 0:
        return 0.0
    return 2.0 * numerator / diffusion_us2_per_h


def main():
    i26 = load("rqir_i26", "d2_calibration_branch_fisher_iteration026.py")
    pack = i26.build()
    _A, _labels, _G, theta0, B2, s2, _Z, Zu, _sv = pack

    means, cov = centered_groups(i26)
    Azu = np.vstack([means, cov]) @ Zu
    vy, vt = drift_vectors(i26, theta0)
    bmean = np.r_[np.ones(14), np.zeros(8)]
    bcov = np.r_[np.zeros(14), np.ones(8)]
    Vsys = np.column_stack([vy, vt, bmean, bcov])

    d1 = d1_detector(i26, pack)
    d2 = (s2, B2 @ Zu)

    results = {}
    for name, (s, bu), gm, gc in [
        ("D1", d1, D1_GM, D1_GC),
        ("D2", d2, D2_GM, D2_GC),
    ]:
        no_prior = [retained(s, bu, Azu, Vsys, gm, gc, [0, 0, 0, 0], scale=x)
                    for x in (1.0, 2.0, 10.0, 100.0)]
        sig = conservative_sigmas(vy, vt, gm, gc)
        f = retained(s, bu, Azu, Vsys, gm, gc, 1.0 / sig**2)
        timing_us = sig[1] / (2.0 * np.pi * 100.0) * 1e6
        results[name] = (no_prior, sig, f, timing_us)
        print(name, "no-prior", no_prior)
        print(name, "sigmas [dy,dtau,bmean,bcov]", sig)
        print(name, "retained with bundle", f)
        print(name, "timing target us @100Hz", timing_us)

    # Undo row normalization for additive-offset bookkeeping.
    raw_m, raw_c = centered_groups(i26, return_raw=True)
    mnorm = np.linalg.norm(raw_m, axis=1)
    cnorm = np.linalg.norm(raw_c, axis=1)
    for name in ("D1", "D2"):
        sig = results[name][1]
        print(name, "raw centered mean offset range", mnorm.min() * sig[2], mnorm.max() * sig[2])
        print(name, "raw centered cov offset range", cnorm.min() * sig[3], cnorm.max() * sig[3])

    # Revalidate the transparent Iteration-023 timing drift benchmark.
    for name in ("D1", "D2"):
        target_us = results[name][3]
        print(name, "reference block s", timing_reference_block_s(target_us, i26))
        for Ddiff in (100.0, 1000.0):
            dh = cadence_hours(target_us, Ddiff)
            print(name, "D", Ddiff, "cadence h", dh, "minutes", 60.0 * dh)

    ratio = (results["D2"][3] / results["D1"][3]) ** 2
    print("equal-diffusion D2/D1 cadence ratio", ratio)

    # Regression guards.
    d1_np, d1_sig, d1_f, d1_t = results["D1"]
    d2_np, d2_sig, d2_f, d2_t = results["D2"]
    assert max(abs(x) for x in d1_np) < 2e-8
    assert max(abs(x) for x in d2_np) < 2e-8
    assert abs(d1_f - 0.8999153331523331) < 2e-10
    assert abs(d2_f - 0.8998934448185817) < 2e-10
    assert abs(d1_t - 11.051087331601504) < 2e-10
    assert abs(d2_t - 9.190010830110957) < 2e-10
    assert abs(d1_sig[2] - 8.88857284e-05) < 2e-13
    assert abs(d1_sig[3] - 1.26817916e-04) < 2e-12
    assert abs(d2_sig[2] - 7.39167814e-05) < 2e-13
    assert abs(d2_sig[3] - 1.30174869e-04) < 2e-12

    assert abs(timing_reference_block_s(d1_t, i26) - 0.13181193160052496) < 2e-12
    assert abs(timing_reference_block_s(d2_t, i26) - 0.1906043025586689) < 2e-12
    assert abs(cadence_hours(d1_t, 100.0) - 2.171138332634369) < 2e-12
    assert abs(cadence_hours(d2_t, 100.0) - 1.5014453165787853) < 2e-12
    assert abs(ratio - 0.691547514043932) < 2e-12


if __name__ == "__main__":
    main()
