from fractions import Fraction as F
import json

# Frozen three-level truncation map:
# d1 = BASE-HALF, d2 = HALF-QUARTER,
# A = a h^4, B = b h^6.
a11, a12 = F(15,16), F(63,64)
a21, a22 = F(15,256), F(63,4096)

# Ratio-free coordinates chosen to isolate B and A exactly.
# Q := d1 - 16 d2 ; P := 64 d2 - d1.
qA = a11 - 16*a21
qB = a12 - 16*a22
pA = 64*a21 - a11
pB = 64*a22 - a12

assert qA == 0
assert qB == F(189,256)
assert pA == F(45,16)
assert pB == 0

# Hence A=(16/45)P and B=(256/189)Q exactly.
assert F(16,45)*pA == 1
assert F(256,189)*qB == 1

result = {
    "iteration": 544,
    "classification": "PASS_ITER424_RATIO_FREE_H4_H6_CONE_FAIL_CLOSED_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING",
    "definitions": {
        "d1": "BASE-HALF",
        "d2": "HALF-QUARTER",
        "A": "a*h^4",
        "B": "b*h^6",
        "P": "64*d2-d1",
        "Q": "d1-16*d2"
    },
    "exact_identities": {
        "P": "45*A/16",
        "Q": "189*B/256",
        "A": "16*P/45",
        "B": "256*Q/189"
    },
    "bounded_error_contract": {
        "if": "|e1|<=eps1 and |e2|<=eps2",
        "P_error_radius": "eps1+64*eps2",
        "Q_error_radius": "eps1+16*eps2",
        "same_sign_FAIL_CLOSED_PASS": "P and Q intervals both exclude zero and have the same sign",
        "opposite_sign_FAIL_CLOSED_RESULT": "P and Q intervals both exclude zero and have opposite signs",
        "otherwise": "BLOCKED/AMBIGUOUS_DIAGNOSTIC; do not infer sign or cancellation"
    },
    "scope": [
        "numerical/truncation diagnostic only",
        "does not promote physical index 2",
        "not Candidate-Gravity consistency PASS/FAIL",
        "not exact comparator identity",
        "not regime-specific non-identifiability",
        "not model-level near-degeneracy",
        "not novelty certificate"
    ],
    "MODEL_READINESS": "24%"
}

print(json.dumps(result, indent=2, sort_keys=True))
