#!/usr/bin/env python3
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[2]
fail=[]
for p in ['candidate_gravity/results/iteration653_closed_sk_gamma2_gamma3_ward_contract.json','candidate_gravity/results/iteration666_ward_controlled_longitudinal_soft_observable_authority.json']:
 q=R/p
 if not q.exists(): fail.append('missing:'+p)
 else:
  d=json.loads(q.read_text())
  if d.get('scientific_gate_pass') is not True: fail.append('nonpass:'+p)
# Search for a committed MSSC001-specific bridge that simultaneously specifies a gauge-invariant physical observable
# and a detector/asymptotic/LSZ reduction. Generic literature/comparator discussion is not same-parent authority.
terms=[re.compile(r'MSSC001',re.I),re.compile(r'(detector|generalized[- ]LSZ|asymptotic observable|gauge[- ]invariant observable)',re.I)]
candidates=[]
for p in (R/'candidate_gravity').rglob('*'):
 if not p.is_file() or p.suffix.lower() not in {'.md','.json','.py','.txt'}: continue
 sp=str(p.relative_to(R))
 if 'iteration667' in sp.lower() or 'iteration_667' in sp.lower(): continue
 try: t=p.read_text(errors='ignore')
 except Exception: continue
 if all(x.search(t) for x in terms): candidates.append(sp)
# Existing current/recovery bookkeeping may mention desired bridge but is not a derivation.
bookkeeping=[x for x in candidates if '/recovery/' in x or '/research_log/' in x]
derived=[x for x in candidates if x not in bookkeeping]
if derived: fail.append('candidate same-parent physical observable bridge requires semantic review:'+','.join(sorted(derived)))
out={'iteration':667,'date':'2026-09-09','MODEL_READINESS':'24%','scientific_gate_pass':not fail,'failures':fail,'blocked':not fail,
 'classification':('BLOCKED_ITER667_NO_COMMITTED_MSSC001_GAUGE_INVARIANT_DETECTOR_OR_ASYMPTOTIC_SOFT_OBSERVABLE_BRIDGE_FOUND__LONGITUDINAL_WARD_DATA_INSUFFICIENT__NON_RESIDUAL' if not fail else 'FAIL_ITER667_PHYSICAL_SOFT_OBSERVABLE_BRIDGE_AUDIT'),
 'candidate_paths':sorted(candidates),'semantic_review_required_paths':sorted(derived),
 'missing_bridge':'An explicit same-parent map from closed-SK metric insertions to a gauge-invariant physical detector/asymptotic observable, including reduction/normalization, soft-leg definition, hard-channel discontinuity, contact/source completion and IR convention.',
 'native_soft_Tcut':'BLOCKED_PHYSICAL_OBSERVABLE_MAP_REQUIRED','source_born_subtraction':'NOT_PERFORMED','zero_fill':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'exact_next_gate':'Iteration668: derive the minimal gauge-invariant observable bridge prospectively from the committed closed-SK parent by coupling an explicit conserved detector/source tensor and proving gauge invariance of the smeared response before any cut integration; if the parent lacks enough detector/source data, freeze those missing inputs explicitly rather than importing an in-out proxy.'}
p=R/'candidate_gravity/results/iteration667_physical_soft_observable_bridge_audit.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if fail: raise SystemExit(2)
