#!/usr/bin/env python3
"""Fail-closed assembly of committed raw-audited Iteration-381 chunks.

No physics recomputation. Exact 0..35 simple-double coverage is mandatory and
any BLOCKED channel blocks the corresponding/full assembly; no zero filling.
"""
from __future__ import annotations
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
R=ROOT/'candidate_gravity'/'results'
files=sorted(R.glob('iteration381_tru1sq_simple_double_chunk_*.json'))
if len(files)!=12:
    raise SystemExit(f'BLOCKED_INCOMPLETE_CHUNK_SET:{len(files)}/12')
rows=[]
for p in files:
    o=json.loads(p.read_text())
    assert o['iteration']==381 and o['scientific_gate_pass'] is True
    assert len(o['channels'])==3
    start=int(o['chunk']['start_inclusive']); end=int(o['chunk']['end_exclusive'])
    assert end-start==3
    got=[r['global_simple_double_index'] for r in o['channels']]
    assert got==list(range(start,end))
    rows.extend(o['channels'])
ids=[r['global_simple_double_index'] for r in rows]
if sorted(ids)!=list(range(36)) or any(v!=1 for v in Counter(ids).values()):
    raise SystemExit('BLOCKED_INDEX_COVERAGE_NOT_EXACT_0_TO_35_ONCE')
blocked=[r for r in rows if r['status']!='CONVERGED']
if blocked:
    raise SystemExit('BLOCKED_NONCONVERGED_CHANNELS:'+','.join(str(r['global_simple_double_index']) for r in blocked))

buckets=defaultdict(float); counts=defaultdict(int)
for r in rows:
    q=min((-1.0,-0.34,-0.14),key=lambda x:abs(x-float(r['q_squared'])))
    assert abs(q-float(r['q_squared']))<1e-12
    z=r['D_s_TrU1sq_simple_double_channel']; assert abs(float(z[1]))<1e-14
    buckets[q]+=float(z[0]); counts[q]+=1
assert sum(counts.values())==36
out={
 'iteration':381,
 'assembly_type':'FULL36_ACCEPTED_RAW_CHUNKS_FAIL_CLOSED',
 'scientific_gate_pass':True,
 'model_readiness_percent':24,
 'exact_index_coverage':[min(ids),max(ids),len(set(ids))],
 'channel_count_by_q2':{str(q):counts[q] for q in sorted(counts)},
 'D_s_TrU1sq_simple_double_sum_by_q2':{str(q):[buckets[q],0.0] for q in sorted(buckets)},
 'all_channels_converged':True,
 'effective_action_weight':'NOT_FOLDED__MINUS_I_OVER_4_TRU1SQ_SEPARATE',
 'guardrails':['DISTINCT_Q2_COORDINATES_NOT_SUMMED','NO_ZERO_FILL','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'combine with ordinary-simple Iteration374 and the still-required double-double sector only after each origin is complete; apply -i/4 only at the complete TrU1sq/e=2 assembly stage'
}
print(json.dumps(out,indent=2,sort_keys=True))
