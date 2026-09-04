#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 428.

Non-promoting conditioning audit for the now-authorized Iteration-424 fallback.

Iteration 421 is raw-valid BLOCKED_CONVERGENCE at the prospectively frozen
physical tolerance 2e-5.  Its symmetric-cross representation uses

  [F(u,v)-F(u,-v)-F(-u,v)+F(-u,-v)]/(4 u v)

with R=1e-5 and radius multipliers {1, 0.75, 0.5, 0.25}.  This audit translates
the unchanged physical tolerance into the maximum absolute perturbation of the
four-corner numerator combination at every frozen |u|,|v| pair.  It also audits
source evidence that the complete fixed-mass F still contains binary64/numpy
numerator arithmetic and nested finite-difference stencils, so an outer-only
high-precision wrapper cannot by itself be described as a true 80/120-digit
fixed-node evaluation.

No new acceptance criterion is introduced.  The purpose is implementation
conditioning only; Iteration 424's prospectively frozen thresholds and nodes are
unchanged.
"""
from __future__ import annotations
import json, math, sys
from pathlib import Path
import numpy as np

ITERATION=428
TARGET_INDEX=2
EXPECTED_CLASS=3
EXPECTED_Q2=-1.0
R=1.0e-5
MULT=(1.0,0.75,0.5,0.25)
PHYSICAL_TOL=2.0e-5

root=Path(__file__).resolve().parent
p421=root/'iteration421_tru1sq_channel2_symmetric_cross_collision_recovery.py'
p424=root/'iteration424_channel2_high_precision_fallback_contract.py'
p407=root/'iteration407_tru1sq_channel4_analytic_spectral_reduction.py'
p368=root/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
p270=root/'iteration270_vd_physical_b3_nonzero.py'
s421=p421.read_text(); s424=p424.read_text(); s407=p407.read_text(); s368=p368.read_text(); s270=p270.read_text()

source_checks={
    'iteration421_radius_frozen': 'RADIUS=1.0e-5' in s421,
    'iteration421_multipliers_frozen': 'RADIUS_MULTIPLIERS=(1.0,0.75,0.5,0.25)' in s421,
    'iteration421_physical_tol_frozen': 'PHYSICAL_TOL=2.0e-5' in s421,
    'iteration424_same_nodes_required': "'same_mass_steps_and_nodes':True" in s424,
    'iteration424_no_smaller_h_required': "'no_smaller_h':True" in s424,
    'iteration424_primary_80_digits': "'primary_decimal_digits':80" in s424,
    'iteration424_verification_120_digits': "'verification_decimal_digits':120" in s424,
    'iteration407_numpy_complex_coefficients': 'np.asarray(train,complex)' in s407,
    'iteration407_complete_numerator_called': 'stripped_limit_massive(alpha,rho*unit_from(z,phi))' in s407,
    'iteration368_nested_Asub_h1': 'def first_u1(p,M,h1=1e-4,h2=5e-4)' in s368,
    'iteration368_nested_y1_h': 'def y1(p,mu,h=4e-5)' in s368,
    'iteration270_five_point_derivative': 'def deriv5(f,x,h):' in s270,
}
if not all(source_checks.values()):
    raise SystemExit(('source_contract_drift',source_checks))

# The cross quotient error caused by an absolute perturbation delta_N in the
# signed four-corner numerator is |delta_N|/(4|uv|).  Therefore the unchanged
# physical tolerance implies delta_N_max = 4|uv|*tol.
eps=float(np.finfo(float).eps)
rows=[]
for mu in MULT:
    for mv in MULT:
        u=R*mu; v=R*mv
        budget=4.0*abs(u*v)*PHYSICAL_TOL
        rows.append({
            'u_multiplier':mu,'v_multiplier':mv,
            'abs_u':u,'abs_v':v,
            'max_abs_signed_corner_sum_error_for_physical_tol':budget,
            'budget_in_float64_eps_at_unit_scale':budget/eps,
            'equal_independent_corner_error_budget_if_four_sum_bound':budget/4.0,
            'equal_corner_budget_in_float64_eps_at_unit_scale':budget/(4.0*eps),
        })

minrow=min(rows,key=lambda x:x['max_abs_signed_corner_sum_error_for_physical_tol'])
maxrow=max(rows,key=lambda x:x['max_abs_signed_corner_sum_error_for_physical_tol'])

# Use the actually recorded Iteration-421 miss only as a scale translation, not
# as a new criterion.
observed_stability=2.2720400683804223e-5
observed_fit=2.585665489102237e-5
obs=[]
for metric,val in [('max_stability_scaled',observed_stability),('max_required_fit_residual_scaled',observed_fit)]:
    for m in (1.0,0.25):
        u=v=R*m
        obs.append({
            'metric':metric,'scaled_value':val,'equal_radius_multiplier':m,
            'equivalent_signed_corner_sum_scale':4.0*u*v*val,
        })

execution_valid=bool(
    all(source_checks.values()) and
    abs(minrow['max_abs_signed_corner_sum_error_for_physical_tol']-5.0e-16)<=1e-30 and
    abs(maxrow['max_abs_signed_corner_sum_error_for_physical_tol']-8.0e-15)<=1e-29 and
    len(rows)==16
)
classification=('PASS_CHANNEL2_FROZEN_MASS_NODE_ACCURACY_BUDGET__NON_PROMOTING' if execution_valid
                else 'FAIL_CHANNEL2_FROZEN_MASS_NODE_ACCURACY_BUDGET')
result={
    'iteration':ITERATION,
    'model_readiness_percent':24,
    'candidate_residual':False,
    'scientific_gate_pass':execution_valid,
    'classification':classification,
    'authority_scope':'CONDITIONING_AND_IMPLEMENTATION_AUDIT__NO_PHYSICAL_COORDINATE_PROMOTION',
    'target':{'double_double_global_index':TARGET_INDEX,'class_id':EXPECTED_CLASS,'q_squared':EXPECTED_Q2,'iteration421_status':'BLOCKED_CONVERGENCE'},
    'frozen_geometry':{'radius':R,'radius_multipliers':list(MULT),'physical_tolerance_scaled':PHYSICAL_TOL,'cross_formula':'signed_four_corner_sum/(4*u*v)'},
    'float64_machine_epsilon':eps,
    'accuracy_budget_rows':rows,
    'tightest_budget':minrow,
    'loosest_budget':maxrow,
    'observed_iteration421_miss_translated_to_corner_sum_scale':obs,
    'source_checks':source_checks,
    'conclusions':[
        'At the smallest frozen |u|=|v|=2.5e-6 node, a 2e-5 cross-quotient tolerance corresponds to only 5e-16 absolute error in the signed four-corner sum.',
        'At unit F scale this is only about 2.25 float64 machine epsilons for the entire signed sum, before accounting for error in each individual F evaluation.',
        'The complete frozen F includes numpy/complex binary64 numerator processing and nested finite-difference stencils; therefore promoting only outer analytic moments/extrapolation to mpmath would not constitute a true 80/120-digit fixed-node evaluation.',
        'This audit does not change Iteration-424 acceptance criteria. It specifies the numerical surface that a faithful high-precision implementation must control.'
    ],
    'implementation_requirement_nonacceptance_rule':'For a true Iteration-424 implementation, precision provenance must cover the complete fixed-mass F evaluation (or explicitly quantify any retained binary64 sublayer); outer-only high precision must be labeled diagnostic rather than 80/120-digit physical authority.',
    'guardrails':['DIAGNOSTIC_ONLY','NO_NEW_PHYSICAL_THRESHOLD','NO_THRESHOLD_WEAKENING','NO_SMALLER_MASS_STEP','NO_ZERO_FILL','ITERATION424_FROZEN_CONTRACT_UNCHANGED','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid:
    raise SystemExit(2)
