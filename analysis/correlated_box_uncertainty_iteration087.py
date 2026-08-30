import math
import numpy as np


def profiled_rate(r2, r4, rho):
    if r2 <= 0 or r4 <= 0:
        raise ValueError("band rates must be positive")
    if not (-1 < rho < 1):
        raise ValueError("rho must lie in (-1,1)")
    return 4.0 * r2 * r4 / (r2 + r4 + 2.0 * rho * math.sqrt(r2 * r4))


def robust_box_lower(r2_lo, r2_hi, r4_lo, r4_hi, rho_lo, rho_hi):
    if not (0 < r2_lo <= r2_hi and 0 < r4_lo <= r4_hi):
        raise ValueError("invalid positive rate intervals")
    if not (-1 < rho_lo <= rho_hi < 1):
        raise ValueError("invalid correlation interval")

    # R is strictly decreasing in rho, so the worst correlation is rho_hi.
    # At fixed rho, each one-dimensional coordinate slice has no interior minimum:
    # for rho>=0 it is monotone; for rho<0 any stationary point is a maximum.
    # Therefore the exact minimum over the rectangle is at one of four rate corners.
    vals = []
    for r2 in (r2_lo, r2_hi):
        for r4 in (r4_lo, r4_hi):
            vals.append((profiled_rate(r2, r4, rho_hi), r2, r4, rho_hi))
    return min(vals, key=lambda x: x[0])


def run_regressions():
    # Two transparent examples.
    lower = robust_box_lower(0.8, 1.2, 3.0, 5.0, -0.6, -0.4)
    assert abs(lower[0] - 3.7490549317691566) < 1e-13

    lower_cross_zero = robust_box_lower(0.8, 1.2, 3.0, 5.0, -0.6, 0.1)
    assert abs(lower_cross_zero[0] - 2.3358581142019457) < 1e-13
    assert lower_cross_zero[0] < lower[0]

    # Random boxes: all random interior samples must lie above the exact corner lower bound.
    rng = np.random.default_rng(20260830)
    min_margin = math.inf
    for _ in range(200):
        r2_lo = 10.0 ** rng.uniform(-3, 2)
        r2_hi = r2_lo * 10.0 ** rng.uniform(0, 1.2)
        r4_lo = 10.0 ** rng.uniform(-3, 2)
        r4_hi = r4_lo * 10.0 ** rng.uniform(0, 1.2)
        rho_lo = rng.uniform(-0.95, 0.8)
        rho_hi = rng.uniform(rho_lo, 0.95)

        exact = robust_box_lower(r2_lo, r2_hi, r4_lo, r4_hi, rho_lo, rho_hi)[0]

        for _ in range(2000):
            r2 = math.exp(rng.uniform(math.log(r2_lo), math.log(r2_hi)))
            r4 = math.exp(rng.uniform(math.log(r4_lo), math.log(r4_hi)))
            rho = rng.uniform(rho_lo, rho_hi)
            value = profiled_rate(r2, r4, rho)
            min_margin = min(min_margin, value - exact)
            assert value >= exact * (1.0 - 2e-12)

    # The four corners at rho_hi include the exact minimum by construction.
    # Correlation monotonicity regression.
    for r2, r4 in ((1.0, 4.0), (0.2, 5.0), (7.0, 0.9)):
        vals = [profiled_rate(r2, r4, rho) for rho in (-0.8, -0.3, 0.0, 0.4, 0.8)]
        assert all(vals[i+1] < vals[i] for i in range(len(vals)-1))

    print("PASS iteration 087")
    print("example robust lower (rho in [-0.6,-0.4])=", lower)
    print("example robust lower (rho in [-0.6,0.1])=", lower_cross_zero)
    print("minimum sampled margin above exact lower bound=", min_margin)


if __name__ == "__main__":
    run_regressions()
