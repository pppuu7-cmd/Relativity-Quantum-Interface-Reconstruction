from fractions import Fraction
from math import sqrt

# Frozen three-level estimator from Iteration 536:
# R3 = (BASE - 80 HALF + 1024 QUARTER)/945.
w = [Fraction(1,945), Fraction(-80,945), Fraction(1024,945)]

l1 = sum(abs(x) for x in w)
l2_sq = sum(x*x for x in w)
linf = max(abs(x) for x in w)

# For X_h = D + a h^4 + b h^6 + c h^8 + e h^10 + ...,
# BASE uses h, HALF h/2, QUARTER h/4.
def leakage(power):
    return (Fraction(1,1) - 80*Fraction(1,2**power) + 1024*Fraction(1,4**power))/945

assert leakage(4) == 0
assert leakage(6) == 0
assert leakage(8) == Fraction(1,1344)
assert leakage(10) == Fraction(1,1024)
assert l1 == Fraction(221,189)
assert l2_sq == Fraction(50237,42525)
assert linf == Fraction(1024,945)

print('weights=', [str(x) for x in w])
print('L1=', l1, float(l1))
print('L2^2=', l2_sq, 'L2=', sqrt(float(l2_sq)))
print('Linf=', linf, float(linf))
print('h4_leak=', leakage(4))
print('h6_leak=', leakage(6))
print('h8_leak=', leakage(8))
print('h10_leak=', leakage(10))
