"""RQIR Iteration 051: QND Ramsey-ancilla source metrology.

A more physical alternative to resolving five energy peaks is a two-level
ancilla coupled QND to the source energy.  With source populations p_i(alpha)
and controlled phase phi E_i, the ancilla coherence is

    c(phi,alpha) = sum_i p_i(alpha) exp(-i phi E_i).

An equatorial binary ancilla measurement with optimized quadrature extracts
Fisher about alpha.  The optimum over the quadrature has the closed form

    F = d^T [I - c c^T]^{-1} d,

where c=(Re c, Im c), d=(Re dc/dalpha, Im dc/dalpha), including an optional
visibility factor V multiplying both vectors.

The script optimizes phi, compares with projective energy Fisher and converts
the result to the current D2 Branch0/best4/best5 cycle-time boundaries.
"""
from __future__ import annotations

import math
import numpy as np

import qnd_energy_pointer_fisher_iteration049 as i49

EPS = 0.08
E = np.array([1., 2., 3., 4., 6.])
C0 = 4.55511
C4 = 0.05006143859980483
T4 = 5.8640185211734766 * 3600.0
T5 = 10.608109160132264 * 3600.0


def ramsey_fisher(phi: float, alpha: float, dpop: np.ndarray,
                  visibility: float = 1.0) -> float:
    if not (0.0 < visibility <= 1.0):
        raise ValueError("visibility must be in (0,1]")
    p = i49.populations(alpha, dpop)
    z = np.exp(-1j * phi * E)
    c = np.sum(p * z)
    dc = EPS * np.sum(dpop * z)
    cv = visibility * np.array([c.real, c.imag])
    dv = visibility * np.array([dc.real, dc.imag])
    metric = np.eye(2) - np.outer(cv, cv)
    return float(dv @ np.linalg.pinv(metric, rcond=1e-14) @ dv)


def optimize_phi(alpha: float, dpop: np.ndarray, visibility: float = 1.0) -> tuple[float, float]:
    # Integer energy spectrum -> 2pi periodic.  Coarse deterministic search,
    # then golden refinement around the best bin.
    grid = np.linspace(1e-6, 2.0 * math.pi - 1e-6, 12001)
    vals = np.array([ramsey_fisher(x, alpha, dpop, visibility) for x in grid])
    j = int(np.argmax(vals))
    step = grid[1] - grid[0]
    lo = max(1e-8, grid[j] - 3.0 * step)
    hi = min(2.0 * math.pi - 1e-8, grid[j] + 3.0 * step)
    phi, neg = i49.golden_max(lambda x: ramsey_fisher(x, alpha, dpop, visibility), lo, hi)
    return phi, neg


def cycle_boundaries(f_per_copy: float) -> tuple[float, float, float, float]:
    n0 = C0 / f_per_copy
    n4 = C4 / f_per_copy
    # Equal acceptance convention: tcycle below these makes the lower-Fisher
    # branch cheaper in the transparent 100-Hz covariance benchmark.
    t04 = T4 / (n0 - n4)
    t45 = (T5 - T4) / n4
    return n0, n4, t04, t45


def main() -> None:
    d = i49.hidden_diagonal()
    fproj = i49.projective_energy_fisher(+1.0, d)

    phi, f = optimize_phi(+1.0, d, 1.0)
    phim, fm = optimize_phi(-1.0, d, 1.0)
    print("plus optimum phi/F", phi, f, "fraction projective", f/fproj)
    print("minus optimum phi/F", phim, fm)

    assert abs(phi - 2.41866767) < 3e-6
    assert abs(f - 0.00389040938079) < 4e-13
    assert abs(f / fproj - 0.41423097112) < 3e-10
    assert abs(phim - 2.41023349) < 4e-6
    assert abs(fm - 0.00353595967205) < 4e-13

    n0, n4, t04, t45 = cycle_boundaries(f)
    print("plus-copy counts Branch0/best4 residual", n0, n4)
    print("cycle-time boundaries seconds", t04, t45)
    assert abs(n0 - 1170.85621439) < 2e-8
    assert abs(n4 - 12.8679102120) < 2e-9
    assert abs(t04 - 18.230293519) < 2e-8
    assert abs(t45 - 1327.23387239) < 2e-8

    # Visibility robustness: re-optimize phase for each contrast.
    expected = {
        0.9: (0.00302711843190, 14.18494871, 17.21195949),
        0.8: (0.00231097475584, 10.82912979, 13.14002236),
        0.5: (0.000838616234002, 3.92972014, 4.76830655),
    }
    for vis, exp in expected.items():
        ph, fv = optimize_phi(+1.0, d, vis)
        _n0, _n4, b04, b45 = cycle_boundaries(fv)
        print("V", vis, "phi", ph, "F", fv,
              "t04 s", b04, "t45 min", b45/60.0)
        assert abs(fv - exp[0]) < 5e-13
        assert abs(b04 - exp[1]) < 3e-7
        assert abs(b45/60.0 - exp[2]) < 3e-7

    # Weak-phase check: trace and mean-energy matching again force the first
    # derivative signal to start at O(phi^2), hence Fisher O(phi^4).
    for ph in (1e-3, 2e-3):
        val = ramsey_fisher(ph, +1.0, d, 1.0)
        print("weak phi", ph, "F/phi^4", val / ph**4)


if __name__ == "__main__":
    main()
