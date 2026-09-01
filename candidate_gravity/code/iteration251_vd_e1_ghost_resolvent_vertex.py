#!/usr/bin/env python3
"""RQIR Iteration 251: first e=1 Vilkovisky ghost-resolvent numerator block.

Frozen convention:
  D=4, Lambda=0, a=-1/2, eta=(-,+,+,+)
  N^alpha_beta = delta^alpha_beta Box + R^alpha_beta
  plane waves exp(i k.x), derivative momentum k_mu = eta_mu_nu k^nu.

This certificate derives and independently finite-difference checks the first
background variation delta N[h] on the same hard TT mode used in Iterations
248-249. It is the explicit c=1 ghost-resolvent insertion needed by the
E^(2) K^(1) part of Tr U1 at cubic metric order.

It does NOT construct the complete U1 tensor numerator: delta(R D R), delta Y,
E^(3), and the e=2 sector remain separate mandatory blocks.
"""
import json
import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])
K_HARD = np.array([0.2, 0.6, 0.3, 0.1])
P_GHOST = np.array([0.7, -0.4, 0.5, 0.9])

q = K_HARD[1:]
u = np.array([q[1], -q[0], 0.0])
u /= np.linalg.norm(u)
v = np.cross(q, u)
v /= np.linalg.norm(v)
E_HARD = np.zeros((4, 4))
E_HARD[1:, 1:] = (np.outer(u, u) - np.outer(v, v)) / np.sqrt(2)


def geometry(a):
    """Metric, inverse, Christoffel, dChristoffel and Ricci at x=0."""
    g = ETA + a * E_HARD
    gi = np.linalg.inv(g)
    kc = ETA @ K_HARD

    dg = np.zeros((4, 4, 4), dtype=complex)
    ddg = np.zeros((4, 4, 4, 4), dtype=complex)
    for mu in range(4):
        dg[mu] = 1j * kc[mu] * a * E_HARD
        for nu in range(4):
            ddg[mu, nu] = -(kc[mu] * kc[nu]) * a * E_HARD

    dgi = np.zeros((4, 4, 4), dtype=complex)
    for lam in range(4):
        dgi[lam] = -gi @ dg[lam] @ gi

    gamma = np.zeros((4, 4, 4), dtype=complex)
    dgamma = np.zeros((4, 4, 4, 4), dtype=complex)
    for al in range(4):
        for mu in range(4):
            for nu in range(4):
                A = [
                    dg[mu, s, nu] + dg[nu, s, mu] - dg[s, mu, nu]
                    for s in range(4)
                ]
                gamma[al, mu, nu] = 0.5 * sum(
                    gi[al, s] * A[s] for s in range(4)
                )
                for lam in range(4):
                    dgamma[lam, al, mu, nu] = 0.5 * sum(
                        dgi[lam, al, s] * A[s]
                        + gi[al, s]
                        * (
                            ddg[lam, mu, s, nu]
                            + ddg[lam, nu, s, mu]
                            - ddg[lam, s, mu, nu]
                        )
                        for s in range(4)
                    )

    ricci = np.zeros((4, 4), dtype=complex)
    for mu in range(4):
        for nu in range(4):
            val = 0j
            for r in range(4):
                val += dgamma[r, r, mu, nu] - dgamma[nu, r, mu, r]
                for ell in range(4):
                    val += (
                        gamma[r, r, ell] * gamma[ell, mu, nu]
                        - gamma[r, nu, ell] * gamma[ell, mu, r]
                    )
            ricci[mu, nu] = val

    return g, gi, gamma, dgamma, ricci


def ghost_operator_matrix(a):
    """N^alpha_beta on v^beta exp(i p.x) at x=0."""
    g, gi, gamma, dgamma, ricci = geometry(a)
    pc = ETA @ P_GHOST
    ricci_mixed = gi @ ricci
    N = np.zeros((4, 4), dtype=complex)

    for beta in range(4):
        pol = np.zeros(4)
        pol[beta] = 1.0
        lap = np.zeros(4, dtype=complex)

        for mu in range(4):
            for nu in range(4):
                for al in range(4):
                    term = -(pc[mu] * pc[nu]) * pol[al]
                    term += sum(
                        dgamma[mu, al, nu, r] * pol[r] for r in range(4)
                    )
                    term += sum(
                        gamma[al, nu, r] * (1j * pc[mu]) * pol[r]
                        for r in range(4)
                    )
                    term += sum(
                        gamma[al, mu, s]
                        * (
                            (1j * pc[nu]) * pol[s]
                            + sum(gamma[s, nu, r] * pol[r] for r in range(4))
                        )
                        for s in range(4)
                    )
                    term -= sum(
                        gamma[s, mu, nu]
                        * (
                            (1j * pc[s]) * pol[al]
                            + sum(gamma[al, s, r] * pol[r] for r in range(4))
                        )
                        for s in range(4)
                    )
                    lap[al] += gi[mu, nu] * term

        N[:, beta] = lap + ricci_mixed @ pol

    return N


