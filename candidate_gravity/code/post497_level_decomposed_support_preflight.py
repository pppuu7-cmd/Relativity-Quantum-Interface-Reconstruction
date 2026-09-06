#!/usr/bin/env python3
import json

# Frozen Iteration-455 source-occurrence mapping, represented by distinct rank.
BASE_RANK_MATRIX = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15],
]
HALF_RANK_MATRIX = [
    [5, 16, 17, 6],
    [18, 19, 20, 21],
    [22, 23, 24, 25],
    [9, 26, 27, 10],
]

# Iteration-497 snapshot: Iteration-496 raw authority certifies rank17 and all
# earlier manifest ranks are retained certified. Rank18 is active, not certified.
CERTIFIED_DISTINCT_RANKS = set(range(18))
ACTIVE_RANK = 18

base = [r for row in BASE_RANK_MATRIX for r in row]
half = [r for row in HALF_RANK_MATRIX for r in row]
shared = sorted(set(base) & set(half))
union = sorted(set(base) | set(half))

assert base == list(range(16))
assert half == [5,16,17,6,18,19,20,21,22,23,24,25,9,26,27,10]
assert shared == [5, 6, 9, 10]
assert union == list(range(28))
assert len(base) == 16 and len(set(base)) == 16
assert len(half) == 16 and len(set(half)) == 16
assert len(union) == 28

base_certified = [r for r in base if r in CERTIFIED_DISTINCT_RANKS]
half_certified = [r for r in half if r in CERTIFIED_DISTINCT_RANKS]
base_missing = [r for r in base if r not in CERTIFIED_DISTINCT_RANKS]
half_missing = [r for r in half if r not in CERTIFIED_DISTINCT_RANKS]

assert base_certified == list(range(16))
assert base_missing == []
assert half_certified == [5,16,17,6,9,10]
assert half_missing == [18,19,20,21,22,23,24,25,26,27]
assert ACTIVE_RANK == half_missing[0]

occurrence_certified = len(base_certified) + len(half_certified)
distinct_certified = len(CERTIFIED_DISTINCT_RANKS)
assert occurrence_certified == 22
assert distinct_certified == 18

result = {
    "stage": "POST497_LEVEL_DECOMPOSED_SUPPORT_AND_ASSEMBLY_MAPPING_PREFLIGHT",
    "classification": "PASS_LEVEL_DECOMPOSED_SUPPORT_AND_ASSEMBLY_MAPPING_PREFLIGHT__NON_PROMOTING",
    "scientific_gate_pass": True,
    "promotes_physical_coordinate": False,
    "MODEL_READINESS": "24%",
    "readiness_change_pp": 0,
    "frozen_mapping": {
        "base_rank_matrix_u_major_v_major": BASE_RANK_MATRIX,
        "half_rank_matrix_u_major_v_major": HALF_RANK_MATRIX,
        "shared_exact_coordinate_ranks": shared,
        "distinct_rank_union": union,
    },
    "iteration497_snapshot": {
        "certified_distinct_ranks": sorted(CERTIFIED_DISTINCT_RANKS),
        "active_rank": ACTIVE_RANK,
        "base_certified_positions": len(base_certified),
        "base_total_positions": 16,
        "base_local_support_fraction": "16/16 = 100%",
        "base_missing_ranks": base_missing,
        "half_certified_positions": len(half_certified),
        "half_total_positions": 16,
        "half_local_support_fraction": "6/16 = 37.5%",
        "half_certified_ranks_in_local_order": half_certified,
        "half_missing_ranks_in_local_order": half_missing,
        "distinct_coverage": "18/28 = 64.28571428571429%",
        "occurrence_weighted_coverage": "22/32 = 68.75%",
    },
    "if_rank18_raw_passes": {
        "half_local_support_fraction": "7/16 = 43.75%",
        "distinct_coverage": "19/28 = 67.85714285714286%",
        "occurrence_weighted_coverage": "23/32 = 71.875%",
        "next_allowed_rank": 19,
    },
    "interpretation": [
        "The aggregate 22/32 occurrence-weighted coverage hides a level asymmetry: BASE local support is already complete at 16/16, while HALF is only 6/16 at the Iteration-497 snapshot.",
        "Complete BASE local support does not authorize early numerical BASE assembly because the frozen contract defers independent BASE/HALF assembly until all 28 distinct support coordinates are locally certified.",
        "The exact BASE/HALF overlap is only ranks 5, 6, 9 and 10; those local precision certificates may be shared, but assembly weights and level identity remain distinct.",
        "The next missing HALF local position is exactly rank18, matching the sole active heavy gate. No support reorder, symmetry fill or zero-fill is permitted.",
    ],
    "guardrails": [
        "NO_EARLY_NUMERICAL_BASE_ASSEMBLY",
        "NO_ZERO_FILL",
        "NO_UV_SWAP_DEDUPLICATION",
        "NO_SUPPORT_REORDERING",
        "ONLY_EXACT_BASE_HALF_OVERLAPS_SHARE_LOCAL_CERTIFICATES",
        "LEVEL_SPECIFIC_ASSEMBLY_REMAINS_DISTINCT",
        "NO_THRESHOLD_CHANGE",
        "NO_PHYSICAL_DS_PROMOTION",
        "NO_ANSATZ003",
        "NO_FISHER_RESOURCES",
    ],
}

print(json.dumps(result, indent=2, sort_keys=True))
