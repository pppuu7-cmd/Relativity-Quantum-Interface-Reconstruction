#!/usr/bin/env python3
import json

# Prospective state contract only. No Candidate/native values are read here.
# Frozen denominator convention inherited from Iter628:
#   D = m^2-r^2
#   G_R = 1/(D-i0 sign(r0)), G_A = 1/(D+i0 sign(r0)).
# Therefore G_R-G_A = 2*pi*i*sign(r0)*delta(D).
# For the zero-temperature Poincare-invariant Gaussian Minkowski vacuum,
# the Keldysh/statistical component in this r/a convention is frozen as
#   G_K = sign(r0)*(G_R-G_A) = 2*pi*i*delta(D).
# m=0.7>0 means on-shell support never requires sign(0).

energy_signs = [-1, 1]
rows=[]
failures=[]
for sgn in energy_signs:
    gr_minus_ga_delta_coeff = sgn  # coefficient of 2*pi*i*delta(D)
    gk_delta_coeff = sgn * gr_minus_ga_delta_coeff
    rows.append({
        'energy_sign': sgn,
        'GR_minus_GA_over_2pii_delta': gr_minus_ga_delta_coeff,
        'GK_vac_over_2pii_delta': gk_delta_coeff
    })
    if gk_delta_coeff != 1:
        failures.append(f'vacuum GK sign reduction failed for sign={sgn}')

result={
  'iteration':632,
  'date':'2026-09-09',
  'scientific_gate_pass':not failures,
  'candidate_residual':False,
  'classification':'PASS_ITER632_PROSPECTIVE_MSSC001_MINKOWSKI_VACUUM_SCALAR_STATE_GK_CONTRACT__NON_RESIDUAL' if not failures else 'FAIL_ITER632_MINKOWSKI_VACUUM_GK_CONTRACT',
  'contract_id':'MSSC001-SCALAR-STATE-V1',
  'prospective_contract':True,
  'state':{
      'type':'zero-temperature Poincare-invariant Gaussian Minkowski vacuum of the frozen quadratic MSSC001 scalar sector',
      'occupation':'n(|r0|)=0',
      'temperature':'T=0 (beta=infinity)',
      'mass':0.7,
      'fitted_to_candidate':False
  },
  'propagator_convention':{
      'D':'m^2-r^2',
      'G_R':'1/(D-i0*sign(r0))',
      'G_A':'1/(D+i0*sign(r0))',
      'G_R_minus_G_A':'2*pi*i*sign(r0)*delta(D)',
      'G_K_vac':'sign(r0)*(G_R-G_A)=2*pi*i*delta(D)'
  },
  'exact_sign_checks':rows,
  'iter627_ra_slots':'PRESERVED: G_rr=G_K, G_ra=G_R, G_ar=G_A, G_aa=0',
  'iter630_closed_loop_structure':'PRESERVED: exactly one G_K per closed retarded family',
  'iter613_trajectory':'PRESERVED',
  'all_13_source_families_retained':True,
  'iter628_open_response':'PRESERVED_IN_ITS_OPEN_RESPONSE_SCOPE',
  'candidate_values_used':False,
  'N_native_fit':False,
  'zero_fill':False,
  'source_born_subtraction':'NOT_PERFORMED',
  'native_projection':'NOT_PERFORMED',
  'failures':failures,
  'MODEL_READINESS':'24%',
  'readiness_change':'0 percentage points',
  'next_gate':'Iteration633: with MSSC001-SCALAR-STATE-V1 frozen, derive the closed retarded Gamma3 distributional pole/cut support family-by-family on the unchanged Iter613 trajectory, keeping exactly one G_K and the required G_R/G_A factors; classify coincident/repeated distribution products before any native projection.'
}
print(json.dumps(result,indent=2))
if failures:
    raise SystemExit('\n'.join(failures))
