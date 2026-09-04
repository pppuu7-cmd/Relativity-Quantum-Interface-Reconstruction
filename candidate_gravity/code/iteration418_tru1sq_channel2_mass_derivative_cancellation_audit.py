#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 418.

Dedicated auxiliary-mass derivative cancellation/roundoff audit for the sole
remaining Tr(U1^2) double-double blocker, global index 2 / class 3 / q^2=-1.

Iteration 413 falsified the previously assumed O(h^4) truncation regime: after
halving h from 2.5e-6 to 1.25e-6 the mixed-derivative discrepancy increased.
This diagnostic therefore does NOT refine h again, does NOT change the angular
representation, observable, normalization, or any physical threshold, and does
NOT promote a physical coordinate.  It reuses the exact Iteration-407 analytic
sphere function specialized to index 2 and measures the numerical condition of
the already-used central4 x central4 mass derivative at the three h values that
have already been evaluated (5e-6, 2.5e-6, 1.25e-6).

The audit decomposes the mixed derivative into its 16 weighted contributions,
computes cancellation condition numbers, compares naive and compensated sums,
and estimates binary64 roundoff amplification.  Any unsupported interpretation
remains BLOCKED.
"""
from __future__ import annotations
import contextlib, io, json, math
from pathlib import Path
import numpy as np

ITERATION = 418
TARGET_INDEX = 2
EXPECTED_CLASS = 3
EXPECTED_Q2 = -1.0
H_VALUES = (5.0e-6, 2.5e-6, 1.25e-6)
PHYSICAL_TOL = 2.0e-5

root = Path(__file__).resolve().parent
parent = root / "iteration407_tru1sq_channel4_analytic_spectral_reduction.py"
src = parent.read_text()

# Fail closed on the frozen parent identity before specializing only the target.
for old, new in [
    ("ITERATION=407", "ITERATION=418"),
    ("TARGET_INDEX=4", "TARGET_INDEX=2"),
    (
        "if int(ch['class_id'])!=5 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))",
        "if int(ch['class_id'])!=3 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))",
    ),
]:
    if src.count(old) != 1:
        raise RuntimeError(("iteration407_specialization_drift", old, src.count(old)))
    src = src.replace(old, new, 1)

marker = "start=time.perf_counter()"
if src.count(marker) != 1:
    raise RuntimeError(("iteration407_start_marker_drift", src.count(marker)))
prefix = src.split(marker, 1)[0]
ns = {"__name__": "iteration418_parent407_prefix", "__file__": str(parent)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix, str(parent), "exec"), ns, ns)

analytic_sphere_G = ns["analytic_sphere_G"]
ch = ns["ch"]
q2 = float(ns["q2"])
if int(ch["class_id"]) != EXPECTED_CLASS or abs(q2 - EXPECTED_Q2) > 1e-12:
    raise RuntimeError(("target_identity_drift_after_exec", ch["class_id"], q2))
if abs(float(ns["ANGULAR_CONVERGENCE_TOL"]) - PHYSICAL_TOL) > 1e-18:
    raise RuntimeError(("physical_threshold_drift", ns["ANGULAR_CONVERGENCE_TOL"]))

# 4-point centered first derivative at nodes [-2h,-h,+h,+2h].
# Mixed derivative weights are their outer product.
base_coeff = np.array([1.0, -8.0, 8.0, -1.0], dtype=float) / 12.0
node_mult = np.array([-2.0, -1.0, 1.0, 2.0], dtype=float)
weight_outer = np.outer(base_coeff, base_coeff)

def compensated_complex_sum(values):
    vals = [complex(x) for x in values]
    return complex(math.fsum(x.real for x in vals), math.fsum(x.imag for x in vals))

def audit_h(h):
    vals = np.empty((4, 4), dtype=complex)
    structure = []
    for i, mi in enumerate(node_mult):
        for j, mj in enumerate(node_mult):
            vals[i, j], diag = analytic_sphere_G(float(mi*h), float(mj*h))
            structure.append(diag)

    contributions = (weight_outer * vals) / (h*h)
    naive = complex(np.sum(contributions))
    compensated = compensated_complex_sum(contributions.ravel())
    abs_sum = float(sum(abs(complex(x)) for x in contributions.ravel()))
    scale = max(abs(compensated), np.finfo(float).tiny)
    cancellation_condition = float(abs_sum / scale)
    compensated_delta = float(abs(naive-compensated) / max(1.0, abs(naive), abs(compensated)))
    eps = float(np.finfo(float).eps)
    roundoff_bound_absolute = float(eps * abs_sum)
    roundoff_bound_scaled = float(roundoff_bound_absolute / max(1.0, abs(compensated)))
    return {
        "h": h,
        "mixed_derivative_naive": [float(naive.real), float(naive.imag)],
        "mixed_derivative_compensated": [float(compensated.real), float(compensated.imag)],
        "D_s_compensated": [float(-compensated.real), float(-compensated.imag)],
        "sum_abs_weighted_contributions": abs_sum,
        "cancellation_condition_number": cancellation_condition,
        "naive_vs_compensated_scaled_delta": compensated_delta,
        "binary64_epsilon_times_abs_sum": roundoff_bound_absolute,
        "binary64_roundoff_bound_scaled": roundoff_bound_scaled,
        "max_polynomial_heldout_scaled_error": float(max(d["poly_heldout_scaled_error"] for d in structure)),
        "max_denominator_affine_scaled_error": float(max(d["den_affine_scaled_error"] for d in structure)),
        "max_radial_richardson_scaled_error": float(max(d["max_radial_richardson_scaled_error"] for d in structure)),
        "minimum_analytic_uncut_abs_denominator": float(min(d["minimum_analytic_uncut_abs_denominator"] for d in structure)),
        "minimum_kallen": float(min(d["minimum_kallen"] for d in structure)),
    }

records = [audit_h(h) for h in H_VALUES]
derivs = [complex(*()) if False else complex(r["mixed_derivative_compensated"][0], r["mixed_derivative_compensated"][1]) for r in records]
pair_discrepancies = [float(abs(derivs[i]-derivs[i+1]) / max(1.0, abs(derivs[i]), abs(derivs[i+1]))) for i in range(len(derivs)-1)]
ratio = float(pair_discrepancies[1] / pair_discrepancies[0]) if pair_discrepancies[0] else float("inf")
observed_order = float(math.log(pair_discrepancies[0]/pair_discrepancies[1], 2.0)) if all(x > 0 for x in pair_discrepancies) else None
max_condition = float(max(r["cancellation_condition_number"] for r in records))
max_comp_delta = float(max(r["naive_vs_compensated_scaled_delta"] for r in records))
max_roundoff_scaled = float(max(r["binary64_roundoff_bound_scaled"] for r in records))
structure_ok = bool(
    all(r["max_polynomial_heldout_scaled_error"] <= 2e-6 for r in records)
    and all(r["max_denominator_affine_scaled_error"] <= 2e-11 for r in records)
    and all(r["max_radial_richardson_scaled_error"] <= ns["RADIAL_EXTRAP_TOL"] for r in records)
    and all(r["minimum_analytic_uncut_abs_denominator"] > ns["UNCUT_MIN_TOL"] for r in records)
    and all(r["minimum_kallen"] > 0.0 for r in records)
)

result = {
    "iteration": ITERATION,
    "model_readiness_percent": 24,
    "candidate_residual": False,
    "scientific_gate_pass": structure_ok,
    "classification": "PASS_TRU1SQ_CHANNEL2_MASS_DERIVATIVE_CANCELLATION_AUDIT__DIAGNOSTIC_ONLY" if structure_ok else "FAIL_TRU1SQ_CHANNEL2_MASS_DERIVATIVE_CANCELLATION_AUDIT_EXECUTION",
    "authority_scope": "DIAGNOSTIC_ONLY__NO_PHYSICAL_COORDINATE_PROMOTION",
    "channel": {"double_double_global_index": TARGET_INDEX, "class_id": int(ch["class_id"]), "q_squared": q2, "physical_status": "BLOCKED_CONVERGENCE"},
    "frozen_h_values_reaudited": list(H_VALUES),
    "records": records,
    "pair_discrepancies": pair_discrepancies,
    "discrepancy_ratio_fine_over_coarse": ratio,
    "observed_order_from_existing_h_pairs": observed_order,
    "expected_O_h4_ratio": 0.0625,
    "max_cancellation_condition_number": max_condition,
    "max_naive_vs_compensated_scaled_delta": max_comp_delta,
    "max_binary64_roundoff_bound_scaled": max_roundoff_scaled,
    "physical_threshold_unchanged": PHYSICAL_TOL,
    "guardrails": [
        "NO_NEW_H_REFINEMENT", "NO_ANGULAR_GRID_ESCALATION", "NO_THRESHOLD_WEAKENING",
        "NO_ZERO_FILL", "NO_PHYSICAL_AUTHORITY_FROM_DIAGNOSTIC", "NO_SOURCE_BORN_SUBTRACTION",
        "NO_ANSATZ003", "NO_FISHER_RESOURCES"
    ],
    "next_gate": "construct an algebraically equivalent analytic/high-precision auxiliary-mass mixed-derivative representation for index 2, prospectively freeze its precision/stability checks, and require the existing original-integrand structural cross-check before any physical promotion",
}
print(json.dumps(result, indent=2, sort_keys=True))
if not structure_ok:
    raise SystemExit(2)
