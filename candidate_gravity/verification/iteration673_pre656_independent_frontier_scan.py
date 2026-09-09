#!/usr/bin/env python3
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[2]
fail=[]
req='candidate_gravity/results/iteration672_independent_frontier_authority_audit_authority.json'
q=R/req
if not q.exists(): fail.append('missing:'+req)
else:
 d=json.loads(q.read_text())
 if d.get('scientific_gate_pass') is not True: fail.append('nonpass:'+req)
# Search strictly below Iter656. Exclude forbidden/closed sectors and any explicit soft/detector/Ward continuation.
exclude=re.compile(r'(soft|detector|ward|source[-_ ]?born|ansatz[-_ ]?003|fisher|resource|full[-_ ]?c5|weighted[-_ ]?b3|\be=3\b|null[-_ ]?soft)',re.I)
c=[]
for p in (R/'candidate_gravity/results').glob('*.json'):
 try: d=json.loads(p.read_text())
 except Exception: continue
 it=d.get('iteration')
 if not isinstance(it,int) or it>=656: continue
 nxt=d.get('exact_next_gate')
 if not isinstance(nxt,str) or not nxt.strip() or exclude.search(nxt): continue
 c.append({'iteration':it,'path':str(p.relative_to(R)),'classification':d.get('classification'),'blocked':d.get('blocked'),'scientific_gate_pass':d.get('scientific_gate_pass'),'exact_next_gate':nxt})
c=sorted(c,key=lambda x:x['iteration'],reverse=True)[:25]
out={'iteration':673,'date':'2026-09-09','MODEL_READINESS':'24%','scientific_gate_pass':not fail,'failures':fail,'blocked':not fail,
 'classification':('BLOCKED_ITER673_PRE656_NONSOFT_FRONTIER_CANDIDATES_INVENTORIED__SEMANTIC_SELECTION_REQUIRED__NON_RESIDUAL' if not fail else 'FAIL_ITER673_PRE656_FRONTIER_SCAN'),
 'candidate_count':len(c),'frontier_candidates':c,
 'selection_rule':'Newest-first semantic review. Reject stale/superseded candidates, proxy residues, closed sectors, and any gate whose prerequisites were invalidated later. Promote exactly one live independent algebraic/provenance gate only after direct authority inspection.',
 'soft_tcut_branch':'FROZEN_PREREQUISITE_BLOCKED','source_born_subtraction':'NOT_PERFORMED','zero_fill':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'exact_next_gate':'Iteration674: directly inspect the newest finite pre656 candidate set from Iter673 and launch exactly one live independent gate; if all are stale, continue backward with the same exclusions.'}
p=R/'candidate_gravity/results/iteration673_pre656_independent_frontier_scan.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if fail: raise SystemExit(2)
