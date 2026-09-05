#!/usr/bin/env python3
"""Iteration 469: exact cancellation decomposition for frozen central4×central4 assembly.

This is an implementation/provenance audit only. It does not alter ds=-d_base,
any frozen threshold, support order, or physical interpretation.
"""
from fractions import Fraction
import json
import random

ALPHA = {
    (1, 1): Fraction(4, 9),
    (1, 2): Fraction(-1, 18),
    (2, 1): Fraction(-1, 18),
    (2, 2): Fraction(1, 144),
}


def quartet(F, a, b):
    return F[(a,b)] - F[(-a,b)] - F[(a,-b)] + F[(-a,-b)]


def metrics(F):
    q = {ab: quartet(F, *ab) for ab in ALPHA}
    D = sum(ALPHA[ab] * q[ab] for ab in ALPHA)
    S_quartet = sum(abs(ALPHA[ab] * q[ab]) for ab in ALPHA)
    S_sample = sum(abs(ALPHA[(a,b)]) * sum(abs(F[(sa*a,sb*b)]) for sa in (-1,1) for sb in (-1,1))
                   for a,b in ALPHA)
    assert abs(D) <= S_quartet <= S_sample
    rho_parity = None if S_sample == 0 else S_quartet / S_sample
    rho_shell = None if S_quartet == 0 else abs(D) / S_quartet
    if D != 0:
        kappa_sample = S_sample / abs(D)
        kappa_quartet = S_quartet / abs(D)
        assert kappa_sample >= kappa_quartet >= 1
        assert rho_parity * rho_shell == Fraction(1, 1) / kappa_sample
        assert rho_shell == Fraction(1, 1) / kappa_quartet
    else:
        kappa_sample = kappa_quartet = None
    return D, S_quartet, S_sample, rho_parity, rho_shell, kappa_sample, kappa_quartet


def main():
    # Exact coefficient checks.
    assert sum(abs(a) for a in ALPHA.values()) == Fraction(9,16)
    assert 4 * sum(abs(a) for a in ALPHA.values()) == Fraction(9,4)

    # Reproducible exact-rational stress test of the universal inequalities/identities.
    random.seed(469)
    n = 5000
    zero_D = 0
    for _ in range(n):
        F = {}
        for a,b in ALPHA:
            for sa in (-1,1):
                for sb in (-1,1):
                    F[(sa*a,sb*b)] = Fraction(random.randint(-1000,1000), random.randint(1,97))
        out = metrics(F)
        if out[0] == 0:
            zero_D += 1

    result = {
        "iteration": 469,
        "classification": "PASS_QUARTET_CANCELLATION_DECOMPOSITION__DIAGNOSTIC_ONLY_NON_PROMOTING",
        "sum_abs_quartet_coefficients": "9/16",
        "canonical_sample_L1_norm_dimensionless": "9/4",
        "theorem": [
            "|D| <= S_quartet <= S_sample",
            "kappa_sample >= kappa_quartet >= 1 when D != 0",
            "rho_parity=S_quartet/S_sample in [0,1]",
            "rho_shell=|D|/S_quartet in [0,1]",
            "kappa_sample=1/(rho_parity*rho_shell)",
            "kappa_quartet=1/rho_shell"
        ],
        "stress_cases": n,
        "zero_D_cases": zero_D,
        "model_readiness_percent": 24,
        "readiness_change_pp": 0
    }
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
