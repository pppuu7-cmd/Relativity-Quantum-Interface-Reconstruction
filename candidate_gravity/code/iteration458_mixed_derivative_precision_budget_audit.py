#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 458.

Exact algebraic audit of how fixed-mass F(u,v) precision errors propagate through
the frozen central4 x central4 auxiliary-mass derivative used by Iteration 407.
No F(u,v) evaluation is performed. This is a prospective post-support assembly
precision contract and does not promote any physical coordinate.
"""
from fractions import Fraction
import json

ITERATION = 458
MODEL_READINESS = 24
BASE_H = Fraction(5, 1_000_000)       # 5e-6
HALF_H = Fraction(25, 10_000_000)     # 2.5e-6
C = [Fraction(1,12), Fraction(-2,3), Fraction(2,3), Fraction(-1,12)]
PHYSICAL_MP_CROSS_PRECISION_TOL = Fraction(2, 1_000_000)  # 2e-6
LOCAL_SCALED_MP_TOL = Fraction(1, 10**30)

l1_first = sum(abs(x) for x in C)
l1_tensor = l1_first * l1_first

def level(h):
    op_l1 = l1_tensor / (h*h)
    uniform_abs_delta_sufficient = PHYSICAL_MP_CROSS_PRECISION_TOL / op_l1
    max_uniform_sample_scale_if_local_scaled_tol_saturated = uniform_abs_delta_sufficient / LOCAL_SCALED_MP_TOL
    return {
        "h": float(h),
        "central4xcentral4_l1_operator_norm": float(op_l1),
        "uniform_absolute_sample_delta_sufficient_for_2e-6_assembly": float(uniform_abs_delta_sufficient),
        "max_uniform_sample_scale_compatible_with_1e-30_local_scaled_gate_if_saturated": float(max_uniform_sample_scale_if_local_scaled_tol_saturated),
        "exact_operator_norm": f"{op_l1.numerator}/{op_l1.denominator}",
        "exact_uniform_abs_delta_sufficient": f"{uniform_abs_delta_sufficient.numerator}/{uniform_abs_delta_sufficient.denominator}",
    }

result = {
    "iteration": ITERATION,
    "MODEL_READINESS": f"{MODEL_READINESS}%",
    "classification": "PASS_MIXED_DERIVATIVE_PRECISION_BUDGET_FROZEN__NON_PROMOTING",
    "scientific_gate_pass": True,
    "promotes_physical_coordinate": False,
    "frozen_algebra": {
        "central4_coefficients": [str(x) for x in C],
        "first_derivative_l1_sum": float(l1_first),
        "tensor_l1_sum_before_h_scaling": float(l1_tensor),
        "physical_mp_cross_precision_tolerance": float(PHYSICAL_MP_CROSS_PRECISION_TOL),
        "local_scaled_mp_tolerance": float(LOCAL_SCALED_MP_TOL),
    },
    "base": level(BASE_H),
    "half": level(HALF_H),
    "prospective_post_support_contract": [
        "After all 28 distinct F(u,v) coordinates have local MP80/120 precision certificates, assemble BASE and HALF mixed derivatives independently at MP80 and MP120 from the same frozen 32 source occurrences and level-specific central4 weights.",
        "Require all four assembled derivatives finite.",
        "Require |d_base_80-d_base_120|/max(1,|d_base_80|,|d_base_120|) <= 2e-6.",
        "Require |d_half_80-d_half_120|/max(1,|d_half_80|,|d_half_120|) <= 2e-6.",
        "Retain the independent frozen BASE-vs-HALF physical mass-step gate <=2e-5; MP cross-precision and mass-step convergence are distinct gates.",
        "Report the maximum absolute F80-F120 difference, maximum local sample scale max(1,|F80|,|F120|), and the weighted error budget sum_ij |w_ij| |F80-F120| for each level.",
    ],
    "guardrails": [
        "NO_FUV_EVALUATION_IN_THIS_ITERATION",
        "NO_ACTIVE_RUN_DUPLICATION",
        "NO_LOCAL_PASS_TO_ASSEMBLY_PASS_SHORTCUT",
        "NO_BASE_HALF_WEIGHT_COLLAPSE",
        "NO_THRESHOLD_CHANGE",
        "NO_PHYSICAL_DS_PROMOTION",
        "NO_ANSATZ003",
        "NO_FISHER_RESOURCES",
    ],
    "readiness_change_pp": 0,
    "next_gate": "raw-consume active run 33946347229 fail-closed; continue only through Iteration-455 manifest order. After complete support coverage, execute this frozen assembly-level MP80/120 contract before Iteration-424 physical promotion.",
}

print(json.dumps(result, indent=2, sort_keys=True))
