#!/usr/bin/env python3
"""Iteration 191: evaluate only the comparator K2 layer on the prospectively
frozen Iteration-190 withheld rows.

No candidate is evaluated.  Test whether the QG-NL-EXP-001 lambda tangent
v_NL=x^2 exp(x) can still be exactly compensated by the frozen local C5
quadratic basis {x,...,x^6}.  The original six-row exact compensation was
forced by finite-sample saturation.  Twelve withheld rows can distinguish
finite polynomial interpolation from the exponential tangent.
"""
from pathlib import Path
import json
import numpy as np
import sympy as sp

x=np.array([0.285525,0.2167875,0.239625,0.17735625,0.225225,0.1621125,
            0.793125,0.6021875,0.665625,0.49265625,0.625625,0.4503125],float)
A=np.column_stack([x**n for n in range(1,7)])
v=x*x*np.exp(x)
Aug=np.column_stack([A,v])
coef=np.linalg.lstsq(A,v,rcond=None)[0]
res=v-A@coef
sA=np.linalg.svd(A,compute_uv=False)
sAug=np.linalg.svd(Aug,compute_uv=False)

# High-precision nonzero certificate on a prospectively fixed subset: first 7
# withheld rows in row-id order.  A nonzero 7x7 minor proves augmented rank 7.
xs=[sp.Float(str(z),80) for z in x[:7]]
M7=sp.Matrix([[z**n for n in range(1,7)]+[z**2*sp.exp(z)] for z in xs])
det7=sp.N(M7.det(),70)
assert det7 != 0

out={
 "iteration":191,
 "model_readiness_percent":24,
 "scope":"Iteration-190 withheld comparator K2 rows only; no candidate evaluated",
 "protocol":"RQIR-WITHHELD-NULLSOFT-12-v1",
 "local_basis":["x","x^2","x^3","x^4","x^5","x^6"],
 "nonlocal_lambda_tangent":"x^2*exp(x)",
 "local_rank":int(np.linalg.matrix_rank(A,tol=1e-12)),
 "augmented_rank":int(np.linalg.matrix_rank(Aug,tol=1e-12)),
 "local_singular_values":sA.tolist(),
 "augmented_singular_values":sAug.tolist(),
 "local_condition_number":float(sA[0]/sA[-1]),
 "least_squares_local_coefficients":coef.tolist(),
 "nonlocal_minus_local_residual_l2":float(np.linalg.norm(res)),
 "nonlocal_minus_local_residual_maxabs":float(np.max(np.abs(res))),
 "relative_residual_l2":float(np.linalg.norm(res)/np.linalg.norm(v)),
 "first7_augmented_minor_det_70digit":str(det7),
 "classification":{
   "original_six_row_compensation":"FINITE_SAMPLE_SATURATION_NOT_THEORY_IDENTITY",
   "withheld_twelve_row_nonlocal_K2":"INDEPENDENT_OF_FROZEN_LOCAL_DIM12_QUADRATIC_BASIS",
   "exact_K2_preserving_nonlocal_plus_local_parameter_null":"ABSENT_ON_WITHHELD_ROWS_FOR_THIS_SEVEN_PARAMETER_BLOCK",
   "candidate_residual":"NOT_TESTED",
   "ANSATZ_003":"NOT_CREATED",
   "Fisher_resources":"FORBIDDEN"
 },
 "retained_results":[
   "NL-NG-006 — WITHHELD_ROWS_BREAK_THE_SIX_POINT_LOCAL_POLYNOMIAL_COMPENSATION_OF_THE_NONLOCAL_K2_TANGENT",
   "REL-NG-008 — EXACT_K2_CALIBRATION_REMOVES_THE_NONLOCAL_LAMBDA_NUISANCE_DIRECTION_ON_THE_WITHHELD_12ROW_BLOCK",
   "NG-FUNNEL-046 — FINITE_ROW_HARD_CONSTRAINT_SATURATION_MUST_BE_RETESTED_ON_PROSPECTIVELY_FROZEN_ROWS"
 ],
 "readiness_change":"unchanged: a major finite-sample degeneracy is broken prospectively, but AS/C3 remain blocked and no candidate residual has been tested"
}
Path('results/withheld_k2_conditioning_iteration191.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
