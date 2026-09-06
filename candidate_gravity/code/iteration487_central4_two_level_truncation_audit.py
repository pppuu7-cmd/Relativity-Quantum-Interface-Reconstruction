from fractions import Fraction
from math import factorial
import json

nodes = [-2, -1, 1, 2]
c = [Fraction(1,12), Fraction(-2,3), Fraction(2,3), Fraction(-1,12)]

moments = {k: sum(ci * (xi ** k) for ci, xi in zip(c, nodes)) for k in range(12)}
coeff = {k: Fraction(moments[k], factorial(k)) for k in (1,5,7,9,11)}

a5, a7, a9 = coeff[5], coeff[7], coeff[9]
# For D_h = L_h^x L_h^y, through O(h^8):
# f_11 + a5 h^4(f_51+f_15) + a7 h^6(f_71+f_17)
# + h^8[a9(f_91+f_19)+a5^2 f_55] + O(h^10).
# BASE-HALF means h versus h/2.
delta = {
    "h4_single": a5 * (1 - Fraction(1,16)),
    "h6_single": a7 * (1 - Fraction(1,64)),
    "h8_single": a9 * (1 - Fraction(1,256)),
    "h8_cross": (a5*a5) * (1 - Fraction(1,256)),
}

expected = {
    "h4_single": Fraction(-1,32),
    "h6_single": Fraction(-1,256),
    "h8_single": Fraction(-17,73728),
    "h8_cross": Fraction(17,15360),
}
assert delta == expected
assert [moments[k] for k in range(6)] == [0,1,0,0,0,-4]

out = {
    "classification": "PASS_CENTRAL4_TWO_LEVEL_TRUNCATION_MISMATCH_EXACT__NON_PROMOTING",
    "nodes": nodes,
    "coefficients": [str(x) for x in c],
    "moments_k0_to_k11": {str(k): str(v) for k,v in moments.items()},
    "one_dimensional_taylor_coefficients": {str(k): str(v) for k,v in coeff.items()},
    "base_minus_half_coefficients_through_h8": {k: str(v) for k,v in delta.items()},
    "leading_identity": "D_h-D_h/2 = -(h^4/32)(f_51+f_15) -(h^6/256)(f_71+f_17) + h^8[-17/73728(f_91+f_19)+17/15360 f_55] + O(h^10)",
    "scope": "exact estimator/truncation provenance only; no physics promotion; no Richardson authorization from two levels"
}
print(json.dumps(out, indent=2))
