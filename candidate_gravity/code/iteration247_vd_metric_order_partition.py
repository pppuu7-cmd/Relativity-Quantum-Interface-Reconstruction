#!/usr/bin/env python3
"""Iteration 247: cubic metric-order partitions of Vilkovisky EOM sectors.

Purpose: prevent an invalid extension of Iteration 246.  The soft linearized
Einstein EOM vanishes, but nonlinear EOM variations E^(2), E^(3) with the soft
leg need not vanish.  Enumerate all perturbative h^3 partitions for a sector
with e explicit EOM factors (each starts at h^1) and a residual kernel/dressing
factor K that may start at h^0.

A sector is guaranteed killed by E^(1)[soft]=0 only if every h^3 partition
forces all external legs into separate linear EOM factors.  That occurs for
e=3 and not for e=1,2.
"""

import json


def compositions(total, n, minimum=1):
    if n == 0:
        return [()] if total == 0 else []
    out = []
    def rec(prefix, left, slots):
        if slots == 1:
            if left >= minimum:
                out.append(tuple(prefix + [left]))
            return
        for x in range(minimum, left - minimum * (slots - 1) + 1):
            rec(prefix + [x], left - x, slots - 1)
    rec([], total, n)
    return out


sectors = {}
for e in (1, 2, 3):
    partitions = []
    # EOM factors each start at h^1; residual kernel K may carry h^k, k>=0.
    for k_order in range(0, 4):
        e_total = 3 - k_order
        for ep in compositions(e_total, e, minimum=1):
            partitions.append({
                "E_orders": list(ep),
                "kernel_order": k_order,
                "contains_nonlinear_E": any(x >= 2 for x in ep),
            })
    sectors[str(e)] = partitions

assert sectors["3"] == [{"E_orders": [1,1,1], "kernel_order": 0, "contains_nonlinear_E": False}]

# Guaranteed null-soft elimination logic.
# e=3: the only partition is E1*E1*E1, so the soft leg must occupy one E1.
# e=2: E1*E2*K0 exists; the soft leg can be inside E2 together with a hard leg.
# e=1: E3*K0 and E2*K1 exist.
guaranteed_killed = {"1": False, "2": False, "3": True}

result = {
    "iteration": 247,
    "model_readiness_percent": 24,
    "cubic_metric_partitions": sectors,
    "guaranteed_null_soft_elimination_by_linear_EOM_zero": guaranteed_killed,
    "surviving_structural_terms": {
        "e1": ["E3 K0", "E2 K1", "E1 K2 (only placements with soft outside isolated E1 survive)"],
        "e2": ["E1 E2 K0", "E2 E1 K0", "E1 E1 K1 (soft must enter K1 to survive)"],
        "e3": []
    },
    "classification": "PASS_CUBIC_METRIC_ORDER_PARTITION_E3_ONLY_GUARANTEED_NULL_SOFT_ZERO",
    "guardrail": "DO_NOT_EXTEND_ITERATION246_ZERO_TO_E1_OR_E2_WITHOUT_NONLINEAR_EOM_CALCULATION",
    "remaining_C5_blocks": ["e0 determinant", "e1 nonlinear EOM/kernel variation", "e2 nonlinear EOM/kernel variation", "source/Ward/causal cut projection"],
    "candidate_residual": False,
    "next_gate": 248
}

print(json.dumps(result, indent=2, sort_keys=True))
