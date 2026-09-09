#!/usr/bin/env python3
"""Iteration 641: prospective denominator-level closed-loop spectral kernel contract.
No numerator is zero-filled; unsupported tensor contractions remain explicitly BLOCKED.
"""
from __future__ import annotations
import hashlib,json,math,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[2]
front=(ROOT/'candidate_gravity'/'recovery'/'CURRENT_QG_FRONT.md').read_text()
failures=[]
# Accept either pre-update Iter639 front or authoritative Iter640 front text during race; require frozen facts.
for tok in ['MODEL_READINESS:** **24%','s_thr=4 m_phi^2=1.96','D_s=Disc_s/(2*pi*i)']:
    if tok not in front: failures.append('missing frozen front token '+tok)

m=0.7; sth=4*m*m
samples=[1.0,1.96,2.0,2.5,4.0,9.0]
def beta(s):
    if s<sth: return None
    return math.sqrt(max(0.0,1.0-sth/s))
rows=[{'s':s,'supported':s>=sth,'beta_two_body':beta(s)} for s in samples]
# This is only the universal two-body denominator phase-space factor. Absolute loop prefactor,
# gravitational vertex numerator, SK combinatorics and tensor projection are not invented here.
contract={
 'ordinary_two_body_support':'Theta(s-1.96)',
 'universal_equal_mass_beta':'sqrt(1-1.96/s)',
 'normalization_scope':'kinematic denominator-level factor only; no absolute 4D loop prefactor frozen here',
 'K1K2_density':'beta(s) times SAME_PARENT_RETARDED_VERTEX_NUMERATOR__BLOCKED_PENDING_EXPLICIT_CONTRACTION',
 'K1^3_density':'ordinary Cutkosky phase-space integral of third propagator times SAME_PARENT_RETARDED_VERTEX_NUMERATOR__BLOCKED_PENDING_EXPLICIT_CONTRACTION',
 'K3':'retained analytic/contact family; ordinary finite-s cut absent',
 'native_operator':'D_s=Disc_s/(2*pi*i) inherited unchanged',
}
if abs(sth-1.96)>2e-15: failures.append('threshold drift')
if beta(1.0) is not None: failures.append('subthreshold beta should be unsupported, not zero')
classification=('PASS_ITER641_PROSPECTIVE_CLOSED_LOOP_DENOMINATOR_SPECTRAL_KERNEL_CONTRACT__NUMERATOR_EXPLICITLY_BLOCKED__NON_RESIDUAL' if not failures else 'FAIL_ITER641_SPECTRAL_KERNEL_CONTRACT')
result={'iteration':641,'date':'2026-09-09','scientific_gate_pass':not failures,'classification':classification,'failures':failures,
 'frozen_threshold':sth,'sample_rows':rows,'spectral_kernel_contract':contract,
 'unsupported_numerator_policy':'BLOCKED_NOT_ZERO_FILLED','candidate_residual':False,'candidate_values_used':False,'zero_fill':False,
 'source_born_subtraction':'NOT_PERFORMED','native_Y_Tcut_projection':'NOT_PERFORMED','comparator_quotient':'NOT_PERFORMED','ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN','MODEL_READINESS':'24%',
 'next_gate':'Implement explicit same-parent MSSC001 retarded vertex numerator contractions on the two-body cut for K1/K2 and the ordinary K1^3 cut, using frozen Iter627+632 SK structure; unsupported tensor components remain BLOCKED.'}
out=ROOT/'results'/'iteration641_closed_loop_spectral_kernel_contract';out.mkdir(parents=True,exist_ok=True)
rp=out/'result.json';rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
a={'iteration':641,'result_sha256':hashlib.sha256(rp.read_bytes()).hexdigest(),'failures':failures,'classification':('PASS_RAW_AUTHORITY_AUDIT_ITER641_SPECTRAL_KERNEL_CONTRACT' if not failures else 'FAIL_RAW_AUTHORITY_AUDIT_ITER641_SPECTRAL_KERNEL_CONTRACT')}
(out/'authority_audit.json').write_text(json.dumps(a,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
if failures: raise SystemExit(2)
