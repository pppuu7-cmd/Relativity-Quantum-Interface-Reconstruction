#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
fail=[]
for p in ['candidate_gravity/results/iteration653_closed_sk_gamma2_gamma3_ward_contract.json','candidate_gravity/results/iteration667_physical_soft_observable_bridge_authority.json']:
 q=R/p
 if not q.exists(): fail.append('missing:'+p)
 else:
  d=json.loads(q.read_text())
  if d.get('scientific_gate_pass') is not True: fail.append('nonpass:'+p)
# Prospective algebraic contract: O_J[h]=Integral J^{mu nu} h_{mu nu}; J symmetric and conserved.
# Under delta h_{mu nu}=partial_mu xi_nu+partial_nu xi_mu,
# delta O_J=-2 Integral xi_nu partial_mu J^{mu nu} plus boundary term, hence zero for compact support / vanishing boundary flux.
contract={
 'name':'MSSC001-CLOSED-SK-CONSERVED-DETECTOR-SMEARING-V1',
 'observable':'O_J[h]=Integral d^4x J^{mu nu}(x) h_{mu nu}(x)',
 'source_constraints':['J^{mu nu}=J^{nu mu}','partial_mu J^{mu nu}=0','compact support or vanishing boundary flux'],
 'gauge_variation':'delta_xi O_J=-2 Integral d^4x xi_nu partial_mu J^{mu nu}+boundary = 0',
 'candidate_values_used':False,
 'detector_geometry':'UNSPECIFIED_BLOCKED','absolute_normalization':'UNSPECIFIED_BLOCKED'}
if contract['detector_geometry']!='UNSPECIFIED_BLOCKED': fail.append('detector geometry invented')
out={'iteration':668,'date':'2026-09-09','MODEL_READINESS':'24%','scientific_gate_pass':not fail,'failures':fail,'blocked':not fail,
 'classification':('BLOCKED_ITER668_MINIMAL_CONSERVED_DETECTOR_SMEARING_IS_GAUGE_INVARIANT__ABSTRACT_OBSERVABLE_BRIDGE_FROZEN__PHYSICAL_GEOMETRY_NORMALIZATION_AND_SOFT_MATCHING_STILL_BLOCKED__NON_RESIDUAL' if not fail else 'FAIL_ITER668_CONSERVED_DETECTOR_BRIDGE'),
 'frozen_contract':contract,
 'result':'A conserved symmetric detector/source tensor defines a gauge-invariant linear smeared metric observable modulo the stated boundary condition. This removes the pure-gauge ambiguity at the measurement-map level without choosing a transverse soft amplitude. It does not specify a physical detector geometry, normalization, soft-leg kernel, or source/Born completion.',
 'native_soft_Tcut':'BLOCKED_DETECTOR_GEOMETRY_NORMALIZATION_AND_SOFT_MATCHING_REQUIRED','source_born_subtraction':'NOT_PERFORMED','zero_fill':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'exact_next_gate':'Iteration669: search committed RQIR source/detector protocols for a conserved tensor geometry compatible with this abstract bridge. If one exists, map it prospectively to the Iter665 soft family before evaluating cuts; otherwise freeze detector geometry/normalization as the precise prerequisite blocker and move to another independent admissible sector.'}
p=R/'candidate_gravity/results/iteration668_conserved_detector_gauge_invariant_bridge.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if fail: raise SystemExit(2)
