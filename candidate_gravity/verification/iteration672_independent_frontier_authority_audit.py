#!/usr/bin/env python3
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[2]
fail=[]
req='candidate_gravity/results/iteration671_iter667_candidate_semantic_closure_authority.json'
q=R/req
if not q.exists(): fail.append('missing:'+req)
else:
 d=json.loads(q.read_text())
 if d.get('scientific_gate_pass') is not True: fail.append('nonpass:'+req)
 if d.get('soft_tcut_branch')!='PREREQUISITE_BLOCKED_NO_SAME_PARENT_CONCRETE_DETECTOR_GEOMETRY': fail.append('Iter671 blocker drift')
# Inventory recent authority/result JSONs carrying an explicit next gate. Exclude the now-frozen soft detector branch,
# forbidden stages, closed C5 e=3/null-soft work, weighted-B3 proxy reuse and blind heavy full-C5 directions.
exclude=re.compile(r'(soft[-_ ]?tcut|detector|source[-_ ]?born|ansatz[-_ ]?003|fisher|resource|full[-_ ]?c5|weighted[-_ ]?b3|\be=3\b|null[-_ ]?soft)',re.I)
cands=[]
for p in (R/'candidate_gravity/results').glob('*.json'):
 try: d=json.loads(p.read_text())
 except Exception: continue
 it=d.get('iteration')
 if not isinstance(it,int) or it>=672: continue
 nxt=d.get('exact_next_gate')
 if not isinstance(nxt,str) or not nxt.strip(): continue
 if exclude.search(nxt): continue
 cands.append({'iteration':it,'path':str(p.relative_to(R)),'classification':d.get('classification'),'blocked':d.get('blocked'),'scientific_gate_pass':d.get('scientific_gate_pass'),'exact_next_gate':nxt})
cands=sorted(cands,key=lambda x:x['iteration'],reverse=True)[:30]
# This gate is an authority-frontier inventory only: no candidate is auto-promoted from text.
out={'iteration':672,'date':'2026-09-09','MODEL_READINESS':'24%','scientific_gate_pass':not fail,'failures':fail,'blocked':not fail,
 'classification':('BLOCKED_ITER672_INDEPENDENT_FRONTIER_CANDIDATES_INVENTORIED__SEMANTIC_SELECTION_REQUIRED__NO_SOFT_TCUT_REOPEN__NON_RESIDUAL' if not fail else 'FAIL_ITER672_INDEPENDENT_FRONTIER_AUDIT'),
 'candidate_count':len(cands),'frontier_candidates':cands,
 'selection_rule':'Choose the newest scientifically independent candidate whose prerequisites remain authoritative and whose proposed gate does not reopen frozen/closed sectors. Text alone is never promoted; Iter673 must directly inspect the top finite candidate set.',
 'soft_tcut_branch':'FROZEN_PREREQUISITE_BLOCKED','source_born_subtraction':'NOT_PERFORMED','zero_fill':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'exact_next_gate':'Iteration673: semantically inspect the newest finite independent candidates from Iter672 and select exactly one nearest algebraic/authority gate; if all are stale/superseded, record that and continue backward until a live independent front is found.'}
p=R/'candidate_gravity/results/iteration672_independent_frontier_authority_audit.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if fail: raise SystemExit(2)
