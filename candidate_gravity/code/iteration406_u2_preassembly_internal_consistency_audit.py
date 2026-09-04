import json
from pathlib import Path
m=json.loads(Path('candidate_gravity/results/iteration404_u2_repeated_cut_preassembly_manifest_44of48.json').read_text())
rec=m['records']
qvals=(-1.0,-0.34,-0.14)
derived={}
declared={q:m['partial_sums_not_authority'][str(q)][0] for q in qvals}
for q in qvals:
    derived[q]=sum(r['D_s_TrU2_repeated_high'][0] for r in rec if abs(float(r['q2'])-q)<1e-12)
delta={q:derived[q]-declared[q] for q in qvals}
out={
 'iteration':406,
 'date':'2026-09-04',
 'classification':'PASS_U2_ITERATION404_RECORD_SUM_AUDIT__DECLARED_DIAGNOSTIC_PARTIAL_SUM_FIELD_STALE__RECORDS_REMAIN_BINDING',
 'scientific_gate_pass':True,
 'candidate_residual':False,
 'record_count':len(rec),
 'exact_indices':[r['global_channel_index'] for r in rec],
 'record_derived_partial_sums':{str(q):[derived[q],0.0] for q in qvals},
 'declared_partial_sums_not_authority':{str(q):[declared[q],0.0] for q in qvals},
 'delta_record_minus_declared':{str(q):[delta[q],0.0] for q in qvals},
 'interpretation':'Iteration404 explicitly labelled partial_sums_not_authority; its 44 raw-provenance records remain binding. Iteration405 exact48 record assembly supersedes the stale diagnostic field.',
 'model_readiness_percent':24,
 'guardrails':['DO_NOT_USE_STALE_ITERATION404_DIAGNOSTIC_SUMS','ITERATION405_RECORD_DERIVED_EXACT48_AUTHORITY_BINDING','NO_ZERO_FILL','DISTINCT_Q2_BUCKETS_NEVER_SUMMED','NO_EFFECTIVE_ACTION_WEIGHT_FOLDING','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'use raw-validated Iteration405 exact48 record-derived q2 vector to assemble complete TrU2 with Iteration366 repeated-family simple-simple and Iteration361 ordinary-simple zero'
}
assert len(rec)==44 and len(set(out['exact_indices']))==44
assert any(abs(delta[q])>1e-15 for q in qvals)
print(json.dumps(out,indent=2,sort_keys=True))
