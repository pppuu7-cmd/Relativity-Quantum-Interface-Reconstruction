#!/usr/bin/env python3
"""RQIR Iteration 252: U1 ghost/orbit-metric factorization and TT weight variation.

This is a notation/orientation audit required before the remaining E^(2)K^(1)
Vilkovisky numerator is assembled.  The paper distinguishes the orbit metric
N_orb from the minimal ghost matrix Nhat = Y^up N_orb.  Therefore

    N_orb^{-1} = Nhat^{-1} Y^up,
    N_orb^{-1} Y_down = Nhat^{-1},

and

    U1 = Nhat^{-1} Y^up [R.(D R).E] Nhat^{-1}.

For the frozen TT perturbation the density contribution to Y^up is zero at
first order, so (up to the fixed overall gauge-weight normalization)

    delta(sqrt(|g|) g^{mu nu}) = -epsilon^{mu nu}.
"""
import json
import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])
K_HARD = np.array([0.2, 0.6, 0.3, 0.1])
q = K_HARD[1:]
u = np.array([q[1], -q[0], 0.0])
u /= np.linalg.norm(u)
v = np.cross(q, u)
v /= np.linalg.norm(v)
E_HARD = np.zeros((4, 4))
E_HARD[1:, 1:] = (np.outer(u, u) - np.outer(v, v)) / np.sqrt(2)
EPS_UP = ETA @ E_HARD @ ETA


def weight_up(amplitude):
    """Representative contravariant DeWitt gauge weight density W=sqrt|g| g^-1.

    Any frozen overall sign/normalization multiplies both W0 and deltaW and is
    intentionally factored out; the relative first variation is unambiguous.
    """
    g = ETA + amplitude * E_HARD
    gi = np.linalg.inv(g)
    density = np.sqrt(abs(np.linalg.det(g)))
    return density * gi


rows = []
for step in [1e-4, 3e-5, 1e-5, 3e-6, 1e-6]:
    fd = (weight_up(step) - weight_up(-step)) / (2.0 * step)
    rows.append({
        "step": step,
        "max_abs_fd_minus_minus_epsilon_up": float(np.max(np.abs(fd + EPS_UP))),
        "fd_frobenius_norm": float(np.linalg.norm(fd)),
    })

# Pure matrix-orientation certificate: if Nhat = W N_orb, then
# N_orb^{-1} W^{-1} = Nhat^{-1}.  We use deterministic nonsingular matrices.
W = np.array([[2.0, 0.1, 0.0], [0.2, 1.7, 0.1], [0.0, -0.1, 1.3]])
Norb = np.array([[1.4, 0.2, -0.1], [0.1, 1.8, 0.3], [0.0, -0.2, 1.6]])
Nhat = W @ Norb
lhs = np.linalg.inv(Norb) @ np.linalg.inv(W)
rhs = np.linalg.inv(Nhat)
factorization_error = float(np.max(np.abs(lhs - rhs)))

result = {
    "iteration": 252,
    "model_readiness_percent": 24,
    "classification": "PASS_SCOPED_U1_ORBIT_GHOST_WEIGHT_FACTORIZATION_AND_TT_DELTA_WEIGHT",
    "notation_audit": {
        "orbit_metric": "N_orb_{alpha beta}=R^i_alpha G_ij R^j_beta (paper Eq. 5)",
        "minimal_ghost_matrix": "Nhat^alpha_beta=Y^{alpha gamma} N_orb_{gamma beta} (paper Eqs. 14,53)",
        "rewritten_U1": "U1 = Nhat^-1 Y^up [R.(D R).E] Nhat^-1",
        "consequence": "the two Iteration-251 delta(Nhat^-1) placements survive; deltaY belongs to the remaining explicit Y^up factor",
    },
    "tt_checks": {
        "trace_eta_epsilon": float(np.sum(ETA * E_HARD)),
        "transversality_max": float(np.max(np.abs((ETA @ K_HARD) @ E_HARD))),
    },
    "relative_weight_variation": "delta[sqrt(|g|) g^{mu nu}] = -epsilon^{mu nu} for TT h",
    "finite_difference_validation": rows,
    "matrix_factorization_max_error": factorization_error,
    "guardrail": "THIS_DOES_NOT_YET_SUPPLY_delta[R(DR)]E2_OR_COMPLETE_E2K1_NUMERATOR",
    "remaining_block": "delta[R^i_gamma(D_i R^j_delta)] E^(2)_j plus combined condensed-index/Ward check",
    "heavy_run_authorized": False,
    "candidate_residual": False,
    "next_gate": 253,
}

assert abs(result["tt_checks"]["trace_eta_epsilon"]) < 1e-14
assert result["tt_checks"]["transversality_max"] < 1e-14
assert rows[-1]["max_abs_fd_minus_minus_epsilon_up"] < 1e-9
assert factorization_error < 1e-14

print(json.dumps(result, indent=2, sort_keys=True))
