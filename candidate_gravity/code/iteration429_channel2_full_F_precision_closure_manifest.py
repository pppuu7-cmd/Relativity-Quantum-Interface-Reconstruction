#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 429.

Static precision-closure manifest for the authorized Iteration-424 fallback.
This is non-promoting and changes no physics.  It identifies the source layers
that a true arbitrary-precision fixed-mass F(u,v) implementation must replace
or explicitly certify, following the actual frozen dependency chain
407 -> 379 -> 374 -> 370 -> 368.
"""
from __future__ import annotations
import json, re
from pathlib import Path

ITERATION=429
ROOT=Path(__file__).resolve().parent
files={
 '407':ROOT/'iteration407_tru1sq_channel4_analytic_spectral_reduction.py',
 '379':ROOT/'iteration379_tru1sq_double_double_one_channel_pilot.py',
 '374':ROOT/'iteration374_tru1sq_simple_simple_normalized_discontinuity.py',
 '370':ROOT/'iteration370_tru1sq_timelike_numerator_transport.py',
 '368':ROOT/'iteration368_tru1sq_timelike_full_prepruning_routing.py',
 '424':ROOT/'iteration424_channel2_high_precision_fallback_contract.py',
 '427':ROOT/'iteration427_channel2_exact_mass_to_kinematic_chain_reduction.py',
 '428':ROOT/'iteration428_channel2_frozen_mass_node_accuracy_budget.py',
}
s={k:p.read_text() for k,p in files.items()}

chain_checks={
 '407_to_379': "PARENT=ROOT/'iteration379_tru1sq_double_double_one_channel_pilot.py'" in s['407'],
 '379_to_374': "SRC374=ROOT/'iteration374_tru1sq_simple_simple_normalized_discontinuity.py'" in s['379'],
 '374_to_370': "SRC370=ROOT/'iteration370_tru1sq_timelike_numerator_transport.py'" in s['374'],
 '370_to_368': "SRC368=ROOT/'iteration368_tru1sq_timelike_full_prepruning_routing.py'" in s['370'],
 '424_digits': bool(re.search(r'PRECISION_LEVELS_DIGITS\s*=\s*\[80,\s*120\]',s['424'])),
 '424_steps': all(x in s['424'] for x in ('5.0e-6','2.5e-6','1.25e-6')),
 '427_full_H_guardrail': 'FULL_H_INCLUDES_NUMERATOR_AND_AFFINE_MOMENTS' in s['427'],
 '428_precision_provenance_rule': 'precision provenance' in s['428'],
}
if not all(chain_checks.values()):
    raise SystemExit(('dependency_chain_drift',chain_checks))

layers={
 'kinematics_and_basis':{
   'files':['407','374'],
   'binary64_anchors':['math.sqrt','np.asarray','np.array'],
   'required_port':'arbitrary-precision scalar/vector Minkowski kinematics or a quantified lower-precision certificate'
 },
 'phi_mean_and_degree4_interpolation':{
   'files':['407'],
   'binary64_anchors':['np.asarray(train,complex)','np.polynomial.polynomial.polyfit','np.polynomial.polynomial.polyval'],
   'required_port':'mp samples plus arbitrary-precision degree-4 solve/evaluation; do not cast numerator samples through complex128'
 },
 'analytic_affine_moments':{
   'files':['407'],
   'binary64_anchors':['np.log','complex('],
   'required_port':'arbitrary-precision complex log/recurrence for all J_n'
 },
 'radial_stripped_limit':{
   'files':['379','374'],
   'binary64_anchors':['complex(z)','mids','ext_fine'],
   'required_port':'preserve frozen radial nodes/Richardson algebra while keeping samples in arbitrary precision'
 },
 'traced_numerator_transport':{
   'files':['370','368'],
   'binary64_anchors':['np.trace','first_u1','second_primitive','np.asarray'],
   'required_port':'arbitrary-precision matrix/tensor numerator evaluation before stripping denominators'
 },
 'nested_parent_derivatives':{
   'files':['368'],
   'binary64_anchors':['first_u1','Asub','y1','4e-5'],
   'required_port':'retain frozen derivative definitions but distinguish high-precision arithmetic from finite-difference truncation; step stability must be separately certified'
 },
 'mass_derivative_and_cross_precision':{
   'files':['424'],
   'binary64_anchors':[],
   'required_port':'evaluate the same frozen mass nodes independently at 80 and 120 digits and apply the pre-frozen fail-closed comparison; do not shrink h'
 },
}

presence={}
for lname,info in layers.items():
    joined='\n'.join(s[f] for f in info['files'])
    presence[lname]={a:(a in joined) for a in info['binary64_anchors']}
    if not all(presence[lname].values()):
        raise SystemExit(('precision_anchor_drift',lname,presence[lname]))

# Minimal staged implementation order: deepest dependency first.
stages=[
 {'stage':1,'scope':'368/370 traced numerator primitives','exit':'fixed generic probe reproduces current binary64 numerator within 2e-11 scaled while arbitrary precision is internally maintained'},
 {'stage':2,'scope':'379/374 radial stripped-limit wrapper','exit':'frozen radial Richardson outputs stable 80 vs 120 digits and reproduce current validated probes within existing structural tolerance'},
 {'stage':3,'scope':'407 fixed-mass analytic/spectral F','exit':'all numerator samples, polynomial solve, affine moments and final sphere F remain arbitrary precision; direct-integrand checks preserved'},
 {'stage':4,'scope':'424 frozen mass nodes','exit':'80/120-digit fixed-node values and pre-frozen physical/cross-precision checks are evaluated fail-closed'},
 {'stage':5,'scope':'427 factorized oracle','exit':'independent full-H chain-rule result agrees with the physical 424 result within the already frozen physical tolerance; oracle remains non-authority unless separately frozen'},
]

result={
 'iteration':ITERATION,'model_readiness_percent':24,'candidate_residual':False,'scientific_gate_pass':True,
 'classification':'PASS_CHANNEL2_FULL_F_PRECISION_CLOSURE_MANIFEST__NON_PROMOTING',
 'authority_scope':'IMPLEMENTATION_MANIFEST__NO_PHYSICAL_COORDINATE_PROMOTION',
 'target':{'double_double_global_index':2,'class_id':3,'q_squared':-1.0,'iteration421_status':'BLOCKED_CONVERGENCE'},
 'dependency_chain':['407','379','374','370','368'],
 'chain_checks':chain_checks,'precision_layers':layers,'anchor_presence':presence,'implementation_stages':stages,
 'core_requirement':'A true 80/120-digit Iteration-424 result requires arbitrary-precision provenance through the complete fixed-mass F path. Finite-difference truncation is a separate error source and is not cured merely by more digits.',
 'guardrails':['NON_PROMOTING','NO_THRESHOLD_WEAKENING','NO_SMALLER_MASS_STEP','NO_NUMERATOR_CHANGE','NO_ROUTING_CHANGE','NO_SIGN_OR_NORMALIZATION_CHANGE','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
