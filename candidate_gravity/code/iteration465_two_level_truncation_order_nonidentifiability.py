#!/usr/bin/env python3
"""Iteration 465: exact two-level truncation-order non-identifiability audit.

This is a scoped numerical-method identifiability result. It does not alter frozen
physics, estimator choice, thresholds, or model-readiness rubric.
"""
from fractions import Fraction
import json

# Let B=D(h), H=D(h/2). Under a single-power model D(h)=D0+a h^p,
# any p != 0 fits the same two observed levels exactly after solving for D0,a.
def continuum_weights(p: int):
    q = Fraction(2) ** p
    return {"H": q / (q - 1), "B": -Fraction(1, q - 1)}

w4 = continuum_weights(4)
w6 = continuum_weights(6)
assert w4 == {"H": Fraction(16, 15), "B": Fraction(-1, 15)}
assert w6 == {"H": Fraction(64, 63), "B": Fraction(-1, 63)}

# Difference of inferred continua from the same pair (B,H):
# D0[p=4]-D0[p=6] = 16(H-B)/315.
diff_B = w4["B"] - w6["B"]
diff_H = w4["H"] - w6["H"]
assert diff_B == Fraction(-16, 315)
assert diff_H == Fraction(16, 315)

result = {
    "iteration": 465,
    "classification": "REGIME_SPECIFIC_NON_IDENTIFIABILITY__TWO_LEVEL_TRUNCATION_ORDER__NON_PROMOTING",
    "statement": "With only BASE=D(h) and HALF=D(h/2), the formal leading power p is not identifiable: for every assumed p!=0, D0 and amplitude a can be chosen to fit both levels exactly.",
    "p4_continuum_weights": {k: str(v) for k,v in w4.items()},
    "p6_continuum_weights": {k: str(v) for k,v in w6.items()},
    "p4_minus_p6_inferred_continuum": {"B": str(diff_B), "H": str(diff_H)},
    "guardrail": "The 16 and 64 signatures from Iteration 464 are theoretical single-term scalings, not empirically identifiable orders from two levels alone. No Richardson promotion; retained ds=-d_base and all frozen thresholds are unchanged.",
    "promotion": False,
    "model_readiness": 24,
}
print(json.dumps(result, indent=2, sort_keys=True))
