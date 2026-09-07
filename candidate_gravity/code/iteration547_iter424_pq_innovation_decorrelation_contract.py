from fractions import Fraction
import json

C11 = Fraction(8322)
C12 = Fraction(-2130)
C22 = Fraction(546)
det = C11*C22 - C12*C12

# Innovation R = Q + alpha P chosen so Cov(P,R)=0.
alpha = -C12 / C11
var_R = C22 + 2*alpha*C12 + alpha*alpha*C11

# Exact inverse covariance for joint quadratic diagnostics.
Cinv = [
    [C22/det, -C12/det],
    [-C12/det, C11/det],
]

# Frozen truncation map P=(45/16)A, Q=(189/256)B.
coef_A_in_R = alpha * Fraction(45, 16)
coef_B_in_R = Fraction(189, 256)

assert det == 6912
assert alpha == Fraction(355, 1387)
assert var_R == Fraction(1152, 1387)
assert Cinv == [
    [Fraction(91, 1152), Fraction(355, 1152)],
    [Fraction(355, 1152), Fraction(1387, 1152)],
]
assert coef_A_in_R == Fraction(15975, 22192)
assert coef_B_in_R == Fraction(189, 256)

result = {
    "iteration": 547,
    "classification": "PASS_ITER424_PQ_INNOVATION_DECORRELATION_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING",
    "covariance_over_sigma2": [[8322, -2130], [-2130, 546]],
    "determinant": 6912,
    "innovation": {
        "definition": "R = Q + alpha P",
        "alpha_exact": "355/1387",
        "alpha_float": float(alpha),
        "cov_P_R_over_sigma2_exact": "0",
        "var_R_over_sigma2_exact": "1152/1387",
        "var_R_over_sigma2_float": float(var_R),
        "R_truncation_map": {
            "A_coefficient_exact": "15975/22192",
            "B_coefficient_exact": "189/256"
        }
    },
    "inverse_covariance_times_sigma2": [
        ["91/1152", "355/1152"],
        ["355/1152", "1387/1152"]
    ],
    "joint_quadratic_form": "chi_PQ = (91 P^2 + 710 P Q + 1387 Q^2)/(1152 sigma^2)",
    "scope": "Equal-variance independent BASE/HALF/QUARTER level-error model only; numerical/truncation diagnostic, not Candidate-Gravity identifiability or model-level near-degeneracy.",
    "model_readiness_percent": 24
}

print(json.dumps(result, indent=2, sort_keys=True))
