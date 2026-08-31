#!/usr/bin/env python3
"""Iteration 159: protocol-compatibility audit for a fixed AS vertex truncation.

Comparator authority: Pawlowski & Traenkle, Phys. Rev. D 110, 086011 (2024),
arXiv:2309.17043. Their TT n-point coefficient used for reconstruction is
parameterised at the momentum-symmetric point. This script quantifies whether
the six frozen RQIR off-shell triplets can be evaluated directly with that
one-variable symmetric-point dressing. They cannot.
"""
from __future__ import annotations

import json
import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])

QS = [np.array(x, float) for x in [
    [0.18,0.70,0.20,0.10], [0.14,0.55,-0.25,0.20], [0.22,0.62,0.18,-0.24],
    [0.16,0.48,0.31,0.12], [0.20,0.58,-0.16,-0.28], [0.12,0.44,0.27,-0.19],
]]
RS = [np.array(x, float) for x in [
    [0.11,-0.21,0.52,0.17], [0.09,0.24,0.46,-0.18], [0.10,-0.18,0.41,0.29],
    [0.13,0.22,-0.37,0.33], [0.08,0.26,0.35,0.21], [0.15,-0.20,0.39,0.25],
]]


def k2(k: np.ndarray) -> float:
    return float(k @ ETA @ k)


rows = []
for i, (q, r) in enumerate(zip(QS, RS)):
    p = q + r
    vals = np.array([k2(p), k2(q), k2(r)], dtype=float)
    mean = float(vals.mean())
    spread = float((vals.max() - vals.min()) / mean)
    rows.append({
        "probe": i,
        "p2": float(vals[0]),
        "q2": float(vals[1]),
        "r2": float(vals[2]),
        "relative_squared_momentum_spread": spread,
        "symmetric_point_compatible": bool(np.allclose(vals, vals.mean(), rtol=1e-10, atol=1e-12)),
    })

spreads = [row["relative_squared_momentum_spread"] for row in rows]

out = {
    "iteration": 159,
    "comparator_id": "AS-PT-001",
    "authority": "Pawlowski & Traenkle, Phys.Rev.D 110, 086011 (2024), arXiv:2309.17043",
    "fixed_truncation_scope": {
        "background_effective_action": "curvature expansion through R^2 and Ricci_mn^2 with full covariant momentum dependence",
        "fluctuation_input": "fully dressed TT 2-, 3-, 4-graviton correlation functions within the stated vertex truncation",
        "three_point_projection": "completely TT coefficient gamma_g^(3)(p) at the momentum-symmetric point",
        "known_tensor_selection": "R^2 has zero TT 3-point overlap; Ricci_mn^2 has nonzero TT 3-point overlap",
    },
    "frozen_rqir_probe_test": {
        "rows": rows,
        "min_relative_squared_momentum_spread": min(spreads),
        "max_relative_squared_momentum_spread": max(spreads),
        "n_symmetric_compatible": sum(int(row["symmetric_point_compatible"]) for row in rows),
        "n_probes": len(rows),
    },
    "decision": "BLOCKED_OFF_SYMMETRIC_RETARDED_VERTEX_MAP",
    "supported_claims": [
        "A concrete finite AS vertex truncation is now frozen as comparator authority.",
        "Its published symmetric-point TT 3-point dressing cannot be directly evaluated on the six frozen non-symmetric RQIR triplets.",
        "R^2 is TT-3pt blind in this truncation whereas Ricci^2 contributes, so the tensor/operator content is sufficiently specific to localise the missing map.",
    ],
    "blocked": {
        "six_probe_chi2R_tangent": "BLOCKED_OFF_SYMMETRIC_VERTEX_DATA_OR_RECONSTRUCTION",
        "lorentzian_retarded_map": "BLOCKED_CTP_RETARDED_CONTINUATION_IN_SAME_PURE_GRAVITON_TRUNCATION",
        "full_AS_quotient": "BLOCKED",
    },
    "retained_results": {
        "AS_NG_001": "SYMMETRIC_POINT_VERTEX_NOT_GENERAL_OFFSHELL_TANGENT",
        "NG_FUNNEL_016": "FIXED_TRUNCATION_STILL_REQUIRES_KINEMATIC_AND_CAUSAL_MAP_BEFORE_ENTERING_RQIR_QUOTIENT",
    },
    "nonclaims": [
        "This is not a consistency failure of asymptotic safety.",
        "No missing off-symmetric or Lorentzian entries are set to zero.",
        "The 2026 Lorentzian two-point spectral results and scalar-scattering continuation are separate calculations and are not spliced into AS-PT-001 as if they were the same truncation.",
    ],
}

print(json.dumps(out, indent=2, sort_keys=True))
