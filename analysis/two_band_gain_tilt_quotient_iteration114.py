#!/usr/bin/env python3
"""RQIR Iteration 114 — two-band gain/tilt quotient certificate.

Checks the exact reduction of a two-band Gaussian science likelihood with
- scalar common science amplitude beta,
- free antisymmetric spectral tilt q,
- two fractional band gains g2,g4,
- independent gain-reference Fisher matrix Cg.

The gain coordinates are transformed to common/differential modes
    g2 = c - d,  g4 = c + d,
so the science score of c is exactly the beta score and the science score of d
is exactly the tilt score.  After profiling tilt and differential gain, only the
reference Fisher on the common-gain quotient matters.

No apparatus numbers are asserted.
"""
from __future__ import annotations

import math
import numpy as np


def profiled_beta_full(s: np.ndarray, W: np.ndarray, Cg: np.ndarray) -> float:
    """Full beta profile with gain reference in per-band coordinates."""
    s = np.asarray(s, float)
    W = np.asarray(W, float)
    Cg = 0.5 * (np.asarray(Cg, float) + np.asarray(Cg, float).T)
    t = np.array([-s[0], s[1]])

    # Variables: beta, g2, g4, q_tilt.
    J = np.column_stack([
        s,
        np.array([s[0], 0.0]),
        np.array([0.0, s[1]]),
        t,
    ])
    F = J.T @ W @ J
    F[1:3, 1:3] += Cg
    N = F[1:, 1:]
    return float(F[0, 0] - F[0, 1:] @ np.linalg.pinv(N, rcond=1e-13) @ F[1:, 0])


def science_after_tilt(s: np.ndarray, W: np.ndarray) -> float:
    s = np.asarray(s, float)
    W = np.asarray(W, float)
    t = np.array([-s[0], s[1]])
    return float(s @ W @ s - (s @ W @ t) ** 2 / (t @ W @ t))


def common_gain_fisher(Cg: np.ndarray) -> float:
    """Reference Fisher on common gain c after profiling differential gain d.

    Per-band coordinates obey [g2,g4]^T = T [c,d]^T with
    T=[[1,-1],[1,1]].  If differential gain has zero Fisher support, PSD implies
    zero common/differential cross Fisher and the retained common block is used.
    """
    Cg = 0.5 * (np.asarray(Cg, float) + np.asarray(Cg, float).T)
    T = np.array([[1.0, -1.0], [1.0, 1.0]])
    Ccd = T.T @ Cg @ T
    Ccc, Ccross, Cdd = Ccd[0, 0], Ccd[0, 1], Ccd[1, 1]
    if Cdd <= 1e-13:
        if abs(Ccross) > 1e-10:
            raise ValueError("PSD support inconsistency")
        return float(Ccc)
    return float(Ccc - Ccross * Ccross / Cdd)


def common_gain_fisher_closed(Cg: np.ndarray) -> float:
    Cg = 0.5 * (np.asarray(Cg, float) + np.asarray(Cg, float).T)
    a, b, d = Cg[0, 0], Cg[0, 1], Cg[1, 1]
    denom = a + d - 2.0 * b
    if denom <= 1e-13:
        return common_gain_fisher(Cg)
    return float(4.0 * (a * d - b * b) / denom)


def combined_rate(Rs: float, Rc: float) -> float:
    return 1.0 / (1.0 / math.sqrt(Rs) + 1.0 / math.sqrt(Rc)) ** 2


def main() -> None:
    rng = np.random.default_rng(114)

    # 1. Random full-likelihood regressions.
    max_err = 0.0
    for _ in range(300):
        A = rng.normal(size=(2, 2))
        W = A.T @ A + 0.4 * np.eye(2)
        s = rng.normal(size=2)
        if min(abs(s)) < 0.05:
            s += np.array([0.2, -0.2])
        B = rng.normal(size=(2, 2))
        Cg = B.T @ B + 0.2 * np.eye(2)

        Fs = science_after_tilt(s, W)
        Ceff = common_gain_fisher(Cg)
        closed = Fs * Ceff / (Fs + Ceff)
        full = profiled_beta_full(s, W, Cg)
        max_err = max(max_err, abs(full - closed))
        assert abs(full - closed) < 2e-10
        assert abs(Ceff - common_gain_fisher_closed(Cg)) < 2e-10

    # 2. No transfer reference -> exact common-amplitude degeneracy.
    s = np.array([0.7, 1.1])
    W = np.array([[2.0, -0.3], [-0.3, 1.4]])
    assert abs(profiled_beta_full(s, W, np.zeros((2, 2)))) < 2e-12

    # 3. Independent band-reference Fisher gives a harmonic common-mode rate.
    c2, c4 = 3.0, 12.0
    Cdiag = np.diag([c2, c4])
    Ceff = common_gain_fisher(Cdiag)
    assert abs(Ceff - 4.0 * c2 * c4 / (c2 + c4)) < 2e-12

    # For fixed c2+c4, balanced independent allocation is optimal.
    total = 10.0
    xs = np.linspace(0.01, total - 0.01, 2000)
    vals = 4.0 * xs * (total - xs) / total
    imax = int(np.argmax(vals))
    assert abs(xs[imax] - total / 2.0) < 0.01
    assert abs(vals[imax] - total) < 2e-5

    # 4. Direct common-mode rank-one reference support is admissible.
    # A reference Fisher K on c corresponds to Cg=(K/4) [[1,1],[1,1]].
    K = 7.5
    Ccommon = (K / 4.0) * np.ones((2, 2))
    assert abs(common_gain_fisher(Ccommon) - K) < 2e-12

    # 5. Fixed-retention requirement.
    Fs = science_after_tilt(s, W)
    q = 0.90
    Crequired = q / (1.0 - q) * Fs
    Fret = Fs * Crequired / (Fs + Crequired)
    assert abs(Fret - q * Fs) < 2e-12

    # 6. Toy014/Toy009 science-ratio regression slice from Iteration 074.
    # This is NOT a physical apparatus result; it only illustrates how a common
    # transfer-reference bottleneck maps a science-only rate ratio toward unity.
    s_ratio = 0.2830146574583767
    zvals = [0.01, 0.1, 1.0, 10.0, 100.0]
    uratios = []
    for zc in zvals:  # zc = Rc,09 / Rs,09, with Rc,14=Rc,09
        u = ((1.0 + zc ** -0.5) /
             (s_ratio ** -0.5 + zc ** -0.5)) ** 2
        uratios.append(u)
        assert s_ratio < u < 1.0

    assert uratios[0] > uratios[-1]
    assert abs(combined_rate(s_ratio, 1.0) / combined_rate(1.0, 1.0) - uratios[2]) < 2e-12

    print("RQIR Iteration 114 regression: PASS")
    print(f"maximum random reduction error = {max_err:.3e}")
    print(f"independent-band Ceff(3,12)    = {Ceff:.12g}")
    print(f"fixed-retention q              = {q:.6g}")
    print(f"required Ceff/Fs               = {Crequired/Fs:.12g}")
    print("Toy014/Toy009 equal-reference illustrative u_DT:")
    for zc, u in zip(zvals, uratios):
        print(f"  Rc09/Rs09={zc:6g} -> u_DT={u:.12g}")


if __name__ == "__main__":
    main()
