#!/usr/bin/env python3
"""Iteration 622: common field-variable / kappa-stripping audit.

Purpose: determine whether the one remaining Iter621 cross-sector normalization
DOF can contain an unfixed power of kappa, or whether both computational sectors
already use the same direct metric perturbation delta g as their expansion
variable.

This audit is value-independent and does not use Iter582 or Iter615 numerical
Candidate values.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]

conn = (ROOT / "candidate_gravity/code/iteration270_vd_physical_b3_nonzero.py").read_text()
src = (ROOT / "analysis/source_cubic_response_completeness_iteration590.py").read_text()
model = (ROOT / "candidate_gravity/models/ANSATZ-PQG-EFT-001/MODEL.md").read_text()
proto = (ROOT / "candidate_gravity/C5_SOURCE_COMPLETED_PROTOCOL_ITERATION149.md").read_text()
front = (ROOT / "candidate_gravity/recovery/CURRENT_QG_FRONT.md").read_text()

failures = []

# Physical field convention: delta g = kappa h.
for token, text, name in [
    ("g_mn = eta_mn + kappa h_mn", model, "reference model"),
    ("g_mn = eta_mn + kappa h_mn", proto, "source-completed protocol"),
]:
    if token not in text:
        failures.append(f"missing physical split in {name}")

# Connection numerical geometry differentiates by amplitudes added directly to g.
if "g=ETA.astype(complex).copy()" not in conn or "g+=a*e" not in conn:
    failures.append("Iter270 connection branch is not bound to direct delta-g amplitudes")

# MSSC source numerical geometry likewise differentiates by amplitudes added directly to g.
if "g=ETA.copy()" not in src or "g += float(e)*h" not in src:
    failures.append("Iter590 source branch is not bound to direct delta-g amplitudes")

# Bind the current one-DOF authority rather than inventing a new normalization.
if "remaining relative complex degree of freedom" not in front and "remaining relative complex normalization" not in front:
    failures.append("Iter621 one-relative-scale front authority missing")

passed = not failures
result = {
    "iteration": 622,
    "date": "2026-09-08",
    "scientific_gate_pass": passed,
    "candidate_residual": False,
    "classification": (
        "PASS_ITER622_COMMON_DIRECT_DELTA_G_VARIABLE_AND_COMMON_KAPPA_STRIPPING__N_NATIVE_DIMENSIONLESS_CONVENTION_BRIDGE_REMAINS_BLOCKED_NON_RESIDUAL"
        if passed else
        "BLOCKED_ITER622_FIELD_VARIABLE_AUTHORITY_DRIFT"
    ),
    "physical_split": "g = eta + kappa h_phys, hence delta_g = kappa h_phys",
    "connection_computational_variable": "direct additive delta_g amplitude in Iter270 geometry",
    "source_computational_variable": "direct additive delta_g amplitude in Iter590 MSSC geometry",
    "derived_consequence": (
        "stored source and connection coefficients are both expressed after stripping the same explicit kappa power associated with converting h_phys to delta_g; the remaining N_native cannot be an independently unknown gravitational-coupling power"
    ),
    "remaining_normalization": (
        "one common dimensionless nonzero complex convention/observable bridge between scalar-endpoint-amputated MSSC response and native gravitational Gamma3/effective-action convention"
    ),
    "forbidden_inference": [
        "does not set N_native=1",
        "does not set N_native=+i or -i",
        "does not infer a factorial or retarded/1PI phase",
        "does not use Candidate/comparator values",
        "does not authorize native projection or Source/Born subtraction",
    ],
    "failures": failures,
    "MODEL_READINESS": "24%",
    "next_gate": (
        "derive the missing dimensionless source-to-Gamma3 generating-functional/Legendre/in-in normalization prospectively; if no universal identity exists for the chosen physical MSSC observable, freeze the exact measurement-level bridge that must be supplied by a future Candidate rather than choosing a convention post hoc"
    ),
}
print(json.dumps(result, indent=2, sort_keys=True))
if failures:
    raise SystemExit(2)
