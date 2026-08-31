#!/usr/bin/env python3
"""Iteration 154: nonlinear classical post-Gaussian C3 comparator.

Extends C3-PQCG-LIN-001 using the same covariant postquantum-classical gravity
family.  The pure-gravity Onsager-Machlup action is

    S[g] = 1/2 int sqrt(-g) [alpha R_mn R^mn - beta R^2].

Around Minkowski, its quadratic covariance is matched to the Iteration-153
spin-2/spin-0 convention

    <h h>_2 = 2 D2 P2 / (k^2)^2,
    <h h>_0 = 2 D0 P0 / (k^2)^2,

which gives D2 = 1/(2 alpha), D0 = 1/[8(alpha-3 beta)].

On the frozen six TT probes R^(1)=0, so the R^2 cubic coefficient vanishes
analytically.  The Ricci-squared cubic coefficient is evaluated directly from
the unreduced covariant action.  At tree level a classical probability action
S=S2+S3+... gives

    <h1 h2 h3>_c = - C1 C2 C3 Gamma3,

so the TT bispectrum scales as D2^2.  Combining this C3sym coordinate with the
Iteration-153 N2 coordinate resolves the linear 5 D2 + D0 degeneracy.

This is a scoped classical stochastic comparator result, not evidence for a
quantum metric and not a full nonlinear C3 closure.
"""

import itertools
import json
import math
import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])
TAU = 0.8
LWIN = 0.6

