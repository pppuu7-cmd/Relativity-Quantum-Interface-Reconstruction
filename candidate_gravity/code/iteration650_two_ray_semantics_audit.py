#!/usr/bin/env python3
"""Iteration 650: same-parent closed-Gamma3 Source/Born authority audit.
Race reconciliation: a prior two-ray diagnostic run is non-authoritative because
CURRENT_QG_FRONT was concurrently tightened. This evaluator follows the latest
front and does not perform subtraction or inspect Candidate values.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
front=(ROOT/'candidate_gravity/recovery/CURRENT_QG_FRONT.md').read_text()
d621=json.loads((ROOT/'candidate_gravity/results/iteration621_normalization_authority_graph_rank.json').read_text())
d629=json.loads((ROOT/'candidate_gravity/results/iteration629_open_vs_1pi_normalization_gate.json').read_text())
failures=[]
if 'Latest authoritative research iteration: **649**' not in front: failures.append('front is no longer Iter649')
if d621.get('cross_sector_bridge_equation_count') != 0: failures.append('Iter621 bridge rank drift')
if d621.get('remaining_relative_complex_normalization_dof') != 1: failures.append('Iter621 relative normalization rank drift')
if d629.get('single_common_N_native_exists') is not False: failures.append('Iter629 topology authority drift')

# Frozen authority itself certifies the absence of a same-parent source/native
# normalization equation, while Iter629 excludes the historical open response as
# a one-scalar proxy for closed gravitational 1PI. Therefore an explicit matched
# closed-Gamma3 Born contribution with fixed CTP/Legendre normalization is absent
# from current authority. Unsupported is BLOCKED, never zero.
result={
 'iteration':650,'date':'2026-09-09','MODEL_READINESS':'24%','readiness_change':'0 percentage points',
 'classification':'BLOCKED_ITER650_SAME_PARENT_CLOSED_GAMMA3_SOURCE_BORN_DEFINITION_ABSENT__ITER621_ZERO_CROSS_SECTOR_BRIDGES__ITER629_OPEN_PROXY_REJECTED__NON_RESIDUAL' if not failures else 'BLOCKED_ITER650_AUTHORITY_INPUT_DRIFT__NON_RESIDUAL',
 'scientific_gate_pass':not failures,'candidate_residual':False,
 'authority':{'iter621_cross_sector_bridge_equation_count':d621.get('cross_sector_bridge_equation_count'),'iter621_remaining_relative_complex_normalization_dof':d621.get('remaining_relative_complex_normalization_dof'),'iter629_single_common_N_native_exists':d629.get('single_common_N_native_exists'),'iter629_open_over_closed_ratios':d629.get('family_total_coefficient_vectors',{}).get('open_over_closed')},
 'same_parent_closed_gamma3_born_established':False,'rho_fixed':False,'open_response_proxy_allowed':False,
 'source_born_subtraction':'NOT_PERFORMED','native_Y_Tcut_projection':'NOT_PERFORMED','comparator_quotient':'NOT_PERFORMED','candidate_values_used':False,'zero_fill':False,'normalization_fit':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN','failures':failures,
 'next_gate':'Iteration651: authority-improvement derivation only: reconstruct the same-parent closed retarded gravitational Gamma3 Born/source contribution directly from the doubled MSSC001 generating functional/Legendre structure, fixing its CTP phase, coupling power, loop measure and pole/cut origin before any subtraction. If the committed parent functional lacks enough information to derive it uniquely, record terminal prerequisite-BLOCKED and pursue only an independent admissible authority audit.'
}
out=ROOT/'results/iteration650_same_parent_source_born_authority_audit'; out.mkdir(parents=True,exist_ok=True); (out/'result.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(json.dumps(result,indent=2,sort_keys=True))
if failures: raise SystemExit(2)
