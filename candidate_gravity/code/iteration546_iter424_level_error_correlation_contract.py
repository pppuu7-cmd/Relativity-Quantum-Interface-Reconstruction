from fractions import Fraction
import math

# Frozen three-level differences and ratio-free combinations:
# d1 = BASE - HALF, d2 = HALF - QUARTER
# P = 64*d2 - d1, Q = d1 - 16*d2
# Let level errors be eB,eH,eQ. Then
# deltaP = -eB + 65 eH - 64 eQ
# deltaQ =  eB - 17 eH + 16 eQ

p = (-1, 65, -64)
q = (1, -17, 16)

var_p = sum(x*x for x in p)
var_q = sum(x*x for x in q)
cov_pq = sum(a*b for a,b in zip(p,q))
det = var_p*var_q - cov_pq*cov_pq
rho = cov_pq / math.sqrt(var_p*var_q)
trace = var_p + var_q
disc = trace*trace - 4*det
lam_hi = (trace + math.sqrt(disc))/2
lam_lo = (trace - math.sqrt(disc))/2
cond_cov = lam_hi/lam_lo
cond_std = math.sqrt(cond_cov)

assert p == (-1,65,-64)
assert q == (1,-17,16)
assert var_p == 8322
assert var_q == 546
assert cov_pq == -2130
assert det == 6912
assert det > 0

print('deltaP coefficients [eB,eH,eQ] =', p)
print('deltaQ coefficients [eB,eH,eQ] =', q)
print('equal-variance covariance/sigma^2 = [[8322,-2130],[-2130,546]]')
print('det(cov/sigma^2) =', det)
print('corr(P,Q) =', repr(rho))
print('covariance condition number =', repr(cond_cov))
print('std-map condition number =', repr(cond_std))
print('bounded-error radii: rhoP = epsB + 65 epsH + 64 epsQ; rhoQ = epsB + 17 epsH + 16 epsQ')
