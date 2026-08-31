#!/usr/bin/env python3
"""Iteration 160: action-level sufficiency audit for AS-FRG-TT-001.

Uses the analytic form-factor fits published in Pawlowski & Traenkle,
Phys. Rev. D 110, 086011 (2024), Appendix H, and evaluates them on the six
frozen RQIR output virtualities. This is an Euclidean action-data audit only.
It deliberately does NOT invent a Lorentzian retarded prescription for the
inverse differential operators appearing after Wick rotation.
"""
from __future__ import annotations

import json
import numpy as np

P2 = np.array([0.7473, 0.6157, 0.4418, 0.6120, 0.6682, 0.4239], dtype=float)
P = np.sqrt(P2)

# Published analytic fit: f_Ricci2(p^2)=a0+sum_i a_i/( (p/p_i)^2 + 1 )
RICCI_A0 = -0.023601
RICCI_A = np.array([-0.13727, 0.13138, -0.22100, -0.15080], dtype=float)
RICCI_PI = np.array([0.12436, 1.2476, 0.56405, 0.021230], dtype=float)

# Published analytic fit: f_R2(p^2)=a0+sum_i a_i/( ((p/p_i)^2 + 1)^2 )
R2_A0 = 0.028373
R2_A = np.array([0.012637, 1.2661, 0.57040], dtype=float)
R2_PI = np.array([5.7131, 0.73200, 0.092956], dtype=float)


def f_ricci2(p: float) -> float:
    return float(RICCI_A0 + np.sum(RICCI_A / ((p / RICCI_PI) ** 2 + 1.0)))


def f_r2(p: float) -> float:
    return float(R2_A0 + np.sum(R2_A / (((p / R2_PI) ** 2 + 1.0) ** 2)))


fRic = np.array([f_ricci2(p) for p in P])
fR2 = np.array([f_r2(p) for p in P])

out = {
    "iteration": 160,
    "comparator_id": "AS-FRG-TT-001",
    "scope": "Euclidean reconstructed curvature-squared action/form-factor sufficiency audit; not a Lorentzian retarded tangent",
    "published_action_data": {
        "curvature_truncation": "Rcal(Delta,R) + R f_R2(Delta) R + Ric_mn f_Ricci2(Delta) Ric^mn",
        "ricci2_fit": {
            "a0": RICCI_A0,
            "a": RICCI_A.tolist(),
            "p_i": RICCI_PI.tolist(),
            "functional_form": "a0 + sum a_i / ((p/p_i)^2+1)",
        },
        "R2_fit": {
            "a0": R2_A0,
            "a": R2_A.tolist(),
            "p_i": R2_PI.tolist(),
            "functional_form": "a0 + sum a_i / (((p/p_i)^2+1)^2)",
        },
        "mapping_caveat": "background/fluctuation reconstruction uses an approximated Nielsen-identity map and a curvature-squared truncation",
    },
    "six_probe_euclidean_values": {
        "p2": P2.tolist(),
        "f_Ricci2": fRic.tolist(),
        "f_R2": fR2.tolist(),
        "f_Ricci2_min": float(fRic.min()),
        "f_Ricci2_max": float(fRic.max()),
        "f_R2_min": float(fR2.min()),
        "f_R2_max": float(fR2.max()),
    },
    "sufficiency": {
        "finite_euclidean_action_level_form_factors": "SUPPORTED",
        "off_symmetric_euclidean_vertex_in_principle": "SUPPORTED_WITHIN_FROZEN_CURVATURE_SQUARED_TRUNCATION",
        "six_probe_lorentzian_retarded_chi2R": "BLOCKED_CAUSAL_OPERATOR_PRESCRIPTION",
        "source_completed_CTP_map": "BLOCKED",
    },
    "causal_obstruction": {
        "wick_rotation_used_in_source": "Delta -> Box",
        "inverse_operator_issue": "analytic form-factor fits become inverse Lorentzian differential operators and require a Green-function/boundary prescription",
        "source_discussion": "paper discusses Green-function construction, including expansion around a flat-space Feynman propagator, and leaves fuller treatment to future work",
        "RQIR_requirement": "ordered response requires a retarded/in-in/CTP prescription fixed in the same comparator",
    },
    "retained_results": {
        "AS_NG_002": "EUCLIDEAN_ACTION_RECONSTRUCTION_DOES_NOT_FIX_RETARDED_GREEN_PRESCRIPTION",
        "NG_FUNNEL_017": "COVARIANT_NONLOCAL_ACTION_REQUIRES_CAUSAL_OPERATOR_PRESCRIPTION_FOR_ORDERED_RQIR_RESPONSE",
    },
    "decision": "ACTION_DATA_EUCLIDEAN_SUPPORTED__RETARDED_RQIR_BLOCKED",
    "model_readiness_percent": 22,
    "nonclaims": [
        "No consistency failure of asymptotic safety is inferred.",
        "No inverse-fit denominator is interpreted as a physical particle pole without a spectral/causal analysis.",
        "No unavailable retarded or CTP entry is set to zero.",
    ],
}

print(json.dumps(out, indent=2, sort_keys=True))
