#!/usr/bin/env python3
"""Iteration656 fail-closed audit for the Iter655 null-soft Ward-image gate.

This script does not evaluate Candidate cut values. It checks only algebraic/provenance
compatibility between the prospective Iter655 soft trajectory and the explicit Iter653
q^2!=0 longitudinal/transverse Ward reconstruction.
"""
from __future__ import annotations

import json
from pathlib import Path


def minkowski_sq(v):
    return v[0] ** 2 - v[1] ** 2 - v[2] ** 2 - v[3] ** 2


n = (1.0, 0.0, 0.0, 1.0)
e1 = (0.0, 1.0, 0.0, 0.0)
e2 = (0.0, 0.0, 1.0, 0.0)

# Iter655: q3(eps) = -eps*n with eps>0.
probe_eps = (1.0, 0.5, 0.125)
q3_sq = {str(eps): minkowski_sq(tuple(-eps * x for x in n)) for eps in probe_eps}

failures = []
if abs(minkowski_sq(n)) > 1e-15:
    failures.append("ITER655_SOFT_DIRECTION_NOT_NULL")
if any(abs(v) > 1e-15 for v in q3_sq.values()):
    failures.append("ITER655_SOFT_LEG_NOT_EXACTLY_NULL")

# Iter653 authority explicitly assumes q^2 != 0 and defines xi with q^-2 and q^-4.
iter653_requires_nonzero_q2 = True
iter653_contains_inverse_q2 = True
iter653_contains_inverse_q4 = True
iter653_projector_applicable_on_iter655_soft_leg = False

# Historical Iter175/205 authority fixes the null soft direction / TT plus polarization
# and D_s/soft-limit ordering, but does not supply a unique closed-SK hard trajectory
# plus an explicit null-safe tensor formula for W[D_s K2]. Do not zero-fill.
historical_iter175_205_unique_full_closed_sk_trajectory = False
historical_iter175_205_explicit_null_safe_closed_sk_ward_image = False
zero_fill_allowed = False
ward_image_value_assigned = None

classification = (
    "BLOCKED_ITER656_NULL_SOFT_WARD_IMAGE_NOT_DEFINED_BY_ITER653_Q2_NONZERO_PROJECTOR"
    "__ITER655_PROSPECTIVE_TRAJECTORY_NOT_UNIQUE_HISTORICAL_RECOVERY__NON_RESIDUAL"
)

result = {
    "iteration": 656,
    "contract_scope": "MSSC001-CLOSED-SK-SOFT-TCUT-KIN-V1 / null-soft Ward-image audit",
    "authoritative_inputs": {
        "iter175": "historical null k=(1,0,0,1) plus-TT polarization / abstract soft Ward split",
        "iter205": "D_s=Disc_s/(2*pi*i), linked-cut then soft-limit protocol",
        "iter653": "closed-SK Gamma2/Gamma3 Ward map with q^2!=0 longitudinal projector",
        "iter655": "prospective q3(eps)=-eps*n soft trajectory; canonical Action 34327833414 success",
    },
    "iter655_soft_direction": list(n),
    "n_squared": minkowski_sq(n),
    "sample_q3_squared": q3_sq,
    "iter653_projector": {
        "requires_q_squared_nonzero": iter653_requires_nonzero_q2,
        "contains_q_inverse_squared": iter653_contains_inverse_q2,
        "contains_q_inverse_fourth": iter653_contains_inverse_q4,
        "applicable_on_iter655_exact_null_soft_leg": iter653_projector_applicable_on_iter655_soft_leg,
    },
    "historical_scope": {
        "iter175_205_unique_full_closed_sk_trajectory": historical_iter175_205_unique_full_closed_sk_trajectory,
        "iter175_205_explicit_null_safe_closed_sk_ward_image": historical_iter175_205_explicit_null_safe_closed_sk_ward_image,
        "iter655_is_prospective_completion": True,
    },
    "guardrails": {
        "zero_fill_allowed": zero_fill_allowed,
        "ward_image_value_assigned": ward_image_value_assigned,
        "candidate_cut_values_read_for_this_gate": False,
        "ansatz003_allowed": False,
        "fisher_or_resources_allowed": False,
    },
    "classification": classification,
    "failures": failures,
    "MODEL_READINESS": "24%",
    "readiness_delta_percentage_points": 0,
    "exact_next_gate": (
        "Derive a null-compatible Ward reconstruction directly from the Iter653 action Ward identity, "
        "without using the q^-2/q^-4 projector; prove auxiliary-vector/regulator independence on the "
        "frozen Iter655 soft trajectory, or classify residual path/gauge-completion freedom as BLOCKED."
    ),
}

out = Path("candidate_gravity/results/iteration656_null_soft_ward_image_audit.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2, sort_keys=True))
if failures:
    raise SystemExit(1)
