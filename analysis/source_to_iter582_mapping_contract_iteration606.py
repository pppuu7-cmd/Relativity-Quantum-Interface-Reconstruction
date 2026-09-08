#!/usr/bin/env python3
"""Iteration 606: prospectively freeze the source-to-Iter582/native-linked mapping contract.

Contract-only gate. It does not perform Source/Born subtraction, does not create a
Candidate-Gravity residual, and does not infer unsupported scalar-pole projection.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ward_path = ROOT / "candidate_gravity/results/iteration605_full_source_nonlinear_ward_raw_consumption.json"
iter582_recovery = ROOT / "candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_582.md"
iter592_recovery = ROOT / "candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_592.md"
out = ROOT / "results/iteration606_source_to_iter582_mapping_contract"
out.mkdir(parents=True, exist_ok=True)

ward = json.loads(ward_path.read_text())
r582 = iter582_recovery.read_text()
r592 = iter592_recovery.read_text()
failures = []
if ward.get("classification") != "PASS_FULL_SOURCE_LEVEL_NONLINEAR_WARD_UNDER_ITER604_FINITE_LATTICE_CONTRACT__NON_RESIDUAL":
    failures.append("Iter605 Ward authority not PASS")
if ward.get("ward_rows_pass") != 12 or ward.get("ward_rows_total") != 12:
    failures.append("Iter605 Ward rows incomplete")
if ward.get("source_family_count") != 13:
    failures.append("13-family source census drift")
if ward.get("source_born_subtraction") != "NOT_PERFORMED":
    failures.append("premature Source/Born subtraction")
for token in ("q^2=-1.0", "q^2=-0.34", "q^2=-0.14", "PASS_GAMMA_E2_Q2_RESOLVED_FROZEN_WEIGHT_ASSEMBLY__NON_RESIDUAL"):
    if token not in r582:
        failures.append(f"Iter582 authority missing token: {token}")
for token in ("distributional", "K1cubed_under_frozen_linked_T_cut", "Source/Born subtraction remains NOT_PERFORMED"):
    if token not in r592:
        failures.append(f"Iter592 blocker missing token: {token}")

contract = {
    "iteration": 606,
    "date": "2026-09-08",
    "classification": "PASS_PROSPECTIVE_SOURCE_TO_ITER582_NATIVE_LINKED_MAPPING_CONTRACT__NON_RESIDUAL" if not failures else "BLOCKED_MAPPING_CONTRACT_PREREQUISITE_DRIFT",
    "scientific_gate_pass": not failures,
    "candidate_residual": False,
    "model_readiness_percent": 24,
    "frozen_prerequisites": {
        "iter605_full_source_level_ward": True,
        "source_family_count": 13,
        "iter582_q2_buckets": [-1.0, -0.34, -0.14],
        "iter582_coordinate": "D_s Gamma_e2 = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2",
        "native_linked_observable": "Y=(K2,S_soft2_full) / T_cut",
    },
    "projection_rules_frozen_before_result": [
        "keep q2 buckets distinct",
        "retain all 13 same-parent MSSC source families through projection",
        "classify ordinary finite branch cut, scalar-pole distribution, and local/contact origin separately",
        "unsupported scalar-pole-to-native-linked projection is BLOCKED, never zero-filled",
        "no K1^3 deletion merely because it is meromorphic away from scalar poles",
        "no Source/Born subtraction before the matched native observable is explicitly constructed",
        "no new normalization, estimator, threshold, q2 regrouping, or internal repartition",
        "preserve Iter582 frozen operator weights exactly",
    ],
    "source_born_subtraction": "NOT_PERFORMED",
    "comparator_quotient": "BLOCKED_UNTIL_MAPPING_EVALUATOR_RAW_VALID",
    "ANSATZ_003": "FORBIDDEN",
    "Fisher_resources": "FORBIDDEN",
    "next_gate": "Implement and raw-validate the full-observable source-to-Iter582/native-linked projection under this frozen contract; unresolved distributional terms must return BLOCKED rather than zero.",
    "failures": failures,
}
result = out / "result.json"
result.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n")
sha = hashlib.sha256(result.read_bytes()).hexdigest()
audit = {
    "classification": "PASS_RAW_AUDIT_ITER606_MAPPING_CONTRACT" if not failures else "FAIL_RAW_AUDIT_ITER606_MAPPING_CONTRACT",
    "result_sha256": sha,
    "failures": failures,
}
(out / "authority_audit.json").write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
print(contract["classification"], sha)
if failures:
    raise SystemExit("\n".join(failures))
