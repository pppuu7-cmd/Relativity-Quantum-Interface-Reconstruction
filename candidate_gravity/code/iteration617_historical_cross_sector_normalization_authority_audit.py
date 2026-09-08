#!/usr/bin/env python3
"""Iteration 617: historical cross-sector normalization authority audit.

Question: after Iter616 reduced the source->native map to one common scalar
N_native, does existing repository authority already determine that scalar?

This audit is intentionally value-blind: it never reads the six Iter615
coefficients or the numerical Iter582 coordinate.  It examines only previously
frozen convention/normalization authorities.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CG = ROOT / "candidate_gravity"

paths = {
    "iter149": CG / "C5_SOURCE_COMPLETED_PROTOCOL_ITERATION149.md",
    "iter151": CG / "C5_WARD_IDENTITY_ITERATION151.md",
    "iter218": CG / "MINIMAL_SCALAR_SOURCE_COMPLETION_ITERATION218.md",
    "iter338": CG / "code/iteration338_det_effective_action_prefactor_audit.py",
    "iter589": ROOT / "analysis/source_k1_k2_normalization_iteration589.py",
    "iter616": CG / "results/iteration616_native_binding_endpoint_amputation_and_normalization_audit.json",
}
texts = {k: p.read_text() for k, p in paths.items()}
failures = []

required = {
    "iter149": [
        "g_mn = eta_mn + kappa h_mn",
        "chi2R_A;BC = - G_R(p) Gamma3 G_R(q) G_R(r)",
    ],
    "iter151": [
        "without importing an incompatible amputated-vertex normalization",
    ],
    "iter218": [
        "g_{\mu\nu}=\eta_{\mu\nu}+\kappa h_{\mu\nu}",
        "Stripping the common gravitational coupling",
    ],
    "iter338": [
        '"common_determinant_effective_action_factor": "+i"',
        '"normalized_discontinuity_relation": "D_s Gamma_det = +i * D_s C_det"',
    ],
    "iter589": [
        "K1(h;p',p)",
        "no extra",
        "relative factor",
    ],
}
for key, toks in required.items():
    for tok in toks:
        if tok not in texts[key]:
            failures.append(f"{key}: missing frozen token {tok!r}")

r616 = json.loads(texts["iter616"])
if r616.get("remaining_binding_dimension") != 1:
    failures.append("Iter616 remaining binding dimension drift")
if r616.get("source_born_subtraction") != "NOT_PERFORMED":
    failures.append("premature Source/Born subtraction")

# Classification logic:
# - Iter338 fixes the connection-sector outer +i factor.
# - Iter147/149 fix a retarded response convention and the physical metric/source
#   convention, including g=eta+kappa h.
# - Iter218 explicitly strips the common gravitational coupling in the displayed
#   MSSC one-graviton vertex.
# - Iter589 fixes relative factors only inside the MSSC source sector.
# - Iter151 explicitly warns that its action-level source completion was chosen
#   without importing an incompatible amputated-vertex normalization.
# Therefore there is no previously frozen cross-sector equation that equates the
# scalar-endpoint-amputated MSSC response to the gravitational retarded/1PI
# Gamma3 convention with an absolute phase/coupling normalization.

classification = (
    "PASS_ITER617_HISTORICAL_NORMALIZATION_AUTHORITY_AUDIT__N_NATIVE_GENUINELY_UNFIXED"
    if not failures else
    "FAIL_ITER617_HISTORICAL_AUTHORITY_TOKEN_DRIFT"
)

result = {
    "iteration": 617,
    "date": "2026-09-08",
    "model_readiness_percent": 24,
    "classification": classification,
    "scientific_gate_pass": not failures,
    "failures": failures,
    "candidate_residual": False,
    "audit_question": "Does pre-Iter616 repository authority uniquely fix the one common cross-sector scalar N_native without using Candidate values?",
    "answer": "NO__HISTORICAL_AUTHORITY_DOES_NOT_FIX_N_NATIVE" if not failures else "UNRESOLVED_DUE_TO_AUDIT_DRIFT",
    "known_exact_factors": {
        "connection_effective_action_outer_factor": "+i (Iter338)",
        "retarded_response_gravitational_amputation_sign": "chi2R = - G_R Gamma3 G_R G_R (Iter147/149)",
        "source_internal_relative_factors": "fixed by one MSSC K[g] (Iter589)",
        "metric_tensor_direction": "same physical metric perturbation convention; Iter149/218 write g=eta+kappa h",
        "q2_bucket_identity_and_scalar_endpoint_amputation": "closed by Iter588/616",
    },
    "missing_exact_identity": "No frozen equation maps the scalar-endpoint-amputated MSSC response, whose displayed source vertex strips the common gravitational coupling, to the gravitational retarded/1PI Gamma3 convention with one absolute phase/coupling normalization.",
    "strong_negative_evidence": "Iter151 explicitly preferred an action-level source-completed Ward identity rather than importing an incompatible amputated-vertex normalization.",
    "remaining_binding_dimension": 1,
    "remaining_binding_parameter": "N_native",
    "N_native_status": "BLOCKED__NOT_DERIVABLE_FROM_EXISTING_REPOSITORY_AUTHORITY",
    "forbidden_inferences": [
        "N_native=+i merely because Iter338 has +i",
        "N_native=-i by combining unrelated amputations",
        "N_native=1 by silently setting kappa=1",
        "fit N_native to Iter615 or Iter582 values",
        "root-dependent or q2-dependent normalization",
    ],
    "source_born_subtraction": "NOT_PERFORMED",
    "comparator_quotient": "BLOCKED",
    "ANSATZ_003": "FORBIDDEN",
    "Fisher_resources": "FORBIDDEN",
    "next_gate": "do not alter Iter606/616 normalization post hoc; search for an independent pre-existing generating-functional/Legendre-transform authority that explicitly relates the MSSC probe normalization to the same retarded gravitational Gamma3 field coordinate. If absent, retain N_native as the exact minimal blocker and advance only independent non-biasing theory/comparator work.",
    "readiness_change": "0 percentage points",
}

print(json.dumps(result, indent=2, sort_keys=True))
if failures:
    raise SystemExit(2)
