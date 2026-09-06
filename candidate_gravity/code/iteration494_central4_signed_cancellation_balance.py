from fractions import Fraction
import json

c = [Fraction(1,12), Fraction(-2,3), Fraction(2,3), Fraction(-1,12)]
weights = [[ci*cj for cj in c] for ci in c]

positive_mass = sum(w for row in weights for w in row if w > 0)
negative_mass_abs = sum(-w for row in weights for w in row if w < 0)
net_mass = sum(w for row in weights for w in row)
l1_mass = sum(abs(w) for row in weights for w in row)

assert positive_mass == Fraction(9,8)
assert negative_mass_abs == Fraction(9,8)
assert net_mass == 0
assert l1_mass == Fraction(9,4)

# For D_h = h^-2 sum_ij w_ij F_ij, split the numerator into
# P = sum_{w>0} w F and N = sum_{w<0} |w| F, so D_h=(P-N)/h^2.
# The signed stencil itself has exactly balanced positive and negative masses 9/8.
# Therefore small |P-N| can arise from cancellation even when P and N are individually large.
# A useful diagnostic condition indicator is kappa_cancel=(|P|+|N|)/|P-N| when P!=N.
# It is unbounded as P->N and is diagnostic only; it is not by itself a consistency FAIL.

out = {
    "classification": "PASS_CENTRAL4_SIGNED_WEIGHT_CANCELLATION_BALANCE_EXACT__NON_PROMOTING",
    "central4_coefficients": [str(x) for x in c],
    "positive_mixed_weight_mass": str(positive_mass),
    "negative_mixed_weight_mass_abs": str(negative_mass_abs),
    "net_mixed_weight_mass": str(net_mass),
    "mixed_l1_weight_mass": str(l1_mass),
    "assembly_split": "D_h=(P-N)/h^2 with P=sum_{w>0} w F and N=sum_{w<0} |w| F",
    "cancellation_indicator": "kappa_cancel=(|P|+|N|)/|P-N| for P!=N",
    "scope": "exact estimator/provenance diagnostic; large cancellation is not Candidate-Gravity consistency FAIL and does not weaken frozen gates"
}
print(json.dumps(out, indent=2))
