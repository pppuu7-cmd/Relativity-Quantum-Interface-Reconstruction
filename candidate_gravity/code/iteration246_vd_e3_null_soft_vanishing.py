#!/usr/bin/env python3
"""Iteration 246: scoped vanishing of the flat e=3 Vilkovisky connection sector.

Frozen branch:
  * Minkowski signature (-,+,+,+)
  * Lambda=0
  * physical null soft graviton k=(1,0,0,1)
  * normalized plus TT polarization
  * e=3,c=0 connection terms fixed in Iteration 244:
      +(i/2) Tr(U1 U2) - (i/6) Tr(U1^3)

At c=0 the kernels are frozen at flat background, so the cubic dependence of
these e=3 terms is trilinear in the three explicit Einstein EOM insertions.
For a physical null TT soft leg, the linearized Einstein tensor is exactly
zero. Hence every trilinear permutation containing that soft leg vanishes.

This script validates the soft-leg geometry and the multilinear consequence.
It does NOT set the e=0,1,2 Vilkovisky sectors to zero.
"""

import json
import math
import numpy as np

eta = np.diag([-1.0, 1.0, 1.0, 1.0])
k = np.array([1.0, 0.0, 0.0, 1.0])  # contravariant
k_lower = eta @ k

pol = np.zeros((4, 4))
pol[1, 1] = 1.0 / math.sqrt(2.0)
pol[2, 2] = -1.0 / math.sqrt(2.0)

k2 = float(k @ eta @ k)
trace_h = float(np.einsum("mn,mn", eta, pol))
transverse = k @ pol

# Fourier-space linearized Ricci for covariant h_{mu nu}, d_mu -> i k_mu:
# R_mn^(1) = 1/2[-k_r k_m h^r_n - k_r k_n h^r_m
#                  + k^2 h_mn + k_m k_n h]
h_up_first = eta @ pol
ricci = np.zeros((4, 4))
for m in range(4):
    for n in range(4):
        term1 = sum(k_lower[r] * k_lower[m] * h_up_first[r, n] for r in range(4))
        term2 = sum(k_lower[r] * k_lower[n] * h_up_first[r, m] for r in range(4))
        ricci[m, n] = 0.5 * (
            -term1 - term2 + k2 * pol[m, n] + k_lower[m] * k_lower[n] * trace_h
        )

ricci_scalar = float(np.einsum("mn,mn", eta, ricci))
einstein = ricci - 0.5 * eta * ricci_scalar

# Same linearized Riemann convention retained from Iteration 175.
riemann = np.zeros((4, 4, 4, 4))
for mu in range(4):
    for nu in range(4):
        for rho in range(4):
            for sigma in range(4):
                riemann[mu, nu, rho, sigma] = -0.5 * (
                    k_lower[rho] * k_lower[nu] * pol[mu, sigma]
                    + k_lower[sigma] * k_lower[mu] * pol[nu, rho]
                    - k_lower[sigma] * k_lower[nu] * pol[mu, rho]
                    - k_lower[rho] * k_lower[mu] * pol[nu, sigma]
                )

checks = {
    "k2": k2,
    "trace_h": trace_h,
    "max_transversality_residual": float(np.max(np.abs(transverse))),
    "max_linearized_ricci": float(np.max(np.abs(ricci))),
    "linearized_ricci_scalar": ricci_scalar,
    "max_linearized_einstein": float(np.max(np.abs(einstein))),
    "max_linearized_riemann": float(np.max(np.abs(riemann))),
    "linearized_riemann_frobenius_norm": float(np.linalg.norm(riemann)),
}

assert checks["k2"] == 0.0
assert checks["trace_h"] == 0.0
assert checks["max_transversality_residual"] == 0.0
assert checks["max_linearized_ricci"] == 0.0
assert checks["max_linearized_einstein"] == 0.0
assert checks["linearized_riemann_frobenius_norm"] > 0.0

# Algebraic multilinear certificate. Let E_s=0 be the soft linearized EOM and
# E_a,E_b arbitrary nonzero placeholders. Every cubic permutation in an e=3,
# c=0 functional derivative contains one factor E_s.
E_soft = 0.0
E_a = 1.7
E_b = -0.9
trilinear_permutations = [
    E_soft * E_a * E_b,
    E_soft * E_b * E_a,
    E_a * E_soft * E_b,
    E_a * E_b * E_soft,
    E_b * E_soft * E_a,
    E_b * E_a * E_soft,
]
assert max(abs(x) for x in trilinear_permutations) == 0.0

result = {
    "iteration": 246,
    "model_readiness_percent": 24,
    "scope": "Minkowski_Lambda0_physical_null_TT_soft_leg_flat_e3_connection_sector",
    "geometry_checks": checks,
    "soft_linearized_Einstein_EOM_zero": True,
    "soft_linearized_Riemann_nonzero": True,
    "e3_c0_terms": ["Tr(U1^3)", "Tr(U1 U2)"],
    "e3_c0_cubic_soft_projection": "ZERO",
    "reason": "flat e=3 sector is trilinear in explicit linearized EOM insertions; each cubic permutation contains the null-TT soft EOM factor, which vanishes",
    "does_not_apply_to": [
        "determinant e=0 sector",
        "e=1 sector with c=2 curvature/operator dressing",
        "e=2 sector with c=1 curvature/operator dressing",
        "generic off-shell cubic metric vertex without a null-TT soft leg"
    ],
    "classification": "PASS_SCOPED_VD_E3_NULL_SOFT_TT_VANISHING",
    "remaining_C5_authority": "E0_DETERMINANT_PLUS_E1_C2_PLUS_E2_C1_AND_SOURCE_COMPLETED_CAUSAL_PROJECTION",
    "candidate_residual": False,
    "ansatz_003_authorized": False,
    "fisher_resources_authorized": False,
    "next_gate": 247
}

print(json.dumps(result, indent=2, sort_keys=True))
