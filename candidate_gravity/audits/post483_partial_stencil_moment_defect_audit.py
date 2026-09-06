#!/usr/bin/env python3
from fractions import Fraction
import json

x=[-2,-1,1,2]
c=[Fraction(1,12),Fraction(-2,3),Fraction(2,3),Fraction(-1,12)]

def moments(indices, max_k=5):
    return [sum(c[i]*Fraction(x[i])**k for i in indices) for k in range(max_k+1)]

full=moments(range(4),5)
known=moments(range(3),5)
missing=moments([3],5)
assert full == [0,1,0,0,0,-4]
assert known == [Fraction(1,12),Fraction(7,6),Fraction(1,3),Fraction(2,3),Fraction(4,3),Fraction(8,3)]
assert missing == [Fraction(-1,12),Fraction(-1,6),Fraction(-1,3),Fraction(-2,3),Fraction(-4,3),Fraction(-20,3)]
assert [known[k]+missing[k] for k in range(6)] == full

# Tensor-product mixed derivative inherits exactness only when both complete
# one-dimensional moment contracts are present. In the currently known BASE
# prefix ranks 0..11, v is complete but u omits x=+2, so the u moment defect
# survives and partial sums cannot be interpreted as fractional derivative
# completion.
result={
  'stage':'POST483_PARTIAL_CENTRAL4_STENCIL_MOMENT_DEFECT_AUDIT__EXACT',
  'classification':'PASS_PARTIAL_WEIGHT_COVERAGE_NOT_DERIVATIVE_COMPLETION__NON_PROMOTING',
  'scientific_gate_pass':True,
  'promotes_physical_coordinate':False,
  'MODEL_READINESS':'24%',
  'readiness_change_pp':0,
  'nodes':x,
  'coefficients':['1/12','-2/3','2/3','-1/12'],
  'full_moments_k0_to_k5':[str(v) for v in full],
  'known_rows_i0_to_i2_moments_k0_to_k5':[str(v) for v in known],
  'missing_row_i3_moments_k0_to_k5':[str(v) for v in missing],
  'exact_restoration':True,
  'interpretation':[
    'The complete central4 first-derivative stencil exactly satisfies M0=0, M1=1, M2=M3=M4=0; the first nonzero truncation moment is M5=-4.',
    'The currently known BASE rows i=0,1,2 do not satisfy those derivative moment conditions. The omitted i=3 row exactly cancels their moment defects through degree 4.',
    'Therefore 17/18=94.444% absolute stencil-weight coverage is only a perturbation-sensitivity diagnostic, not 94.444% derivative completion.',
    'The large magnitude of the known-12 partial spectral sum is structurally compatible with a missing outer row producing essential cancellation; it must not be compared to physical D_s.',
    'Full BASE derivative authority requires all four u rows, i.e. manifest ranks 0..15, with no zero-fill or inference.'
  ],
  'guardrails':['EXACT_RATIONAL_AUDIT','NO_PARTIAL_DERIVATIVE_PROMOTION','NO_ZERO_FILL','NO_SUPPORT_REORDERING','NO_THRESHOLD_CHANGE','NO_PHYSICAL_DS_PROMOTION','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
