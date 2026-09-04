#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 444.

Source-level, non-promoting audit of the post-parent contraction boundary in
Iteration 368.  This freezes the exact arithmetic graph that must be ported to
80/120-digit arithmetic after the Iteration-443 Y-site gate passes.
"""
from __future__ import annotations
import json
from pathlib import Path

ITERATION = 444
ROOT = Path(__file__).resolve().parent
P368 = ROOT / 'iteration368_tru1sq_timelike_full_prepruning_routing.py'
src = P368.read_text()

required = {
    'first_u1_chain': 'return Q0(p+q)@A1@Q0(p)@Y0',
    'v2_chain': 'return Q0(p+q)@A2@Q0(p)@Y0',
    'nl_chain': 'return Q1(M,dleg,p+qv)@A1@Q0(p)@Y0',
    'nr_chain': 'return Q0(p+qd+qv)@A1@Q1(M,dleg,p)@Y0',
    'y_chain': 'return Q0(p+qd+qv)@A1@Q0(p+qd)@y1(dleg)',
    'orientation_a': 'amp_A=np.trace(F(singleton,p+qp)@S(pair,spec,p))',
    'orientation_b': 'amp_B=np.trace(S(pair,spec,p+qs)@F(singleton,p))',
    'cyclic_shift': 'amp_A_shift=np.trace(F(singleton,p)@S(pair,spec,p+qs))',
}
counts = {k: src.count(v) for k, v in required.items()}
source_pass = all(v == 1 for v in counts.values())

# Each U1 block contains three matrix products.  Each traced two-block amplitude
# adds one more block product before trace: seven matrix products + one trace.
per_amplitude = {'u1_block_matmuls_each': 3, 'block_product_matmuls': 1,
                 'total_matmuls': 7, 'trace_operations': 1}

result = {
    'iteration': ITERATION,
    'model_readiness_percent': 24,
    'candidate_residual': False,
    'scientific_gate_pass': source_pass,
    'classification': ('PASS_ITER444_LAYER368_POSTPARENT_CONTRACTION_BOUNDARY_CONTRACT__NON_PROMOTING'
                       if source_pass else
                       'FAIL_ITER444_LAYER368_POSTPARENT_SOURCE_DRIFT'),
    'authority_scope': 'METHODOLOGICAL_PRECISION_CONTRACT__NO_PHYSICAL_COORDINATE_PROMOTION',
    'source_file': str(P368.name),
    'required_source_pattern_counts': counts,
    'per_traced_amplitude_arithmetic_graph': per_amplitude,
    'frozen_next_contract': {
        'precondition': 'Iteration-443 Y-site y1 gate must PASS first',
        'same_parent_values': True,
        'same_routing_and_orientation': True,
        'precision_digits': [80, 120],
        'cross_precision_scaled_discrepancy_max': 1e-30,
        'finite_outputs_required': True,
        'all_representative_368_370_contractions_required': True,
        'binary64_vs_120': 'diagnostic_only_not_acceptance',
        'forbidden': [
            'threshold_weakening', 'routing_change', 'numerator_change',
            'orientation_quotient_before_routed_translation_check',
            'outer_high_precision_around_binary64_matmul_or_trace'
        ],
    },
    'interpretation': (
        'Iteration-270 parent precision closure and a future Y-site PASS still do not certify '
        'the post-parent arithmetic unless the matrix products and traces themselves are '
        'performed continuously at 80/120 digits (or equivalently certified before use). '
        'The exact contraction graph is now frozen prospectively.'
    ),
    'guardrails': [
        'NO_PHYSICAL_DS_VALUE','NO_ANSATZ003','NO_FISHER_RESOURCES',
        'NO_THRESHOLD_WEAKENING','NO_ZERO_FILL','NO_PARENT_DYNAMICS_CHANGE'
    ],
}
print(json.dumps(result, indent=2, sort_keys=True))
if not source_pass:
    raise SystemExit(2)
