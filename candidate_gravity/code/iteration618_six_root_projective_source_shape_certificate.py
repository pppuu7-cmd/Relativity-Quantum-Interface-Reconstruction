#!/usr/bin/env python3
"""Iteration 618: six-root projective source-shape certificate.

Iter617 proves that one common nonzero N_native is not fixed by historical
authority.  This diagnostic extracts only information invariant under

    c_r -> N_native * c_r

for the six Iter615 scalar-pole coefficients.  Roots remain separate: no roots
are summed by q2 bucket or any other grouping.

The projective anchor is chosen BEFORE looking at coefficient magnitudes: sort by
the already-authoritative Iter614 root coordinate s and use the smallest-s root.
This makes the representation deterministic and kinematic rather than
value-selected.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CG = ROOT / "candidate_gravity"
r615 = json.loads((CG / "results/iteration615_native_s_source_pole_coefficient_audit.json").read_text())
r617 = json.loads((CG / "results/iteration617_historical_cross_sector_normalization_authority_audit.json").read_text())

failures = []
if r615.get("classification") != "PASS_ITER615_FROZEN_NATIVE_S_INTERNAL_SCALAR_POLE_SOURCE_COEFFICIENT_AUDIT__NON_NORMALIZED_NON_RESIDUAL":
    failures.append("Iter615 authority drift")
if r617.get("classification") != "PASS_ITER617_HISTORICAL_NORMALIZATION_AUTHORITY_AUDIT__N_NATIVE_GENUINELY_UNFIXED":
    failures.append("Iter617 authority drift")
if r617.get("remaining_binding_dimension") != 1:
    failures.append("Iter617 one-scalar blocker drift")

rows = sorted(r615["root_rows"], key=lambda x: float(x["s"]))
if len(rows) != 6:
    failures.append(f"expected six root rows, got {len(rows)}")

for i in range(1, len(rows)):
    if not float(rows[i]["s"]) > float(rows[i-1]["s"]):
        failures.append("root s ordering is not strictly increasing")

coeff = [float(x["aggregate_normalized_internal_scalar_cut_coefficient"]) for x in rows]
if not all(math.isfinite(x) and x != 0.0 for x in coeff):
    failures.append("projective coordinate requires six finite nonzero coefficients")

anchor = coeff[0] if coeff else float("nan")
ratios = [x / anchor for x in coeff] if coeff and anchor != 0 else []

projective_rows = []
for row, c, ratio in zip(rows, coeff, ratios):
    projective_rows.append({
        "root_denominator": row["root_denominator"],
        "s": float(row["s"]),
        "source_coefficient": c,
        "ratio_to_smallest_s_anchor": float(ratio),
        "same_projective_phase_as_anchor": bool(ratio > 0),
    })

# Internal scale-invariance regression under several arbitrary nonzero complex
# multipliers.  Ratios must be unchanged; this is a representation check only.
scales = [2.5, -3.0, 1.0j, 2.0-1.5j]
max_ratio_error = 0.0
for z in scales:
    zc = [z * c for c in coeff]
    zr = [x / zc[0] for x in zc]
    for a, b in zip(ratios, zr):
        max_ratio_error = max(max_ratio_error, abs(complex(a) - complex(b)))
if max_ratio_error > 5e-15:
    failures.append(f"projective scale-invariance regression failed: {max_ratio_error}")

classification = (
    "PASS_ITER618_SIX_ROOT_PROJECTIVE_SOURCE_SHAPE_CERTIFICATE__N_NATIVE_INVARIANT_NON_RESIDUAL"
    if not failures else
    "FAIL_ITER618_PROJECTIVE_SOURCE_SHAPE_CERTIFICATE"
)

result = {
    "iteration": 618,
    "date": "2026-09-08",
    "model_readiness_percent": 24,
    "classification": classification,
    "scientific_gate_pass": not failures,
    "failures": failures,
    "candidate_residual": False,
    "scope": "SOURCE_SIDE_ONLY__NORMALIZATION_INVARIANT_DIAGNOSTIC",
    "root_order_rule": "strict ascending Iter614 s; never coefficient-magnitude ordered",
    "anchor_rule": "smallest-s root; fixed by kinematics before projective ratios",
    "anchor": {
        "root_denominator": rows[0]["root_denominator"] if rows else None,
        "s": float(rows[0]["s"]) if rows else None,
        "source_coefficient": anchor,
    },
    "projective_rows": projective_rows,
    "five_independent_ratios_after_anchor": [float(x) for x in ratios[1:]],
    "raw_source_sign_pattern_in_ascending_s_order": [1 if x > 0 else -1 for x in coeff],
    "relative_sign_pattern_to_anchor": [1 if x > 0 else -1 for x in ratios],
    "projective_scale_regression": {
        "tested_common_nonzero_scales": ["2.5", "-3", "+i", "2-1.5i"],
        "max_ratio_error": max_ratio_error,
    },
    "invariance_statement": "All reported ratios are unchanged under one common nonzero real or complex N_native multiplying all six source coefficients.",
    "future_fail_closed_use": "Any future claimed common-N_native bridge that changes these root-by-root ratios is an implementation/projection corruption and must be rejected before Source/Born subtraction or comparator quotient.",
    "explicit_nonclaims": [
        "does not determine N_native",
        "does not map any root to an Iter582 numerical value",
        "does not sum roots sharing a q2 bucket",
        "does not perform Source/Born subtraction",
        "does not create a Candidate residual",
    ],
    "source_born_subtraction": "NOT_PERFORMED",
    "comparator_quotient": "BLOCKED",
    "ANSATZ_003": "FORBIDDEN",
    "Fisher_resources": "FORBIDDEN",
    "next_gate": "derive additional normalization-invariant consistency checks that use the frozen root/Jacobian structure but do not aggregate distinct roots, or advance an independent comparator/theory gate; N_native itself remains BLOCKED",
    "readiness_change": "0 percentage points",
}

print(json.dumps(result, indent=2, sort_keys=True))
if failures:
    raise SystemExit(2)
