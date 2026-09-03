#!/usr/bin/env python3
"""Fail-closed assembly contract for Iteration 384 accepted raw chunk authorities.

This script does no physics recomputation. It reads only committed, individually
raw-audited Iteration-384 two-channel result files and refuses to assemble a q2
coordinate unless all 48 global indices occur exactly once and every channel is
CONVERGED under one identical frozen arithmetic contract.
"""
from __future__ import annotations
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
R=ROOT/'candidate_gravity'/'results'
files=sorted(R.glob('iteration384_u2_repeated_cut_chunk_*.json'))
if len(files)!=24:
    raise SystemExit(f'BLOCKED_INCOMPLETE_CHUNK_SET:{len(files)}/24')

rows=[]; arithmetic=None; chunks=[]
for p in files:
    o=json.loads(p.read_text())
    assert o['iteration']==384 and o['scientific_gate_pass'] is True
    assert o['classification']=='PASS_U2_REPEATED_CUT_FULL48_TWO_CHANNEL_CHUNK_EXECUTION'
    if arithmetic is None: arithmetic=o['frozen_arithmetic']
    assert o['frozen_arithmetic']==arithmetic
    assert len(o['records'])==2
    exp=o['chunk']['expected_indices']
    got=[r['global_channel_index'] for r in o['records']]
    assert got==exp and len(exp)==2
    chunks.append(tuple(exp))
    rows.extend(o['records'])

ids=[r['global_channel_index'] for r in rows]
if sorted(ids)!=list(range(48)) or any(v!=1 for v in Counter(ids).values()):
    raise SystemExit('BLOCKED_INDEX_COVERAGE_NOT_EXACT_0_TO_47_ONCE')
blocked=[r for r in rows if r['status']!='CONVERGED']
if blocked:
    raise SystemExit('BLOCKED_NONCONVERGED_CHANNELS:'+','.join(str(r['global_channel_index']) for r in blocked))

buckets=defaultdict(float); counts=defaultdict(int)
for r in rows:
    q=min((-1.0,-0.34,-0.14), key=lambda x:abs(x-float(r['q2'])))
    assert abs(q-float(r['q2']))<1e-12
    val=r['D_s_TrU2_repeated_high']
    assert abs(float(val[1]))<1e-14
    buckets[q]+=float(val[0]); counts[q]+=1
assert sum(counts.values())==48

out={
 'iteration':384,
 'assembly_type':'FULL48_ACCEPTED_RAW_CHUNKS_FAIL_CLOSED',
 'scientific_gate_pass':True,
 'model_readiness_percent':24,
 'exact_index_coverage':ids and [min(ids),max(ids),len(set(ids))],
 'channel_count_by_q2':{str(q):counts[q] for q in sorted(counts)},
 'D_s_TrU2_repeated_sum_by_q2':{str(q):[buckets[q],0.0] for q in sorted(buckets)},
 'all_channels_converged':True,
 'frozen_arithmetic':arithmetic,
 'guardrails':['NO_EFFECTIVE_ACTION_WEIGHT_FOLDED','DISTINCT_Q2_COORDINATES_NOT_SUMMED','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'combine with already-frozen ordinary/simple-family TrU2 origins q2-by-q2 only after preserving their provenance; then apply +i/2 only at the complete TrU2/e=2 assembly stage'
}
print(json.dumps(out,indent=2,sort_keys=True))
