#!/usr/bin/env python3
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[2]
fail=[]
for p in ['candidate_gravity/results/iteration668_conserved_detector_gauge_invariant_bridge_authority.json','candidate_gravity/results/iteration669_committed_detector_geometry_inventory_authority.json']:
 q=R/p
 if not q.exists(): fail.append('missing:'+p)
 else:
  d=json.loads(q.read_text())
  if d.get('scientific_gate_pass') is not True: fail.append('nonpass:'+p)
# Same-parent authority scan: require explicit MSSC001 mention and detector/source geometry/conserved-smearing content.
# Bookkeeping, Iter668/669/670 audit files are not derivations and are excluded.
geom=re.compile(r'(detector|source\s+geometry|conserved\s+(?:source|tensor|stress)|smear(?:ed|ing)|probe\s+map)',re.I)
parent=re.compile(r'MSSC001',re.I)
hits=[]
for p in (R/'candidate_gravity').rglob('*'):
 if not p.is_file() or p.suffix.lower() not in {'.md','.json','.py','.txt'}: continue
 sp=str(p.relative_to(R)); sl=sp.lower()
 if any(x in sl for x in ['/recovery/','/research_log/','iteration668','iteration_668','iteration669','iteration_669','iteration670','iteration_670']): continue
 try: t=p.read_text(errors='ignore')
 except Exception: continue
 if parent.search(t) and geom.search(t): hits.append(sp)
out={'iteration':670,'date':'2026-09-09','MODEL_READINESS':'24%','scientific_gate_pass':not fail,'failures':fail,'blocked':not fail,
 'classification':(('BLOCKED_ITER670_NO_COMMITTED_MSSC001_SPECIFIC_CONCRETE_CONSERVED_DETECTOR_GEOMETRY_FOUND__SOFT_TCUT_BRANCH_PREREQUISITE_FROZEN__NON_RESIDUAL' if not hits else 'BLOCKED_ITER670_MSSC001_DETECTOR_GEOMETRY_CANDIDATES_REQUIRE_DIRECT_SEMANTIC_REVIEW__NON_RESIDUAL') if not fail else 'FAIL_ITER670_MSSC001_DETECTOR_AUTHORITY_SCAN'),
 'same_parent_candidate_paths':hits,'candidate_count':len(hits),
 'historical_comparator_nonpromotion':['C5 Iter148/149 source-completion protocol is comparator-specific, spacelike off-shell, signature (-,+,+,+), not an MSSC001 soft detector map','C3 Iter229 is a comparator underdetermination certificate, not an MSSC001 detector geometry'],
 'soft_tcut_branch':('PREREQUISITE_BLOCKED_NO_SAME_PARENT_DETECTOR_GEOMETRY' if not hits else 'BLOCKED_PENDING_CANDIDATE_SEMANTIC_REVIEW'),
 'native_soft_Tcut':'BLOCKED_DETECTOR_GEOMETRY_NORMALIZATION_AND_SOFT_MATCHING_REQUIRED','source_born_subtraction':'NOT_PERFORMED','zero_fill':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'exact_next_gate':('Iteration671: soft-Tcut branch is prerequisite-blocked; select the nearest independent admissible Candidate-Gravity gate from current recovery without reopening C5 e=3 or importing detector geometry. Audit remaining active model-readiness blockers and launch the closest algebraic/authority gate.' if not hits else 'Iteration671: directly inspect only the MSSC001-specific candidate paths and either freeze an authoritative geometry prospectively or preserve the prerequisite blocker.')}
p=R/'candidate_gravity/results/iteration670_mssc001_detector_geometry_authority_scan.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if fail: raise SystemExit(2)
