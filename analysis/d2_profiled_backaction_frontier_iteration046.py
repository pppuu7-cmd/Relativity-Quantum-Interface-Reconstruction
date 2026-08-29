"""RQIR Iteration 046: full hard-constrained profiled D2 backaction frontier.

Iteration 044 bounded same-copy mean information using raw detector-signal
attenuation.  This script propagates the same ideal reciprocal-linear/dephasing
proxy through the complete 22D hard-constrained detector nuisance Jacobian and
recomputes F_beta|theta for the centered complementary best4 branch at y_ref=-4.

The calibration likelihood is granted unchanged while the science detector
Jacobian is dephased.  This is optimistic: a true shared trajectory would also
modify calibration score vectors and add measurement-noise/backaction nuisance.
Therefore failure here is a strong negative diagnostic, while success would
still require a fuller stochastic detector model.
"""
from __future__ import annotations

import math
import numpy as np

import physical_coordinate_centered_covariance_audit_iteration034 as i34
import d2_information_backaction_proxy_iteration043 as i43

TARGET = 0.90
BEST4 = (0, 1, 3, 7)


def build_model():
    i26 = i34.load("rqir_i26_for_i46", "d2_calibration_branch_fisher_iteration026.py")
    pack = i26.build()
    _A, _labels, _G, theta0, B, s, _Z, Zu, _sv = pack

    # Recompute the preferred centered D2 gamma_mean/gamma_cov benchmark.
    pm, pc = i34.operator_rows(i26, [i26.probe(0.0), i26.probe(i26.Y1)], centered=True)
    d2 = i34.optimize_groups(s, B @ Zu, Zu, pm, pc)
    _cost, gm, gc = d2[1]

    # Current complementary branch at y_ref=-4 with best4 force covariance.
    yref = -4.0
    rm, rc = i34.operator_rows(
        i26,
        [i26.probe(0.0) - i26.probe(yref),
         i26.probe(i26.Y1) - i26.probe(yref)],
        centered=True,
    )
    fm, fc = i34.operator_rows(
        i26,
        [i26.grad_probe(0.0), i26.grad_probe(i26.Y1)],
        centered=True,
    )
    means = np.vstack([rm, fm])
    cov = np.vstack([rc] + [fc[j][None, :] for j in BEST4])
    return i26, pack, means, cov, float(gm), float(gc)


def dephasing_superoperator(i26, zeta: float) -> np.ndarray:
    g0 = i26.grad_probe(0.0)
    g1 = i26.grad_probe(i26.Y1)
    m0 = g0 / np.linalg.norm(g0, ord="fro")
    m1 = g1 / np.linalg.norm(g1, ord="fro")
    E = np.zeros((i26.D * i26.D, i26.D * i26.D), float)
    for j in range(i26.D * i26.D):
        e = np.zeros(i26.D * i26.D)
        e[j] = 1.0
        op = i26.mat(e)
        out = i43.dephase(i43.dephase(op, m0, zeta), m1, zeta)
        E[:, j] = i26.herm_vec(out)
    return E


def profiled(model, xi: float, c_alpha: float, scale: float = 1.0,
             eta: float = 1.0) -> tuple[float, float]:
    i26, pack, means, cov, gm, gc = model
    _A, _labels, _G, theta0, B, _s, _Z, Zu, _sv = pack
    zeta = xi * xi / (4.0 * eta)
    E = dephasing_superoperator(i26, zeta)
    Bd = B @ E
    sd = Bd @ theta0

    Jd = np.column_stack([sd, sd, Bd @ Zu])
    F = Jd.T @ Jd

    M = np.vstack([means, cov])
    W = np.r_[np.full(len(means), gm), np.full(len(cov), gc)] * scale
    Jc = np.column_stack([M @ theta0, M @ Zu])
    F[1:, 1:] += Jc.T @ (W[:, None] * Jc)
    F[1, 1] += c_alpha

    N = F[1:, 1:]
    c = F[0, 1:]
    fb = float(F[0, 0] - c @ np.linalg.solve(N, c))
    return fb, float(F[0, 0])


def min_calpha(model, xi: float, scale: float = 1.0,
               eta: float = 1.0) -> float:
    f = lambda ca: profiled(model, xi, ca, scale, eta)[0]
    if f(0.0) >= TARGET:
        return 0.0
    if f(1e12) < TARGET:
        return math.inf
    lo, hi = 0.0, 1.0
    while f(hi) < TARGET:
        hi *= 10.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if f(mid) >= TARGET:
            hi = mid
        else:
            lo = mid
    return hi


