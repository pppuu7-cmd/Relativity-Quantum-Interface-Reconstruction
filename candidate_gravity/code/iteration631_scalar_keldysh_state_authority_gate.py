#!/usr/bin/env python3
import json

# Authority/identifiability gate, not a choice of state.  Iter627 fixes the
# causal r/a matrix slots and G_R for the measured open scalar response, but its
# frozen contract contains no initial density matrix / occupation / Hadamard
# boundary condition for G_K.  Demonstrate non-uniqueness without Candidate data:
# for the same spectral function rho=(G_R-G_A), stationary Gaussian bosonic
# states with occupations n=0 and n=1 have distinct statistical factors
# G_K=(1+2n) rho while sharing the same G_R/G_A causal support.

examples=[
  {'label':'n0','occupation_n':0,'G_K_over_rho':1},
  {'label':'n1','occupation_n':1,'G_K_over_rho':3}
]
same_retarded_advanced=True
distinct_GK=examples[0]['G_K_over_rho'] != examples[1]['G_K_over_rho']
iter627_explicit_state_boundary_condition=False
failures=[]
if not same_retarded_advanced: failures.append('causal propagators unexpectedly state-dependent in structural witness')
if not distinct_GK: failures.append('state non-uniqueness witness collapsed')
if iter627_explicit_state_boundary_condition: failures.append('Iter627 unexpectedly marked as explicit scalar-state contract')

result={
  'iteration':631,
  'date':'2026-09-09',
  'scientific_gate_pass':not failures,
  'candidate_residual':False,
  'classification':'BLOCKED_ITER631_ITER627_CTP_CAUSAL_CONTRACT_DOES_NOT_FIX_SCALAR_KELDYSH_STATE__GK_REQUIRES_PROSPECTIVE_STATE_BOUNDARY_CONDITION__NON_RESIDUAL' if not failures else 'FAIL_ITER631_SCALAR_STATE_AUTHORITY_AUDIT',
  'authority_statement':{
    'iter627_fixes':'r/a rotation, physical h_a=0, open measured G_phi^{ra}=G_R, causal matrix slots G_rr=G_K/G_ra=G_R/G_ar=G_A/G_aa=0',
    'iter627_does_not_fix':'initial density matrix, occupation distribution, vacuum/Hadamard prescription, temperature, or an absolute G_K state normalization',
    'therefore':'G_R/G_A plus the Iter627 causal slot structure do not uniquely determine G_K'
  },
  'nonuniqueness_witness':{
    'rho_definition':'rho proportional to G_R-G_A (overall convention irrelevant to the witness)',
    'states':examples,
    'same_G_R_G_A':same_retarded_advanced,
    'distinct_G_K':distinct_GK
  },
  'allowed_resolution':'prospectively freeze a same-parent scalar state/boundary-condition contract before inspecting closed-loop/native Candidate values; then compute G_K and the Iter630 closed retarded loop on Iter613 kinematics',
  'forbidden_resolution':'do not set G_K=0, vacuum, thermal, or fit a distribution from Iter582/Candidate values without a prospective state contract',
  'iter628_open_response':'PRESERVED',
  'source_born_subtraction':'NOT_PERFORMED',
  'native_projection':'NOT_PERFORMED',
  'candidate_values_used':False,
  'zero_fill':False,
  'failures':failures,
  'MODEL_READINESS':'24%',
  'readiness_change':'0 percentage points',
  'next_gate':'Iteration632: prospective same-parent scalar-state contract (or independent historical authority if found) defining the Minkowski/other admissible G_K boundary condition before numerical closed-loop pole/cut evaluation.'
}
print(json.dumps(result,indent=2))
if failures: raise SystemExit('\n'.join(failures))
