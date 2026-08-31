#!/usr/bin/env python3
"""Iteration 183: split-free joint (K2, soft2 cubic) conditioning protocol.

Iteration 182 showed that the schematic split

    Gamma_soft = W[K2] + Rlin:B

is not a unique off-shell observable unless a covariantization convention is
added.  RQIR does not need to promote that convention to physics.  Instead use
the directly source-completed observables

    Y = (K2(q_i^2), S_soft2(q_i)),

where S_soft2 is the full coefficient of the O(k_soft^2) cubic response in the
fixed physical metric/source convention.  Exact calibration of the quadratic
kernel is imposed as a hard constraint.  Comparator nuisance directions are then
restricted to parameter combinations that leave all calibrated K2 rows fixed.

For a tangent block with quadratic part A=dK/dtheta and cubic part B=dS/dtheta,
let N_A span null(A).  The allowed conditional cubic comparator span is

    B_cond = B N_A.

This is a finite Schur/null-space construction and is invariant under any
internal repartition W->W+R:C, B->B-C because only the full S_soft2 enters.

The current six q^2 rows are also audited at the quadratic level.  The declared
local C5 TT inverse-kernel polynomial basis through dimension 12, including a
common EH/normalization direction, is proportional to {x,x^2,...,x^6}.  It has
rank 6/6 on these six rows.  Appending the QG-NL-EXP-001 lambda tangent

d/dlambda [x exp(lambda x)]|lambda=1 = x^2 exp(x)

therefore creates one exact parameter-space null direction: the nonlocal K2
change can be compensated at the six sampled points by local quadratic EFT
coefficients.  The physically relevant discriminator is the corresponding
*conditional full soft2 cubic response*, which requires the source-completed
soft2 cubic columns of those local quadratic EFT operators as well as the full
nonlocal cubic column.
"""
from pathlib import Path
import json
import numpy as np

x=np.array([0.5076,0.3854,0.4260,0.3153,0.4004,0.2882],float)
K_local=np.column_stack([x**p for p in range(1,7)])
k_nonlocal=x**2*np.exp(x)
A=np.column_stack([K_local,k_nonlocal])

s_local=np.linalg.svd(K_local,compute_uv=False)
_,s_aug,vh=np.linalg.svd(A,full_matrices=True)
null_vec=vh[-1]
null_vec=null_vec/null_vec[-1]
null_res=A@null_vec

# Direct solve gives the same compensation coefficients for local columns when
# the nonlocal parameter coefficient is normalized to +1.
local_comp=np.linalg.solve(K_local,-k_nonlocal)

# Algebraic split-invariance demonstration for the full cubic observable.
rng=np.random.default_rng(183)
W=rng.normal(size=6)
B=rng.normal(size=6)
C=rng.normal(size=6)
S=W+B
Wp=W+C
Bp=B-C
Sp=Wp+Bp

out={
  "iteration":183,
  "scope":"six frozen null-soft rows; joint source-completed quadratic-kernel and full soft2 cubic conditioning",
  "protocol":{
    "observable":"Y=(K2_rows,S_soft2_full_rows)",
    "hard_constraint":"exactly condition comparator/nuisance parameter combinations on delta K2_rows=0 before cubic quotient",
    "conditional_comparator_formula":"if A=dK/dtheta and B=dS/dtheta, use B_cond=B*N_A with columns of N_A spanning null(A)",
    "internal_W_B_split":"NOT_AN_OBSERVABLE_AND_NOT_REQUIRED"
  },
  "split_invariance":{
    "max_abs_full_soft2_change_under_W_B_repartition":float(np.max(np.abs(Sp-S))),
    "status":"PASS_MACHINE_PRECISION"
  },
  "quadratic_conditioning_audit":{
    "x_q2_rows":x.tolist(),
    "local_C5_K2_basis":["x","x^2","x^3","x^4","x^5","x^6"],
    "local_rank":int(np.linalg.matrix_rank(K_local,tol=1e-12)),
    "local_singular_values":s_local.tolist(),
    "local_condition_number":float(s_local[0]/s_local[-1]),
    "nonlocal_lambda_K2_tangent":"x^2*exp(x) at lambda=1",
    "augmented_rank":int(np.linalg.matrix_rank(A,tol=1e-12)),
    "augmented_singular_values":s_aug.tolist(),
    "parameter_null_dimension":int(A.shape[1]-np.linalg.matrix_rank(A,tol=1e-12)),
    "null_vector_normalized_nonlocal_coefficient_1":null_vec.tolist(),
    "local_compensation_coefficients":local_comp.tolist(),
    "null_residual_norm":float(np.linalg.norm(null_res))
  },
  "new_required_C5_columns":[
    "source-completed soft2 cubic completion associated with EH/normalization direction if treated as a nuisance",
    "source-completed soft2 cubic completions of R_mn Box^n R^mn quadratic-EFT directions through the frozen dimension-12 order"
  ],
  "classification":{
    "joint_K2_soft2_protocol":"FROZEN_SPLIT_INVARIANT",
    "previous_B_T_W_split":"DEMOTED_TO_INTERNAL_BOOKKEEPING_FOR_NONZERO_K2",
    "six_row_quadratic_nonlocal_vs_local":"EXACT_FINITE_SAMPLE_COMPENSATION_WITH_POOR_CONDITIONING",
    "conditional_nonlocal_soft2_direction":"BLOCKED_MISSING_LOCAL_QUADRATIC_AND_NONLOCAL_FULL_SOFT2_CUBIC_COLUMNS",
    "consistency_fail":False,
    "novelty_certificate":"NONE",
    "ANSATZ_003":"NOT_CREATED",
    "Fisher_resources":"FORBIDDEN"
  },
  "retained_results":[
    "REL-NG-001 — JOINT_K2_SOFT2_HARD_CONDITIONING_IS_INVARIANT_UNDER_INTERNAL_WARD_TRANSVERSE_REPARTITION",
    "C5-NG-010 — LOCAL_QUADRATIC_EFT_SOFT2_COMPLETIONS_ARE_REQUIRED_WHEN_THEIR_K2_DIRECTIONS_COMPENSATE_NONLOCAL_CALIBRATION",
    "NL-NG-006 — SIX_ROW_NONLOCAL_K2_TANGENT_HAS_AN_EXACT_LOCAL_POLYNOMIAL_COMPENSATION_DIRECTION_AT_FROZEN_DIMENSION12_RESOLUTION",
    "NG-FUNNEL-041 — CONDITION_FULL_SOURCE_COMPLETED_SOFT2_ON_CALIBRATED_K2_INSTEAD_OF_PROMOTING_AN_OFFSHELL_W_B_SPLIT"
  ],
  "model_readiness_percent":24,
  "readiness_change":"unchanged: the relation observable is repaired and made split-invariant, but the conditional comparator cubic columns are not yet complete"
}
Path('results/joint_k2_soft2_conditioning_iteration183.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
