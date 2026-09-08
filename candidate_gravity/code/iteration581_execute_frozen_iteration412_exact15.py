#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 581.

Execute the prospectively frozen Iteration-412 exact15 Tr(U1^2) assembly after
Iteration-580 closed the frozen Iteration-424 physical index-2 gate 5/5.

No estimator is selected here.  The physical-value rule is inherited from the
pre-existing Iteration-407/420 parent convention: D_s is the negative BASE-h
mixed derivative (the channel record stores D_s=-d_base).  Iteration-424 added
higher-precision BASE/HALF/QUARTER acceptance checks but explicitly did not
replace that promotion/value/normalization rule.  Therefore index 2 is taken
from the raw-consumed Iteration-574 BASE value only after CURRENT_QG_FRONT
records Iteration-580 5/5 PASS.

The other 14 values are consumed only from the Iteration-412 staged raw-
authority manifest.  Unsupported values are never zero-filled or inferred by
symmetry.  Distinct q^2 buckets are never summed and the -i/4 effective-action
weight is not folded at this stage.
"""
from __future__ import annotations

import json
import math
from decimal import Decimal
from pathlib import Path

ITERATION = 581
ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "contracts" / "iteration412_exact15_staged_authority_manifest_14of15.json"
ITER574 = ROOT / "results" / "iteration574_iter424_full_spectrum_raw_consumption.json"
FRONT = ROOT / "recovery" / "CURRENT_QG_FRONT.md"
REC580 = ROOT / "recovery" / "RECOVERY_DELTA_ITERATION_580.md"

EXPECTED_Q2 = {
    **{i: -1.0 for i in range(0, 5)},
    **{i: -0.14 for i in range(5, 10)},
    **{i: -0.34 for i in range(10, 15)},
}
QKEY = {-1.0: "-1.0", -0.34: "-0.34", -0.14: "-0.14"}
SIMPLE_SIMPLE = {
    "-1.0": 6.253219881951187e-05,
    "-0.34": 3.5044107116946374e-05,
    "-0.14": 2.9297648005638963e-05,
}
SIMPLE_DOUBLE = {
    "-1.0": -0.002329411286740447,
    "-0.34": -0.0005948791870822445,
    "-0.14": -7.368142632096214e-05,
}


def fail(msg, *data):
    raise RuntimeError((msg, *data))


def scaled_equal(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


manifest = json.loads(MANIFEST.read_text())
iter574 = json.loads(ITER574.read_text())
front = FRONT.read_text()
rec580 = REC580.read_text()

# Frozen prerequisite authority, fail closed.
if manifest.get("assembly_contract_iteration") != 412:
    fail("iteration412_manifest_identity_drift")
if manifest.get("scientific_gate_pass") is not True:
    fail("iteration412_manifest_not_scientific_pass")
if manifest.get("missing_indices") != [2] or manifest.get("record_count") != 14:
    fail("iteration412_manifest_not_exact_14of15", manifest.get("missing_indices"), manifest.get("record_count"))
if iter574.get("scientific_gate_pass") is not True:
    fail("iteration574_raw_consumption_not_pass")
if iter574.get("target") != {"double_double_index": 2, "class_id": 3, "q_squared": -1.0}:
    fail("iteration574_target_drift", iter574.get("target"))
if iter574.get("workflow_authority", {}).get("authority_audit_raw_result_integrity_valid") is not True:
    fail("iteration574_raw_integrity_not_valid")
required_front = [
    "Latest authoritative research iteration: **580**",
    "Post-Iteration580 unresolved physical set: **`[]`**",
    "Iter424 frozen high-precision decision: **5/5 PASS**",
    "PASS_ITER421_TENSOR11_MP80_MP120__ITER424_5_OF_5_PASS__PHYSICAL_INDEX2_NUMERICAL_BLOCKER_CLOSED",
]
if any(x not in front for x in required_front):
    fail("iteration580_front_authority_missing", [x for x in required_front if x not in front])
if "MP80 tensor11 residual `1.341057348963658e-8` — PASS" not in rec580 or "MP120 tensor11 residual `1.341057348963658e-8` — PASS" not in rec580:
    fail("iteration580_recovery_tensor11_authority_missing")

# Pre-existing promotion/value rule: BASE is the stored channel D_s authority.
base80 = Decimal(iter574["physical_Ds"]["BASE"]["MP80"])
base120 = Decimal(iter574["physical_Ds"]["BASE"]["MP120"])
if base80 != base120:
    fail("base_cross_precision_drift", str(base80), str(base120))
index2_ds = float(base120)
if not math.isfinite(index2_ds):
    fail("nonfinite_promoted_index2")

# Consume the 14 raw-authority-staged records exactly once.
by_index = {}
provenance = []
for rec in manifest.get("records", []):
    idx = rec.get("index")
    if not isinstance(idx, int) or idx not in EXPECTED_Q2 or idx == 2:
        fail("invalid_staged_index", idx)
    if idx in by_index:
        fail("duplicate_staged_index", idx)
    if rec.get("status") != "CONVERGED":
        fail("nonconverged_staged_record", idx, rec.get("status"))
    q2 = float(rec.get("q_squared"))
    if not scaled_equal(q2, EXPECTED_Q2[idx]):
        fail("staged_q2_drift", idx, q2, EXPECTED_Q2[idx])
    coord = rec.get("D_s_TrU1sq_double_double_channel")
    if not (isinstance(coord, list) and len(coord) == 2):
        fail("staged_coordinate_missing", idx)
    value = complex(float(coord[0]), float(coord[1]))
    if not (math.isfinite(value.real) and math.isfinite(value.imag)):
        fail("staged_coordinate_nonfinite", idx)
    by_index[idx] = value
    provenance.append({
        "index": idx,
        "q_squared": q2,
        "source_iteration": rec.get("source_iteration"),
        "raw_result_sha256": rec.get("raw_result_sha256"),
        "authority_audit_sha256": rec.get("authority_audit_sha256"),
        "authority": "ITERATION412_STAGED_RAW_AUTHORITY_MANIFEST",
    })

# Append exactly one newly promoted physical index-2 record. No zero fill.
if set(by_index) != set(range(15)) - {2}:
    fail("staged_index_set_drift", sorted(by_index))
by_index[2] = complex(index2_ds, 0.0)
provenance.append({
    "index": 2,
    "q_squared": -1.0,
    "source_iterations": [574, 580],
    "source_workflow_run": iter574["workflow_authority"]["run_id"],
    "source_artifact_id": iter574["workflow_authority"]["artifact_id"],
    "source_result_json_sha256": iter574["workflow_authority"]["result_json_sha256"],
    "source_authority_audit_sha256": iter574["workflow_authority"]["authority_audit_json_sha256"],
    "value_rule": "PRE_EXISTING_ITER407_PARENT_RULE__D_s_EQUALS_NEGATIVE_BASE_H_MIXED_DERIVATIVE__ITER424_NO_NEW_ESTIMATOR",
    "D_s_decimal": str(base120),
    "authority": "ITER574_RAW_CONSUMPTION_PLUS_ITER580_FROZEN_5_OF_5_PROMOTION",
})

if set(by_index) != set(range(15)):
    fail("exact15_not_closed", sorted(by_index))

dd = {"-1.0": 0j, "-0.34": 0j, "-0.14": 0j}
counts = {k: 0 for k in dd}
for idx in range(15):
    key = QKEY[EXPECTED_Q2[idx]]
    dd[key] += by_index[idx]
    counts[key] += 1
if counts != {"-1.0": 5, "-0.34": 5, "-0.14": 5}:
    fail("q2_count_drift", counts)

complete = {}
for key in ("-1.0", "-0.34", "-0.14"):
    val = complex(SIMPLE_SIMPLE[key], 0.0) + complex(SIMPLE_DOUBLE[key], 0.0) + dd[key]
    complete[key] = [float(val.real), float(val.imag)]

result = {
    "iteration": ITERATION,
    "date": "2026-09-08",
    "classification": "PASS_EXECUTED_FROZEN_ITER412_TRU1SQ_EXACT15__PHYSICAL_INDEX2_FROM_ITER580_PROMOTION",
    "status": "PASS_EXACT15_ASSEMBLY_PENDING_INDEPENDENT_RAW_ARTIFACT_CONSUMPTION",
    "scientific_gate_pass": True,
    "candidate_residual": False,
    "model_readiness_percent": 24,
    "frozen_contract_iteration": 412,
    "physical_promotion_decision_iteration": 580,
    "exact_double_double_channel_count": 15,
    "double_double_q2_counts": counts,
    "D_s_TrU1sq_double_double_q2": {k: [float(v.real), float(v.imag)] for k, v in dd.items()},
    "components": {
        "simple_simple_iteration": 374,
        "simple_simple_q2": SIMPLE_SIMPLE,
        "simple_double_iteration": 393,
        "simple_double_q2": SIMPLE_DOUBLE,
        "double_double_records": sorted(provenance, key=lambda x: x["index"]),
    },
    "D_s_TrU1sq_complete_q2": complete,
    "effective_action_weight": "NOT_FOLDED__MINUS_I_OVER_4_TRU1SQ_SEPARATE",
    "guardrails": [
        "ITERATION412_EXACT15_CONTRACT_BINDING",
        "EXACT_15_UNIQUE_DOUBLE_DOUBLE_INDICES_REQUIRED",
        "INDEX2_VALUE_RULE_INHERITED_FROM_ITER407_BASE_H_PROMOTION_CONVENTION",
        "ITER580_5_OF_5_REQUIRED_BEFORE_INDEX2_APPEND",
        "NO_POSTHOC_ESTIMATOR_SELECTION",
        "NO_BLOCKED_DIAGNOSTIC_VALUE",
        "NO_ZERO_FILL",
        "DISTINCT_Q2_BUCKETS_NEVER_SUMMED",
        "NO_EFFECTIVE_ACTION_WEIGHT_FOLDING",
        "NO_ANSATZ003",
        "NO_FISHER_RESOURCES",
    ],
    "next_gate": "independently raw-consume this artifact; if exact15 raw-valid, combine q2-by-q2 with authoritative Iteration406 TrU2 using +(i/2)TrU2-(i/4)TrU1sq, then proceed to D_s Gamma_e2 and concrete Source/Ward/contact+K2 before any fixed comparator quotient",
}
print(json.dumps(result, indent=2, sort_keys=True))
