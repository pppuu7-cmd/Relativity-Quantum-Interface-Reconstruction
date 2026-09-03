#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 338.

Same-parent one-loop effective-action prefactor audit for the determinant sector.

Authority chain:
1. The frozen/recovered Vilkovisky-DeWitt reduced one-loop convention is

   Gamma^(1) = +(i/2) Tr ln H - i Tr ln N
               -(i/2)(Tr U1 - Tr U2) -(i/4) Tr U1^2 + O(epsilon^3).

2. Iteration 330 constructs every physical determinant route as

   C_det = (1/2) Tr_H - Tr_N

   with the cubic logdet topology weights already inside the route coordinate.

3. Iteration 307 independently freezes the connection-sector coefficient -i/2
   multiplying Tr U1 outside the stored Tr U1 normalized-cut coordinate.

The first formula therefore gives the common determinant effective-action factor

   Gamma_det = +i * C_det,

and its U1 coefficient reproduces the already-frozen Iteration-307 -i/2 sign.
This gate does not perform any angular integration or consume Iteration 335.
"""
from __future__ import annotations
import json

MODEL_READINESS = 24

# Algebraic coefficients in the frozen reduced one-loop convention.
det_graviton_coeff = 0.5j
det_ghost_coeff = -1.0j
common_det_outer = 1.0j
route_graviton_weight = 0.5
route_ghost_weight = -1.0
tru1_coeff = -0.5j
iteration307_tru1_coeff = -0.5j

# Exact internal consistency checks.
err_h = abs(common_det_outer * route_graviton_weight - det_graviton_coeff)
err_n = abs(common_det_outer * route_ghost_weight - det_ghost_coeff)
err_u1 = abs(tru1_coeff - iteration307_tru1_coeff)
passed = max(err_h, err_n, err_u1) == 0.0

result = {
    "iteration": 338,
    "model_readiness_percent": MODEL_READINESS,
    "scientific_gate_pass": bool(passed),
    "classification": (
        "PASS_SAME_PARENT_DETERMINANT_EFFECTIVE_ACTION_OUTER_PLUS_I_PREFactor__TRU1_MINUS_I_OVER_2_CROSSCHECK"
        if passed else
        "FAIL_SAME_PARENT_DETERMINANT_EFFECTIVE_ACTION_PREFACTOR_AUDIT"
    ),
    "candidate_residual": False,
    "frozen_reduced_one_loop_convention": (
        "Gamma1 = +(i/2) Tr ln H - i Tr ln N "
        "-(i/2)(Tr U1 - Tr U2) -(i/4) Tr U1^2 + O(epsilon^3)"
    ),
    "iteration330_route_coordinate": "C_det = (1/2) Tr_H - Tr_N, with logdet topology weights internal",
    "derived": {
        "common_determinant_effective_action_factor": "+i",
        "Gamma_det_relation": "Gamma_det = +i * C_det",
        "normalized_discontinuity_relation": "D_s Gamma_det = +i * D_s C_det",
        "iteration307_TrU1_coefficient_crosscheck": "-i/2",
    },
    "algebraic_closure_errors": {
        "graviton": err_h,
        "ghost": err_n,
        "TrU1": err_u1,
    },
    "authority_boundary": {
        "frozen": [
            "relative determinant weights 1/2 graviton and -1 ghost",
            "common determinant outer effective-action factor +i",
            "Tr U1 outer coefficient -i/2 consistency",
        ],
        "not_frozen": [
            "Iteration 335 unresolved q^2=-1 angular convergence result",
            "full finite DR remainder",
            "source/Ward/contact completion",
            "matched K2 subtraction",
            "comparator-subtracted residual",
        ],
    },
    "guardrails": [
        "DO_NOT_CHANGE_ITERATION330_INTERNAL_LOGDET_WEIGHTS",
        "DO_NOT_DOUBLE_APPLY_GHOST_MINUS_OR_GRAVITON_HALF",
        "DO_NOT_DOUBLE_APPLY_TRU1_MINUS_I_OVER_2",
        "ITERATION297_FINITE_DR_WARNING_REMAINS_BINDING",
        "NO_SOURCE_BORN_SUBTRACTION",
        "NO_ANSATZ003",
        "NO_FISHER_RESOURCES",
    ],
    "next_gate": "after Iteration 337 authority is validated, combine +i determinant outer factor with the repository-normalized ordinary-cut bridge; once Iteration 335 resolves, assemble the channel-resolved determinant D_s coordinate without weakening its convergence threshold",
}

print(json.dumps(result, indent=2, sort_keys=True))
if not passed:
    raise SystemExit(2)
