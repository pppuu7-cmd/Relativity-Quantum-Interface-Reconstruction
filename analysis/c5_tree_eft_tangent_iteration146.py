#!/usr/bin/env python3
"""Iteration 146: finite C5 tree-level gravitational-EFT tangent audit.

This script intentionally computes an on-shell amplitude fingerprint, not the full
RQIR retarded/CTP tangent.  It uses the D=4 parity-even tree-level graviton EFT
amplitude of de Rham, Jaitly & Tolley (arXiv:2212.04975, eq. 4.4), linearized
around the Einstein-Hilbert point in the Wilson coefficients.

The purpose is twofold:
1) certify that a finite fixed C5 local-EFT truncation has a nontrivial, finite,
   reproducible Wilson tangent at frozen kinematics;
2) prevent the on-shell S-matrix tangent from being silently identified with the
   Iteration-145 ordered RQIR response tangent.  The latter requires an explicit
   retarded/CTP continuation and remains BLOCKED in Iteration 146.
"""

import json
import math
from pathlib import Path
import numpy as np

# Dimensionless convention: Lambda = 1, and amplitudes are multiplied by M_Pl^2.
# D=4.  c_GB does not enter linearly in the quoted D=4 amplitude around the EH point.
PARAMS = ["c3", "c_plus", "c_minus", "e_plus", "e_minus",
          "f_plus", "f_minus", "g_plus", "g_minus", "j1"]

# (s/Lambda^2, t/Lambda^2, phi).  u is fixed by s+t+u=0.
KINEMATICS = [
    (0.20, -0.07, 0.0),
    (0.20, -0.07, math.pi/3),
    (0.20, -0.07, math.pi/2),
    (0.30, -0.11, 0.0),
    (0.30, -0.11, math.pi/3),
    (0.30, -0.11, math.pi/2),
    (0.18, -0.05, 0.0),
    (0.18, -0.05, math.pi/3),
    (0.18, -0.05, math.pi/2),
    (0.26, -0.09, math.pi/6),
    (0.26, -0.09, math.pi/4),
    (0.26, -0.09, 2*math.pi/3),
]


def tangent_row(s, t, phi):
    u = -s - t
    x = s*t + t*u + u*s
    y = s*t*u
    cp = math.cos(phi)
    c2 = math.cos(2*phi)

    # Linear derivatives of M_Pl^2 A, from eq. (4.4), at c_i=0 in D=4.
    # Terms quadratic in c3 have zero first derivative at the EH point.
    return np.array([
        6.0*(2.0*cp + 5.0*c2)*y,                  # d/d c3
        8.0*x*x,                                    # d/d c_plus
        8.0*c2*x*x,                                 # d/d c_minus
        -10.0*x*y,                                  # d/d e_plus
        -10.0*c2*x*y,                               # d/d e_minus
        3.0*y*y - 2.0*x**3,                         # d/d f_plus
        c2*(3.0*y*y - 2.0*x**3),                    # d/d f_minus
        -0.5*(3.0*y*y + 2.0*x**3),                  # d/d g_plus
        -0.5*c2*(3.0*y*y + 2.0*x**3),               # d/d g_minus
        -(3.0/8.0)*(cp + c2)*y*y,                   # d/d j1
    ], dtype=float)


def main():
    V = np.vstack([tangent_row(*p) for p in KINEMATICS])
    U, svals, VT = np.linalg.svd(V, full_matrices=False)
    tol = max(V.shape) * np.finfo(float).eps * svals[0]
    rank = int(np.sum(svals > tol))

    result = {
        "iteration": 146,
        "scope": "D=4 parity-even local gravitational EFT; tree-level on-shell amplitude fingerprint only",
        "dimensionless_convention": "Lambda=1, report M_Pl^2 A",
        "parameters": PARAMS,
        "kinematics": [
            {"s": s, "t": t, "u": -s-t, "phi": phi}
            for s, t, phi in KINEMATICS
        ],
        "matrix_shape": list(V.shape),
        "rank": rank,
        "svd_tolerance": float(tol),
        "singular_values": [float(x) for x in svals],
        "condition_ratio_smin_over_smax": float(svals[-1] / svals[0]),
        "full_column_rank": bool(rank == len(PARAMS)),
        "blockers": {
            "loop_nonanalytic": "BLOCKED_NOT_DERIVED_IN_ITER145_RQIR_COORDINATES",
            "rqir_retarded_ctp_map": "BLOCKED_ON_SHELL_AMPLITUDE_IS_NOT_CHI2R",
            "N2_C3sym_rows": "BLOCKED_REQUIRE_CTP_STATE_AND_LOOP_OR_INFLUENCE_FUNCTIONAL_DERIVATION"
        },
        "claim": "Finite local C5 tree-EFT Wilson tangent is rank-certified at frozen kinematics; full post-Gaussian RQIR V_C5 remains blocked until retarded/CTP mapping is derived."
    }

    out = Path("results/c5_tree_eft_tangent_iteration146.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
