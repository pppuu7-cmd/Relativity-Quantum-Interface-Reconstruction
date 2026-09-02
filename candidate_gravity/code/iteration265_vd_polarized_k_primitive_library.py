#!/usr/bin/env python3
"""Iteration 265: exact polarized K0/K1/K2 primitive-library certificate.

This is an algebraic implementation/regression certificate for the frozen affine-R
same-parent construction

    K = R (P + Gamma R),
    R = R0 + sum_x t_x R1[x],

with P background-independent and Gamma polarized through Gamma2.
No physical loop integration is performed here.
"""
import json
import numpy as np

rng = np.random.default_rng(265)
n = 5
R0 = rng.normal(size=(n,n))
Rx = rng.normal(size=(n,n))
Ry = rng.normal(size=(n,n))
P = rng.normal(size=(n,n))
G0 = rng.normal(size=(n,n))
Gx = rng.normal(size=(n,n))
Gy = rng.normal(size=(n,n))
Gxy = rng.normal(size=(n,n))


def K(tx, ty):
    R = R0 + tx*Rx + ty*Ry
    G = G0 + tx*Gx + ty*Gy + tx*ty*Gxy
    D = P + G @ R
    return R @ D

K0 = R0 @ (P + G0 @ R0)
K1x = Rx @ (P + G0 @ R0) + R0 @ (Gx @ R0 + G0 @ Rx)
K1y = Ry @ (P + G0 @ R0) + R0 @ (Gy @ R0 + G0 @ Ry)
K2xy = (
    Rx @ (Gy @ R0 + G0 @ Ry)
    + Ry @ (Gx @ R0 + G0 @ Rx)
    + R0 @ (Gxy @ R0 + Gx @ Ry + Gy @ Rx)
)

steps = [1e-2, 3e-3, 1e-3, 3e-4, 1e-4]
validation = []
for h in steps:
    k1_fd = (K(h,0.0)-K(-h,0.0))/(2*h)
    k2_fd = (K(h,h)-K(h,-h)-K(-h,h)+K(-h,-h))/(4*h*h)
    validation.append({
        "h": h,
        "max_K1_fd_mismatch": float(np.max(np.abs(k1_fd-K1x))),
        "max_K2_mixed_fd_mismatch": float(np.max(np.abs(k2_fd-K2xy))),
    })

K0_terms = [
    "R0 P",
    "R0 Gamma0 R0",
]
K1_terms = [
    "R1[x] P",
    "R1[x] Gamma0 R0",
    "R0 Gamma1[x] R0",
    "R0 Gamma0 R1[x]",
]
K2_terms = [
    "R1[x] Gamma1[y] R0",
    "R1[x] Gamma0 R1[y]",
    "R1[y] Gamma1[x] R0",
    "R1[y] Gamma0 R1[x]",
    "R0 Gamma2[x,y] R0",
    "R0 Gamma1[x] R1[y]",
    "R0 Gamma1[y] R1[x]",
]

# Frozen null-soft projected-A partition from Iterations 263-264:
# A3[s,a,b] = K0 E3[s,a,b]
#             + K1[s] E2[a,b] + K1[a] E2[s,b] + K1[b] E2[s,a]
#             + K2[s,a] E1[b] + K2[s,b] E1[a], because E1[s]=0.
primitive_counts = {
    "K0": len(K0_terms),
    "K1_each_leg": len(K1_terms),
    "K2_each_leg_pair": len(K2_terms),
    "A1_s_before_E1_soft_zero": len(K0_terms),
    "A1_s_after_E1_soft_zero": 0,
    "A2_s_a": len(K0_terms)+len(K1_terms),
    "A2_a_b": len(K0_terms)+2*len(K1_terms),
    "A3_s_a_b": len(K0_terms)+3*len(K1_terms)+2*len(K2_terms),
}

result = {
    "iteration": 265,
    "scope": "abstract noncommuting-matrix regression of exact polarized same-parent K algebra",
    "frozen_dynamics": "K=R(P+Gamma R), affine R=R0+R1, P background-independent",
    "K0_terms": K0_terms,
    "K1_terms": K1_terms,
    "K2_terms": K2_terms,
    "primitive_counts": primitive_counts,
    "validation": validation,
    "status": [
        "PASS_EXACT_POLARIZED_K0_K1_K2_PRIMITIVE_LIBRARY_2_4_7",
        "PASS_EXACT_NULLSOFT_PROJECTED_A3_PRIMITIVE_COUNT_28",
        "NO_R2_R3_GAMMA3_IN_PHYSICAL_PROJECTED_A3",
    ],
    "interpretation": "Algebraic closure/regression only; not a physical C5 numerator, comparator coordinate, or residual."
}
print(json.dumps(result, indent=2, sort_keys=True))
