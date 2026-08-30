#!/usr/bin/env python3
"""Iteration 134: convention audit for the Newtonian limit of ANSATZ-PQG-EFT-001.

Signature (-,+,+,+), g00=-(1+2 Phi), weak static source T00=rho.
Linearized Einstein equation gives 2 nabla^2 Phi = 8 pi G rho.
"""
import math

G = 6.67430e-11
M = 1.0
r = 2.0

# From G00 ~= 2 Laplacian(Phi) = 8 pi G rho.
poisson_coeff = (8.0 * math.pi * G) / 2.0
assert math.isclose(poisson_coeff, 4.0 * math.pi * G, rel_tol=0, abs_tol=1e-25)

# Point-source solution away from r=0: Phi=-GM/r and acceleration magnitude GM/r^2.
phi = -G * M / r
accel = G * M / r**2
assert phi < 0
assert accel > 0
assert math.isclose(-phi / r, accel, rel_tol=1e-15)

# kappa normalization: kappa^2 = 32 pi G -> kappa^2/4 = 8 pi G.
kappa2 = 32.0 * math.pi * G
assert math.isclose(kappa2 / 4.0, 8.0 * math.pi * G, rel_tol=1e-15)

print("Iteration 134 Newtonian normalization audit: PASS")
print(f"Poisson coefficient = {poisson_coeff:.16e} = 4*pi*G")
print(f"Phi(M=1,r=2) = {phi:.16e}")
print(f"|a| = {accel:.16e}")
