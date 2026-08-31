#!/usr/bin/env python3
"""Iteration 181: conditioning audit for QG-NL-EXP-001 on the frozen six B_T rows.

This does NOT substitute for the full tensor Frechet projection of the parent
action. It tests whether the existing six-row q^2 lever arm can numerically
resolve the characteristic analytic exponential form-factor shapes from the
already-authorized local C5 basis r0*{1,-x,x^2,-x^3}.
"""
from pathlib import Path
import json
import numpy as np

q2=np.array([0.5076,0.3854,0.4260,0.3153,0.4004,0.2882],float)
r0=np.array([-1.6411697071822275,0.06385882717014456,0.8548821188463769,-0.17055215671317986,-0.3261917310634991,-0.1655609264695088],float)
V=np.column_stack([r0,-q2*r0,q2**2*r0,-q2**3*r0])
P=V@np.linalg.pinv(V)

def Fm(x): return -(np.exp(x)-1.0)/x                  # F(-x), lambda=1

def dFm(x): return -(np.exp(x)*x-(np.exp(x)-1.0))/x**2

def d2Fm(x):
    h=1e-5
    return (dFm(x+h)-dFm(x-h))/(2*h)

shapes={
  'r0*F(-q2)':r0*Fm(q2),
  'r0*q2*dFminus_dx':r0*q2*dFm(q2),
  'r0*q2^2*d2Fminus_dx2':r0*q2**2*d2Fm(q2),
  'r0*exp(q2)':r0*np.exp(q2),
}
metrics={}
for name,c in shapes.items():
    res=c-P@c
    A=np.column_stack([V,c])
    s=np.linalg.svd(A,compute_uv=False)
    metrics[name]={
      'residual_norm':float(np.linalg.norm(res)),
      'relative_residual':float(np.linalg.norm(res)/np.linalg.norm(c)),
      'augmented_rank_tol_1e-10':int(np.linalg.matrix_rank(A,tol=1e-10)),
      'augmented_singular_values':s.tolist(),
      'fifth_singular_value':float(s[-1]),
    }

error_envelope=5.262558013335861e-06
out={
 'iteration':181,
 'comparator':'QG-NL-EXP-001',
 'scope':'conditioning/resolution audit only; full tensor action-level B_T projection remains required',
 'q2':q2.tolist(),
 'local_C5_rank':int(np.linalg.matrix_rank(V,tol=1e-10)),
 'local_C5_basis':'Riemann3_B_T * {1,-q2,q2^2,-q2^3}',
 'iteration178_extrapolation_error_envelope':error_envelope,
 'analytic_nonlocal_shape_metrics':metrics,
 'max_candidate_fifth_singular_value':float(max(v['fifth_singular_value'] for v in metrics.values())),
 'max_candidate_fifth_singular_over_error_envelope':float(max(v['fifth_singular_value'] for v in metrics.values())/error_envelope),
 'classification':{
   'six_row_formfactor_resolution':'NEAR_DEGENERATE_BELOW_EXISTING_B_T_NUMERICAL_ENVELOPE_FOR_TESTED_ANALYTIC_SHAPES',
   'full_QG_NL_EXP_001_B_T':'BLOCKED_NONLOCAL_B_T_TENSOR_FRECHET_IMPLEMENTATION_NOT_ZERO',
   'consistency_fail':False,
   'exact_comparator_identity':False,
   'novelty_certificate':'NONE',
   'ANSATZ_003':'NOT_CREATED',
   'Fisher_resources':'FORBIDDEN'},
 'guardrail':'A fifth blind singular value from an analytic nonlocal scalar shape must not be promoted while it lies below the frozen Iteration-178 B_T extrapolation/error envelope; the full tensor Frechet column is still required.',
 'model_readiness_percent':24,
 'readiness_change':'unchanged: this iteration exposes a resolution blocker/near-degeneracy but does not close the fixed nonlocal comparator or produce a residual'
}
Path('results/nonlocal_soft_transverse_resolution_audit_iteration181.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
