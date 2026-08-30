#!/usr/bin/env python3
"""RQIR Iteration 093 — robust Toy009/Toy014 physical crossover.

This script is a deterministic algebra/regression certificate.  It does not
supply hardware performance.  The input intervals are either measured/design
inputs or explicitly synthetic regression values.
"""

from dataclasses import dataclass
from math import isclose
import random


@dataclass(frozen=True)
class ArchBox:
    A_lo: float
    A_hi: float
    Rsrc_lo: float
    Rsrc_hi: float
    d_lo: float
    d_hi: float

    def validate(self):
        assert 0 < self.A_lo <= self.A_hi
        assert 0 < self.Rsrc_lo <= self.Rsrc_hi
        assert 0 <= self.d_lo <= self.d_hi < 1

    @property
    def m_lo(self):
        return 1.0 / (1.0 - self.d_lo)

    @property
    def m_hi(self):
        return 1.0 / (1.0 - self.d_hi)


def time_lower(a: ArchBox, R0: float, Csrc: float) -> float:
    return a.m_lo * (a.A_lo / R0 + Csrc / a.Rsrc_hi)


def time_upper(a: ArchBox, R0: float, Csrc: float) -> float:
    return a.m_hi * (a.A_hi / R0 + Csrc / a.Rsrc_lo)


def robust_difference_coeffs(i: ArchBox, k: ArchBox, Csrc: float):
    """Coefficients of T_i^upper - T_k^lower = D/R0 + S."""
    D = i.m_hi * i.A_hi - k.m_lo * k.A_lo
    S = Csrc * (i.m_hi / i.Rsrc_lo - k.m_lo / k.Rsrc_hi)
    return D, S


def winning_region(D: float, S: float, eps: float = 1e-15):
    """Return exact positive-R0 region where D/R0+S < 0.

    Result is (kind, threshold):
      ('all', None), ('none', None), ('above', R*), ('below', R*).
    """
    if abs(D) < eps:
        D = 0.0
    if abs(S) < eps:
        S = 0.0

    if D <= 0 and S <= 0 and (D < 0 or S < 0):
        return "all", None
    if D >= 0 and S >= 0:
        return "none", None
    Rstar = -D / S
    assert Rstar > 0
    if D > 0 and S < 0:
        return "above", Rstar
    if D < 0 and S > 0:
        return "below", Rstar
    raise AssertionError("unhandled sign case")


def brute_box_extrema(a: ArchBox, R0: float, Csrc: float):
    vals = []
    for A in (a.A_lo, a.A_hi):
        for R in (a.Rsrc_lo, a.Rsrc_hi):
            for d in (a.d_lo, a.d_hi):
                vals.append((1.0 / (1.0 - d)) * (A / R0 + Csrc / R))
    return min(vals), max(vals)


def main():
    # Synthetic regression only; these are NOT apparatus forecasts.
    Csrc = 225.0
    toy009 = ArchBox(1.0, 1.1, 1.0, 1.1, 0.02, 0.04)
    toy014 = ArchBox(3.3, 3.8, 1.4, 1.6, 0.03, 0.06)
    toy009.validate(); toy014.validate()

    D14, S14 = robust_difference_coeffs(toy014, toy009, Csrc)
    kind14, cross14 = winning_region(D14, S14)
    D09, S09 = robust_difference_coeffs(toy009, toy014, Csrc)
    kind09, cross09 = winning_region(D09, S09)

    assert kind14 == "above"
    assert kind09 == "below"
    assert isclose(cross14, 0.08006274509803925, rel_tol=1e-12)
    assert isclose(cross09, 0.025237237237237236, rel_tol=1e-12)
    assert cross09 < cross14  # an unresolved NG-030 throughput band exists

    # Endpoint formulas are exact for independent Cartesian boxes.
    for R0 in (0.01, 0.03, 0.1, 1.0, 100.0):
        for a in (toy009, toy014):
            blo, bhi = brute_box_extrema(a, R0, Csrc)
            assert isclose(blo, time_lower(a, R0, Csrc), rel_tol=1e-13)
            assert isclose(bhi, time_upper(a, R0, Csrc), rel_tol=1e-13)

    # Random interior points must remain inside the analytic time interval.
    rng = random.Random(20260830093)
    for _ in range(10000):
        a = toy014 if rng.random() < 0.5 else toy009
        R0 = 10 ** rng.uniform(-2.5, 2.5)
        A = rng.uniform(a.A_lo, a.A_hi)
        R = rng.uniform(a.Rsrc_lo, a.Rsrc_hi)
        d = rng.uniform(a.d_lo, a.d_hi)
        t = (A / R0 + Csrc / R) / (1.0 - d)
        assert time_lower(a, R0, Csrc) - 1e-12 <= t <= time_upper(a, R0, Csrc) + 1e-12

    # Check the three regions explicitly.
    assert time_upper(toy009, 0.01, Csrc) < time_lower(toy014, 0.01, Csrc)
    assert not (time_upper(toy009, 0.05, Csrc) < time_lower(toy014, 0.05, Csrc))
    assert not (time_upper(toy014, 0.05, Csrc) < time_lower(toy009, 0.05, Csrc))
    assert time_upper(toy014, 0.1, Csrc) < time_lower(toy009, 0.1, Csrc)

    print("PASS Iteration 093 robust physical crossover")
    print(f"Toy009 robust-win region: R0 < {cross09:.15g}")
    print(f"unresolved NG-030 band: [{cross09:.15g}, {cross14:.15g}]")
    print(f"Toy014 robust-win region: R0 > {cross14:.15g}")


if __name__ == "__main__":
    main()
