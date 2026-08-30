"""RQIR Iteration 073: local-source physical Pareto / lower-envelope audit.

Uses physical D2 science-time factors, Iteration-063 spectral-tilt-profiled
calibration-cost ratios, and independent zero-reset Ramsey source-metrology
time factors to determine which retained local source designs can minimize a
weighted projected wall-clock objective

    L_i(x,y) = q_s,i + q_c,i x + q_p,i y,

where x and y are Toy009-reference calibration/science and source/science time
ratios.  For locality-only comparison x,y are simply nonnegative resource
weights; they need not imply that Toy009 itself is physically admissible.

The Iteration-063 Toy011/Toy012 calibration ratios are finite-scan values and
are therefore used as reference central values, not exact apparatus constants.
The script emphasizes robust witness points rather than over-interpreting the
last digits of pairwise crossover locations.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Source:
    qs: float  # science time / Toy009 science time
    qc: float  # physical calibration time proxy / Toy009
    qp: float  # Ramsey source-metrology time / Toy009


# Physical science factors.
SOURCES = {
    # Iteration 053 physical two-band S_eff ratios + Iteration 063 physical cal
    # ratios + Iteration 054 Ramsey-rate ratios.
    "Toy011-response": Source(
        qs=1.0 / 0.1558200714788344,
        qc=21.7,
        qp=1.0 / 0.2660,
    ),
    "Toy011-conditioning": Source(
        qs=1.0 / 0.08163415302222209,
        qc=8.83,
        qp=1.0 / 0.4195,
    ),
    # Iteration 062 physical science ratio, Iteration 063 physical calibration
    # central value (~5.2e2), Iteration 055 Ramsey rate ratio.
    "Toy012-high": Source(
        qs=1.0 / 1.2139856294e-4,
        qc=520.0,
        qp=1.0 / 1.150503,
    ),
    # Executed Iteration 065/066 values.
    "Toy013-29100": Source(
        qs=23.64956630775,
        qc=0.1233011369,
        qp=330.9066843,
    ),
}

TOY009 = Source(1.0, 1.0, 1.0)


def objective(s: Source, x: float, y: float) -> float:
    if x < 0 or y < 0:
        raise ValueError("resource weights must be nonnegative")
    return s.qs + s.qc * x + s.qp * y


def winner(x: float, y: float, sources=SOURCES) -> str:
    return min(sources, key=lambda name: objective(sources[name], x, y))


def intersection_axis(a: Source, b: Source, axis: str) -> float:
    if axis == "x":
        den = a.qc - b.qc
        return (b.qs - a.qs) / den
    if axis == "y":
        den = a.qp - b.qp
        return (b.qs - a.qs) / den
    raise ValueError(axis)


def componentwise_dominated(a: Source, b: Source) -> bool:
    """True if a is no better than b on every axis and worse on at least one."""
    vals_a = (a.qs, a.qc, a.qp)
    vals_b = (b.qs, b.qc, b.qp)
    return all(x >= y for x, y in zip(vals_a, vals_b)) and any(
        x > y for x, y in zip(vals_a, vals_b)
    )


def main() -> None:
    for name, s in SOURCES.items():
        print(name, s)

    # Unrestricted comparison: Toy009 componentwise dominates both Toy011
    # points.  Toy012-high and Toy013 each retain one axis better than Toy009
    # (source metrology and calibration respectively), so they remain
    # conditional contenders rather than strict dominated points.
    assert componentwise_dominated(SOURCES["Toy011-response"], TOY009)
    assert componentwise_dominated(SOURCES["Toy011-conditioning"], TOY009)
    assert not componentwise_dominated(SOURCES["Toy012-high"], TOY009)
    assert not componentwise_dominated(SOURCES["Toy013-29100"], TOY009)

    # Locality-only lower-envelope witnesses.  Each retained local source wins
    # at at least one well-separated point, robust to modest rounding of the
    # Iteration-063 calibration ratios.
    witnesses = {
        "Toy011-response": (0.0, 0.0),
        "Toy011-conditioning": (0.7, 0.0),
        "Toy013-29100": (2.0, 0.0),
        "Toy012-high": (0.0, 6000.0),
    }
    for expected, (x, y) in witnesses.items():
        got = winner(x, y)
        print("witness", x, y, "->", got)
        assert got == expected

    r = SOURCES["Toy011-response"]
    c = SOURCES["Toy011-conditioning"]
    h = SOURCES["Toy012-high"]
    t = SOURCES["Toy013-29100"]

    # Central-value axis crossovers, useful only as reference geometry.
    x_rc = intersection_axis(r, c, "x")
    x_ct = intersection_axis(c, t, "x")
    y_rc = intersection_axis(r, c, "y")
    y_ch = intersection_axis(c, h, "y")
    print("central y=0 x crossovers response->conditioning->Toy013", x_rc, x_ct)
    print("central x=0 y crossovers response->conditioning->Toy012-high", y_rc, y_ch)

    assert 0.44 < x_rc < 0.47
    assert 1.25 < x_ct < 1.37
    assert 4.0 < y_rc < 4.5
    assert 5.2e3 < y_ch < 5.7e3

    # Direct balanced Toy012 was removed in Iteration 072; the high-response
    # point is the only Toy012 branch retained in this local reference Pareto
    # set because its Ramsey axis is genuinely better than Toy009.


if __name__ == "__main__":
    main()
