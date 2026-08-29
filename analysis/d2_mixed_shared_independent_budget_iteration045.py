"""RQIR Iteration 045: mixed shared-science + independent mean-calibration budget.

Iteration 044 found that, in the reciprocal linear quantum-limited class, a
science/source copy that must preserve at least 90% of the unperturbed raw D2
signal Fisher can carry at most

    xi_shared <= 0.7239816836
    I_shared <= 0.5241494782

of normalized force-mean Fisher per row at eta=1 in the current Toy009
dephasing proxy.

This script credits that maximum amount to each accepted best4 covariance
trajectory, then computes the residual centered gamma_mean that must still be
obtained on independent/sacrificial time-layer preparations.

This is deliberately optimistic: it assumes the shared-copy cap can be earned
for every mean row without additional cross-time backaction and uses raw signal
Fisher rather than the full profiled F_beta|theta.  Therefore it is a lower
bound on the required independent calibration burden.
"""
from __future__ import annotations

import math

import d2_time_layer_mean_budget_iteration042 as i42
import d2_reciprocal_linear_probe_bound_iteration044 as i44

TARGET_RAW_FISHER_RETENTION = 0.90


def shared_xi_cap(eta: float = 1.0) -> float:
    return i44.max_xi_for_response_norm(math.sqrt(TARGET_RAW_FISHER_RETENTION), eta)


def shared_info_cap(eta: float = 1.0) -> float:
    x = shared_xi_cap(eta)
    return x * x


def residual_mean_fisher_per_row(eta: float = 1.0) -> float:
    credited = i42.N_COV_BEST4 * shared_info_cap(eta)
    return max(0.0, i42.GAMMA_MEAN - credited)


def shared_fraction_of_mean_target(eta: float = 1.0) -> float:
    return min(1.0, i42.N_COV_BEST4 * shared_info_cap(eta) / i42.GAMMA_MEAN)


def residual_mean_wall_time_seconds(xi_independent: float, gap_hz: float,
                                    acceptance: float = 1.0,
                                    dead_time_s: float = 0.0,
                                    eta_shared: float = 1.0) -> float:
    if xi_independent <= 0:
        raise ValueError("xi_independent must be positive")
    residual = residual_mean_fisher_per_row(eta_shared)
    te = i42.evolution_times_seconds(gap_hz)
    per_layer_attempts = residual / (xi_independent * xi_independent) / acceptance
    return per_layer_attempts * float((te + dead_time_s).sum())


def mixed_campaign_seconds(xi_independent: float, gap_hz: float,
                           acceptance: float = 1.0,
                           dead_time_s: float = 0.0,
                           eta_shared: float = 1.0) -> float:
    # best4 covariance/science trajectory plus residual independent mean layers.
    return (i42.covariance_floor_seconds(gap_hz, acceptance, dead_time_s)
            + residual_mean_wall_time_seconds(xi_independent, gap_hz,
                                              acceptance, dead_time_s,
                                              eta_shared))


def main() -> None:
    xi = shared_xi_cap(1.0)
    info = shared_info_cap(1.0)
    credited = i42.N_COV_BEST4 * info
    residual = residual_mean_fisher_per_row(1.0)
    frac = shared_fraction_of_mean_target(1.0)

    print("90%-raw-Fisher shared xi cap", xi)
    print("shared per-row Fisher cap", info)
    print("best4 trajectories credited mean Fisher/row", credited)
    print("residual mean Fisher/row", residual)
    print("fraction of gamma_mean that can be shared", frac)

    assert abs(xi - 0.7239816836368367) < 2e-12
    assert abs(info - 0.5241494782416287) < 2e-12
    assert abs(credited - 618629.5182925953) < 2e-6
    assert abs(residual - 1211635.4817074048) < 2e-6
    assert abs(frac - 0.3379999717486786) < 2e-12

    # Even this optimistic science-copy credit closes only ~33.8% of the
    # centered per-row mean target; at least ~66.2% must remain independent.
    assert residual / i42.GAMMA_MEAN > 0.66

    # Transparent benchmark retained from Iteration 042.
    p = 0.5
    dead = 1e-3
    gap = 100.0
    tcov = i42.covariance_floor_seconds(gap, p, dead)
    print("best4 covariance/science floor hours", tcov / 3600.0)

    expected_mixed = {
        1.0: 35.71039134553725,
        2.0: 13.325610549144002,
        3.0: 9.180280772034143,
        5.0: 7.057871926153894,
        10.0: 6.162480694298163,
    }
    for xi_ind, expected_hours in expected_mixed.items():
        tres = residual_mean_wall_time_seconds(xi_ind, gap, p, dead, 1.0)
        tmix = tcov + tres
        tfull = tcov + i42.mean_wall_time_seconds(xi_ind, gap, p, dead, True)
        print("xi_ind", xi_ind,
              "residual mean h", tres / 3600.0,
              "mixed total h", tmix / 3600.0,
              "fully independent total h", tfull / 3600.0,
              "optimistic shared saving h", (tfull - tmix) / 3600.0)
        assert abs(tmix / 3600.0 - expected_hours) < 2e-12

    # Shared-copy efficiency below one makes the same-copy mean credit smaller.
    for eta in (0.8, 0.5, 0.2):
        f = shared_fraction_of_mean_target(eta)
        print("eta_shared", eta, "shareable fraction of gamma_mean", f)
        # xi cap^2 scales linearly with eta in the present quantum-limited proxy.
        assert abs(f - frac * eta) < 2e-12


if __name__ == "__main__":
    main()
