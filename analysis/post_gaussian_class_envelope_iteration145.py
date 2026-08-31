#!/usr/bin/env python3
"""Iteration 145 structural class-envelope audit.

This script is NOT a physical comparator tangent calculation. It diagnoses why
broad theory-class capability masks cannot be used as RQIR nuisance matrices.
Physical Iteration-146+ work must replace these masks by derivatives of fixed
finite comparator realizations.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


FULL_COORDS = [
    "norm",
    "N2",
    "chi1R",
    "C3sym",
    "chi2R_even",
    "chi2R_odd",
    "soft0",
    "soft1",
    "soft2",
    "tensor_geo",
    "threshold",
]

# Hard locks: calibrated massless normalization plus leading/subleading soft
# consistency coordinates. The reduced coordinates are therefore the remaining
# eight entries.
HARD_LOCKS = {"norm", "soft0", "soft1"}
REDUCED = [c for c in FULL_COORDS if c not in HARD_LOCKS]

# Conservative class-level capabilities. If a class can in principle modify a
# coordinate somewhere in the broad class, the envelope grants an independent
# basis direction on that coordinate. This intentionally destroys internal
# model correlations and is therefore an over-complete diagnostic only.
CAPABILITIES = {
    "C3_postquantum_classical_envelope": {
        "N2",
        "chi1R",
        "C3sym",
        "chi2R_even",
        "chi2R_odd",
        "tensor_geo",
        "threshold",
    },
    "C4_quantum_mediator_envelope": {
        "N2",
        "chi1R",
        "C3sym",
        "chi2R_even",
        "chi2R_odd",
        "tensor_geo",
        "threshold",
    },
    "C5_quantum_gravity_EFT_envelope": set(REDUCED),
}


def axis_columns(supported: set[str]) -> np.ndarray:
    cols = []
    for j, name in enumerate(REDUCED):
        if name in supported:
            e = np.zeros(len(REDUCED))
            e[j] = 1.0
            cols.append(e)
    return np.column_stack(cols) if cols else np.zeros((len(REDUCED), 0))


def residual_norm(M: np.ndarray, b: np.ndarray) -> float:
    if M.shape[1] == 0:
        return float(np.linalg.norm(b))
    return float(np.linalg.norm(b - M @ (np.linalg.pinv(M) @ b)))


def main() -> int:
    blocks = {name: axis_columns(supp) for name, supp in CAPABILITIES.items()}
    combined = np.column_stack(list(blocks.values()))

    block_ranks = {name: int(np.linalg.matrix_rank(mat)) for name, mat in blocks.items()}
    combined_rank = int(np.linalg.matrix_rank(combined))

    # Test every reduced coordinate as a hypothetical one-coordinate candidate
    # tangent. Full class-envelope saturation must remove all of them.
    candidate_residuals = {}
    for j, coord in enumerate(REDUCED):
        b = np.zeros(len(REDUCED))
        b[j] = 1.0
        candidate_residuals[coord] = residual_norm(combined, b)

    result = {
        "iteration": 145,
        "scope": "structural capability-envelope diagnostic; not physical comparator tangents",
        "full_coordinates": FULL_COORDS,
        "hard_locks": sorted(HARD_LOCKS),
        "reduced_coordinates": REDUCED,
        "reduced_dimension": len(REDUCED),
        "block_ranks": block_ranks,
        "combined_rank": combined_rank,
        "full_rank_saturated": combined_rank == len(REDUCED),
        "single_axis_candidate_residual_norms": candidate_residuals,
        "soft_interpretation": {
            "soft0": "hard consistency lock; not a novelty coordinate",
            "soft1": "hard consistency lock in the frozen standard-GR boundary",
            "soft2": "measured coordinate but included in the C5 EFT capability envelope",
        },
        "decision": "REQUIRE_FIXED_FINITE_COMPARATOR_REALIZATIONS",
        "nonclaim": "Full rank here is not a no-go theorem; it is caused by deliberately independent per-coordinate class capabilities.",
    }

    out = Path("results/post_gaussian_class_envelope_iteration145.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))

    ok = result["full_rank_saturated"] and all(v < 1e-12 for v in candidate_residuals.values())
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