def analytic_delta_N():
    """First TT-background variation of delta*Box + Ricci."""
    pc = ETA @ P_GHOST
    qc = ETA @ K_HARD
    eps_up = ETA @ E_HARD @ ETA
    eps_mixed = ETA @ E_HARD
    pdotq = P_GHOST @ ETA @ K_HARD
    epspp = pc @ eps_up @ pc

    out = np.zeros((4, 4))
    for al in range(4):
        for be in range(4):
            out[al, be] = epspp * (1.0 if al == be else 0.0)
            out[al, be] -= pdotq * eps_mixed[al, be]
            out[al, be] -= qc[be] * sum(
                pc[mu] * eps_up[al, mu] for mu in range(4)
            )
            out[al, be] += K_HARD[al] * sum(
                pc[mu] * eps_mixed[mu, be] for mu in range(4)
            )
    return out


analytic = analytic_delta_N()
rows = []
for step in [1e-4, 3e-5, 1e-5, 3e-6, 1e-6]:
    fd = (ghost_operator_matrix(step) - ghost_operator_matrix(-step)) / (2 * step)
    rows.append(
        {
            "step": step,
            "max_abs_fd_minus_analytic": float(np.max(np.abs(fd - analytic))),
            "fd_frobenius_norm": float(np.linalg.norm(fd)),
        }
    )

checks = {
    "hard_k2": float(K_HARD @ ETA @ K_HARD),
    "hard_transversality_max": float(np.max(np.abs((ETA @ K_HARD) @ E_HARD))),
    "hard_trace": float(np.sum(ETA * E_HARD)),
}

result = {
    "iteration": 251,
    "model_readiness_percent": 24,
    "frozen_convention": {
        "D": 4,
        "Lambda": 0,
        "deWitt_a": -0.5,
        "signature": "-+++",
        "plane_wave": "exp(i k.x)",
        "ghost_operator": "N^alpha_beta = delta^alpha_beta Box + R^alpha_beta",
        "loop_denominator_convention": "D_F(p)=1/(p^2+i0); N0^-1 carries the algebraic minus sign from Box -> -p^2",
    },
    "tt_checks": checks,
    "analytic_delta_N_frobenius_norm": float(np.linalg.norm(analytic)),
    "finite_difference_validation": rows,
    "e1_E2K1_resolvent_identity": (
        "delta(N^-1) = -N0^-1 (delta N) N0^-1; "
        "insert on either of the two N^-1 factors in U1 = N^-1 [R.(D R).E] N^-1 Y"
    ),
    "loop_topology_consequence": (
        "one deltaN insertion raises/repeats a ghost segment but creates no fourth external-momentum corner; "
        "this subblock stays inside the already-authorized raised bubble/triangle families"
    ),
    "classification": "PASS_SCOPED_E1_GHOST_RESOLVENT_VERTEX_FREEZE_AND_TT_VALIDATION",
    "guardrail": (
        "THIS_IS_ONLY_THE_GHOST_RESOLVENT_PART_OF_E2_K1; "
        "DO_NOT_PROMOTE_TO_COMPLETE_U1_OR_C5_COMPARATOR"
    ),
    "remaining_mandatory_e1_blocks": [
        "delta[R^i_gamma (D_i R^j_delta)] times E^(2)_j",
        "delta Y times E^(2)",
        "flat-kernel E^(3)",
        "E^(1) K^(2) placements with soft outside the isolated linear EOM",
    ],
    "candidate_residual": False,
    "heavy_run_authorized": False,
    "next_gate": 252,
}

assert abs(result["tt_checks"]["hard_trace"]) < 1e-14
assert result["tt_checks"]["hard_transversality_max"] < 1e-14
assert result["analytic_delta_N_frobenius_norm"] > 0.9
assert rows[-1]["max_abs_fd_minus_analytic"] < 2e-9

print(json.dumps(result, indent=2, sort_keys=True))
