#!/usr/bin/env python3
"""Iteration 519: exact sufficient local-scaled -> assembled MP discrepancy contract.

This audit does not replace the frozen assembled BASE/HALF MP80<->MP120 gate.
It derives a sufficient envelope criterion showing when local scaled precision
certificates are strong enough to imply the assembled scaled threshold, and
also proves why local PASS alone is not logically sufficient without amplitude
information.
"""
from fractions import Fraction
import json

h = Fraction(5, 10**6)          # frozen BASE_H = 5e-6
local_eps = Fraction(1, 10**30) # local scaled MP80<->MP120 limit
assembled_tau = Fraction(2, 10**6)  # frozen assembled scaled limit 2e-6

l1_base = Fraction(9, 4)
l1_half = Fraction(9, 1)
l1_delta = Fraction(397, 36)

# For each coordinate i, local scaled PASS means
# |x80_i-x120_i| <= local_eps * S_i,
# S_i=max(1,|x80_i|,|x120_i|).
# For a frozen assembly row w (dimensionless weights in units 1/h^2),
# |A80-A120| <= local_eps/h^2 * sum_i |w_i| S_i.
# Since max(1,|A80|,|A120|)>=1, the same absolute RHS is also an upper
# bound on assembled scaled discrepancy. Hence the sufficient weighted-envelope
# condition is sum_i |w_i| S_i <= assembled_tau*h^2/local_eps.
weighted_budget = assembled_tau * h * h / local_eps
assert weighted_budget == 50_000_000_000_000

uniform_base = weighted_budget / l1_base
uniform_half = weighted_budget / l1_half
uniform_delta = weighted_budget / l1_delta

assert uniform_base == Fraction(200_000_000_000_000, 9)
assert uniform_half == Fraction(50_000_000_000_000, 9)
assert uniform_delta == Fraction(1_800_000_000_000_000, 397)

result = {
    "iteration": 519,
    "classification": "PASS_LOCAL_SCALED_TO_ASSEMBLED_MP_SUFFICIENT_ENVELOPE_CONTRACT_EXACT__NON_PROMOTING",
    "frozen_inputs": {
        "base_h": "5e-6",
        "local_scaled_mp_limit": "1e-30",
        "assembled_scaled_mp_limit": "2e-6",
        "BASE_l1": "9/4",
        "HALF_l1": "9",
        "DELTA_union_l1": "397/36"
    },
    "exact_statement": "If local scaled discrepancies obey |x80_i-x120_i| <= eps*S_i with S_i=max(1,|x80_i|,|x120_i|), then assembled scaled discrepancy for row w is <= eps/h^2 * sum_i |w_i|S_i. Therefore sum_i |w_i|S_i <= tau*h^2/eps is sufficient for the frozen assembled threshold tau.",
    "weighted_envelope_budget": str(weighted_budget),
    "uniform_Smax_sufficient_bounds": {
        "BASE": str(uniform_base),
        "HALF": str(uniform_half),
        "BASE_minus_HALF_if_cross_precision_diagnostic_is_evaluated": str(uniform_delta)
    },
    "guardrail": "Local scaled MP PASS by itself does not imply assembled scaled MP PASS because the local normalization S_i carries amplitude information and assembled cancellation can make the assembled denominator as small as 1. The frozen assembled BASE/HALF gate therefore remains mandatory.",
    "promotion": False,
    "model_readiness_percent": 24
}

print(json.dumps(result, indent=2, sort_keys=True))
