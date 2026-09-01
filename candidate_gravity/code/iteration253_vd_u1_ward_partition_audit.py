#!/usr/bin/env python3
"""Iteration 253: algebraic audit of the cubic Ward partition for U1.

This script is intentionally a bookkeeping certificate, not a tensor integral.
It verifies which background-order partitions contribute to K[E] at total
order three when K = R.(D R) is expanded as K0+t K1+t^2 K2+... and the
Einstein EOM as E=t E1+t^2 E2+t^3 E3+....
"""
import sympy as sp
import json


t = sp.symbols('t')
K0, K1, K2 = sp.symbols('K0 K1 K2', commutative=False)
E1, E2, E3 = sp.symbols('E1 E2 E3', commutative=False)

K = K0 + t*K1 + t**2*K2
E = t*E1 + t**2*E2 + t**3*E3
expr = sp.expand(K*E)
coeff3 = sp.expand(expr).coeff(t, 3)
expected = K0*E3 + K1*E2 + K2*E1

result = {
    "total_order_3": str(coeff3),
    "expected": str(expected),
    "partition_match": bool(sp.expand(coeff3 - expected) == 0),
    "partitions": ["K0*E3", "K1*E2", "K2*E1"],
    "ward_identity": "R_gamma^i (D_i R_delta^j) E_j = -R_gamma^i R_delta^j (D_i E_j)",
    "scientific_guardrail": (
        "Symmetry/Ward consistency applies to the complete order-3 sum. "
        "K1*E2 alone is not licensed as a standalone Ward-pass object unless "
        "an independent same-parent identity proves the other partitions separately symmetric."
    )
}

print(json.dumps(result, indent=2))
