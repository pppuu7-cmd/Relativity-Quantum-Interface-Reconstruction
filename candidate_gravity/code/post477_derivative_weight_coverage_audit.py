#!/usr/bin/env python3
"""Post-Iteration-477 derivative-weight coverage audit.

Collision-safe diagnostic only.  It measures how much of the frozen central4
mixed-derivative sensitivity has already received local MP certification under
the Iteration-455 source-order manifest.  It does NOT authorize support
reordering, deduplication, threshold changes, physical promotion, or skipping
HALF-level convergence closure.
"""
from fractions import Fraction
import json

c = [Fraction(1, 12), Fraction(-2, 3), Fraction(2, 3), Fraction(-1, 12)]
W = [[c[i] * c[j] for j in range(4)] for i in range(4)]

full_l1 = sum(abs(x) for row in W for x in row)
full_frob2 = sum(x * x for row in W for x in row)

# Current authority through Iteration 475 + pre-certified rank 10:
# Iteration-455 distinct BASE ranks 0..10 are certified; rank 11 is active.
current_base_ranks = set(range(0, 11))
prospective_base_ranks = set(range(0, 12))

# Exact BASE/HALF overlaps already certified at current front are the four
# coordinates (+/-5e-6,+/-5e-6), which are HALF corner nodes.
half_corner_indices = [(0, 0), (0, 3), (3, 0), (3, 3)]

def stats(ranks):
    ij = [(r // 4, r % 4) for r in sorted(ranks)]
    l1 = sum(abs(W[i][j]) for i, j in ij)
    f2 = sum(W[i][j] * W[i][j] for i, j in ij)
    return {
        "l1_weight": str(l1),
        "l1_fraction": str(l1 / full_l1),
        "l1_percent": float(100 * l1 / full_l1),
        "frob2_weight": str(f2),
        "frob2_fraction": str(f2 / full_frob2),
        "frob2_percent": float(100 * f2 / full_frob2),
    }

half_l1 = sum(abs(W[i][j]) for i, j in half_corner_indices)
half_f2 = sum(W[i][j] * W[i][j] for i, j in half_corner_indices)

result = {
    "classification": "PASS_BASE_DERIVATIVE_SENSITIVITY_WEIGHT_COVERAGE_AUDIT__DIAGNOSTIC_ONLY_NON_PROMOTING",
    "scientific_gate_pass": True,
    "promotes_physical_coordinate": False,
    "authority_anchor": "Iteration 477 current front; Iteration 475 latest completed mass-support authority",
    "active_run": {"run_id": 33989317870, "distinct_rank": 11, "u": 5e-6, "v": 1e-5},
    "central4": {
        "c": [str(x) for x in c],
        "sum_abs_weights": str(full_l1),
        "frob2_total": str(full_frob2),
    },
    "current": {
        "certified_occurrence_coverage": "15/32",
        "certified_occurrence_percent": 46.875,
        "certified_distinct_coordinates": "11/28",
        "base_ranks_certified": list(range(0, 11)),
        "base_sensitivity": stats(current_base_ranks),
        "half_overlap_only": {
            "description": "four exact BASE/HALF overlap coordinates at HALF corners",
            "l1_weight": str(half_l1),
            "l1_fraction": str(half_l1 / full_l1),
            "l1_percent": float(100 * half_l1 / full_l1),
            "frob2_weight": str(half_f2),
            "frob2_fraction": str(half_f2 / full_frob2),
            "frob2_percent": float(100 * half_f2 / full_frob2),
        },
    },
    "if_active_rank11_passes": {
        "certified_occurrence_coverage": "16/32",
        "certified_occurrence_percent": 50.0,
        "certified_distinct_coordinates": "12/28",
        "base_ranks_certified": list(range(0, 12)),
        "base_sensitivity": stats(prospective_base_ranks),
        "half_overlap_unchanged": True,
    },
    "interpretation": [
        "Occurrence coverage is not a derivative-sensitivity metric.",
        "The BASE stencil is already mostly covered in derivative-sensitive weight even though total occurrence coverage is below one half.",
        "The HALF stencil remains largely uncertified in derivative-sensitive weight, so BASE-vs-HALF convergence closure is still open.",
        "These weights are diagnostic only and cannot reorder the frozen Iteration-455 queue or substitute for local MP certification.",
    ],
    "guardrails": [
        "NO_SUPPORT_REORDERING",
        "NO_UV_SWAP_DEDUPLICATION",
        "NO_SKIPPING_UNTESTED_COORDINATES",
        "NO_THRESHOLD_CHANGE",
        "NO_LOCAL_PASS_ASSEMBLY_SUBSTITUTION",
        "NO_PHYSICAL_DS_PROMOTION",
        "NO_ANSATZ003",
        "NO_FISHER_RESOURCES",
    ],
    "MODEL_READINESS": "24%",
    "readiness_change_pp": 0,
}

assert full_l1 == Fraction(9, 4)
assert full_frob2 == Fraction(4225, 5184)
assert stats(current_base_ranks)["l1_fraction"] == "149/162"
assert stats(current_base_ranks)["frob2_fraction"] == "8353/8450"
assert stats(prospective_base_ranks)["l1_fraction"] == "17/18"
assert stats(prospective_base_ranks)["frob2_fraction"] == "129/130"
assert half_l1 / full_l1 == Fraction(1, 81)
assert half_f2 / full_frob2 == Fraction(1, 4225)

print(json.dumps(result, indent=2, sort_keys=True))
