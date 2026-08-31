#!/usr/bin/env python3
"""Iteration 176: compatibility gate for reusing finite C5 cubic columns in soft B_T space.

Iteration 150 evaluated C5 cubic responses on six finite off-shell momentum
triplets.  Iteration 175 defines a different observable: the Ward-subtracted
O(epsilon^2) coefficient when one external graviton momentum is softened as
k_soft = epsilon k0.

A finite value at epsilon=1, even together with the universal soft0 and soft1
coefficients, cannot determine soft2.  The analytic family

  f_c(eps) = f0(eps) + c eps^2 (1-eps)^2

has identical f(0), f'(0), and f(1) for every c, but a different eps^2 Taylor
coefficient.  Therefore old finite-probe response columns cannot be relabeled as
B_T columns; a new action-level soft deformation is required.
"""
from pathlib import Path
import json

# baseline f0 = a0 + a1 e + a2 e^2
A0, A1, A2 = 1.25, -0.7, 2.4
cs = [-5.0, -1.0, 0.0, 2.0, 7.5]
rows=[]
for c in cs:
    # delta = c*(e^2 - 2e^3 + e^4)
    value_e0=A0
    derivative_e0=A1
    soft2_coeff=A2+c
    value_e1=A0+A1+A2  # deformation exactly vanishes at e=1
    rows.append({
        "c":c,
        "f_at_0":value_e0,
        "fprime_at_0":derivative_e0,
        "soft2_coefficient":soft2_coeff,
        "f_at_1":value_e1,
    })

out={
  "iteration":176,
  "question":"Can Iteration-150 finite off-shell C5 cubic columns be reused as Iteration-175 soft-transverse B_T columns?",
  "answer":"NO",
  "analytic_counterfamily":"f_c(epsilon)=f0(epsilon)+c*epsilon^2*(1-epsilon)^2",
  "invariants_shared_by_all_c":["f(0)","f'(0)","f(1)"],
  "quantity_not_determined":"epsilon^2 soft coefficient / Ward-subtracted B_T",
  "toy_rows":rows,
  "iteration150_authority":{
    "kinematics":"six finite off-shell triplets (p,-q,-r), p=q+r",
    "explicit_C5_columns":["Tr(Ricci^3)","cyclic(Riemann^3)"],
    "finite_response_rank":"2/2",
    "status":"VALID_FINITE_OFFSHELL_C5_AUTHORITY_BUT_NOT_SOFT_B_T_DATA"
  },
  "iteration151_authority":{
    "EH_source_completed_Ward":"PASS_SCOPED",
    "curvature_cubic_soft_transverse_projection":"NOT_COMPUTED"
  },
  "required_soft_protocol":{
    "soft_family":"k_soft(epsilon)=epsilon*k0 with momentum conservation enforced for all epsilon",
    "hard_structure":"same physical metric/source convention; hard legs chosen target-independently",
    "operation_order":[
      "derive source-completed cubic vertex from covariant action",
      "subtract W[K2] at each epsilon",
      "project transverse tensor structure",
      "extract epsilon^2 coefficient at epsilon->0",
      "form six-row B_T comparator columns",
      "compute rank/SVD"
    ]
  },
  "classification":{
    "reuse_iteration150_numeric_columns_as_B_T":"FORBIDDEN_PROTOCOL_MISMATCH",
    "iteration150_scientific_result":"RETAIN_VALID_IN_ITS_FROZEN_FINITE_OFFSHELL_SCOPE",
    "C5_B_T":"BLOCKED_NEW_SOFT_DEFORMED_ACTION_LEVEL_COMPUTATION_REQUIRED",
    "ANSATZ_003":"NOT_CREATED",
    "Fisher_resources":"FORBIDDEN"
  },
  "retained_results":[
    "C5-NG-007 — FINITE_OFFSHELL_CUBIC_RESPONSE_DOES_NOT_DETERMINE_WARD_SUBTRACTED_SOFT2_COEFFICIENT",
    "SOFT-NG-003 — PRESERVING_SOFT0_SOFT1_AND_ONE_FINITE_POINT_STILL_LEAVES_SOFT2_FREE",
    "NG-FUNNEL-036 — TRANSVERSE_SOFT_COMPARATOR_COLUMNS_MUST_BE_RECOMPUTED_FROM_SOFT_DEFORMED_PARENT_ACTION"
  ],
  "model_readiness_percent":24,
  "readiness_change":"unchanged: protocol incompatibility is resolved, but the required C5 transverse columns still need a new action-level computation"
}

Path("results/c5_soft_transverse_compatibility_iteration176.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2,sort_keys=True))
