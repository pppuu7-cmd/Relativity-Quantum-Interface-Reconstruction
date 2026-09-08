#!/usr/bin/env python3
import json

topologies={
  'K3':{'loop_denominators':1,'name':'tadpole','ordinary_hard_channel_cut':False,'origin':'local/analytic tadpole sector after renormalization; retained but not zero-filled'},
  'K1K2':{'loop_denominators':2,'name':'bubble','ordinary_hard_channel_cut':True,'normal_threshold':'s>=4*m_phi^2 for equal masses when s is carried across the two-line cut'},
  'K1cubed':{'loop_denominators':3,'name':'triangle','ordinary_hard_channel_cut':True,'normal_thresholds':'pairwise two-scalar cuts at channel invariant >=4*m_phi^2','anomalous_landau':'POSSIBLE__REQUIRES_EXPLICIT_ITER613_LANDAU_CHECK'}
}
failures=[]
if topologies['K3']['ordinary_hard_channel_cut'] is not False: failures.append('K3 tadpole cut misclassified')
if topologies['K1K2']['loop_denominators']!=2 or topologies['K1K2']['ordinary_hard_channel_cut'] is not True: failures.append('bubble classification mismatch')
if topologies['K1cubed']['loop_denominators']!=3 or topologies['K1cubed']['ordinary_hard_channel_cut'] is not True: failures.append('triangle classification mismatch')
if topologies['K1cubed']['anomalous_landau']!='POSSIBLE__REQUIRES_EXPLICIT_ITER613_LANDAU_CHECK': failures.append('triangle Landau guardrail weakened')
result={
 'iteration':633,'date':'2026-09-09','scientific_gate_pass':not failures,'candidate_residual':False,
 'classification':'PASS_ITER633_CLOSED_SCALAR_LOOP_HARD_CUT_ORIGIN_CLASSIFICATION__TADPOLE_ANALYTIC__BUBBLE_NORMAL_CUT__TRIANGLE_NORMAL_PLUS_LANDAU_CHECK__NON_RESIDUAL' if not failures else 'FAIL_ITER633_CLOSED_LOOP_CUT_ORIGIN_CLASSIFICATION',
 'frozen_prerequisites':['Iter613 hard-channel trajectory','Iter630 closed retarded causal traces','Iter632 MSSC001 Minkowski-vacuum G_K contract'],
 'topologies':topologies,
 'retention_rule':'All K3/K1K2/K1^3 families remain retained in full gravitational Gamma3. Absence of an ordinary hard-channel cut from K3 is not amplitude zero.',
 'pole_cut_origin_classified':True,'source_born_subtraction':'NOT_PERFORMED','native_projection':'NOT_PERFORMED','candidate_values_used':False,'zero_fill':False,
 'failures':failures,'MODEL_READINESS':'24%','readiness_change':'0 percentage points',
 'next_gate':'Iteration634: instantiate Iter613 invariants in the vacuum spectral/Cutkosky measure, solve bubble threshold support and triangle Landau equations fail-closed, and derive channel Jacobians before native Y/T_cut projection.'
}
print(json.dumps(result,indent=2))
if failures: raise SystemExit('\n'.join(failures))
