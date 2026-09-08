#!/usr/bin/env python3
"""Iteration 616: exact endpoint-amputation / native-normalization audit.

This gate is deliberately result-blind with respect to any projected Candidate value.
It consumes only previously frozen authority and asks how much of the remaining
Iter615 source->native binding is algebraically fixed before any comparator or
Source/Born subtraction.

Closed inputs:
- Iter588: same physical three-mode fixture, with eta_S=-eta_C, so source q2 maps
  exactly to the existing Iter582 bucket by sign flip without merging buckets.
- Iter594: complete unamputated same-action cubic scalar response
    d_abc G = -G Kabc G + sum_6(G Ki G Kjk G) - sum_6(G Ki G Kj G Kk G).
- Iter589: all K1/K2 relative factors/signs are derivatives of one scalar K[g].
- Iter608/613/614/615: normalized scalar-pole distribution, native-s pullback,
  simple-root Jacobians and six nonzero source-side coefficients.

The exact external endpoint amputation is
    S_amp = K0_out (d_abc G) K0_in
which removes only the two common external scalar propagators.  It does NOT
remove internal scalar propagators, K3, K1^3, or any pole support.

This audit must fail closed on the one item not fixed by the historical
cross-sector conventions: the absolute source-response <-> Iter582 native
phase/normalization.  No value from Iter582 is fitted to the source coefficients.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CG = ROOT / "candidate_gravity"

r594 = json.loads((CG / "results/iteration594_full_cubic_routed_assembly.json").read_text())
r615 = json.loads((CG / "results/iteration615_native_s_source_pole_coefficient_audit.json").read_text())

failures = []
if r594.get("classification") != "PASS_FULL_SAME_ACTION_ROUTED_CUBIC_SOURCE_ASSEMBLY_AND_PERMUTATION_SYMMETRY__NON_WARD_NON_RESIDUAL":
    failures.append("Iter594 authority drift")
if r615.get("classification") != "PASS_ITER615_FROZEN_NATIVE_S_INTERNAL_SCALAR_POLE_SOURCE_COEFFICIENT_AUDIT__NON_NORMALIZED_NON_RESIDUAL":
    failures.append("Iter615 authority drift")
if r615.get("root_count") != 6 or r615.get("zero_fill") is not False:
    failures.append("Iter615 pole-support census drift")

# The q2 bucket map itself was already prospectively frozen and raw-checked by
# Iter588 from the same Iter368 vectors under ETA_C=(-+++) and ETA_S=-ETA_C.
q2_bucket_map = {
    "s": {"source_q2_plus_minus_minus_minus": +1.0, "iter582_connection_q2_minus_plus_plus_plus": -1.0},
    "b": {"source_q2_plus_minus_minus_minus": +0.34, "iter582_connection_q2_minus_plus_plus_plus": -0.34},
    "a": {"source_q2_plus_minus_minus_minus": +0.14, "iter582_connection_q2_minus_plus_plus_plus": -0.14},
}
for leg, row in q2_bucket_map.items():
    if abs(row["source_q2_plus_minus_minus_minus"] + row["iter582_connection_q2_minus_plus_plus_plus"]) > 1e-15:
        failures.append(f"{leg}: signature q2 map drift")

# Numerically re-check the exact endpoint-amputation identity on both frozen
# Iter594 probes.  Stored decimal components are rounded, so this check uses a
# very tight envelope only to catch bookkeeping/sign mistakes, not to define new
# physics tolerance.
amputation_rows = []
for pr in r594["probe_results"]:
    k0 = float(pr["K0_external"])
    c = pr["canonical_assembly"]
    direct = (k0 * k0) * float(c["full_dabcG"])
    termwise = (
        -float(c["K3_mixed"])
        + (k0 * k0) * float(c["six_K1K2_sum"])
        - (k0 * k0) * float(c["six_K1cubed_sum_before_minus"])
    )
    err = abs(direct - termwise)
    if not all(math.isfinite(x) for x in (direct, termwise, err)):
        failures.append("nonfinite endpoint-amputation audit")
    if err > 5e-15:
        failures.append(f"endpoint-amputation identity drift {err}")
    amputation_rows.append({
        "p0": pr["p0"],
        "K0_external": k0,
        "K0sq_times_unamputated_full": direct,
        "termwise_amputated_full": termwise,
        "absolute_difference_from_stored_rounding": err,
    })

# Historical source normalization is internally fixed (Iter589), but the source
# side and connection-effective-action side were never given one explicit common
# absolute phase/normalization equation.  Iter218 explicitly stripped the common
# gravitational coupling from V; Iter582 is connection-sector bookkeeping with
# its own +(i/2), -(i/4) effective-action weights.  The remaining map is therefore
# represented by ONE common nonzero scalar N_native, to be fixed independently of
# the six Candidate source values.  It must be common across roots/buckets;
# per-root or per-bucket fitting is forbidden.
normalization_status = "BLOCKED_ONE_COMMON_CROSS_SECTOR_PHASE_NORMALIZATION_SCALAR"

classification = (
    "BLOCKED_ITER616_ENDPOINT_AMPUTATION_AND_Q2_BINDING_CLOSED__ONE_COMMON_NATIVE_NORMALIZATION_SCALAR_UNRESOLVED__NON_RESIDUAL"
    if not failures else
    "FAIL_ITER616_PREREQUISITE_OR_AMPUTATION_IDENTITY_DRIFT"
)

result = {
    "iteration": 616,
    "date": "2026-09-08",
    "model_readiness_percent": 24,
    "classification": classification,
    "scientific_gate_pass": False if not failures else False,
    "failures": failures,
    "candidate_residual": False,
    "closed_subgates": {
        "q2_bucket_correspondence": "CLOSED_BY_ITER588__SAME_MODE_IDENTITY_AND_ETA_SIGN_FLIP",
        "external_endpoint_amputation": "CLOSED_EXACTLY__K0_OUT_d3G_K0_IN",
        "source_internal_relative_normalization": "CLOSED_BY_ITER589_SAME_ACTION_K1_K2_AND_ITER594_13_FAMILY_IDENTITY",
        "scalar_pole_distribution_and_native_s_pullback": "CLOSED_BY_ITER608_613_614_615",
    },
    "q2_bucket_map": q2_bucket_map,
    "endpoint_amputation": {
        "definition": "S_amp^(3)=K0_out*(d_abc G)*K0_in",
        "identity": "S_amp^(3)=-Kabc+sum_6(Ki G Kjk)-sum_6(Ki G Kj G Kk)",
        "preserves_internal_scalar_propagators": True,
        "preserves_K3_local_contact": True,
        "preserves_all_K1cubed_chains": True,
        "zero_fill": False,
        "probe_regression": amputation_rows,
    },
    "remaining_binding_dimension": 1,
    "remaining_binding_parameter": "N_native (one common nonzero source-response <-> Iter582 phase/normalization scalar)",
    "normalization_status": normalization_status,
    "forbidden_rescues": [
        "no fit of N_native to the six Iter615 source coefficients",
        "no separate N per root",
        "no separate N per q2 bucket",
        "no q2 regrouping or summation",
        "no deletion of K1^3 or K3",
        "no Source/Born subtraction yet",
        "no comparator quotient yet",
    ],
    "source_born_subtraction": "NOT_PERFORMED",
    "comparator_quotient": "BLOCKED_UNTIL_N_NATIVE_IS_FIXED_PROSPECTIVELY",
    "ANSATZ_003": "FORBIDDEN",
    "Fisher_resources": "FORBIDDEN",
    "next_gate": "prospectively fix N_native from an independent lower-order/common-field normalization identity (same physical metric perturbation and retarded/effective-action convention), without using any Iter615 projected Candidate value; then rerun the full native Y/T_cut binding with the six roots and all 13 source families retained",
    "readiness_change": "0 percentage points; mapping ambiguity is reduced to one scalar but no robust comparator-subtracted residual exists",
}

print(json.dumps(result, indent=2, sort_keys=True))
if failures:
    raise SystemExit(2)
