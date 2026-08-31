#!/usr/bin/env python3
"""Iteration 203: shared-Wilson cross-polarization audit.

Iteration 202 proved that the declared Riemann-chain Box^n family can saturate
each finite 12-row v3 polarization protocol separately if enough local analytic
orders are admitted.  Physical Wilson coefficients are not polarization-specific,
so this audit stacks v3-A and v3-B vertically and uses one coefficient per Box
power across both protocols.

For each hard node x_i the family obeys

  S_A(i) = r_A(i) f(x_i),
  S_B(i) = r_B(i) f(x_i),

for the same scalar polynomial/analytic function f.  Therefore every member of
this family satisfies twelve exact cross-polarization relations

  r_B(i) S_A(i) - r_A(i) S_B(i) = 0.

These relations are family-specific.  They are NOT claimed to annihilate the
full all-orders C5 tensor EFT, whose higher-dimension operator basis can contain
other derivative/tensor contractions.
"""
from pathlib import Path
import json
import numpy as np

A=json.loads(Path('results/withheld_v3_local_c5_soft2_iteration197.json').read_text())
B=json.loads(Path('results/withheld_v3_local_c5_soft2_iteration199.json').read_text())
x=np.array(A['q2'],float); xb=np.array(B['q2'],float)
rA=np.array(A['Riemann3_soft2'],float); rB=np.array(B['Riemann3_soft2'],float)
assert np.allclose(x,xb,rtol=0,atol=1e-13)

def family(r,ncols):
    return np.column_stack([r if n==0 else (2/3)*r*((-x)**n) for n in range(ncols)])

ladder=[]
for ncols in range(4,13):
    V=np.vstack([family(rA,ncols),family(rB,ncols)])
    s=np.linalg.svd(V,compute_uv=False)
    ladder.append({'ncols':ncols,'max_box_power':ncols-1,'stack_rank_tol_1e-12':int(np.linalg.matrix_rank(V,tol=1e-12)),
                   'smax':float(s[0]),'smin':float(s[-1]),'condition_number':float(s[0]/s[-1])})

V12=np.vstack([family(rA,12),family(rB,12)])
L=np.zeros((12,24))
for i in range(12):
    L[i,i]=rB[i]
    L[i,12+i]=-rA[i]
rel=L@V12
s12=np.linalg.svd(V12,compute_uv=False)

out={
 'iteration':203,'date':'2026-09-01','model_readiness_percent':23,
 'protocol':'joint v3-A + v3-B, identical hard nodes, common Wilson coefficients',
 'family':'Riemann-chain Box^n zero-K2 local analytic cubic family',
 'stack_shape':[24,12],
 'rank_12column_stack':int(np.linalg.matrix_rank(V12,tol=1e-12)),
 'left_null_dimension_for_family':int(24-np.linalg.matrix_rank(V12,tol=1e-12)),
 'singular_values_12column_stack':s12.tolist(),
 'condition_number_12column_stack':float(s12[0]/s12[-1]),
 'cross_relation':'for each node i: rB_i*S_A_i-rA_i*S_B_i=0',
 'cross_relation_matrix_rank':int(np.linalg.matrix_rank(L,tol=1e-12)),
 'max_abs_cross_relation_on_12column_family':float(np.max(np.abs(rel))),
 'ladder':ladder,
 'classification':{
   'single_family_shared_wilson_stack':'RANK12_OF_24_WITH_12_EXACT_CROSS_POLARIZATION_RELATIONS',
   'separate_protocol_saturation':'DOES_NOT_IMPLY_SHARED_WILSON_24ROW_SATURATION',
   'full_all_orders_C5_tensor_basis':'BLOCKED_NOT_REDUCED_TO_SINGLE_FAMILY',
   'candidate_residual':'NONE',
   'AS':'BLOCKED_NOT_ZERO','C3':'BLOCKED_NOT_ZERO','ANSATZ_003':'NOT_CREATED','Fisher_resources':'FORBIDDEN'},
 'retained_results':[
   'REL-NG-016 — SHARED_WILSON_RIEMANN_DERIVATIVE_TOWER_HAS_TWELVE_EXACT_CROSS_POLARIZATION_RELATIONS_ON_V3_A_PLUS_B',
   'C5-NG-020 — SINGLE_ANALYTIC_TENSOR_FAMILY_SATURATES_EACH_12ROW_PROTOCOL_SEPARATELY_BUT_ONLY_RANK12_ON_THE_COMMON_COEFFICIENT_24ROW_STACK',
   'NG-FUNNEL-058 — PHYSICAL_COMPARATOR_COEFFICIENTS_MUST_BE_SHARED_ACROSS_POLARIZATION_PROTOCOLS_BEFORE_DECLARING_FINITE_INTERPOLATION_DEGENERACY_OR_RESIDUAL'
 ],
 'readiness_change':'unchanged at 23%: shared-coefficient relations recover useful structure, but the full all-orders C5 tensor remainder plus AS/C3 are not closed'
}
Path('results/c5_shared_wilson_cross_polarization_iteration203.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
