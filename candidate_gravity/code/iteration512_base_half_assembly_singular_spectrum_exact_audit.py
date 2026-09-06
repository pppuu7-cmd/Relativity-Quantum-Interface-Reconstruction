#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
import json
import math

# Exact Gram matrix fixed by Iteration 510 for the two frozen BASE/HALF assembly rows.
a = Fraction(4225, 5184)
b = Fraction(4, 81)
d = Fraction(4225, 324)
trace = a + d
det = a*d - b*b

# Eigenvalues of a symmetric 2x2 matrix: (tr +/- sqrt((a-d)^2+4b^2))/2.
# Keep the algebraic form exact in the record; Decimal values are diagnostics only.
disc_num = 4016652769
disc_den = 10368
lambda_minus_exact = "(71825-sqrt(4016652769))/10368"
lambda_plus_exact = "(71825+sqrt(4016652769))/10368"

getcontext().prec = 60
sqrt_disc = Decimal(disc_num).sqrt()
lam_minus = (Decimal(71825) - sqrt_disc) / Decimal(10368)
lam_plus = (Decimal(71825) + sqrt_disc) / Decimal(10368)
cond_G = lam_plus / lam_minus
cond_A = cond_G.sqrt()  # singular-value condition number of the 2-row assembly map

result = {
    "iteration": 512,
    "classification": "AUDIT_BASE_HALF_ASSEMBLY_SINGULAR_SPECTRUM_EXACT__NON_PROMOTING",
    "scope": "exact numerical/provenance conditioning of the frozen two-row BASE/HALF assembly map; no physical promotion",
    "gram_matrix": [["4225/5184", "4/81"], ["4/81", "4225/324"]],
    "trace_exact": "71825/5184",
    "determinant_exact": "5948843/559872",
    "eigenvalues_exact": [lambda_minus_exact, lambda_plus_exact],
    "eigenvalue_min_decimal": str(lam_minus),
    "eigenvalue_max_decimal": str(lam_plus),
    "gram_condition_number_decimal": str(cond_G),
    "assembly_singular_condition_number_decimal": str(cond_A),
    "positive_definite": True,
    "rank": 2,
    "interpretation": "BASE and HALF assembly rows remain linearly independent and moderately conditioned in their two-dimensional row space. This quantifies numerical geometry only; it is not a new frozen threshold, observable covariance claim, Fisher authority, or Candidate-Gravity PASS.",
    "model_readiness_percent": 24,
    "readiness_change_percentage_points": 0
}

print(json.dumps(result, indent=2, sort_keys=True))