def min_scale(model, xi: float, c_alpha: float,
              eta: float = 1.0) -> float:
    f = lambda lam: profiled(model, xi, c_alpha, lam, eta)[0]
    if f(1.0) >= TARGET:
        return 1.0
    if f(1e8) < TARGET:
        return math.inf
    lo, hi = 1.0, 2.0
    while f(hi) < TARGET:
        hi *= 2.0
    for _ in range(100):
        mid = math.sqrt(lo * hi)
        if f(mid) >= TARGET:
            hi = mid
        else:
            lo = mid
    return hi


def max_xi_strong_prep(model, scale: float = 1.0,
                       eta: float = 1.0) -> float:
    f = lambda x: profiled(model, x, 1e12, scale, eta)[0]
    lo, hi = 0.0, 2.0
    if f(0.0) < TARGET:
        return 0.0
    while f(hi) >= TARGET:
        hi *= 2.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if f(mid) >= TARGET:
            lo = mid
        else:
            hi = mid
    return lo


def main() -> None:
    model = build_model()
    _i26, _pack, _means, _cov, gm, gc = model
    print("centered gm/gc", gm, gc)
    assert abs(gm - 1830264.702984567) < 2e-6
    assert abs(gc - 590127.2924902983) < 2e-6

    # Unperturbed best4 branch and its minimal residual source prior.
    f0, fbb0 = profiled(model, 0.0, 0.0)
    c0 = min_calpha(model, 0.0)
    f0c, _ = profiled(model, 0.0, c0)
    print("baseline F no prep", f0, "C_alpha90", c0, "F with C*", f0c)
    assert abs(f0 - 0.8994767689611344) < 3e-12
    assert abs(c0 - 0.05006143859980483) < 3e-12
    assert abs(f0c - TARGET) < 3e-12
    assert abs(fbb0 - 1.0) < 3e-12

    # With current calibration scale, even infinitely strong amplitude metrology
    # cannot keep the profiled target once xi exceeds ~0.7001.
    xcrit = max_xi_strong_prep(model, 1.0, 1.0)
    fcrit, fbbcrit = profiled(model, xcrit, 1e12)
    print("xi critical at lambda=1,strong prep", xcrit,
          "I", xcrit*xcrit, "Fprofile", fcrit, "Fbb", fbbcrit)
    assert abs(xcrit - 0.7001012922938202) < 3e-12
    assert abs(xcrit*xcrit - 0.4901418194714771) < 3e-12
    assert abs(fcrit - TARGET) < 3e-10
    assert abs(fbbcrit - 0.9061462209963413) < 3e-12

    # Preparation burden at fixed calibration exposure rises sharply.
    expected_ca = {
        0.1: 0.21086589748023954,
        0.2: 0.7361838487125212,
        0.3: 1.786896007030798,
        0.4: 3.7929231529763356,
        0.5: 8.091366088110298,
        0.6: 21.42108729448109,
        0.65: 48.311435497228665,
        0.68: 128.84597578464516,
    }
    for xi, expected in expected_ca.items():
        ca = min_calpha(model, xi)
        print("xi", xi, "C_alpha90(lambda=1)", ca)
        assert abs(ca - expected) < 2e-9

    # Alternatively retain the old residual source prior and pay more
    # gravitational calibration exposure.
    expected_lam = {
        0.1: 1.0186605305873464,
        0.2: 1.079273055061552,
        0.3: 1.1989303492667658,
        0.4: 1.421707986346658,
        0.5: 1.8754244549655623,
        0.6: 3.1059318123243145,
        0.65: 4.991794419631671,
        0.68: 8.192382244848675,
        0.7: 14.782531524904865,
    }
    for xi, expected in expected_lam.items():
        lam = min_scale(model, xi, c0)
        print("xi", xi, "lambda90(C_alpha=C0)", lam)
        assert abs(lam - expected) < 2e-9

    # Current optimistic shared targets are impossible at 90% irrespective of
    # preparation/calibration because their detector-only Fbb is already below 0.9.
    for xi, expected_fbb in [
        (i43.XI_SHARED_N4, 0.7343881235771952),
        (i43.XI_MEAN_COV_CROSS, 0.24349302016306754),
    ]:
        fb_inf, fbb = profiled(model, xi, 1e12, 1e8)
        print("large-resource xi", xi, "Fprofile", fb_inf, "Fbb", fbb)
        assert abs(fbb - expected_fbb) < 3e-10
        assert fbb < TARGET
        assert fb_inf <= fbb + 1e-10

    # Maximum optimistic shared fraction at lambda=1 even with perfect source
    # amplitude metrology.
    n4 = 1.180254e6
    shared_mean = n4 * xcrit * xcrit
    frac = shared_mean / gm
    print("max lambda=1 strong-prep shared mean Fisher/row", shared_mean,
          "fraction of gamma_mean", frac)
    assert abs(shared_mean - 578491.8429984888) < 2e-6
    assert abs(frac - 0.31606999150313686) < 2e-12


if __name__ == "__main__":
    main()
