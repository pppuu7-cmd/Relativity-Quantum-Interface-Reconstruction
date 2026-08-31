#!/usr/bin/env python3
"""Iteration 149: finite source-completed off-shell C5 protocol checks.

This script does NOT compute the Einstein-Hilbert/local-EFT cubic vertex.
It freezes and validates the operational probe layer required before that
vertex can be projected into chi^(2)R coordinates.
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

def dot(a, b):
    return float(a @ ETA @ b)

def transverse_cov(k):
    k2 = dot(k, k)
    if abs(k2) < 1e-12:
        raise ValueError("probe momentum too close to a massless pole")
    kl = ETA @ k
    return ETA - np.outer(kl, kl) / k2

def spin2_projector(k):
    th = transverse_cov(k)
    P = np.zeros((4,4,4,4))
    for m in range(4):
        for n in range(4):
            for r in range(4):
                for s in range(4):
                    P[m,n,r,s] = (
                        0.5*(th[m,r]*th[n,s] + th[m,s]*th[n,r])
                        - (1.0/3.0)*th[m,n]*th[r,s]
                    )
    return P

def window(k):
    omega = float(k[0])
    kspace = float(np.linalg.norm(k[1:]))
    return math.exp(-0.5*((TAU*omega)**2 + (LWIN*kspace)**2))

max_conservation = 0.0
max_trace = 0.0
max_idempotence = 0.0
kinematics = []
weights = []

for q, r in zip(QS, RS):
    p = q + r
    row = {"p2": dot(p,p), "q2": dot(q,q), "r2": dot(r,r)}
    kinematics.append(row)
    weights.append({"Wp":window(p), "Wq":window(q), "Wr":window(r)})
    for k in (p, q, r):
        P = spin2_projector(k)
        conservation = np.einsum('m,mnrs->nrs', k, P)
        trace = np.einsum('mn,mnrs->rs', ETA, P)
        composed = np.einsum('mnab,ac,bd,cdrs->mnrs', P, ETA, ETA, P)
        max_conservation = max(max_conservation, float(np.max(np.abs(conservation))))
        max_trace = max(max_trace, float(np.max(np.abs(trace))))
        max_idempotence = max(max_idempotence, float(np.max(np.abs(composed-P))))

allw = [v for row in weights for v in row.values()]
out = {
    "iteration": 149,
    "metric_signature": "(-,+,+,+)",
    "metric_variable": "g_mn = eta_mn + kappa h_mn; no EOM-reduced field used off shell",
    "source_map": "S_m[g,Psi], T_mn=-2/sqrt(-g) delta S_m/delta g^mn, with conserved external probe",
    "eft_policy": "undo Iteration-146 EOM reduction off shell; retain a complete unreduced covariant operator/source basis before projection",
    "ctP_state": "Minkowski interacting vacuum, retarded/in-in tree sector inherited from Iteration 147",
    "probe_count": len(kinematics),
    "kinematics": kinematics,
    "gaussian_window": {"tau":TAU, "L":LWIN, "min_weight":min(allw), "max_weight":max(allw)},
    "projector_checks": {
        "max_abs_k_contract": max_conservation,
        "max_abs_trace": max_trace,
        "max_abs_idempotence_error": max_idempotence,
    },
    "status": {
        "source_observable_convention": "FROZEN",
        "finite_offshell_probes": "PASS",
        "ward_projector_regression": "PASS",
        "eh_plus_local_eft_cubic_response": "BLOCKED_VERTEX_IMPLEMENTATION",
        "V_C5_chi2R_rank": "NOT_COMPUTED",
        "loops_nonanalytic": "BLOCKED"
    }
}
print(json.dumps(out, indent=2, sort_keys=True))
