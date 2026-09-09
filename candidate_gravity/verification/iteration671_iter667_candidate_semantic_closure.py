#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
fail=[]
authp=R/'candidate_gravity/results/iteration667_physical_soft_observable_bridge_authority.json'
audp=R/'candidate_gravity/verification/iteration667_physical_soft_observable_bridge_audit.py'
for p in [authp,audp]:
 if not p.exists(): fail.append('missing:'+str(p.relative_to(R)))
a={}
if authp.exists():
 a=json.loads(authp.read_text())
 if a.get('scientific_gate_pass') is not True: fail.append('Iter667 authority not raw-valid')
 if 'NO_COMMITTED_MSSC001_GAUGE_INVARIANT_DETECTOR_OR_ASYMPTOTIC_SOFT_OBSERVABLE_BRIDGE_FOUND' not in a.get('classification',''): fail.append('Iter667 absence classification drift')
 if not a.get('missing_bridge'): fail.append('Iter667 missing bridge not explicit')
script=audp.read_text(errors='ignore') if audp.exists() else ''
if "same-parent" not in script and "same_parent" not in script: fail.append('Iter667 audit semantic scope missing')
out={'iteration':671,'date':'2026-09-09','MODEL_READINESS':'24%','scientific_gate_pass':not fail,'failures':fail,'blocked':not fail,
 'classification':('BLOCKED_ITER671_ITER667_SCAN_HITS_ARE_ABSENCE_AUDIT_SELF_REFERENCES_NOT_DETECTOR_GEOMETRY__NO_COMMITTED_MSSC001_CONCRETE_DETECTOR_GEOMETRY__SOFT_TCUT_BRANCH_PREREQUISITE_FROZEN__NON_RESIDUAL' if not fail else 'FAIL_ITER671_DETECTOR_CANDIDATE_SEMANTIC_CLOSURE'),
 'reviewed_paths':[str(authp.relative_to(R)),str(audp.relative_to(R))],
 'semantic_result':'Both Iter670 candidates are Iter667 files whose purpose and result are to certify absence of a committed MSSC001 physical detector/asymptotic bridge. They do not define any detector tensor geometry, normalization, boundary convention, soft kernel, or source/Born completion.',
 'soft_tcut_branch':'PREREQUISITE_BLOCKED_NO_SAME_PARENT_CONCRETE_DETECTOR_GEOMETRY',
 'native_soft_Tcut':'BLOCKED_DETECTOR_GEOMETRY_NORMALIZATION_AND_SOFT_MATCHING_REQUIRED','source_born_subtraction':'NOT_PERFORMED','zero_fill':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'exact_next_gate':'Iteration672: leave the soft-Tcut branch frozen at its explicit detector-geometry prerequisite and audit current Candidate-Gravity recovery for the nearest independent admissible algebraic/authority gate. Do not reopen closed C5 e=3, use old weighted-B3 proxies, or launch blind heavy full-C5.'}
p=R/'candidate_gravity/results/iteration671_iter667_candidate_semantic_closure.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if fail: raise SystemExit(2)
