#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 428.

Non-promoting conditioning audit after the raw-valid Iteration-421
BLOCKED_CONVERGENCE result.

This revision deliberately separates two prospectively frozen objects:

* Iteration 421: symmetric-cross radius R=1e-5 with multipliers
  {1, 0.75, 0.5, 0.25};
* Iteration 424: an independent fallback contract with frozen mass steps
  {5e-6, 2.5e-6, 1.25e-6} and required 80/120 decimal-digit evaluations.

The first version of this diagnostic incorrectly treated these two geometries as
identical.  That operational/scoping defect is corrected here before any result
is interpreted.  No physical threshold or frozen node is changed.

For the explicitly known Iteration-421 symmetric-cross formula, this audit
translates the unchanged 2e-5 physical tolerance into the maximum absolute
perturbation of the signed four-corner numerator.  For Iteration 424, whose
contract does not itself freeze a particular derivative-stencil formula, the
audit reports its mass steps and the generic h^2 conditioning scale only; it
does not pretend that this is an acceptance budget.

The audit also records that the complete fixed-mass F path still traverses
binary64/numpy complex arithmetic and nested finite-difference numerator
stencils.  Therefore an outer-only mpmath wrapper cannot honestly be described
as a complete 80/120-digit F evaluation.
"""
from __future__ import annotations
import json, re
from pathlib import Path
import numpy as np

ITERATION=428
TARGET_INDEX=2
EXPECTED_CLASS=3
EXPECTED_Q2=-1.0
R421=1.0e-5
MULT421=(1.0,0.75,0.5,0.25)
PHYSICAL_TOL=2.0e-5
FALLBACK424_STEPS=(5.0e-6,2.5e-6,1.25e-6)
FALLBACK424_DIGITS=(80,120)

root=Path(__file__).resolve().parent
p420=root/'iteration420_tru1sq_channel2_symmetric_cross_derivative.py'
p424=root/'iteration424_channel2_high_precision_fallback_contract.py'
p407=root/'iteration407_tru1sq_channel4_analytic_spectral_reduction.py'
p368=root/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
p270=root/'iteration270_vd_physical_b3_nonzero.py'
s420=p420.read_text(); s424=p424.read_text(); s407=p407.read_text(); s368=p368.read_text(); s270=p270.read_text()

source_checks={
    'iteration421_parent_radius_frozen': bool(re.search(r'RADIUS\s*=\s*1\.0e-5',s420)),
    'iteration421_parent_multipliers_frozen': all(x in s420 for x in ['1.0','0.75','0.5','0.25']) and 'RADII_MULT' in s420,
    'iteration421_parent_physical_tol_frozen': bool(re.search(r'PHYSICAL_TOL\s*=\s*2\.0e-5',s420)),
    'iteration421_symmetric_cross_formula_present': 'num/(4.0*r*s)' in s420,
    'iteration424_same_mass_nodes_required': '"same_mass_nodes": True' in s424,
    'iteration424_no_smaller_h_required': '"no_smaller_h": True' in s424,
    'iteration424_precision_80_120': bool(re.search(r'PRECISION_LEVELS_DIGITS\s*=\s*\[80,\s*120\]',s424)),
    'iteration424_frozen_steps': all(tok in s424 for tok in ['5.0e-6','2.5e-6','1.25e-6']) and 'FROZEN_MASS_STEPS' in s424,
    'iteration407_numpy_complex_coefficients': 'np.asarray(train,complex)' in s407,
    'iteration407_complete_numerator_called': 'stripped_limit_massive(alpha,rho*unit_from(z,phi))' in s407,
    'iteration368_nested_first_u1_present': 'first_u1' in s368 and 'Asub' in s368,
    'iteration368_nested_y1_present': 'y1' in s368 and '4e-5' in s368,
    'iteration270_finite_difference_derivative_present': 'deriv5' in s270,
}
if not all(source_checks.values()):
    raise SystemExit(('source_contract_drift',source_checks))

# Iteration-421 has an explicit symmetric-cross quotient.  If delta_N is the
# absolute error in the signed four-corner sum, its induced quotient error is
# delta_N/(4|uv|), hence delta_N_max = 4|uv|*tol.
eps=float(np.finfo(float).eps)
rows421=[]
for mu in MULT421:
    for mv in MULT421:
        u=R421*mu; v=R421*mv
        budget=4.0*abs(u*v)*PHYSICAL_TOL
        rows421.append({
            'u_multiplier':mu,'v_multiplier':mv,'abs_u':u,'abs_v':v,
            'max_abs_signed_corner_sum_error_for_2e-5_quotient_error':budget,
            'budget_in_float64_eps_at_unit_scale':budget/eps,
            'equal_four_corner_share':budget/4.0,
            'equal_corner_share_in_float64_eps_at_unit_scale':budget/(4.0*eps),
        })
tight421=min(rows421,key=lambda x:x['max_abs_signed_corner_sum_error_for_2e-5_quotient_error'])
loose421=max(rows421,key=lambda x:x['max_abs_signed_corner_sum_error_for_2e-5_quotient_error'])

# Iteration-424 freezes step sizes but not, in this contract file, a derivative
# stencil.  Report h^2 only as a conditioning scale.  Do not reinterpret it as
# a physical acceptance threshold.
rows424=[]
for h in FALLBACK424_STEPS:
    rows424.append({
        'frozen_mass_step':h,
        'h_squared':h*h,
        'h_squared_times_unchanged_2e-5_reference':h*h*PHYSICAL_TOL,
        'note':'conditioning scale only; not an Iteration-424 acceptance budget because the contract does not freeze a stencil denominator here',
    })

execution_valid=bool(
    all(source_checks.values()) and len(rows421)==16 and len(rows424)==3 and
    abs(tight421['max_abs_signed_corner_sum_error_for_2e-5_quotient_error']-5.0e-16)<=1e-30 and
    abs(loose421['max_abs_signed_corner_sum_error_for_2e-5_quotient_error']-8.0e-15)<=1e-29 and
    tuple(FALLBACK424_DIGITS)==(80,120)
)
classification=('PASS_CHANNEL2_PRECISION_SURFACE_AND_NODE_CONDITIONING_AUDIT__NON_PROMOTING' if execution_valid
                else 'FAIL_CHANNEL2_PRECISION_SURFACE_AND_NODE_CONDITIONING_AUDIT')
result={
    'iteration':ITERATION,
    'model_readiness_percent':24,
    'candidate_residual':False,
    'scientific_gate_pass':execution_valid,
    'classification':classification,
    'authority_scope':'CONDITIONING_AND_IMPLEMENTATION_AUDIT__NO_PHYSICAL_COORDINATE_PROMOTION',
    'target':{'double_double_global_index':TARGET_INDEX,'class_id':EXPECTED_CLASS,'q_squared':EXPECTED_Q2,'iteration421_status':'BLOCKED_CONVERGENCE'},
    'geometry_separation':{
        'iteration421':{'radius':R421,'radius_multipliers':list(MULT421),'formula':'signed_four_corner_sum/(4*u*v)','physical_tolerance_scaled':PHYSICAL_TOL},
        'iteration424_contract':{'frozen_mass_steps':list(FALLBACK424_STEPS),'required_precision_digits':list(FALLBACK424_DIGITS),'same_mass_nodes':True,'no_smaller_h':True,'stencil_formula_frozen_in_contract_file':False},
    },
    'float64_machine_epsilon':eps,
    'iteration421_accuracy_budget_rows':rows421,
    'iteration421_tightest_budget':tight421,
    'iteration421_loosest_budget':loose421,
    'iteration424_conditioning_scales_not_acceptance_budgets':rows424,
    'source_checks':source_checks,
    'conclusions':[
        'At the smallest Iteration-421 symmetric-cross node |u|=|v|=2.5e-6, a 2e-5 quotient tolerance corresponds to only 5e-16 absolute error in the complete signed four-corner sum.',
        'At unit F scale this is about 2.25 binary64 epsilons for the entire signed sum, before accounting for error in each F evaluation.',
        'Iteration 424 is a distinct frozen fallback geometry: its mass steps are 5e-6, 2.5e-6 and 1.25e-6 and its required precision levels are 80 and 120 decimal digits.',
        'The complete fixed-mass F path includes numpy/complex binary64 processing and nested finite-difference numerator machinery. Outer-only high precision is therefore insufficient to claim a complete 80/120-digit F evaluation.',
        'No Iteration-424 acceptance threshold or stencil is inferred from h^2 alone.'
    ],
    'implementation_requirement_nonacceptance_rule':'A physical Iteration-424 implementation must explicitly document precision provenance for the complete fixed-mass F path, or quantify retained lower-precision sublayers. Any outer-only high-precision implementation is diagnostic until that provenance is closed.',
    'guardrails':['DIAGNOSTIC_ONLY','421_AND_424_GEOMETRIES_KEPT_DISTINCT','NO_NEW_PHYSICAL_THRESHOLD','NO_THRESHOLD_WEAKENING','NO_SMALLER_MASS_STEP','NO_ZERO_FILL','ITERATION424_FROZEN_CONTRACT_UNCHANGED','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid:
    raise SystemExit(2)
