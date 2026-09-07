#!/usr/bin/env python3
"""Iteration 563: exact post-rank10 two-point QUARTER tail contract."""
from fractions import Fraction
import json

# Frozen Iteration-424 / Iteration-532 central4 conventions.
nodes = (-2, -1, 1, 2)
w = (1, -8, 8, -1)
coeff = {(u, v): w[i] * w[j] for i, u in enumerate(nodes) for j, v in enumerate(nodes)}

# After raw-valid rank10, all QUARTER coordinates except ranks 11 and 12 are known.
rank11 = (2, -1)
rank12 = (2, 1)
assert coeff[rank11] == 8
assert coeff[rank12] == -8
assert coeff[rank11] + coeff[rank12] == 0

# Mixed derivative normalization is 1/(144 h^2).
c11 = Fraction(coeff[rank11], 144)
c12 = Fraction(coeff[rank12], 144)
assert c11 == Fraction(1, 18)
assert c12 == Fraction(-1, 18)

# If Delta = F11-F12, the complete unknown tail is Delta/(18 h^2).
# If d=(F11-F12)/2, tail=d/(9 h^2); common mode m=(F11+F12)/2 cancels exactly.
common_mode = c11 + c12
differential_mode_for_half_difference = c11 - c12
assert common_mode == 0
assert differential_mode_for_half_difference == Fraction(1, 9)

# Independent equal-variance coordinate errors e11,e12 with Var=sigma^2.
variance_factor = c11 * c11 + c12 * c12  # multiplying sigma^2/h^4
assert variance_factor == Fraction(1, 162)

result = {
    "schema": "rqir_iter424_post_rank10_two_point_tail_exact_v1",
    "iteration": 563,
    "date": "2026-09-08",
    "classification": "PASS_ITER424_POST_RANK10_TWO_POINT_TAIL_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING",
    "scope": "prospective exact assembly/error contract after raw-valid QUARTER rank10",
    "frozen": {
        "nodes_scaled": list(nodes),
        "central4_integer_weights": list(w),
        "mixed_normalization": "1/(144 h^2)",
        "remaining_after_rank10": {
            "rank11": {"scaled_coordinate": [2, -1], "integer_coefficient": 8},
            "rank12": {"scaled_coordinate": [2, 1], "integer_coefficient": -8},
        },
    },
    "exact": {
        "tail": "[F(+2h,-h)-F(+2h,+h)]/(18 h^2)",
        "common_mode_coefficient": "0",
        "half_difference_mode_coefficient": "1/(9 h^2)",
        "rank11_normalized_coefficient": "1/(18 h^2)",
        "rank12_normalized_coefficient": "-1/(18 h^2)",
        "independent_equal_variance_factor": "1/(162 h^4)",
        "independent_equal_sigma_std": "sigma/(9 sqrt(2) h^2)",
        "bounded_error": "|delta tail| <= (eps11+eps12)/(18 h^2)",
    },
    "conclusions": {
        "remaining_unknown_support_dimension_after_rank10": 2,
        "remaining_unknown_assembly_mode_dimension": 1,
        "common_offset_between_rank11_rank12_cancels_exactly": True,
        "rank_skipping_authorized": False,
        "uv_substitution_authorized": False,
        "physical_index2_promoted": False,
        "ansatz003_authorized": False,
        "fisher_resources_authorized": False,
    },
    "MODEL_READINESS": "24%",
    "readiness_change_pp": 0,
}
print(json.dumps(result, indent=2, sort_keys=True))
