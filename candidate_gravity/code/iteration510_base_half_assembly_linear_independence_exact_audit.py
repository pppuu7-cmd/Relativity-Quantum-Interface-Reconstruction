#!/usr/bin/env python3
"""Iteration 510 exact BASE/HALF assembly linear-independence audit.

This audit is purely algebraic/provenance. It uses the frozen tensor-product
central4 geometry in BASE-h units and exact rational arithmetic. It proves that
BASE and HALF are two independent linear functionals on the 28 distinct sampled
coordinates, while the retained BASE-minus-HALF discrepancy is exactly their
linear combination and therefore is not a third independent observable.
"""

from fractions import Fraction
import json
from pathlib import Path

OFFSETS = [Fraction(-2), Fraction(-1), Fraction(1), Fraction(2)]
COEFFS = [Fraction(1, 12), Fraction(-2, 3), Fraction(2, 3), Fraction(-1, 12)]


def frac(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def rank_rational(rows):
    a = [list(r) for r in rows]
    m, n = len(a), len(a[0]) if a else 0
    rank = 0
    col = 0
    while rank < m and col < n:
        pivot = next((i for i in range(rank, m) if a[i][col] != 0), None)
        if pivot is None:
            col += 1
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        p = a[rank][col]
        a[rank] = [v / p for v in a[rank]]
        for i in range(m):
            if i != rank and a[i][col] != 0:
                f = a[i][col]
                a[i] = [x - f * y for x, y in zip(a[i], a[rank])]
        rank += 1
        col += 1
    return rank


base = {}
half = {}
for i, x in enumerate(OFFSETS):
    for j, y in enumerate(OFFSETS):
        base[(x, y)] = COEFFS[i] * COEFFS[j]
        # HALF step is h/2, so each 1D derivative gets factor 2/h.
        half[(x / 2, y / 2)] = 4 * COEFFS[i] * COEFFS[j]

union = sorted(set(base) | set(half))
wb = [base.get(p, Fraction(0)) for p in union]
wh = [half.get(p, Fraction(0)) for p in union]
wd = [b - h for b, h in zip(wb, wh)]

assert len(base) == 16
assert len(half) == 16
assert len(set(base) & set(half)) == 4
assert len(union) == 28
assert rank_rational([wb, wh]) == 2
assert rank_rational([wb, wh, wd]) == 2
assert all(d == b - h for d, b, h in zip(wd, wb, wh))

# Exact Gram matrix in the 28-coordinate Euclidean coefficient space.
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
gbb = dot(wb, wb)
gbh = dot(wb, wh)
ghh = dot(wh, wh)
gram_det = gbb * ghh - gbh * gbh
assert gram_det > 0

# There are BASE-only and HALF-only coordinates with nonzero weights, which is
# an immediate exact witness that the two rows cannot be proportional.
base_only = [p for p in union if p in base and p not in half and base[p] != 0]
half_only = [p for p in union if p in half and p not in base and half[p] != 0]
assert base_only and half_only

result = {
    "iteration": 510,
    "classification": "PASS_BASE_HALF_ASSEMBLY_LINEAR_INDEPENDENCE_EXACT__NON_PROMOTING",
    "scope": "exact frozen central4 assembly/provenance only",
    "coordinate_count": len(union),
    "base_source_occurrences": len(base),
    "half_source_occurrences": len(half),
    "overlap_coordinates": len(set(base) & set(half)),
    "rank_base_half": rank_rational([wb, wh]),
    "rank_base_half_delta": rank_rational([wb, wh, wd]),
    "nullity_base_half_on_union": len(union) - rank_rational([wb, wh]),
    "exact_relation": "W_DELTA = W_BASE - W_HALF",
    "gram_matrix": [[frac(gbb), frac(gbh)], [frac(gbh), frac(ghh)]],
    "gram_determinant": frac(gram_det),
    "independence_witness": {
        "base_only_nonzero_count": len(base_only),
        "half_only_nonzero_count": len(half_only),
    },
    "guardrail": "BASE, HALF, and BASE-HALF discrepancy must not be counted as three independent assembled observables/constraints; delta is a derived diagnostic from the same two linear functionals.",
    "nonclaims": [
        "not Candidate-Gravity consistency PASS or FAIL",
        "not physical promotion of unresolved index 2",
        "not comparator identity or novelty certificate",
        "not identifiability/Fisher authority",
        "does not authorize ANSATZ-003 or Fisher/resources",
    ],
    "model_readiness_percent": 24,
}

out = Path("candidate_gravity/results/iteration510_base_half_assembly_linear_independence_exact_audit.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
