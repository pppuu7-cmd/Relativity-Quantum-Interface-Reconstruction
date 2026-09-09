#!/usr/bin/env python3
"""Iteration 652: restore the exact meaning of the source-completion term in
frozen Iter205 T_cut after Iter649-651 proxy-Born no-go audits.

This is an authority/scope audit only. It does not compute a new K2 or W map and
uses no Candidate/comparator values.
"""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[2]
failures=[]

d205=json.loads((ROOT/'results/linked_nonanalytic_cut_protocol_iteration205.json').read_text())
code205=(ROOT/'analysis/linked_nonanalytic_cut_protocol_iteration205.py').read_text()
d651=json.loads((ROOT/'candidate_gravity/results/iteration651_same_parent_closed_gamma3_born_raw_consumption.json').read_text())
code582=(ROOT/'candidate_gravity/code/iteration582_connection_e2_effective_action_q2.py').read_text()
d644=json.loads((ROOT/'results/iteration644_external_tensor_transport_contract/result.json').read_text())
ward151=(ROOT/'candidate_gravity/C5_WARD_IDENTITY_ITERATION151.md').read_text()

expected='T_cut = D Gamma3_ret,soft - W[D K2] in one source-completed convention'
if d205.get('proposed_coordinate')!=expected: failures.append('Iter205 T_cut coordinate drift')
if 'This W is not the physical gravity Ward operator' not in code205: failures.append('Iter205 toy-W warning missing')
if 'B3[L_xi, h2, h3] + B2[Lie_xi h2, h3] + B2[h2, Lie_xi h3] = 0' not in ward151: failures.append('Iter151 action Ward skeleton missing')
if "scope':'CONNECTION_SECTOR_ONLY__NOT_FULL_SOURCE_WARD_CONTACT_K2'" not in code582: failures.append('Iter582 scope drift')
if d644.get('frozen_v1',{}).get('gauge_condition')!='NONE_ADDED': failures.append('Iter644 gauge-condition authority drift')
if d651.get('old_iter214_eligible') is not False or d651.get('old_iter222_eligible') is not False: failures.append('Iter651 proxy no-go drift')

result={
 'iteration':652,
 'date':'2026-09-09',
 'MODEL_READINESS':'24%',
 'readiness_change':'0 percentage points',
 'classification':(
   'PASS_ITER652_FROZEN_T_CUT_SOURCE_COMPLETION_IS_W_OF_SAME_PARENT_TWO_POINT_CUT__HISTORICAL_BORN_PROXY_ROUTE_TERMINAL_BUT_CONSTRUCTIVE_K2_W_ROUTE_OPEN__NON_RESIDUAL'
   if not failures else 'BLOCKED_ITER652_AUTHORITY_INPUT_DRIFT__NON_RESIDUAL'),
 'scientific_gate_pass':not failures,
 'candidate_residual':False,
 'frozen_coordinate':'T_cut = D_s Gamma3_ret,soft - W[D_s K2]',
 'exact_scope_correction':{
   'Iter651_terminal_scope':'terminal only for importing Iter214/222/open-response Born proxies into closed Gamma3',
   'Iter205_source_completion_semantics':'Ward/soft-determined image W[D_s K2] of the same-parent gravitational inverse two-point kernel',
   'external_Born_amplitude_required_by_definition':False
 },
 'authority_status':{
   'Iter205_physical_W_defined':False,
   'Iter205_W_is_toy_protocol_validator':True,
   'Iter151_action_level_longitudinal_Ward_skeleton_exists':True,
   'Iter151_sufficient_as_full_physical_soft_W_for_current_closed_scalar_loop':False,
   'Iter582_is_full_matched_K2_authority':False,
   'Iter582_scope':'connection-sector bookkeeping only, explicitly not full Source/Ward/contact+K2',
   'Iter644_generic_probe_gauge_condition':'NONE_ADDED'
 },
 'constructive_next_contract':{
   'name':'MSSC001-CLOSED-SK-K2-WARD-SOFT-V1',
   'must_freeze_before_values':[
      'same doubled MSSC001 CTP/Legendre parent and absolute loop normalization for both Gamma2 and Gamma3',
      'retarded/CTP component of the gravitational two-point inverse kernel K2',
      'normalized hard-channel D_s K2 in the same s,t,u invariant family as closed Gamma3',
      'physical linear Ward/soft map W acting on the frozen external tensor family, not the Iter205 toy W',
      'contact/source completion implied by the same diffeomorphism identity',
      'relative factorial/i/sign normalization between Gamma3 and W[K2] before inspecting T_cut values'
   ],
   'expected_two_point_loop_structure':'derive from the same scalar TrLog parent; local/tadpole pieces are classified separately and discontinuity support comes only from genuinely nonanalytic two-propagator structure',
   'anti_bias':'no Iter645/648/Iter582 values may select W, tensor projection, or normalization'
 },
 'source_born_subtraction':'NOT_PERFORMED',
 'native_Y_Tcut_projection':'NOT_PERFORMED',
 'comparator_quotient':'NOT_PERFORMED',
 'zero_fill':False,
 'ANSATZ_003':'FORBIDDEN',
 'Fisher_resources':'FORBIDDEN',
 'failures':failures,
 'next_gate':'Iteration653: prospectively freeze MSSC001-CLOSED-SK-K2-WARD-SOFT-V1 and derive the same-parent closed-SK gravitational two-point kernel/CTP component plus the physical W map before any new cut values are evaluated.'
}
out=ROOT/'candidate_gravity/results/iteration652_linked_tcut_source_completion_scope_audit.json'
out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
if failures: raise SystemExit(2)
