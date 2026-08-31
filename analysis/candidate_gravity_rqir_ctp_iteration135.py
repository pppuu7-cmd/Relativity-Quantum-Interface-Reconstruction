#!/usr/bin/env python3
"""Iteration 135 scoped audit for ANSATZ-RQIR-CTP-001.

This is deliberately a Euclidean/spacelike kernel audit only. It does not claim
Lorentzian unitarity, ghost freedom, microcausality, or novelty.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.special import exp1


def rho_hat(s: float) -> float:
    if s < 1.0:
        return 0.0
    return math.exp(1.0 - s)


def f_e(x):
    """Spacelike form factor F_E(x)=x exp(1+x) E1(1+x), x>=0."""
    x = np.asarray(x, dtype=float)
    return x * np.exp(1.0 + x) * exp1(1.0 + x)


def main() -> int:
    rho_norm, rho_err = quad(rho_hat, 1.0, np.inf, epsabs=1e-13, epsrel=1e-13)
    a1 = math.e * float(exp1(1.0))

    xs = np.concatenate(([0.0], np.logspace(-8, 2, 161)))
    vals = f_e(xs)
    upper = xs / (1.0 + xs)

    positivity_margin = float(np.min(vals))
    upper_violation = float(np.max(vals - upper))

    beta_grid = [0.0, 1e-3, 0.1, 1.0, 10.0]
    kernel_min_all = {
        f"{beta:g}": float(np.min(1.0 + beta * vals)) for beta in beta_grid
    }
    kernel_min_nonzero_x = {
        f"{beta:g}": float(np.min(1.0 + beta * vals[1:])) for beta in beta_grid
    }

    x_ir = 1e-8
    ir_ratio = float(f_e(np.array([x_ir]))[0] / x_ir)

    checks = {
        "spectral_density_normalized": abs(rho_norm - 1.0) < 1e-12,
        "form_factor_nonnegative_on_grid": positivity_margin >= -1e-14,
        "analytic_upper_bound_holds_on_grid": upper_violation <= 1e-13,
        "kernel_factor_no_spacelike_zero_for_test_betas": all(
            value >= 1.0 - 1e-13 for value in kernel_min_all.values()
        ),
        "infrared_slope_matches_eE1": abs(ir_ratio - a1) < 1e-7,
    }

    result = {
        "model_id": "ANSATZ-RQIR-CTP-001",
        "iteration": 135,
        "scope": "Euclidean/spacelike positive-spectral-kernel audit",
        "rho_norm": rho_norm,
        "rho_quad_error": rho_err,
        "A1_e_E1_1": a1,
        "IR_ratio_at_x_1e-8": ir_ratio,
        "grid_x_min": float(xs.min()),
        "grid_x_max": float(xs.max()),
        "grid_points": int(xs.size),
        "F_E_max_on_grid": float(vals.max()),
        "max_upper_bound_violation": upper_violation,
        "kernel_min_all_x": kernel_min_all,
        "kernel_min_nonzero_x": kernel_min_nonzero_x,
        "checks": checks,
        "overall": "PASS_SCOPED" if all(checks.values()) else "FAIL",
        "nonclaims": [
            "No Lorentzian pole/branch-sheet audit performed",
            "No microscopic unitary dilation proved",
            "No nonlinear diffeomorphism closure proved",
            "No comparator novelty proved",
        ],
    }

    out = Path("results/candidate_gravity_rqir_ctp_iteration135.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["overall"] == "PASS_SCOPED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
