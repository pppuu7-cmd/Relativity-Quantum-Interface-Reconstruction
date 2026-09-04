#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 431.

Fail-closed source dependency audit for the first arbitrary-precision port stage
authorized by Iteration 430.  This audit does not evaluate or promote a physical
D_s coordinate.  It establishes the actual precision boundary below nominal
Iterations 368/370 and prevents a false 'high-precision 368/370' certificate
that leaves hidden binary64 parent primitives untouched.
"""
from __future__ import annotations
import ast
import json
from pathlib import Path

ITERATION = 431
ROOT = Path(__file__).resolve().parent
SRC270 = ROOT / "iteration270_vd_physical_b3_nonzero.py"
SRC368 = ROOT / "iteration368_tru1sq_timelike_full_prepruning_routing.py"
SRC370 = ROOT / "iteration370_tru1sq_timelike_numerator_transport.py"

for p in (SRC270, SRC368, SRC370):
    if not p.exists():
        raise SystemExit(f"missing frozen source: {p}")

s270 = SRC270.read_text()
s368 = SRC368.read_text()
s370 = SRC370.read_text()

# Iteration 368 executes the pre-certificate prefix of Iteration 270 and extracts
# these exact numerical primitives from its namespace.
required_parent_bindings = ["ETA", "Q0", "Q1", "Asub", "y_down"]
parent_path_bound = "iteration270_vd_physical_b3_nonzero.py" in s368
binding_checks = {name: (f"ns['{name}']" in s368 or f'ns["{name}"]' in s368) for name in required_parent_bindings}

# Iteration 370, in turn, executes the setup/block-definition prefix of 368.
child_path_bound = "iteration368_tru1sq_timelike_full_prepruning_routing.py" in s370
child_required = ["first_u1", "second_primitive", "second_specs", "ksum"]
child_binding_checks = {name: (f"ns['{name}']" in s370 or f'ns["{name}"]' in s370) for name in child_required}

# Establish that the parent is a numerical binary64 layer, not a symbolic-only
# declaration.  We intentionally report anchors rather than attempting an error
# certificate here; Iteration 430 requires either a later quantitative bound or
# an arbitrary-precision port.
binary64_anchors = {
    "numpy_import": "import numpy as np" in s270,
    "linalg_inv": "np.linalg.inv" in s270,
    "linalg_det": "np.linalg.det" in s270,
    "linalg_norm": "np.linalg.norm" in s270,
    "float_arrays": "dtype=float" in s270 or "astype(float)" in s270,
    "complex_arrays": "complex)" in s270 or "complex)" in s270,
    "finite_difference_N1": "def N1(" in s270 and "/(2*h)" in s270,
    "finite_difference_N2": "def N2(" in s270 and "/(4*h*h)" in s270,
    "finite_difference_Asub": "def Asub(" in s270 and "Acoef" in s270,
}

# AST-level function presence makes the dependency audit robust to comments.
tree270 = ast.parse(s270)
funcs270 = {n.name for n in ast.walk(tree270) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
required_parent_functions = ["Q0", "Q1", "Asub", "y_down"]
function_checks = {name: name in funcs270 for name in required_parent_functions}

passed = bool(
    parent_path_bound
    and child_path_bound
    and all(binding_checks.values())
    and all(child_binding_checks.values())
    and all(binary64_anchors.values())
    and all(function_checks.values())
)

result = {
    "iteration": ITERATION,
    "model_readiness_percent": 24,
    "scientific_gate_pass": passed,
    "physical_promotion": False,
    "candidate_residual": False,
    "classification": (
        "PASS_CHANNEL2_STAGE1_PARENT_PRECISION_BOUNDARY_CLOSURE__NON_PROMOTING"
        if passed else
        "BLOCKED_CHANNEL2_STAGE1_PARENT_PRECISION_BOUNDARY_AUDIT"
    ),
    "scope": "SOURCE_LEVEL_PRECISION_DEPENDENCY_BOUNDARY_ONLY__NO_PHYSICAL_D_S",
    "nominal_stage_from_iteration430": "368/370",
    "corrected_stage1_precision_closure": "270[Q0,Q1,Asub,y_down plus recursive numerical dependencies] -> 368/370",
    "source_chain": {
        "iteration370_executes_368_setup": child_path_bound,
        "iteration368_executes_270_prefix": parent_path_bound,
        "iteration368_parent_bindings": binding_checks,
        "iteration370_child_bindings": child_binding_checks,
        "iteration270_function_presence": function_checks,
        "iteration270_binary64_anchors": binary64_anchors,
    },
    "frozen_interpretation": [
        "A nominal 368/370 arbitrary-precision wrapper is not a complete stage-1 precision certificate if Iteration-270 parent primitives remain uncertified binary64.",
        "Every retained lower-precision parent primitive must receive a quantitative error bound sufficient for all downstream Iteration-424 gates; otherwise it must be ported to arbitrary precision.",
        "This source-dependency correction does not change parent dynamics, routing, numerator, sign, normalization, mass nodes, finite-difference definitions, or any frozen threshold.",
        "Passing this audit does not promote index 2 or unlock exact15 assembly.",
    ],
    "unchanged_downstream_gates": {
        "mass_step_max": 2e-5,
        "original_integrand_max": 2e-6,
        "tensor_1_1_fit_max": 2e-5,
        "cross_precision_Ds_80_120_max": 2e-6,
        "precision_decimal_digits": [80, 120],
    },
    "next_gate": "Port or quantitatively certify the Iteration-270 parent primitive closure Q0/Q1/Asub/y_down and recursively used numerical operations at 80/120-digit provenance; only then certify nominal 368/370 and continue 379/374 -> 407 -> Iteration 424 -> Iteration 427.",
    "guardrails": [
        "NO_PHYSICAL_PROMOTION",
        "NO_THRESHOLD_WEAKENING",
        "NO_SMALLER_MASS_STEP",
        "NO_ZERO_FILL",
        "NO_ANSATZ003",
        "NO_FISHER_RESOURCES",
    ],
}

print(json.dumps(result, indent=2, sort_keys=True))
if not passed:
    raise SystemExit(2)
