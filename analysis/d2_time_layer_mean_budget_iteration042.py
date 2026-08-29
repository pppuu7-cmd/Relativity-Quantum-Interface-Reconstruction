"""RQIR Iteration 042: backaction-safe D2 time-layer mean calibration budget.

Uses Iteration 041's operator compatibility result: at each stored phase the two
probe-force observables commute, while observables at distinct phases do not.
A conservative strong-measurement baseline therefore uses seven independent
source-preparation/time layers and (optimistically) measures the two probes in
parallel within each layer.

Maps the current centered D2 mean Fisher target into accepted repetitions and
wall time as a function of per-cycle standardized row sensitivity xi_mu,
acceptance p, gap frequency and dead/readout time.

This is a lower-bound scheduling model, not an apparatus forecast. State
preparation time and physical force transduction are not included unless they
are explicitly added to the per-cycle overhead.
"""
from __future__ import annotations

import math
import numpy as np

GAMMA_MEAN = 1.830265e6
TIMES = np.array([0., 3.09855988, 3.45849306, 2.93830159,
                  4.13016958, 4.84480925, 4.99085067])
N_COV_BEST4 = 1.180254e6


def evolution_times_seconds(gap_hz: float) -> np.ndarray:
    return TIMES / (2.0 * math.pi * gap_hz)


def accepted_cycles_per_layer(xi_mu: float) -> float:
    if xi_mu <= 0:
        raise ValueError("xi_mu must be positive")
    return GAMMA_MEAN / (xi_mu * xi_mu)


def total_accepted_layer_cycles(xi_mu: float, parallel_two_probe: bool = True) -> float:
    factor = 7.0 if parallel_two_probe else 14.0
    return factor * GAMMA_MEAN / (xi_mu * xi_mu)


def mean_wall_time_seconds(xi_mu: float, gap_hz: float,
                           acceptance: float = 1.0,
                           dead_time_s: float = 0.0,
                           parallel_two_probe: bool = True) -> float:
    if not (0 < acceptance <= 1):
        raise ValueError("acceptance must be in (0,1]")
    te = evolution_times_seconds(gap_hz)
    per_layer = accepted_cycles_per_layer(xi_mu) / acceptance
    # Same-time dual-probe readout shares one preparation/evolution only in the
    # parallel branch. Otherwise each probe requires an independent campaign.
    factor = 1.0 if parallel_two_probe else 2.0
    return factor * per_layer * float(np.sum(te + dead_time_s))


def covariance_floor_seconds(gap_hz: float, acceptance: float = 1.0,
                             dead_time_s: float = 0.0) -> float:
    tmax = float(np.max(evolution_times_seconds(gap_hz)))
    return N_COV_BEST4 / acceptance * (tmax + dead_time_s)


def xi_for_mean_not_slower_than_cov(gap_hz: float, acceptance: float = 1.0,
                                     dead_time_s: float = 0.0,
                                     parallel_two_probe: bool = True) -> float:
    t_mean_xi1 = mean_wall_time_seconds(1.0, gap_hz, acceptance, dead_time_s,
                                       parallel_two_probe)
    t_cov = covariance_floor_seconds(gap_hz, acceptance, dead_time_s)
    return math.sqrt(t_mean_xi1 / t_cov)


def main() -> None:
    # Exact scheduling arithmetic at 100 Hz.
    te = evolution_times_seconds(100.0)
    print("evolution times [s]", te)
    print("sum evolution time per 7-layer bundle", float(np.sum(te)))
    print("max coherence/evolution time", float(np.max(te)))

    # Ideal lower bound: p=1, zero dead/readout time.
    ideal_par = mean_wall_time_seconds(1.0, 100.0, 1.0, 0.0, True)
    ideal_seq = mean_wall_time_seconds(1.0, 100.0, 1.0, 0.0, False)
    cov_ideal = covariance_floor_seconds(100.0, 1.0, 0.0)
    xi_ideal = xi_for_mean_not_slower_than_cov(100.0, 1.0, 0.0, True)
    xi_ideal_seq = xi_for_mean_not_slower_than_cov(100.0, 1.0, 0.0, False)
    print("ideal parallel mean hours xi=1", ideal_par / 3600.0)
    print("ideal sequential mean hours xi=1", ideal_seq / 3600.0)
    print("ideal best4 covariance floor hours", cov_ideal / 3600.0)
    print("xi mean<=cov parallel/sequential", xi_ideal, xi_ideal_seq)

    assert abs(float(np.sum(te)) - 0.03733963409163134) < 1e-15
    assert abs(float(np.max(te)) - 0.00794318793930142) < 1e-15
    assert abs(ideal_par / 3600.0 - 18.983729275199895) < 1e-12
    assert abs(ideal_seq / 3600.0 - 37.96745855039979) < 1e-12
    assert abs(cov_ideal / 3600.0 - 2.6041601418397935) < 1e-12
    assert abs(xi_ideal - 2.699957463820608) < 1e-12
    assert abs(xi_ideal_seq - 3.8183164631655693) < 1e-12

    # Transparent benchmark retained from earlier resource work.
    p = 0.5
    dead = 1e-3
    cov = covariance_floor_seconds(100.0, p, dead)
    print("\np=0.5, dead=1ms best4 covariance floor hours", cov / 3600.0)
    for xi in (1.0, 2.0, 3.0, 5.0, 10.0):
        tpar = mean_wall_time_seconds(xi, 100.0, p, dead, True)
        nacc = total_accepted_layer_cycles(xi, True)
        print("xi", xi, "accepted layer-cycles", nacc,
              "parallel mean hours", tpar / 3600.0)

    xi_par = xi_for_mean_not_slower_than_cov(100.0, p, dead, True)
    xi_seq = xi_for_mean_not_slower_than_cov(100.0, p, dead, False)
    print("xi mean<=cov with p=.5 dead=1ms parallel/sequential", xi_par, xi_seq)

    assert abs(cov / 3600.0 - 5.864016950346254) < 1e-12
    assert abs(mean_wall_time_seconds(1.0, 100.0, p, dead, True) / 3600.0
               - 45.08515577262202) < 1e-12
    assert abs(mean_wall_time_seconds(10.0, 100.0, p, dead, True) / 3600.0
               - 0.4508515577262202) < 1e-12
    assert abs(xi_par - 2.7728040440172337) < 1e-12
    assert abs(xi_seq - 3.921337084852136) < 1e-12

    # Seven same-time layers halve the accepted-copy count relative to 14
    # independent row campaigns if dual-probe parallel readout is physically
    # available.
    assert abs(total_accepted_layer_cycles(1.0, True) - 7 * GAMMA_MEAN) < 1e-9
    assert abs(total_accepted_layer_cycles(1.0, False) - 14 * GAMMA_MEAN) < 1e-9


if __name__ == "__main__":
    main()
