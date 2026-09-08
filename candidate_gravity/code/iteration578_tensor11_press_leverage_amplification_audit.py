#!/usr/bin/env python3
from fractions import Fraction
import json

x = [Fraction(1,1), Fraction(9,16), Fraction(1,4), Fraction(1,16)]
# Exact one-axis leverages inherited from Iter577 exact calculation.
h1 = [Fraction(209,258), Fraction(23,86), Fraction(89,258), Fraction(149,258)]
h2 = [[a*b for b in h1] for a in h1]
amp = [[Fraction(1,1)/(1-h) for h in row] for row in h2]

flat_h = [h for row in h2 for h in row]
flat_a = [a for row in amp for a in row]
assert sum(flat_h, Fraction(0,1)) == Fraction(4,1)
assert max(flat_h) == Fraction(43681,66564)
assert min(flat_h) == Fraction(529,7396)
assert max(flat_a) == Fraction(66564,22883)
assert min(flat_a) == Fraction(7396,6867)
assert all(h < 1 for h in flat_h)

out = {
  "iteration": 578,
  "observable": "original Iter421 tensor11 degree-(1,1) fit",
  "classification": "PASS_ITER421_TENSOR11_PRESS_LEVERAGE_AMPLIFICATION_AUDIT_EXACT__NON_PROMOTING",
  "one_axis_leverages": [f"{v.numerator}/{v.denominator}" for v in h1],
  "two_axis_leverage_sum": "4",
  "h_min": "529/7396",
  "h_max": "43681/66564",
  "press_amplification_formula": "LOO residual_i = ordinary residual_i/(1-h_ii)",
  "press_amplification_min": "7396/6867",
  "press_amplification_max": "66564/22883",
  "press_amplification_min_decimal": float(Fraction(7396,6867)),
  "press_amplification_max_decimal": float(Fraction(66564,22883)),
  "all_finite": True,
  "interpretation": "No frozen symmetric-cross observation has divergent leave-one-out amplification; worst exact leverage-only amplification is below 2.91. Diagnostic only; does not alter or relax the frozen tensor11 statistic or threshold."
}
print(json.dumps(out, indent=2))
