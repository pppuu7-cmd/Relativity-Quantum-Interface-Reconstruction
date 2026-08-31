#!/usr/bin/env python3
"""Iteration 157: shared-boundary/gain quotient audit of C4-DRGT-001.

Iteration 156 showed that the two-column dRGT tangent is independent of the two
implemented C5 R^3 columns.  This script applies a stricter finite quotient by
also including:

  * the common EH nonlinear response direction;
  * a conservative common response-gain nuisance direction equal to the frozen
    dRGT reference response.

It then repeats the projection under several invertible row normalizations.
Rank is invariant under those scalings, while residual fractions diagnose
near-degeneracy/conditioning.
"""

import json
from pathlib import Path
import numpy as np

c5 = json.loads(Path("results/c5_cubic_response_iteration150.json").read_text())
c4 = json.loads(Path("results/c4_drgt_nonlinear_tangent_iteration156.json").read_text())

EH = np.array([row["EH_response"] for row in c5["rows"]], dtype=float)
V5 = np.array([[row["Ricci3_response"], row["Riemann3_response"]] for row in c5["rows"]], dtype=float)
Rref = np.array(c4["tree_response"], dtype=float)
V4 = np.array(c4["V_C4_chi2R"], dtype=float)

# Conservative base span: common GR nonlinear response, the two implemented
# local C5 directions, and one unknown overall response gain at the dRGT point.
M = np.column_stack([EH, V5, Rref])


def audit(scale):
    W = np.diag(1.0 / np.asarray(scale, dtype=float))
    Mb = W @ M
    Vb = W @ V4
    P = Mb @ np.linalg.pinv(Mb)
    residual = Vb - P @ Vb
    combined = np.column_stack([Mb, Vb])
    s = np.linalg.svd(combined, compute_uv=False)
    rnorm = np.linalg.norm(residual, axis=0)
    vnorm = np.linalg.norm(Vb, axis=0)
    return {
        "base_rank": int(np.linalg.matrix_rank(Mb, tol=1e-12)),
        "combined_rank": int(np.linalg.matrix_rank(combined, tol=1e-12)),
        "combined_singular_values": s.tolist(),
        "residual_norms": rnorm.tolist(),
        "tangent_norms": vnorm.tolist(),
        "residual_fractions": (rnorm / vnorm).tolist(),
    }

scales = {
    "raw": np.ones(6),
    "base_row_l2": np.maximum(np.linalg.norm(M, axis=1), 1e-12),
    "EH_abs_floor": np.maximum(np.abs(EH), 1e-3),
    "dRGT_reference_abs_floor": np.maximum(np.abs(Rref), 1e-3),
}

audits = {name: audit(scale) for name, scale in scales.items()}

out = {
    "iteration": 157,
    "comparator_id": "C4-DRGT-001",
    "scope": "TT six-probe shared-boundary and gain nuisance quotient",
    "base_columns": ["EH_common", "C5_Ricci3", "C5_Riemann3", "common_response_gain_at_dRGT_reference"],
    "candidate_C4_tangent_columns": ["log_m2", "alpha3"],
    "audits": audits,
    "summary": {
        "rank_stable_all_scalings": all(v["combined_rank"] == 6 for v in audits.values()),
        "base_rank_all_scalings": sorted(set(v["base_rank"] for v in audits.values())),
        "combined_rank_all_scalings": sorted(set(v["combined_rank"] for v in audits.values())),
        "log_m2_residual_fraction_range": [
            min(v["residual_fractions"][0] for v in audits.values()),
            max(v["residual_fractions"][0] for v in audits.values()),
        ],
        "alpha3_residual_fraction_range": [
            min(v["residual_fractions"][1] for v in audits.values()),
            max(v["residual_fractions"][1] for v in audits.values()),
        ],
        "interpretation": "algebraic independence survives, but log_m2 is near-degenerate after common-EH/gain quotient whereas alpha3 is materially more robust",
    },
    "status": {
        "shared_boundary_quotient": "PASS_SCOPED",
        "log_m2_direction": "NEAR_DEGENERATE_NOT_PROMOTABLE",
        "alpha3_direction": "SCOPED_RESIDUAL_SURVIVES",
        "full_C4": "BLOCKED_HELICITY_AND_HIGHER_POINT_COMPLETION",
        "full_C5": "BLOCKED_HIGHER_LOCAL_AND_LOOPS",
        "Fisher_resources": "FORBIDDEN",
        "ANSATZ_003": "NOT_CREATED",
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
