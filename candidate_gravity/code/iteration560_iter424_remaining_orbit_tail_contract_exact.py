from fractions import Fraction

# Frozen central4 scaled nodes and integer weights.
nodes = (-2, -1, 1, 2)
w = {-2: 1, -1: -8, 1: 8, 2: -1}

# After a raw-valid rank9 PASS, the only incomplete exchange orbits are
# ranks6/11: (-1,+2)<->(+2,-1), and
# ranks10/12: (+1,+2)<->(+2,+1).
A = ((-1, 2), (2, -1))
B = ((1, 2), (2, 1))

coeff_A = [w[u] * w[v] for u, v in A]
coeff_B = [w[u] * w[v] for u, v in B]
assert coeff_A == [8, 8]
assert coeff_B == [-8, -8]
assert sum(coeff_A) == 16
assert sum(coeff_B) == -16
assert sum(coeff_A) + sum(coeff_B) == 0

# Let EA and EB denote exchange-orbit averages.
# Tail numerator = 16*(EA-EB); full central4 normalization is 1/(144 h^2).
normalized_orbit_average_factor = Fraction(16, 144)
assert normalized_orbit_average_factor == Fraction(1, 9)

# With per-coordinate absolute errors eps_i, the sharp L1 error factor is
# (8/144)/h^2 = 1/(18 h^2) multiplying the sum of the four eps_i.
per_coordinate_error_factor = Fraction(8, 144)
assert per_coordinate_error_factor == Fraction(1, 18)

# With orbit-average error bounds eps_A and eps_B, the sharp bound factor is
# 1/(9 h^2) * (eps_A + eps_B).
orbit_average_error_factor = Fraction(1, 9)

print("PASS_ITER424_REMAINING_ORBIT_TAIL_FAIL_CLOSED_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING")
print("orbit_A_integer_sum=+16")
print("orbit_B_integer_sum=-16")
print("remaining_integer_sum=0")
print("tail=(EA-EB)/(9*h^2)")
print("per_coordinate_error_bound=(eps1+eps2+eps3+eps4)/(18*h^2)")
print("orbit_average_error_bound=(eps_A+eps_B)/(9*h^2)")
