from fractions import Fraction

nodes = (-2, -1, 1, 2)
w = {-2: 1, -1: -8, 1: 8, 2: -1}

# Mixed central4 coefficient matrix C = w \otimes w.
C2 = {(u, v): (w[u] * w[v]) ** 2 for u in nodes for v in nodes}
norm2 = sum(C2.values())
assert norm2 == 16900

leverage = {k: Fraction(v, norm2) for k, v in C2.items()}
assert sum(leverage.values(), Fraction(0, 1)) == 1

central = [(u, v) for u in (-1, 1) for v in (-1, 1)]
edges = [(u, v) for u in nodes for v in nodes if ((abs(u) == 2) ^ (abs(v) == 2))]
corners = [(u, v) for u in (-2, 2) for v in (-2, 2)]

assert len(central) == 4
assert len(edges) == 8
assert len(corners) == 4

central_share = sum((leverage[p] for p in central), Fraction(0, 1))
edge_share = sum((leverage[p] for p in edges), Fraction(0, 1))
corner_share = sum((leverage[p] for p in corners), Fraction(0, 1))

assert central_share == Fraction(4096, 4225)
assert edge_share == Fraction(128, 4225)
assert corner_share == Fraction(1, 4225)
assert central_share + edge_share + corner_share == 1

# Each coordinate within a geometric class has identical iid-variance leverage.
assert {leverage[p] for p in central} == {Fraction(1024, 4225)}
assert {leverage[p] for p in edges} == {Fraction(16, 4225)}
assert {leverage[p] for p in corners} == {Fraction(1, 16900)}

# Final frozen rank11/rank12 pair are both edge-class coordinates.
rank11 = (2, -1)
rank12 = (2, 1)
assert leverage[rank11] == leverage[rank12] == Fraction(16, 4225)
assert leverage[rank11] + leverage[rank12] == Fraction(32, 4225)

print('PASS_ITER424_QUARTER_COORDINATE_VARIANCE_LEVERAGE_MAP_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING')
print('norm_C_squared=16900')
print('central4_share=', central_share)
print('edge8_share=', edge_share)
print('corner4_share=', corner_share)
print('each_central=', Fraction(1024, 4225))
print('each_edge=', Fraction(16, 4225))
print('each_corner=', Fraction(1, 16900))
print('rank11_rank12_pair_share=', Fraction(32, 4225))
