#!/usr/bin/env python3
"""Iteration 140 low-energy C5/EFT degeneracy audit for ANSATZ-RQIR-KL-002.

The candidate-specific positive continuum is analytic for Euclidean x=q^2/M_*^2<1:
C(x)=int_1^infty rho(s)/(s+x) ds = sum_n (-x)^n A_{n+1}.
At any finite derivative order, these coefficients are indistinguishable from local EFT
Wilson coefficients unless the full threshold/nonanalytic structure is resolved.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad


def rho(s: float) -> float:
    return math.exp(1.0 - s) if s >= 1.0 else 0.0


def moment(k: int) -> float:
    return quad(lambda s: rho(s) / (s**k), 1.0, np.inf, epsabs=1e-12, epsrel=1e-12)[0]


def exact_c(x: float) -> float:
    return quad(lambda s: rho(s) / (s + x), 1.0, np.inf, epsabs=1e-12, epsrel=1e-12)[0]


def trunc_c(x: float, max_n: int, moments: list[float]) -> float:
    return sum(((-x) ** n) * moments[n] for n in range(max_n + 1))


def main() -> int:
    # moments[n] = A_{n+1}
    moments = [moment(k) for k in range(1, 6)]
    xs = [0.01, 0.1, 0.3, 0.5]
    samples = []
    for x in xs:
        exact = exact_c(x)
        approx = {}
        for n in range(5):
            val = trunc_c(x, n, moments)
            approx[f"through_x^{n}"] = {
                "value": val,
                "relative_error": abs(val - exact) / abs(exact),
            }
        samples.append({"x": x, "exact": exact, "series": approx})

    result = {
        "model_id": "ANSATZ-RQIR-KL-002",
        "iteration": 140,
        "scope": "below-threshold analytic expansion and finite-order EFT degeneracy",
        "moments_A1_to_A5": moments,
        "analytic_identity": "C(x)=sum_{n>=0}(-x)^n A_{n+1} for |x|<1",
        "funnel_result": "DEGENERATE_WITH_LOCAL_C5_EFT_AT_ANY_FIXED_FINITE_DERIVATIVE_ORDER_BELOW_THRESHOLD",
        "required_escape": "resolve the full threshold/nonanalytic shape near p^2~M_*^2 or use linked observables not independently absorbable into EFT/nuisance coefficients",
        "samples": samples,
        "overall": "PASS_NEGATIVE_RESULT",
    }

    out = Path("results/candidate_gravity_c5_ir_degeneracy_iteration140.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
