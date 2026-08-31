#!/usr/bin/env python3
"""Iteration 172: finite relation-level CTP comparator matrix.

Rows: six frozen kinematic points, four coordinates per point:
  (Gamma_arr, Gamma_aar, Gamma_aaa, WardLock).

Generic closed-unitary C4/C5 cubic dynamics is represented conservatively by
one independent amplitude direction per row, with
  Gamma_aar=0, Gamma_aaa=Gamma_arr/4, WardLock=0.
This deliberately does not restrict the ordinary quantum comparator to the EH
kinematic fingerprint.

The fixed PQCG tree realization contributes the already-authoritative EH
Gamma_arr fingerprint but no quantum aaa vertex at this supported tree order.
Full diffusion/MSR ordered vertices remain BLOCKED and are not zero-filled.
"""
from pathlib import Path
import json
import numpy as np

B_EH = np.array([
    0.30003001285313774,
    -1.461790494216445,
    -12.034873790942026,
    -14.434681522564402,
    4.867521776975717,
    -2.7789127642722273,
], dtype=float)

nrow = len(B_EH)
ncoord = 4*nrow
cols = []
labels = []

# Strong generic closed-unitary C4/C5 comparator: arbitrary row-local cubic
# amplitude while preserving the exact r/a relation and source/Ward lock.
for i in range(nrow):
    v = np.zeros(ncoord)
    v[4*i + 0] = 1.0
    v[4*i + 2] = 0.25
    cols.append(v)
    labels.append(f"unitary_row_{i+1}")

# Supported fixed C3/PQCG tree piece: classical nonlinear Einstein drift.
v_c3 = np.zeros(ncoord)
for i, b in enumerate(B_EH):
    v_c3[4*i + 0] = b
cols.append(v_c3)
labels.append("C3_PQCG_tree_EH_arr_only")

M = np.column_stack(cols)
s = np.linalg.svd(M, compute_uv=False)
rank = int(np.linalg.matrix_rank(M))

# Relation map per row: (Gamma_aar, Gamma_aaa-Gamma_arr/4, WardLock).
Q = []
relation_labels = []
for i in range(nrow):
    q = np.zeros(ncoord); q[4*i+1] = 1.0
    Q.append(q); relation_labels.append(f"row{i+1}_aar")
    q = np.zeros(ncoord); q[4*i+2] = 1.0; q[4*i+0] = -0.25
    Q.append(q); relation_labels.append(f"row{i+1}_aaa_minus_arr_over4")
    q = np.zeros(ncoord); q[4*i+3] = 1.0
    Q.append(q); relation_labels.append(f"row{i+1}_WardLock")
Q = np.vstack(Q)
R = Q @ M
sr = np.linalg.svd(R, compute_uv=False)
rank_r = int(np.linalg.matrix_rank(R))

out = {
  "iteration": 172,
  "scope": "six frozen amputated CTP kinematic rows; fixed source convention from Iterations 148-149 and r/a normalization from Iteration 171",
  "raw_coordinate_order_per_row": ["Gamma_arr","Gamma_aar","Gamma_aaa","WardLock"],
  "comparator_columns": labels,
  "raw_matrix_shape": list(M.shape),
  "raw_rank": rank,
  "raw_singular_values": [float(x) for x in s],
  "raw_smin_over_smax": float(s[-1]/s[0]),
  "relation_coordinates_per_row": ["Gamma_aar","Gamma_aaa-Gamma_arr/4","WardLock"],
  "relation_matrix_shape": list(R.shape),
  "relation_rank": rank_r,
  "relation_singular_values": [float(x) for x in sr],
  "C3_supported_relation_norm": float(np.linalg.norm(R[:,-1])),
  "classification": {
    "generic_closed_unitary_C4_C5": "EXACT_RELATION_SUBSPACE; six arbitrary row amplitudes removed without assuming EH shape",
    "fixed_C3_tree": "ONE_SUPPORTED_EH_SHAPED_NONUNITARY_RELATION_DIRECTION",
    "C3_diffusion_MSR_ordered_vertices": "BLOCKED_NOT_ZERO",
    "WardLock_nonzero": "CONSISTENCY_FAIL_NOT_NOVELTY",
    "remaining_relation_space": "NOT_NOVELTY_CERTIFICATE_WHILE_C3_NONLINEAR_ORDERED_AND_NONLOCAL_AS_CTP_COMPLETIONS_ARE_BLOCKED",
    "ANSATZ_003": "NOT_CREATED",
    "Fisher_resources": "FORBIDDEN"
  },
  "retained_results": [
    "CTP-NG-003 — GENERIC_CLOSED_UNITARY_C4_C5_REMOVES_ROW_LOCAL_CUBIC_AMPLITUDE_BUT_NOT_RELATION_VIOLATIONS",
    "CTP-NG-004 — FIXED_PQCG_TREE_ADDS_ONE_EH_SHAPED_CLASSICAL_RELATION_DIRECTION",
    "NG-FUNNEL-032 — WARD_LOCK_VIOLATION_IS_CONSISTENCY_FAIL_NOT_NOVELTY"
  ],
  "model_readiness_percent": 24,
  "readiness_change": "unchanged: first finite relation-level rank certificate obtained, but unsupported C3/nonlocal/AS ordered CTP pieces prevent a robust residual certificate"
}

Path("results/ctp_relation_comparator_iteration172.json").write_text(json.dumps(out, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps(out, indent=2, sort_keys=True))
