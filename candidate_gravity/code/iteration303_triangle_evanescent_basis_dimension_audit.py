#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 303.

Exact combinatorial audit of the HV-like evanescent polynomial basis invisible
to the four-dimensional direct-timelike triangle numerator oracle.

Frozen upstream sector authority (Iterations 292/293/295):
- one ordinary-triangle sector, degree ceiling 4, full-coordinate 4D basis 70;
- three raised-triangle sectors, degree ceiling 6, full-coordinate 4D basis 210 each;
- Iteration 295 validates all eight non-scaleless direct-timelike families.

With external vectors/tensors in a barred 4D subspace and O(D-4) covariance in
the evanescent subspace, hidden loop dependence enters through mu^2=-hat(l)^2:
  P_d(bar l,mu^2)=sum_{r=0}^{floor(d/2)} (mu^2)^r P_{d-2r}(bar l).
The r=0 layer is the 4D-oracle layer. All r>=1 layers vanish on that sampling
surface and cannot be inferred from it alone.
"""
from pathlib import Path
from math import comb
import json

HERE=Path(__file__).resolve().parent
R295=HERE.parent/'results'/'iteration295_timelike_tru1_family_reconstruction_s0016.json'
r295=json.loads(R295.read_text())
assert r295['iteration']==295
assert r295['non_scaleless_family_count']==8
assert r295['classification'].startswith('PASS_DIRECT_TIMELIKE_S0016')


def nbar(deg):
    return comb(deg+4,4)

# Sector multiplicities and degree ceilings are frozen by Iterations 292/293.
sectors=[
  ('ordinary_triangle',4,70,1),
  ('raised_triangle',6,210,3),
]
rows={}
total_visible=0
total_hidden=0
for family,d,certified_visible,multiplicity in sectors:
    visible=nbar(d)
    assert visible==certified_visible
    layers=[]; hidden=0
    for rr in range(1,d//2+1):
        bd=d-2*rr; n=nbar(bd); hidden+=n
        layers.append({'mu_power':2*rr,'barred_degree_ceiling':bd,'barred_monomial_count':n})
    rows[family]={
      'multiplicity':multiplicity,
      'degree_ceiling':d,
      'visible_4d_oracle_basis_size_per_family':visible,
      'hidden_evanescent_basis_size_per_family':hidden,
      'hv_total_polynomial_basis_size_per_family':visible+hidden,
      'hidden_layers':layers,
      'hidden_fraction_per_family':hidden/(visible+hidden),
    }
    total_visible+=multiplicity*visible
    total_hidden+=multiplicity*hidden

assert rows['ordinary_triangle']['hidden_evanescent_basis_size_per_family']==16
assert rows['raised_triangle']['hidden_evanescent_basis_size_per_family']==86
assert total_visible==700
assert total_hidden==274

result={
 'iteration':303,
 'model_readiness_percent':24,
 'classification':'PASS_EXACT_TRIANGLE_EVANESCENT_BASIS_DIMENSION_AUDIT__274_HIDDEN_HV_POLYNOMIAL_COEFFICIENTS_BEFORE_PARENT_CONSTRAINTS',
 'candidate_residual':False,
 'upstream_authority':{
   'iteration295_classification':r295['classification'],
   'iteration295_non_scaleless_family_count':r295['non_scaleless_family_count'],
   'sector_structure':'Iteration292 denominator census plus Iteration293 basis ceilings: ordinary triangle degree4 basis70 x1; raised triangle degree6 basis210 x3'
 },
 'assumption':'HV-like split with external states barred-4D and O(D-4) covariance in the evanescent subspace; raw count is before additional same-parent tensor, Ward, routing or permutation constraints',
 'triangle_sector_basis':rows,
 'total_visible_4d_oracle_coefficients':total_visible,
 'total_hidden_evanescent_coefficients_before_parent_constraints':total_hidden,
 'total_hv_polynomial_coefficients':total_visible+total_hidden,
 'hidden_fraction_total':total_hidden/(total_visible+total_hidden),
 'structural_nonidentifiability_statement':'The 274 r>=1 coefficients multiply positive powers of mu^2 and vanish identically on the current four-dimensional loop-momentum sampling surface. They are not determined by Iteration-295 4D samples alone.',
 'guardrails':[
   '274_IS_A_RAW_POLYNOMIAL_BASIS_COUNT_BEFORE_PARENT_WARD_OR_SYMMETRY_REDUCTION_NOT_274_NEW_PHYSICAL_PARAMETERS',
   'DO_NOT_ZERO_FILL_THE_HIDDEN_LAYERS',
   'BUBBLE_CUT_PROTECTION_FROM_ITERATION301_DOES_NOT_AUTOMATICALLY_EXTEND_TO_TRIANGLES',
   'TRIANGLE_CUT_PROMOTION_REQUIRES_D_PARENT_COEFFICIENTS_OR_A_PROOF_THAT_EACH_RELEVANT_HIDDEN_LAYER_IS_CUT_NULL'
 ],
 'next_gate':'reduce the 274 raw hidden triangle coefficients by cut power counting first: classify mu2/mu4/mu6 dimension-shifted ordinary/raised triangle normalized-cut pole orders, then derive parent coefficients only for hidden layers capable of surviving epsilon->0.'
}
print(json.dumps(result,indent=2,sort_keys=True))
