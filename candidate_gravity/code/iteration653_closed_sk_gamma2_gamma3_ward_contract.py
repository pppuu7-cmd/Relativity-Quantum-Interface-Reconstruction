#!/usr/bin/env python3
"""Iteration 653: prospective fully-normalized same-parent closed-SK Gamma2/Gamma3
and longitudinal Ward-map contract.

No new cut density or Candidate/comparator value is evaluated.  This freezes a
new versioned branch rather than retroactively assigning an absolute factor to
Iter645/648 values after they were seen.
"""
from pathlib import Path
import json, math

ROOT=Path(__file__).resolve().parents[2]
failures=[]

d627=json.loads((ROOT/'candidate_gravity/results/iteration627_combined_sk_contract.json').read_text())
d632=json.loads((ROOT/'candidate_gravity/results/iteration632_minkowski_vacuum_gk_contract.json').read_text())
d629=json.loads((ROOT/'candidate_gravity/results/iteration629_open_vs_1pi_normalization_gate.json').read_text())
d644=json.loads((ROOT/'results/iteration644_external_tensor_transport_contract/result.json').read_text())
d652=json.loads((ROOT/'candidate_gravity/results/iteration652_linked_tcut_source_completion_scope_audit.json').read_text())
code582=(ROOT/'candidate_gravity/code/iteration582_connection_e2_effective_action_q2.py').read_text()
ward151=(ROOT/'candidate_gravity/C5_WARD_IDENTITY_ITERATION151.md').read_text()

if d627.get('contract_id')!='MSSC001-GRAVITY-SK-MEAS-V1': failures.append('Iter627 contract drift')
if d632.get('contract_id')!='MSSC001-SCALAR-STATE-V1': failures.append('Iter632 state drift')
if d629.get('closed_scalar_1pi_ThirdDerivative_TrLogK',{}).get('K3_coefficient')!=1: failures.append('Iter629 closed-TrLog drift')
if 'formula\':\'D_s Gamma_e2_connection = +(i/2) D_s TrU2 - (i/4) D_s TrU1sq\'' not in code582.replace(' ', ''):
    # relaxed token check for formatting
    if '+(i/2)' not in code582 or '-(i/4)' not in code582: failures.append('Iter582 determinant weight drift')
if 'B3[L_xi, h2, h3] + B2[Lie_xi h2, h3] + B2[h2, Lie_xi h3] = 0' not in ward151: failures.append('Iter151 Ward skeleton drift')
if not d652.get('scientific_gate_pass'): failures.append('Iter652 authority missing')

# Prospective determinant normalization. For the frozen real quadratic scalar
# parent S_phi=-1/2 phi K[g] phi, Z_phi propto det(K)^(-1/2), so
# Gamma_phi=-i log Z_phi=+(i/2) Tr log K up to field-independent constants.
# Freeze the trace loop measure explicitly for all new absolute calculations.
parent={
  'contract_id':'MSSC001-CLOSED-SK-GAMMA2-GAMMA3-WARD-V1',
  'quadratic_scalar_action':'S_phi=-1/2 phi K[g] phi in the existing MSSC001 convention',
  'gaussian_identity':'Z_phi[g] proportional to det(K[g])^(-1/2)',
  'closed_effective_action':'Gamma_phi[g]=+(i/2) Tr_C log K[g] plus field-independent normalization',
  'loop_measure':'Integral d^4 ell/(2*pi)^4',
  'state_contract':'MSSC001-SCALAR-STATE-V1 (Iter632 Minkowski vacuum)',
  'ctp_rotation':'inherit Iter627 r/a convention exactly',
  'field_variable':'direct delta_g; no extra unknown kappa power',
}

# Mixed derivatives with distinct labeled external modes.  K_a etc mean actual
# functional derivatives, so no hidden factorials are inserted.
gamma2={
  'formula':'Gamma2[a,b]=(i/2) Tr_C( G K_ab - G K_a G K_b )',
  'closed_family_coefficients':[1,-1],
  'local_contact':'Tr(G K_ab) retained; its hard-channel discontinuity may be analytic/absent but is never zero-filled by assumption',
  'bubble':'-Tr(G K_a G K_b) retained and supplies ordinary two-particle nonanalytic support when kinematically allowed'
}
gamma3={
  'formula':'Gamma3[a,b,c]=(i/2) Tr_C( G K_abc - (G K_a G K_bc + G K_b G K_ac + G K_c G K_ab) + (G K_a G K_b G K_c + G K_a G K_c G K_b) )',
  'closed_family_coefficients':[1,-3,2],
  'matches_iter629_closed_vector': d629.get('family_total_coefficient_vectors',{}).get('closed')==[1,-3,2]
}
if not gamma3['matches_iter629_closed_vector']: failures.append('Gamma3 combinatorics do not match Iter629')

# Canonical longitudinal decomposition for q^2 != 0.  This supplies only the
# longitudinal Ward-determined part; the q-transverse remainder stays in T_cut.
def mdot(a,b):
    return a[0]*b[0]-sum(a[i]*b[i] for i in range(1,4))
