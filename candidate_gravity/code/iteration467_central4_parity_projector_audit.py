#!/usr/bin/env python3
"""Iteration 467: exact parity-projector audit for frozen central4 x central4.

No floating-point arithmetic is needed.  The audit proves that the tensor mixed
operator sees only the odd-in-u, odd-in-v sector and derives an exact quartet
representation that can later cross-check the canonical 16-term assembly.
"""
from fractions import Fraction
import json

nodes = (-2, -1, 1, 2)
c = {
    -2: Fraction(1, 12),
    -1: Fraction(-2, 3),
     1: Fraction(2, 3),
     2: Fraction(-1, 12),
}

# Exact antisymmetry of the one-dimensional derivative weights.
assert all(c[-x] == -c[x] for x in (1, 2))

# Tensor sign symmetries.
w = {(u, v): c[u] * c[v] for u in nodes for v in nodes}
assert all(w[(-u, v)] == -w[(u, v)] for u in nodes for v in nodes)
assert all(w[(u, -v)] == -w[(u, v)] for u in nodes for v in nodes)
assert all(w[(-u, -v)] == w[(u, v)] for u in nodes for v in nodes)

# Symbolic coefficient audit for parity sectors.  Represent a generic value at
# (+/- a,+/- b) by parity signs su,sv.  The weighted quartet coefficient for a
# sector with parities pu,pv in {+1 even,-1 odd} is evaluated exactly.
def quartet_sector_factor(pu: int, pv: int) -> Fraction:
    # F(-u,+v)=pu F(+u,+v), F(+u,-v)=pv F(+u,+v),
    # F(-u,-v)=pu*pv F(+u,+v).
    return Fraction(1) - pu - pv + pu * pv

sectors = {
    "even_even": quartet_sector_factor(+1, +1),
    "even_odd": quartet_sector_factor(+1, -1),
    "odd_even": quartet_sector_factor(-1, +1),
    "odd_odd": quartet_sector_factor(-1, -1),
}
assert sectors == {
    "even_even": Fraction(0),
    "even_odd": Fraction(0),
    "odd_even": Fraction(0),
    "odd_odd": Fraction(4),
}

# Positive-node quartet coefficients.  The dimensionful operator is 1/h^2
# times these dimensionless coefficients multiplying the signed quartet
# F(+a,+b)-F(-a,+b)-F(+a,-b)+F(-a,-b).
quartet_coefficients = {
    (a, b): c[a] * c[b]
    for a in (1, 2)
    for b in (1, 2)
}

# Verify exact equivalence of canonical 16 weights and quartet expansion by
# reconstructing every source coefficient.
reconstructed = {}
for a in (1, 2):
    for b in (1, 2):
        q = quartet_coefficients[(a, b)]
        reconstructed[( a,  b)] = q
        reconstructed[(-a,  b)] = -q
        reconstructed[( a, -b)] = -q
        reconstructed[(-a, -b)] = q
assert reconstructed == w

out = {
    "iteration": 467,
    "classification": "PASS_CENTRAL4_EXACT_ODD_ODD_PARITY_PROJECTOR__NON_PROMOTING",
    "nodes": list(nodes),
    "coefficients": {str(k): str(v) for k, v in c.items()},
    "one_dimensional_antisymmetry": True,
    "tensor_sign_symmetries": {
        "w(-u,v)=-w(u,v)": True,
        "w(u,-v)=-w(u,v)": True,
        "w(-u,-v)=w(u,v)": True,
    },
    "parity_sector_factors": {k: str(v) for k, v in sectors.items()},
    "surviving_sector": "odd_odd_only",
    "quartet_coefficients_positive_nodes": {
        f"({a},{b})": str(q) for (a, b), q in quartet_coefficients.items()
    },
    "canonical_16_term_equals_4_quartet_form_exactly": True,
    "scope": "exact algebra / implementation-provenance diagnostic only",
    "physics_promotion": False,
    "model_readiness_percent": 24,
}
print(json.dumps(out, indent=2, sort_keys=True))
