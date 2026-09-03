#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 299.

Exact algebraic audit of what a four-dimensional numerator oracle can and cannot
fix when the same-parent loop measure is dimensionally regulated.

Write delta = D-4 and
    N(delta) = sum_{j>=0} N_j delta^j,
    M(delta) = sum_{k>=-p} A_k delta^k.
The coefficient of delta^r in N M is the convolution
    C_r = sum_j N_j A_{r-j}.

The C5 primary authority performs intermediate algebra at arbitrary D before
D->4 pole extraction.  Therefore N_{j>0} is not licensed to be zero merely
because a 4D numerical oracle cannot see it.

This iteration does not infer any missing N_j.  It freezes a fail-closed
promotion rule for later bubble/triangle Laurent results.
"""
import json
from fractions import Fraction


def product_coeff(n, a, r):
    """Exact coefficient of delta**r for finite Laurent dictionaries."""
    s = Fraction(0)
    terms = []
    for j, nj in sorted(n.items()):
        k = r - j
        if k in a:
            term = nj * a[k]
            s += term
            terms.append((j, k, term))
    return s, terms

# Symbolic dependency maps represented by coefficient labels rather than values.
def dependency_map(pole_order, max_n=4):
    # A_k exists from -pole_order upward.  For each requested coefficient, list
    # which numerator Taylor orders N_j can enter.
    out = {}
    for r, name in [(-pole_order, 'leading_pole'), (-1, 'single_pole'), (0, 'finite')]:
        if r < -pole_order:
            continue
        deps = []
        for j in range(max_n + 1):
            k = r - j
            if k >= -pole_order:
                deps.append({'numerator_order_j': j, 'master_order_k': k})
        out[name] = deps
    return out

simple = dependency_map(1)
double = dependency_map(2)

# Exact numerical spot checks of the convolution identities.
N = {0: Fraction(2), 1: Fraction(3), 2: Fraction(5)}
M1 = {-1: Fraction(7), 0: Fraction(11), 1: Fraction(13)}
M2 = {-2: Fraction(17), -1: Fraction(19), 0: Fraction(23)}

c_simple_res, _ = product_coeff(N, M1, -1)
c_simple_fin, _ = product_coeff(N, M1, 0)
c_double_lead, _ = product_coeff(N, M2, -2)
c_double_single, _ = product_coeff(N, M2, -1)
c_double_fin, _ = product_coeff(N, M2, 0)

assert c_simple_res == N[0] * M1[-1]
assert c_simple_fin == N[0] * M1[0] + N[1] * M1[-1]
assert c_double_lead == N[0] * M2[-2]
assert c_double_single == N[0] * M2[-1] + N[1] * M2[-2]
assert c_double_fin == N[0] * M2[0] + N[1] * M2[-1] + N[2] * M2[-2]

# Promotion rules follow directly from the convolution structure.
rules = {
    'simple_pole_case': {
        'leading_1_over_delta_residue_from_4d_numerator': 'PROTECTED_AGAINST_O_DELTA_NUMERATOR_TERMS',
        'finite_remainder_from_4d_numerator': 'BLOCKED_IF_LEADING_POLE_NONZERO_WITHOUT_N1_OR_SCHEME_CONVERSION',
        'reason': 'C_-1=N0*A_-1, but C_0=N0*A_0+N1*A_-1',
    },
    'double_or_higher_pole_case': {
        'leading_highest_pole_from_4d_numerator': 'PROTECTED',
        'subleading_poles_from_4d_numerator': 'BLOCKED_WITHOUT_REQUIRED_NJ',
        'finite_remainder_from_4d_numerator': 'BLOCKED',
        'reason': 'for p=2, C_-1=N0*A_-1+N1*A_-2 and C_0=N0*A_0+N1*A_-1+N2*A_-2',
    },
    'no_pole_case': {
        'finite_cut_from_4d_numerator': 'NOT_BLOCKED_BY_POLE_TIMES_EVANESCENT_MECHANISM_AT_THIS_ORDER',
        'caveat': 'other scheme dependence still requires matched same-parent observable audit',
    },
}

result = {
    'iteration': 299,
    'model_readiness_percent': 24,
    'scope': 'exact algebraic evanescent/pole sensitivity theorem for 4D numerator oracle plus D-dimensional loop measure',
    'parent_authority': {
        'paper': 'Giacchini, de Paula Netto, Shapiro, Phys. Rev. D 102, 106006 (2020), arXiv:2006.04217',
        'authority_fact': 'intermediate quantum-gravity calculation is kept at arbitrary D and the D->4 limit is taken only for the pole coefficient; explicit intermediate coefficients contain D-4 factors',
        'interpretation': 'same-parent D-dimensional numerator Taylor coefficients beyond N0 are not licensed to zero-fill',
    },
    'delta_definition': 'delta=D-4=-2 epsilon',
    'simple_pole_dependency_map': simple,
    'double_pole_dependency_map': double,
    'promotion_rules': rules,
    'classification': 'PASS_EXACT_EVANESCENT_POLE_SENSITIVITY_PROMOTION_RULE__FINITE_SAME_PARENT_REMAINDER_STILL_BLOCKED',
    'candidate_residual': False,
    'guardrails': [
        'FOUR_DIMENSIONAL_ORACLE_ABSENCE_OF_EVANESCENT_TERMS_IS_NONIDENTIFIABILITY_NOT_ZERO',
        'DO_NOT_PROMOTE_FINITE_REMAINDER_ACROSS_A_NONZERO_POLE_WITHOUT_REQUIRED_D_DIMENSIONAL_NUMERATOR_COEFFICIENTS_OR_EXPLICIT_SCHEME_CONVERSION',
        'LEADING_HIGHEST_LAURENT_POLE_IS_INSENSITIVE_TO_POSITIVE_DELTA_NUMERATOR_ORDERS',
        'FOR_DOUBLE_OR_HIGHER_POLES_SUBLEADING_POLES_CAN_BE_EVANESCENT_SENSITIVE',
    ],
    'next_gate': 'when corrected Iteration 296 is schema-valid, classify its observed bubble pole order and promote only coefficients protected by this theorem; keep finite same-parent authority blocked until D-dimensional numerator continuation or explicit scheme conversion is supplied',
}

print(json.dumps(result, indent=2, sort_keys=True))
