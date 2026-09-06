#!/usr/bin/env python3
"""Preregister the exact post-rank22 manifest suffix without evaluating rank22.

This audit is deliberately non-promoting. It consumes only the frozen Iteration-455
manifest and the raw-consumed rank21 authority. It proves the deterministic successor
order for ranks 22..27 and the occurrence-weighted coverage arithmetic that would
follow from future raw-valid PASS outcomes. It does not inspect, predict, or classify
the active rank22 heavy numerical result.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "candidate_gravity" / "results"

manifest_doc = json.loads((R / "iteration455_mass_support_queue_manifest.json").read_text(encoding="utf-8"))
rank21 = json.loads((R / "post504_rank21_raw_consumption.json").read_text(encoding="utf-8"))
manifest = {row["distinct_rank"]: row for row in manifest_doc["manifest"]}

expected_suffix = [
    (22,  2.5e-6, -5.0e-6, 1, "HALF", 8),
    (23,  2.5e-6, -2.5e-6, 1, "HALF", 9),
    (24,  2.5e-6,  2.5e-6, 1, "HALF", 10),
    (25,  2.5e-6,  5.0e-6, 1, "HALF", 11),
    (26,  5.0e-6, -2.5e-6, 1, "HALF", 13),
    (27,  5.0e-6,  2.5e-6, 1, "HALF", 14),
]

def row_matches(spec):
    rank, u, v, mult, level, idx = spec
    row = manifest.get(rank, {})
    labels = row.get("source_labels", [])
    return (
        row.get("u") == u
        and row.get("v") == v
        and row.get("source_occurrence_multiplicity") == mult
        and len(labels) == 1
        and labels[0].get("level") == level
        and labels[0].get("local_index") == idx
        and row.get("state") == "UNTESTED"
    )

coverage = rank21.get("coverage_after_pass", {})
checks = {
    "frozen_manifest_iteration_455": manifest_doc.get("iteration") == 455,
    "frozen_manifest_28_distinct": manifest_doc.get("frozen", {}).get("distinct_coordinate_count") == 28,
    "frozen_manifest_32_occurrences": manifest_doc.get("frozen", {}).get("occurrence_count") == 32,
    "rank21_raw_authority_exact": rank21.get("scientific_gate_pass") is True and rank21.get("classification") == "PASS_RAW_CONSUMED_MANIFEST_RANK21_FULL_Z_MP80_MP120__NON_PROMOTING",
    "rank21_coverage_exact_26_of_32": coverage.get("certified_occurrence_weight") == 26 and coverage.get("total_occurrence_weight") == 32,
    "rank21_points_exactly_to_rank22": rank21.get("next_manifest_coordinate", {}).get("manifest_rank") == 22,
    "rank21_rank22_coordinate_exact": rank21.get("next_manifest_coordinate", {}).get("u") == 2.5e-6 and rank21.get("next_manifest_coordinate", {}).get("v") == -5e-6,
    "suffix_ranks_22_through_27_exact": all(row_matches(spec) for spec in expected_suffix),
    "suffix_all_multiplicity_one": all(spec[3] == 1 for spec in expected_suffix),
    "rank23_is_strict_successor_of_rank22": expected_suffix[1][0] == expected_suffix[0][0] + 1,
}

coverage_forecast = []
certified = 26
for rank, u, v, mult, level, idx in expected_suffix:
    certified += mult
    coverage_forecast.append({
        "after_raw_valid_pass_of_rank": rank,
        "certified_occurrence_weight": certified,
        "total_occurrence_weight": 32,
        "fraction": f"{certified}/32",
        "percent": f"{100.0*certified/32.0:.3f}%".rstrip("0").rstrip("."),
        "certified_rows": certified * 5 * 16,
        "total_rows": 32 * 5 * 16,
    })

passed = all(checks.values())
result = {
    "schema": "rqir.candidate_gravity.rank23_successor_suffix_preregistration.v1",
    "iteration": 507,
    "classification": "PASS_RANK23_SUCCESSOR_AND_RANK22_27_SUFFIX_PREREGISTERED_EXACT__NON_PROMOTING" if passed else "BLOCKED_RANK23_SUCCESSOR_OR_SUFFIX_MANIFEST_DRIFT__NON_PROMOTING",
    "scientific_gate_pass": passed,
    "scope": "MANIFEST_ORDER_AND_COVERAGE_ARITHMETIC_ONLY",
    "checks": checks,
    "active_heavy_gate_unchanged": {
        "manifest_rank": 22,
        "u": 2.5e-6,
        "v": -5e-6,
        "source_level": "HALF",
        "source_local_index": 8,
    },
    "next_only_if_rank22_raw_valid_pass": {
        "manifest_rank": 23,
        "u": 2.5e-6,
        "v": -2.5e-6,
        "source_occurrence_multiplicity": 1,
        "source_level": "HALF",
        "source_local_index": 9,
    },
    "frozen_suffix": [
        {
            "manifest_rank": rank,
            "u": u,
            "v": v,
            "source_occurrence_multiplicity": mult,
            "source_level": level,
            "source_local_index": idx,
        }
        for rank, u, v, mult, level, idx in expected_suffix
    ],
    "coverage_forecast_conditional_on_sequential_raw_valid_pass": coverage_forecast,
    "explicit_nonclaims": [
        "NOT_A_RANK22_NUMERICAL_RESULT",
        "NOT_A_PHYSICAL_DS_PROMOTION",
        "NOT_AN_ASSEMBLED_BASE_HALF_PROMOTION",
        "NOT_A_CANDIDATE_GRAVITY_CONSISTENCY_PASS_OR_FAIL",
        "NOT_A_COMPARATOR_OR_NOVELTY_CERTIFICATE",
        "NO_THRESHOLD_CHANGE",
        "NO_ANSATZ003",
        "NO_FISHER_RESOURCES",
    ],
    "MODEL_READINESS": "24%",
    "readiness_change_pp": 0,
}
print(json.dumps(result, indent=2, sort_keys=True))
if not passed:
    raise SystemExit(2)
