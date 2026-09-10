"""Paper III QST hardening: second independent quantum-sensing architecture.

Reduced atomic-clock / Ramsey frequency-sensing benchmark
---------------------------------------------------------
The purpose is not an apparatus forecast.  It is a cross-architecture transfer
regression for Paper III Eq. (1), using the same frozen RQIR nuisance profiler
through ``paper3_profiled_resource_law``.

Four interleaved clock interrogation/control settings are represented at
normalized cycle times t = (-3/2,-1/2,+1/2,+3/2).  The shared nuisance space is
spanned by a local-oscillator (LO) frequency offset and a linear LO drift:

    J_k = [1, t_k].

Two science-response patterns are compared:

* ``unmodulated``: [1,1,1,1], exactly collinear with the free LO offset and
  therefore non-identifiable without independent offset calibration;
* ``control_reversal``: [1,-1,-1,1], a reduced signed-sensitivity control
  pattern whose uniform allocation is orthogonal to both offset and drift.

The benchmark also demonstrates finite-calibration rescue and loss of
profiled information under an asymmetric allocation.  All quantities are
normalized, dimensionless Fisher/resource units; no clock instability or
accuracy claim is made.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from paper3_profiled_resource_law import profiled_resource_information

TIMES = np.array([-1.5, -0.5, 0.5, 1.5], dtype=float)
UNIFORM = np.full(4, 0.25, dtype=float)
ASYMMETRIC = np.array([0.4, 0.3, 0.2, 0.1], dtype=float)
UNMODULATED = np.ones(4, dtype=float)
CONTROL_REVERSAL = np.array([1.0, -1.0, -1.0, 1.0], dtype=float)
ZERO_PRIOR = np.zeros((2, 2), dtype=float)


def clock_nuisance_jacobian() -> np.ndarray:
    """Shared LO offset and linear-drift score directions."""
    return np.column_stack([np.ones(4), TIMES])


def offset_calibration_precision(strength: float) -> np.ndarray:
    """Independent LO-offset calibration; drift remains unconstrained."""
    if strength < 0.0:
        raise ValueError("calibration strength must be non-negative")
    return np.diag([float(strength), 0.0])


def information(signal: np.ndarray, allocation: np.ndarray, lam: np.ndarray) -> float:
    return profiled_resource_information(
        allocation,
        signal,
        clock_nuisance_jacobian(),
        lam,
    )


def benchmark_results() -> dict[str, object]:
    unmodulated_free = information(UNMODULATED, UNIFORM, ZERO_PRIOR)
    reversal_uniform = information(CONTROL_REVERSAL, UNIFORM, ZERO_PRIOR)
    reversal_asymmetric = information(CONTROL_REVERSAL, ASYMMETRIC, ZERO_PRIOR)
    unmodulated_cal1 = information(
        UNMODULATED, UNIFORM, offset_calibration_precision(1.0)
    )
    unmodulated_cal9 = information(
        UNMODULATED, UNIFORM, offset_calibration_precision(9.0)
    )

    # Exact regression guards.  These encode the four reviewer-facing facts:
    # nuisance failure, response-diversity recovery, calibration recovery, and
    # resource-allocation sensitivity.
    assert abs(unmodulated_free - 0.0) < 1e-12
    assert abs(reversal_uniform - 1.0) < 1e-12
    assert abs(unmodulated_cal1 - 0.5) < 1e-12
    assert abs(unmodulated_cal9 - 0.9) < 1e-12
    assert abs(reversal_asymmetric - 0.84) < 1e-12
    assert reversal_asymmetric < reversal_uniform

    # The uniform control-reversal score is exactly orthogonal, under the
    # resource metric, to both clock nuisance directions.
    j = clock_nuisance_jacobian()
    weighted_cross = j.T @ (UNIFORM * CONTROL_REVERSAL)
    assert np.linalg.norm(weighted_cross) < 1e-12

    return {
        "schema": "rqir-paper-iii-second-sensor-benchmark-v1",
        "date": "2026-09-10",
        "architecture": "reduced interleaved atomic-clock/Ramsey frequency sensing",
        "claim_class": "cross-architecture design-principle regression; not apparatus forecast",
        "core_profiler": "analysis/protocol002_profiled_fisher.py::profiled_beta_information",
        "resource_law_adapter": "analysis/paper3_profiled_resource_law.py::profiled_resource_information",
        "settings": {
            "normalized_times": TIMES.tolist(),
            "nuisances": ["shared_LO_frequency_offset", "linear_LO_drift"],
            "uniform_allocation": UNIFORM.tolist(),
            "asymmetric_allocation": ASYMMETRIC.tolist(),
            "unmodulated_response": UNMODULATED.tolist(),
            "control_reversal_response": CONTROL_REVERSAL.tolist(),
        },
        "results": {
            "unmodulated_free_nuisance_information": unmodulated_free,
            "control_reversal_uniform_information": reversal_uniform,
            "control_reversal_asymmetric_information": reversal_asymmetric,
            "unmodulated_offset_calibration_lambda1_information": unmodulated_cal1,
            "unmodulated_offset_calibration_lambda9_information": unmodulated_cal9,
            "uniform_reversal_nuisance_cross_norm": float(np.linalg.norm(weighted_cross)),
        },
        "gates": {
            "independent_sensor_architecture": "PASS",
            "same_profiled_resource_law": "PASS",
            "nuisance_induced_failure_present": "PASS",
            "response_diversity_recovery_present": "PASS",
            "calibration_recovery_present": "PASS",
            "allocation_sensitivity_present": "PASS",
            "core_decision_rules_modified": False,
        },
    }


def canonical_json(data: dict[str, object]) -> str:
    return json.dumps(data, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check-result",
        action="store_true",
        help="fail unless the checked-in machine-readable result matches exactly",
    )
    args = parser.parse_args()

    data = benchmark_results()
    text = canonical_json(data)
    print(text, end="")

    if args.check_result:
        result_path = Path(__file__).resolve().parents[1] / "results" / "paper3_atomic_clock_second_sensor.json"
        if result_path.read_text(encoding="utf-8") != text:
            raise SystemExit(f"checked-in result is stale: {result_path}")
        print("checked-in atomic-clock second-sensor result: PASS")


if __name__ == "__main__":
    main()
