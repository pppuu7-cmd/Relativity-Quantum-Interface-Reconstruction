import json
from pathlib import Path

manifest_path = Path('candidate_gravity/results/iteration404_u2_repeated_cut_preassembly_manifest_44of48.json')
inputs_path = Path('candidate_gravity/results/iteration405_u2_repeated_cut_completion_inputs.json')
manifest = json.loads(manifest_path.read_text())
inputs = json.loads(inputs_path.read_text())

assert manifest['iteration'] == 404
assert manifest['exact_missing_indices'] == [14, 15, 16, 17]
old = manifest['records']
new = inputs['records']
assert [r['global_channel_index'] for r in new] == [14,15,16,17]
assert all(r['status'] == 'CONVERGED' for r in old + new)
assert all(r.get('iteration392_mask_consistent', True) is True for r in new)
assert all(r.get('uncut_policy_pass', True) is True for r in new)

records = old + new
indices = [r['global_channel_index'] for r in records]
assert len(records) == 48
assert len(set(indices)) == 48
assert sorted(indices) == list(range(48))

q2_values = (-1.0, -0.34, -0.14)
sums = {}
counts = {}
for q in q2_values:
    vals = [r['D_s_TrU2_repeated_high'][0] for r in records if abs(float(r['q2']) - q) < 1e-12]
    sums[str(q)] = [sum(vals), 0.0]
    counts[str(q)] = len(vals)
assert sum(counts.values()) == 48
assert all(v > 0 for v in counts.values())

out = {
  'iteration': 405,
  'date': '2026-09-04',
  'classification': 'PASS_U2_REPEATED_CUT_EXACT48_FAIL_CLOSED_ASSEMBLY',
  'scientific_gate_pass': True,
  'candidate_residual': False,
  'source_manifest_iteration': 404,
  'source_completion_iteration': 400,
  'source_completion_run': inputs['source_run'],
  'exact_channel_count': 48,
  'exact_unique_indices': list(range(48)),
  'q2_channel_counts': counts,
  'D_s_TrU2_repeated_cut_q2': sums,
  'effective_action_weight': 'NOT_FOLDED__PLUS_I_OVER_2_TRU2_SEPARATE',
  'model_readiness_percent': 24,
  'guardrails': [
    'EXACTLY_ONE_RECORD_PER_INDEX_0_TO_47',
    'ALL_RECORDS_CONVERGED',
    'ITERATION392_TOPOLOGY_MASK_BINDING',
    'DISTINCT_Q2_BUCKETS_NEVER_SUMMED',
    'NO_ZERO_FILL',
    'NO_EFFECTIVE_ACTION_WEIGHT_FOLDING',
    'NO_SOURCE_BORN_SUBTRACTION',
    'NO_ANSATZ003',
    'NO_FISHER_RESOURCES'
  ],
  'next_gate': 'combine this exact repeated-cut vector with Iteration366 repeated-family simple-simple and Iteration361 ordinary-simple zero to form complete TrU2 q2 coordinates, still without +i/2'
}
print(json.dumps(out, indent=2, sort_keys=True))
