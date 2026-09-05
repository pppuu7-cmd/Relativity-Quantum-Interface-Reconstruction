#!/usr/bin/env python3
"""Iteration 464: exact leading truncation structure of frozen central4 x central4 mixed derivative.

This is a diagnostic/provenance audit only. It does not change the retained physical
quantity ds=-d_base, does not introduce BASE/HALF Richardson promotion, and does not
alter any frozen thresholds.
"""
from fractions import Fraction
import json

X = (-2, -1, 1, 2)
C = (Fraction(1, 12), Fraction(-2, 3), Fraction(2, 3), Fraction(-1, 12))

moments = {k: sum(ci * Fraction(xi) ** k for xi, ci in zip(X, C)) for k in range(10)}

assert moments[0] == 0
assert moments[1] == 1
assert moments[2] == moments[3] == moments[4] == 0
assert moments[5] == -4
assert moments[6] == 0
assert moments[7] == -20
assert moments[8] == 0
assert moments[9] == -84

# For D_h f = sum_i c_i f(x+h x_i)/h, Taylor coefficient at derivative order k is
# m_k/k! * h^(k-1). Thus the leading nonzero error is -(1/30) h^4 f^(5), followed
# by -(1/252) h^6 f^(7), etc.
from math import factorial
coeff_5 = moments[5] / factorial(5)
coeff_7 = moments[7] / factorial(7)
assert coeff_5 == Fraction(-1, 30)
assert coeff_7 == Fraction(-1, 252)

# Tensor product D_u,h D_v,h F. Through total h^6 terms:
# F_uv - h^4/30 (F_{5,1}+F_{1,5}) - h^6/252 (F_{7,1}+F_{1,7}) + O(h^8),
# while the product of the two h^4 one-dimensional errors first enters at h^8.
leading_tensor = {
    "F_1_1": "1",
    "h4_F_5_1": str(coeff_5),
    "h4_F_1_5": str(coeff_5),
    "h6_F_7_1": str(coeff_7),
    "h6_F_1_7": str(coeff_7),
    "h8_F_5_5_cross": str(coeff_5 * coeff_5),
}
assert coeff_5 * coeff_5 == Fraction(1, 900)

# BASE h_B and HALF h_H=h_B/2: a pure h^4 leading truncation term scales by 16.
ratio_h4 = Fraction(1, 1) / Fraction(1, 2) ** 4
ratio_h6 = Fraction(1, 1) / Fraction(1, 2) ** 6
assert ratio_h4 == 16
assert ratio_h6 == 64

# Diagnostic-only cancellation of a pure h^4 term. If D(h)=D0+a h^4+b h^6+...,
# then (16 D(h/2)-D(h))/15 removes a h^4, but this is NOT the retained physical
# estimator and must never substitute for ds=-d_base or the frozen BASE/HALF gate.
richardson_h4_weights = {"D_half": str(Fraction(16, 15)), "D_base": str(Fraction(-1, 15))}

result = {
    "iteration": 464,
    "classification": "PASS_CENTRAL4_LEADING_TRUNCATION_STRUCTURE__DIAGNOSTIC_ONLY_NON_PROMOTING",
    "moments_k0_to_k9": {str(k): str(v) for k, v in moments.items()},
    "one_dimensional_error_coefficients": {
        "h4_f5": str(coeff_5),
        "h6_f7": str(coeff_7),
    },
    "tensor_expansion_through_h6": leading_tensor,
    "base_to_half_expected_scaling_if_single_term_dominates": {
        "h4": str(ratio_h4),
        "h6": str(ratio_h6),
    },
    "diagnostic_only_h4_cancelling_combination": richardson_h4_weights,
    "guardrail": "No Richardson promotion: retained physics remains ds=-d_base; BASE/HALF scaled discrepancy threshold remains <=2e-5; assembled MP80/120 threshold remains <=2e-6.",
    "promotion": False,
}

print(json.dumps(result, indent=2, sort_keys=True))
