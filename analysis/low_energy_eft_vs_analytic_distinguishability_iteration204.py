#!/usr/bin/env python3
"""Iteration 204: low-energy EFT-control versus analytic distinguishability.

This is a target-independent K2/design diagnostic, not a Candidate Gravity test.
Choose a low-energy hard-node family solely from an EFT-control target x_max=0.1:
scale the six historical base q vectors by s_hi=sqrt(0.1/max(x_base)) and by
s_lo=0.65*s_hi.  The ratio 0.65 is a fixed design choice, not optimized against
any candidate or residual.

Questions:
1. How small can the omitted local derivative remainder be under an *explicit*
   coefficient envelope |c_n|<=C?
2. What happens to distinguishability of the analytic nonlocal hard tangent
   x^2 exp(x) against the local polynomial basis [x,...,x^6] in the same IR
   regime?
"""
from pathlib import Path
import json, math
import numpy as np

ETA=np.diag([-1.,1.,1.,1.])
QS0=np.array([[0.18,0.70,0.20,0.10],[0.14,0.55,-0.25,0.20],[0.22,0.62,0.18,-0.24],[0.16,0.48,0.31,0.12],[0.20,0.58,-0.16,-0.28],[0.12,0.44,0.27,-0.19]],float)
base_x=np.array([q@ETA@q for q in QS0])
x_target=0.1
s_hi=math.sqrt(x_target/base_x.max())
s_lo=0.65*s_hi
x=np.concatenate([(s_lo**2)*base_x,(s_hi**2)*base_x])

A=np.column_stack([x**n for n in range(1,7)])
nl=x**2*np.exp(x)
Aug=np.column_stack([A,nl])
sv=np.linalg.svd(Aug,compute_uv=False)
AugN=Aug/np.linalg.norm(Aug,axis=0)
svn=np.linalg.svd(AugN,compute_uv=False)
coef=np.linalg.lstsq(A,nl,rcond=None)[0]
res=nl-A@coef

# Conditional geometric-series remainder bounds in the coefficient convention
# |c_n|<=C. Cubic dimension-12 Riemann chain retains n<=3, so omitted n>=4.
# Hard K2 local polynomial block retains powers through x^6, so omitted n>=7.
cubic_remainder_per_C=(2/3)*x_target**4/(1-x_target)
k2_remainder_per_C=x_target**7/(1-x_target)
critical_C_for_nonlocal_residual=float(np.max(np.abs(res))/k2_remainder_per_C)

out={
 'iteration':204,'date':'2026-09-01','model_readiness_percent':23,
 'scope':'target-independent low-energy K2/design diagnostic; no candidate and no polarization cubic evaluation',
 'design_rule':{'x_max_target':x_target,'s_hi':s_hi,'s_lo_ratio':0.65,'s_lo':s_lo},
 'x_rows':x.tolist(),'x_min':float(x.min()),'x_max':float(x.max()),
 'conditional_eft_remainder':{
   'assumption':'dimensionless omitted coefficients obey |c_n|<=C in the declared monomial normalization',
   'cubic_dimension12_omitted_n_ge_4_bound_per_C':cubic_remainder_per_C,
   'K2_local_through_x6_omitted_n_ge_7_bound_per_C':k2_remainder_per_C,
   'warning':'This is conditional on an explicit coefficient envelope; it is not a model-independent Wilson bound.'},
 'analytic_nonlocal_vs_local_K2':{
   'local_basis':['x','x^2','x^3','x^4','x^5','x^6'],
   'nonlocal_tangent':'x^2 exp(x)',
   'augmented_rank_tol_1e-15':int(np.linalg.matrix_rank(Aug,tol=1e-15)),
   'raw_condition_number':float(sv[0]/sv[-1]),
   'raw_smin':float(sv[-1]),
   'column_normalized_condition_number':float(svn[0]/svn[-1]),
   'column_normalized_smin':float(svn[-1]),
   'nonlocal_minus_local_residual_l2':float(np.linalg.norm(res)),
   'nonlocal_minus_local_relative_l2':float(np.linalg.norm(res)/np.linalg.norm(nl)),
   'nonlocal_minus_local_maxabs':float(np.max(np.abs(res))),
   'coefficient_envelope_C_where_K2_omitted_bound_equals_max_nonlocal_residual':critical_C_for_nonlocal_residual},
 'classification':{
   'low_energy_EFT_control':'POSSIBLE_ONLY_CONDITIONALLY_ON_EXPLICIT_WILSON_REMAINDER_ENVELOPE',
   'analytic_new_shape_in_deep_IR':'EXTREMELY_NEAR_DEGENERATE_WITH_LOCAL_EFT',
   'preferred_future_witness':'LINKED_NONANALYTIC_OR_CAUSAL_MULTIPOINT_RELATION',
   'candidate_residual':'NONE','ANSATZ_003':'NOT_CREATED','Fisher_resources':'FORBIDDEN'},
 'retained_results':[
   'EFT-NG-001 — DEEP_IR_IMPROVES_DERIVATIVE_REMAINDER_CONTROL_ONLY_AFTER_AN_EXPLICIT_WILSON_ENVELOPE_IS_DECLARED',
   'REL-NG-017 — DEEP_IR_ANALYTIC_NONLOCAL_TANGENT_BECOMES_EXTREMELY_NEAR_DEGENERATE_WITH_LOCAL_C5_POLYNOMIALS',
   'NG-FUNNEL-059 — HIGH_ENERGY_ANALYTIC_DISTINGUISHABILITY_AND_LOW_ENERGY_EFT_TRUNCATION_CONTROL_FORM_A_TRADEOFF',
   'NG-FUNNEL-060 — PRIORITIZE_LINKED_NONANALYTIC_MULTIPOINT_RELATIONS_OVER_FINITE_ANALYTIC_SHAPE_SEARCH'
 ],
 'readiness_change':'unchanged at 23%: the audit identifies a viable conditional low-energy strategy and a stronger future observable class, but no comparator gap is fully closed'
}
Path('results/low_energy_eft_vs_analytic_distinguishability_iteration204.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
