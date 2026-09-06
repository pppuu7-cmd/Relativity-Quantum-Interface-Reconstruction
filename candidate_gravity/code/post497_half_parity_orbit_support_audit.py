#!/usr/bin/env python3
from fractions import Fraction
import json

nodes = [-2, -1, 1, 2]
coeff = {
    -2: Fraction(1,12),
    -1: Fraction(-2,3),
    1: Fraction(2,3),
    2: Fraction(-1,12),
}

# Frozen Iteration-455 HALF local mapping: signed central4 node pair -> distinct rank.
half_rank = {
    (-2,-2): 5,  (-2,-1): 16, (-2,1): 17, (-2,2): 6,
    (-1,-2): 18, (-1,-1): 19, (-1,1): 20, (-1,2): 21,
    (1,-2): 22,  (1,-1): 23,  (1,1): 24,  (1,2): 25,
    (2,-2): 9,   (2,-1): 26,   (2,1): 27,   (2,2): 10,
}

certified = set(range(18))  # Iteration-497 snapshot; rank18 is active only.
active_rank = 18

orbits = []
all_orbit_ranks = []
for ax in (1,2):
    for ay in (1,2):
        coords = [(ax,ay), (-ax,ay), (ax,-ay), (-ax,-ay)]
        ranks = [half_rank[p] for p in coords]
        all_orbit_ranks.extend(ranks)
        weight = coeff[ax] * coeff[ay]
        certified_ranks = [r for r in ranks if r in certified]
        missing_ranks = [r for r in ranks if r not in certified]
        orbits.append({
            "abs_node_pair": [ax, ay],
            "orbit_difference_order": ["F(+,+)", "F(-,+)", "F(+,-)", "F(-,-)"],
            "signed_coordinates": [list(p) for p in coords],
            "distinct_ranks": ranks,
            "orbit_coefficient_before_h2": str(weight),
            "coefficient_nonzero": weight != 0,
            "certified_ranks": certified_ranks,
            "missing_ranks": missing_ranks,
            "complete": len(missing_ranks) == 0,
        })

assert sorted(all_orbit_ranks) == sorted([5,16,17,6,18,19,20,21,22,23,24,25,9,26,27,10])
assert len(set(all_orbit_ranks)) == 16
assert all(o["coefficient_nonzero"] for o in orbits)

by_pair = {tuple(o["abs_node_pair"]): o for o in orbits}
assert by_pair[(2,2)]["distinct_ranks"] == [10,6,9,5]
assert by_pair[(2,2)]["complete"] is True
assert sorted(by_pair[(2,1)]["certified_ranks"]) == [16,17]
assert sorted(by_pair[(1,2)]["missing_ranks"]) == [18,21,22,25]
assert sorted(by_pair[(1,1)]["missing_ranks"]) == [19,20,23,24]

remaining = sorted(set(range(18,28)))
covered_by_incomplete_orbits = sorted({r for o in orbits if not o["complete"] for r in o["missing_ranks"]})
assert covered_by_incomplete_orbits == remaining
assert active_rank in covered_by_incomplete_orbits

result = {
    "stage": "POST497_HALF_PARITY_ORBIT_SUPPORT_NOSKIP_AUDIT",
    "classification": "PASS_PARITY_PROJECTION_REDUCES_FORM_NOT_REQUIRED_SUPPORT__NON_PROMOTING",
    "scientific_gate_pass": True,
    "promotes_physical_coordinate": False,
    "MODEL_READINESS": "24%",
    "readiness_change_pp": 0,
    "iteration497_snapshot": {
        "certified_distinct_ranks": list(range(18)),
        "active_rank": active_rank,
        "remaining_half_exclusive_ranks": remaining,
    },
    "parity_orbits": orbits,
    "exact_conclusion": {
        "complete_orbit_count": sum(o["complete"] for o in orbits),
        "total_orbit_count": 4,
        "all_orbit_coefficients_nonzero": True,
        "all_remaining_ranks_18_to_27_are_required_by_incomplete_orbits": covered_by_incomplete_orbits == remaining,
        "remaining_required_ranks": covered_by_incomplete_orbits,
    },
    "interpretation": [
        "Iteration-497 odd-odd parity projection reduces the 16-sample HALF assembly to four orbit differences, but every orbit coefficient is exactly nonzero: 4/9, -1/18, -1/18, 1/144 before the common 1/h^2 factor.",
        "At the Iteration-497 support snapshot only the outer-outer |x|=2,|y|=2 orbit is complete, using the four exact BASE/HALF overlap ranks 5,6,9,10.",
        "The outer-inner orbit is only half complete (ranks 16,17 certified; 26,27 missing), while the two inner-containing orbits remain incomplete.",
        "Every remaining rank 18..27 appears in an incomplete orbit with nonzero coefficient. Therefore parity projection provides an exact assembly/checksum reduction but does not authorize skipping any remaining HALF support coordinate without an additional independently frozen field symmetry identity.",
        "Frozen manifest order remains controlling; rank18 stays the sole active heavy gate and PASS would authorize only rank19 next."
    ],
    "guardrails": [
        "NO_PARITY_BASED_SUPPORT_SKIPPING",
        "NO_ZERO_FILL",
        "NO_UV_SWAP_DEDUPLICATION",
        "NO_SUPPORT_REORDERING",
        "NO_UNFROZEN_FIELD_SYMMETRY_ASSUMPTION",
        "NO_THRESHOLD_CHANGE",
        "NO_PHYSICAL_DS_PROMOTION",
        "NO_ANSATZ003",
        "NO_FISHER_RESOURCES"
    ]
}

print(json.dumps(result, indent=2, sort_keys=True))