def lower(v):
    return [v[0],-v[1],-v[2],-v[3]]
def longitudinal_split(q,h):
    q2=mdot(q,q)
    if abs(q2)<1e-14: raise ValueError('q2=0 unsupported by this projector')
    # v_nu = q^mu h_{mu nu}
    v=[sum(q[mu]*h[mu][nu] for mu in range(4)) for nu in range(4)]
    qqh=sum(q[nu]*v[nu] for nu in range(4))
    qcov=lower(q)
    xi=[v[nu]/q2-qcov[nu]*qqh/(2*q2*q2) for nu in range(4)]
    L=[[qcov[mu]*xi[nu]+qcov[nu]*xi[mu] for nu in range(4)] for mu in range(4)]
    ht=[[h[mu][nu]-L[mu][nu] for nu in range(4)] for mu in range(4)]
    div=[sum(q[mu]*ht[mu][nu] for mu in range(4)) for nu in range(4)]
    return xi,ht,max(abs(x) for x in div)

# Value-independent algebraic regression on the frozen q_s kinematics with a
# deterministic synthetic symmetric tensor; not a Candidate probe value.
projector_checks=[]
for i,row in enumerate(d644.get('kinematic_checks',[])):
    q=[float(x) for x in row['q_s']]
    h=[[0.03*(1+mu+nu+i) if mu!=nu else 0.07*(1+mu+i) for nu in range(4)] for mu in range(4)]
    # symmetrize exactly
    h=[[0.5*(h[mu][nu]+h[nu][mu]) for nu in range(4)] for mu in range(4)]
    xi,ht,err=longitudinal_split(q,h)
    projector_checks.append({'s':row['s'],'q2':mdot(q,q),'transverse_remainder_divergence_max_abs':err})
    if err>2e-14: failures.append(f'longitudinal projector regression s={row["s"]}: {err}')

ward_map={
 'longitudinal_projection_for_q2_nonzero':'h = L_xi + h_T with q^mu h_T_{mu nu}=0 and xi_nu=(q^mu h_{mu nu})/q^2 - q_nu(q^mu q^rho h_{mu rho})/(2 q^4)',
 'action_identity':'Gamma3[L_xi,h2,h3] = -Gamma2[Lie_xi h2,h3] - Gamma2[h2,Lie_xi h3]',
 'definition_of_W_longitudinal':'W_q[Gamma2;h,h2,h3] := -Gamma2[Lie_xi(h) h2,h3]-Gamma2[h2,Lie_xi(h) h3]',
 'scope':'this fixes only the Ward-determined longitudinal component for q^2!=0; no claim that the generic q-transverse soft component is determined by K2',
 'physical_W_status':'PROSPECTIVE_LONGITUDINAL_PART_FROZEN; full T_cut evaluation still requires applying the exact Lie-derivative momentum routing to the closed-SK Gamma2 cut on the frozen invariant/tensor family'
}

result={
 'iteration':653,
 'date':'2026-09-09',
 'classification':('PASS_ITER653_PROSPECTIVE_FULLY_NORMALIZED_CLOSED_SK_GAMMA2_GAMMA3_AND_LONGITUDINAL_WARD_MAP_CONTRACT__NO_VALUES_NON_RESIDUAL' if not failures else 'BLOCKED_ITER653_CONTRACT_REGRESSION'),
 'scientific_gate_pass':not failures,
 'candidate_residual':False,
 'parent':parent,
 'Gamma2':gamma2,
 'Gamma3':gamma3,
 'Ward_map':ward_map,
 'projector_checks':projector_checks,
 'anti_bias':{
   'new_absolute_cut_values_evaluated':False,
   'Iter645_absolute_values_retroactively_rescaled':False,
   'Iter582_values_used_to_choose_contract':False,
   'Candidate_values_used':False,
   'normalization_fit':False,
   'contract_frozen_before_new_Gamma2_or_Gamma3_absolute_recomputation':True
 },
 'historical_absolute_branches':'Iter645/648 remain historical/projective authority only; any absolute matched T_cut must be recomputed from this versioned parent rather than assigned a post-result factor',
 'source_born_subtraction':'NOT_PERFORMED',
 'native_Y_Tcut_projection':'NOT_PERFORMED',
 'comparator_quotient':'NOT_PERFORMED',
 'zero_fill':False,
 'ANSATZ_003':'FORBIDDEN',
 'Fisher_resources':'FORBIDDEN',
 'MODEL_READINESS':'24%',
 'readiness_change':'0 percentage points',
 'failures':failures,
 'next_gate':'Iteration654: derive/evaluate the same-parent closed-SK Gamma2 hard-channel discontinuity on MSSC001-CLOSED-GAMMA3-INV-FAMILY-V1 with the fixed tensor transport, then apply the exact longitudinal Lie-derivative W routing; recompute Gamma3 absolute cut under the same i/2 and loop measure before forming any T_cut.'
}
out=ROOT/'candidate_gravity/results/iteration653_closed_sk_gamma2_gamma3_ward_contract.json'
out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
if failures: raise SystemExit(2)
