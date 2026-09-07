from fractions import Fraction

# Frozen three-level truncation diagnostics from Iterations 536/540.
# d1 = BASE-HALF, d2 = HALF-QUARTER.
# A = a h^4, B = b h^6.
K = Fraction(80, 21)

# Exact inversion identities:
# A = 16(64 d2-d1)/45
# B = 256(d1-16 d2)/189
# q := B/A = K (d1-16 d2)/(64 d2-d1).
assert Fraction(256, 189) / Fraction(16, 45) == K

# If r=d1/d2, q = K (r-16)/(64-r).
# Exact derivative dq/dr = 1280/[7(64-r)^2].
assert K * 48 == Fraction(1280, 7)

# First-order partials in (d1,d2), with D=64d2-d1:
# dq/dd1 = (1280/7) d2/D^2
# dq/dd2 = -(1280/7) d1/D^2.
# Relative condition of q with respect to r:
# kappa_rel(r)=|48 r/((r-16)(64-r))|.

# Exact finite-error fail-closed guard. For |e1|<=eps1, |e2|<=eps2,
# D'=D+64e2-e1. If m=|D|-(eps1+64eps2)>0, the quotient is guaranteed
# not to cross its A=0 pole and
# |q'-q| <= K[(eps1+16eps2)|D| + |N|(eps1+64eps2)]/(|D| m),
# N=d1-16d2.

# Structural identities: D=0 iff reconstructed A=0; N=0 iff reconstructed B=0.

print('q_factor=', K)
print('dq_dr_prefactor=', Fraction(1280, 7))
print('q=(80/21)*(d1-16*d2)/(64*d2-d1)')
print('relative_condition=abs(48*r/((r-16)*(64-r)))')
print('pole_guard=abs(64*d2-d1) > eps1+64*eps2')
print('A_zero_surface: d1=64*d2')
print('B_zero_surface: d1=16*d2')
