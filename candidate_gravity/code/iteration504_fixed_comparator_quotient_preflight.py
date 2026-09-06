#!/usr/bin/env python3
"""Fail-closed preflight for the fixed Candidate-Gravity comparator quotient.

This audit does not evaluate any comparator physics. It checks whether the repository-
authoritative upstream target required to *start* the fixed C3/C4/C5/nonlocal/
asymptotic-safety quotient exists. Absence is BLOCKED, never identity/FAIL/novelty.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FRONT = ROOT / "candidate_gravity" / "recovery" / "CURRENT_QG_FRONT.md"

text = FRONT.read_text(encoding="utf-8")
checks = {
    "physical_unresolved_set_is_2": "Exact unresolved physical set: **`[2]`**" in text,
    "source_ward_stage_is_downstream": "Source/Ward/contact+K2" in text,
    "fixed_comparator_quotient_is_downstream": "fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient" in text,
    "robust_residual_is_downstream": "robust nonzero residual" in text,
    "ansatz003_forbidden": "`ANSATZ-003` remains uncreated" in text,
    "fisher_resources_forbidden": "Fisher/resources remain forbidden" in text,
}

# Fail closed: the current front explicitly says the physical/operator chain has not
# reached Source/Ward/contact+K2 and the robust residual is absent. Therefore there
# is no concrete assembled target on which the fixed comparator quotient can act.
upstream_target_assembled = False
classification = (
    "READY_FOR_FIXED_COMPARATOR_QUOTIENT"
    if upstream_target_assembled and all(checks.values())
    else "BLOCKED_FIXED_COMPARATOR_QUOTIENT_UPSTREAM_TARGET_NOT_ASSEMBLED__NON_PROMOTING"
)

result = {
    "schema": "rqir.candidate_gravity.comparator_preflight.v1",
    "authoritative_front": str(FRONT.relative_to(ROOT)),
    "checks": checks,
    "upstream_target_assembled": upstream_target_assembled,
    "classification": classification,
    "scientific_semantics": {
        "consistency_fail": False,
        "exact_comparator_identity": False,
        "regime_specific_non_identifiability": False,
        "near_degeneracy": False,
        "novelty_certificate_available": False,
        "operational_blocked": True,
    },
    "guardrails": {
        "ansatz003_allowed": False,
        "fisher_allowed": False,
        "resources_allowed": False,
        "frozen_gates_changed": False,
    },
}

if not all(checks.values()):
    result["audit_error"] = "authoritative-front contract markers missing; treat as provenance BLOCKED"

print(json.dumps(result, indent=2, sort_keys=True))
