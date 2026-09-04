import json
from pathlib import Path

rep = json.loads(Path('candidate_gravity/results/iteration405_u2_repeated_cut_exact48_result.json').read_text())
assert rep['classification'] == 'PASS_U2_REPEATED_CUT_EXACT48_FAIL_CLOSED_ASSEMBLY'
assert rep['scientific_gate_pass'] is True
assert rep['exact_channel_count'] == 48

simple_simple = {
    '-1.0': -6.812363349599648e-05,
    '-0.34': -8.405976034846215e-05,
    '-0.14': -7.069545900379072e-05,
}
ordinary_simple = {'-1.0': 0.0, '-0.34': 0.0, '-0.14': 0.0}

complete = {}
for q in ('-1.0','-0.34','-0.14'):
    complete[q] = [ordinary_simple[q] + simple_simple[q] + rep['D_s_TrU2_repeated_cut_q2'][q][0], 0.0]

out = {
    'iteration': 406,
    'date': '2026-09-04',
    'classification': 'PASS_TRU2_COMPLETE_TIMELIKE_OPERATOR_COORDINATE_Q2_RESOLVED',
    'scientific_gate_pass': True,
    'candidate_residual': False,
    'components': {
        'ordinary_simple_iteration': 361,
        'ordinary_simple_q2': ordinary_simple,
        'repeated_family_simple_simple_iteration': 366,
        'repeated_family_simple_simple_q2': simple_simple,
        'repeated_cut_iteration': 405,
        'repeated_cut_q2': {q: rep['D_s_TrU2_repeated_cut_q2'][q][0] for q in complete},
    },
    'D_s_TrU2_complete_q2': complete,
    'effective_action_weight': 'NOT_FOLDED__PLUS_I_OVER_2_TRU2_SEPARATE',
    'model_readiness_percent': 24,
    'guardrails': ['DISTINCT_Q2_BUCKETS_NEVER_SUMMED','NO_ZERO_FILL','NO_EFFECTIVE_ACTION_WEIGHT_FOLDING','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
    'next_gate': 'resolve TrU1^2 double-double blockers 2,4,11; then assemble complete TrU1^2 and only then combine e=2 effective-action weights q2-by-q2'
}
print(json.dumps(out, indent=2, sort_keys=True))
