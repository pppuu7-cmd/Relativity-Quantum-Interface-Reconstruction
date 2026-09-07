#!/usr/bin/env python3
"""Exact full-PSD covariance propagation contract for frozen BASE/HALF assembly.

This audit is deliberately non-promoting. It generalizes Iteration 516 from
independent/diagonal coordinate noise to an arbitrary positive-semidefinite
28-coordinate covariance matrix Sigma. No physical-observable covariance claim
is made.
"""
from fractions import Fraction
import json

# Exact squared Euclidean norms / Gram entry from frozen assembly authority.
BB = Fraction(4225, 5184)
HH = Fraction(4225, 324)
BH = Fraction(4, 81)
DD = BB + HH - 2 * BH
CROSS_SPECTRAL_BOUND = Fraction(4225, 1296)  # sqrt(BB*HH), exact because 4225=65^2

assert DD == Fraction(23771, 1728)
assert CROSS_SPECTRAL_BOUND * CROSS_SPECTRAL_BOUND == BB * HH

result = {
    "iteration": 518,
    "classification": "PASS_BASE_HALF_FULL_PSD_COVARIANCE_SPECTRAL_CONTRACT_EXACT__NON_PROMOTING",
    "scope": "numerical assembly/error-provenance only",
    "dimension": 28,
    "formulas": {
        "assembled_covariance": "C_A = h^-4 A Sigma A^T, A=[w_BASE^T; w_HALF^T]",
        "delta_variance": "Var(BASE-HALF)=h^-4 (w_BASE-w_HALF)^T Sigma (w_BASE-w_HALF)",
        "psd": "Sigma >= 0 => C_A >= 0",
    },
    "exact_weight_norms": {
        "wB_norm2_sq": str(BB),
        "wH_norm2_sq": str(HH),
        "wDelta_norm2_sq": str(DD),
        "wB_wH_inner_product": str(BH),
    },
    "lambda_max_bounds": {
        "Var_BASE_coeff": str(BB),
        "Var_HALF_coeff": str(HH),
        "Var_DELTA_coeff": str(DD),
        "abs_Cov_BASE_HALF_coeff": str(CROSS_SPECTRAL_BOUND),
        "units": "lambda_max(Sigma)/h^4",
    },
    "key_guardrail": "For arbitrary correlated PSD Sigma, Cov(BASE,HALF) need not be nonnegative; the nonnegative sign in Iteration 516 is diagonal-noise-specific.",
    "nonclaims": [
        "not Candidate-Gravity physical covariance",
        "not consistency PASS/FAIL",
        "not comparator identity",
        "not non-identifiability or near-degeneracy",
        "not novelty certificate",
        "not Fisher authorization",
    ],
}

print(json.dumps(result, indent=2, sort_keys=True))
