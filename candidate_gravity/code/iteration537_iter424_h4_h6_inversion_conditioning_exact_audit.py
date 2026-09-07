#!/usr/bin/env python3
"""Exact conditioning audit for the frozen Iteration-424 h4/h6 inversion.

This is diagnostic-only and non-promoting. It changes no dynamics, mass nodes,
precision settings, thresholds, successor order, or physical acceptance clause.
"""
from fractions import Fraction
from decimal import Decimal, getcontext
import json
import math

# d = M [A,B]^T under X_h = D + A + B + O(h^8), with
# A=a h^4, B=b h^6, BASE=h, HALF=h/2, QUARTER=h/4.
M = (
    (Fraction(15,16), Fraction(63,64)),
    (Fraction(15,256), Fraction(63,4096)),
)

def det2(A):
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]

D = det2(M)
assert D == Fraction(-2835,65536)

Minv = (
    ( M[1][1]/D, -M[0][1]/D),
    (-M[1][0]/D,  M[0][0]/D),
)
assert Minv == (
    (Fraction(-16,45), Fraction(1024,45)),
    (Fraction(256,189), Fraction(-4096,189)),
)

# Exact M^T M.
a,b = M[0]
c,d = M[1]
mtm = (
    (a*a+c*c, a*b+c*d),
    (a*b+c*d, b*b+d*d),
)
assert mtm == (
    (Fraction(57825,65536), Fraction(968625,1048576)),
    (Fraction(968625,1048576), Fraction(16260993,16777216)),
)

trace = mtm[0][0] + mtm[1][1]
det_mtm = det2(mtm)
disc = trace*trace - 4*det_mtm
assert trace == Fraction(31064193,16777216)
assert det_mtm == Fraction(8037225,4294967296)
assert disc == Fraction(962877176430849,281474976710656)

# Since sqrt(disc)=sqrt(N)/2^24 and trace=T/2^24,
# kappa_2=sqrt((T+sqrt(N))/(T-sqrt(N))).
T = 31064193
N = 962877176430849
getcontext().prec = 60
sqrtN = Decimal(N).sqrt()
kappa2 = ((Decimal(T)+sqrtN)/(Decimal(T)-sqrtN)).sqrt()

result = {
    "iteration": 537,
    "classification": "PASS_ITER424_H4_H6_INVERSION_CONDITIONING_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING",
    "forward_matrix": [[str(x) for x in row] for row in M],
    "inverse_matrix": [[str(x) for x in row] for row in Minv],
    "det_forward": str(D),
    "mtm": [[str(x) for x in row] for row in mtm],
    "trace_mtm": str(trace),
    "det_mtm": str(det_mtm),
    "discriminant_mtm": str(disc),
    "kappa2_exact": "sqrt((31064193+sqrt(962877176430849))/(31064193-sqrt(962877176430849)))",
    "kappa2_decimal": str(kappa2),
    "interpretation": {
        "invertible": True,
        "conditioning_scope": "unscaled h4/h6 coefficient inversion in [A,B] coordinates",
        "distinct_from_iteration531": "Iteration 531 conditions normalized BASE/HALF/QUARTER stencil rows; this audit conditions the two-difference truncation-component inversion.",
        "near_degeneracy_claim": False,
        "physical_promotion": False
    },
    "model_readiness_percent": 24
}
print(json.dumps(result, indent=2, sort_keys=True))
