#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 420.

Prospective interpretation contract for the sole remaining Tr(U1^2) double-double
blocker (global index 2 / class 3 / q^2=-1), frozen before Iteration 419 raw
results are consumed. This script does not compute or promote a physical
coordinate. It fixes how the Iteration-419 diagnostics are to be interpreted so
that no post-hoc explanation can be selected after seeing the measured
cancellation/roundoff metrics.
"""
import json

ITERATION = 420
MODEL_READINESS = 24
PHYSICAL_TOL = 2.0e-5
OBSERVED_FINE_DISCREPANCY = 2.769196909034482e-4  # raw Iteration 413
MATERIAL_FRACTION = 0.25
MATERIAL_ROUNDOFF = MATERIAL_FRACTION * OBSERVED_FINE_DISCREPANCY

contract = {
    "iteration": ITERATION,
    "model_readiness_percent": MODEL_READINESS,
    "candidate_residual": False,
    "scientific_gate_pass": True,
    "classification": "PASS_CHANNEL2_CANCELLATION_INTERPRETATION_CONTRACT__PROSPECTIVE_NONPROMOTING",
    "authority_scope": "METHODOLOGICAL_ONLY__NO_PHYSICAL_COORDINATE_PROMOTION",
    "target": {"double_double_global_index": 2, "class_id": 3, "q_squared": -1.0, "physical_status": "BLOCKED_CONVERGENCE"},
    "frozen_inputs": {
        "iteration413_scaled_mass_step_discrepancy": OBSERVED_FINE_DISCREPANCY,
        "physical_threshold": PHYSICAL_TOL,
        "material_roundoff_fraction_of_observed_discrepancy": MATERIAL_FRACTION,
        "material_roundoff_absolute_threshold": MATERIAL_ROUNDOFF
    },
    "decision_rule_after_iteration419": [
        {
            "condition": "max_binary64_roundoff_bound_scaled >= material_roundoff_absolute_threshold OR max_naive_vs_compensated_scaled_delta >= material_roundoff_absolute_threshold",
            "classification": "BINARY64_CANCELLATION_MATERIALLY_CAPABLE_OF_EXPLAINING_INSTABILITY",
            "authorized_next_gate": "re-evaluate the SAME frozen analytic fixed-mass sphere values and central4xcentral4 mixed derivative with an algebraically identical higher-precision arithmetic path; require precision ladder stability and existing original-integrand cross-check; do not refine h"
        },
        {
            "condition": "both roundoff indicators < material_roundoff_absolute_threshold",
            "classification": "BINARY64_SUMMATION_ALONE_INSUFFICIENT_TO_EXPLAIN_INSTABILITY",
            "authorized_next_gate": "audit conditioning of the fixed-mass analytic_sphere_G evaluation itself (kinematics, polynomial reconstruction, affine-denominator recurrence, radial extrapolation) and construct algebraically equivalent high-precision mass-node evaluation; do not refine h"
        }
    ],
    "promotion_rule": "Iteration 419 cannot promote index 2 under either branch. A physical coordinate requires a later raw-valid CONVERGED high-precision/algebraically-equivalent derivative representation with unchanged 2e-5 threshold and the existing structural/direct-integrand checks.",
    "guardrails": [
        "NO_THRESHOLD_WEAKENING", "NO_NEW_SMALLER_H", "NO_ANGULAR_GRID_ESCALATION", "NO_ZERO_FILL",
        "NO_PHYSICAL_AUTHORITY_FROM_ITERATION419_OR_420", "NO_SOURCE_BORN_SUBTRACTION", "NO_ANSATZ003", "NO_FISHER_RESOURCES"
    ]
}

print(json.dumps(contract, indent=2, sort_keys=True))
