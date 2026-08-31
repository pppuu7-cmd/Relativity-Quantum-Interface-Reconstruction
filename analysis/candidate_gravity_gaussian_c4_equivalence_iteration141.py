#!/usr/bin/env python3
"""Iteration 141 Gaussian C4/KK equivalence audit for ANSATZ-RQIR-KL-002.

For rho_hat(s)=exp(1-s), set s=1+t. Then the continuum integral is
an e^{-t}-weighted direct integral of ordinary massive propagators. Gauss-Laguerre
quadrature gives a positive discrete mediator approximation whose covariance converges
to the KL continuum. The exact theorem is the spectral direct-integral identity; the
numerics only illustrate it.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.laguerre import laggauss
from scipy.integrate import quad


def exact_c(x: float) -> float:
    return quad(lambda t: math.exp(-t) / (1.0 + t + x), 0.0, np.inf,
                epsabs=1e-13, epsrel=1e-13)[0]


def discrete_c(x: float, n: int) -> float:
    nodes, weights = laggauss(n)
    # Positive mediator weights weights_i and masses^2/M_*^2=1+nodes_i.
    return float(np.sum(weights / (1.0 + nodes + x)))


def main() -> int:
    xs = [0.1, 1.0, 10.0]
    ns = [4, 8, 16, 32]
    samples = []
    for x in xs:
        ex = exact_c(x)
        approximations = []
        for n in ns:
            val = discrete_c(x, n)
            approximations.append({
                "N_positive_mediators": n,
                "value": val,
                "abs_error": abs(val - ex),
            })
        samples.append({"x": x, "exact_continuum": ex, "approximations": approximations})

    result = {
        "model_id": "ANSATZ-RQIR-KL-002",
        "iteration": 141,
        "scope": "Gaussian linear spectral equivalence to a positive continuum/discrete tower of ordinary massive spin-2 mediators",
        "exact_identity": (
            "h = h_massless + sqrt(beta) direct_integral ds sqrt(rho_hat(s)) H_s; "
            "for independent Gaussian H_s, <hh> = D_GR + beta int ds rho_hat(s) D_s"
        ),
        "influence_functional_consequence": (
            "With linear conserved-stress coupling, identical D_R and D_H imply an identical Gaussian CTP influence functional and therefore identical linear-Gaussian RQIR likelihoods."
        ),
        "samples": samples,
        "funnel_result": "FAIL_QG007_EXACT_GAUSSIAN_C4_KK_DEGENERACY",
        "decision": "RETAIN_AS_REFERENCE_CONTROL_NOT_PROMOTABLE",
        "required_escape": (
            "A future candidate must add derived nonlinear/non-Gaussian gravitational self-consistency or another observable relation that cannot be reproduced by an ordinary mediator continuum."
        ),
        "overall": "PASS_NEGATIVE_RESULT",
    }

    out = Path("results/candidate_gravity_gaussian_c4_equivalence_iteration141.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
