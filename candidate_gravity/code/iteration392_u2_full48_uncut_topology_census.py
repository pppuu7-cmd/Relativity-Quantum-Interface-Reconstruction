#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 392.

Topology-only census of the exact frozen Iteration-359 ordering of all 48
cut-through-repeated-pole Tr U2 channels.  No physical integration is rerun.

Purpose: prospectively distinguish channels whose cut exhausts every distinct
propagator momentum group (hence there is *no* uncut denominator and an empty
minimum is represented by +Infinity) from channels that must retain a finite,
positive uncut-denominator separation test.
"""
from __future__ import annotations
import contextlib, io, json, runpy
from collections import Counter, defaultdict
from pathlib import Path

ITERATION = 392
ROOT = Path(__file__).resolve().parent

with contextlib.redirect_stdout(io.StringIO()):
    p359 = runpy.run_path(str(ROOT / 'iteration359_u2_repeated_pole_derivative_contract.py'),
                          run_name='iteration392_parent359')
parent = p359['result']
if not parent.get('scientific_gate_pass'):
    raise RuntimeError('iteration359_parent_not_authoritative')

channels = []
for fam in parent['families']:
    groups = fam['groups']
    for ch in fam['timelike_distinct_group_channels']:
        if not ch['repeated_pole_reduction_required']:
            continue
        idx = len(channels)
        pair = [int(x) for x in ch['group_pair']]
        uncut = [g for g in range(len(groups)) if g not in set(pair)]
        channels.append({
            'global_channel_index': idx,
            'route': int(fam['route']),
            'subterm': int(fam['subterm']),
            'q2': float(ch['q2']),
            'group_pair': pair,
            'multiplicity_pair': [int(x) for x in ch['multiplicity_pair']],
            'denominator_group_count': int(len(groups)),
            'uncut_group_indices': uncut,
            'uncut_group_count': int(len(uncut)),
            'topology_no_uncut_denominator': bool(len(uncut) == 0),
            'required_minimum_uncut_policy': ('EMPTY_SET_POSITIVE_INFINITY_SENTINEL'
                                                if len(uncut) == 0 else
                                                'FINITE_POSITIVE_SEPARATION_REQUIRED'),
        })

q2_counts = Counter()
q2_no_uncut = Counter()
group_count_census = Counter()
mult_pair_census = Counter()
indices_no_uncut = []
for r in channels:
    qkey = f"{r['q2']:.12g}"
    q2_counts[qkey] += 1
    if r['topology_no_uncut_denominator']:
        q2_no_uncut[qkey] += 1
        indices_no_uncut.append(r['global_channel_index'])
    group_count_census[str(r['denominator_group_count'])] += 1
    mult_pair_census[str(tuple(r['multiplicity_pair']))] += 1

# Structural theorem used by the wrappers: because a channel cuts two distinct
# momentum groups, there is no uncut denominator iff the family has exactly two
# distinct groups.  This is checked route-by-route, not assumed.
structural_equivalence = all(
    r['topology_no_uncut_denominator'] == (r['denominator_group_count'] == 2)
    for r in channels
)
all_pairs_valid = all(
    len(set(r['group_pair'])) == 2 and
    min(r['group_pair']) >= 0 and
    max(r['group_pair']) < r['denominator_group_count']
    for r in channels
)
pass_gate = bool(
    len(channels) == 48 and structural_equivalence and all_pairs_valid and
    sum(q2_counts.values()) == 48 and len(indices_no_uncut) > 0
)

result = {
    'iteration': ITERATION,
    'model_readiness_percent': 24,
    'scientific_gate_pass': pass_gate,
    'candidate_residual': False,
    'classification': ('PASS_U2_FULL48_UNCUT_TOPOLOGY_CENSUS__EMPTY_INFINITY_SENTINEL_EXACTLY_WHEN_NO_UNCUT_GROUP'
                       if pass_gate else
                       'FAIL_U2_FULL48_UNCUT_TOPOLOGY_CENSUS'),
    'parent_authority': 'Iteration359 exact repeated-cut channel ordering',
    'census': {
        'total_repeated_cut_channels': len(channels),
        'q2_channel_counts': dict(sorted(q2_counts.items())),
        'q2_no_uncut_counts': dict(sorted(q2_no_uncut.items())),
        'denominator_group_count_census': dict(sorted(group_count_census.items())),
        'multiplicity_pair_census': dict(sorted(mult_pair_census.items())),
        'no_uncut_channel_count': len(indices_no_uncut),
        'finite_uncut_required_channel_count': len(channels) - len(indices_no_uncut),
        'no_uncut_global_channel_indices': indices_no_uncut,
        'structural_equivalence_no_uncut_iff_two_groups': structural_equivalence,
    },
    'channels': channels,
    'scope': 'TOPOLOGY_ONLY__NO_PHYSICAL_REINTEGRATION__NO_DISCONTINUITY_REASSEMBLY',
    'guardrails': [
        'ITERATION359_ORDERING_BINDING',
        'NO_THRESHOLD_WEAKENING',
        'INFINITY_ALLOWED_ONLY_FOR_EMPTY_UNCUT_GROUP_SET',
        'FINITE_UNCUT_CHANNELS_STILL_REQUIRE_POSITIVE_SEPARATION',
        'BLOCKED_NEVER_ZERO_FILLED',
        'DISTINCT_Q2_BUCKETS_NEVER_SUMMED',
        'NO_EFFECTIVE_ACTION_WEIGHT_FOLDING',
        'NO_SOURCE_BORN_SUBTRACTION',
        'NO_ANSATZ003',
        'NO_FISHER_RESOURCES',
    ],
    'next_gate': ('apply this immutable topology mask when validating recovered Iteration384/390 raw chunks; '
                  'only after exact indices 0..47 are each scientifically resolved may q2-resolved repeated TrU2 sums be assembled'),
}
print(json.dumps(result, indent=2, sort_keys=True))
if not pass_gate:
    raise SystemExit(2)
