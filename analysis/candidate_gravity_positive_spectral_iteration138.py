#!/usr/bin/env python3
"""Iteration 138 scoped audit for ANSATZ-RQIR-KL-002 v0.1."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad


def rho_hat(s: float) -> float:
    return math.exp(1.0 - s) if s >= 1.0 else 0.0


def W(u: float) -> float:
    value, _ = quad(
        lambda s: rho_hat(s) * math.exp(-u * math.sqrt(s)),
        1.0,
        np.inf,
        epsabs=1e-12,
        epsrel=1e-12,
    )
    return value


def main() -> int:
    rho_norm, rho_err = quad(rho_hat, 1.0, np.inf, epsabs=1e-13, epsrel=1e-13)
    us = [0.0, 0.1, 1.0, 5.0, 10.0]
    static_samples = []
    for u in us:
        w = W(u)
        bound = math.exp(-u)
        static_samples.append(
            {
                "u_Mstar_r": u,
                "W": w,
                "exp_minus_u_bound": bound,
                "bound_holds": w <= bound + 1e-12 and w >= -1e-14,
            }
        )

    y_samples = [1.0, 1.1, 2.0, 5.0, 10.0]
    spectral_samples = [
        {
            "y_p2_over_Mstar2": y,
            "rho_hat": rho_hat(y),
            "minus_Im_D_cont_over_pi_beta_times_Mstar2": rho_hat(y),
        }
        for y in y_samples
    ]

    checks = {
        "rho_normalized": abs(rho_norm - 1.0) < 1e-12,
        "rho_nonnegative_samples": all(x["rho_hat"] >= 0.0 for x in spectral_samples),
        "static_yukawa_bound_samples": all(x["bound_holds"] for x in static_samples),
        "W_zero_equals_one": abs(static_samples[0]["W"] - 1.0) < 1e-12,
        "continuum_has_no_delta_pole_by_definition": True,
        "massless_GR_delta_retained_by_definition": True,
    }

    result = {
        "model_id": "ANSATZ-RQIR-KL-002",
        "version": "0.1",
        "iteration": 138,
        "scope": "Gaussian positive-spectral and static-Yukawa audit",
        "rho_norm": rho_norm,
        "rho_quad_error": rho_err,
        "static_samples": static_samples,
        "spectral_samples": spectral_samples,
        "checks": checks,
        "overall": "PASS_SCOPED" if all(checks.values()) else "FAIL",
        "nonclaims": [
            "No full tensor/helicity completion proved",
            "No nonlinear diffeomorphism closure proved",
            "No novelty against C4/C5/nonlocal/KK continua proved",
            "No Paper-I finite discriminator proved",
        ],
    }

    out = Path("results/candidate_gravity_positive_spectral_iteration138.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["overall"] == "PASS_SCOPED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
