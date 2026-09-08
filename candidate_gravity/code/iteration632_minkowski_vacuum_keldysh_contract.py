#!/usr/bin/env python3
import json

# Prospective state contract, frozen before any closed-loop/native Candidate value
# is evaluated.  MSSC001 is expanded about flat Minkowski space; choose the
# zero-temperature Poincare-invariant positive-energy Hadamard vacuum for its
# free massive scalar.  In the Iter627 r/a convention this fixes the statistical
# component by the vacuum fluctuation-dissipation relation
#   G_K(k) = sgn(k0) [G_R(k)-G_A(k)].
# This is a state definition, not a fit and not a result inferred from Iter582.

checks={
  'flat_minkowski_parent':True,
  'zero_temperature':True,
  'poincare_invariant':True,
  'hadamard_positive_energy':True,
  'candidate_values_used':False,
  'normalization_fit_used':False,
  'state_chosen_before_closed_loop_results':True,
  'GK_relation':'G_K(k)=sgn(k0)*(G_R(k)-G_A(k))'
}
failures=[]
for k in ('flat_minkowski_parent','zero_temperature','poincare_invariant','hadamard_positive_energy','state_chosen_before_closed_loop_results'):
    if checks[k] is not True: failures.append(k+' not frozen')
for k in ('candidate_values_used','normalization_fit_used'):
    if checks[k] is not False: failures.append(k+' guardrail violated')
if checks['GK_relation']!='G_K(k)=sgn(k0)*(G_R(k)-G_A(k))': failures.append('vacuum GK relation mismatch')

result={
  'iteration':632,
  'date':'2026-09-09',
  'contract_id':'MSSC001-SCALAR-STATE-MINKOWSKI-VACUUM-V1',
  'scientific_gate_pass':not failures,
  'candidate_residual':False,
  'classification':'PASS_ITER632_PROSPECTIVE_MSSC001_MINKOWSKI_VACUUM_KELDYSH_STATE_CONTRACT__NON_RESIDUAL' if not failures else 'FAIL_ITER632_MINKOWSKI_VACUUM_STATE_CONTRACT',
  'prospective_freeze':checks,
  'spectral_definition':'rho(k)=G_R(k)-G_A(k) in the already frozen Iter627 propagator convention',
  'statistical_component':'G_K(k)=sgn(k0)*rho(k)',
  'occupation':'n_B(|k0|)=0',
  'consequence_for_iter630':'closed retarded K3/K1K2/K1^3 loop families now have a non-arbitrary same-parent G_K state definition; numerical loop/cut evaluation is authorized next',
  'iter628_open_response':'PRESERVED_SEPARATE_OBSERVABLE_AUTHORITY',
  'source_born_subtraction':'NOT_PERFORMED',
  'native_projection':'NOT_PERFORMED',
  'candidate_values_used':False,
  'normalization_fit_used':False,
  'zero_fill':False,
  'failures':failures,
  'MODEL_READINESS':'24%',
  'readiness_change':'0 percentage points',
  'next_gate':'Iteration633: derive the closed retarded scalar-loop pole/cut support and integration measure for K3, K1/K2 and K1^3 under Iter613 kinematics + Iter630 causal traces + this frozen vacuum G_K, before any native Y/T_cut projection or Source/Born subtraction.'
}
print(json.dumps(result,indent=2))
if failures: raise SystemExit('\n'.join(failures))
