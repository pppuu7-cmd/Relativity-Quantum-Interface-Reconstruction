from fractions import Fraction
import json
from pathlib import Path

# Frozen central4 first-derivative weights, expressed in units of 1/h.
BASE_1D = {
    Fraction(-2): Fraction(1, 12),
    Fraction(-1): Fraction(-2, 3),
    Fraction(1): Fraction(2, 3),
    Fraction(2): Fraction(-1, 12),
}
# HALF uses physical step h/2 and offsets in units of h.
HALF_1D = {
    Fraction(-1): Fraction(1, 6),
    Fraction(-1, 2): Fraction(-4, 3),
    Fraction(1, 2): Fraction(4, 3),
    Fraction(1): Fraction(-1, 6),
}

def tensor(weights):
    return {(x, y): ax * ay for x, ax in weights.items() for y, ay in weights.items()}

B = tensor(BASE_1D)
H = tensor(HALF_1D)
union = sorted(set(B) | set(H))
D = {p: B.get(p, Fraction(0)) - H.get(p, Fraction(0)) for p in union}

l1_B = sum(abs(v) for v in B.values())
l1_H = sum(abs(v) for v in H.values())
l1_D = sum(abs(v) for v in D.values())

assert l1_B == Fraction(9, 4)
assert l1_H == Fraction(9, 1)
assert l1_D == Fraction(397, 36)
assert len(union) == 28

# For coordinate-wise interval errors |e_i| <= eps*S_i, linear programming over a box gives
# sup |sum_i w_i e_i| = eps * sum_i |w_i| S_i.  Equality is attained by
# e_i = eps*S_i*sign(w_i), or its negative.  Therefore Iteration 519's bound is
# not merely sufficient: it is the exact minimax radius under the stated local interval model.

def frac_str(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)

result = {
    "iteration": 521,
    "classification": "PASS_LOCAL_MP_INTERVAL_TO_ASSEMBLED_SHARP_MINIMAX_CERTIFICATE_EXACT__NON_PROMOTING",
    "scope": "numerical/provenance only; coordinate-wise local MP interval model",
    "support_union_coordinates": len(union),
    "exact_l1_norms": {
        "BASE": frac_str(l1_B),
        "HALF": frac_str(l1_H),
        "BASE_MINUS_HALF": frac_str(l1_D),
    },
    "theorem": "If |e_i| <= eps*S_i independently coordinate-wise, then sup_box |h^-2 sum_i w_i e_i| = eps*h^-2 sum_i |w_i|S_i, attained by sign alignment.",
    "implication": "The Iteration-519 weighted envelope is the sharp worst-case minimax certificate for the stated interval model, not merely a loose sufficient triangle-inequality bound.",
    "nonclaims": [
        "does not imply assembled MP PASS until actual S_i values for complete support are evaluated",
        "does not promote physical index 2",
        "does not establish Candidate-Gravity consistency",
        "does not establish comparator identity/non-identifiability/near-degeneracy/novelty",
        "does not authorize ANSATZ-003, Fisher, or resource work",
    ],
    "model_readiness_percent": 24,
    "readiness_change_percentage_points": 0,
}

out = Path("candidate_gravity/results/iteration521_local_mp_sharp_minimax_certificate.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