QS = [np.array(x, float) for x in [
    [0.18, 0.70, 0.20, 0.10],
    [0.14, 0.55,-0.25, 0.20],
    [0.22, 0.62, 0.18,-0.24],
    [0.16, 0.48, 0.31, 0.12],
    [0.20, 0.58,-0.16,-0.28],
    [0.12, 0.44, 0.27,-0.19],
]]
RS = [np.array(x, float) for x in [
    [0.11,-0.21, 0.52, 0.17],
    [0.09, 0.24, 0.46,-0.18],
    [0.10,-0.18, 0.41, 0.29],
    [0.13, 0.22,-0.37, 0.33],
    [0.08, 0.26, 0.35, 0.21],
    [0.15,-0.20, 0.39, 0.25],
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


def curvature_density(eps, ks, es, alpha=1.0, beta=0.0):
    """Local density 1/2 sqrt(-g) [alpha Ricci^2 - beta R^2] at x=0."""
    g = ETA.astype(complex).copy()
    dg = np.zeros((4, 4, 4), complex)       # dg[lambda,a,b]
    ddg = np.zeros((4, 4, 4, 4), complex)  # ddg[lambda,mu,a,b]

    for ep, k, e in zip(eps, ks, es):
        kc = ETA @ k
        g += ep * e
        dg += ep * 1j * np.einsum("l,ab->lab", kc, e)
        ddg += -ep * np.einsum("l,m,ab->lmab", kc, kc, e)

    gi = np.linalg.inv(g)
    sqrtmg = np.sqrt(-np.linalg.det(g))

    dgi = np.empty((4, 4, 4), complex)
    for lam in range(4):
        dgi[lam] = -gi @ dg[lam] @ gi

    Gamma = np.zeros((4, 4, 4), complex)
    dGamma = np.zeros((4, 4, 4, 4), complex)

    for a, m, n in itertools.product(range(4), repeat=3):
        Avec = np.array(
            [dg[m, b, n] + dg[n, b, m] - dg[b, m, n] for b in range(4)]
        )
        Gamma[a, m, n] = 0.5 * np.dot(gi[a], Avec)
        for lam in range(4):
            dA = np.array([
                ddg[lam, m, b, n]
                + ddg[lam, n, b, m]
                - ddg[lam, b, m, n]
                for b in range(4)
            ])
            dGamma[lam, a, m, n] = 0.5 * (
                np.dot(dgi[lam, a], Avec) + np.dot(gi[a], dA)
            )

    Ric = np.zeros((4, 4), complex)
    for m, n in itertools.product(range(4), repeat=2):
        val = sum(
            dGamma[a, a, m, n] - dGamma[n, a, m, a]
            for a in range(4)
        )
        val += sum(
            Gamma[a, a, b] * Gamma[b, m, n]
            - Gamma[a, n, b] * Gamma[b, m, a]
            for a, b in itertools.product(range(4), repeat=2)
        )
        Ric[m, n] = val

    Rscalar = np.einsum("mn,mn", gi, Ric)
    Ricci2 = np.einsum("mn,ma,nb,ab", Ric, gi, gi, Ric)
    return 0.5 * sqrtmg * (alpha * Ricci2 - beta * Rscalar * Rscalar)


def mixed3(fun, d):
    total = 0j
    for signs in itertools.product([-1, 1], repeat=3):
        total += np.prod(signs) * fun([d * x for x in signs])
    return total / (8.0 * d ** 3)


# Same deterministic TT seeds used by the frozen C5 six-probe layer.
seeds = []
for i in range(18):
    rng = np.random.default_rng(100 + i)
    Aseed = rng.normal(size=(4, 4))
    seeds.append((Aseed + Aseed.T) / 2.0)

rows = []
B_terms = []
alpha_convergence_ratios = []
beta_quarter_ratios = []

for i, (q, r) in enumerate(zip(QS, RS)):
    p = q + r
    ks = [p, -q, -r]
    es = [polarization(ks[j], seeds[3 * i + j]) for j in range(3)]

    ds = (2.5e-3, 1.25e-3, 6.25e-4)
    alpha_raw = [
        mixed3(lambda ep: curvature_density(ep, ks, es, 1.0, 0.0), d).real
        for d in ds
    ]
    beta_raw = [
        mixed3(lambda ep: curvature_density(ep, ks, es, 0.0, 1.0), d).real
        for d in ds
    ]

    # Central mixed third derivative has O(d^2) error.
    alpha_cubic = (4.0 * alpha_raw[-1] - alpha_raw[-2]) / 3.0
    beta_cubic = (4.0 * beta_raw[-1] - beta_raw[-2]) / 3.0

    da1 = abs(alpha_raw[1] - alpha_raw[0])
    da2 = abs(alpha_raw[2] - alpha_raw[1])
    alpha_convergence_ratios.append(da2 / da1 if da1 else 0.0)

    babs = [abs(x) for x in beta_raw]
    beta_quarter_ratios.append([
        babs[1] / babs[0] if babs[0] else 0.0,
        babs[2] / babs[1] if babs[1] else 0.0,
    ])

    denom = (dot(p, p) * dot(q, q) * dot(r, r)) ** 2
    w3 = window(p) * window(q) * window(r)

    # C3_i = - C_p C_q C_r Gamma3.  With C_s=2 D2/(k^2)^2 and
    # alpha=1/(2 D2), C3_i = B_i D2^2.
    B_i = -4.0 * alpha_cubic * w3 / denom
    B_terms.append(B_i)

    rows.append({
        "probe": i,
        "p2": dot(p, p),
        "q2": dot(q, q),
        "r2": dot(r, r),
        "Ricci2_cubic_alpha1": alpha_cubic,
        "R2_cubic_beta1_numeric_regression": beta_cubic,
        "B_i_in_C3sym_equals_B_i_D2_squared": B_i,
    })

# Iteration-153 N2 coefficient.
ks_all = []
for q, r in zip(QS, RS):
    ks_all.extend([q, r, q + r])
A_noise = sum(
    2.0 * window(k) ** 2 / (dot(k, k) ** 2)
    for k in ks_all
)
B_bispectrum = float(sum(B_terms))

# Supported nonlinear comparator map:
# N2 = A (5 D2 + D0)
# C3sym_TT = B D2^2
# Therefore d(N2,C3sym)/d(D2,D0) has determinant -2 A B D2,
# which is nonzero for every physical D2>0 because A>0 and B!=0.
# A normalized D2*=1 point is used only to report an SVD condition diagnostic;
# the generic rank proof is analytic and does not rely on this normalization.
V_normalized = np.array([
    [5.0 * A_noise, A_noise],
    [2.0 * B_bispectrum, 0.0],
])
svals = np.linalg.svd(V_normalized, compute_uv=False)

out = {
    "iteration": 154,
    "comparator_id": "C3-PQCG-NL-001",
    "scope": "pure-gravity nonlinear Onsager-Machlup extension on six frozen TT probes",
    "literature_action": "S=1/2 int sqrt(-g) [alpha Ricci_mn Ricci^mn - beta R^2]",
    "parameter_map": {
        "D2": "1/(2 alpha)",
        "D0": "1/[8(alpha-3 beta)]",
    },
    "supported_rows": ["N2", "C3sym_TT"],
    "blocked_rows": [
        "chi2R_even",
        "chi2R_odd",
        "soft2",
        "tensor_geo",
        "threshold",
    ],
    "rows": rows,
    "A_noise": float(A_noise),
    "B_bispectrum": B_bispectrum,
    "observable_map": {
        "N2": "A_noise*(5 D2 + D0)",
        "C3sym_TT": "B_bispectrum*D2^2",
    },
    "generic_tangent": [
        ["5*A_noise", "A_noise"],
        ["2*B_bispectrum*D2", "0"],
    ],
    "generic_determinant": "-2*A_noise*B_bispectrum*D2",
    "generic_rank_for_D2_positive": 2,
    "normalized_D2_equals_1_tangent": V_normalized.tolist(),
    "normalized_singular_values": svals.tolist(),
    "normalized_smin_over_smax": float(svals[-1] / svals[0]),
    "max_abs_R2_cubic_extrapolated": float(
        max(abs(row["R2_cubic_beta1_numeric_regression"]) for row in rows)
    ),
    "max_alpha_convergence_ratio_error_from_quarter": float(
        max(abs(x - 0.25) for x in alpha_convergence_ratios)
    ),
    "max_beta_raw_quarter_ratio_error_from_quarter": float(
        max(abs(x - 0.25) for pair in beta_quarter_ratios for x in pair)
    ),
    "interpretation": {
        "linear_D2_D0_degeneracy": "RESOLVED_SCOPED_BY_C3SYM_TT",
        "classical_non_gaussianity": "PRESENT_FROM_THE_SAME_COVARIANT_STOCHASTIC_ACTION",
        "quantum_metric_claim": "NOT_SUPPORTED_BY_C3SYM_ALONE",
        "full_C3_comparator": "BLOCKED_ORDERED_RESPONSE_AND_NON_TT_COMPLETION",
        "fisher_resources": "FORBIDDEN",
        "ANSATZ_003": "NOT_CREATED",
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
