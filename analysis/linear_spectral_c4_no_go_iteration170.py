#!/usr/bin/env python3
"""Iteration 170: linear positive-spectral C4 equivalence audit.

The scientific result is analytic.  This script is only a finite numerical
certificate illustrating the direct-integral/mediator representation on the
frozen Iteration-166 timelike rows.

For any non-negative TT Kallen-Lehmann spectral measure rho(mu^2),

    chi_R(s) = int dmu^2 rho(mu^2)/(s-mu^2+i0 sgn omega)

is exactly the retarded response of a direct integral of independent positive-
norm massive spin-2 mediator fields with coupling density sqrt(rho).  The same
construction reproduces the Gaussian Hadamard kernel when the mediator state is
chosen to match the spectral state.  Hence no linear-Gaussian RQIR observable can
distinguish the two descriptions.

The discrete calculation below is illustrative only: it compares the same
positive spectral measure written once as a spectral sum and once as an explicit
mediator tower.  Equality is algebraic, not a numerical approximation theorem.
"""
from pathlib import Path
import json
import numpy as np

s = np.array([0.004 * i for i in range(1, 9)], dtype=float)
mu2 = np.array([0.0025, 0.0065, 0.0110, 0.0180, 0.0270, 0.0410], dtype=float)
weights = np.array([0.12, 0.07, 0.20, 0.14, 0.19, 0.11], dtype=float)
eps = 1.0e-6

assert np.all(weights >= 0.0)

spectral = np.array([
    np.sum(weights / (x - mu2 + 1j * eps)) for x in s
])
mediator = np.array([
    sum(float(w) / (x - float(m2) + 1j * eps) for m2, w in zip(mu2, weights))
    for x in s
])

max_abs_difference = float(np.max(np.abs(spectral - mediator)))

out = {
    "iteration": 170,
    "scope": "frozen eight-row timelike conserved-traceless TT linear source-response sector",
    "theorem": "ANY_POSITIVE_TT_KALLEN_LEHMANN_TWO_POINT_RESPONSE_HAS_AN_EXACT_POSITIVE_NORM_C4_MEDIATOR_DIRECT_INTEGRAL_REPRESENTATION",
    "spectral_nodes_mu2": mu2.tolist(),
    "positive_weights": weights.tolist(),
    "retarded_regulator": eps,
    "max_abs_discrete_tower_difference": max_abs_difference,
    "classification": {
        "positive_linear_spectral_shape": "EXACT_C4_GAUSSIAN_DEGENERACY",
        "threshold_branch_cut_shape": "INCLUDED_WHEN_ENCODED_BY_POSITIVE_SPECTRAL_MEASURE",
        "negative_or_indefinite_spectral_weight": "NOT_PROMOTABLE_WITHOUT_SEPARATE_PHYSICAL_POSITIVITY_GAUGE_OBSERVABILITY_AUDIT",
        "five_dimensional_iteration169_remainder": "NOT_A_GRAVITY_SPECIFIC_RESIDUAL_AT_LINEAR_GAUSSIAN_LEVEL",
        "ANSATZ_003": "NOT_CREATED",
        "Fisher_resources": "FORBIDDEN_NO_GRAVITY_SPECIFIC_RESIDUAL",
    },
    "retained_results": [
        "C4-NG-008 — POSITIVE_LINEAR_TT_SPECTRAL_RESPONSE_IS_EXACTLY_REPRESENTABLE_BY_ORDINARY_MEDIATOR_CONTINUUM",
        "ABS-SHAPE-005 — FINITE_FREQUENCY_LINEAR_SPECTRAL_SHAPE_CANNOT_CERTIFY_GRAVITY_SPECIFIC_NOVELTY_AGAINST_C4",
        "NG-FUNNEL-030 — LINEAR_SPECTRAL_RESIDUAL_REQUIRES_A_LINKED_NONLINEAR_OR_POST_GAUSSIAN_GRAVITY_RELATION_FOR_PROMOTION",
    ],
    "model_readiness_percent": 24,
    "readiness_change": "unchanged: a whole false-positive search branch is closed, but no robust Candidate Gravity residual or parent dynamics exists",
}

Path("results/linear_spectral_c4_no_go_iteration170.json").write_text(
    json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(out, indent=2, sort_keys=True))
