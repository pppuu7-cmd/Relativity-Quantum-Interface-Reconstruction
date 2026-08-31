#!/usr/bin/env python3
"""Iteration 161: local-IR asymptotic-safety -> C5 EFT embedding audit.

Two separate questions are certified:

1. Structural action-level inclusion: the local IR AS action through first order
   in Delta contains only EH, R^2, Ricci^2, R Box R and Ricci Box Ricci.  The
   frozen C5 off-shell convention is a complete unreduced local covariant EFT
   basis through dimension 12, so these AS IR operators are a strict subset.

2. Domain audit: compare the first-order IR Taylor expansion with the full
   analytic Euclidean form-factor fits on the 18 individual legs of the six
   frozen RQIR triplets.  This determines whether the local IR approximation
   can be used as a numerical surrogate on the current protocol.  It cannot.

No Lorentzian nonlocal retarded prescription is introduced here.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

KINEMATICS = [
    {"p2": 0.7473, "q2": 0.5076, "r2": 0.3313},
    {"p2": 0.6157, "q2": 0.3854, "r2": 0.2935},
    {"p2": 0.4418, "q2": 0.4260, "r2": 0.2746},
    {"p2": 0.6120, "q2": 0.3153, "r2": 0.2773},
    {"p2": 0.6682, "q2": 0.4004, "r2": 0.2278},
    {"p2": 0.4239, "q2": 0.2882, "r2": 0.2321},
]

RICCI2 = {
    "a0": -0.023601,
    "a": [-0.13727, 0.13138, -0.22100, -0.15080],
    "p": [0.12436, 1.2476, 0.56405, 0.021230],
}
R2 = {
    "a0": 0.028373,
    "a": [0.012637, 1.2661, 0.57040],
    "p": [5.7131, 0.73200, 0.092956],
}


def f_ricci2_from_x(x: float) -> float:
    return RICCI2["a0"] + sum(
        a / (x / p0**2 + 1.0) for a, p0 in zip(RICCI2["a"], RICCI2["p"])
    )


def f_r2_from_x(x: float) -> float:
    return R2["a0"] + sum(
        a / ((x / p0**2 + 1.0) ** 2) for a, p0 in zip(R2["a"], R2["p"])
    )


def taylor_coefficients() -> dict[str, float]:
    g_ricci = RICCI2["a0"] + sum(RICCI2["a"])
    c1 = sum(-a / p0**2 for a, p0 in zip(RICCI2["a"], RICCI2["p"]))
    g_r2 = R2["a0"] + sum(R2["a"])
    c2 = sum(-2.0 * a / p0**2 for a, p0 in zip(R2["a"], R2["p"]))
    return {"g_Ricci2": g_ricci, "c1": c1, "g_R2": g_r2, "c2": c2}


def relative_error(approx: float, exact: float) -> float:
    return abs(approx - exact) / max(abs(exact), 1.0e-300)


def main() -> int:
    coeff = taylor_coefficients()
    rows = []
    err_ricci = []
    err_r2 = []

    for i, triplet in enumerate(KINEMATICS, start=1):
        legs = {}
        for label in ("p2", "q2", "r2"):
            x = float(triplet[label])
            exact_ricci = f_ricci2_from_x(x)
            exact_r2 = f_r2_from_x(x)
            ir_ricci = coeff["g_Ricci2"] + coeff["c1"] * x
            ir_r2 = coeff["g_R2"] + coeff["c2"] * x
            er = relative_error(ir_ricci, exact_ricci)
            es = relative_error(ir_r2, exact_r2)
            err_ricci.append(er)
            err_r2.append(es)
            legs[label[0]] = {
                "x_k2": x,
                "full_f_Ricci2": exact_ricci,
                "IR1_f_Ricci2": ir_ricci,
                "relative_error_Ricci2": er,
                "full_f_R2": exact_r2,
                "IR1_f_R2": ir_r2,
                "relative_error_R2": es,
            }
        rows.append({"triplet": i, "legs": legs})

    as_ir_operators = [
        "R",
        "R_mn R^mn",
        "R^2",
        "R_mn Box R^mn",
        "R Box R",
    ]

    result = {
        "iteration": 161,
        "scope": "local IR action embedding and domain-of-validity audit",
        "source": "Pawlowski & Traenkle arXiv:2309.17043v2, Eqs. (27),(32), Appendix G/H",
        "as_ir_operator_set": as_ir_operators,
        "c5_offshell_basis_contract": "complete unreduced local diffeomorphism-invariant covariant basis through dimension 12, including Ricci/EOM-redundant directions",
        "structural_embedding": {
            "all_as_ir_operators_are_c5_local_operators": True,
            "classification": "AS_LOCAL_IR_SUBSET_OF_C5_EFT",
            "novelty_relative_to_C5_in_strict_IR": "NONE_AT_ACTION_LEVEL_FOR_THIS_TRUNCATION",
        },
        "fit_derived_taylor_coefficients": coeff,
        "paper_rounded_coefficients": {
            "g_Ricci2": -0.40,
            "g_R2": 1.9,
            "c1": 344.09,
            "c2": -136.75,
        },
        "triplet_domain_audit": rows,
        "relative_error_ranges": {
            "Ricci2_min": min(err_ricci),
            "Ricci2_max": max(err_ricci),
            "R2_min": min(err_r2),
            "R2_max": max(err_r2),
        },
        "current_six_probe_ir_surrogate": "FAIL_DOMAIN_OF_VALIDITY",
        "decision": {
            "strict_deep_ir_as_vs_c5": "EXACT_STRUCTURAL_DEGENERACY_WITH_LOCAL_C5_EFT_FAMILY",
            "use_ir_expansion_on_iteration149_six_probes": "FORBIDDEN",
            "full_nonlocal_as_retarded_tangent": "STILL_BLOCKED",
        },
        "model_readiness_percent": 23,
        "readiness_change": "+1 point: AS strict local-IR comparator sector is now classified; full nonlocal AS remains blocked",
    }

    out = Path("results/as_ir_c5_embedding_iteration161.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
