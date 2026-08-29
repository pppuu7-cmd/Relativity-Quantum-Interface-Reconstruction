"""RQIR Iteration 040: covariance graph congestion and subset resource dominance.

Uses the actual centered D2 covariance graph to compare three already-confirmed
row selections at y_ref=-4, lambda=1:

  best4 = (0,1,3,7), C_alpha*=0.0500614, F_beta~0.899477
  best5 = (0,1,3,6,7), C_alpha*=0, F_beta~0.903527
  all8  = (0,1,2,3,4,5,6,7), C_alpha*=0, F_beta~0.905293

For the natural cross-covariance-only joint Gaussian trajectory, a uniform edge
derivative amplitude a must satisfy a*rho(A_graph)<1 for every signed edge
pattern.  The worst sign pattern has spectral radius equal to that of the
unsigned graph here.  Thus per-edge Fisher K_ii=a^2 is bounded by
1/rho(A_graph)^2.

Adding covariance rows can therefore make every simultaneously acquired edge
more expensive by increasing graph spectral radius.  This script quantifies
that congestion penalty and compares best4+minimal source metrology against
best5 with no source prior.
"""
from __future__ import annotations

import math
import numpy as np

GAMMA_COV = 0.590127e6
FQ_ALPHA = 0.0849323916
C0 = 4.55511
C4 = 0.0500614
TMAX = 4.99085067

# Eight centered force-covariance rows mapped to the unique endpoint graph.
# Vertex IDs:
# 0 G0@0, 1 G1@0, 2 G0@TR, 3 G0@T1, 4 G1@T5,
# 5 G1@TR, 6 G1@T3, 7 G0@T6.
EDGES = {
    0: (0, 2),
    1: (1, 3),
    2: (1, 4),
    3: (0, 5),
    4: (1, 2),
    5: (0, 6),
    6: (0, 7),
    7: (1, 7),
}

SUBSETS = {
    "best4": (0, 1, 3, 7),
    "best5": (0, 1, 3, 6, 7),
    "all8": tuple(range(8)),
}


def adjacency(subset: tuple[int, ...]) -> np.ndarray:
    a = np.zeros((8, 8), float)
    for e in subset:
        i, j = EDGES[e]
        a[i, j] = 1.0
        a[j, i] = 1.0
    return a


def spectral_radius(subset: tuple[int, ...]) -> float:
    ev = np.linalg.eigvalsh(adjacency(subset))
    return float(np.max(np.abs(ev)))


def edge_fisher_limit(subset: tuple[int, ...]) -> float:
    rho = spectral_radius(subset)
    return 1.0 / (rho * rho)


def accepted_cycles_lower_bound(subset: tuple[int, ...]) -> float:
    return GAMMA_COV / edge_fisher_limit(subset)


def coherence_floor(gap_hz: float) -> float:
    return TMAX / (2.0 * math.pi * gap_hz)


def main() -> None:
    out = {}
    for name, subset in SUBSETS.items():
        rho = spectral_radius(subset)
        flim = edge_fisher_limit(subset)
        n = accepted_cycles_lower_bound(subset)
        out[name] = (rho, flim, n)
        print(name, "rho=", rho, "Kii_limit=", flim, "N_lower=", n)

    rho4, f4, n4 = out["best4"]
    rho5, f5, n5 = out["best5"]
    rho8, f8, n8 = out["all8"]

    assert abs(rho4 - math.sqrt(2.0)) < 1e-12
    assert abs(f4 - 0.5) < 1e-12
    # rho^2 for best5 is (5+sqrt(5))/2 = 3.6180339887...
    assert abs(rho5**2 - 3.618033988749895) < 1e-12
    assert abs(f5 - 0.27639320225002106) < 1e-12
    assert abs(rho8 - math.sqrt(6.0)) < 1e-12
    assert abs(f8 - 1.0 / 6.0) < 1e-12

    assert abs(n4 - 1180254.0) < 1e-6
    assert abs(n5 - 2135099.5436790087) < 1e-6
    assert abs(n8 - 3540762.0) < 1e-6

    # Whole-subset comparison to source metrology from the no-extra-force-cov
    # baseline C_alpha=C0.
    for name, c_saved in (("best4", C0 - C4), ("best5", C0), ("all8", C0)):
        n = out[name][2]
        prep_copy_equiv = c_saved / FQ_ALPHA
        ratio = n / prep_copy_equiv
        print(name, "saved prep copies=", prep_copy_equiv, "tP/tC break-even=", ratio)

    # Critical comparison: best4 + residual source prior versus best5 with no
    # source prior.  The fifth edge eliminates only C4, but it raises the graph
    # congestion floor for the entire shared covariance trajectory.
    extra_cov_cycles = n5 - n4
    residual_prep_copies = C4 / FQ_ALPHA
    ratio_5_vs_4prep = extra_cov_cycles / residual_prep_copies
    print("best5 minus best4 extra covariance cycles", extra_cov_cycles)
    print("best4 residual prep copy equivalents", residual_prep_copies)
    print("best5 beats best4+prep only if tP/tC >", ratio_5_vs_4prep)

    assert abs(extra_cov_cycles - 954845.5436790087) < 1e-6
    assert abs(residual_prep_copies - 0.5894264727145632) < 1e-12
    assert abs(ratio_5_vs_4prep - 1619957.0054625017) < 1e-6

    tc100 = coherence_floor(100.0)
    tpcrit = ratio_5_vs_4prep * tc100
    tpcrit_dead = ratio_5_vs_4prep * (tc100 + 1e-3)
    print("100Hz best5-vs-best4+prep tPcrit", tpcrit,
          "with +1ms", tpcrit_dead)
    assert abs(tpcrit - 12867.619067108051) < 1e-6
    assert abs(tpcrit_dead - 14487.576072570551) < 1e-6

    # At the fixed 90% target, all8 and best5 both require C_alpha=0, while
    # all8 has a strictly larger graph-congestion lower bound.  Hence all8 is
    # resource-dominated by best5 for covariance-only replacement under this
    # architecture, absent another robustness/target benefit.
    assert n8 > n5


if __name__ == "__main__":
    main()
