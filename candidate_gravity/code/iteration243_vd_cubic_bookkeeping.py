#!/usr/bin/env python3
"""Iteration 243: curvature/EOM bidegree bookkeeping for finite VD O(R^3).

Scope: frozen Minkowski target, Lambda=0. The Einstein equations of motion
are O(R) around flat space.  A Vilkovisky connection-sector term with EOM
order e and additional background-curvature dressing c can contribute to the
curvature-cubic effective action only if e+c <= 3.

This script enumerates the required finite sectors and the allowed trace
monomial topologies built from U1 (degree 1), U2 (degree 2), and a primitive
U3 sector (degree 3).  It does NOT infer unknown coefficients of the exact
O(epsilon^3) Vilkovisky reduction.
"""

from itertools import product
import json

MAX_R = 3

required = []
for e in range(0, 6):
    max_c = MAX_R - e
    required.append({
        "eom_degree": e,
        "max_background_curvature_degree": max(max_c, -1),
        "can_contribute_to_R3": max_c >= 0,
    })

# Trace-cyclic monomial topologies of total EOM degree 3.
# U1 has degree 1; U2 has degree 2; U3 denotes one or more primitive degree-3
# structures from the full VD reduction.
cubic_topologies = [
    {"topology": "Tr(U3_a)", "degree": 3, "coefficient_known": False,
     "note": "primitive O(epsilon^3) VD structure(s); exact operator content/coefficients must come from full reduction"},
    {"topology": "Tr(U1 U2)", "degree": 3, "coefficient_known": False,
     "note": "cyclic trace identifies Tr(U1 U2)=Tr(U2 U1); coefficient cannot be inferred from the UV-truncated Eq.(14) alone"},
    {"topology": "Tr(U1^3)", "degree": 3, "coefficient_known": False,
     "note": "allowed composite cubic topology; coefficient cannot be inferred from the UV-truncated Eq.(14) alone"},
]

# Lower EOM orders whose kernels must be curvature-dressed so total order is 3.
dressing = [
    {"sector": "determinants Tr ln H and Tr ln N", "eom_degree": 0,
     "required_background_order": 3, "generic_CPT3_reusable": True},
    {"sector": "O(epsilon): Tr U1", "eom_degree": 1,
     "required_background_order": 2, "generic_CPT3_reusable": "only after composite operator is represented in reusable master traces"},
    {"sector": "O(epsilon^2): Tr U2 and Tr U1^2", "eom_degree": 2,
     "required_background_order": 1, "generic_CPT3_reusable": "partially; composite inverse-operator structure must be preserved"},
    {"sector": "O(epsilon^3): primitive/composite cubic insertion sector", "eom_degree": 3,
     "required_background_order": 0, "generic_CPT3_reusable": "flat-kernel master integrals sufficient once exact operator formula is known"},
]

result = {
    "iteration": 243,
    "scope": "Minkowski_Lambda0_finite_curvature_cubic",
    "model_readiness_percent": 24,
    "max_total_curvature_order": MAX_R,
    "required_eom_orders": [0, 1, 2, 3],
    "provably_irrelevant_eom_orders_for_R3": "e>=4",
    "required_sectors": required,
    "cubic_trace_topologies": cubic_topologies,
    "curvature_dressing_requirements": dressing,
    "heavy_run_authorized": False,
    "missing_minimal_authority": "exact full Vilkovisky O(epsilon^3) reduced operator formula and coefficients",
    "classification": "FINITE_CUBIC_VD_BOOKKEEPING_CLOSED_OEPS3_FORMULA_STILL_BLOCKED"
}

assert all(x["can_contribute_to_R3"] for x in required[:4])
assert not any(x["can_contribute_to_R3"] for x in required[4:])
assert sum(1 for x in cubic_topologies if x["degree"] == 3) == 3

print(json.dumps(result, indent=2, sort_keys=True))
