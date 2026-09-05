#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 481.

Exact deterministic audit of the frozen Iteration-455 support-manifest tail after
raw-valid rank 11. Provenance/queue result only: no F(u,v) evaluation, no
threshold/dynamics change, no physical promotion.
"""
from collections import Counter
import json

BASE_H = 5e-6
HALF_H = 2.5e-6

def nodes(h):
    return [-2*h, -h, h, 2*h]

base = [(u, v) for u in nodes(BASE_H) for v in nodes(BASE_H)]
half = [(u, v) for u in nodes(HALF_H) for v in nodes(HALF_H)]
occurrences = [('BASE', i, p) for i, p in enumerate(base)] + [('HALF', i, p) for i, p in enumerate(half)]
counts = Counter(p for _, _, p in occurrences)
first_order = []
for _, _, p in occurrences:
    if p not in first_order:
        first_order.append(p)

assert len(occurrences) == 32
assert len(first_order) == 28
assert first_order[11] == (5e-6, 1e-5)
assert first_order[12] == (1e-5, -1e-5)
assert counts[first_order[12]] == 1

remaining = first_order[12:]
assert len(remaining) == 16
assert all(counts[p] == 1 for p in remaining)
assert first_order[12:16] == [(1e-5,-1e-5),(1e-5,-5e-6),(1e-5,5e-6),(1e-5,1e-5)]
assert all(p in base for p in first_order[:16])
assert all(p in half and p not in base for p in first_order[16:])

result = {
    'iteration': 481,
    'classification': 'PASS_FROZEN_MANIFEST_TAIL_EXACT_RECONSTRUCTION__NON_PROMOTING',
    'scientific_gate_pass': True,
    'promotes_physical_coordinate': False,
    'MODEL_READINESS': '24%',
    'readiness_change_pp': 0,
    'frozen': {
        'base_h': BASE_H,
        'half_h': HALF_H,
        'source_order': 'BASE 4x4 u-major/v-major, then HALF 4x4 u-major/v-major',
        'occurrence_count': 32,
        'distinct_coordinate_count': 28,
        'raw_valid_through_rank': 11,
        'certified_occurrence_weight_through_rank11': 16,
    },
    'audit': {
        'next_exact_unresolved': {'distinct_rank': 12, 'u': 1e-5, 'v': -1e-5, 'multiplicity': 1},
        'remaining_distinct_count_after_rank11': 16,
        'remaining_occurrence_weight_after_rank11': 16,
        'all_remaining_multiplicity_one': True,
        'coverage_increment_per_remaining_coordinate_fraction': '1/32',
        'coverage_increment_per_remaining_coordinate_percent': 3.125,
        'base_manifest_ranks': [0, 15],
        'half_exclusive_manifest_ranks': [16, 27],
        'remaining_base_only_ranks_after_rank11': [12, 13, 14, 15],
        'half_exclusive_tail_ranks': [16, 27],
        'remaining_manifest': [
            {'distinct_rank': i, 'u': p[0], 'v': p[1], 'multiplicity': counts[p],
             'support_scope': ('BASE' if i <= 15 else 'HALF_EXCLUSIVE')}
            for i, p in enumerate(first_order) if i >= 12
        ],
    },
    'guardrails': [
        'NO_UV_SWAP_INFERENCE',
        'NO_CERTIFIED_RANK_RELAUNCH',
        'NO_EARLY_ASSEMBLY_PROMOTION',
        'NO_THRESHOLD_CHANGE',
        'NO_PHYSICAL_DS_PROMOTION',
        'NO_ANSATZ003',
        'NO_FISHER_RESOURCES',
    ],
    'next_gate': 'raw-consume canonical rank12 run 33997856739 fail-closed; only on PASS advance to frozen manifest rank13 (+1e-5,-5e-6)'
}
print(json.dumps(result, indent=2, sort_keys=True))
