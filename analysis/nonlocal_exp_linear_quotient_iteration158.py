#!/usr/bin/env python3
"""Iteration 158: finite linear TT quotient for QG-NL-EXP-001.

Comparator:
  S = Mpl^2/2 int sqrt(-g) [ R + G_mn F(Box) R^mn ] + S_m[g]
  F(Box) = (exp(-Box/M^2)-1)/Box.

Around Minkowski in the spin-2 TT sector, with x=k^2>0 on the frozen
spacelike probes, the linear response is normalized as
  chi_NL(x; lambda) = exp(-lambda*x)/x, lambda=1/M^2.

The frozen C5 local quadratic EFT through operator dimension 12 supplies one
spin-2 response tangent per R_mn Box^n R^mn, n=0,...,4, proportional to
  1, x, x^2, x^3, x^4,
while an unknown common response gain supplies 1/x.

There are exactly six frozen p^2 probe values.  This script tests whether that
six-column nuisance/comparator block saturates the six-row linear TT space.
"""

import json
from pathlib import Path
import numpy as np

src = json.loads(Path("results/c5_source_completed_protocol_iteration149.json").read_text())
x = np.array([row["p2"] for row in src["kinematics"]], dtype=float)

lambda0 = 1.0
chi = np.exp(-lambda0 * x) / x
dchi_dlambda = -np.exp(-lambda0 * x)

# Common multiplicative GR response gain plus local spin-2 EFT response
# tangents induced by inverse-propagator terms x^2,...,x^6.
M = np.column_stack([
    1.0 / x,
    np.ones_like(x),
    x,
    x**2,
    x**3,
    x**4,
])

s = np.linalg.svd(M, compute_uv=False)
rank = int(np.linalg.matrix_rank(M, tol=1e-12))

# Since M is square and full rank, solve directly rather than relying on a
# pseudoinverse of an ill-conditioned Vandermonde-like matrix.
coef_chi = np.linalg.solve(M, chi)
coef_tangent = np.linalg.solve(M, dchi_dlambda)
rec_chi = M @ coef_chi
rec_tangent = M @ coef_tangent

out = {
    "iteration": 158,
    "comparator_id": "QG-NL-EXP-001",
    "scope": "linear TT six-probe response only",
    "lambda0": lambda0,
    "p2": x.tolist(),
    "nonlocal_response": chi.tolist(),
    "nonlocal_lambda_tangent": dchi_dlambda.tolist(),
    "base_columns": [
        "GR_response_gain_1_over_p2",
        "C5_dim4_spin2",
        "C5_dim6_spin2",
        "C5_dim8_spin2",
        "C5_dim10_spin2",
        "C5_dim12_spin2",
    ],
    "base_rank": rank,
    "singular_values": s.tolist(),
    "smin_over_smax": float(s[-1] / s[0]),
    "condition_number": float(s[0] / s[-1]),
    "response_interpolation_coefficients": coef_chi.tolist(),
    "tangent_interpolation_coefficients": coef_tangent.tolist(),
    "max_abs_response_reconstruction_error": float(np.max(np.abs(rec_chi - chi))),
    "max_abs_tangent_reconstruction_error": float(np.max(np.abs(rec_tangent - dchi_dlambda))),
    "status": {
        "linear_TT_base_span": "FULL_ROW_RANK_6_OF_6",
        "nonlocal_linear_residual": "ZERO_BY_PROTOCOL_SATURATION",
        "interpretation": "REGIME_SPECIFIC_NON_IDENTIFIABILITY_NOT_THEORY_IDENTITY",
        "nonlocal_cubic_chi2R": "BLOCKED_NONLOCAL_VERTEX_IMPLEMENTATION",
        "full_nonlocal_comparator": "BLOCKED",
        "Fisher_resources": "FORBIDDEN",
        "ANSATZ_003": "NOT_CREATED"
    }
}

print(json.dumps(out, indent=2, sort_keys=True))
