#!/usr/bin/env python3
"""Iteration 570: exact covariance propagation for frozen QUARTER central4 stencil.

Diagnostic-only.  No physical promotion, no support substitution, no threshold or
precision changes.  The 4x4 mixed stencil is C = w⊗w with w=(1,-8,8,-1) and
normalization 1/(144 h^2).
"""
from fractions import Fraction
import json

w = [1, -8, 8, -1]

# Exact deterministic identities.
assert sum(w) == 0
norm2 = sum(x*x for x in w)
assert norm2 == 130

# For a separable coordinate-error covariance Cov(vec E)=Sigma_v⊗Sigma_u,
# vec(C)=w⊗w, hence Var(<C,E>)=(w^T Sigma_u w)(w^T Sigma_v w).
# We record the quadratic-form coefficient ledger for any symmetric 4x4 Sigma.
quad_terms = {
    "S00": 1,
    "S01": -16,
    "S02": 16,
    "S03": -2,
    "S11": 64,
    "S12": -128,
    "S13": 16,
    "S22": 64,
    "S23": -16,
    "S33": 1,
}
assert sum(quad_terms.values()) == 0  # Sigma=J common-mode covariance is nulled.

# iid check: Sigma_u=Sigma_v=sigma^2 I -> (130 sigma^2)^2/(144^2 h^4)
# = 16900 sigma^4/(20736 h^4).  If coordinate variance itself is tau^2,
# iid 16-coordinate covariance is not this separable parameterization unless one
# factor is dimensionless; retain this only as a Kronecker-factor consistency check.

out = {
    "iteration": 570,
    "classification": "PASS_ITER424_QUARTER_SEPARABLE_CORRELATED_COVARIANCE_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING",
    "w": w,
    "w_sum": sum(w),
    "w_norm2_squared": norm2,
    "quadratic_form_coefficients": quad_terms,
    "exact_contract": "Var(D_uv)=(w^T Sigma_u w)(w^T Sigma_v w)/(144^2 h^4) for Cov(vec E)=Sigma_v kron Sigma_u",
    "common_mode_null": "w^T J w=0, so a perfectly common correlated mode in either tensor factor contributes zero variance",
    "guardrails": [
        "diagnostic-only",
        "non-promoting",
        "no rank skipping or substitution",
        "no ANSATZ-003",
        "no Fisher/resources before nonzero algebraic residual"
    ],
    "MODEL_READINESS": "24%"
}
print(json.dumps(out, indent=2, sort_keys=True))
