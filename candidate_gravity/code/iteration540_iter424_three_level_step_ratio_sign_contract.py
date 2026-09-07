#!/usr/bin/env python3
"""Iteration 540: exact BASE/HALF/QUARTER step-ratio sign contract.

Diagnostic-only.  This script does not consume physics artifacts and does not
modify any frozen Iteration-424 acceptance threshold.
"""
from fractions import Fraction as F
import json

# X_h = D + A + B + C + O(h^10), with A=a h^4, B=b h^6, C=c h^8.
# HALF uses h/2, QUARTER h/4.
d1 = {
    "A": F(15,16),
    "B": F(63,64),
    "C": F(255,256),
}
d2 = {
    "A": F(15,256),
    "B": F(63,4096),
    "C": F(255,65536),
}

pure_ratios = {k: d1[k] / d2[k] for k in d1}
assert pure_ratios == {"A": F(16), "B": F(64), "C": F(256)}

# For the h^4+h^6 truncation model let t=B/A.  Using q=Y/X, where
# X=d2_A and Y=d2_B, q=(21/80)t and r=d1/d2=(16+64q)/(1+q).
q_over_t = d2["B"] / d2["A"]
assert q_over_t == F(21,80)

# Exact cancellation locations in t=B/A.
t_d2_pole = -1 / q_over_t              # d2=0 -> r undefined
t_d1_zero = -F(1,4) / q_over_t         # 16+64q=0
assert t_d2_pole == F(-80,21)
assert t_d1_zero == F(-20,21)

# Inverse map t(r), valid away from r=64 and d2=0.
# t = (80/21)*(r-16)/(64-r).
inv_prefactor = F(80,21)

result = {
    "iteration": 540,
    "classification": "PASS_ITER424_THREE_LEVEL_STEP_RATIO_SIGN_STRUCTURE_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING",
    "model_readiness_percent": 24,
    "definitions": {
        "d1": "BASE-HALF",
        "d2": "HALF-QUARTER",
        "expansion": "X_h=D+A+B+C+O(h^10), A=a*h^4, B=b*h^6, C=c*h^8"
    },
    "coefficients": {
        "d1": {k: str(v) for k,v in d1.items()},
        "d2": {k: str(v) for k,v in d2.items()},
        "pure_order_d1_over_d2": {k: str(v) for k,v in pure_ratios.items()}
    },
    "h4_h6_ratio_map": {
        "q": "(21/80)*(B/A)",
        "r": "(16+64*q)/(1+q)",
        "inverse_B_over_A": "(80/21)*(r-16)/(64-r)",
        "d2_cancellation_B_over_A": str(t_d2_pole),
        "d1_cancellation_B_over_A": str(t_d1_zero)
    },
    "exact_sign_bounds": {
        "A_and_B_same_sign_nonzero_d2": "16 <= r <= 64",
        "A_B_C_same_sign_nonzero_d2": "16 <= r <= 256",
        "interpretation": "Violation implies opposite-sign cancellation and/or omitted higher-order terms; it is not by itself a Candidate-Gravity consistency FAIL."
    },
    "guardrails": [
        "diagnostic only",
        "does not replace frozen Iteration-424 five-clause physical acceptance",
        "does not promote physical index 2",
        "does not create ANSATZ-003",
        "does not authorize Fisher/resources"
    ]
}

print(json.dumps(result, indent=2, sort_keys=True))
