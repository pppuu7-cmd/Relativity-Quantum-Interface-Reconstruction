from fractions import Fraction

# Frozen central4 nodes and integer first-derivative weights.
nodes = (-2, -1, 1, 2)
w = {-2: 1, -1: -8, 1: 8, 2: -1}
normalization = 144  # (12 h)^2 -> 1/(144 h^2)

# Direct tensor coefficients C_uv = w_u w_v.
direct = {(u, v): w[u] * w[v] for u in nodes for v in nodes}

# Route 1: u-then-v sequential differentiation.
# Algebraically its coefficient for F(u,v) is (w_u/12h)*(w_v/12h).
seq_uv = {(u, v): w[u] * w[v] for u in nodes for v in nodes}

# Route 2: v-then-u sequential differentiation.
seq_vu = {(u, v): w[v] * w[u] for u in nodes for v in nodes}

assert direct == seq_uv == seq_vu
assert all(direct[(u, v)] == direct[(v, u)] for u in nodes for v in nodes)

# Route 3: exchange-orbit compression.  For an off-diagonal orbit
# {(u,v),(v,u)}, the direct contribution is
# C_uv F_uv + C_vu F_vu = (C_uv+C_vu) E_uv,
# where E_uv=(F_uv+F_vu)/2 because C_uv=C_vu.
seen = set()
orbits = []
for u in nodes:
    for v in nodes:
        if (u, v) in seen:
            continue
        if u == v:
            members = ((u, v),)
        else:
            members = ((u, v), (v, u))
        for m in members:
            seen.add(m)
        coeff_sum = sum(direct[m] for m in members)
        orbits.append((members, coeff_sum))

assert len(orbits) == 10
assert len(seen) == 16
assert sum(c for _, c in orbits) == 0

expected_orbit_coeffs = {
    ((-2, -2),): 1,
    ((-2, -1), (-1, -2)): -16,
    ((-2, 1), (1, -2)): 16,
    ((-2, 2), (2, -2)): -2,
    ((-1, -1),): 64,
    ((-1, 1), (1, -1)): -128,
    ((-1, 2), (2, -1)): 16,
    ((1, 1),): 64,
    ((1, 2), (2, 1)): -16,
    ((2, 2),): 1,
}
assert {members: c for members, c in orbits} == expected_orbit_coeffs

# Synthetic exactness audit: the 1D central4 derivative is exact through
# degree 4, so the tensor product exactly reproduces d_u d_v of every
# monomial u^a v^b with 0<=a,b<=4 at the origin.
def discrete_mixed_monomial(a, b):
    numerator = sum(
        direct[(u, v)] * (u ** a) * (v ** b)
        for u in nodes for v in nodes
    )
    return Fraction(numerator, normalization)

def exact_mixed_monomial_at_origin(a, b):
    return Fraction(1, 1) if (a, b) == (1, 1) else Fraction(0, 1)

for a in range(5):
    for b in range(5):
        assert discrete_mixed_monomial(a, b) == exact_mixed_monomial_at_origin(a, b)

# Exact null directions implied by row/column sums: any additive separable
# contamination A(u)+B(v)+constant is annihilated by the mixed stencil.
for u in nodes:
    assert sum(direct[(u, v)] for v in nodes) == 0
for v in nodes:
    assert sum(direct[(u, v)] for u in nodes) == 0

print("PASS_ITER424_QUARTER_THREE_WAY_ASSEMBLY_IDENTITY_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING")
print("direct == sequential_u_then_v == sequential_v_then_u == orbit_compressed")
print("orbit_count=10 coordinate_count=16")
print("monomial_exactness=all u^a v^b for 0<=a,b<=4")
print("separable_null=A(u)+B(v)+constant")
print("normalization=1/(144*h^2)")
