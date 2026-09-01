#!/usr/bin/env python3
"""Iteration 229: reproducible algebraic/numerical certificate for C3 completion ambiguity.

The script verifies an explicit O(h) homogeneous family that is transverse in
both response-index pairs and can survive a TT soft perturbation while
vanishing on the Minkowski background.  This is not a candidate model; it is a
counterexample to uniqueness from Eq.-(26) + conservation alone.

Convention: eta = diag(-,+,+,+).
"""

import itertools
import json
import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


def lower(v):
    return ETA @ v


def q_tensor(k):
    """Q^{mu nu}=k^2 eta^{mu nu}-k^mu k^nu, so k_mu Q^{mu nu}=0."""
    kc = lower(k)
    k2 = float(k @ kc)
    return k2 * ETA - np.outer(k, k)


def linearized_riemann(q, h):
    """Linearized R_{a b c d} in momentum space, up to an overall sign."""
    qc = lower(q)
    R = np.zeros((4, 4, 4, 4))
    for a, b, c, d in itertools.product(range(4), repeat=4):
        R[a, b, c, d] = 0.5 * (
            qc[c] * qc[b] * h[a, d]
            + qc[d] * qc[a] * h[b, c]
            - qc[d] * qc[b] * h[a, c]
            - qc[c] * qc[a] * h[b, d]
        )
    return R


def main():
    # Two generic response momenta.
    k = np.array([2.0, 1.0, 0.0, 0.0])
    kp = np.array([3.0, 0.0, 1.0, 0.0])
    Qk = q_tensor(k)
    Qkp = q_tensor(kp)

    left_transversality = lower(k) @ Qk
    right_transversality = lower(kp) @ Qkp

    # Null soft momentum along +z and a standard plus TT polarization.
    q = np.array([1.0, 0.0, 0.0, 1.0])
    h = np.zeros((4, 4))
    h[1, 1] = 1.0
    h[2, 2] = -1.0

    q_dot_h = q @ h
    trace_h = float(np.sum(ETA * h))

    # A gauge-invariant linear-curvature scalar which is nonzero for this TT row.
    # S = u^a v^b u^c v^d R^{(1)}_{a b c d}.
    u = np.array([1.0, 1.0, 0.0, 0.0])
    v = np.array([0.0, 1.0, 0.0, 1.0])
    R = linearized_riemann(q, h)
    S = float(np.einsum("a,b,c,d,abcd", u, v, u, v, R))

    # H^{mu nu,rho sigma}=c*S*Q_k^{mu nu} Q_k'^{rho sigma}.
    # Choose c=1 only to demonstrate a nonzero member of the family.
    H = S * np.einsum("mn,rs->mnrs", Qk, Qkp)
    div_left = np.einsum("m,mnrs->nrs", lower(k), H)
    div_right = np.einsum("r,mnrs->mns", lower(kp), H)

    out = {
        "metric_signature": "(-,+,+,+)",
        "max_abs_kQ": float(np.max(np.abs(left_transversality))),
        "max_abs_kprimeQ": float(np.max(np.abs(right_transversality))),
        "tt_max_abs_qh": float(np.max(np.abs(q_dot_h))),
        "tt_trace": trace_h,
        "tt_curvature_contraction_S": S,
        "max_abs_left_div_H": float(np.max(np.abs(div_left))),
        "max_abs_right_div_H": float(np.max(np.abs(div_right))),
        "H_frobenius_norm": float(np.linalg.norm(H)),
        "classification": "FORMAL_UNDERDETERMINATION_CERTIFICATE",
    }

    assert out["max_abs_kQ"] < 1e-12
    assert out["max_abs_kprimeQ"] < 1e-12
    assert out["tt_max_abs_qh"] < 1e-12
    assert abs(out["tt_trace"]) < 1e-12
    assert abs(out["tt_curvature_contraction_S"]) > 1e-12
    assert out["max_abs_left_div_H"] < 1e-12
    assert out["max_abs_right_div_H"] < 1e-12
    assert out["H_frobenius_norm"] > 1e-12

    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
