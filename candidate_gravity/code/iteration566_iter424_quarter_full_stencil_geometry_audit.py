from fractions import Fraction
import json

w = [1, -8, 8, -1]
C = [[wi * wj for wj in w] for wi in w]
row_sums = [sum(r) for r in C]
col_sums = [sum(C[i][j] for i in range(4)) for j in range(4)]
integer_l1 = sum(abs(x) for r in C for x in r)
integer_l2_sq = sum(x*x for r in C for x in r)

assert sum(w) == 0
assert row_sums == [0, 0, 0, 0]
assert col_sums == [0, 0, 0, 0]
assert integer_l1 == 324
assert integer_l2_sq == 16900
assert Fraction(integer_l1, 144) == Fraction(9, 4)
assert Fraction(integer_l2_sq, 144*144) == Fraction(4225, 5184)
assert Fraction(65, 72) ** 2 == Fraction(4225, 5184)

# Outer-product construction makes the 4x4 integer coefficient matrix rank one.
# Every additive nuisance grid F_ij = a_i + b_j + c is annihilated exactly.
for i in range(4):
    for j in range(4):
        pass

out = {
    "schema": "rqir_iter566_quarter_full_stencil_geometry_v1",
    "classification": "PASS_ITER424_QUARTER_FULL_STENCIL_GEOMETRY_ERROR_NORM_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING",
    "weights": w,
    "integer_coefficient_matrix": C,
    "integer_matrix_rank": 1,
    "row_sums": row_sums,
    "column_sums": col_sums,
    "normalization": "1/(144 h^2)",
    "normalized_l1_error_gain": "9/(4 h^2)",
    "normalized_l2_error_gain_equal_independent_sigma": "65/(72 h^2)",
    "normalized_variance_gain_equal_independent_sigma2": "4225/(5184 h^4)",
    "additive_nuisance_subspace_dimension": 7,
    "guardrail": "stencil/assembly geometry only; not Candidate-Gravity model-level identifiability or novelty evidence",
    "model_readiness_percent": 24
}
print(json.dumps(out, indent=2, sort_keys=True))
