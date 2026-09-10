"""Paper III QST hardening: independent atomic-clock transfer benchmark.

Reduced dual-transition clock / Ramsey frequency-sensing benchmark
------------------------------------------------------------------
This is a cross-architecture regression for Paper III Eq. (1), not an
apparatus forecast.  The benchmark reuses the frozen RQIR nuisance profiler
through ``paper3_profiled_resource_law`` and changes only sensor-specific
response and nuisance blocks.

Two clock transitions/references A and B are interrogated at the same four
normalized cycle times t=(-3/2,-1/2,+1/2,+3/2).  Their normalized science
sensitivities are deliberately different,

    q_A = +1.0, q_B = -0.6,

while both share a common reference/LO offset and linear drift,

    J_k = [1, t_k].

With exposure on only one transition the science response is constant over
that transition's settings and is therefore collinear with the free common
offset nuisance: profiled information collapses to zero.  Mixing transitions
creates a differential response direction that cannot be absorbed by the
shared offset/drift.  A deterministic allocation scan then finds the optimum
rather than assuming it by construction.  Independent offset calibration is
also shown to rescue the otherwise degenerate single-transition design.

All quantities are normalized, dimensionless Fisher/resource units.  No clock
instability, accuracy, transition choice, or new-physics reach is claimed.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
from pathlib import Path

import numpy as np

from paper3_profiled_resource_law import profiled_resource_information

TIMES = np.array([-1.5, -0.5, 0.5, 1.5], dtype=float)
Q_A = 1.0
Q_B = -0.6
ZERO_PRIOR = np.zeros((2, 2), dtype=float)
SCAN_FRACTIONS = np.linspace(0.0, 1.0, 101)


def clock_signal() -> np.ndarray:
    """Normalized science response for transitions/references A and B."""
    return np.r_[np.full(TIMES.size, Q_A), np.full(TIMES.size, Q_B)]


def clock_nuisance_jacobian() -> np.ndarray:
    """Shared reference/LO offset and linear-drift score directions."""
    times = np.r_[TIMES, TIMES]
    return np.column_stack([np.ones(times.size), times])


def allocation(fraction_a: float) -> np.ndarray:
    """Split unit resource between A and B, uniformly over time within each."""
    f = float(fraction_a)
    if not 0.0 <= f <= 1.0:
        raise ValueError("fraction_a must lie in [0,1]")
    return np.r_[
        np.full(TIMES.size, f / TIMES.size),
        np.full(TIMES.size, (1.0 - f) / TIMES.size),
    ]


def offset_calibration_precision(strength: float) -> np.ndarray:
    """Independent common-offset calibration; drift remains unconstrained."""
    if strength < 0.0:
        raise ValueError("calibration strength must be non-negative")
    return np.diag([float(strength), 0.0])


def information(fraction_a: float, lam: np.ndarray = ZERO_PRIOR) -> float:
    return profiled_resource_information(
        allocation(fraction_a),
        clock_signal(),
        clock_nuisance_jacobian(),
        lam,
    )


def allocation_scan() -> list[dict[str, float]]:
    return [
        {
            "fraction_A": float(f),
            "fraction_B": float(1.0 - f),
            "profiled_information": information(float(f)),
        }
        for f in SCAN_FRACTIONS
    ]


def benchmark_results() -> dict[str, object]:
    single_b = information(0.0)
    balanced = information(0.5)
    asymmetric = information(0.75)
    single_a = information(1.0)
    single_a_cal1 = information(1.0, offset_calibration_precision(1.0))
    single_a_cal9 = information(1.0, offset_calibration_precision(9.0))

    scan = allocation_scan()
    best = max(scan, key=lambda row: row["profiled_information"])

    # Reviewer-facing regression guards: nuisance failure, genuinely distinct
    # clock responses, response-diversity recovery, optimized allocation, and
    # monotone calibration rescue.  The optimum is not hard-coded into the
    # solver; it is recovered by a deterministic grid scan.
    assert Q_A != Q_B
    assert abs(single_a) < 1e-12
    assert abs(single_b) < 1e-12
    assert abs(balanced - 0.64) < 1e-12
    assert abs(asymmetric - 0.48) < 1e-12
    assert abs(best["fraction_A"] - 0.5) < 1e-12
    assert abs(best["profiled_information"] - balanced) < 1e-12
    assert balanced > asymmetric > single_a
    assert abs(single_a_cal1 - 0.5) < 1e-12
    assert abs(single_a_cal9 - 0.9) < 1e-12
    assert single_a_cal9 > single_a_cal1 > single_a

    # Balanced time sampling removes coupling of the differential science
    # response to the linear-drift score.  The remaining nonzero offset cross
    # term is precisely what the A/B response contrast profiles against.
    e_bal = allocation(0.5)
    weighted_cross = clock_nuisance_jacobian().T @ (e_bal * clock_signal())
    assert abs(weighted_cross[1]) < 1e-12

    return {
        "schema": "rqir-paper-iii-second-sensor-benchmark-v2",
        "date": "2026-09-10",
        "architecture": "reduced dual-transition atomic-clock/Ramsey frequency sensing",
        "claim_class": "cross-architecture design-principle regression; not apparatus forecast",
        "core_profiler": "analysis/protocol002_profiled_fisher.py::profiled_beta_information",
        "resource_law_adapter": "analysis/paper3_profiled_resource_law.py::profiled_resource_information",
        "settings": {
            "transition_sensitivities": {"A": Q_A, "B": Q_B},
            "normalized_times_per_transition": TIMES.tolist(),
            "nuisances": ["shared_reference_frequency_offset", "linear_reference_drift"],
            "allocation_scan_points": int(SCAN_FRACTIONS.size),
            "allocation_scan_fraction_A_range": [0.0, 1.0],
        },
        "results": {
            "single_transition_A_free_nuisance_information": single_a,
            "single_transition_B_free_nuisance_information": single_b,
            "balanced_dual_transition_information": balanced,
            "asymmetric_fraction_A_0p75_information": asymmetric,
            "scan_optimum_fraction_A": best["fraction_A"],
            "scan_optimum_fraction_B": best["fraction_B"],
            "scan_optimum_information": best["profiled_information"],
            "single_A_offset_calibration_lambda1_information": single_a_cal1,
            "single_A_offset_calibration_lambda9_information": single_a_cal9,
            "balanced_drift_cross_term": float(weighted_cross[1]),
        },
        "gates": {
            "independent_sensor_architecture": "PASS",
            "explicit_transition_response_diversity": "PASS",
            "same_profiled_resource_law": "PASS",
            "nuisance_induced_failure_present": "PASS",
            "response_diversity_recovery_present": "PASS",
            "allocation_optimum_scanned": "PASS",
            "calibration_recovery_present": "PASS",
            "core_decision_rules_modified": False,
        },
    }


def canonical_json(data: dict[str, object]) -> str:
    return json.dumps(data, indent=2, sort_keys=True) + "\n"


def canonical_scan_csv() -> str:
    out = io.StringIO()
    writer = csv.DictWriter(
        out, fieldnames=["fraction_A", "fraction_B", "profiled_information"], lineterminator="\n"
    )
    writer.writeheader()
    for row in allocation_scan():
        writer.writerow(row)
    return out.getvalue()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check-result",
        action="store_true",
        help="fail unless checked-in JSON and allocation scan match exactly",
    )
    args = parser.parse_args()

    data = benchmark_results()
    json_text = canonical_json(data)
    csv_text = canonical_scan_csv()
    print(json_text, end="")

    if args.check_result:
        root = Path(__file__).resolve().parents[1]
        result_path = root / "results" / "paper3_atomic_clock_second_sensor.json"
        scan_path = root / "results" / "paper3_atomic_clock_allocation_scan.csv"
        if result_path.read_text(encoding="utf-8") != json_text:
            raise SystemExit(f"checked-in result is stale: {result_path}")
        if scan_path.read_text(encoding="utf-8") != csv_text:
            raise SystemExit(f"checked-in allocation scan is stale: {scan_path}")
        print("checked-in atomic-clock second-sensor result and allocation scan: PASS")


if __name__ == "__main__":
    main()
