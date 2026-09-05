#!/usr/bin/env python3
"""Iteration 462: exact frozen central4 x central4 tensor-moment invariants.

No floating-point arithmetic is used.  This script verifies the operator identities
that the post-support BASE/HALF assembly must satisfy before any physical promotion.
"""
from fractions import Fraction
import json

X = (-2, -1, 1, 2)
C = (Fraction(1, 12), Fraction(-2, 3), Fraction(2, 3), Fraction(-1, 12))

moments = {k: sum(ci * Fraction(xi) ** k for xi, ci in zip(X, C)) for k in range(8)}
expected_0_to_5 = {
    0: Fraction(0),
    1: Fraction(1),
    2: Fraction(0),
    3: Fraction(0),
    4: Fraction(0),
    5: Fraction(-4),
}
assert all(moments[k] == v for k, v in expected_0_to_5.items())

# Dimensionless tensor moments.  Physical weights are c_i c_j / h^2 and
# coordinates are h*x_i, h*x_j, so h cancels in the normalized monomial test.
tensor = {}
for a in range(5):
    for b in range(5):
        value = moments[a] * moments[b]
        tensor[f"u^{a}v^{b}"] = str(value)
        target = Fraction(1) if (a, b) == (1, 1) else Fraction(0)
        assert value == target

l1_1d = sum(abs(ci) for ci in C)
l1_tensor = l1_1d * l1_1d
assert l1_1d == Fraction(3, 2)
assert l1_tensor == Fraction(9, 4)

result = {
    "iteration": 462,
    "classification": "PASS_CENTRAL4_TENSOR_MOMENT_INVARIANTS__NON_PROMOTING",
    "nodes": list(X),
    "coefficients": [str(v) for v in C],
    "moments_k0_to_k7": {str(k): str(v) for k, v in moments.items()},
    "exactness_statement": "For a,b in {0,1,2,3,4}, sum_ij c_i c_j x_i^a x_j^b = 1 only for (a,b)=(1,1), and 0 otherwise.",
    "tensor_moments_a0_to4_b0_to4": tensor,
    "l1_1d": str(l1_1d),
    "l1_tensor_prescaling": str(l1_tensor),
    "first_nonzero_1d_truncation_moment": {"k": 5, "value": str(moments[5])},
    "promotion": False,
}
print(json.dumps(result, indent=2, sort_keys=True))
