#!/usr/bin/env python3
"""RQIR Iteration 106 — robust detector-side ratio certificate.

Derives matrix rather than scalar bounds on
    u = R_D,14 / R_D,09
for a common campaign schedule.  Synthetic matrices are regression tests only;
they are not apparatus forecasts.
"""
from __future__ import annotations

import itertools
import math
import numpy as np


def profiled(J: np.ndarray) -> float:
    """Scalar beta Fisher after profiling all nuisance coordinates."""
    J = np.asarray(J, dtype=float)
    a = float(J[0, 0])
    b = J[0, 1:]
    N = J[1:, 1:]
    return float(a - b @ np.linalg.solve(N, b))


def relative_loewner_bounds(J09: np.ndarray, J14: np.ndarray):
    """Return generalized-eigenvalue [alpha,beta] for positive-definite J09.

    Then alpha J09 <= J14 <= beta J09 in Loewner order.
    Singular support must be handled explicitly in a physical application.
    """
    e, Q = np.linalg.eigh(J09)
    if np.min(e) <= 0:
        raise ValueError("regression helper requires positive-definite J09")
    invsqrt = Q @ np.diag(e ** -0.5) @ Q.T
    M = invsqrt @ J14 @ invsqrt
    lam = np.linalg.eigvalsh(M)
    return float(lam[0]), float(lam[-1])


def optimized_rate(Js, ngrid=10001):
    """Two-campaign simplex regression optimizer."""
    assert len(Js) == 2
    best = -math.inf
    bestx = None
    for x in np.linspace(0.0, 1.0, ngrid):
        J = x * Js[0] + (1.0 - x) * Js[1]
        f = profiled(J)
        if f > best:
            best, bestx = f, float(x)
    return best, bestx


def arch_ratio(u, v, z, delta=1.0):
    """Iteration-105 Q14/Q09 final-significance rate ratio."""
    assert u > 0 and v > 0 and z > 0 and delta > 0
    return delta * ((1.0 + z ** -0.5) /
                    (u ** -0.5 + (v * z) ** -0.5)) ** 2


def required_u(v, z, delta=1.0):
    """Detector-side u threshold for Toy014 to beat Toy009.

    Returns infinity if even u -> infinity cannot rescue Toy014.
    """
    rhs = math.sqrt(delta) * (1.0 + z ** -0.5) - (v * z) ** -0.5
    return math.inf if rhs <= 0.0 else rhs ** -2


def box_ratio_bounds(ulo, uhi, vlo, vhi, zlo, zhi, dlo, dhi):
    """Exact extrema over an independent positive box.

    G is increasing in u,v,delta.  Its z monotonicity is set by sign(v-u).
    """
    assert 0 < ulo <= uhi and 0 < vlo <= vhi
    assert 0 < zlo <= zhi and 0 < dlo <= dhi
    z_for_lo = zhi if vlo > ulo else zlo if vlo < ulo else zlo
    z_for_hi = zlo if vhi > uhi else zhi if vhi < uhi else zlo
    lo = arch_ratio(ulo, vlo, z_for_lo, dlo)
    hi = arch_ratio(uhi, vhi, z_for_hi, dhi)
    return lo, hi, z_for_lo, z_for_hi


def make_relative(A, eigenvalues, R):
    e, Q = np.linalg.eigh(A)
    sqrtA = Q @ np.diag(np.sqrt(e)) @ Q.T
    M = R @ np.diag(eigenvalues) @ R.T
    return sqrtA @ M @ sqrtA


def main():
    # Synthetic common-coordinate campaign matrices.
    J9a = np.array([[3.0, .6, .2], [.6, 2.0, .1], [.2, .1, 1.5]])
    J9b = np.array([[1.7, .1, .3], [.1, 1.4, .2], [.3, .2, 2.2]])

    t = .42
    R1 = np.array([[math.cos(t), -math.sin(t), 0.0],
                   [math.sin(t),  math.cos(t), 0.0],
                   [0.0, 0.0, 1.0]])
    t = .31
    R2 = np.array([[1.0, 0.0, 0.0],
                   [0.0, math.cos(t), -math.sin(t)],
                   [0.0, math.sin(t),  math.cos(t)]])
    J14a = make_relative(J9a, [.55, .90, 1.25], R1)
    J14b = make_relative(J9b, [.62, 1.05, 1.40], R2)

    bounds = [relative_loewner_bounds(A, B)
              for A, B in ((J9a, J14a), (J9b, J14b))]
    alpha = min(x[0] for x in bounds)
    beta = max(x[1] for x in bounds)
    assert abs(alpha - .55) < 2e-13
    assert abs(beta - 1.40) < 2e-13

    R09, x09 = optimized_rate([J9a, J9b])
    R14, x14 = optimized_rate([J14a, J14b])
    u = R14 / R09
    assert alpha <= u <= beta
    assert abs(u - 0.6172845157964684) < 3e-7

    # Exact independent-box RESOURCE-063 regression.
    box = (.2, .5, 1.2, 1.7, .01, .2, .9, 1.0)
    lo, hi, zlo_active, zhi_active = box_ratio_bounds(*box)
    brute = []
    for uu, vv, zz, dd in itertools.product(
            box[:2], box[2:4], box[4:6], box[6:8]):
        brute.append(arch_ratio(uu, vv, zz, dd))
    assert abs(lo - min(brute)) < 1e-14
    assert abs(hi - max(brute)) < 1e-14

    # RESOURCE-062/NG-062 engineering-threshold regressions.
    v_rob = 1.39  # retained finite Ramsey design-box lower ratio; regression only
    vals = {z: required_u(v_rob, z, 1.0) for z in (.01, .03, .1, 1.0)}
    assert abs(vals[.01] - .157706779074743) < 2e-15
    assert abs(vals[.03] - .2839954412778913) < 2e-15
    assert abs(vals[.1] - .45649520299373264) < 2e-15
    assert abs(vals[1.0] - .7537676652498215) < 2e-15

    # Iteration-105 crossover recovered exactly with mature zero-reset v.
    v0 = 1.4913343179877905
    z0 = 0.042393961570158255
    u0 = required_u(v0, z0, 1.0)
    assert abs(u0 - 0.2830146574583767) < 2e-15

    # No-rescue condition: delta*v*(1+sqrt(z))^2 <= 1.
    vbad, zbad, dbad = .25, .01, .8
    assert dbad * vbad * (1.0 + math.sqrt(zbad)) ** 2 <= 1.0
    assert math.isinf(required_u(vbad, zbad, dbad))

    print("PASS Iteration 106 detector-side ratio certificate")
    print("campaign generalized bounds =", bounds)
    print("global Loewner alpha,beta =", alpha, beta)
    print("optimized R09,R14,u =", R09, R14, u, "fractions", x09, x14)
    print("box Q14/Q09 bounds =", lo, hi,
          "active z endpoints", zlo_active, zhi_active)
    print("u_req with robust Ramsey regression v=1.39 =", vals)
    print("Iteration-105 crossover recovery u =", u0)


if __name__ == "__main__":
    main()
