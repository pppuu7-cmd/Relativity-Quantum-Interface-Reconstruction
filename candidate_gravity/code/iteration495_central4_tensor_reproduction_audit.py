#!/usr/bin/env python3
"""Iteration 495: exact tensor-product central4 nullspace/reproduction audit.

Pure rational arithmetic; no Candidate-Gravity dynamics are modified.
"""
from fractions import Fraction
import json

nodes = [-2, -1, 1, 2]
c = [Fraction(1, 12), Fraction(-2, 3), Fraction(2, 3), Fraction(-1, 12)]

moments = {
    k: sum((ci * Fraction(n) ** k for ci, n in zip(c, nodes)), Fraction(0))
    for k in range(5)
}
expected = {0: Fraction(0), 1: Fraction(1), 2: Fraction(0), 3: Fraction(0), 4: Fraction(0)}
assert moments == expected

# Tensor moments factor exactly: M_ab = M_a M_b.
tensor = {(a, b): moments[a] * moments[b] for a in range(5) for b in range(5)}
for (a, b), value in tensor.items():
    assert value == (Fraction(1) if (a, b) == (1, 1) else Fraction(0))

# Row and column sums of w_ij=c_i*c_j vanish exactly. Therefore every
# sampled additive field F_ij = f_i + g_j + const is annihilated with no
# polynomial assumption.
weights = [[ci * cj for cj in c] for ci in c]
row_sums = [sum(row, Fraction(0)) for row in weights]
col_sums = [sum((weights[i][j] for i in range(4)), Fraction(0)) for j in range(4)]
assert all(x == 0 for x in row_sums)
assert all(x == 0 for x in col_sums)

out = {
    "iteration": 495,
    "classification": "PASS_CENTRAL4_TENSOR_NULLSPACE_POLYNOMIAL_REPRODUCTION_EXACT__NON_PROMOTING",
    "nodes": nodes,
    "coefficients": [str(x) for x in c],
    "moments_k0_to_k4": [str(moments[k]) for k in range(5)],
    "tensor_nonzero_moments_a_b_le_4": {"1,1": "1"},
    "row_sums": [str(x) for x in row_sums],
    "column_sums": [str(x) for x in col_sums],
    "exact_claims": {
        "polynomial_reproduction": "For degree <=4 in each variable, D_h p(0,0)=partial_x partial_y p(0,0) exactly.",
        "additive_nullspace": "For arbitrary sampled F_ij=f_i+g_j+const, D_h=0 exactly.",
        "bilinear_normalization": "For p(x,y)=x*y, D_h=1 exactly for every nonzero h."
    }
}
print(json.dumps(out, indent=2, sort_keys=True))
