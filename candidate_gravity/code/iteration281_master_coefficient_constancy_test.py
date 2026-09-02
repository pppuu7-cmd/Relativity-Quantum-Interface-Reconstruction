#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 281.

Guardrail test: do the Iteration-279 non-scaleless family traces admit a
constant-coefficient representation on the Iteration-280 scalar cut-support
basis?  This is deliberately a diagnostic, not an IBP reduction.
"""
import json
import numpy as np

s=np.arange(.004,.033,.004)
t=s+0.2
X=np.column_stack([1/s,1/t,np.log(s/t)/(s-t)])
y=np.array([
-13.609106332884231,-14.910818885815592,-16.464537419433167,-18.344887367747777,
-20.65906520134745,-23.566779268831326,-27.31688547355838,-32.31966851082898])
coef, *_ = np.linalg.lstsq(X,y,rcond=None)
pred=X@coef
res=y-pred
relative=float(np.linalg.norm(res)/np.linalg.norm(y))
max_abs=float(np.max(np.abs(res)))
result={
  'iteration':281,
  'model_readiness_percent':24,
  'test':'constant coefficients multiplying Iteration-280 three-dimensional scalar cut-support basis',
  'coefficients':[float(x) for x in coef],
  'relative_l2_residual':relative,
  'max_absolute_residual':max_abs,
  'rank':int(np.linalg.matrix_rank(X)),
  'classification':'FAIL_SCOPED_CONSTANT_MASTER_COEFFICIENT_SURROGATE_ON_TIMELIKE_SLICE',
  'interpretation':'Iteration-279 pre-integration family traces cannot be replaced by three kinematics-independent coefficients multiplying the scalar master cut-support shapes.',
  'guardrail':'THIS IS NOT A CONSISTENCY FAIL AND DOES NOT DETERMINE THE TRUE IBP-REDUCED C5 COEFFICIENT FUNCTIONS.',
  'next_gate':'reconstruct family numerators as p- and invariant-dependent tensor/rational functions and perform genuine tensor/IBP reduction to obtain coefficient functions of s,t'
}
assert np.linalg.matrix_rank(X)==3
assert relative>0.05
print(json.dumps(result,indent=2,sort_keys=True))
