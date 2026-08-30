#!/usr/bin/env python3
"""RQIR Iteration 115 — full-complex common-gain Fisher-rate certificate.

This deterministic regression verifies:
1. direct 4D Schur profiling equals nested phase-then-differential profiling;
2. the 2x2 common/differential closed form;
3. source-independent identical reference likelihood gives c=1 exactly;
4. Loewner relative bounds propagate to the scalar common-gain rate;
5. the Toy014/Toy009 R_DT box is attained on corners for interval inputs.

No apparatus-specific Fisher rates are asserted.
"""
from __future__ import annotations

import itertools
import numpy as np

SEED = 20260831115


def _sym(a):
    return 0.5 * (a + a.T)


def _spd(rng, n):
    a = rng.normal(size=(n, n))
    return a.T @ a + 0.5 * np.eye(n)


def schur_scalar(k, index=0):
    """Scalar Schur complement after profiling every coordinate except index."""
    k = _sym(np.asarray(k, dtype=float))
    keep = [i for i in range(k.shape[0]) if i != index]
    v = k[index, keep]
    n = k[np.ix_(keep, keep)]
    return float(k[index, index] - v @ np.linalg.solve(n, v))


def to_common_differential(k_band_complex):
    """Map (g2,g4,phi2,phi4) -> (c,d,phi2,phi4), g2=c-d, g4=c+d."""
    t = np.array(
        [[1.0, -1.0, 0.0, 0.0],
         [1.0,  1.0, 0.0, 0.0],
         [0.0,  0.0, 1.0, 0.0],
         [0.0,  0.0, 0.0, 1.0]]
    )
    return _sym(t.T @ k_band_complex @ t)


def gain_rate_after_phase(k_cd):
    """Profile phases first, returning the 2x2 (common,differential) gain rate."""
    g = [0, 1]
    p = [2, 3]
    gg = k_cd[np.ix_(g, g)]
    gp = k_cd[np.ix_(g, p)]
    pp = k_cd[np.ix_(p, p)]
    return _sym(gg - gp @ np.linalg.solve(pp, gp.T))


def common_rate_2x2(c_gain):
    return float(c_gain[0, 0] - c_gain[0, 1] ** 2 / c_gain[1, 1])


def common_rate_closed_band(k_gain_band):
    """Iteration-114 formula for a 2x2 Fisher matrix in (g2,g4)."""
    k = _sym(np.asarray(k_gain_band, dtype=float))
    return float(4.0 * np.linalg.det(k) / (k[0, 0] + k[1, 1] - 2.0 * k[0, 1]))


def u_dt(s, c, z):
    return ((1.0 + z ** -0.5) /
            (s ** -0.5 + (c * z) ** -0.5)) ** 2


def main():
    rng = np.random.default_rng(SEED)

    # 1) Associativity / quotient-order regression for the full complex 4D block.
    max_rel = 0.0
    for _ in range(1000):
        k_band = _spd(rng, 4)
        k_cd = to_common_differential(k_band)
        direct = schur_scalar(k_cd, 0)
        nested = common_rate_2x2(gain_rate_after_phase(k_cd))
        rel = abs(direct - nested) / max(1.0, abs(direct))
        max_rel = max(max_rel, rel)
    assert max_rel < 3e-14

    # 2) Exact recovery of the Iteration-114 2x2 formula when phases are absent.
    for _ in range(1000):
        k = _spd(rng, 2)
        # transform band gains into common/differential coordinates
        m = np.array([[1.0, -1.0], [1.0, 1.0]])
        c = _sym(m.T @ k @ m)
        a = common_rate_2x2(c)
        b = common_rate_closed_band(k)
        assert abs(a - b) / max(1.0, abs(a)) < 3e-14

    # 3) Identical same-state reference likelihood -> exact c=1.
    k0 = _spd(rng, 4)
    r0 = schur_scalar(to_common_differential(k0), 0)
    r09 = schur_scalar(to_common_differential(k0.copy()), 0)
    r14 = schur_scalar(to_common_differential(k0.copy()), 0)
    assert abs(r14 / r09 - 1.0) < 1e-15

    # 4) Relative Loewner bounds propagate to the common-gain shorted rate.
    # Construct Ki=K0^(1/2) A K0^(1/2), eig(A) in [m,M].
    w, v = np.linalg.eigh(k0)
    khalf = v @ np.diag(np.sqrt(w)) @ v.T
    mlo, mhi = 0.72, 1.31
    q, _ = np.linalg.qr(rng.normal(size=(4, 4)))
    lam = np.array([mlo, 0.86, 1.07, mhi])
    a = q @ np.diag(lam) @ q.T
    ki = _sym(khalf @ a @ khalf)
    ri = schur_scalar(to_common_differential(ki), 0)
    assert mlo * r0 - 1e-12 <= ri <= mhi * r0 + 1e-12

    # 5) Robust architecture box: exact corner enclosure.
    s_bounds = (0.25, 0.35)
    c_bounds = (0.80, 1.25)
    z_bounds = (0.05, 20.0)
    corners = []
    for s, c, z in itertools.product(s_bounds, c_bounds, z_bounds):
        corners.append((u_dt(s, c, z), s, c, z))
    corners.sort()
    lo, hi = corners[0], corners[-1]

    # Dense deterministic interior check: no interior point escapes corner envelope.
    for s in np.linspace(*s_bounds, 81):
        for c in np.linspace(*c_bounds, 81):
            for z in np.geomspace(*z_bounds, 101):
                u = u_dt(float(s), float(c), float(z))
                assert lo[0] - 2e-12 <= u <= hi[0] + 2e-12

    print("RQIR Iteration 115 regression: PASS")
    print(f"max nested/direct Schur relative error = {max_rel:.3e}")
    print(f"identical-reference c = {r14/r09:.16f}")
    print(f"Loewner test R_c/R_c0 = {ri/r0:.12g} in [{mlo}, {mhi}]")
    print("u_DT test box lower corner =", lo)
    print("u_DT test box upper corner =", hi)


if __name__ == "__main__":
    main()
