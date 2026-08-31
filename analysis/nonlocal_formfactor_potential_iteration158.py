#!/usr/bin/env python3
"""Iteration 158: first fixed weakly-nonlocal comparator sub-block.

The goal is deliberately scoped: freeze one entire TT form factor and two local
curvature-cubic potential directions, compute the supported six-probe linear
shape tangent, reuse the already validated Ricci^3/Riemann^3 nonlinear response
columns, and make explicit which genuinely nonlocal cubic response is still
BLOCKED rather than silently set to zero.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])
TAU = 0.8
LWIN = 0.6
SIGMA0 = 1.0

QS = [np.array(x, float) for x in [
    [0.18,0.70,0.20,0.10], [0.14,0.55,-0.25,0.20], [0.22,0.62,0.18,-0.24],
    [0.16,0.48,0.31,0.12], [0.20,0.58,-0.16,-0.28], [0.12,0.44,0.27,-0.19],
]]
RS = [np.array(x, float) for x in [
    [0.11,-0.21,0.52,0.17], [0.09,0.24,0.46,-0.18], [0.10,-0.18,0.41,0.29],
    [0.13,0.22,-0.37,0.33], [0.08,0.26,0.35,0.21], [0.15,-0.20,0.39,0.25],
]]


def k2(k: np.ndarray) -> float:
    return float(k @ ETA @ k)


def window(k: np.ndarray) -> float:
    return math.exp(-0.5*((TAU*k[0])**2 + (LWIN*np.linalg.norm(k[1:]))**2))


def H(z: float) -> float:
    # Frozen entire form factor for this comparator version only.
    return z*z


def tt_transfer(k: np.ndarray, sigma: float) -> float:
    x = k2(k)
    if x <= 0:
        raise RuntimeError("Iteration-158 probe protocol expects spacelike p")
    return window(k) * math.exp(-H(sigma*x)) / x


# The six output momenta are the same p=q+r triplets frozen in Iteration 149.
PS = [q+r for q, r in zip(QS, RS)]
linear_ref = np.array([tt_transfer(p, SIGMA0) for p in PS], dtype=float)
# For H(z)=z^2: d/dlog(sigma) exp[-(sigma k^2)^2]
linear_logsigma = np.array([
    -2.0*(SIGMA0*k2(p))**2 * tt_transfer(p, SIGMA0) for p in PS
], dtype=float)

gain = linear_ref.copy()
proj_gain = gain * float(gain @ linear_logsigma) / float(gain @ gain)
linear_residual = linear_logsigma - proj_gain
linear_residual_fraction = float(np.linalg.norm(linear_residual) / np.linalg.norm(linear_logsigma))
lin_matrix = np.column_stack([gain, linear_logsigma])
lin_sv = np.linalg.svd(lin_matrix, compute_uv=False)

# Curvature-potential directions are loaded from the already Ward-validated
# Iteration-150/152 local C5 response layer. They are part of the same frozen
# nonlocal action as independent potential coefficients, but because they are
# exactly those C5 columns they add no new nonlinear span relative to current C5.
c5_path = Path("results/c5_cubic_response_iteration150.json")
c5 = json.loads(c5_path.read_text(encoding="utf-8"))
ricci3 = np.array([row["Ricci3_response"] for row in c5["rows"]], dtype=float)
riem3 = np.array([row["Riemann3_response"] for row in c5["rows"]], dtype=float)
c5_local = np.column_stack([ricci3, riem3])

# NL potential tangent is exactly the two frozen local columns.
nl_potential = c5_local.copy()
P = c5_local @ np.linalg.pinv(c5_local)
potential_residual = nl_potential - P @ nl_potential
potential_residual_norms = [float(np.linalg.norm(potential_residual[:,j])) for j in range(2)]

out = {
    "iteration": 158,
    "comparator_id": "NL-WNL-001",
    "scope": "tree/spacelike TT linear form-factor shape + explicit local cubic potential sub-block; form-factor-induced cubic vertex not yet derived",
    "action_convention": {
        "schematic_action": "S=-2/kappa^2 int sqrt(-g)[R + R gamma0(box) R + Ric gamma2(box) Ric + V]",
        "tt_form_factor": "D_TT(k)=exp[-H(sigma k^2)]/(k^2+i0 k0), H(z)=z^2",
        "sigma_reference": SIGMA0,
        "potential": "V=lambda_Ricci3 Tr(Ricci^3)+lambda_Riemann3 cyclic(Riemann^3)",
        "parameter_order": ["log_sigma", "lambda_Ricci3", "lambda_Riemann3"],
    },
    "linear_six_probe": {
        "p2": [k2(p) for p in PS],
        "reference_response": linear_ref.tolist(),
        "d_dlog_sigma": linear_logsigma.tolist(),
        "common_gain_rank": int(np.linalg.matrix_rank(gain[:,None])),
        "gain_plus_sigma_rank": int(np.linalg.matrix_rank(lin_matrix)),
        "singular_values_gain_plus_sigma": lin_sv.tolist(),
        "smin_over_smax": float(lin_sv[-1]/lin_sv[0]),
        "sigma_residual_after_common_gain": linear_residual.tolist(),
        "sigma_residual_fraction_after_common_gain": linear_residual_fraction,
    },
    "nonlinear_potential_six_probe": {
        "lambda_Ricci3_column": ricci3.tolist(),
        "lambda_Riemann3_column": riem3.tolist(),
        "rank": int(np.linalg.matrix_rank(nl_potential)),
        "residual_norms_against_existing_C5_R3_span": potential_residual_norms,
        "interpretation": "EXACT_CURRENT_C5_LOCAL_SPAN_IDENTITY",
    },
    "blocked": {
        "form_factor_induced_chi2R": "BLOCKED_NONLOCAL_CUBIC_VERTEX_IMPLEMENTATION",
        "causal_Lorentzian_microstructure": "BLOCKED_FULL_RETARDED_NONLOCAL_COMPLETION",
        "N2_C3sym": "BLOCKED_QUANTUM_STATE_CTP_COMPLETION",
        "full_nonlocal_comparator_quotient": "BLOCKED",
    },
    "retained_results": {
        "NL_NG_001": "FORM_FACTOR_DOES_NOT_FIX_NONLINEAR_RESPONSE: the quadratic form factor leaves independent curvature-potential coefficients invisible at two-point level",
        "NL_NG_002": "LOCAL_CUBIC_POTENTIAL_ALREADY_IN_C5_SPAN: the two frozen potential columns add zero nonlinear residual against the current C5 R^3 block",
        "NG_FUNNEL_015": "FIX_PROPAGATOR_AND_INTERACTION_POTENTIAL_SEPARATELY before treating a nonlocal theory as a finite nonlinear comparator",
    },
    "nonclaims": [
        "The sigma linear-shape residual is a property of this known nonlocal comparator, not Candidate Gravity novelty.",
        "No claim is made that H(z)=z^2 is a unique or phenomenologically preferred form factor.",
        "The full nonlocal cubic response is not set to zero; it remains explicitly BLOCKED.",
    ],
}

print(json.dumps(out, indent=2, sort_keys=True))
