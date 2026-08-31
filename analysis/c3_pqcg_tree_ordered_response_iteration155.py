#!/usr/bin/env python3
"""Iteration 155: tree causal nonlinear response of the fixed PQCG comparator.

The covariant PQCG Onsager-Machlup dynamics diffuses around Einstein's equation.
At tree level, functional differentiation of the nonlinear Einstein drift gives
exactly the standard GR retarded second-order response kernel

    chi2R = - G_R Gamma3_EH G_R G_R.

This script imports the already-frozen six-probe EH response fingerprint from
Iteration 150 and records the crucial comparator fact: with G_N fixed by the
hard GR normalization, this tree response has zero tangent with respect to the
PQCG diffusion parameters (D2,D0).  It is a nonzero common GR-boundary response,
not a new diffusion direction.

Diffusion-dependent stochastic/MSR loop corrections and the protocol-specific
order-sensitive scalar selector remain BLOCKED rather than zero-filled.
"""

import json
from pathlib import Path
import numpy as np

base_path = Path("results/c5_cubic_response_iteration150.json")
base = json.loads(base_path.read_text(encoding="utf-8"))
eh = np.array([row["EH_response"] for row in base["rows"]], dtype=float)

# Parameter vector inherited from C3-PQCG-LIN/NL: (D2,D0).
# The tree Einstein drift coefficient is fixed by the calibrated G_N boundary,
# hence the derivative of this tree response wrt diffusion parameters is zero.
V_diffusion_tree = np.zeros((len(eh), 2), dtype=float)

out = {
    "iteration": 155,
    "comparator_id": "C3-PQCG-NL-001",
    "scope": "tree causal nonlinear response from the same covariant PQCG Einstein drift",
    "tree_kernel": "chi2R_A;BC = - G_R_AA' Gamma3_EH^A'_{B'C'} G_R^B'_B G_R^C'_C",
    "six_probe_tree_response": eh.tolist(),
    "parameter_order": ["D2", "D0"],
    "V_diffusion_tree_chi2R": V_diffusion_tree.tolist(),
    "rank_added_in_diffusion_tangent": int(np.linalg.matrix_rank(V_diffusion_tree)),
    "reason_zero_tangent": "tree Einstein response is fixed by calibrated G_N and does not vary with D2,D0",
    "status": {
        "nonzero_classical_causal_nonlinear_response": "PASS_SCOPED",
        "tree_common_GR_boundary": "PASS_SCOPED",
        "diffusion_dependent_ordered_response": "BLOCKED_STOCHASTIC_LOOP_RESPONSE",
        "chi2R_order_sensitive_scalar_selector": "BLOCKED_SELECTOR_COMPLETION",
        "full_C3_ordered_tangent": "BLOCKED",
        "Fisher_resources": "FORBIDDEN",
        "ANSATZ_003": "NOT_CREATED",
    },
    "interpretation": {
        "new_C3_diffusion_rank": 0,
        "quantum_metric_claim_from_nonzero_chi2R": "NOT_SUPPORTED",
        "next_action": "move to fixed nonlinear C4 unless a same-convention diffusion-dependent PQCG ordered response is explicitly derived",
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
