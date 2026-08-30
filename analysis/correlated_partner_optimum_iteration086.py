import math
import numpy as np


def profiled_rate(r2, r4, rho):
    if r2 <= 0 or r4 <= 0:
        raise ValueError("band rates must be positive")
    if not (-1 < rho < 1):
        raise ValueError("rho must lie in (-1,1) for the ordinary positive-definite covariance likelihood")
    return 4.0 * r2 * r4 / (r2 + r4 + 2.0 * rho * math.sqrt(r2 * r4))


def fixed_weak_optimum(r_weak, rho):
    """Return (partner_rate, maximum_profiled_rate).

    For rho>=0 the supremum occurs only as partner_rate -> infinity.
    For rho<0 the maximum is finite at partner/weak = 1/rho^2.
    """
    if not (-1 < rho < 1):
        raise ValueError("rho must lie in (-1,1)")
    if rho < 0:
        r_partner = r_weak / (rho * rho)
        r_max = 4.0 * r_weak / (1.0 - rho * rho)
        return r_partner, r_max
    return math.inf, 4.0 * r_weak


def minimum_weak_rate_for_target(R_target, rho):
    """Necessary weak-band rate after optimizing the partner band."""
    if rho < 0:
        return 0.25 * (1.0 - rho * rho) * R_target
    return 0.25 * R_target


def run_regressions():
    # Explicit counterexample to the over-strong global reading of the old weak-band ceiling.
    # r_weak=1, rho=-1/2, partner=4 gives R=16/3 > 4*r_weak.
    got = profiled_rate(1.0, 4.0, -0.5)
    expected = 16.0 / 3.0
    assert abs(got - expected) < 1e-14
    assert got > 4.0

    # Exact finite optimum for negative correlation.
    for rho in (-0.9, -0.5, -0.2):
        r_w = 1.7
        r_p, r_max = fixed_weak_optimum(r_w, rho)
        assert abs(profiled_rate(r_w, r_p, rho) - r_max) < 1e-13

        # Check both sides of the optimum are lower.
        assert profiled_rate(r_w, 0.9 * r_p, rho) < r_max
        assert profiled_rate(r_w, 1.1 * r_p, rho) < r_max

    # For rho>=0 the rate is monotone upward in partner strength and tends to 4*r_weak.
    for rho in (0.0, 0.2, 0.7):
        r_w = 2.3
        vals = [profiled_rate(r_w, r_w * x, rho) for x in (1, 10, 100, 1000, 1e6)]
        assert all(vals[i + 1] > vals[i] for i in range(len(vals) - 1))
        assert abs(vals[-1] / (4.0 * r_w) - 1.0) < 2e-3

    # Random numerical scan of the analytic finite optimum for rho<0.
    rng = np.random.default_rng(20260830)
    max_rel = 0.0
    for _ in range(1000):
        rho = rng.uniform(-0.95, -0.01)
        r_w = 10.0 ** rng.uniform(-4, 3)
        r_p, exact = fixed_weak_optimum(r_w, rho)
        factors = np.logspace(-2, 2, 2001)
        numeric = max(profiled_rate(r_w, r_p * f, rho) for f in factors)
        max_rel = max(max_rel, abs(numeric - exact) / exact)
    assert max_rel < 1e-11

    # At fixed total raw rate, balance r2=r4 remains optimal for every |rho|<1.
    S = 10.0
    for rho in (-0.9, -0.5, 0.0, 0.5, 0.9):
        balanced = profiled_rate(S / 2, S / 2, rho)
        xs = np.linspace(0.001, S - 0.001, 20001)
        numeric = max(profiled_rate(x, S - x, rho) for x in xs)
        assert abs(numeric - balanced) / balanced < 1e-7

    print("PASS iteration 086")
    print("rho=-0.5 counterexample R=", expected)
    print("1000-case finite-optimum max relative discrepancy=", max_rel)


if __name__ == "__main__":
    run_regressions()
