"""RQIR Iteration 039: endpoint-sharing graph bound for high-value D2 covariance rows.

The best centered force-covariance rows from Iteration 034 are (0,1,3,7).
When written as pairwise phase/probe covariance entries they use only six
unique scalar detector endpoints, not eight independent outputs.  This script
builds that endpoint graph and derives a stricter positivity/Fisher bound for
a natural cross-covariance-only Gaussian encoding.

Rows:
  0: cov[G0(TR), G0(0)]
  1: cov[G0(T1), G1(0)]
  3: cov[G1(TR), G0(0)]
  7: cov[G0(T6), G1(0)]

The graph is two disjoint degree-2 stars.  If each source covariance coordinate
changes only its corresponding detector cross-covariance entry with whitened
amplitude a, the signed derivative sum on each star has operator norm a*sqrt(2).
Full-hypercube positivity therefore requires a<1/sqrt(2), so the per-row Fisher
K_ii=a^2 is <1/2.  This is stricter than the generic m=6 trace bound 3/4.
"""
from __future__ import annotations

import itertools
import math
import numpy as np

GAMMA_COV = 0.590127e6
DELTA_C_ALPHA = 4.55511 - 0.0500614
FQ_ALPHA = 0.0849323916
TR = 3.45849306
T1 = 3.09855988
T6 = 4.99085067

# Vertex labels for the six unique phase/probe endpoints.
VERTICES = (
    "G0@0",
    "G0@TR",
    "G0@T1",
    "G1@0",
    "G1@TR",
    "G0@T6",
)
VID = {x: i for i, x in enumerate(VERTICES)}

# High-value row index -> endpoint pair.
EDGES = {
    0: ("G0@TR", "G0@0"),
    1: ("G0@T1", "G1@0"),
    3: ("G1@TR", "G0@0"),
    7: ("G0@T6", "G1@0"),
}


def edge_derivatives(amplitude: float) -> list[np.ndarray]:
    m = len(VERTICES)
    hs = []
    for row in (0, 1, 3, 7):
        u, v = EDGES[row]
        h = np.zeros((m, m), float)
        i, j = VID[u], VID[v]
        h[i, j] = amplitude
        h[j, i] = amplitude
        hs.append(h)
    return hs


def fisher(hs: list[np.ndarray]) -> np.ndarray:
    q = len(hs)
    k = np.empty((q, q), float)
    for i in range(q):
        for j in range(q):
            k[i, j] = 0.5 * float(np.trace(hs[i] @ hs[j]))
    return k


def full_hypercube_positive(hs: list[np.ndarray]) -> bool:
    eye = np.eye(hs[0].shape[0])
    for signs in itertools.product((-1.0, 1.0), repeat=len(hs)):
        a = sum(s * h for s, h in zip(signs, hs))
        if np.min(np.linalg.eigvalsh(eye + a)) <= 0:
            return False
    return True


def opnorm_signed_max(hs: list[np.ndarray]) -> float:
    out = 0.0
    for signs in itertools.product((-1.0, 1.0), repeat=len(hs)):
        a = sum(s * h for s, h in zip(signs, hs))
        out = max(out, float(np.linalg.norm(a, 2)))
    return out


def ideal_edge_fisher_limit() -> float:
    return 0.5


def ideal_cycle_ratio() -> float:
    return GAMMA_COV * FQ_ALPHA / (DELTA_C_ALPHA * ideal_edge_fisher_limit())


def coherence_floor(gap_hz: float) -> float:
    return T6 / (2.0 * math.pi * gap_hz)


def critical_prep_cycle(gap_hz: float, dead_s: float = 0.0,
                        prep_eff: float = 1.0, cov_eff: float = 1.0) -> float:
    return ideal_cycle_ratio() * (coherence_floor(gap_hz) + dead_s) * prep_eff / cov_eff


def main() -> None:
    assert len(set(VERTICES)) == 6
    assert len(EDGES) == 4

    # Verify the graph degrees: two degree-2 centers and four leaves.
    deg = {v: 0 for v in VERTICES}
    for u, v in EDGES.values():
        deg[u] += 1
        deg[v] += 1
    print("endpoint degrees", deg)
    assert sorted(deg.values()) == [1, 1, 1, 1, 2, 2]

    # Near-saturating cross-covariance encoding.
    a = 0.999 / math.sqrt(2.0)
    hs = edge_derivatives(a)
    assert full_hypercube_positive(hs)
    signed_norm = opnorm_signed_max(hs)
    print("max signed derivative op norm", signed_norm)
    assert abs(signed_norm - 0.999) < 1e-12

    k = fisher(hs)
    eig = np.linalg.eigvalsh(k)
    print("K", k)
    print("K eig", eig)
    assert np.allclose(k, (0.999**2 / 2.0) * np.eye(4), atol=1e-14)
    assert np.max(eig) < 0.5

    # Generic m=6,q=4 trace theorem from Iteration 038 only gives 0.75;
    # the actual graph-sparse cross-covariance encoding is stricter: 0.5.
    generic_limit = 6.0 / (2.0 * 4.0)
    graph_limit = ideal_edge_fisher_limit()
    print("generic weakest-direction limit", generic_limit,
          "graph cross-covariance limit", graph_limit)
    assert graph_limit < generic_limit

    n_ideal = GAMMA_COV / graph_limit
    n_near = GAMMA_COV / float(np.min(eig))
    ratio = ideal_cycle_ratio()
    print("ideal accepted joint cycles >", n_ideal)
    print("near-saturating accepted joint cycles", n_near)
    print("equal-efficiency tP/tC >", ratio)
    assert abs(n_ideal - 1180254.0) < 1e-9
    assert abs(n_near - 1182618.0534889246) < 1e-6
    assert abs(ratio - 22250.990791856584) < 1e-9

    for f in (10.0, 100.0, 1000.0):
        tc = coherence_floor(f)
        tp0 = critical_prep_cycle(f)
        tp1 = critical_prep_cycle(f, 1e-3)
        print(f"gap={f:g}Hz Tcoh={tc:.12g}s tPcrit={tp0:.12g}s tPcrit+1ms={tp1:.12g}s")

    assert abs(coherence_floor(100.0) - 0.007943185543639977) < 1e-15
    assert abs(critical_prep_cycle(100.0) - 176.74374838954145) < 1e-6
    assert abs(critical_prep_cycle(100.0, 1e-3) - 198.99473918139802) < 1e-6


if __name__ == "__main__":
    main()
