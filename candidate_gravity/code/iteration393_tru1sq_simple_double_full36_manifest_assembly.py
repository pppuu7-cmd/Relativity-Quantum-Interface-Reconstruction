#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 393.

Fail-closed assembly of the complete Iteration-381 raw-manifest for all 36
physical Tr(U1^2) simple-double channels.  No physics is recomputed.  Exact
index coverage, q2 census, raw-chunk provenance count, CONVERGED/execution-valid
status, and all frozen numerical thresholds are required before q2 sums exist.
"""
from __future__ import annotations
import json, math
from collections import Counter, defaultdict
from pathlib import Path

ITERATION=393
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'candidate_gravity/results/iteration381_full36_raw_manifest.json'
m=json.loads(p.read_text())
rows=m['channels']; hashes=m['chunk_raw_sha256']
ids=[int(r['index']) for r in rows]
exact_indices=(sorted(ids)==list(range(36)) and len(set(ids))==36)
exact_chunks=(len(hashes)==12 and sorted(hashes)==[f'{i:02d}-{i+2:02d}' for i in range(0,36,3)])
all_converged=all(r['status']=='CONVERGED' and r['execution_valid'] is True for r in rows)
thresholds_ok=all(float(r['conv'])<=2e-5 and float(r['shell'])<=2e-10 and float(r['radial'])<=5e-4 and float(r['min_uncut'])>1e-10 for r in rows)
counts=Counter(round(float(r['q2']),12) for r in rows)
q2_census_ok=(counts==Counter({-1.0:12,-0.34:12,-0.14:12}))
buckets=defaultdict(float)
for r in rows:
    buckets[round(float(r['q2']),12)] += float(r['value'])
pass_gate=bool(m.get('source_iteration')==381 and m.get('source_run')==33816213900 and exact_indices and exact_chunks and all_converged and thresholds_ok and q2_census_ok)
out={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':pass_gate,'candidate_residual':False,
 'classification':('PASS_TRU1SQ_SIMPLE_DOUBLE_FULL36_RAW_MANIFEST_ASSEMBLY__ALL_CONVERGED' if pass_gate else 'FAIL_TRU1SQ_SIMPLE_DOUBLE_FULL36_RAW_MANIFEST_ASSEMBLY'),
 'source_iteration':381,'source_run':m.get('source_run'),'source_workflow_head':m.get('workflow_head'),
 'raw_chunk_sha256':hashes,'census':{'channel_count':len(rows),'unique_index_count':len(set(ids)),'exact_indices_0_to_35':exact_indices,
   'raw_chunk_count':len(hashes),'exact_12_chunk_provenance':exact_chunks,'all_channels_converged':all_converged,'all_thresholds_pass':thresholds_ok,
   'channel_count_by_q2':{str(k):counts[k] for k in sorted(counts)}},
 'numerical_envelope':{'max_scaled_convergence_error':max(float(r['conv']) for r in rows),
   'max_cut_shell_abs_error':max(float(r['shell']) for r in rows),'max_radial_richardson_scaled_error':max(float(r['radial']) for r in rows),
   'minimum_sampled_uncut_abs_denominator':min(float(r['min_uncut']) for r in rows)},
 'D_s_TrU1sq_simple_double_sum_by_q2':{str(q):[buckets[q],0.0] for q in sorted(buckets)} if pass_gate else None,
 'effective_action_weight':'NOT_FOLDED__MINUS_I_OVER_4_TRU1SQ_SEPARATE',
 'scope':'COMPLETE_36_CHANNEL_SIMPLE_DOUBLE_OPERATOR_COORDINATE_ONLY',
 'guardrails':['EXACT_RAW_MANIFEST_COVERAGE_REQUIRED','NO_ZERO_FILL','DISTINCT_Q2_COORDINATES_NOT_SUMMED','NO_EFFECTIVE_ACTION_WEIGHT_FOLDING',
   'NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'combine with Iteration374 simple-simple and complete Iteration389 double-double only after the 15-channel double-double operator coordinate is fully resolved; apply -i/4 only after complete TrU1sq closure'
}
print(json.dumps(out,indent=2,sort_keys=True))
if not pass_gate: raise SystemExit(2)
