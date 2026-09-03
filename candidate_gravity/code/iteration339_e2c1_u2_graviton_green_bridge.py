#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 339.

Close only the graviton-Green part of the Iteration-309 physical U2 blocker.

Iteration 309 uses ``H`` for the field-space Green operator inside

    U2 = N_L V1_L H V1_R N_R Y.

Iterations 319/329 subsequently froze the *minimal graviton differential
operator* through first background order on the same D=4, Lambda=0, a=-1/2
parent.  To avoid a notation collision this gate calls that operator K and its
inverse G.  For a Fourier insertion q,

    K = K0 + h K1 + ...,
    G0(p) = K0(p)^-1,
    G1(q;p) = -G0(p+q) K1(q;p) G0(p).

The shifted left propagator is mandatory.  The identity is tested with the
actual physical Iteration-319 K1 matrix and with K0 independently reconstructed
at p and p+q from the same parent code.  No V1 kernel is invented: V1_1/V1_2
remain BLOCKED and no e=2,c<=1 numerator is assembled.
"""
from __future__ import annotations

import contextlib
import io
import json
import re
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
PARENT = ROOT / "iteration319_det_graviton_three_mode_routing.py"
SRC0 = PARENT.read_text().split("FIT=indices(4)", 1)[0]


def load_parent(p_in: np.ndarray):
    """Execute the frozen Iteration-319 physical operator prefix at chosen p."""
    replacement = "p=P_IN.copy()"
    src, n = re.subn(r"p=np\.array\([^\n]+\)", replacement, SRC0, count=1)
    if n != 1:
        raise RuntimeError(f"failed to specialize Iteration-319 input momentum: {n}")
    ns = {"P_IN": np.array(p_in, dtype=float)}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src, "iteration319_u2_green_bridge", "exec"), ns, ns)
    return ns


base = load_parent(np.array([0.61, -0.33, 0.24, 0.52], dtype=float))
p = np.array(base["p"], dtype=float)
q = np.array(base["qs"][0], dtype=float)
pout = p + q
out = load_parent(pout)

eta = np.array(base["eta"], dtype=complex)
NB = int(base["NB"])
I = np.eye(NB, dtype=complex)
a = (1, 0, 0)

K0_in = np.array(base["H"][base["ZERO"]], dtype=complex)
K1 = np.array(base["H"][a], dtype=complex)
K0_out = np.array(out["H"][out["ZERO"]], dtype=complex)

p2 = complex(np.einsum("mn,m,n->", eta, p, p))
pout2 = complex(np.einsum("mn,m,n->", eta, pout, pout))
flat_in_error = float(np.max(np.abs(K0_in - p2 * I)))
flat_out_error = float(np.max(np.abs(K0_out - pout2 * I)))

G0_in = np.linalg.inv(K0_in)
G0_out = np.linalg.inv(K0_out)
G1 = -G0_out @ K1 @ G0_in

# Independent finite block inverse.  Momentum-sector ordering is (p, p+q), so
# K1 is the lower-left block: input p -> output p+q.
def block_operator(t: float):
    z = np.zeros((NB, NB), dtype=complex)
    return np.block([[K0_in, z], [t * K1, K0_out]])

steps = [0.37, -0.23, 0.11]
block_errors = []
for t in steps:
    Binv = np.linalg.inv(block_operator(t))
    routed = Binv[NB:, :NB]
    block_errors.append(float(np.max(np.abs(routed - t * G1))))

fd_h = 1.0e-5
Gp = np.linalg.inv(block_operator(fd_h))[NB:, :NB]
Gm = np.linalg.inv(block_operator(-fd_h))[NB:, :NB]
fd_G1 = (Gp - Gm) / (2.0 * fd_h)
fd_error = float(np.max(np.abs(fd_G1 - G1)))

# Explicitly test that using the unshifted left propagator is generally a
# different object; this prevents accidental collapse back to G0(p) K1 G0(p).
wrong_unshifted = -G0_in @ K1 @ G0_in
shift_matter_norm = float(np.linalg.norm(G1 - wrong_unshifted))

thresholds = {
    "flat_K0_identity_max": 1.0e-12,
    "block_inverse_max": 1.0e-11,
    "finite_difference_G1_max": 1.0e-9,
    "shift_matter_min_norm": 1.0e-6,
}

passed = bool(
    abs(p2) > 1.0e-8
    and abs(pout2) > 1.0e-8
    and flat_in_error <= thresholds["flat_K0_identity_max"]
    and flat_out_error <= thresholds["flat_K0_identity_max"]
    and max(block_errors) <= thresholds["block_inverse_max"]
    and fd_error <= thresholds["finite_difference_G1_max"]
    and shift_matter_norm >= thresholds["shift_matter_min_norm"]
)

classification = (
    "PASS_E2C1_U2_GRAVITON_GREEN_H0_H1_SAME_PARENT_ROUTING_BRIDGE__V1_KERNELS_REMAIN_BLOCKED"
    if passed
    else "FAIL_E2C1_U2_GRAVITON_GREEN_H0_H1_ROUTING_BRIDGE"
)

result = {
    "iteration": 339,
    "model_readiness_percent": 24,
    "scientific_gate_pass": passed,
    "classification": classification,
    "candidate_residual": False,
    "scope": {
        "sector": "connection e=2,c<=1 physical U2 prerequisite",
        "parent": "Iteration-319 minimal graviton operator K=-(Box+Pi)",
        "convention": {"D": 4, "Lambda": 0, "a": "-1/2"},
        "tensor_basis_dimension": NB,
        "input_p": [float(x) for x in p],
        "background_q": [float(x) for x in q],
        "output_p": [float(x) for x in pout],
        "routing": "K1(q;p): p -> p+q",
    },
    "notation_disambiguation": {
        "K": "physical graviton differential operator frozen by Iteration 319",
        "G": "field-space Green operator denoted H in Iteration 309 U2 contract",
        "G0": "K0^-1",
        "G1": "-G0(p+q) K1(q;p) G0(p)",
    },
    "checks": {
        "p2": [float(p2.real), float(p2.imag)],
        "pout2": [float(pout2.real), float(pout2.imag)],
        "flat_K0_in_max_error": flat_in_error,
        "flat_K0_out_max_error": flat_out_error,
        "block_inverse_errors": block_errors,
        "block_inverse_max_error": max(block_errors),
        "finite_difference_G1_error": fd_error,
        "shifted_vs_wrong_unshifted_frobenius_norm": shift_matter_norm,
        "thresholds": thresholds,
    },
    "physical_status": {
        "U2_H0_flat_graviton_green": "FROZEN_FROM_SAME_PARENT_IF_PASS",
        "U2_H1_first_background_graviton_green": "FROZEN_FROM_SAME_PARENT_IF_PASS",
        "V1_1_flat_momentum_kernel": "BLOCKED_UNCHANGED",
        "V1_2_mixed_background_kernel": "BLOCKED_UNCHANGED",
        "N_and_Y_green_routing_bridge": "NOT_CLOSED_BY_THIS_GATE",
        "e2c1_U2_numerator": "NOT_AUTHORIZED",
    },
    "guardrails": [
        "OPERATOR_K_IS_NOT_THE_U2_GREEN_H_NOTATION",
        "LEFT_GREEN_PROPAGATOR_USES_SHIFTED_MOMENTUM_P_PLUS_Q",
        "UNSUPPORTED_V1_COMPONENTS_REMAIN_BLOCKED_NOT_ZERO_FILLED",
        "NO_U2_NUMERATOR_ASSEMBLY_FROM_THIS_BRIDGE_ALONE",
        "NO_SOURCE_BORN_SUBTRACTION",
        "NO_ANSATZ003",
        "NO_FISHER_RESOURCES",
        "NO_BLIND_HEAVY_FULL_C5",
    ],
    "next_gate": (
        "derive/freeze same-parent physical V1_1 and V1_2 kernels in the Iteration-309 index orientation; separately bridge any required N/Y inverse routing before U2 numerator assembly"
        if passed
        else "preserve FAIL and diagnose operator-to-Green momentum routing without changing Iteration-319 parent dynamics"
    ),
}

print(json.dumps(result, indent=2, sort_keys=True))
if not passed:
    raise SystemExit(2)
