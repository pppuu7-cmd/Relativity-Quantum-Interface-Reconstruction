#!/usr/bin/env python3
"""Iteration 499: exact truncation-series audit for frozen mixed central4.

This is estimator/provenance authority only.  It does not alter any frozen gate,
threshold, dynamics, support order, BASE/HALF convention, or ds=-d_base.
"""
from fractions import Fraction
from math import factorial
import json

nodes = (-2, -1, 1, 2)
c = (Fraction(1, 12), Fraction(-2, 3), Fraction(2, 3), Fraction(-1, 12))

moments = {n: sum(ci * (x ** n) for ci, x in zip(c, nodes)) for n in range(10)}
series = {n: moments[n] / factorial(n) for n in range(10) if moments[n]}

assert moments[0] == 0
assert moments[1] == 1
assert moments[2] == moments[3] == moments[4] == 0
assert series[5] == Fraction(-1, 30)
assert series[7] == Fraction(-1, 252)
assert series[9] == Fraction(-1, 4320)

# If L_h = d + a h^4 d^5 + b h^6 d^7 + c8 h^8 d^9 + O(h^10),
# then D_h = L_h^x L_h^y.  Record the exact mixed coefficients through h^8.
a = series[5]
b = series[7]
c8 = series[9]
mixed = {
    "h4_axis_terms": a,
    "h6_axis_terms": b,
    "h8_axis_terms": c8,
    "h8_cross_d5x_d5y": a * a,
}
assert mixed["h8_cross_d5x_d5y"] == Fraction(1, 900)

# HALF uses h/2 in each direction, so order-h^p terms scale by 2^-p.
half_scaling = {4: Fraction(1, 16), 6: Fraction(1, 64), 8: Fraction(1, 256)}
base_minus_half = {p: Fraction(1, 1) - s for p, s in half_scaling.items()}
assert base_minus_half == {4: Fraction(15, 16), 6: Fraction(63, 64), 8: Fraction(255, 256)}

out = {
    "iteration": 499,
    "classification": "PASS_CENTRAL4_MIXED_TRUNCATION_SERIES_EXACT__NON_PROMOTING",
    "nodes": list(nodes),
    "coefficients": [str(x) for x in c],
    "moments_0_to_9": {str(k): str(v) for k, v in moments.items()},
    "one_dimensional_series": {str(k): str(v) for k, v in series.items()},
    "mixed_through_h8": {k: str(v) for k, v in mixed.items()},
    "half_scaling_by_order": {str(k): str(v) for k, v in half_scaling.items()},
    "base_minus_half_factor_by_order": {str(k): str(v) for k, v in base_minus_half.items()},
    "scope": "estimator/provenance only; asymptotic smooth-field statement, not an exact mode-independent Richardson law",
    "model_readiness": 24,
}
print(json.dumps(out, indent=2, sort_keys=True))
