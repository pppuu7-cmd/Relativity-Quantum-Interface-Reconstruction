#!/usr/bin/env python3
"""RQIR Iteration 083: sequential narrowband retuning likelihood.

Two science bands are acquired in separate apparatus configurations. Each setting has
an independent fractional gain/relock nuisance with independent calibration Fisher C_i.
The exact profiled beta Fisher is compared against the closed form sum_i P_i C_i/(P_i+C_i).
"""

import numpy as np


def profiled_beta(P2, P4, C2, C4):
    F = np.array([
        [P2 + P4, P2, P4],
        [P2, P2 + C2, 0.0],
        [P4, 0.0, P4 + C4],
    ], dtype=float)
    nuis = F[1:, 1:]
    cross = F[0, 1:]
    return F[0, 0] - cross @ np.linalg.pinv(nuis, rcond=1e-15) @ cross


def closed_form(P2, P4, C2, C4):
    return P2 * C2 / (P2 + C2) + P4 * C4 / (P4 + C4)

cases = [
    (1.0, 1.0, 0.0, 0.0),
    (1.0, 1.0, 1.0, 1.0),
    (1.0, 3.0, 100.0, 100.0),
    (0.2, 4.0, 0.5, 10.0),
]

for case in cases:
    p = profiled_beta(*case)
    c = closed_form(*case)
    assert np.isclose(p, c, atol=1e-12, rtol=1e-12), (case, p, c)

assert np.isclose(profiled_beta(1, 1, 0, 0), 0.0, atol=1e-12)
assert np.isclose(profiled_beta(1, 1, 1, 1), 1.0, atol=1e-12)
assert profiled_beta(1, 3, 1e9, 1e9) > 3.999999

print("RQIR Iteration 083 sequential-retuning likelihood")
for case in cases:
    print(case, profiled_beta(*case))
print("PASS")
