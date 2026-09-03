#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 303.

Exact combinatorial audit of the HV-like evanescent polynomial basis invisible
to the four-dimensional Iteration-295 triangle numerator oracle.

With all external vectors/tensors in a barred 4D subspace and no external
vectors in the evanescent subspace, O(D-4) covariance implies that evanescent
loop dependence enters through mu^2=-hat(l)^2. A total numerator degree ceiling
d therefore decomposes as
  P_d(bar l,mu^2)=sum_{r=0}^{floor(d/2)} (mu^2)^r P_{d-2r}(bar l).
The r=0 layer is exactly what the current 4D oracle reconstructs. All r>=1
layers vanish identically on its sampling surface and are therefore structurally
non-identifiable from those samples alone.
"""
from pathlib import Path
from math import comb
import json

HERE=Path(__file__).resolve().parent
RAW=HERE.parent/'results'/'iteration295_timelike_tru1_family_reconstruction_s0016.json'
r=json.loads(RAW.read_text())
assert r['iteration']==295


def nbar(deg):
    # Number of monomials of total degree <=deg in four barred components.
    return comb(deg+4,4)

rows={}
total_visible=0
total_hidden=0
for name,f in sorted(r['families'].items()):
    if f['family'] not in ('ordinary_triangle','raised_triangle'):
        continue
    d=int(f['degree_ceiling'])
    visible=nbar(d)
    assert visible==int(f['basis_size'])
    layers=[]
    hidden=0
    for rr in range(1,d//2+1):
        bd=d-2*rr
        n=nbar(bd)
        hidden+=n
        layers.append({'mu_power':2*rr,'barred_degree_ceiling':bd,'barred_monomial_count':n})
    rows[name]={
      'family':f['family'],
      'degree_ceiling':d,
      'visible_4d_oracle_basis_size':visible,
      'hidden_evanescent_basis_size':hidden,
      'hv_total_polynomial_basis_size':visible+hidden,
      'hidden_layers':layers,
      'hidden_fraction_of_hv_basis':hidden/(visible+hidden),
    }
    total_visible+=visible; total_hidden+=hidden

fam_counts={}
for x in rows.values(): fam_counts[x['family']]=fam_counts.get(x['family'],0)+1
assert fam_counts=={'ordinary_triangle':1,'raised_triangle':3},fam_counts
assert sorted(x['hidden_evanescent_basis_size'] for x in rows.values())==[16,86,86,86]
assert total_hidden==274

result={
 'iteration':303,
 'model_readiness_percent':24,
 'classification':'PASS_EXACT_TRIANGLE_EVANESCENT_BASIS_DIMENSION_AUDIT__274_HIDDEN_HV_POLYNOMIAL_COEFFICIENTS_BEFORE_PARENT_CONSTRAINTS',
 'candidate_residual':False,
 'assumption':'HV-like split with all external states barred-4D and O(D-4) covariance in the evanescent subspace; count is before imposing additional same-parent tensor/Ward constraints',
 'triangle_families':rows,
 'family_counts':fam_counts,
 'total_visible_4d_oracle_coefficients':total_visible,
 'total_hidden_evanescent_coefficients_before_parent_constraints':total_hidden,
 'total_hv_polynomial_coefficients':total_visible+total_hidden,
 'hidden_fraction_total':total_hidden/(total_visible+total_hidden),
 'structural_nonidentifiability_statement':'All 274 counted r>=1 coefficients multiply positive powers of mu^2 and vanish identically on the current four-dimensional loop-momentum sampling surface. They cannot be inferred from Iteration-295 4D oracle samples without additional same-parent D-dimensional structure.',
 'guardrails':[
   '274_IS_A_RAW_POLYNOMIAL_BASIS_COUNT_BEFORE_PARENT_WARD_OR_SYMMETRY_REDUCTION_NOT_274_NEW_PHYSICAL_PARAMETERS',
   'DO_NOT_ZERO_FILL_THE_HIDDEN_LAYERS',
   'BUBBLE_CUT_PROTECTION_FROM_ITERATION301_DOES_NOT_AUTOMATICALLY_EXTEND_TO_TRIANGLES',
   'TRIANGLE_CUT_PROMOTION_REQUIRES_D_PARENT_COEFFICIENTS_OR_A_PROOF_THAT_EACH_RELEVANT_HIDDEN_LAYER_IS_CUT_NULL'
 ],
 'next_gate':'reduce the 274 raw hidden triangle coefficients using same-parent tensor structure and cut power counting: first classify mu2/mu4/mu6 dimension-shifted ordinary/raised triangle normalized-cut pole orders; then only derive parent coefficients for layers capable of surviving epsilon->0.'
}
print(json.dumps(result,indent=2,sort_keys=True))
