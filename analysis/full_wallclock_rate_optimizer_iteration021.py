"""RQIR Iteration 021 — parametric full wall-clock Fisher-rate optimizer.

This iteration closes a methodological gap after Iterations 019-020.  Detector
(D1/D2) and preparation rates now have physical/native forms, but gravitational
mean/covariance calibration and reference-control channels still lack hardware-
specific Fisher rates.  Therefore a unique wall-clock optimum cannot yet be
claimed.

The script performs the exact hard-constrained (Iteration-015) local Fisher
optimization for four resource pools:
  detector, independent source-preparation metrology, mean calibration,
  covariance calibration.
Rates are supplied as ratios per wall second.  The output is therefore a map
from measurable rate ratios to the optimal allocation, not a hardware forecast.

Systematic-control priors from Iteration 016 are intentionally not assigned an
invented seconds-to-prior conversion here; they remain an additional mandatory
resource.  The next hardware layer must provide those rates explicitly.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.optimize import differential_evolution

import hard_constraint_fisher_audit_iteration015 as hc
import heterogeneous_calibration_allocation_iteration013 as het


def model():
    m, im, ic, z, acz, bu1 = hc.reduced_model()
    s2, bu2 = hc.d2_reduced(m, z)
    am = acz[im]
    av = acz[ic]
    return (m['s'], bu1), (s2, bu2), am, av


def softmax(y):
    y = np.asarray(y, float)
    e = np.exp(y - np.max(y))
    return e / np.sum(e)


def profiled_rate(fractions, branch, rates, am, av):
    """Profiled beta Fisher per unit total wall time.

    rates=(R_D,R_P,R_mean,R_cov).  The detector local model has unit
    detector-only Fisher per unit detector information.  R_P is independent
    Fisher on the hidden amplitude a.  R_mean/R_cov are row-normalized
    calibration Fisher rates in the exact hard-constrained basis.
    """
    xD, xP, xM, xC = map(float, fractions)
    RD, RP, RM, RC = map(float, rates)
    s, bu = branch

    S = RD * xD
    Ca = RP * xP
    gm = RM * xM
    gc = RC * xC

    # parameters = [beta, a, u_1 ... u_22]
    J = np.column_stack([s, s, bu])
    F = S * (J.T @ J)
    F[1, 1] += Ca
    F[2:, 2:] += gm * (am.T @ am) + gc * (av.T @ av)

    N = F[1:, 1:]
    c = F[0, 1:]
    try:
        return float(F[0, 0] - c @ np.linalg.solve(N, c))
    except np.linalg.LinAlgError:
        return 0.0


def optimize(branch, rates, am, av, seed=20260829):
    def objective(y):
        return -profiled_rate(softmax(y), branch, rates, am, av)
    res = differential_evolution(objective, [(-8.0, 8.0)] * 4,
                                 seed=seed, tol=1e-10, polish=True)
    x = softmax(res.x)
    return x, -float(res.fun)


def square_root_limit(rp_over_rd):
    q = math.sqrt(float(rp_over_rd))
    return np.array([q / (1.0 + q), 1.0 / (1.0 + q)])


def main():
    d1, d2, am, av = model()
    branches = {'D1': d1, 'D2': d2}

    # Dimensionless rate-ratio map.  RD=1 defines the clock unit only.
    print('rate columns: RP/RD, Rcal/RD; allocation=[D,P,mean,cov]; F/T')
    for name, branch in branches.items():
        print('\n' + name)
        for rp in (1.0, 10.0, 100.0):
            for rcal in (1e4, 1e6, 1e8):
                x, f = optimize(branch, (1.0, rp, rcal, rcal), am, av)
                print(rp, rcal, np.round(x, 6), f)

    # Regression: when calibration becomes effectively free the exact
    # four-resource solution must approach the Iteration-018 two-resource
    # square-root detector/preparation allocation.
    for rp in (1.0, 10.0, 100.0):
        x, _ = optimize(d1, (1.0, rp, 1e12, 1e12), am, av)
        lim = square_root_limit(rp)
        assert np.max(np.abs(x[:2] - lim)) < 5e-4
        assert x[2] + x[3] < 1e-3

    # Stored benchmark guards (rate-ratio diagnostics, not hardware claims).
    x1, f1 = optimize(d1, (1.0, 10.0, 1e6, 1e6), am, av)
    x2, f2 = optimize(d2, (1.0, 10.0, 1e6, 1e6), am, av)
    assert np.max(np.abs(x1 - np.array([0.56086,0.17265,0.18805,0.07845]))) < 3e-3
    assert np.max(np.abs(x2 - np.array([0.5393,0.1666,0.2251,0.0690]))) < 4e-3
    assert 0.295 < f1 < 0.301
    assert 0.274 < f2 < 0.281


if __name__ == '__main__':
    main()
