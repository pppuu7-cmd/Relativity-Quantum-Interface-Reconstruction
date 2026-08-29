"""RQIR Iteration 049: finite-strength QND energy-pointer metrology.

Replace the ideal projective energy measurement of Iteration 047 by a finite-
resolution Gaussian pointer.  Conditional on energy level E_i, one accepted
readout is

    y | i ~ N(r E_i, 1),

while the hidden family has populations

    p_i(alpha) = 1/5 + EPS * alpha * d_i,

where d_i are the diagonal entries of the Toy009 hidden operator Delta0.
The dimensionless separation r is the adjacent-level pointer separation in
units of output standard deviation.

For a standard QND diffusive energy monitor one may write

    r = 2 sqrt(eta * kappa_E * T),

so the Fisher throughput at zero reset overhead is

    R_E = 4 p_E eta kappa_E * F_alpha(r)/r^2.

The script uses Gauss-Hermite quadrature only (NumPy dependency) and verifies
the weak-readout quartic suppression, finite-strength Fisher fractions and the
throughput-optimal pointer strength.
"""
from __future__ import annotations

import math
import numpy as np
from numpy.polynomial.hermite import hermgauss

import d2_information_backaction_proxy_iteration043 as i43

EPS = 0.08
E = np.array([1., 2., 3., 4., 6.])
N_GH = 120
XGH, WGH = hermgauss(N_GH)


def hidden_diagonal() -> np.ndarray:
    return np.real(np.diag(i43.hidden_operator()))


def populations(alpha: float, d: np.ndarray) -> np.ndarray:
    p = np.ones(len(d)) / len(d) + EPS * alpha * d
    if np.min(p) <= 0:
        raise ValueError("state not positive")
    return p


def projective_energy_fisher(alpha: float, d: np.ndarray) -> float:
    p = populations(alpha, d)
    dp = EPS * d
    return float(np.sum(dp * dp / p))


def pointer_fisher(r: float, alpha: float, d: np.ndarray) -> float:
    """Classical Fisher about alpha for y|i~N(r E_i,1)."""
    p = populations(alpha, d)
    dp = EPS * d
    mu = r * E
    total = 0.0
    # Evaluate E_{y|i}[score(y)^2] by Gauss-Hermite quadrature.
    for i in range(len(E)):
        y = mu[i] + math.sqrt(2.0) * XGH
        g = np.exp(-0.5 * (y[:, None] - mu[None, :])**2) / math.sqrt(2.0 * math.pi)
        py = g @ p
        dpy = g @ dp
        score2 = (dpy / py)**2
        total += p[i] * float(np.sum(WGH * score2) / math.sqrt(math.pi))
    return total


def golden_max(fun, lo: float, hi: float, tol: float = 1e-10) -> tuple[float, float]:
    q = (math.sqrt(5.0) - 1.0) / 2.0
    c = hi - q * (hi - lo)
    d = lo + q * (hi - lo)
    fc, fd = fun(c), fun(d)
    for _ in range(160):
        if hi - lo < tol:
            break
        if fc > fd:
            hi, d, fd = d, c, fc
            c = hi - q * (hi - lo)
            fc = fun(c)
        else:
            lo, c, fc = c, d, fd
            d = lo + q * (hi - lo)
            fd = fun(d)
    x = 0.5 * (lo + hi)
    return x, fun(x)


def main() -> None:
    d = hidden_diagonal()
    print("hidden diagonal", d)
    print("trace moment", np.sum(d), "energy moment", d @ E)
    assert abs(np.sum(d)) < 1e-12
    assert abs(d @ E) < 1e-12

    fproj = projective_energy_fisher(+1.0, d)
    print("projective F_alpha plus", fproj)
    assert abs(fproj - 0.00939188436411534) < 3e-14

    # Because both trace and mean energy are exactly matched, the weak pointer
    # cannot see alpha at O(r^0) or O(r^1).  The leading score is the variance
    # channel and Fisher starts at O(r^4):
    # F ~= 1/2 [EPS sum_i d_i E_i^2]^2 r^4.
    coeff = 0.5 * (EPS * float(d @ (E**2)))**2
    print("weak-r quartic coefficient", coeff)
    assert abs(coeff - 0.015860361623731754) < 2e-15

    for r, expected_frac in [
        (0.5, 0.04358749111074538),
        (1.0, 0.21688959233407368),
        (2.0, 0.5761366395735013),
        (3.0, 0.8138512082253507),
        (4.0, 0.9352150673205186),
        (6.0, 0.9960773383643636),
    ]:
        f = pointer_fisher(r, +1.0, d)
        frac = f / fproj
        print("r", r, "F", f, "projective fraction", frac)
        assert abs(frac - expected_frac) < 3e-8

    # At zero source-reset overhead, maximize Fisher per measurement action
    # r^2, since T=r^2/(4 eta kappa_E).
    rstar, metric = golden_max(lambda r: pointer_fisher(r, +1.0, d) / r**2,
                               0.02, 8.0)
    fstar = pointer_fisher(rstar, +1.0, d)
    fracstar = fstar / fproj
    rate_coeff = 4.0 * metric  # R_E = p_E eta kappa_E * rate_coeff
    print("throughput optimum r", rstar)
    print("Fstar", fstar, "fraction", fracstar)
    print("max rate coefficient R/(p eta kappa)", rate_coeff)

    assert abs(rstar - 0.8677465252) < 2e-7
    assert abs(fstar - 0.0015568124985) < 3e-12
    assert abs(fracstar - 0.1657614636) < 3e-9
    assert abs(rate_coeff - 0.0082700956855) < 3e-12

    # Weak-readout regression: F/r^4 approaches the analytic coefficient.
    rweak = 1e-2
    fweak = pointer_fisher(rweak, +1.0, d)
    print("weak regression F/r^4", fweak / rweak**4)
    assert abs(fweak / rweak**4 - coeff) / coeff < 5e-3


if __name__ == "__main__":
    main()
