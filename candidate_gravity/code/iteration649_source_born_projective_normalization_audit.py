#!/usr/bin/env python3
"""Iteration 649: Source/Born vs projective closed-Gamma3 normalization-class audit.

This is a prerequisite audit only. It does NOT perform Source/Born subtraction.
The Iter648 projective observable removes one common nonzero factor from a closed
Gamma3 cut vector A. For a matched subtraction R=A-B, projectivization is lawful
without absolute normalization only when A and B share the same single factor:
A=lambda*A0 and B=lambda*B0. If B carries an independent factor mu, then
[A-B] depends on mu/lambda and cannot be inferred from projective data.

Existing authority also rejects identifying the historical open scalar response
with the closed gravitational 1PI object by one scalar normalization (Iter629).
Therefore, until a same-parent matched Source/Born term B is explicitly defined
inside the closed Gamma3 observable and shown to inherit the same lambda, the
subtraction remains provenance-BLOCKED. Unsupported is never zero-filled.
"""
from __future__ import annotations
import json
from pathlib import Path

ITERATION = 649
ROOT = Path(__file__).resolve().parents[2]

p629 = ROOT / "candidate_gravity" / "results" / "iteration629_open_vs_1pi_normalization_gate.json"
p648 = ROOT / "candidate_gravity" / "results" / "iteration648_projective_closed_gamma3_shape_summary.json"

d629 = json.loads(p629.read_text())
d648 = json.loads(p648.read_text())
failures = []

if d629.get("iteration") != 629:
    failures.append("Iter629 authority missing or drifted")
if d629.get("single_common_N_native_exists") is not False:
    failures.append("Iter629 no longer rejects a single open-response-to-closed-1PI normalization")
if d629.get("source_born_subtraction") != "NOT_PERFORMED":
    failures.append("Iter629 source/Born status drift")
if d648.get("iteration") != 648 or d648.get("scientific_gate_pass") is not True:
    failures.append("Iter648 projective authority missing or not PASS")
if d648.get("source_born_subtraction") != "NOT_PERFORMED":
    failures.append("Iter648 source/Born status drift")
if d648.get("absolute_normalization_status") != "PERMANENTLY_BLOCKED_FOR_ABSOLUTE_ITER645_BRANCH__NOT_NEEDED_FOR_THIS_PROJECTIVE_GATE":
    failures.append("Iter648 absolute-normalization authority drift")

# Pure algebraic prerequisite. For R=A-B with A=lambda A0 and B=mu B0,
# lambda^{-1} R = A0 - (mu/lambda) B0. The projective class [R] therefore
# depends on rho=mu/lambda unless rho is fixed by same-parent authority (or B0=0,
# which is forbidden to assume/zero-fill). Existing authority supplies no such
# matched B definition, and Iter629 explicitly rejects using the open response
# as a one-factor proxy for the closed 1PI object.
algebra = {
    "candidate": "A=lambda*A0",
    "subtraction_general": "B=mu*B0",
    "matched_residual": "R=A-B=lambda*(A0-(mu/lambda)*B0)",
    "projective_commutation_condition": "mu/lambda must be fixed by same-parent authority; the sufficient one-common-factor case is mu=lambda",
    "independent_factor_consequence": "[R] depends on rho=mu/lambda and cannot be recovered from [A] alone",
    "zero_B_assumption": "FORBIDDEN_UNSUPPORTED_NOT_ZERO_FILLED",
}

same_common_factor_established = False
matched_source_born_object_established = False
open_response_usable_as_closed_born_proxy = False

if failures:
    classification = "BLOCKED_ITER649_AUTHORITY_INPUT_DRIFT__SOURCE_BORN_SUBTRACTION_NOT_PERFORMED__NON_RESIDUAL"
    scientific_gate_pass = False
else:
    classification = "BLOCKED_ITER649_MATCHED_SOURCE_BORN_ONE_COMMON_FACTOR_CLASS_NOT_ESTABLISHED__OPEN_RESPONSE_PROXY_REJECTED_BY_ITER629__NON_RESIDUAL"
    scientific_gate_pass = True

result = {
    "iteration": ITERATION,
    "date": "2026-09-09",
    "MODEL_READINESS": "24%",
    "readiness_change": "0 percentage points",
    "classification": classification,
    "scientific_gate_pass": scientific_gate_pass,
    "candidate_residual": False,
    "authority_inputs": {
        "iteration629": str(p629.relative_to(ROOT)),
        "iteration648": str(p648.relative_to(ROOT)),
        "iter629_open_over_closed_family_ratios": d629.get("family_total_coefficient_vectors", {}).get("open_over_closed"),
        "iter629_single_common_N_native_exists": d629.get("single_common_N_native_exists"),
        "iter648_projective_observable": d648.get("observable", {}).get("projector"),
    },
    "algebra": algebra,
    "matched_source_born_object_established": matched_source_born_object_established,
    "same_common_factor_established": same_common_factor_established,
    "open_response_usable_as_closed_born_proxy": open_response_usable_as_closed_born_proxy,
    "source_born_subtraction": "NOT_PERFORMED",
    "native_Y_Tcut_projection": "NOT_PERFORMED",
    "comparator_quotient": "NOT_PERFORMED",
    "candidate_values_used": False,
    "normalization_fit": False,
    "zero_fill": False,
    "ANSATZ_003": "FORBIDDEN",
    "Fisher_resources": "FORBIDDEN",
    "failures": failures,
    "next_gate": "Iteration650: derive or locate an explicit same-parent Source/Born contribution in the closed retarded gravitational Gamma3 matched observable, with its CTP/Legendre normalization and pole/cut origin fixed before subtraction. If no such committed definition exists, record that prerequisite as the terminal operational blocker; do not use the Iter629 open response as a proxy and do not set the missing term to zero.",
}

out = ROOT / "results" / "iteration649_source_born_projective_normalization_audit"
out.mkdir(parents=True, exist_ok=True)
(out / "result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, indent=2, sort_keys=True))
if failures:
    raise SystemExit(2)
