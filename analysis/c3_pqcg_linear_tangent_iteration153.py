#!/usr/bin/env python3
"""Iteration 153: first fixed finite C3-PQCG linear stochastic tangent.

This is deliberately a scoped linearized pure-gravity stochastic block of a
covariant classical-quantum gravity comparator, not a full nonlinear C3 model.
Unsupported post-Gaussian rows are reported BLOCKED and are never zero-filled.
"""
import json
import math
import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])
TAU = 0.8
LWIN = 0.6

QS = [
    np.array([0.18, 0.70, 0.20, 0.10]),
    np.array([0.14, 0.55,-0.25, 0.20]),
    np.array([0.22, 0.62, 0.18,-0.24]),
    np.array([0.16, 0.48, 0.31, 0.12]),
    np.array([0.20, 0.58,-0.16,-0.28]),
    np.array([0.12, 0.44, 0.27,-0.19]),
]
RS = [
    np.array([0.11,-0.21, 0.52, 0.17]),
    np.array([0.09, 0.24, 0.46,-0.18]),
    np.array([0.10,-0.18, 0.41, 0.29]),
    np.array([0.13, 0.22,-0.37, 0.33]),
    np.array([0.08, 0.26, 0.35, 0.21]),
    np.array([0.15,-0.20, 0.39, 0.25]),
]

def dot(k):
    return float(k @ ETA @ k)

def window(k):
    omega = float(k[0])
    kspace = float(np.linalg.norm(k[1:]))
    return math.exp(-0.5*((TAU*omega)**2 + (LWIN*kspace)**2))

# Frozen linear stochastic mode convention:
# box h_s = J_s + xi_s, <xi_s xi_s'> = 2 D_s delta_ss' delta^4,
# s in {2,0}.  On the frozen spacelike probes G_R=1/k^2 is real.
# The scalar N2 protocol coordinate traces the transverse symmetric tensor
# noise. Barnes-Rivers projector ranks in D=4 give Tr(P2)=5, Tr(P0)=1.
ks = []
for q, r in zip(QS, RS):
    ks.extend([q, r, q+r])

terms = []
for k in ks:
    k2 = dot(k)
    if k2 <= 0.0:
        raise RuntimeError("Iteration-153 protocol expects spacelike probes")
    w = window(k)
    terms.append(2.0*w*w/(k2*k2))

A = float(sum(terms))
# Supported row order: (N2, chi1R); parameter order: (D2, D0).
# chi1R=G_R is nonzero but independent of D2,D0 in this frozen parameterization.
V = np.array([[5.0*A, A], [0.0, 0.0]], dtype=float)
s = np.linalg.svd(V, compute_uv=False)
rank = int(np.linalg.matrix_rank(V, tol=1e-12))

out = {
    "iteration": 153,
    "comparator_id": "C3-PQCG-LIN-001",
    "scope": "linearized covariant postquantum-classical stochastic pure-gravity block",
    "parameter_order": ["D2", "D0"],
    "supported_rows": ["N2", "chi1R"],
    "blocked_rows": ["C3sym", "chi2R_even", "chi2R_odd", "soft2", "tensor_geo", "threshold"],
    "probe_count": len(ks),
    "probe_k2_min": min(dot(k) for k in ks),
    "probe_k2_max": max(dot(k) for k in ks),
    "A": A,
    "V_supported": V.tolist(),
    "rank_supported": rank,
    "singular_values": s.tolist(),
    "interpretation": {
        "D2_D0_identifiability": "REGIME_SPECIFIC_NON_IDENTIFIABILITY: one scalar N2 coordinate spans only one combination 5 D2 + D0",
        "full_C3_tangent": "BLOCKED_NONLINEAR_COMPLETION",
        "fisher_resources": "FORBIDDEN",
    },
}
print(json.dumps(out, indent=2, sort_keys=True))
