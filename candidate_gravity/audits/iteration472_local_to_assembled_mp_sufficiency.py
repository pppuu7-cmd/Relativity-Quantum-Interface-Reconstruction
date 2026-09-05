from fractions import Fraction

# Exact local-to-assembled precision implication audit.
# For a linear assembled operator D=sum_i w_i F_i, define
# delta_i=F80_i-F120_i, s_i=max(1,|F80_i|,|F120_i|), e_i=|delta_i|/s_i.
# If e_i<=eps_local for all i, then
# |DeltaD| <= eps_local * E, E=sum_i |w_i| s_i.

M = 10**30
eps_local = Fraction(1, M)
tau_assembled = Fraction(2, 10**6)

# Two actual equal-and-opposite sample weights occur inside one central4 parity quartet.
w = Fraction(4, 9)
weights = [w, -w]
F120 = [Fraction(M), Fraction(M)]
F80 = [Fraction(M + 1), Fraction(M - 1)]

scales = [max(Fraction(1), abs(a), abs(b)) for a, b in zip(F80, F120)]
local_errors = [abs(a-b)/s for a, b, s in zip(F80, F120, scales)]
assert all(e <= eps_local for e in local_errors)

D80 = sum(wi*fi for wi, fi in zip(weights, F80))
D120 = sum(wi*fi for wi, fi in zip(weights, F120))
DeltaD = D80 - D120
assembled_scale = max(Fraction(1), abs(D80), abs(D120))
assembled_error = abs(DeltaD) / assembled_scale

E = sum(abs(wi)*si for wi, si in zip(weights, scales))
B_actual = sum(abs(wi)*abs(a-b) for wi, a, b in zip(weights, F80, F120))

assert abs(DeltaD) <= B_actual <= eps_local * E
assert assembled_error > tau_assembled

print('max_local_error =', max(local_errors))
print('eps_local =', eps_local)
print('D80 =', D80, 'D120 =', D120)
print('assembled_error =', assembled_error)
print('tau_assembled =', tau_assembled)
print('E =', E)
print('B_actual =', B_actual)
print('PASS: local sample threshold alone does not imply assembled threshold')
print('PASS: |DeltaD| <= B_actual <= eps_local * E')
