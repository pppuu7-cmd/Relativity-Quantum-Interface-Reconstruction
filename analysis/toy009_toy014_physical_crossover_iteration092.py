"""RQIR Iteration 092 — physical Toy009/Toy014 rate-space crossover.

Purpose
-------
Translate the historical abstract (x,y) crossover into physical rate space
without assuming that source metrology is zero-reset or that detector and
calibration kernels are identical between sources.

The script reconstructs the Toy009 and Toy014 hidden directions using mature
repository machinery, evaluates reset/visibility-aware Ramsey Fisher rates,
and verifies the exact wall-clock crossover law.
"""
from __future__ import annotations

import math
import numpy as np

import toy011_local_nearest_neighbor_source as t11
import toy011_centered_profiled_resource_audit_iteration054 as i54
import toy014_multiresource_local_codesign_iteration074 as i74

Z = 5.0
C_SRC = 225.0


def golden_max(f, a, b, tol=1e-12):
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    c = b - gr * (b - a)
    d = a + gr * (b - a)
    fc, fd = f(c), f(d)
    for _ in range(220):
        if b - a < tol:
            break
        if fc > fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a)
            fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a)
            fd = f(d)
    x = 0.5 * (a + b)
    return x, f(x)


def ramsey_rate_coeff(d0, visibility=1.0, tau_reset=0.0):
    """Return max_phi F_alpha(phi,V)/(tau_reset+phi).

    tau_reset = Omega_E * t_reset is dimensionless.  Hence physical
    R_src = p_E * Omega_E * coeff.
    """
    dpop = np.real(np.diag(d0))
    grid = np.linspace(1e-6, 2.0 * math.pi - 1e-6, 12001)
    vals = np.array([
        i54.ramsey_fisher(phi, 1.0, dpop, visibility) / (tau_reset + phi)
        for phi in grid
    ])
    j = int(np.argmax(vals))
    step = grid[1] - grid[0]
    lo = max(1e-8, grid[j] - 4.0 * step)
    hi = min(2.0 * math.pi - 1e-8, grid[j] + 4.0 * step)
    return golden_max(
        lambda phi: i54.ramsey_fisher(phi, 1.0, dpop, visibility)
        / (tau_reset + phi), lo, hi
    )


def reconstruct_d0s():
    p009 = i54.make_pack(t11.V009_SORTED, t11.Y1_BASE, t11.TIMES_BASE)
    q014 = t11.lanczos_q(i74.Q0)
    assert q014 is not None
    p014 = i54.make_pack(q014, i74.Y1, i74.TIMES)
    return p009['d0'], p014['d0']


def wall_time(A, R0, Rsrc, duty, Csrc=C_SRC):
    return (A / R0 + Csrc / Rsrc) / (1.0 - duty)


def crossover_R0(A009, A014, Rsrc009, Rsrc014, d009=0.0, d014=0.0,
                 Csrc=C_SRC):
    """Exact positive-R0 crossover, or None if no finite crossing.

    Let D = m14*A14 - m09*A09 and S = C*(m14/R14-m09/R09).
    T14-T09 = D/R0 + S.
    """
    m9 = 1.0 / (1.0 - d009)
    m14 = 1.0 / (1.0 - d014)
    D = m14 * A014 - m9 * A009
    S = Csrc * (m14 / Rsrc014 - m9 / Rsrc009)
    if abs(S) < 1e-18:
        return None, D, S
    r = -D / S
    return (r if r > 0 else None), D, S


def main():
    d009, d014 = reconstruct_d0s()

    # Zero-reset regression to Iteration 074.
    phi9, c9 = ramsey_rate_coeff(d009, 1.0, 0.0)
    phi14, c14 = ramsey_rate_coeff(d014, 1.0, 0.0)
    ratio = c14 / c9
    print('zero reset:', phi9, c9, phi14, c14, ratio)
    assert abs(c9 - 0.0025234392) < 3e-10
    assert abs(c14 - 0.00376329150) < 3e-10
    assert abs(ratio - 1.49133432) < 3e-6

    # Declared reset/visibility audit.  This is a deterministic design-box
    # scan, not a theorem outside the box.
    audit = []
    min_ratio = (float('inf'), None)
    for V in np.linspace(0.5, 1.0, 11):
        for tau in np.r_[np.linspace(0.0, 2.0, 9), np.logspace(0.5, 3.0, 13)]:
            _, a9 = ramsey_rate_coeff(d009, float(V), float(tau))
            _, a14 = ramsey_rate_coeff(d014, float(V), float(tau))
            kappa = a14 / a9
            audit.append((V, tau, kappa))
            if kappa < min_ratio[0]:
                min_ratio = (kappa, (V, tau))
    print('declared box min Rsrc014/Rsrc009 =', min_ratio)
    assert min_ratio[0] > 1.39

    # Exact physical crossover regression with arbitrary source-specific A.
    A9, A14 = 2.0, 6.0
    R9, R14 = 1.0, 1.5
    R0c, D, S = crossover_R0(A9, A14, R9, R14)
    assert R0c is not None
    t9 = wall_time(A9, R0c, R9, 0.0)
    t14 = wall_time(A14, R0c, R14, 0.0)
    print('synthetic crossover', R0c, D, S, t9, t14)
    assert abs(t9 - t14) < 1e-11

    # NG-042 guard: if Toy014 is worse in detector/calibration AND has no
    # duty-adjusted source-rate advantage, it can never win for positive R0.
    R0c2, D2, S2 = crossover_R0(2.0, 6.0, 1.0, 0.9)
    assert D2 > 0 and S2 > 0 and R0c2 is None

    # If D>0 and S<0, Toy014 wins only above the physical throughput crossing.
    eps = 1e-6
    assert wall_time(A14, R0c*(1+eps), R14, 0.0) < wall_time(A9, R0c*(1+eps), R9, 0.0)
    assert wall_time(A14, R0c*(1-eps), R14, 0.0) > wall_time(A9, R0c*(1-eps), R9, 0.0)

    print('PASS Iteration 092')


if __name__ == '__main__':
    main()
