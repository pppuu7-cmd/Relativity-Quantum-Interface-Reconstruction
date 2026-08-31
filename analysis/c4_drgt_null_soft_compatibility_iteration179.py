#!/usr/bin/env python3
"""Iteration 179: compatibility of the fixed dRGT C4 comparator with the frozen null-soft B_T protocol.

The frozen comparator C4-DRGT-001 has m^2=0.04 and cubic TT potential
V3 = m^2(3+alpha3)/8 Tr(H^3). The Iteration-175/177/178 B_T protocol is
conditioned on a physical null massless spin-2 soft leg k=(1,0,0,1), k^2=0.

For the fixed massive comparator the TT inverse kernel at that momentum is
K2 = k^2 + m^2 = m^2 != 0, so the null leg is not a physical dRGT soft pole.
A metric-only massless soft Ward subtraction is therefore not the same frozen
physical observable for this comparator. Unsupported projection must be BLOCKED,
not zero-filled.

In the formal m^2 -> 0 boundary the dRGT nonderivative cubic potential vanishes
linearly with m^2 and the TT propagator approaches the massless EH boundary, but
that is not the fixed m^2=0.04 comparator point and does not authorize a tangent
column there.
"""
from pathlib import Path
import json

m2=0.04
alpha3=0.0
k2_null=0.0
K2_null=k2_null+m2
v3_coeff=m2*(3+alpha3)/8
m2_seq=[0.04,0.02,0.01,0.005,0.0025]
v3_seq=[x*(3+alpha3)/8 for x in m2_seq]
ratios=[v3_seq[i+1]/v3_seq[i] for i in range(len(v3_seq)-1)]

out={
  'iteration':179,
  'comparator':'C4-DRGT-001',
  'frozen_m2':m2,
  'frozen_alpha3':alpha3,
  'null_soft_k2':k2_null,
  'TT_inverse_kernel_at_null_soft':K2_null,
  'physical_null_soft_pole_at_frozen_point':False,
  'cubic_TT_potential_coefficient_m2_times_3plusalpha3_over8':v3_coeff,
  'formal_massless_boundary':{
    'm2_sequence':m2_seq,
    'V3_coefficients':v3_seq,
    'halving_ratios':ratios,
    'limit':'V3_dRGT -> 0 linearly as m2 -> 0; TT propagator approaches massless EH boundary'},
  'classification':{
    'fixed_dRGT_B_T':'BLOCKED_C4_NULL_SOFT_PROTOCOL_MISMATCH',
    'zero_column_authorized':False,
    'consistency_fail':False,
    'theory_excluded':False,
    'massless_boundary_same_fixed_comparator':False,
    'ANSATZ_003':'NOT_CREATED',
    'Fisher_resources':'FORBIDDEN'},
  'retained_results':[
    'C4-NG-009 — FIXED_NONZERO_MASS_DRGТ_COMPARATOR_DOES_NOT_SHARE_THE_PHYSICAL_NULL_SOFT_POLE_OF_THE_B_T_PROTOCOL',
    'SOFT-NG-006 — COMPARATOR_PROTOCOL_MISMATCH_MUST_BE_BLOCKED_NOT_ZERO_FILLED',
    'C4-NG-010 — FORMAL_DRGТ_MASSLESS_TT_BOUNDARY_REMOVES_THE_NONDERIVATIVE_CUBIC_POTENTIAL_AND_COLLAPSES_TOWARD_THE_SHARED_EH_TT_BOUNDARY'],
  'model_readiness_percent':24,
  'readiness_change':'unchanged: C4 protocol applicability is clarified, but a compatible fixed C4 transverse control and the nonlocal/AS/C3 completion remain open'
}
Path('results/c4_drgt_null_soft_compatibility_iteration179.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
