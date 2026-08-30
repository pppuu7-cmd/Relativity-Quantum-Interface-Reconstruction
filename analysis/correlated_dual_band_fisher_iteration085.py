import math
import numpy as np


def profiled_rate(g2, g4, s2, s4, rho):
    """Profile common amplitude beta against antisymmetric spectral tilt.

    Covariance per unit live time is
        Sigma = [[s2, rho*sqrt(s2*s4)], [rho*sqrt(s2*s4), s4]]
    with |rho|<1. Signal derivative is (g2,g4); tilt derivative is (-g2,g4).
    """
    c = rho * math.sqrt(s2 * s4)
    Sigma = np.array([[s2, c], [c, s4]], dtype=float)
    W = np.linalg.inv(Sigma)
    g = np.array([g2, g4], dtype=float)
    h = np.array([-g2, g4], dtype=float)
    Fbb = g @ W @ g
    Fbq = g @ W @ h
    Fqq = h @ W @ h
    return Fbb - Fbq * Fbq / Fqq


def closed_rate(g2, g4, s2, s4, rho):
    c = rho * math.sqrt(s2 * s4)
    den = s4 * g2 * g2 + 2.0 * c * g2 * g4 + s2 * g4 * g4
    return 4.0 * g2 * g2 * g4 * g4 / den


def rate_from_single_band_rates(r2, r4, rho_eff):
    """Equivalent form after channel signs/phases are absorbed into rho_eff."""
    return 4.0 * r2 * r4 / (
        r2 + r4 + 2.0 * rho_eff * math.sqrt(r2 * r4)
    )


def main():
    rng = np.random.default_rng(20260830085)
    max_abs_err = 0.0
    for _ in range(1000):
        g2, g4 = np.exp(rng.normal(size=2))
        s2, s4 = np.exp(rng.normal(size=2))
        rho = rng.uniform(-0.95, 0.95)
        f1 = profiled_rate(g2, g4, s2, s4, rho)
        f2 = closed_rate(g2, g4, s2, s4, rho)
        max_abs_err = max(max_abs_err, abs(f1 - f2))
    assert max_abs_err < 2e-11

    # Independent-band regression: rho=0 reproduces Iteration 084.
    for r2, r4 in [(0.3, 0.7), (1.0, 1.0), (2.0, 5.0)]:
        f = rate_from_single_band_rates(r2, r4, 0.0)
        old = 4.0 * r2 * r4 / (r2 + r4)
        assert abs(f - old) < 1e-14

    # Balanced-band law R=2r/(1+rho).
    for rho in (-0.8, -0.2, 0.0, 0.5, 0.9):
        r = 0.73
        f = rate_from_single_band_rates(r, r, rho)
        target = 2.0 * r / (1.0 + rho)
        assert abs(f - target) < 1e-13

    # Weak-band ceiling survives finite correlation: r4 -> infinity => 4 r2.
    r2 = 0.17
    for rho in (-0.8, 0.0, 0.8):
        f = rate_from_single_band_rates(r2, 1e12, rho)
        assert abs(f / (4.0 * r2) - 1.0) < 2e-6

    # Positive-definiteness guard.
    for bad in (-1.0, 1.0):
        try:
            _ = profiled_rate(1.0, 1.0, 1.0, 1.0, bad)
        except np.linalg.LinAlgError:
            pass
        else:
            raise AssertionError("|rho|=1 must be treated as singular-limit, not ordinary inversion")

    print("PASS")
    print(f"max Schur-vs-closed abs error = {max_abs_err:.3e}")
    print("correlated two-band rate law verified")


if __name__ == "__main__":
    main()
