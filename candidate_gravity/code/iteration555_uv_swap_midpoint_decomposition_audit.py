#!/usr/bin/env python3
"""Iteration 555: exact u<->v midpoint/antisymmetric routing decomposition.

Diagnostic/provenance only. No Candidate-Gravity promotion is implied.
"""
from sympy import symbols, simplify, sqrt

s, m, d = symbols('s m d', nonzero=True)
u = m - d
v = m + d

alpha_uv = -(s + u - v)/(2*s)
alpha_vu = -(s + v - u)/(2*s)
lambda_uv = s**2 + u**2 + v**2 - 2*s*u - 2*s*v - 2*u*v

assert simplify(alpha_uv - (-1/2 + d/s)) == 0
assert simplify(alpha_vu - (-1/2 - d/s)) == 0
assert simplify((alpha_uv + alpha_vu)/2 + 1/2) == 0
assert simplify(alpha_uv - alpha_vu - 2*d/s) == 0
assert simplify(lambda_uv - (s**2 - 4*s*m + 4*d**2)) == 0

rho = sqrt(lambda_uv)/(2*sqrt(s))
rho_mid = sqrt(s**2 - 4*s*m + 4*d**2)/(2*sqrt(s))
assert simplify(rho-rho_mid) == 0

print('alpha_uv = -1/2 + d/s')
print('alpha_vu = -1/2 - d/s')
print('alpha_mid = -1/2')
print('lambda = s^2 - 4*s*m + 4*d^2 (even in d)')
print('p_uv = p_mid + (d/s) q')
print('p_vu = p_mid - (d/s) q')
print('p_mid = -a - q/2 + rho(m,d^2) n')
print('classification = PASS_ITER424_UV_SWAP_MIDPOINT_ANTISYMMETRIC_DECOMPOSITION_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING')
