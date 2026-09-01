#!/usr/bin/env python3
"""RQIR Iteration 248: nonlinear Einstein mixed soft-hard certificate.

Purpose
-------
Iteration 247 proved that the Vilkovisky e=1 and e=2 EOM sectors cannot be
removed by the linear null-soft equation E^(1)[h_s]=0 alone, because cubic
metric-order partitions can contain E^(2) and E^(3).  This executable check
constructs one explicit null-soft TT mode h_s and one spacelike hard TT mode
h_h and evaluates the exact Einstein tensor of

    g = eta + a h_s exp(i k_s.x) + b h_h exp(i k_h.x)

at x=0.  A symmetric finite difference in amplitudes extracts the mixed
coefficient d^2 G/(da db)|_0.  Nonzero convergence is a scoped existence
certificate that G^(2)[h_s,h_h] can survive although G^(1)[h_s]=0.

This is not a full Vilkovisky e1/e2 comparator column and not a Candidate
Gravity residual.
"""

import json
import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])

K_SOFT = np.array([1.0, 0.0, 0.0, 1.0])
E_SOFT = np.zeros((4, 4))
E_SOFT[1, 1] = 1 / np.sqrt(2)
E_SOFT[2, 2] = -1 / np.sqrt(2)

K_HARD = np.array([0.2, 0.6, 0.3, 0.1])
q = K_HARD[1:]
u = np.array([q[1], -q[0], 0.0])
u /= np.linalg.norm(u)
v = np.cross(q, u)
v /= np.linalg.norm(v)
E_HARD = np.zeros((4, 4))
E_HARD[1:, 1:] = (np.outer(u, u) - np.outer(v, v)) / np.sqrt(2)


def einstein_tensor(a, b):
    g = ETA + a * E_SOFT + b * E_HARD
    gi = np.linalg.inv(g)
    ks = ETA @ K_SOFT
    kh = ETA @ K_HARD

    dg = np.zeros((4, 4, 4), dtype=complex)
    ddg = np.zeros((4, 4, 4, 4), dtype=complex)
    for mu in range(4):
        dg[mu] = 1j * (ks[mu] * a * E_SOFT + kh[mu] * b * E_HARD)
        for nu in range(4):
            ddg[mu, nu] = -(
                ks[mu] * ks[nu] * a * E_SOFT
                + kh[mu] * kh[nu] * b * E_HARD
            )

    dgi = np.zeros((4, 4, 4), dtype=complex)
    for lam in range(4):
        dgi[lam] = -gi @ dg[lam] @ gi

    gamma = np.zeros((4, 4, 4), dtype=complex)
    dgamma = np.zeros((4, 4, 4, 4), dtype=complex)
    for r in range(4):
        for m in range(4):
            for n in range(4):
                A = [dg[m, s, n] + dg[n, s, m] - dg[s, m, n] for s in range(4)]
                gamma[r, m, n] = 0.5 * sum(gi[r, s] * A[s] for s in range(4))
                for lam in range(4):
                    dgamma[lam, r, m, n] = 0.5 * sum(
                        dgi[lam, r, s] * A[s]
                        + gi[r, s]
                        * (
                            ddg[lam, m, s, n]
                            + ddg[lam, n, s, m]
                            - ddg[lam, s, m, n]
                        )
                        for s in range(4)
                    )

    ricci = np.zeros((4, 4), dtype=complex)
    for m in range(4):
        for n in range(4):
            val = 0j
            for r in range(4):
                val += dgamma[r, r, m, n] - dgamma[n, r, m, r]
                for ell in range(4):
                    val += (
                        gamma[r, r, ell] * gamma[ell, m, n]
                        - gamma[r, n, ell] * gamma[ell, m, r]
                    )
            ricci[m, n] = val

    scalar = np.sum(gi * ricci)
    return ricci - 0.5 * g * scalar


def mixed_second(step):
    return (
        einstein_tensor(step, step)
        - einstein_tensor(step, -step)
        - einstein_tensor(-step, step)
        + einstein_tensor(-step, -step)
    ) / (4 * step * step)


steps = [1e-2, 3e-3, 1e-3, 3e-4]
rows = []
for h in steps:
    mix = mixed_second(h)
    rows.append(
        {
            "step": h,
            "frobenius_norm": float(np.linalg.norm(mix)),
            "max_abs_component": float(np.max(np.abs(mix))),
        }
    )

result = {
    "iteration": 248,
    "model_readiness_percent": 24,
    "soft_k2": float(K_SOFT @ ETA @ K_SOFT),
    "hard_k2": float(K_HARD @ ETA @ K_HARD),
    "soft_transversality_max": float(np.max(np.abs((ETA @ K_SOFT) @ E_SOFT))),
    "hard_transversality_max": float(np.max(np.abs((ETA @ K_HARD) @ E_HARD))),
    "soft_trace": float(np.sum(ETA * E_SOFT)),
    "hard_trace": float(np.sum(ETA * E_HARD)),
    "mixed_second_difference": rows,
    "classification": "PASS_SCOPED_NONLINEAR_EINSTEIN_MIXED_SOFT_HARD_NONZERO",
    "scientific_claim": "E1_soft_zero_does_not_eliminate_E2_soft_hard",
    "guardrail": "DO_NOT_ZERO_VD_E1_E2_SECTORS_FROM_LINEAR_NULL_SOFT_EOM",
    "candidate_residual": False,
    "next_gate": 249,
}

# Frozen sanity requirements.
assert abs(result["soft_k2"]) < 1e-14
assert result["soft_transversality_max"] < 1e-14
assert result["hard_transversality_max"] < 1e-14
assert abs(result["soft_trace"]) < 1e-14
assert abs(result["hard_trace"]) < 1e-14
assert rows[-1]["frobenius_norm"] > 0.7
assert rows[-1]["max_abs_component"] > 0.4
assert abs(rows[-1]["frobenius_norm"] - rows[-2]["frobenius_norm"]) < 2e-5

print(json.dumps(result, indent=2, sort_keys=True))
