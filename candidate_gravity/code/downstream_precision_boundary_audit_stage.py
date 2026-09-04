#!/usr/bin/env python3
"""Non-promoting downstream precision-boundary source audit after Iteration 446.

Locates actual source files/references for the retained active index-2 path toward
Iterations 379/407/421/424, fingerprints them, and inventories explicit
binary64/NumPy arithmetic markers. Source inspection freezes the next numerical
precision gate; it is not itself a numerical precision closure.
"""
from __future__ import annotations
import hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'candidate_gravity'
TOKENS=('iteration379','iteration407','iteration421','iteration424')
MARKERS=('np.','numpy','dtype=float','dtype=complex','complex128','float64','np.linalg','np.trace','@')
CERTIFIED=('iteration368','iteration370','postparent_contraction_precision_stage','iteration445','iteration446')

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    candidates=[]
    for sub in ('code','recovery'):
        for p in (BASE/sub).rglob('*'):
            if not p.is_file() or p.suffix not in ('.py','.md','.json'): continue
            text=p.read_text(errors='replace'); low=(str(p.relative_to(ROOT))+'\n'+text).lower()
            hits=[t for t in TOKENS if t in low]
            if not hits: continue
            marker_hits=[]
            if p.suffix=='.py':
                for n,line in enumerate(text.splitlines(),1):
                    if any(m in line for m in MARKERS): marker_hits.append({'line':n,'text':line.strip()[:240]})
            candidates.append({'path':str(p.relative_to(ROOT)),'sha256':sha(p),'token_hits':hits,'binary64_numpy_markers':marker_hits[:200]})
    code=[x for x in candidates if x['path'].startswith('candidate_gravity/code/')]
    refs={t:sorted(x['path'] for x in candidates if t in x['token_hits']) for t in TOKENS}
    code407=[x for x in code if 'iteration407' in x['token_hits']]
    code_active=[x for x in code if any(t in x['token_hits'] for t in ('iteration407','iteration421','iteration424'))]
    explicit=[{'path':x['path'],'marker_count':len(x['binary64_numpy_markers']),'markers':x['binary64_numpy_markers']} for x in code_active if x['binary64_numpy_markers']]
    # PASS here means provenance located sufficiently to freeze a next numerical gate,
    # never that the numerical layer is precision-certified.
    passed=bool(code407 and code_active)
    first_boundary=(explicit[0]['path'] if explicit else (code_active[0]['path'] if code_active else None))
    out={
      'stage':'DOWNSTREAM_PRECISION_BOUNDARY_AUDIT__POST_ITER446__UNNUMBERED_UNTIL_RAW_CONSUME',
      'authority_scope':'SOURCE_PROVENANCE_ONLY__ACTIVE_INDEX2_DOWNSTREAM_OF_CERTIFIED_368_370_POSTPARENT',
      'classification':'PASS_SOURCE_BOUNDARY_LOCATED__NON_PROMOTING_NOT_NUMERICAL_CLOSURE' if passed else 'BLOCKED_SOURCE_BOUNDARY_NOT_LOCATED',
      'scientific_gate_pass':passed,'promotes_physical_coordinate':False,'numerical_precision_closed':False,
      'references':refs,'source_records':candidates,'active_code_records':len(code_active),'iteration407_code_records':len(code407),
      'explicit_binary64_numpy_boundaries':explicit,'first_uncertified_boundary_candidate':first_boundary,
      'already_certified_scope_labels':list(CERTIFIED),
      'next_gate_if_pass':'freeze and execute continuous 80/120-digit numerical certificate for the first still-uncertified active downstream arithmetic layer identified here, preserving exact routing/numerator/nodes/thresholds',
      'guardrails':['SOURCE_AUDIT_IS_NOT_NUMERICAL_PASS','DO_NOT_REOPEN_ITER374_PHYSICS','NO_ZERO_FILL','NO_THRESHOLD_WEAKENING','NO_ROUTING_OR_NUMERATOR_CHANGE','INDEX2_REMAINS_BLOCKED'],
      'MODEL_READINESS':'24%','readiness_change_pp':0}
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed: raise SystemExit(2)
if __name__=='__main__': main()
