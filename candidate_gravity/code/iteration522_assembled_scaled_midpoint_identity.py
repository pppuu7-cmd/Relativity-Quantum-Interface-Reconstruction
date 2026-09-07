from fractions import Fraction
import json
from pathlib import Path

# Frozen assembled scaled-MP threshold.
TAU = Fraction(2, 10**6)  # 2e-6 = 1/500000
assert TAU == Fraction(1, 500000)

# For real x,y define midpoint M=(x+y)/2 and d=|x-y|.
# Exact real identity:
# max(|x|,|y|) = max(|M+d_signed/2|, |M-d_signed/2|) = |M| + d/2.
# Therefore the repository's scaled discrepancy
#   d / max(1, |x|, |y|)
# is exactly
#   d / max(1, |M| + d/2).
# No approximation and no sign assumption are used.

# On the amplitude branch |M|+d/2 > 1, PASS at threshold tau obeys
# d <= tau (|M| + d/2), hence
# d <= [tau/(1-tau/2)] |M|.
amplitude_factor = TAU / (1 - TAU / 2)
assert amplitude_factor == Fraction(2, 999999)

# On the floor branch |M|+d/2 <= 1, PASS is simply d <= tau.

# If an independent certificate gives only 0 <= d <= R while midpoint magnitude m=|M|
# is fixed, f(d)=d/max(1,m+d/2) is monotone nondecreasing in d. Thus
#   sup_{0<=d<=R} f(d) = R/max(1,m+R/2).
# This is an exact worst-case transfer from a numerator-radius certificate to the
# repository's assembled scaled metric for fixed midpoint magnitude.

def scaled_from_pair(x: Fraction, y: Fraction) -> Fraction:
    d = abs(x - y)
    return d / max(Fraction(1), abs(x), abs(y))


def scaled_from_midpoint(x: Fraction, y: Fraction) -> Fraction:
    m = abs((x + y) / 2)
    d = abs(x - y)
    return d / max(Fraction(1), m + d / 2)

# Exact rational regression samples spanning signs and both denominator branches.
samples = [
    (Fraction(1, 10), Fraction(2, 10)),
    (Fraction(-3, 2), Fraction(-7, 5)),
    (Fraction(9, 4), Fraction(-1, 3)),
    (Fraction(-5, 2), Fraction(11, 4)),
    (Fraction(1), Fraction(1)),
]
for x, y in samples:
    assert scaled_from_pair(x, y) == scaled_from_midpoint(x, y)

result = {
    "iteration": 522,
    "classification": "PASS_ASSEMBLED_SCALED_MIDPOINT_DENOMINATOR_IDENTITY_EXACT__NON_PROMOTING",
    "scope": "numerical/assembly metric identity only",
    "frozen_threshold_tau": "1/500000",
    "exact_identity": "max(|A80|,|A120|)=|M|+d/2 for M=(A80+A120)/2 and d=|A80-A120|",
    "exact_scaled_form": "scaled=d/max(1,|M|+d/2)",
    "floor_branch_pass": "if |M|+d/2<=1, PASS iff d<=tau",
    "amplitude_branch_pass": "if |M|+d/2>1, PASS iff d<=[tau/(1-tau/2)]|M|",
    "amplitude_branch_factor": "2/999999",
    "fixed_midpoint_radius_transfer": "if 0<=d<=R and m=|M| is fixed, sup scaled = R/max(1,m+R/2)",
    "nonclaims": [
        "does not establish actual BASE or HALF assembled PASS before full support is available",
        "does not replace direct independent BASE/HALF MP80/MP120 assembly",
        "does not promote physical index 2",
        "does not establish Candidate-Gravity consistency",
        "does not establish comparator identity, non-identifiability, near-degeneracy, or novelty",
        "does not authorize ANSATZ-003, Fisher, or resource work"
    ],
    "model_readiness_percent": 24,
    "readiness_change_percentage_points": 0
}

out = Path("candidate_gravity/results/iteration522_assembled_scaled_midpoint_identity.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
