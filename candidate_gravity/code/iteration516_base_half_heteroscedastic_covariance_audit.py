from fractions import Fraction
import json

# Frozen central4 mixed-derivative rows, coefficients in units of 1/h^2.
c_base = {
    Fraction(-2): Fraction(1, 12),
    Fraction(-1): Fraction(-2, 3),
    Fraction(1): Fraction(2, 3),
    Fraction(2): Fraction(-1, 12),
}
c_half = {
    Fraction(-1): Fraction(1, 6),
    Fraction(-1, 2): Fraction(-4, 3),
    Fraction(1, 2): Fraction(4, 3),
    Fraction(1): Fraction(-1, 6),
}

coords = sorted(
    set((x, y) for x in c_base for y in c_base)
    | set((x, y) for x in c_half for y in c_half)
)
wb = {(x, y): c_base.get(x, 0) * c_base.get(y, 0) for x, y in coords}
wh = {(x, y): c_half.get(x, 0) * c_half.get(y, 0) for x, y in coords}
shared = [p for p in coords if wb[p] != 0 and wh[p] != 0]

assert len(coords) == 28
assert shared == [
    (Fraction(-1), Fraction(-1)),
    (Fraction(-1), Fraction(1)),
    (Fraction(1), Fraction(-1)),
    (Fraction(1), Fraction(1)),
]
assert all(wb[p] * wh[p] == Fraction(1, 81) for p in shared)
assert all((wb[p] - wh[p]) ** 2 == Fraction(25, 144) for p in shared)

# For independent, mean-zero, heteroscedastic coordinate errors e_p with
# Var(e_p)=v_p, exact assembled covariance is diagonal propagation:
#   Cov(BASE,HALF) = h^-4 sum_p wb[p] wh[p] v_p.
# Only the four shared nodes contribute, each with coefficient 1/81.
result = {
    "iteration": 516,
    "classification": "PASS_BASE_HALF_HETEROSCEDASTIC_DIAGONAL_COVARIANCE_EXACT__NON_PROMOTING",
    "scope": "independent mean-zero coordinate errors with arbitrary nonnegative per-coordinate variances",
    "coordinate_count": len(coords),
    "shared_nodes": [[str(x), str(y)] for x, y in shared],
    "covariance_formula": "Cov(BASE,HALF)=h^-4*(1/81)*sum_{p in shared} v_p",
    "shared_covariance_coefficient_each": "1/81",
    "shared_discrepancy_variance_coefficient_each": "25/144",
    "general_variance_formula_base": "Var(BASE)=h^-4*sum_p wb[p]^2 v_p",
    "general_variance_formula_half": "Var(HALF)=h^-4*sum_p wh[p]^2 v_p",
    "general_variance_formula_delta": "Var(BASE-HALF)=h^-4*sum_p (wb[p]-wh[p])^2 v_p",
    "sign_claim": "Cov(BASE,HALF)>=0 for diagonal independent coordinate noise; equality iff all four shared-node variances vanish",
    "iid_reduction": "if v_p=sigma^2 for all p, Cov(BASE,HALF)=(4/81)*sigma^2/h^4",
    "guardrail": "Do not infer physical covariance, do not treat BASE-HALF as independent, and do not replace assembled scaled-discrepancy gates with this stochastic propagation identity.",
    "MODEL_READINESS": "24%",
}

print(json.dumps(result, indent=2, sort_keys=True))
