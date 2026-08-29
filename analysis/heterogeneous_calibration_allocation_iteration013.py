"""RQIR Iteration 013: heterogeneous calibration Fisher allocation.

Reuses the Iteration-012 physical resource model but replaces scalar gamma by
separate information strengths for the 14 potential-mean rows and 8
symmetrized-covariance rows. Trace normalization and source-energy metrology
are treated as independently calibrated high-information constraints.

The script minimizes a shot-equivalent cost at fixed retained profiled
F_{beta|theta}. q_mean and q_cov are single-shot Fisher informations in a
common standardized parameterization. Results are design diagnostics, not
hardware forecasts.
"""
from __future__ import annotations
import numpy as np
import physical_resource_budget_iteration012 as r

TARGET = 0.90
N_MEAN = 14
N_COV = 8


def d2_model(base):
    vals, v, scale = r.VALS, r.V, r.SCALE
    grad = (v @ np.diag((vals / scale) ** 2) @ v.T).astype(complex)
    p0 = r.probe(0.0)
    B = np.zeros((4, r.D * r.D), float)
    for j in range(r.D * r.D):
        e = np.zeros(r.D * r.D); e[j] = 1.0
        op = r.mat(e)
        h2 = r.harmonic(op, grad, p0, 2)
        h4 = r.harmonic(op, grad, p0, 4)
        B[:, j] = [h2.real, h2.imag, h4.real, h4.imag]
    theta0 = base['theta0']
    s = B @ theta0
    B /= np.linalg.norm(s)
    s = B @ theta0
    return s, B @ base['Q']


def extended_model():
    m = r.build_model()
    # Reconstruct theta0 because Iteration-012 build_model did not return it.
    _, _, vh = np.linalg.svd(m['A'], full_matrices=True)
    n = vh[-1]
    d0 = r.mat(n)
    d0 /= np.max(np.abs(np.linalg.eigvalsh(d0)))
    m['theta0'] = 2.0 * r.EPS * r.herm_vec(d0)
    return m


def group_matrices(m):
    labels = m['labels']; ac = m['Ac']
    mean_idx = [i for i, x in enumerate(labels) if x == 'mean']
    cov_idx = [i for i, x in enumerate(labels) if x == 'cov']
    fixed_idx = [i for i, x in enumerate(labels) if x in ('trace', 'energy')]
    mm = sum(np.outer(ac[i], ac[i]) for i in mean_idx)
    mc = sum(np.outer(ac[i], ac[i]) for i in cov_idx)
    mf = 1e12 * sum(np.outer(ac[i], ac[i]) for i in fixed_idx)
    return mf, mm, mc


def profiled(ss, bu, mf, mm, mc, gamma_mean, gamma_cov):
    fuu = bu.T @ bu + mf + gamma_mean * mm + gamma_cov * mc
    cross = ss @ bu
    return float(ss @ ss - cross @ np.linalg.pinv(fuu, rcond=1e-12) @ cross)


def required_cov(ss, bu, mats, gamma_mean, target=TARGET):
    mf, mm, mc = mats
    lo, hi = 1e1, 1e10
    if profiled(ss, bu, mf, mm, mc, gamma_mean, hi) < target:
        return np.inf
    for _ in range(35):
        mid = np.sqrt(lo * hi)
        if profiled(ss, bu, mf, mm, mc, gamma_mean, mid) >= target:
            hi = mid
        else:
            lo = mid
    return hi


def uniform_threshold(ss, bu, mats, target=TARGET):
    mf, mm, mc = mats
    lo, hi = 1e2, 1e9
    for _ in range(50):
        mid = np.sqrt(lo * hi)
        if profiled(ss, bu, mf, mm, mc, mid, mid) >= target:
            hi = mid
        else:
            lo = mid
    return hi


def optimize_groups(ss, bu, mats, q_cov_over_q_mean=1.0, target=TARGET):
    q = float(q_cov_over_q_mean)
    gu = uniform_threshold(ss, bu, mats, target)
    uniform_cost = (N_MEAN + N_COV / q) * gu
    best = (uniform_cost, gu, gu)
    for gm in np.logspace(3, 8, 450):
        gc = required_cov(ss, bu, mats, float(gm), target)
        if not np.isfinite(gc):
            continue
        cost = N_MEAN * gm + N_COV * gc / q
        if cost < best[0]:
            best = (float(cost), float(gm), float(gc))
    return gu, best, uniform_cost / best[0]


def main():
    m = extended_model(); mats = group_matrices(m)
    d1 = (m['s'], m['Bu'])
    d2 = d2_model(m)
    for name, branch in [('D1', d1), ('D2', d2)]:
        print(name)
        for q in [0.1, 1.0, 10.0]:
            gu, best, gain = optimize_groups(*branch, mats, q_cov_over_q_mean=q)
            print(' q_cov/q_mean=', q,
                  'uniform_gamma=', gu,
                  'optimal_cost=', best[0],
                  'gamma_mean=', best[1],
                  'gamma_cov=', best[2],
                  'cost_gain=', gain)

    # Regression guards around the recorded q=1 results.
    g1, b1, gain1 = optimize_groups(*d1, mats, q_cov_over_q_mean=1.0)
    g2, b2, gain2 = optimize_groups(*d2, mats, q_cov_over_q_mean=1.0)
    assert 1.45e6 < g1 < 1.65e6
    assert 5.0e6 < b1[0] < 5.8e6
    assert 5.5 < gain1 < 7.0
    assert 2.0e6 < g2 < 2.3e6
    assert 9.0e6 < b2[0] < 1.2e7
    assert 4.0 < gain2 < 5.2


if __name__ == '__main__':
    main()
