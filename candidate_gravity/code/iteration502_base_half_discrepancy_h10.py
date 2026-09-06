from fractions import Fraction
from math import factorial

xs = [-2, -1, 1, 2]
cs = [Fraction(1,12), Fraction(-2,3), Fraction(2,3), Fraction(-1,12)]

moments = {n: sum(c * (x ** n) for c, x in zip(cs, xs)) for n in range(14)}
assert moments[1] == 1
for n in [0,2,3,4,6,8,10,12]:
    assert moments[n] == 0

one_d = {n: moments[n] / factorial(n) for n in [5,7,9,11,13]}
assert one_d[5] == Fraction(-1,30)
assert one_d[7] == Fraction(-1,252)
assert one_d[9] == Fraction(-1,4320)
assert one_d[11] == Fraction(-17,1995840)

# At total h^10 in D_h=L_h^x L_h^y:
# pure sector from h^10 x derivative-order 11 on one axis,
# cross sector from h^4*h^6.
pure_h10 = one_d[11]
cross_h10 = one_d[5] * one_d[7]
assert cross_h10 == Fraction(1,7560)

base_minus_half_factor_h10 = Fraction(1,1) - Fraction(1,2**10)
pure_discrepancy = pure_h10 * base_minus_half_factor_h10
cross_discrepancy = cross_h10 * base_minus_half_factor_h10

assert pure_discrepancy == Fraction(-527,61931520)
assert cross_discrepancy == Fraction(341,2580480)

print('M11 =', moments[11])
print('1D h^10 coefficient =', one_d[11])
print('mixed h^10 pure coefficient =', pure_h10)
print('mixed h^10 cross coefficient =', cross_h10)
print('BASE-HALF h^10 pure coefficient =', pure_discrepancy)
print('BASE-HALF h^10 cross coefficient =', cross_discrepancy)
