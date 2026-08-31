#!/usr/bin/env python3
"""Iteration 136 Lorentzian sub-threshold pole audit for ANSATZ-RQIR-CTP-001 v0.1.

The analytic theorem is stronger than the numerical samples:
for every beta>0 the frozen v0.1 form factor produces exactly one additional
real timelike zero below the spectral threshold. The residue of the scalarized
spin-2 propagator at that zero has the opposite sign to the GR pole in the
frozen multiplicative convention.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq
from scipy.special import exp1


def f_below(y: float) -> float:
    """F_R for positive-frequency timelike 0<y=p^2/M_*^2<1 (real below cut)."""
    return -y * np.exp(1.0 - y) * exp1(1.0 - y)


def dfdy_below(y: float) -> float:
    """Exact derivative dF/dy on 0<y<1."""
    a = 1.0 - y
    h = np.exp(a) * exp1(a)
    # g(y)=y h(1-y), F=-g; dh(1-y)/dy = 1/a-h >0
    gp = h + y * (1.0 / a - h)
    return -gp


def root_for_beta(beta: float) -> float:
    fn = lambda y: 1.0 + beta * f_below(y)
    # For beta >= 0.1 the root is numerically resolvable in double precision.
    return brentq(fn, 1.0e-14, 1.0 - 1.0e-14, xtol=1.0e-14, rtol=1.0e-14)


def main() -> int:
    betas = [0.1, 1.0, 10.0]
    samples = []
    for beta in betas:
        y0 = root_for_beta(beta)
        slope = dfdy_below(y0)
        relative_residue_factor = 1.0 / (y0 * beta * slope)
        samples.append(
            {
                "beta": beta,
                "y0_p2_over_Mstar2": y0,
                "distance_to_threshold_1_minus_y0": 1.0 - y0,
                "dF_dy_at_root": slope,
                "relative_residue_factor": relative_residue_factor,
            }
        )

    theorem_checks = {
        "F_at_zero": 0.0,
        "F_negative_for_0_lt_y_lt_1": True,
        "F_tends_to_minus_infinity_as_y_to_1_minus": True,
        "dF_dy_strictly_negative_for_0_lt_y_lt_1": True,
        "unique_root_of_1_plus_beta_F_for_every_beta_gt_0": True,
        "extra_pole_residue_opposite_sign": True,
    }

    result = {
        "model_id": "ANSATZ-RQIR-CTP-001",
        "version": "0.1",
        "iteration": 136,
        "scope": "positive-frequency timelike sub-threshold Lorentzian pole audit",
        "analytic_statement": (
            "For y=p^2/M_*^2 in (0,1), F(y)=-y exp(1-y) E1(1-y) is continuous, "
            "strictly decreasing from 0 to -infinity. Hence for every beta>0, "
            "1+beta F(y) has exactly one zero y0 in (0,1). Since dF/dy<0, the "
            "scalarized dressed-pole residue factor 1/[y0 beta F'(y0)] is negative."
        ),
        "small_beta_threshold_asymptotic": "1-y0 ~ exp(-EulerGamma-1/beta)",
        "samples": samples,
        "theorem_checks": theorem_checks,
        "overall": "FAIL_QG004_EXTRA_NEGATIVE_RESIDUE_POLE",
        "decision": "REJECT_V0.1",
        "nonclaims": [
            "This rejects the frozen v0.1 sign/domain, not all spectral/nonlocal gravity models.",
            "No claim is made that every additional pole in every convention is a ghost; the sign statement is relative to the frozen GR pole convention used by this ansatz.",
        ],
    }

    out = Path("results/candidate_gravity_lorentzian_iteration136.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
