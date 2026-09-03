#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 302.

Combine independently validated Iterations 296 and 301.

296 supplies the four actual weight-completed direct-timelike TrU1 bubble-family
normalized cut coefficients at the frozen s=0.016 external row.
301 proves, in the explicit HV-like barred-external / D-loop split and through
the bubble degree ceiling <=4, that mu^2 and mu^4 evanescent bubble insertions
vanish in the epsilon->0 normalized discontinuity.

This promotes the bubble-only TrU1 cut subsector in that explicit cut scope.
It does not promote the full finite amplitude, triangle sector, source-completed
Gamma3, linked T_cut, or a Candidate residual.
"""
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
RDIR=HERE.parent/'results'
r296=json.loads((RDIR/'iteration296_timelike_tru1_bubble_dr_laurent_authority.json').read_text())
r301=json.loads((RDIR/'iteration301_hv_evanescent_bubble_cut_protection_authority.json').read_text())

assert r296['iteration']==296 and r296['github_actions']['schema_validator_pass']
assert r301['iteration']==301 and r301['github_actions']['schema_validator_pass']
assert r296['classification'].startswith('PASS_DIRECT_TIMELIKE_TRU1_BUBBLE')
assert r301['classification'].startswith('PASS_HV_EVANESCENT_BUBBLE_CUT_PROTECTION')

coeffs=r296['bubble_cut_finite_coefficients']
poles=r296['bubble_cut_pole_residues']
total=sum(coeffs.values())
total_pole=sum(poles.values())
assert abs(total-r296['sum_four_bubble_cut_finite_coefficients'])<1e-15
assert abs(total_pole-r296['sum_four_bubble_cut_pole_residues'])<1e-15
assert max(abs(x) for x in poles.values())<1e-7
assert r301['max_abs_mu_evanescent_cut_epsilon_to_zero_limit_r_gt_0']<1e-5

result={
 'iteration':302,
 'model_readiness_percent':24,
 'classification':'PASS_ACTUAL_WEIGHT_COMPLETED_TRU1_BUBBLE_NORMALIZED_CUT_SUBSECTOR_PROMOTED_IN_HV_SCOPE',
 'candidate_residual':False,
 'frozen_external_row':{'s':0.016,'ks2':0.0,'ka2':-0.016,'kb2':-0.216,'ks_dot_ka':-0.1},
 'input_authorities':{
   'iteration296':r296['github_actions'],
   'iteration301':r301['github_actions'],
 },
 'four_bubble_cut_coefficients':coeffs,
 'four_bubble_cut_pole_residues':poles,
 'sum_four_bubble_normalized_cut':total,
 'sum_four_bubble_cut_pole_residue':total_pole,
 'evanescent_protection_scope':r301['scope'],
 'statement':'Within the explicit HV-like normalized-cut scope certified by Iteration301, the actual weight-completed TrU1 ordinary+raised bubble contribution at the frozen timelike row is nonzero and equals the reported sum. This is a TrU1 bubble subsector coordinate only.',
 'guardrails':[
   'DO_NOT_MULTIPLY_OR_REINTERPRET_AS_FULL_GAMMA3_WITHOUT_EFFECTIVE_ACTION_AND_SOURCE_COMPLETION_BOOKKEEPING',
   'TRIANGLE_SECTOR_REMAINS_OPEN',
   'FULL_FINITE_AMPLITUDE_REMAINS_SCHEME_SCOPED',
   'K2_LINKED_WARD_SOURCE_CONTACT_COMPLETION_REMAINS_OPEN',
   'NO_COMPARATOR_SUBTRACTED_RESIDUAL_NO_ANSATZ003_NO_FISHER'
 ],
 'next_gate':'derive and audit the evanescent-sensitive direct-timelike triangle normalized-cut basis (ordinary degree<=4 and raised degree<=6), because triangle cuts can carry Laurent poles; only then promote the full e=1,c=2 TrU1 cut.'
}
print(json.dumps(result,indent=2,sort_keys=True))
