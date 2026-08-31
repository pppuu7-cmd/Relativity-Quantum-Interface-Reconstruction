#!/usr/bin/env python3
"""Iteration 160: asymptotic-safety action/form-factor coverage audit.

Scope
-----
This script evaluates the analytic Euclidean curvature-squared form-factor fits
reported by Pawlowski & Traenkle (arXiv:2309.17043 / PRD 110, 086011) on the
individual spacelike leg virtualities of the six frozen RQIR triplets from
Iteration 149.

It deliberately does NOT construct a Lorentzian retarded three-point vertex,
chi^(2)R, or an AS novelty tangent.  The source paper reconstructs a Euclidean
covariant effective action and discusses a Wick rotation/nonlocal Green-function
problem, but does not freeze the in-in/CTP retarded prescription required by
RQIR.  The output is therefore an action-data coverage diagnostic only.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

# Frozen Lorentzian spacelike invariants from
# results/c5_source_completed_protocol_iteration149.json.
# With signature (-,+,+,+), every leg is spacelike and k_L^2 > 0.  Under the
# flat-space Euclidean correspondence used only for this coverage diagnostic,
# the positive Euclidean momentum magnitude is sqrt(k_L^2).
KINEMATICS = [
    {"p2": 0.7473, "q2": 0.5076, "r2": 0.3313},
    {"p2": 0.6157, "q2": 0.3854, "r2": 0.2935},
    {"p2": 0.4418, "q2": 0.4260, "r2": 0.2746},
    {"p2": 0.6120, "q2": 0.3153, "r2": 0.2773},
    {"p2": 0.6682, "q2": 0.4004, "r2": 0.2278},
    {"p2": 0.4239, "q2": 0.2882, "r2": 0.2321},
]

# Appendix-H analytic fits in arXiv:2309.17043v2.
# f_Ricci2(p^2) = a0 + sum_i ai / ((p/pi)^2 + 1)
RICCI2 = {
    "a0": -0.023601,
    "a": [-0.13727, 0.13138, -0.22100, -0.15080],
    "p": [0.12436, 1.2476, 0.56405, 0.021230],
}

# f_R2(p^2) = a0 + sum_i ai / (((p/pi)^2 + 1)^2)
R2 = {
    "a0": 0.028373,
    "a": [0.012637, 1.2661, 0.57040],
    "p": [5.7131, 0.73200, 0.092956],
}


def f_ricci2(p: float) -> float:
    return RICCI2["a0"] + sum(
        a / ((p / p0) ** 2 + 1.0) for a, p0 in zip(RICCI2["a"], RICCI2["p"])
    )


def f_r2(p: float) -> float:
    return R2["a0"] + sum(
        a / (((p / p0) ** 2 + 1.0) ** 2) for a, p0 in zip(R2["a"], R2["p"])
    )


def main() -> int:
    rows = []
    ricci_values = []
    r2_values = []

    for i, triplet in enumerate(KINEMATICS, start=1):
        legs = {}
        for leg in ("p2", "q2", "r2"):
            k2 = float(triplet[leg])
            p_e = math.sqrt(k2)
            fr = f_ricci2(p_e)
            fs = f_r2(p_e)
            ricci_values.append(fr)
            r2_values.append(fs)
            legs[leg[0]] = {
                "lorentzian_spacelike_k2": k2,
                "euclidean_momentum_magnitude": p_e,
                "f_Ricci2": fr,
                "f_R2": fs,
            }
        rows.append({"triplet": i, "legs": legs})

    result = {
        "iteration": 160,
        "scope": "Euclidean AS curvature-squared form-factor coverage diagnostic only; not a retarded RQIR tangent",
        "source": {
            "paper": "Pawlowski & Traenkle, arXiv:2309.17043v2 / Phys. Rev. D 110, 086011 (2024)",
            "input_protocol": "results/c5_source_completed_protocol_iteration149.json",
            "fit_policy": "Appendix-H analytic fits evaluated independently on every spacelike leg",
        },
        "fit_coefficients": {"Ricci2": RICCI2, "R2": R2},
        "triplets": rows,
        "ranges": {
            "f_Ricci2_min": min(ricci_values),
            "f_Ricci2_max": max(ricci_values),
            "f_R2_min": min(r2_values),
            "f_R2_max": max(r2_values),
        },
        "decision": {
            "euclidean_action_data": "SUPPORTED_WITHIN_FROZEN_CURVATURE_SQUARED_TRUNCATION",
            "off_symmetric_euclidean_vertex_in_principle": "DERIVABLE_FROM_ACTION",
            "lorentzian_retarded_green_function_prescription": "BLOCKED",
            "six_probe_chi2R_even_odd": "NOT_COMPUTED",
            "as_rqir_tangent": "NOT_COMPUTED",
            "classification": "BLOCKED_AS_RETARDED_GREEN_FUNCTION_PRESCRIPTION",
        },
        "nonclaims": [
            "No Euclidean form-factor value is treated as a Lorentzian retarded response.",
            "No interpolation of the published symmetric-point three-graviton dressing is used.",
            "No blocked AS coordinate is set to zero.",
            "This is not a consistency failure of asymptotic safety.",
        ],
        "model_readiness_percent": 22,
    }

    out = Path("results/as_action_formfactor_audit_iteration160.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
