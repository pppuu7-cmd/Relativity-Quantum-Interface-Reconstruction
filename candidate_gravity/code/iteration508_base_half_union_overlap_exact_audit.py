#!/usr/bin/env python3
from fractions import Fraction
import json

# Frozen fourth-order central first-derivative stencil.
offsets = (-2, -1, 1, 2)
c = {
    -2: Fraction(1, 12),
    -1: Fraction(-2, 3),
    1: Fraction(2, 3),
    2: Fraction(-1, 12),
}

# Coordinates are expressed in units of BASE_H = h.
base_axis = tuple(Fraction(k, 1) for k in offsets)
half_axis = tuple(Fraction(k, 2) for k in offsets)
base_nodes = {(x, y) for x in base_axis for y in base_axis}
half_nodes = {(x, y) for x in half_axis for y in half_axis}
overlap = base_nodes & half_nodes
union = base_nodes | half_nodes

assert len(base_nodes) == 16
assert len(half_nodes) == 16
assert overlap == {
    (Fraction(-1), Fraction(-1)),
    (Fraction(-1), Fraction(1)),
    (Fraction(1), Fraction(-1)),
    (Fraction(1), Fraction(1)),
}
assert len(overlap) == 4
assert len(union) == 28
assert len(base_nodes) + len(half_nodes) == 32

# Dimensionless mixed-derivative weights in units of 1/h^2.
def base_1d_weight(x):
    return c[int(x)]

def half_1d_weight(x):
    # HALF step = h/2. The physical derivative coefficient is c[k]/(h/2)
    # = 2*c[k]/h, with k = 2*x in BASE-h units.
    return 2 * c[int(2 * x)]

def wb(node):
    x, y = node
    return base_1d_weight(x) * base_1d_weight(y)

def wh(node):
    x, y = node
    return half_1d_weight(x) * half_1d_weight(y)

expected_overlap = {
    (Fraction(-1), Fraction(-1)): (Fraction(4, 9), Fraction(1, 36), Fraction(5, 12)),
    (Fraction(-1), Fraction(1)): (Fraction(-4, 9), Fraction(-1, 36), Fraction(-5, 12)),
    (Fraction(1), Fraction(-1)): (Fraction(-4, 9), Fraction(-1, 36), Fraction(-5, 12)),
    (Fraction(1), Fraction(1)): (Fraction(4, 9), Fraction(1, 36), Fraction(5, 12)),
}
for p, (b, h2, d) in expected_overlap.items():
    assert wb(p) == b
    assert wh(p) == h2
    assert wb(p) - wh(p) == d

base_l1 = sum(abs(wb(p)) for p in base_nodes)
half_l1 = sum(abs(wh(p)) for p in half_nodes)
# Aggregate D_BASE-D_HALF on the 28-point union before taking the L1 norm.
disc_weights = {}
for p in union:
    disc_weights[p] = (wb(p) if p in base_nodes else 0) - (wh(p) if p in half_nodes else 0)
disc_l1 = sum(abs(v) for v in disc_weights.values())

assert base_l1 == Fraction(9, 4)
assert half_l1 == Fraction(9, 1)
assert disc_l1 == Fraction(397, 36)
assert base_l1 + half_l1 == Fraction(45, 4)
assert (base_l1 + half_l1) - disc_l1 == Fraction(2, 9)

result = {
    "iteration": 508,
    "classification": "PASS_BASE_HALF_32_OCCURRENCES_28_DISTINCT_OVERLAP_WEIGHTS_EXACT__NON_PROMOTING",
    "base_source_occurrences": 16,
    "half_source_occurrences": 16,
    "total_source_occurrences": 32,
    "distinct_union_coordinates": 28,
    "exact_overlap_count": 4,
    "overlap_coordinates_in_BASE_H_units": [[str(x), str(y)] for x, y in sorted(overlap)],
    "overlap_weights_in_1_over_h2": {
        f"({x},{y})": {
            "BASE": str(wb((x, y))),
            "HALF": str(wh((x, y))),
            "BASE_minus_HALF": str(wb((x, y)) - wh((x, y))),
        }
        for x, y in sorted(overlap)
    },
    "l1_weight_norms_in_1_over_h2": {
        "BASE": str(base_l1),
        "HALF": str(half_l1),
        "BASE_plus_HALF_separate": str(base_l1 + half_l1),
        "BASE_minus_HALF_union_aggregated": str(disc_l1),
        "overlap_cancellation_reduction": str((base_l1 + half_l1) - disc_l1),
    },
    "scope": "exact frozen central4 coordinate/weight geometry only; local sample certificates may be shared at the four identical coordinates, but BASE and HALF derivative weights remain distinct",
    "promotion": False,
    "model_readiness_percent": 24,
}
print(json.dumps(result, indent=2, sort_keys=True))
