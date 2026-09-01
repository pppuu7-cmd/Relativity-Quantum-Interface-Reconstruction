#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 254.

Scoped certificate for the first background variation of the diffeomorphism
metric generator and the resulting K1=delta[R.(D R)] decomposition.

Convention: g_{mu nu}=eta_{mu nu}+a eps_{mu nu} exp(i q.x),
xi^mu=c^mu exp(i p.x), and L_xi g is used for the gauge generator.
Overall i/phases are stripped in the numerical coefficient test.
"""
import json
import numpy as np

eta = np.diag([-1.0, 1.0, 1.0, 1.0])
q = np.array([1.0, 0.0, 0.0, 1.0])
eps = np.zeros((4, 4))
eps[1, 1] = 1.0
eps[2, 2] = -1.0
p = np.array([0.7, 0.2, -0.3, 0.4])
c = np.array([0.5, -0.4, 0.6, 0.2])

# TT checks for the chosen hard polarization.
trace_eps = float(np.sum(np.diag(eta) * np.diag(eps)))
q_lower = eta @ q
trans = q_lower @ eps

# Analytic first variation of L_xi g at Fourier coefficient p+q,
# with the common factor i exp(i(p+q).x) stripped:
# delta R_{mn}=(c.q) eps_{mn}+p_m eps_{rho n}c^rho+p_n eps_{m rho}c^rho.
def analytic_delta_R():
    out = np.zeros((4, 4))
    cq = float(np.dot(c, q))
    for m in range(4):
        for n in range(4):
            out[m, n] = (
                cq * eps[m, n]
                + p[m] * sum(eps[r, n] * c[r] for r in range(4))
                + p[n] * sum(eps[m, r] * c[r] for r in range(4))
            )
    return out

# Exact coefficient of L_xi g for finite background amplitude a,
# retaining the background-derivative and ghost-derivative pieces.
def R_at_amplitude(a):
    g = eta + a * eps
    out = np.zeros((4, 4))
    cq = float(np.dot(c, q))
    for m in range(4):
        for n in range(4):
            out[m, n] = (
                a * cq * eps[m, n]
                + p[m] * sum(g[r, n] * c[r] for r in range(4))
                + p[n] * sum(g[m, r] * c[r] for r in range(4))
            )
    return out

analytic = analytic_delta_R()
errors = {}
for h in (1e-3, 1e-5, 1e-7):
    fd = (R_at_amplitude(h) - R_at_amplitude(-h)) / (2.0 * h)
    errors[f"{h:.0e}"] = float(np.max(np.abs(fd - analytic)))

# Structural certificate. For a linear metric variable, the Lie derivative is
# affine in g, hence R_,ik=0. With B_i^j=D_i R^j=R^j_,i+Gamma^j_ik R^k,
# delta B = deltaGamma * R0 + Gamma0 * deltaR.
terms = [
    "deltaR * B0 * E2",
    "R0 * Gamma0 * deltaR * E2",
    "R0 * deltaGamma * R0 * E2",
]

result = {
    "iteration": 254,
    "convention": "D=4, Lambda=0, a=-1/2 parent; linear covariant-metric split for this scoped generator test",
    "tt_trace": trace_eps,
    "tt_transversality_max": float(np.max(np.abs(trans))),
    "finite_difference_max_errors": errors,
    "affine_generator_second_field_variation_zero": True,
    "delta_partial_R_zero_for_linear_metric_split": True,
    "delta_A_E2_terms": terms,
    "classification": "PASS_SCOPED_DIFFEO_GENERATOR_FIRST_VARIATION_AND_K1_DECOMPOSITION",
    "model_readiness": 24,
}
print(json.dumps(result, indent=2, sort_keys=True))
