#!/usr/bin/env python3
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[2]
fail=[]
req=R/'candidate_gravity/results/iteration673_pre656_independent_frontier_scan_authority.json'
if not req.exists(): fail.append('missing Iter673 authority')
else:
 d=json.loads(req.read_text())
 if d.get('scientific_gate_pass') is not True or d.get('candidate_count')!=0: fail.append('Iter673 authority drift')
# Broader authority graph: inspect raw/result JSON states, not only explicit exact_next_gate strings.
# Keep unresolved BLOCKED/prerequisite records below the soft trajectory. Exclude closed/forbidden branches and
# obvious bookkeeping/self-audit records. This is inventory; no candidate is auto-promoted.
exclude=re.compile(r'(soft|detector|ward|ansatz[-_ ]?003|fisher|resource|full[-_ ]?c5|weighted[-_ ]?b3|\be=3\b|null[-_ ]?soft)',re.I)
book=re.compile(r'(frontier|inventory|authority_scan|semantic_closure|recovery)',re.I)
cands=[]
for p in (R/'candidate_gravity/results').glob('*.json'):
 try: d=json.loads(p.read_text())
 except Exception: continue
 it=d.get('iteration')
 if not isinstance(it,int) or it>=656: continue
 if d.get('blocked') is not True: continue
 blob=' '.join([str(p.name),str(d.get('classification','')),str(d.get('exact_next_gate','')),str(d.get('status','')),str(d.get('result',''))])
 if exclude.search(blob) or book.search(p.name): continue
 # Surface concrete prerequisite text and relevant named state keys for semantic review.
 prereq=[]
 for k,v in d.items():
  if isinstance(v,str) and re.search(r'(BLOCKED|prereq|missing|unsupported|underdetermin|not[_ ]performed|required)',v,re.I):
   prereq.append({'key':k,'value':v[:500]})
 cands.append({'iteration':it,'path':str(p.relative_to(R)),'classification':d.get('classification'),'exact_next_gate':d.get('exact_next_gate'),'prerequisite_evidence':prereq[:8]})
cands=sorted(cands,key=lambda x:x['iteration'],reverse=True)[:40]
out={'iteration':674,'date':'2026-09-09','MODEL_READINESS':'24%','scientific_gate_pass':not fail,'failures':fail,'blocked':not fail,
 'classification':('BLOCKED_ITER674_REPOSITORY_AUTHORITY_GRAPH_UNRESOLVED_NONSOFT_BRANCHES_INVENTORIED__DIRECT_SEMANTIC_SELECTION_REQUIRED__NON_RESIDUAL' if cands and not fail else ('BLOCKED_ITER674_NO_UNRESOLVED_ADMISSIBLE_NONSOFT_AUTHORITY_BRANCH_FOUND__GLOBAL_CURRENT_PREREQUISITE_EXHAUSTION_CANDIDATE__NON_RESIDUAL' if not fail else 'FAIL_ITER674_REPOSITORY_AUTHORITY_GRAPH_AUDIT')),
 'candidate_count':len(cands),'authority_graph_candidates':cands,
 'scope':'pre-Iter656 BLOCKED result authorities excluding soft/detector/Ward, closed C5 e=3/null-soft, weighted-B3 proxy, blind full-C5, ANSATZ-003, Fisher/resources and bookkeeping inventories',
 'promotion_rule':'Inventory is not authority promotion. The newest candidates must be read directly and rejected if superseded or comparator-only; select exactly one only if prerequisites remain live.',
 'soft_tcut_branch':'FROZEN_PREREQUISITE_BLOCKED','source_born_subtraction':'NOT_PERFORMED','zero_fill':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'exact_next_gate':('Iteration675: directly inspect the newest Iter674 authority-graph candidates and select exactly one live independent algebraic/provenance gate; if all are stale/superseded, record global present prerequisite exhaustion.' if cands else 'Iteration675: certify global present prerequisite exhaustion against CURRENT_QG_FRONT and the stable readiness rubric, enumerate exact external/missing authorities, and do not launch artificial computation until new authority enters the repository.')}
p=R/'candidate_gravity/results/iteration674_repository_authority_graph_audit.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if fail: raise SystemExit(2)
