from fractions import Fraction
import json

c = [Fraction(1,12), Fraction(-2,3), Fraction(2,3), Fraction(-1,12)]
weights = [[ci*cj for cj in c] for ci in c]

sum_abs_1d = sum(abs(x) for x in c)
l1_2d = sum(abs(w) for row in weights for w in row)
l2sq_1d = sum(x*x for x in c)
frobenius_sq_2d = sum(w*w for row in weights for w in row)
max_abs_weight = max(abs(w) for row in weights for w in row)

assert sum_abs_1d == Fraction(3,2)
assert l1_2d == Fraction(9,4)
assert l2sq_1d == Fraction(65,72)
assert frobenius_sq_2d == Fraction(4225,5184)
assert max_abs_weight == Fraction(4,9)

# If each sampled value F_ij has independent absolute perturbation |delta F_ij| <= eps,
# then for D_h = sum_ij c_i c_j F_ij / h^2,
# |delta D_h| <= (sum_ij |c_i c_j|) eps / h^2 = (9/4) eps / h^2.
# HALF uses h/2, so the same per-sample absolute-error cap implies a factor-four larger bound.
base_bound_factor = l1_2d
half_bound_factor_in_base_h_units = 4*l1_2d
assert half_bound_factor_in_base_h_units == Fraction(9,1)
assert half_bound_factor_in_base_h_units / base_bound_factor == 4

out = {
    "classification": "PASS_CENTRAL4_SAMPLE_ERROR_AMPLIFICATION_BOUND_EXACT__NON_PROMOTING",
    "central4_coefficients": [str(x) for x in c],
    "sum_abs_1d": str(sum_abs_1d),
    "mixed_l1_weight_sum": str(l1_2d),
    "mixed_frobenius_norm_sq": str(frobenius_sq_2d),
    "max_abs_mixed_weight": str(max_abs_weight),
    "base_absolute_error_bound": "|delta D_BASE| <= (9/4) eps / h^2",
    "half_absolute_error_bound_same_eps_base_h_units": "|delta D_HALF| <= 9 eps / h^2",
    "half_to_base_worst_case_bound_ratio_same_sample_eps": 4,
    "scope": "estimator/provenance only; not Candidate-Gravity consistency PASS/FAIL or physical promotion"
}
print(json.dumps(out, indent=2))
