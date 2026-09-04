#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 410.

Resource-recovery wrapper for the Iteration-408 STRUCTURE-ONLY oracle.
The cancelled two-target run is split prospectively into one target per job.
Physics, structural tests and all frozen thresholds are imported verbatim from
Iteration 408; this wrapper changes only scheduling/resource granularity.
"""
from __future__ import annotations
import contextlib, io, json, os
from pathlib import Path

ITERATION = 410
TARGET = int(os.environ.get('TARGET_INDEX', '-1'))
if TARGET not in (2, 11):
    raise RuntimeError(('unsupported_target', TARGET))

ROOT = Path(__file__).resolve().parent
PARENT = ROOT / 'iteration408_tru1sq_blockers2_11_analytic_structure_oracle.py'
src = PARENT.read_text()
marker = 'results=[evaluate_target(i) for i in TARGETS]'
if src.count(marker) != 1:
    raise RuntimeError('iteration408_result_marker_drift')
ns = {'__name__': 'iteration410_parent408_prefix', '__file__': str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split(marker, 1)[0], str(PARENT), 'exec'), ns, ns)

row = ns['evaluate_target'](TARGET)
status = row['structure_status']
if status not in ('PASS', 'BLOCKED'):
    raise RuntimeError(('unexpected_structure_status', status))

result = {
    'iteration': ITERATION,
    'model_readiness_percent': 24,
    'scientific_gate_pass': True,
    'candidate_residual': False,
    'classification': f'{status}_TRU1SQ_BLOCKER{TARGET}_ANALYTIC_AZIMUTH_STRUCTURE_SPLIT_RECOVERY',
    'target': row,
    'oracle_thresholds': {
        'denominator_affine_scaled_max': ns['DEN_AFFINE_REL_TOL'],
        'phase_mean_scaled_max': ns['PHASE_MEAN_REL_TOL'],
        'fourier_tail_above_abs_mode_8_scaled_max': ns['FOURIER_TAIL_REL_TOL'],
        'azimuth_mean_polynomial_heldout_scaled_max': ns['POLY_HELDOUT_REL_TOL'],
        'candidate_polynomial_degrees': list(ns['DEGREES']),
    },
    'scope': f'STRUCTURE_ONLY__INDEX_{TARGET}__ITER408_SPLIT_RESOURCE_RECOVERY__NO_NEW_D_S_VALUE',
    'physics_immutability': {
        'parent': 'Iteration408 exact structural oracle / Iteration379-389 physical integrand',
        'frozen_physical_convergence_threshold': 2e-5,
        'mass_derivative_stencil': 'unchanged central4 x central4',
        'normalization': 'unchanged D_s_double_double=-sphere_mean[d_u d_v G]',
    },
    'guardrails': [
        'ITER408_ARITHMETIC_IMPORTED_VERBATIM',
        'ONLY_RESOURCE_GRANULARITY_CHANGED',
        'NO_PHYSICAL_VALUE_PROMOTION',
        'NO_THRESHOLD_WEAKENING',
        'NO_ANGULAR_GRID_LADDER',
        'NO_SOURCE_BORN_SUBTRACTION',
        'NO_ANSATZ003',
        'NO_FISHER_RESOURCES',
    ],
    'next_gate': (
        'Raw-audit both split target artifacts fail-closed. A PASS authorizes the already-frozen '
        'Iteration407 physical analytic/spectral reduction for that same index with its own held-out '
        'original-integrand checks and unchanged 2e-5 physical convergence threshold; BLOCKED remains '
        'a structural blocker and must not be zero-filled.'
    ),
}
print(json.dumps(result, indent=2, sort_keys=True))
