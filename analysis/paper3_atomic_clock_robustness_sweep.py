"""Paper III QST hardening: robustness sweep for the atomic-clock transfer benchmark.

This is a reviewer-facing anti-cherry-picking regression. It reuses the same
Paper III Eq. (1) adapter and frozen RQIR nuisance profiler as the reduced
atomic-clock benchmark, but evaluates continuous one-parameter families of
calibration strength and resource allocation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from paper3_atomic_clock_second_sensor_benchmark import (
    ASYMMETRIC,
    CONTROL_REVERSAL,
    UNIFORM,
    UNMODULATED,
    information,
    offset_calibration_precision,
)

CALIBRATION_STRENGTHS = np.array([0.0, 0.1, 0.3, 1.0, 3.0, 9.0, 30.0])
ALLOCATION_MIX = np.linspace(0.0, 1.0, 6)
ZERO_PRIOR = np.zeros((2, 2), dtype=float)


def stable_float(value: float) -> float:
    """Canonicalize diagnostic output while preserving stricter raw assertions."""
    return float(f"{float(value):.12g}")


def robustness_results() -> dict[str, object]:
    calibration = []
    for lam in CALIBRATION_STRENGTHS:
        measured = information(
            UNMODULATED, UNIFORM, offset_calibration_precision(float(lam))
        )
        expected = float(lam / (1.0 + lam))
        assert abs(measured - expected) < 1e-12
        calibration.append(
            {
                "lambda": stable_float(lam),
                "information": stable_float(measured),
                "analytic": stable_float(expected),
            }
        )

    calibration_values = np.array([x["information"] for x in calibration])
    assert np.all(np.diff(calibration_values) > 0.0)
    assert calibration_values[0] == 0.0
    assert calibration_values[-1] > 0.96

    allocation = []
    raw_allocation_values = []
    for alpha in ALLOCATION_MIX:
        e = (1.0 - alpha) * UNIFORM + alpha * ASYMMETRIC
        value = information(CONTROL_REVERSAL, e, ZERO_PRIOR)
        raw_allocation_values.append(value)
        allocation.append(
            {
                "alpha": stable_float(alpha),
                "allocation": [stable_float(x) for x in e],
                "information": stable_float(value),
            }
        )

    raw_allocation_values = np.array(raw_allocation_values)
    assert abs(raw_allocation_values[0] - 1.0) < 1e-12
    assert abs(raw_allocation_values[-1] - 0.84) < 1e-12
    assert np.all(np.diff(raw_allocation_values) < 0.0)

    return {
        "schema": "rqir-paper-iii-atomic-clock-robustness-v1",
        "date": "2026-09-10",
        "purpose": "anti-cherry-picking robustness check for cross-architecture transfer",
        "calibration_sweep": calibration,
        "allocation_sweep": allocation,
        "gates": {
            "calibration_curve_matches_analytic_law": "PASS",
            "calibration_recovery_is_monotonic": "PASS",
            "allocation_degradation_is_monotonic_on_test_path": "PASS",
            "same_frozen_profiler_reused": "PASS",
            "core_decision_rules_modified": False,
        },
    }


def canonical_json(data: dict[str, object]) -> str:
    return json.dumps(data, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-result", action="store_true")
    args = parser.parse_args()

    text = canonical_json(robustness_results())
    print(text, end="")

    if args.check_result:
        path = Path(__file__).resolve().parents[1] / "results" / "paper3_atomic_clock_robustness_sweep.json"
        if path.read_text(encoding="utf-8") != text:
            raise SystemExit(f"checked-in robustness result is stale: {path}")
        print("checked-in atomic-clock robustness result: PASS")


if __name__ == "__main__":
    main()
