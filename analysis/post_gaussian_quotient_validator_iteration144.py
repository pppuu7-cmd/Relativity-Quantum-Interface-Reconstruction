#!/usr/bin/env python3
"""Reusable finite post-Gaussian RQIR quotient validator.

Input JSON schema (all arrays numeric):
{
  "H": [[...], ...],
  "v_beta": [...],
  "blocks": {"nuisance": [[column...], ...], "C3": ..., ...},
  "error_bound": 1e-10,
  "svd_rtol": 1e-12,
  "sym_indices": [..],
  "ordered_indices": [..]
}

Block matrices are given in row-major observable coordinates: shape (n_obs, n_cols).
Empty blocks may be []. The script eliminates exact hard constraints first, then
checks whether the candidate tangent adds rank beyond the combined comparator span.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def nullspace(H: np.ndarray, rtol: float) -> np.ndarray:
    n = H.shape[1]
    if H.size == 0 or H.shape[0] == 0:
        return np.eye(n)
    u, s, vh = np.linalg.svd(H, full_matrices=True)
    tol = rtol * (s[0] if s.size else 1.0)
    rank = int(np.sum(s > tol))
    return vh[rank:].T


def matrix_rank(A: np.ndarray, rtol: float) -> int:
    if A.size == 0 or min(A.shape) == 0:
        return 0
    s = np.linalg.svd(A, compute_uv=False)
    tol = rtol * (s[0] if s.size else 1.0)
    return int(np.sum(s > tol))


def as_block(value, n_obs: int) -> np.ndarray:
    if value is None or value == []:
        return np.zeros((n_obs, 0))
    A = np.asarray(value, dtype=float)
    if A.ndim == 1:
        A = A.reshape(n_obs, 1)
    if A.shape[0] != n_obs:
        raise ValueError(f"block has {A.shape[0]} rows, expected {n_obs}")
    return A


def validate(payload: dict) -> dict:
    b_full = np.asarray(payload["v_beta"], dtype=float)
    if b_full.ndim != 1:
        raise ValueError("v_beta must be one-dimensional")
    n_obs = b_full.size
    rtol = float(payload.get("svd_rtol", 1e-12))
    error_bound = float(payload.get("error_bound", 0.0))

    H_raw = payload.get("H", [])
    H = np.asarray(H_raw, dtype=float) if H_raw != [] else np.zeros((0, n_obs))
    if H.ndim == 1:
        H = H.reshape(1, -1)
    if H.shape[1] != n_obs:
        raise ValueError("H must have n_obs columns")

    Q = nullspace(H, rtol)
    b = Q.T @ b_full

    reduced_blocks = {}
    pieces = []
    for name, raw in payload.get("blocks", {}).items():
        A = as_block(raw, n_obs)
        Ared = Q.T @ A
        reduced_blocks[name] = Ared
        if Ared.shape[1]:
            pieces.append(Ared)

    M = np.concatenate(pieces, axis=1) if pieces else np.zeros((Q.shape[1], 0))
    rank_M = matrix_rank(M, rtol)
    Mb = np.column_stack([M, b])
    rank_aug = matrix_rank(Mb, rtol)

    if M.shape[1]:
        pinv = np.linalg.pinv(M, rcond=rtol)
        residual = b - M @ (pinv @ b)
    else:
        residual = b.copy()

    residual_norm = float(np.linalg.norm(residual))
    novelty_by_rank = rank_aug > rank_M
    above_error = residual_norm > error_bound

    # Map residual back to the original observable coordinates for selector diagnostics.
    residual_full = Q @ residual
    sym_indices = [int(i) for i in payload.get("sym_indices", [])]
    ord_indices = [int(i) for i in payload.get("ordered_indices", [])]
    sym_norm = float(np.linalg.norm(residual_full[sym_indices])) if sym_indices else None
    ord_norm = float(np.linalg.norm(residual_full[ord_indices])) if ord_indices else None

    return {
        "n_observables": n_obs,
        "hard_constraint_rank": matrix_rank(H, rtol),
        "allowed_tangent_dimension": int(Q.shape[1]),
        "combined_comparator_rank": rank_M,
        "augmented_rank_with_candidate": rank_aug,
        "candidate_adds_rank": novelty_by_rank,
        "residual_norm": residual_norm,
        "error_bound": error_bound,
        "residual_above_error_bound": above_error,
        "symmetric_residual_norm": sym_norm,
        "ordered_residual_norm": ord_norm,
        "algebraic_gate": "PASS" if novelty_by_rank and above_error else "FAIL_OR_BLOCKED",
        "warning": "This is an algebraic pre-Fisher certificate only; it does not establish physical consistency, likelihood identifiability, or resource closure."
    }


def self_test() -> dict:
    # Four toy observables. H fixes the first coordinate tangent to zero.
    # Comparator spans coordinates 2 and 3; candidate A is contained, candidate B adds ordered coordinate 4.
    base = {
        "H": [[1, 0, 0, 0]],
        "blocks": {
            "C3": [[0], [1], [0], [0]],
            "C4": [[0], [0], [1], [0]],
        },
        "error_bound": 1e-12,
        "svd_rtol": 1e-12,
        "sym_indices": [1],
        "ordered_indices": [2, 3],
    }
    contained = dict(base, v_beta=[0, 2, 3, 0])
    residual = dict(base, v_beta=[0, 2, 3, 1])
    return {
        "contained_example": validate(contained),
        "rank_adding_example": validate(residual),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", help="JSON quotient specification")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test or not args.input:
        result = self_test()
    else:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        result = validate(payload)

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
