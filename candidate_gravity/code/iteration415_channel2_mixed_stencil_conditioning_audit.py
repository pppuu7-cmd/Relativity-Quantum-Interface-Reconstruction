#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 415.

Prospective numerical-conditioning audit for the sole remaining Tr(U1^2)
double-double blocker (index 2), frozen while Iteration 413 is still active.

This is not a physical computation and does not inspect Iteration-413 output.
It derives the exact L1 amplification of independent fixed-mass node errors for
the unchanged central4 x central4 mixed auxiliary-mass stencil.

For central4 weights (1,-8,8,-1)/(12 h), ||w||_1 = 3/(2 h).
For the tensor-product mixed derivative, ||w⊗w||_1 = 9/(4 h^2).
Thus an absolute node error epsilon_G has worst-case derivative amplification
(9/(4 h^2))*epsilon_G.  We compare the per-node absolute accuracy required to
keep this worst-case contribution below the frozen physical 2e-5 threshold at
the three already-defined mass scales h, h/2 and h/4.
"""
from __future__ import annotations
import json, math, sys

ITERATION=415
PHYS_TOL=2e-5
STEPS=[5e-6,2.5e-6,1.25e-6]
FLOAT64_EPS=sys.float_info.epsilon
rows=[]
for h in STEPS:
    gain=2.25/(h*h)
    required=PHYS_TOL/gain
    rows.append({
      'h':h,
      'mixed_stencil_l1_gain':gain,
      'required_node_absolute_error_for_worst_case_derivative_below_threshold':required,
      'required_node_error_in_float64_eps_units':required/FLOAT64_EPS,
      'unit_scale_float64_epsilon_worst_case_derivative_bound':gain*FLOAT64_EPS,
    })
result={
 'iteration':ITERATION,
 'date':'2026-09-04',
 'model_readiness_percent':24,
 'scientific_gate_pass':True,
 'candidate_residual':False,
 'physical_authority_promoted':False,
 'classification':'PASS_CHANNEL2_CENTRAL4X4_NUMERICAL_CONDITIONING_AUDIT__NON_PROMOTING',
 'target':{'double_double_global_index':2,'class_id':3,'q_squared':-1.0},
 'stencil':{'one_derivative_weights':'(1,-8,8,-1)/(12h)','one_derivative_l1_gain':'1.5/h','mixed_l1_gain':'2.25/h^2'},
 'float64_machine_epsilon':FLOAT64_EPS,
 'frozen_physical_convergence_threshold':PHYS_TOL,
 'scales':rows,
 'interpretation':[
   'The h^-2 amplification is an exact conditioning property of the unchanged mixed finite-difference stencil, not a statement about the actual correlated node error.',
   'At h=2.5e-6 and 1.25e-6, a worst-case guarantee at the 2e-5 derivative threshold would require sub-epsilon absolute accuracy for unit-scale independent node noise.',
   'Therefore a failed Iteration413 halving cannot by itself be interpreted as physical nonconvergence; roundoff/cancellation conditioning must be separated from truncation.',
   'Iteration414 remains the complementary truncation-dominated O(h^4) predictor; Iteration415 supplies the roundoff-conditioning side of the error budget.'
 ],
 'guardrails':['NO_ITERATION413_OUTPUT_USED','NO_PHYSICAL_DS_VALUE','NO_THRESHOLD_WEAKENING','NO_CLAIM_THAT_ACTUAL_NODE_ERRORS_EQUAL_MACHINE_EPSILON','NO_MORE_BLIND_H_SHRINKING_IF_ITERATION413_BLOCKS','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'consume Iteration413 raw result; if it blocks, build a prospectively validated auxiliary-mass derivative extraction with better conditioning (for example symmetric mass-spectral/Taylor coefficient recovery or higher-precision node evaluation) rather than further h shrinking'
}
print(json.dumps(result,indent=2,sort_keys=True))
