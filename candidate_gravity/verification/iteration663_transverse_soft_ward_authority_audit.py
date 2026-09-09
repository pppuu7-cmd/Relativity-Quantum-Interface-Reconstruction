#!/usr/bin/env python3
"""Iter663: fail-closed authority audit for W[D_s K2] on frozen transverse +TT soft component."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
fail=[]
p653=ROOT/'candidate_gravity/results/iteration653_closed_sk_gamma2_gamma3_ward_contract.json'
p658=ROOT/'candidate_gravity/results/iteration658_plus_tt_null_quotient_invariance.json'
p662=ROOT/'candidate_gravity/results/iteration662_plus_tt_quarter_turn_selection_rule_authority.json'
for p in (p653,p658,p662):
 if not p.exists(): fail.append('missing:'+p.name)
if not fail:
 d653=json.loads(p653.read_text()); d658=json.loads(p658.read_text()); d662=json.loads(p662.read_text())
 if not all(d.get('scientific_gate_pass') is True for d in (d653,d658,d662)): fail.append('parent authority nonpass')
 W=d653.get('Ward_map',{})
 longitudinal_only=('fixes only the Ward-determined longitudinal component' in W.get('scope',''))
 generic_transverse_denied=('no claim that the generic q-transverse soft component is determined by K2' in W.get('scope',''))
 plus_transverse=d658.get('checks',{}).get('plus_TT_is_transverse') is True
 plus_nontrivial=d658.get('checks',{}).get('measurement_is_nontrivial_on_quotient_witness') is True
 gamma3_zero='vanishes exactly' in d662.get('exact_result','')
 if not longitudinal_only: fail.append('Iter653 longitudinal-only scope not recovered')
 if not generic_transverse_denied: fail.append('Iter653 transverse limitation not recovered')
 if not plus_transverse or not plus_nontrivial: fail.append('Iter658 transverse quotient witness not recovered')
 if not gamma3_zero: fail.append('Iter662 exact +++ Gamma3-cut zero not recovered')
else:
 longitudinal_only=generic_transverse_denied=plus_transverse=plus_nontrivial=gamma3_zero=False
# A successful audit is intentionally BLOCKED on the physical W value: unsupported != zero.
blocked=(not fail and longitudinal_only and generic_transverse_denied and plus_transverse and plus_nontrivial)
out={
 'iteration':663,'date':'2026-09-09','MODEL_READINESS':'24%',
 'classification':('BLOCKED_ITER663_EXISTING_WARD_AUTHORITY_IS_LONGITUDINAL_ONLY__FROZEN_PLUS_TT_SOFT_COMPONENT_IS_TRANSVERSE_NONTRIVIAL_QUOTIENT__W_DS_K2_UNDEFINED_NOT_ZERO__NON_RESIDUAL' if blocked else 'FAIL_ITER663_WARD_AUTHORITY_AUDIT'),
 'scientific_gate_pass':not fail,'failures':fail,'blocked':blocked,
 'checks':{'Iter653_W_longitudinal_only':longitudinal_only,'Iter653_denies_generic_transverse_determination':generic_transverse_denied,'Iter658_plus_TT_transverse':plus_transverse,'Iter658_plus_TT_nontrivial_quotient':plus_nontrivial,'Iter662_plus_plus_plus_Gamma3_cut_exact_zero':gamma3_zero},
 'authority_statement':'Current same-parent Ward authority does not define W[D_s K2] on the frozen transverse plus-TT soft quotient component. Therefore the exact Iter662 Gamma3-cut zero cannot yet be promoted to a matched T_cut value. The missing Ward image is BLOCKED, never zero-filled.',
 'source_born_subtraction':'NOT_PERFORMED','native_soft_Tcut':'BLOCKED_W_TRANSVERSE_OPERATOR_UNDEFINED','zero_fill':False,'candidate_values_used':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'exact_next_gate':'Iteration664 authority-improvement derivation: from the same-parent diffeomorphism/soft generating-functional identity underlying Iter653, derive whether a physical transverse soft operator exists for the frozen null plus-TT quotient. Keep it distinct from the longitudinal gauge Ward map; if the parent dynamics supplies no such identity, record the T_cut plus-TT branch as prerequisite-BLOCKED and move to an independent polarization/observable channel rather than inventing W.'}
p=ROOT/'candidate_gravity/results/iteration663_transverse_soft_ward_authority_audit.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if fail: raise SystemExit(2)
