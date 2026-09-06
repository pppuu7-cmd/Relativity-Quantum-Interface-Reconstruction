#!/usr/bin/env python3
"""Iteration 514: exact deterministic error-propagation audit for frozen BASE/HALF central4 assembly.

This audit is deliberately model-agnostic and non-promoting.  It establishes the
induced l_infinity -> absolute-value operator bounds for coordinate-level
perturbations on the frozen 28-coordinate union.  No iid/noise-distribution
assumption is used.
"""
from fractions import Fraction
import json

# Exact l1 row norms in units of 1/h^2, independently established in Iteration 508.
base = Fraction(9, 4)
half = Fraction(9, 1)
delta_union = Fraction(397, 36)
separate_triangle = base + half
cancellation = separate_triangle - delta_union
retained_fraction = delta_union / separate_triangle
relative_reduction = cancellation / separate_triangle

assert separate_triangle == Fraction(45, 4)
assert cancellation == Fraction(2, 9)
assert retained_fraction == Fraction(397, 405)
assert relative_reduction == Fraction(8, 405)

result = {
    "iteration": 514,
    "classification": "PASS_BASE_HALF_DETERMINISTIC_LINF_ERROR_OPERATOR_BOUND_EXACT__NON_PROMOTING",
    "assumption": "For the frozen 28-coordinate union, each absolute coordinate perturbation obeys |e_i| <= epsilon. No iid, Gaussian, covariance, or physical-noise assumption is made.",
    "bounds": {
        "BASE": "|delta BASE| <= (9/4) * epsilon / h^2",
        "HALF": "|delta HALF| <= 9 * epsilon / h^2",
        "BASE_minus_HALF_union": "|delta(BASE-HALF)| <= (397/36) * epsilon / h^2",
        "BASE_minus_HALF_separate_triangle_only": "<= (45/4) * epsilon / h^2",
    },
    "exact_coefficients": {
        "BASE_l1": str(base),
        "HALF_l1": str(half),
        "DELTA_union_l1": str(delta_union),
        "separate_triangle_l1": str(separate_triangle),
        "shared_node_cancellation": str(cancellation),
        "union_over_separate": str(retained_fraction),
        "relative_bound_reduction": str(relative_reduction),
    },
    "guardrail": "The bound is an absolute deterministic assembly-error certificate only. It does not convert local scaled MP discrepancies into assembled scaled discrepancies without an explicit common absolute normalization, does not define a new threshold, and does not make BASE-HALF an independent observable/Fisher row.",
    "promotion": False,
    "model_readiness_percent": 24,
}

print(json.dumps(result, indent=2, sort_keys=True))
