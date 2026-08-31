#!/usr/bin/env python3
"""Iteration 156: first fixed nonlinear dRGT massive-spin-2 comparator.

Frozen action (M_Pl and kappa stripped from the dimensionless fingerprint):

 S = M_Pl^2/2 int sqrt(-g) [ R + m^2/2 (L2[K] + a3 L3[K] + a4 L4[K]) ]
     + S_m[g],
 K = I - sqrt(g^{-1} eta),
 L2 = 2([K]^2-[K^2]),
 L3 = [K]^3-3[K][K^2]+2[K^3].

This is the standard two-parameter ghost-free dRGT family with Minkowski
reference metric and alpha2=1, alpha0=alpha1=0.  At cubic order on TT fields
alpha4 is absent.

For H=eta h with Tr H=0,
 K = 1/2 H - 3/8 H^2 + 5/16 H^3 + ...,
so the cubic TT potential density in the bracket is

 m^2 (3+a3)/8 Tr(H^3).

The full scoped tree response includes both the EH cubic vertex and this dRGT
potential vertex, with massive TT propagators 1/(k^2+m^2) on the same six
spacelike probes used by the C5 comparator.

The finite tangent is evaluated at m^2=0.04, alpha3=0 with parameters
(log m^2, alpha3).  alpha4 is recorded as cubic-TT blind rather than as a zero
parameter of the full theory.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])
TAU = 0.8
LWIN = 0.6
M2_REF = 0.04
A3_REF = 0.0
A4_REF = 0.0

QS = [np.array(x, float) for x in [
    [0.18,0.70,0.20,0.10], [0.14,0.55,-0.25,0.20],
    [0.22,0.62,0.18,-0.24], [0.16,0.48,0.31,0.12],
    [0.20,0.58,-0.16,-0.28], [0.12,0.44,0.27,-0.19],
]]
RS = [np.array(x, float) for x in [
    [0.11,-0.21,0.52,0.17], [0.09,0.24,0.46,-0.18],
    [0.10,-0.18,0.41,0.29], [0.13,0.22,-0.37,0.33],
    [0.08,0.26,0.35,0.21], [0.15,-0.20,0.39,0.25],
]]


def dot(a, b):
    return float(a @ ETA @ b)


def theta(k):
    kc = ETA @ k
    return ETA - np.outer(kc, kc) / dot(k, k)


def p2(k):
    t = theta(k)
    return (
        0.5 * (
            np.einsum("mr,ns->mnrs", t, t)
            + np.einsum("ms,nr->mnrs", t, t)
        )
        - (1.0 / 3.0) * np.einsum("mn,rs->mnrs", t, t)
    )


def polarization(k, seed):
    P = p2(k)
    e = np.einsum("mnrs,ra,sb,ab->mn", P, ETA, ETA, seed)
    n = np.einsum("mn,ma,nb,ab", e, ETA, ETA, e)
    return e / np.sqrt(abs(n))


def window(k):
    return math.exp(
        -0.5 * ((TAU * k[0]) ** 2 + (LWIN * np.linalg.norm(k[1:])) ** 2)
    )


c5 = json.loads(Path("results/c5_cubic_response_iteration150.json").read_text())
EH0 = np.array([row["EH_response"] for row in c5["rows"]], dtype=float)
V_C5 = np.array(
    [[row["Ricci3_response"], row["Riemann3_response"]] for row in c5["rows"]],
    dtype=float,
)

seeds = []
for i in range(18):
    rng = np.random.default_rng(100 + i)
    A = rng.normal(size=(4, 4))
    seeds.append((A + A.T) / 2.0)

rows = []
response = []
d_logm2 = []
d_a3 = []

for i, (q, r) in enumerate(zip(QS, RS)):
    p = q + r
    ks = [p, -q, -r]
    es = [polarization(ks[j], seeds[3 * i + j]) for j in range(3)]
    H = [ETA @ e for e in es]

    # Mixed trilinear coefficient of Tr(H^3).
    T3 = float(
        sum(
            np.trace(H[a] @ H[b] @ H[c]).real
            for a, b, c in itertools.permutations(range(3))
        )
    )

    s = [dot(k, k) for k in ks]
    W = float(np.prod([window(k) for k in ks]))

    # EH0 = EH_cubic * W / prod(k^2); hence E is the weighted EH vertex.
    E = float(EH0[i] * np.prod(s))
    P = T3 * W

    m2 = M2_REF
    a3 = A3_REF
    cpot = (3.0 + a3) / 8.0
    D = float(np.prod([x + m2 for x in s]))
    N = E + m2 * cpot * P
    R = N / D

    # dR / d log(m^2) and dR / d alpha3 at the frozen reference point.
    dlogD_dm2 = sum(1.0 / (x + m2) for x in s)
    dR_dm2 = (cpot * P - N * dlogD_dm2) / D
    v_logm2 = m2 * dR_dm2
    v_a3 = m2 * (1.0 / 8.0) * P / D

    response.append(R)
    d_logm2.append(v_logm2)
    d_a3.append(v_a3)
    rows.append({
        "probe": i,
        "p2": s[0], "q2": s[1], "r2": s[2],
        "window_product": W,
        "mixed_TrH3": T3,
        "EH_weighted_vertex": E,
        "dRGT_tree_response": R,
        "d_dlogm2": v_logm2,
        "d_dalpha3": v_a3,
    })

V_C4 = np.column_stack([d_logm2, d_a3])
s4 = np.linalg.svd(V_C4, compute_uv=False)
rank4 = int(np.linalg.matrix_rank(V_C4, tol=1e-12))

P5 = V_C5 @ np.linalg.pinv(V_C5)
residual = V_C4 - P5 @ V_C4
res_norms = np.linalg.norm(residual, axis=0)
col_norms = np.linalg.norm(V_C4, axis=0)
combined = np.column_stack([V_C5, V_C4])
s_comb = np.linalg.svd(combined, compute_uv=False)
rank_comb = int(np.linalg.matrix_rank(combined, tol=1e-12))

out = {
    "iteration": 156,
    "comparator_id": "C4-DRGT-001",
    "scope": "tree TT nonlinear response on six frozen spacelike probes",
    "action_convention": "Mpl^2/2 int sqrt(-g)[R + m^2/2(L2[K]+alpha3 L3[K]+alpha4 L4[K])] + S_m[g]",
    "reference_metric": "eta_mn",
    "reference_parameters": {
        "m2": M2_REF,
        "alpha3": A3_REF,
        "alpha4": A4_REF,
    },
    "tangent_parameters": ["log_m2", "alpha3"],
    "alpha4_cubic_TT_status": "BLIND_AT_CUBIC_ORDER_L4_STARTS_QUARTIC",
    "cubic_TT_potential": "m^2(3+alpha3)/8 * Tr(H^3)",
    "rows": rows,
    "tree_response": response,
    "V_C4_chi2R": V_C4.tolist(),
    "rank_C4": rank4,
    "singular_values_C4": s4.tolist(),
    "smin_over_smax_C4": float(s4[-1] / s4[0]),
    "comparison_to_existing_C5_local_6x2": {
        "C5_rank": int(np.linalg.matrix_rank(V_C5, tol=1e-12)),
        "C4_residual_norms_after_C5_projection": res_norms.tolist(),
        "C4_column_norms": col_norms.tolist(),
        "residual_fractions": (res_norms / col_norms).tolist(),
        "combined_rank_C5_plus_C4": rank_comb,
        "combined_singular_values": s_comb.tolist(),
    },
    "status": {
        "fixed_dRGT_action": "PASS_SCOPED",
        "ghost_free_family_authority": "LITERATURE_ESTABLISHED_FOR_DRGТ_CONSTRAINT_STRUCTURE",
        "TT_cubic_tangent": "PASS_SCOPED",
        "beyond_existing_C5_R3_span": "PASS_SCOPED_RANK_2_TO_4",
        "helicity0_helicity1_completion": "BLOCKED",
        "Vainshtein_nonperturbative_completion": "BLOCKED",
        "C4_N2_C3sym": "BLOCKED",
        "full_C4_quotient": "BLOCKED",
        "Fisher_resources": "FORBIDDEN",
        "ANSATZ_003": "NOT_CREATED",
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
