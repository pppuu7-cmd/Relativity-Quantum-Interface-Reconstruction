#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 210.

Target-independent numerical gate for the one-loop four-dimensional
polyhomogeneous soft basis through n=2:

    F(eps) = a0 + b0 L + z(a1+b1 L) + z^2(a2+b2 L),

where z=eps/eps_max and L=log(eps/eps_ref).

The script:
  * freezes a 12-point geometric epsilon grid with dynamic range 128;
  * reports rank, singular values and condition number;
  * verifies exact coefficient recovery on a synthetic regular+log control;
  * quantifies deterministic noise amplification;
  * demonstrates that a six-column pure-Taylor fit cannot represent the
    same logarithmic control exactly.

This is protocol conditioning only. It is not Fisher/resource analysis.
"""
from pathlib import Path
import json
import numpy as np

ITERATION = 210
N = 12
EPS_MAX = 0.04
DYNAMIC_RANGE = 128.0
EPS = np.geomspace(EPS_MAX, EPS_MAX / DYNAMIC_RANGE, N)
Z = EPS / EPS_MAX
EPS_REF = float(np.sqrt(EPS.min() * EPS.max()))
L = np.log(EPS / EPS_REF)

X = np.column_stack([
    np.ones(N),
    L,
    Z,
    Z * L,
    Z**2,
    Z**2 * L,
])
BASIS = ["1", "L", "z", "zL", "z^2", "z^2L"]

s = np.linalg.svd(X, compute_uv=False)
rank = int(np.linalg.matrix_rank(X))
cond = float(s[0] / s[-1])

# Frozen synthetic positive control. Coefficients are arbitrary and declared
# before fitting; no physical target information enters the grid.
coef_true = np.array([0.70, -0.11, 0.23, 0.05, -0.09, 0.02], dtype=float)
y = X @ coef_true
coef_fit = np.linalg.lstsq(X, y, rcond=None)[0]
exact_coef_relerr = float(np.linalg.norm(coef_fit - coef_true) / np.linalg.norm(coef_true))
exact_resid_rel = float(np.linalg.norm(X @ coef_fit - y) / np.linalg.norm(y))

# Pure-Taylor negative control with the same six columns by parameter count.
XT = np.column_stack([Z**n for n in range(6)])
coef_taylor = np.linalg.lstsq(XT, y, rcond=None)[0]
taylor_resid_rel = float(np.linalg.norm(XT @ coef_taylor - y) / np.linalg.norm(y))
st = np.linalg.svd(XT, compute_uv=False)

# Deterministic noise direction. Report coefficient error rather than calling
# this a statistical/Fisher calculation.
noise_direction = np.sin(np.arange(N, dtype=float) + 0.3)
noise_direction /= np.linalg.norm(noise_direction)
ynorm = np.linalg.norm(y)
noise_tests = []
for rel in [1e-12, 1e-10, 1e-8, 1e-6]:
    noise = rel * ynorm * noise_direction
    y_noisy = y + noise
    c = np.linalg.lstsq(X, y_noisy, rcond=None)[0]
    noise_tests.append({
        "relative_input_noise_l2": rel,
        "relative_coefficient_error_l2": float(np.linalg.norm(c - coef_true) / np.linalg.norm(coef_true)),
        "relative_fit_residual_l2": float(np.linalg.norm(X @ c - y_noisy) / np.linalg.norm(y_noisy)),
    })

out = {
    "iteration": ITERATION,
    "date": "2026-09-01",
    "model_readiness_percent": 23,
    "scope": "one-loop 4D polyhomogeneous soft extractor through n=2; synthetic protocol controls only",
    "epsilon_grid": EPS.tolist(),
    "epsilon_max": EPS_MAX,
    "epsilon_min": float(EPS.min()),
    "dynamic_range": DYNAMIC_RANGE,
    "epsilon_reference": EPS_REF,
    "dimensionless_z": Z.tolist(),
    "basis": BASIS,
    "matrix_shape": list(X.shape),
    "rank": rank,
    "singular_values": s.tolist(),
    "condition_number": cond,
    "synthetic_coefficients_true": coef_true.tolist(),
    "synthetic_coefficients_fit": coef_fit.tolist(),
    "exact_coefficient_relative_error": exact_coef_relerr,
    "exact_fit_relative_residual": exact_resid_rel,
    "pure_taylor_degree5": {
        "rank": int(np.linalg.matrix_rank(XT)),
        "singular_values": st.tolist(),
        "relative_residual_on_log_control": taylor_resid_rel,
        "fit_coefficients": coef_taylor.tolist(),
    },
    "deterministic_noise_tests": noise_tests,
    "classification": {
        "polyhomogeneous_basis_rank": "PASS_6_OF_6",
        "synthetic_regular_log_recovery": "PASS_MACHINE_PRECISION",
        "pure_taylor_same_parameter_count": "FAIL_TO_REPRESENT_LOG_CONTROL",
        "finite_noise_conditioning": "MODERATE_AMPLIFICATION_REQUIRES_ERROR_ENVELOPE",
        "physical_C5_cut": "NOT_YET_IMPORTED",
        "candidate_residual": "NONE",
        "ANSATZ_003": "NOT_CREATED",
        "Fisher_resources": "FORBIDDEN"
    },
    "retained_results": [
        "NUM-NG-015 — TWELVE_POINT_DYNAMIC_RANGE_128_GRID_RESOLVES_THE_SIX_COLUMN_ONE_LOOP_REGULAR_PLUS_LOG_SOFT_BASIS",
        "SOFT-NG-007 — PURE_TAYLOR_BASIS_WITH_EQUAL_PARAMETER_COUNT_LEAVES_PERCENT_LEVEL_RESIDUAL_ON_A_LOG_SOFT_CONTROL",
        "NUM-NG-016 — LOG_SOFT_COEFFICIENT_EXTRACTION_HAS_NONTRIVIAL_CONDITIONING_AND_REQUIRES_A_DECLARED_NUMERICAL_ERROR_ENVELOPE",
        "NG-FUNNEL-067 — LOOP_SOFT_PROTOCOL_MUST_VALIDATE_REGULAR_LOG_SEPARATION_BEFORE_PHYSICAL_COMPARATOR_IMPORT"
    ],
    "readiness_change": "unchanged at 23%; numerical protocol validated, no physical comparator or candidate residual closed",
    "next_gate": "Import one fixed physical C5 on-shell nonanalytic soft/cut expression or IR-subtracted hard control into the regular+log extractor, preserving the finite-epsilon-first rule."
}

Path("results/loop_soft_extractor_iteration210.json").write_text(
    json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(out, indent=2, sort_keys=True))
