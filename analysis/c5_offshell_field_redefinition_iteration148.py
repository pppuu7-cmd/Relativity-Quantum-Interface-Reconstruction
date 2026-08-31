#!/usr/bin/env python3
"""Iteration 148: off-shell response / field-redefinition audit.

This is a deliberately minimal algebraic regression showing why an on-shell
EFT basis cannot be used as an off-shell retarded-response basis without an
explicit observable/source completion.

Toy dynamics:
    K phi + g/2 phi^2 + J = 0
so the tree second response is
    chi_phi(p;q,r) = -g Gp Gq Gr,  G=K^{-1}.

Under the local field redefinition
    phi = psi + a psi^2 + O(a^2),
the coordinate response of psi differs off shell:
    chi_psi = chi_phi - 2 a Gq Gr.
The physical observable phi is reconstructed as psi+a psi^2, which adds the
contact/source-map term +2 a Gq Gr and restores chi_phi exactly.

The lesson is structural and applies to the gravity comparator: an off-shell
chi2R tangent is basis-independent only after the operational metric/source
map is transformed consistently. An on-shell EOM-reduced Wilson basis alone
is not enough.
"""

from __future__ import annotations
import json
import random
from pathlib import Path

SEED = 148
N = 12
g = 0.37
a = 0.23
rng = random.Random(SEED)
rows = []
max_reconstruction_error = 0.0
min_coordinate_shift = float("inf")

for i in range(N):
    # Finite off-shell inverse propagators, deliberately away from poles.
    Kp = 0.4 + 1.6 * rng.random()
    Kq = 0.4 + 1.6 * rng.random()
    Kr = 0.4 + 1.6 * rng.random()
    Gp, Gq, Gr = 1.0 / Kp, 1.0 / Kq, 1.0 / Kr

    chi_phi = -g * Gp * Gq * Gr
    chi_psi_coordinate = chi_phi - 2.0 * a * Gq * Gr
    contact_observable_map = 2.0 * a * Gq * Gr
    chi_phi_reconstructed = chi_psi_coordinate + contact_observable_map

    reconstruction_error = abs(chi_phi_reconstructed - chi_phi)
    coordinate_shift = abs(chi_psi_coordinate - chi_phi)
    max_reconstruction_error = max(max_reconstruction_error, reconstruction_error)
    min_coordinate_shift = min(min_coordinate_shift, coordinate_shift)

    rows.append({
        "i": i,
        "Kp": Kp,
        "Kq": Kq,
        "Kr": Kr,
        "chi_phi": chi_phi,
        "chi_psi_coordinate": chi_psi_coordinate,
        "contact_observable_map": contact_observable_map,
        "chi_phi_reconstructed": chi_phi_reconstructed,
        "reconstruction_error": reconstruction_error,
        "coordinate_shift": coordinate_shift,
    })

result = {
    "iteration": 148,
    "seed": SEED,
    "n_points": N,
    "parameters": {"g": g, "a": a},
    "max_reconstruction_error": max_reconstruction_error,
    "min_nonzero_coordinate_shift": min_coordinate_shift,
    "pass_reconstruction": max_reconstruction_error < 1e-14,
    "pass_offshell_coordinate_noninvariance": min_coordinate_shift > 1e-8,
    "conclusion": "Off-shell coordinate response changes under a local field redefinition, while the physical observable response is restored only after the induced observable/source contact term is included.",
    "rows": rows,
}

out = Path("results/c5_offshell_field_redefinition_iteration148.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({k: result[k] for k in [
    "max_reconstruction_error",
    "min_nonzero_coordinate_shift",
    "pass_reconstruction",
    "pass_offshell_coordinate_noninvariance",
]}, indent=2))
