"""RQIR Iteration 120: strong-vs-shared calibration-cover bracket.

Dimensionless accepted-cycle regression using the stored Toy009/Toy014 gamma
normalizations.  This is not an apparatus wall-clock forecast.
"""
from __future__ import annotations

import math

GM09 = 1.830264703e6
GC09 = 5.901272925e5
GM14 = 5.6776851e6
GC14 = 2.7186736e6


def burdens(gm: float, gc: float, xi_mean: float):
    if xi_mean <= 0:
        raise ValueError("xi_mean must be positive")
    mean = 7.0 * gm / (xi_mean * xi_mean)
    cov_matching = 4.0 * gc   # Iteration 119 optimistic detector-output optimum
    cov_separate = 8.0 * gc   # no covariance-row sharing
    lower_shared = max(mean, cov_matching)
    matching_separate_from_mean = mean + cov_matching
    conservative = mean + cov_separate
    return mean, cov_matching, cov_separate, lower_shared, matching_separate_from_mean, conservative


def main() -> None:
    # Mean-vs-optimal-covariance crossover.
    xi9 = math.sqrt(7.0 * GM09 / (4.0 * GC09))
    xi14 = math.sqrt(7.0 * GM14 / (4.0 * GC14))
    assert abs(xi9 - 2.3297167719007548) < 1e-12
    assert abs(xi14 - 1.9117281723217037) < 1e-12

    # Transparent xi_mean=3 regression, inherited from the older calibration examples.
    b9 = burdens(GM09, GC09, 3.0)
    b14 = burdens(GM14, GC14, 3.0)

    expected9 = (1423539.2134444444, 2360509.17, 4721018.34,
                 2360509.17, 3784048.3834444443, 6144557.553444444)
    expected14 = (4415977.3, 10874694.4, 21749388.8,
                  10874694.4, 15290671.7, 26165366.1)
    for x, y in zip(b9, expected9):
        assert abs(x-y) < 2e-6 * max(1.0, abs(y))
    for x, y in zip(b14, expected14):
        assert abs(x-y) < 2e-6 * max(1.0, abs(y))

    ratios = (b14[3]/b9[3], b14[4]/b9[4], b14[5]/b9[5])
    assert abs(ratios[0] - 4.606927411343206) < 1e-12
    assert abs(ratios[1] - 4.040823517716655) < 1e-12
    assert abs(ratios[2] - 4.258299458084257) < 1e-12

    # Limiting branch ratios are set by the stored gamma ratios.
    assert abs(GM14/GM09 - 3.1021114545309567) < 1e-12
    assert abs(GC14/GC09 - 4.606927411343206) < 1e-12

    print("mean/cov crossover xi Toy009", xi9)
    print("mean/cov crossover xi Toy014", xi14)
    print("xi=3 Toy009 burdens", b9)
    print("xi=3 Toy014 burdens", b14)
    print("Toy014/Toy009 lower, matching, conservative ratios", ratios)


if __name__ == "__main__":
    main()
