from fractions import Fraction as F
import json

# Frozen three-level central4 scaling:
# BASE=h, HALF=h/2, QUARTER=h/4.
# Write X_h = D + A + B + C + O(h^10), where
# A=a h^4, B=b h^6, C=c h^8.
# Then HALF and QUARTER scale these components by 2^-4k, 2^-6k, 2^-8k.

# d1 = BASE-HALF; d2 = HALF-QUARTER.
a1 = F(15,16); b1 = F(63,64); c1 = F(255,256)
a2 = F(15,256); b2 = F(63,4096); c2 = F(255,65536)

# Exact inversion of the h4/h6 two-component system.
# Ahat = -16/45 d1 + 1024/45 d2
# Bhat = 256/189 d1 - 4096/189 d2
A_d1, A_d2 = F(-16,45), F(1024,45)
B_d1, B_d2 = F(256,189), F(-4096,189)

assert A_d1*a1 + A_d2*a2 == 1
assert A_d1*b1 + A_d2*b2 == 0
assert B_d1*a1 + B_d2*a2 == 0
assert B_d1*b1 + B_d2*b2 == 1

# Exact h8 contamination of these diagnostics.
A_C = A_d1*c1 + A_d2*c2
B_C = B_d1*c1 + B_d2*c2
assert A_C == F(-17,64)
assert B_C == F(425,336)

# Frozen three-level Richardson diagnostic R3=(BASE-80 HALF+1024 QUARTER)/945.
# It cancels h4 and h6 and has leading h8 contamination C/1344.
r3_D = F(1-80+1024,945)
r3_A = F(1,945)*(1 - F(80,16) + F(1024,256))
r3_B = F(1,945)*(1 - F(80,64) + F(1024,4096))
r3_C = F(1,945)*(1 - F(80,256) + F(1024,65536))
assert r3_D == 1
assert r3_A == 0
assert r3_B == 0
assert r3_C == F(1,1344)

out = {
    "iteration": 536,
    "classification": "PASS_ITER424_THREE_LEVEL_H4_H6_ERROR_COMPONENT_INVERSION_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING",
    "frozen_levels": ["BASE=h", "HALF=h/2", "QUARTER=h/4"],
    "definitions": {
        "d1": "BASE-HALF",
        "d2": "HALF-QUARTER",
        "A": "a*h^4",
        "B": "b*h^6",
        "C": "c*h^8"
    },
    "exact_estimators": {
        "Ahat": "(-16*d1 + 1024*d2)/45",
        "Bhat": "(256*d1 - 4096*d2)/189"
    },
    "h8_contamination": {
        "Ahat": "A - (17/64)*C + O(h^10)",
        "Bhat": "B + (425/336)*C + O(h^10)",
        "R3": "D + C/1344 + O(h^10)"
    },
    "guardrail": "Diagnostic only: does not alter or rescue the frozen Iteration-424 five-clause physical gate; no physical promotion, ANSATZ-003, Fisher, or resources."
}
print(json.dumps(out, indent=2))
