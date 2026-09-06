#!/usr/bin/env python3
"""Exact source/provenance audit for frozen manifest rank22 before raw consumption.

This audit does not evaluate the heavy numerical result. It verifies that the rank22
stage is chained to the raw-valid rank21 authority and retains the same frozen parent
sampling/dynamics and parameter convention. Any drift is provenance BLOCKED, never a
Candidate-Gravity consistency FAIL.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "candidate_gravity" / "results"
C = ROOT / "candidate_gravity" / "code"

auth = json.loads((R / "post504_rank21_raw_consumption.json").read_text(encoding="utf-8"))
stage = (C / "post505_manifest_rank22_full_z_mp_stage.py").read_text(encoding="utf-8")

checks = {
    "rank21_raw_pass_required": auth.get("scientific_gate_pass") is True and auth.get("classification") == "PASS_RAW_CONSUMED_MANIFEST_RANK21_FULL_Z_MP80_MP120__NON_PROMOTING",
    "rank21_successor_is_rank22": auth.get("next_manifest_coordinate", {}).get("manifest_rank") == 22,
    "rank22_coordinate_exact": auth.get("next_manifest_coordinate", {}).get("u") == 2.5e-6 and auth.get("next_manifest_coordinate", {}).get("v") == -5e-6,
    "rank22_multiplicity_one": auth.get("next_manifest_coordinate", {}).get("source_occurrence_multiplicity") == 1,
    "rank22_half_local_index_8": auth.get("next_manifest_coordinate", {}).get("source_local_index") == 8,
    "stage_reads_rank21_authority": "post504_rank21_raw_consumption.json" in stage,
    "stage_requires_rank21_pass_classification": "PASS_RAW_CONSUMED_MANIFEST_RANK21_FULL_Z_MP80_MP120__NON_PROMOTING" in stage,
    "stage_inherits_frozen_sampling_parent": "post447_class3_phi_sample_mp_stage.py" in stage,
    "stage_inherits_frozen_mass_binding_parent": "iteration379_tru1sq_double_double_one_channel_pilot.py" in stage,
    "base_h_frozen_5e6": "abs(BASE_H-5e-6)>1e-18" in stage,
    "rank22_mass_binding_from_base_h": "MASS_U=0.5*BASE_H; MASS_V=-BASE_H" in stage,
    "training_z_frozen": "Z_SAMPLES=(-0.86,-0.43,0.0,0.43,0.86)" in stage,
    "precision_levels_inherited": "MP_LEVELS=C['MP_LEVELS']" in stage,
    "mp_threshold_inherited": "MP_LIMIT=C['MP_LIMIT']" in stage,
    "phi_nodes_inherited": "NPHI=C['NPHI']" in stage,
    "radial_threshold_inherited": "RADIAL_LIMIT=C['RADIAL_LIMIT']" in stage,
    "no_physical_promotion_guardrail": "NO_PHYSICAL_DS_PROMOTION" in stage,
    "no_threshold_weakening_guardrail": "NO_THRESHOLD_WEAKENING" in stage,
    "no_ansatz003_guardrail": "NO_ANSATZ003" in stage,
    "no_fisher_resources_guardrail": "NO_FISHER_RESOURCES" in stage,
}

passed = all(checks.values())
result = {
    "schema": "rqir.candidate_gravity.rank22_prerequisite_dynamics_chain.v1",
    "iteration": 506,
    "classification": "PASS_RANK22_PREREQUISITE_DYNAMICS_PARAMETER_CHAIN_EXACT__NON_PROMOTING" if passed else "BLOCKED_RANK22_PREREQUISITE_DYNAMICS_PARAMETER_CHAIN_DRIFT__NON_PROMOTING",
    "scientific_gate_pass": passed,
    "scope": "SOURCE_PROVENANCE_AND_FROZEN_PARAMETER_CONVENTION_ONLY",
    "checks": checks,
    "target": {
        "manifest_rank": 22,
        "u": 2.5e-6,
        "v": -5e-6,
        "source_occurrence_multiplicity": 1,
        "source_level": "HALF",
        "source_local_index": 8,
    },
    "scientific_semantics": {
        "candidate_gravity_consistency_fail": False,
        "exact_comparator_identity": False,
        "regime_specific_non_identifiability": False,
        "near_degeneracy": False,
        "novelty_certificate": False,
        "operational_blocked_if_failed": True,
    },
    "MODEL_READINESS": "24%",
    "readiness_change_pp": 0,
}
print(json.dumps(result, indent=2, sort_keys=True))
if not passed:
    raise SystemExit(2)
