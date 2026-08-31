#!/usr/bin/env python3
"""Iteration 169: conservative O(p^6) C5 absorptive shape envelope.

Scope: the eight timelike conserved-TT linear-response rows frozen in Iterations
166-167.  Iteration 168 proved that the complete leading massless one-loop
curvature-squared C5 absorptive sector is the constant shape and is profiled out.

At the next EFT order, gravitational power counting

    P = 2 + 2 L + sum_v (d_v - 2)

permits O(p^6) contributions from:
  * tree six-derivative local operators (absorptively zero off pole),
  * one loop with one four-derivative insertion,
  * two-loop Einstein-Hilbert graphs.

For a massless one-scale two-point function in 4D, the conservative renormalised
nonanalytic structure through two loops is polynomial in log_R(-s/mu^2) of
degree <= 2.  After the two external EH propagators and taking the frequency-odd
imaginary part, the entire O(p^6) absorptive shape envelope is therefore

    span { s, s log(s/mu^2) }.

Changing mu only mixes the two shapes.  We use x=s/s_max, so the profile basis is
{1, x, x log x}, where 1 is the already-profiled leading O(p^4) massless-loop
shape.  This is a conservative shape envelope, not a claim that all coefficients
are nonzero or independently measurable.
"""
from pathlib import Path
import json
import numpy as np

s = np.array([0.004 * i for i in range(1, 9)], dtype=float)
x = s / s.max()

# leading p^4 constant plus conservative p^6 absorptive envelope
B = np.column_stack([np.ones_like(x), x, x * np.log(x)])
Q, _ = np.linalg.qr(B, mode="complete")
Q_res = Q[:, 3:]
sv = np.linalg.svd(B, compute_uv=False)

# Next-order capacity diagnostic only: p^8-like one-scale absorptive shapes.
T_nnlo = np.column_stack([
    x**2,
    x**2 * np.log(x),
    x**2 * np.log(x)**2,
])
T_proj = Q_res.T @ T_nnlo
sv_nnlo = np.linalg.svd(T_proj, compute_uv=False)

profiled_norms = {
    "constant_p4": float(np.linalg.norm(Q_res.T @ np.ones_like(x))),
    "x_p6": float(np.linalg.norm(Q_res.T @ x)),
    "xlogx_p6": float(np.linalg.norm(Q_res.T @ (x * np.log(x)))),
}

out = {
    "iteration": 169,
    "scope": "eight frozen timelike conserved-TT linear absorptive rows",
    "s_rows": s.tolist(),
    "x_rows": x.tolist(),
    "power_counting_order": "O(p^6) relative EFT numerator/self-energy order",
    "authorized_sources": [
        "tree local six-derivative operators: absorptively zero off isolated poles",
        "one loop with one four-derivative insertion",
        "two-loop Einstein-Hilbert massless sector",
    ],
    "conservative_absorptive_shape_basis": ["1", "x", "x*log(x)"],
    "basis_rank": int(np.linalg.matrix_rank(B, tol=1e-12)),
    "basis_singular_values": sv.tolist(),
    "basis_smin_over_smax": float(sv[-1] / sv[0]),
    "basis_condition_number": float(sv[0] / sv[-1]),
    "residual_shape_dimension": int(Q_res.shape[1]),
    "max_profile_orthogonality_error": float(np.max(np.abs(Q_res.T @ B))),
    "profiled_component_norms": profiled_norms,
    "nnlo_capacity_test_basis": ["x^2", "x^2*log(x)", "x^2*log(x)^2"],
    "nnlo_capacity_projected_rank": int(np.linalg.matrix_rank(T_proj, tol=1e-12)),
    "nnlo_capacity_projected_singular_values": sv_nnlo.tolist(),
    "classification": {
        "leading_p4_massless_one_loop": "PROFILED",
        "nlo_p6_massless_shape_envelope": "PROFILED_CONSERVATIVELY",
        "five_dimensional_shape_remainder": "OPEN_COMPARATOR_SPACE_NOT_CANDIDATE_RESIDUAL",
        "finite_frequency_AS": "BLOCKED_NUMERICAL_SPECTRAL_DATA_OR_CONTROLLED_REPRODUCTION",
        "massive_thresholds": "BLOCKED_SEPARATE_THRESHOLD_COMPARATOR",
        "C3_C4_loop_absorptive": "BLOCKED_NOT_ZERO",
        "ANSATZ_003": "NOT_CREATED",
        "Fisher_resources": "FORBIDDEN",
    },
    "retained_results": [
        "C5-NG-006 — NEXT_ORDER_P6_MASSLESS_TT_ABSORPTIVE_ENVELOPE_IS_SPAN_X_XLOGX",
        "ABS-SHAPE-004 — PROFILING_CONSTANT_X_XLOGX_LEAVES_FIVE_TIMELIKE_SHAPE_DIMENSIONS",
        "NG-FUNNEL-029 — ORDER_BY_ORDER_LOOP_SHAPE_ENVELOPES_MUST_BE_PROFILED_BEFORE_CANDIDATE_RESIDUAL",
    ],
    "model_readiness_percent": 24,
    "readiness_change": "unchanged: NLO C5 shape uncertainty is structured, but finite-frequency AS and threshold/loop comparator completion remain open",
}

Path("results/c5_nlo_absorptive_shape_envelope_iteration169.json").write_text(
    json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(out, indent=2, sort_keys=True))
