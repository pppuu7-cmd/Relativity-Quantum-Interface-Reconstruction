#!/usr/bin/env python3
from fractions import Fraction
import json

xs = [Fraction(1,1), Fraction(9,16), Fraction(1,4), Fraction(1,16)]

# A has rows [1,x].  Exact inverse of A^T A for the frozen one-axis design.
Ginv = [
    [Fraction(59,86), Fraction(-40,43)],
    [Fraction(-40,43), Fraction(256,129)],
]

def h1(x, y):
    return Ginv[0][0] + Ginv[0][1]*y + x*Ginv[1][0] + x*Ginv[1][1]*y

H1 = [[h1(x,y) for y in xs] for x in xs]
lev1 = [H1[i][i] for i in range(4)]
lev2 = [[lev1[i]*lev1[j] for j in range(4)] for i in range(4)]
flat = [z for row in lev2 for z in row]

assert lev1 == [Fraction(209,258), Fraction(23,86), Fraction(89,258), Fraction(149,258)]
assert sum(flat, Fraction(0,1)) == Fraction(4,1)
assert min(flat) == Fraction(529,7396)
assert max(flat) == Fraction(43681,66564)
assert max(flat) < 1

residual_diag = [[Fraction(1,1)-z for z in row] for row in lev2]
assert min(z for row in residual_diag for z in row) == Fraction(22883,66564)

out = {
    "iteration": 577,
    "classification": "PASS_ITER421_TENSOR11_LEVERAGE_SINGLE_ORBIT_ROBUSTNESS_AUDIT_EXACT__NON_PROMOTING",
    "frozen_axis_x": [str(x) for x in xs],
    "one_axis_hat_matrix": [[str(z) for z in row] for row in H1],
    "one_axis_leverages": [str(z) for z in lev1],
    "two_axis_leverages": [[str(z) for z in row] for row in lev2],
    "sum_two_axis_leverages": "4",
    "min_two_axis_leverage": str(min(flat)),
    "max_two_axis_leverage": str(max(flat)),
    "min_residual_projector_diagonal": str(min(z for row in residual_diag for z in row)),
    "all_leverages_strictly_below_one": True,
    "single_observation_deletion_preserves_design_rank": True,
    "scope": "design robustness only; does not evaluate tensor11 residual, alter the frozen fit, or promote physical index2",
    "model_readiness": "24%",
}

print(json.dumps(out, indent=2))
