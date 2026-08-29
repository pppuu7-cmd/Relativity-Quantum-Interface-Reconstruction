"""RQIR Iteration 023 — colored drift / Allan-variance cadence audit.

This layer does not assume a specific clock or reference instrument.  It maps a
required physical prior sigma_target into a recalibration cadence under a simple
white-reference + random-walk drift + optional irreducible Allan-floor model.

If each reference block leaves variance sigma_ref^2 and the uncontrolled drift is
a Brownian/random-walk process with diffusion D [unit^2/s], then the time-average
variance over a recalibration interval Delta is

    <sigma^2> = sigma_floor^2 + sigma_ref^2 + D Delta / 2.

Thus a target variance sigma_target^2 is feasible only when
sigma_floor^2 + sigma_ref^2 < sigma_target^2, and the maximum cadence is

    Delta_max = 2 (sigma_target^2 - sigma_floor^2 - sigma_ref^2) / D.

The reference duty-cost is approximately t_ref / Delta_max when Delta_max is much
longer than one block.  An irreducible Allan floor >= sigma_target makes the
requirement impossible regardless of recalibration frequency.
"""
from __future__ import annotations

import math


def coherence_floor_s(tau_max: float, f_gap_hz: float) -> float:
    return tau_max / (2.0 * math.pi * f_gap_hz)


def reference_block_time_s(
    sigma_event: float,
    sigma_ref: float,
    cycle_s: float,
    acceptance: float = 1.0,
) -> float:
    """White independent-event time to estimate a reference coordinate."""
    return cycle_s / acceptance * (sigma_event / sigma_ref) ** 2


def max_recalibration_interval_s(
    sigma_target: float,
    sigma_ref: float,
    diffusion_per_s: float,
    sigma_floor: float = 0.0,
) -> float:
    """Maximum interval for the *time-averaged* variance budget.

    diffusion_per_s is D in Var[x(t+dt)-x(t)] = D dt.
    Returns inf for D=0 and raises ValueError when the target is infeasible even
    immediately after a reference block.
    """
    margin = sigma_target**2 - sigma_floor**2 - sigma_ref**2
    if margin <= 0.0:
        raise ValueError("Allan/reference floor exhausts target variance budget")
    if diffusion_per_s == 0.0:
        return math.inf
    if diffusion_per_s < 0.0:
        raise ValueError("diffusion must be non-negative")
    return 2.0 * margin / diffusion_per_s


def reference_overhead_fraction(block_s: float, cadence_s: float) -> float:
    if math.isinf(cadence_s):
        return 0.0
    return block_s / cadence_s


def diffusion_us2_per_hour_to_s2_per_s(value: float) -> float:
    return value * 1.0e-12 / 3600.0


def benchmark() -> None:
    tau_max = 4.99085067
    f_gap = 100.0
    dead_s = 1.0e-3
    acceptance = 0.5
    t_cycle = coherence_floor_s(tau_max, f_gap) + dead_s

    # Iteration-016/018 first-order physical timing-prior targets.
    targets_us = {"D1": 9.47, "D2": 8.01}
    sigma_event_us = 10.0

    # Reserve only 1/9 of target variance for white reference estimation:
    # sigma_ref = sigma_target/3. Remaining budget is available for drift.
    for branch, target_us in targets_us.items():
        sigma_ref_us = target_us / 3.0
        block_s = reference_block_time_s(
            sigma_event_us * 1e-6,
            sigma_ref_us * 1e-6,
            t_cycle,
            acceptance,
        )
        print(branch, "reference block [s]", block_s)

        for d_us2_h in (1.0, 10.0, 100.0, 1000.0):
            cadence_s = max_recalibration_interval_s(
                target_us * 1e-6,
                sigma_ref_us * 1e-6,
                diffusion_us2_per_hour_to_s2_per_s(d_us2_h),
            )
            overhead = reference_overhead_fraction(block_s, cadence_s)
            print(
                branch,
                "D [us^2/h]", d_us2_h,
                "cadence [h]", cadence_s / 3600.0,
                "overhead", overhead,
            )

    # Regression values for the transparent benchmark.
    d1_block = reference_block_time_s(10e-6, (9.47/3)*1e-6, t_cycle, acceptance)
    d2_block = reference_block_time_s(10e-6, (8.01/3)*1e-6, t_cycle, acceptance)
    assert 0.179 < d1_block < 0.180
    assert 0.250 < d2_block < 0.252

    d1_cad = max_recalibration_interval_s(
        9.47e-6, (9.47/3)*1e-6, diffusion_us2_per_hour_to_s2_per_s(100.0)
    )
    d2_cad = max_recalibration_interval_s(
        8.01e-6, (8.01/3)*1e-6, diffusion_us2_per_hour_to_s2_per_s(100.0)
    )
    assert abs(d1_cad/3600.0 - 1.5943271111111113) < 1e-12
    assert abs(d2_cad/3600.0 - 1.140624) < 1e-12

    # Irreducible floor gate.
    try:
        max_recalibration_interval_s(8.01e-6, 1e-6, 1e-20, sigma_floor=8.01e-6)
    except ValueError:
        pass
    else:
        raise AssertionError("floor >= target must be infeasible")


if __name__ == "__main__":
    benchmark()
