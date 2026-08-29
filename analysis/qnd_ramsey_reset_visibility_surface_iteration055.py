"""RQIR Iteration 055: QND Ramsey source-metrology reset/visibility surface.

Extends Iteration 051 from Fisher per accepted copy to physical Fisher rate
including source acceptance p_E, Ramsey visibility V, interaction rate Omega_E,
and fresh-source/reset overhead t_reset.

For phase phi = Omega_E T,
    R_alpha(phi)=p_E F_alpha(phi,V)/(t_reset + phi/Omega_E).

The code optimizes phi and maps the result to the centered D2 Branch0/best4/
best5 source-amplitude closure thresholds. This is an independent/sacrificial
source-metrology budget; it does not waive NG-023 (QND w.r.t. H is not ordered-
response nondemolition).
"""
from __future__ import annotations
import math
import numpy as np
import qnd_ramsey_ancilla_metrology_iteration051 as i51

C0 = 4.55511
C4 = 0.05006143859980483
T4 = 5.8640185211734766 * 3600.0
T5 = 10.608109160132264 * 3600.0


def fisher_rate(phi, omega, t_reset, p_accept, visibility, dpop):
    if omega <= 0 or t_reset < 0 or not (0 < p_accept <= 1):
        raise ValueError('invalid physical resource parameter')
    f = i51.ramsey_fisher(phi, +1.0, dpop, visibility)
    return p_accept * f / (t_reset + phi / omega)


def optimize_rate(omega, t_reset, p_accept, visibility, dpop):
    # Deterministic logarithmic+linear grid followed by golden refinement.
    grid = np.unique(np.r_[np.geomspace(1e-5, 0.2, 2500),
                           np.linspace(0.2, 2*math.pi-1e-5, 10000)])
    vals = np.array([fisher_rate(x, omega, t_reset, p_accept, visibility, dpop)
                     for x in grid])
    j = int(np.argmax(vals))
    lo = grid[max(0, j-2)]; hi = grid[min(len(grid)-1, j+2)]
    phi, rate = i51.i49.golden_max(
        lambda x: fisher_rate(x, omega, t_reset, p_accept, visibility, dpop), lo, hi)
    return phi, rate


def branch_times(rate):
    """Source-metrology time added to branch0/best4; best5 needs no C_alpha."""
    return C0/rate, T4 + C4/rate, T5


def classify(rate):
    t0, t4, t5 = branch_times(rate)
    vals = {'branch0+Ramsey': t0, 'best4+Ramsey': t4, 'best5': t5}
    return min(vals, key=vals.get), vals


def main():
    d = i51.i49.hidden_diagonal()
    # Representative physical surface. Omega is dimensionless phase rate in s^-1.
    for V in (1.0, 0.9, 0.8, 0.5):
        for treset in (0.0, 0.1, 1.0, 10.0, 100.0):
            for omega in (1e-3, 1e-2, 1e-1, 1.0, 10.0):
                phi, rate = optimize_rate(omega, treset, 0.5, V, d)
                winner, times = classify(rate)
                print('V',V,'reset',treset,'Omega',omega,'phi*',phi,
                      'R',rate,'winner',winner,'times_s',times)

    # Structural regression guards.
    # Reset overhead can only reduce the optimum achievable rate at fixed Omega,V,p.
    for V in (1.0, 0.8):
        _, r0 = optimize_rate(0.1, 0.0, 0.5, V, d)
        _, r1 = optimize_rate(0.1, 1.0, 0.5, V, d)
        _, r10 = optimize_rate(0.1, 10.0, 0.5, V, d)
        assert r0 >= r1 >= r10 > 0
    # Lower visibility cannot improve the optimized Fisher rate.
    _, rv1 = optimize_rate(0.1, 1.0, 0.5, 1.0, d)
    _, rv8 = optimize_rate(0.1, 1.0, 0.5, 0.8, d)
    assert rv1 >= rv8 > 0
    # Branch boundaries in rate form are exact consequences of previous budgets.
    r04 = (C0-C4)/T4
    r45 = C4/(T5-T4)
    print('exact rate boundaries branch0/best4, best4/best5', r04, r45)
    assert r04 > r45 > 0

if __name__ == '__main__':
    main()
