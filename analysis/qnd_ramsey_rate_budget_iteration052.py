"""RQIR Iteration 052: physical Fisher/sec budget for QND Ramsey ancilla metrology.

Iteration 051 optimized Fisher per accepted ancilla shot over the controlled
source-energy phase phi.  For apparatus design the relevant quantity is Fisher
per wall time.  If the controlled phase accumulates at rate Omega_E,

    phi = Omega_E T,

and source reset/preparation is negligible, the accepted Fisher rate is

    R_E = p_E Omega_E F_alpha(phi)/phi.

This script shows that the rate-optimal phase differs substantially from the
per-copy optimum and converts the result into the current D2 Branch0/best4 and
best4/best5 rate thresholds.
"""
from __future__ import annotations

import math
import numpy as np

import qnd_energy_pointer_fisher_iteration049 as i49
import qnd_ramsey_ancilla_metrology_iteration051 as i51

R04 = 2.13404e-4
R45 = 2.93122e-6


def rate_optimum(alpha: float = 1.0, visibility: float = 1.0):
    d = i49.hidden_diagonal()
    grid = np.linspace(1e-6, 2.0 * math.pi - 1e-6, 16001)
    vals = np.array([i51.ramsey_fisher(x, alpha, d, visibility) / x for x in grid])
    j = int(np.argmax(vals))
    step = grid[1] - grid[0]
    lo = max(1e-8, grid[j] - 4 * step)
    hi = min(2.0 * math.pi - 1e-8, grid[j] + 4 * step)
    phi, coeff = i49.golden_max(
        lambda x: i51.ramsey_fisher(x, alpha, d, visibility) / x, lo, hi
    )
    f = i51.ramsey_fisher(phi, alpha, d, visibility)
    return phi, f, coeff


def main():
    d = i49.hidden_diagonal()
    fproj = i49.projective_energy_fisher(+1.0, d)
    phi, f, c = rate_optimum(+1.0, 1.0)
    print("rate-optimal phi", phi)
    print("F_alpha", f, "fraction projective", f / fproj)
    print("rate coefficient R/(p_E Omega_E)", c)

    assert abs(phi - 1.092306912) < 3e-7
    assert abs(f - 0.002756370099) < 5e-12
    assert abs(c - 0.002523439217) < 5e-12
    assert abs(f / fproj - 0.293482112) < 3e-7

    # Current transparent D2 rate thresholds from Iteration 050.
    for p in (1.0, 0.5):
        om04 = R04 / (p * c)
        om45 = R45 / (p * c)
        print("p", p, "Omega Branch0/best4", om04,
              "Omega best4/best5", om45,
              "Tinteraction at 04", phi / om04)

    om04_p05 = R04 / (0.5 * c)
    om45_p05 = R45 / (0.5 * c)
    assert abs(om04_p05 - 0.16914) < 2e-5
    assert abs(om45_p05 - 0.002323) < 2e-6
    assert abs(phi / om04_p05 - 6.457) < 0.01

    # Visibility penalty after re-optimizing rate phase.
    for vis in (0.9, 0.8, 0.5):
        ph, fv, cv = rate_optimum(+1.0, vis)
        print("V", vis, "phi", ph, "F", fv,
              "rate coeff", cv,
              "Omega04 p=.5", R04 / (0.5 * cv))


if __name__ == "__main__":
    main()
