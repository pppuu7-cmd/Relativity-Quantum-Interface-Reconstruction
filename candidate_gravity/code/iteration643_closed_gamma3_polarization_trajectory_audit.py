#!/usr/bin/env python3
"""Iteration 643: audit whether closed-Gamma3 external tensor/polarization trajectory h_i(s) is frozen.

The scalar-denominator invariant family alone is insufficient for explicit gravitational
vertex cut numerators if the external metric tensors are not continued along s.
Missing trajectory authority is BLOCKED, not guessed from the s0 fixture.
"""
from __future__ import annotations
import hashlib,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[2]
front=(ROOT/'candidate_gravity'/'recovery'/'CURRENT_QG_FRONT.md').read_text()
p368=ROOT/'candidate_gravity'/'code'/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
p594=ROOT/'analysis'/'source_full_cubic_routed_assembly_iteration594.py'
failures=[]
for p in [p368,p594]:
    if not p.exists(): failures.append(f'missing same-parent file {p.relative_to(ROOT)}')
text368=p368.read_text(errors='replace') if p368.exists() else ''
text594=p594.read_text(errors='replace') if p594.exists() else ''
# Existing exact fixture contains q/h tensors at s0, while Iter636 front freezes only invariant family.
fixture_has_h=('M=' in text368 or 'M =' in text368) and ('LEGS' in text368)
front_has_invariant_family='MSSC001-CLOSED-GAMMA3-INV-FAMILY-V1' in front or 'frozen closed-Gamma3 invariant family' in front
# Search explicitly for a committed h_i(s), polarization transport, or tensor trajectory statement.
patterns=[r'h_[sab]\s*\(s\)',r'h\w*\(s\)',r'polarization.{0,40}trajectory',r'tensor.{0,40}trajectory',r'parallel.{0,20}transport']
trajectory_hits=[]
for pat in patterns:
    for m in re.finditer(pat,front,flags=re.I|re.S): trajectory_hits.append(m.group(0))
trajectory_frozen=bool(trajectory_hits)
blocked=bool(fixture_has_h and front_has_invariant_family and not trajectory_frozen)
classification=('BLOCKED_ITER643_CLOSED_GAMMA3_EXTERNAL_TENSOR_TRAJECTORY_NOT_FROZEN__S0_FIXTURE_CANNOT_BE_EXTENDED_POST_HOC__NON_RESIDUAL' if blocked and not failures else
                'PASS_ITER643_CLOSED_GAMMA3_EXTERNAL_TENSOR_TRAJECTORY_ALREADY_FROZEN__NON_RESIDUAL' if trajectory_frozen and not failures else
                'FAIL_ITER643_POLARIZATION_TRAJECTORY_AUDIT')
result={'iteration':643,'date':'2026-09-09','classification':classification,'failures':failures,
 'fixture_has_external_tensors_at_s0':fixture_has_h,'invariant_family_frozen':front_has_invariant_family,
 'external_tensor_trajectory_frozen':trajectory_frozen,'trajectory_hits':trajectory_hits,'blocked':blocked,
 'scientific_gate_pass':bool((blocked or trajectory_frozen) and not failures),'candidate_residual':False,'candidate_values_used':False,'zero_fill':False,
 'reason':'Explicit K1/K2/K1^3 gravitational cut numerators depend on external metric tensors as well as scalar invariants. The exact Iter368/588 fixture supplies tensors only at s0; without a prospective h_i(s) continuation/transport contract, evaluating them for s>=1.96 would introduce post-hoc observable data.',
 'required_if_blocked':'prospectively freeze a Lorentz-covariant external tensor/polarization continuation h_s(s),h_a(s),h_b(s) consistent with q_s+q_a+q_b=0, fixed t0/u0 and the exact s0 fixture, before viewing cut-numerator outputs',
 'source_born_subtraction':'NOT_PERFORMED','native_Y_Tcut_projection':'NOT_PERFORMED','comparator_quotient':'NOT_PERFORMED','ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN','MODEL_READINESS':'24%',
 'next_gate':'If BLOCKED, derive/freeze the minimal external tensor trajectory contract from same-parent covariance and exact fixture without fitting cut outputs; otherwise implement explicit cut numerators.'}
out=ROOT/'results'/'iteration643_closed_gamma3_polarization_trajectory_audit';out.mkdir(parents=True,exist_ok=True)
rp=out/'result.json';rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
a={'iteration':643,'result_sha256':hashlib.sha256(rp.read_bytes()).hexdigest(),'failures':failures,'classification':('BLOCKED_RAW_AUTHORITY_AUDIT_ITER643_EXTERNAL_TENSOR_TRAJECTORY' if blocked and not failures else 'PASS_RAW_AUTHORITY_AUDIT_ITER643_EXTERNAL_TENSOR_TRAJECTORY' if trajectory_frozen and not failures else 'FAIL_RAW_AUTHORITY_AUDIT_ITER643_EXTERNAL_TENSOR_TRAJECTORY')}
(out/'authority_audit.json').write_text(json.dumps(a,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
if failures: raise SystemExit(2)
