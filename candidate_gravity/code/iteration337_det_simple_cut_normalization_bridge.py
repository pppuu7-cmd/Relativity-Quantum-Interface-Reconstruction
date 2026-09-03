#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 337.

Repository-internal normalization bridge for ordinary two-particle cuts.

Frozen inputs only:
- Iteration 296: common loop normalization i*pi^(D/2),
  D_s F=(F_advanced-F_retarded)/(2*pi*i), and the ordinary massless scalar
  bubble calibrates to D_s B -> -1 in D->4.
- Iteration 336: standard Lorentz-invariant two-massless-particle phase space
  integrates to 1/(8*pi), and a normalized sphere mean obeys
  int dPhi2 F = mean(F)/(8*pi).
- Iteration 333 determinant cuts are ordinary two-simple-line Cutkosky surfaces;
  no raised cut propagators are introduced by this bridge.

Therefore the repository-normalized simple cut conversion is fixed by the same
scalar bubble calibration, without importing a textbook sign convention:

    D_s I[F] = -8*pi * int dPhi2 F = - mean(F).

This gate deliberately does NOT infer the common outer determinant effective-
action factor. Iteration 307 explicitly freezes -i/2 for its Tr U1 connection
coordinate, but transferring that coefficient to the determinant sector without
same-parent determinant provenance is forbidden here.
"""
from __future__ import annotations
import json, math

MODEL_READINESS = 24

# Frozen scalar calibration from Iteration 296.
scalar_bubble_repo_Ds = -1.0
# Frozen geometric factor from Iteration 336.
phase_space_for_unit_integrand = 1.0 / (8.0 * math.pi)
mean_to_phase_space = 1.0 / (8.0 * math.pi)

# Calibrated bridge from standard LIPS to repository-normalized D_s.
phase_space_to_repo_Ds = scalar_bubble_repo_Ds / phase_space_for_unit_integrand
mean_to_repo_Ds = phase_space_to_repo_Ds * mean_to_phase_space

err_phase = abs(phase_space_to_repo_Ds - (-8.0 * math.pi))
err_mean = abs(mean_to_repo_Ds - (-1.0))
passed = err_phase < 1e-14 and err_mean < 1e-14

result = {
    "iteration": 337,
    "model_readiness_percent": MODEL_READINESS,
    "scientific_gate_pass": bool(passed),
    "classification": (
        "PASS_REPOSITORY_NORMALIZED_SIMPLE_TWO_PARTICLE_CUT_CONVERSION__DET_OUTER_EFFECTIVE_ACTION_FACTOR_REMAINS_BLOCKED"
        if passed else
        "FAIL_REPOSITORY_NORMALIZED_SIMPLE_TWO_PARTICLE_CUT_CONVERSION"
    ),
    "candidate_residual": False,
    "frozen_inputs": {
        "iteration296_loop_normalization": "i*pi^(D/2)",
        "iteration296_Ds": "(advanced-retarded)/(2*pi*i)",
        "iteration296_scalar_bubble_Ds_limit": scalar_bubble_repo_Ds,
        "iteration336_integrated_massless_dPhi2": "1/(8*pi)",
        "iteration336_normalized_sphere_mean_to_dPhi2": "1/(8*pi)",
    },
    "derived_bridge": {
        "standard_phase_space_to_repository_Ds": "-8*pi",
        "normalized_sphere_mean_to_repository_Ds": "-1",
        "ordinary_simple_cut_formula": "D_s I[F] = -8*pi * int(dPhi2 F) = - sphere_mean(F)",
        "numeric_phase_space_to_repository_Ds": phase_space_to_repo_Ds,
        "numeric_mean_to_repository_Ds": mean_to_repo_Ds,
        "closure_errors": {
            "phase_space_factor": err_phase,
            "sphere_mean_factor": err_mean,
        },
    },
    "scope": {
        "allowed": [
            "ordinary two-particle cuts with two simple massless cut propagators",
            "same advanced-retarded branch orientation as Iteration 296",
            "same repository loop normalization as Iteration 296",
            "uncut numerator/propagator factors evaluated on the same Cutkosky shell",
        ],
        "not_covered": [
            "raised cut propagators or derivative delta distributions",
            "overlapping/third-propagator singular cuts",
            "full finite DR remainder",
            "source/Ward/contact completion",
            "matched K2 subtraction",
            "common outer determinant effective-action i/prefactor",
        ],
    },
    "sector_separation": {
        "iteration307_connection_prefactor": "-i/2 multiplying Tr U1, stored outside that coordinate",
        "transfer_to_determinant_authorized": False,
        "reason": "connection-sector prefactor must not be synthetically reused as determinant-sector outer prefactor without explicit same-parent determinant provenance",
    },
    "guardrails": [
        "NO_TEXTBOOK_SIGN_IMPORT_NEEDED_FOR_THIS_BRIDGE",
        "NO_RAISED_CUT_PROPAGATOR_PROMOTION",
        "NO_SYNTHETIC_TRU1_TO_DETERMINANT_OUTER_PREFACTOR_TRANSFER",
        "ITERATION297_FINITE_DR_WARNING_REMAINS_BINDING",
        "NO_SOURCE_BORN_SUBTRACTION",
        "NO_ANSATZ003",
        "NO_FISHER_RESOURCES",
    ],
    "next_gate": "locate or derive the same-parent common outer determinant effective-action convention; independently, when Iteration 335 resolves, convert its ordinary channel sphere means with the frozen -1 mean-to-D_s bridge before matched-observable assembly",
}

print(json.dumps(result, indent=2, sort_keys=True))
if not passed:
    raise SystemExit(2)
