#!/usr/bin/env python3
"""Iteration 654: audit whether the current finite closed-Gamma3 family is the
soft three-point observable required by frozen Iter205/175 T_cut.

No new cut values are computed.  This is a fail-closed observable-identity audit.
"""
from pathlib import Path
import json, math

ROOT=Path(__file__).resolve().parents[2]
failures=[]

d205=json.loads((ROOT/'results/linked_nonanalytic_cut_protocol_iteration205.json').read_text())
d175=json.loads((ROOT/'results/soft_ward_transverse_decomposition_iteration175.json').read_text())
d636=json.loads((ROOT/'candidate_gravity/results/iteration636_closed_gamma3_invariant_family_contract.json').read_text())
d644=json.loads((ROOT/'results/iteration644_external_tensor_transport_contract/result.json').read_text())
d653=json.loads((ROOT/'candidate_gravity/results/iteration653_closed_sk_gamma2_gamma3_ward_contract.json').read_text())

if d205.get('proposed_coordinate')!='T_cut = D Gamma3_ret,soft - W[D K2] in one source-completed convention':
    failures.append('Iter205 linked target drift')
if not str(d175.get('decomposition','')).startswith('Gamma3_soft = W[K2]'):
    failures.append('Iter175 soft decomposition drift')
if d636.get('contract',{}).get('external_channel')!='s := q_s^2 > 0':
    failures.append('Iter636 hard-channel family drift')
if d644.get('contract_id')!='MSSC001-CLOSED-GAMMA3-TENSOR-TRANSPORT-V1':
    failures.append('Iter644 tensor family drift')
if d653.get('parent',{}).get('contract_id')!='MSSC001-CLOSED-SK-GAMMA2-GAMMA3-WARD-V1':
    failures.append('Iter653 normalized parent missing')

rows=[]
for r in d644.get('kinematic_checks',[]):
    norms={}
    for leg in ('q_s','q_a','q_b'):
        q=[float(x) for x in r[leg]]
        norms[leg]=math.sqrt(sum(x*x for x in q))
    inv=[float(x) for x in r['invariants']]
    rows.append({'s':float(r['s']),'invariants':inv,'euclidean_fourvector_norms':norms,
                 'minimum_external_fourvector_norm':min(norms.values()),
                 'minimum_abs_external_invariant':min(abs(x) for x in inv)})

if not rows: failures.append('Iter644 kinematic rows absent')
min_norm=min((r['minimum_external_fourvector_norm'] for r in rows),default=0.0)
min_inv=min((r['minimum_abs_external_invariant'] for r in rows),default=0.0)
# In the frozen finite family t=0.14 and u=0.34 are fixed, q_s^2=s>=1 on
# contract/transport checks.  None of the three external four-vectors tends to 0.
finite_family_has_soft_leg = min_norm < 1e-12
if finite_family_has_soft_leg:
    failures.append('unexpected soft external leg in Iter644 finite family')

result={
 'iteration':654,
 'date':'2026-09-09',
 'classification':(
   'BLOCKED_ITER654_CURRENT_S_WITH_TU_FIXED_CLOSED_GAMMA3_FAMILY_IS_FINITE_MOMENTUM_NOT_FROZEN_SOFT_T_CUT__NEW_PROSPECTIVE_SOFT_KINEMATIC_CONTRACT_REQUIRED_NON_RESIDUAL'
   if not failures else 'BLOCKED_ITER654_AUTHORITY_OR_KINEMATIC_INPUT_DRIFT__NON_RESIDUAL'),
 'scientific_gate_pass':not failures,
 'candidate_residual':False,
 'MODEL_READINESS':'24%',
 'readiness_change':'0 percentage points',
 'frozen_target':{
   'Iter205':'T_cut = D_s Gamma3_ret,soft - W[D_s K2]',
   'Iter175':'Gamma3_soft = W[K2] + transverse/nonminimal soft structure + higher-soft-order'
 },
 'current_family':{
   'contract_id':'MSSC001-CLOSED-GAMMA3-INV-FAMILY-V1',
   'definition':'q_s^2=s>0 varied while q_a^2=t0=0.14 and q_b^2=u0=0.34 remain fixed; q_s+q_a+q_b=0',
   'tensor_transport':'MSSC001-CLOSED-GAMMA3-TENSOR-TRANSPORT-V1',
   'soft_leg_present':False,
   'minimum_external_fourvector_norm_across_audited_rows':min_norm,
   'minimum_abs_external_invariant_across_audited_rows':min_inv,
   'rows':rows
 },
 'scope_conclusion':(
   'Iterations636-648 remain valid finite-momentum closed-Gamma3 support/projective diagnostics in their declared scope, but they do not instantiate the exact soft three-point observable named in frozen Iter205/175. Iter653 remains valid as a generic q^2!=0 normalized closed-SK Gamma2/Gamma3 parent and longitudinal decomposition; it does not by itself supply the missing soft kinematics.'
 ),
 'forbidden_inference':[
   'do not identify finite-family Iter645/648 values with Gamma3_ret,soft',
   'do not evaluate W[D_s K2] on the finite family and call it the frozen T_cut',
   'do not set one existing leg to zero after inspecting cut values',
   'do not discard finite-family results; retain them as finite-momentum diagnostics'
 ],
 'next_contract_requirements':{
   'contract_id':'MSSC001-CLOSED-SK-SOFT-TCUT-KIN-V1',
   'must_be_frozen_before_new_values':[
      'soft leg label selected prospectively',
      'soft scaling parameter epsilon and direction/polarization transport',
      'hard two-point momentum p with hard invariant s held as the D_s variable',
      'momentum closure q_soft(epsilon)+p+q_other(epsilon)=0',
      'epsilon->0 limit with q_soft four-vector ->0 and q_other->-p',
      'which hard invariants/state/tensor components are held fixed under D_s and under epsilon->0',
      'order of limits/discontinuity: define whether D_s is taken before or after soft extraction and prove/declare commutation domain',
      'same Iter653 i/2, loop measure, r/a state and no Candidate-value tuning'
   ]
 },
 'source_born_subtraction':'NOT_PERFORMED',
 'native_Y_Tcut_projection':'NOT_PERFORMED',
 'comparator_quotient':'NOT_PERFORMED',
 'zero_fill':False,
 'ANSATZ_003':'FORBIDDEN',
 'Fisher_resources':'FORBIDDEN',
 'failures':failures,
 'next_gate':'Iteration655: prospectively freeze MSSC001-CLOSED-SK-SOFT-TCUT-KIN-V1, preferably reusing a pre-Candidate soft direction/polarization convention if an exact compatible authority exists; no cut values before the freeze.'
}
out=ROOT/'candidate_gravity/results/iteration654_soft_target_vs_finite_family_compatibility_audit.json'
out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
if failures: raise SystemExit(2)
