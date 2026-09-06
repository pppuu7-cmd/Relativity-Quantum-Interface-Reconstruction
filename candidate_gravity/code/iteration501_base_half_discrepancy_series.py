from fractions import Fraction
import json

# Frozen mixed-central4 expansion retained from Iteration 499:
# D_h = dxy + a4 h^4 S4 + a6 h^6 S6 + h^8(a8 Spure8 + b8 Scross8) + O(h^10)
# where
# S4 = d_x^5 d_y + d_x d_y^5
# S6 = d_x^7 d_y + d_x d_y^7
# Spure8 = d_x^9 d_y + d_x d_y^9
# Scross8 = d_x^5 d_y^5

a4 = -Fraction(1, 30)
a6 = -Fraction(1, 252)
a8 = -Fraction(1, 4320)
b8 = Fraction(1, 900)

# HALF uses h/2, so BASE-minus-HALF multiplies each h^n sector by (1 - 2^-n).
c4 = a4 * (1 - Fraction(1, 16))
c6 = a6 * (1 - Fraction(1, 64))
c8_pure = a8 * (1 - Fraction(1, 256))
c8_cross = b8 * (1 - Fraction(1, 256))

assert c4 == -Fraction(1, 32)
assert c6 == -Fraction(1, 256)
assert c8_pure == -Fraction(17, 73728)
assert c8_cross == Fraction(17, 15360)

# The leading discrepancy coefficient is exact within the smooth-field asymptotic expansion.
# This does NOT license a universal Richardson identity or any change to frozen ds=-d_base.

out = {
    "classification": "PASS_BASE_HALF_DISCREPANCY_ASYMPTOTIC_SERIES_EXACT__NON_PROMOTING",
    "base_minus_half": {
        "h4_S4": str(c4),
        "h6_S6": str(c6),
        "h8_Spure8": str(c8_pure),
        "h8_Scross8": str(c8_cross),
    },
    "statement": "D_BASE-D_HALF = -h^4/32 S4 - h^6/256 S6 + h^8[-17/73728 Spure8 + 17/15360 Scross8] + O(h^10).",
    "scope": "smooth-field asymptotic estimator/provenance authority only; no universal mode-independent Richardson promotion",
}

print(json.dumps(out, indent=2))
