#!/usr/bin/env python3
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[2]
fail=[]
for p in ['candidate_gravity/results/iteration665_prospective_noncollinear_soft_redesign_authority.json','candidate_gravity/results/iteration668_conserved_detector_gauge_invariant_bridge_authority.json']:
 q=R/p
 if not q.exists(): fail.append('missing:'+p)
 else:
  d=json.loads(q.read_text())
  if d.get('scientific_gate_pass') is not True: fail.append('nonpass:'+p)
# Inventory only. Keyword hits are not automatically authority; this gate reports them for semantic review.
patterns=[re.compile(x,re.I) for x in [r'detector',r'source\s+geometry',r'smear(?:ed|ing)',r'conserved\s+(?:source|tensor|stress)',r'compact\s+support']]
hits=[]
for p in (R/'candidate_gravity').rglob('*'):
 if not p.is_file() or p.suffix.lower() not in {'.md','.json','.py','.txt'}: continue
 sp=str(p.relative_to(R))
 if 'iteration669' in sp.lower() or 'iteration_669' in sp.lower(): continue
 try: t=p.read_text(errors='ignore')
 except Exception: continue
 found=[pat.pattern for pat in patterns if pat.search(t)]
 if found: hits.append({'path':sp,'patterns':found})
# Exclude bookkeeping and the Iter668 abstract construction itself from concrete-geometry candidates.
def bookkeeping(sp):
 s=sp.lower()
 return ('/recovery/' in s or '/research_log/' in s or 'iteration668' in s or 'iteration_668' in s)
candidates=[h for h in hits if not bookkeeping(h['path'])]
out={'iteration':669,'date':'2026-09-09','MODEL_READINESS':'24%','scientific_gate_pass':not fail,'failures':fail,'blocked':not fail,
 'classification':('BLOCKED_ITER669_COMMITTED_DETECTOR_SOURCE_GEOMETRY_INVENTORY_REQUIRES_SEMANTIC_REVIEW__NO_GEOMETRY_PROMOTED_BY_KEYWORD__NON_RESIDUAL' if not fail else 'FAIL_ITER669_DETECTOR_GEOMETRY_INVENTORY'),
 'all_hits':hits,'semantic_review_candidates':candidates,'candidate_count':len(candidates),
 'authority_rule':'Keyword occurrence is inventory only. A candidate may be promoted only if it explicitly gives a symmetric conserved tensor/source geometry, normalization/boundary convention, and compatibility with the frozen soft family; otherwise it remains non-authority.',
 'native_soft_Tcut':'BLOCKED_DETECTOR_GEOMETRY_NORMALIZATION_AND_SOFT_MATCHING_REQUIRED','source_born_subtraction':'NOT_PERFORMED','zero_fill':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'exact_next_gate':'Iteration670: semantically inspect the finite Iter669 candidate set. If a concrete conserved detector/source geometry exists, freeze only its already-authoritative data and test compatibility with Iter665. If none qualifies, record detector geometry as prerequisite-blocked and switch to the nearest independent admissible Candidate-Gravity gate outside the soft-Tcut branch.'}
p=R/'candidate_gravity/results/iteration669_committed_detector_geometry_inventory.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if fail: raise SystemExit(2)
