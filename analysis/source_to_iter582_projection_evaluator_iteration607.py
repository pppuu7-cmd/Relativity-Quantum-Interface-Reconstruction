#!/usr/bin/env python3
"""Iteration 607: fail-closed source->Iter582/native-linked projection evaluator.

This evaluator consumes the frozen Iter606 contract. It is allowed to emit BLOCKED
when the repository does not contain the distributional scalar-pole projector needed
to map the source tree into native linked Y/T_cut. Missing authority is never zero-filled.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract_path = ROOT / "candidate_gravity/results/iteration606_source_to_iter582_mapping_contract_raw_consumption.json"
iter592_path = ROOT / "candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_592.md"
iter605_path = ROOT / "candidate_gravity/results/iteration605_full_source_nonlinear_ward_raw_consumption.json"
out = ROOT / "results/iteration607_source_to_iter582_projection"
out.mkdir(parents=True, exist_ok=True)

C = json.loads(contract_path.read_text())
W = json.loads(iter605_path.read_text())
R592 = iter592_path.read_text()
pre_fail = []
if C.get("classification") != "PASS_PROSPECTIVE_SOURCE_TO_ITER582_NATIVE_LINKED_MAPPING_CONTRACT__NON_RESIDUAL":
    pre_fail.append("Iter606 mapping contract authority missing")
if W.get("ward_rows_pass") != 12 or W.get("source_family_count") != 13:
    pre_fail.append("Iter605 source/Ward authority drift")
if "BLOCKED__NEEDS_EXPLICIT_SOURCE_TO_T_CUT_DISTRIBUTIONAL_MAP" not in R592:
    pre_fail.append("Iter592 distributional blocker provenance missing")

# The required projector must be an explicit, separately authoritative object.  A prose
# mention or the prospective Iter606 contract is not enough and cannot be promoted.
projector_candidates = [
    ROOT / "candidate_gravity/results/source_to_native_linked_distributional_projection_authority.json",
    ROOT / "candidate_gravity/results/mssc_scalar_pole_to_tcut_projection_authority.json",
]
projector = next((p for p in projector_candidates if p.exists()), None)
missing = []
if projector is None:
    missing = [
        "explicit scalar-pole distribution -> native Y/T_cut projector",
        "kinematic pullback relating each internal MSSC scalar pole momentum to the native linked cut variable",
        "normalization/sign prescription tying the distributional pole term to the already-frozen Iter582 coordinate without Born subtraction",
    ]

if pre_fail:
    classification = "BLOCKED_ITER607_PREREQUISITE_AUTHORITY_DRIFT"
elif missing:
    classification = "BLOCKED_ITER607_EXPLICIT_DISTRIBUTIONAL_SOURCE_TO_NATIVE_LINKED_PROJECTOR_ABSENT"
else:
    classification = "PASS_ITER607_EXPLICIT_DISTRIBUTIONAL_PROJECTOR_PRESENT__READY_FOR_NUMERICAL_PROJECTION"

result_obj = {
    "iteration": 607,
    "date": "2026-09-08",
    "classification": classification,
    "scientific_gate_pass": classification.startswith("PASS_"),
    "blocked_is_scientific_result": classification.startswith("BLOCKED_"),
    "candidate_residual": False,
    "model_readiness_percent": 24,
    "iter606_contract_consumed": True,
    "iter605_full_ward_consumed": True,
    "source_family_count": 13,
    "q2_buckets": [-1.0, -0.34, -0.14],
    "source_born_subtraction": "NOT_PERFORMED",
    "zero_fill": False,
    "projector_authority_path": str(projector.relative_to(ROOT)) if projector else None,
    "missing_authority": missing,
    "prerequisite_failures": pre_fail,
    "interpretation": "A scalar propagator pole has a distributional discontinuity, but Iter592 establishes that repository authority does not identify its pullback into native split-invariant Y/T_cut. Iter606 forbids assuming that pullback or deleting K1^3. Therefore absence of an explicit projector is BLOCKED, not zero.",
    "next_gate": "Derive and prospectively freeze the scalar-pole distributional projector from the same MSSC parent kinematics/native observable definition; then rerun the matched projection. No Source/Born subtraction or comparator quotient before that authority exists." if missing else "Execute the matched numerical/symbolic source-to-Iter582 projection using the explicit projector, preserving q2 buckets and all 13 source families.",
    "ANSATZ_003": "FORBIDDEN",
    "Fisher_resources": "FORBIDDEN",
}
result = out / "result.json"
result.write_text(json.dumps(result_obj, indent=2, sort_keys=True) + "\n")
sha = hashlib.sha256(result.read_bytes()).hexdigest()
audit_fail = list(pre_fail)
audit = {
    "classification": "PASS_RAW_AUDIT_ITER607_FAIL_CLOSED_PROJECTION_EVALUATOR" if not audit_fail else "FAIL_RAW_AUDIT_ITER607_PROJECTION_EVALUATOR",
    "result_sha256": sha,
    "failures": audit_fail,
}
(out / "authority_audit.json").write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
print(classification, sha)
# BLOCKED is a valid scientific outcome and must still upload. Only provenance drift fails CI.
if pre_fail:
    raise SystemExit("\n".join(pre_fail))
