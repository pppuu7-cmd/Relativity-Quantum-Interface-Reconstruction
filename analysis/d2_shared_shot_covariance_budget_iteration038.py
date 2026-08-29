"""RQIR Iteration 038: shared-shot covariance Fisher budget and coherence break-even.

Builds on Iterations 034-037.  Consider a real m-dimensional phase-referenced
Gaussian detector output with q calibration coordinates u_i entering affinely
through the covariance

    Sigma(u) = Sigma0 + sum_i u_i Sigma_i,

and require the same local detector model to remain positive for the full
hypercube u_i in [-1,1].  In whitened coordinates H_i = Sigma0^-1/2 Sigma_i
Sigma0^-1/2, positivity at all hypercube vertices implies

    ||sum_i s_i H_i||_op < 1  for every sign vector s_i=+/-1.

Averaging Tr[(sum_i s_i H_i)^2] over signs gives

    sum_i Tr(H_i^2) < m,

so the covariance Fisher matrix K_ij=1/2 Tr(H_i H_j) obeys

    Tr K < m/2,  lambda_min(K) <= m/(2q).

For the four high-value D2 centered covariance rows and a minimal m=8 joint
output, the weakest-direction per-shot Fisher therefore cannot exceed one.
The script also checks a near-saturating block encoding, nuisance profiling,
and the resulting coherence-coupled wall-clock break-even against corrected
source-preparation QFI.
"""
from __future__ import annotations

import itertools
import math
import numpy as np

# Preferred centered D2 benchmark from Iteration 034 (rounded documented value).
GAMMA_COV = 0.590127e6
# Preparation Fisher saved by adding the best four force-covariance rows at
# y_ref=-4, lambda=1: C_alpha 4.55511 -> 0.0500614.
DELTA_C_ALPHA = 4.55511 - 0.0500614
# Coordinate-correct source QFI per accepted single-branch copy.
FQ_ALPHA = 0.0849323916
# Largest stored dimensionless source phase used by the joint high-value set.
MAX_PHASE = 4.99085067


def covariance_fisher_matrix(hs: list[np.ndarray]) -> np.ndarray:
    q = len(hs)
    out = np.empty((q, q), float)
    for i in range(q):
        for j in range(q):
            out[i, j] = 0.5 * float(np.trace(hs[i] @ hs[j]))
    return out


def hypercube_positive_whitened(hs: list[np.ndarray]) -> bool:
    m = hs[0].shape[0]
    eye = np.eye(m)
    for signs in itertools.product((-1.0, 1.0), repeat=len(hs)):
        a = sum(s * h for s, h in zip(signs, hs))
        if np.min(np.linalg.eigvalsh(eye + a)) <= 0:
            return False
    return True


def block_encoding(q: int, amplitude: float = 0.999) -> list[np.ndarray]:
    """Near-saturating m=2q construction with disjoint traceless 2x2 blocks."""
    if not (0 < amplitude < 1):
        raise ValueError("amplitude must lie in (0,1)")
    m = 2 * q
    hs = []
    for i in range(q):
        h = np.zeros((m, m), float)
        h[2 * i, 2 * i] = amplitude
        h[2 * i + 1, 2 * i + 1] = -amplitude
        hs.append(h)
    return hs


def profiled_fisher(kuu: np.ndarray, kug: np.ndarray, kgg: np.ndarray) -> np.ndarray:
    return kuu - kug @ np.linalg.pinv(kgg, rcond=1e-14) @ kug.T


def ideal_joint_cycle_ratio() -> float:
    """Necessary tP/tC at equal efficiencies in the m=8,q=4 ideal limit."""
    # The positivity theorem gives lambda_min(K)<1 for m=8,q=4.
    return GAMMA_COV * FQ_ALPHA / DELTA_C_ALPHA


def coherence_floor(gap_hz: float) -> float:
    return MAX_PHASE / (2.0 * math.pi * gap_hz)


def critical_prep_cycle(gap_hz: float, dead_s: float = 0.0,
                        prep_eff: float = 1.0, cov_eff: float = 1.0) -> float:
    """Necessary source-metrology cycle time for covariance to be able to win.

    Here prep_eff=p_P*eta_P and cov_eff=p_C*eta_C.  The joint covariance cycle
    is given the optimistic lower bound Tcoh+dead_s.
    """
    if prep_eff <= 0 or cov_eff <= 0:
        raise ValueError("efficiencies must be positive")
    tc = coherence_floor(gap_hz) + dead_s
    return ideal_joint_cycle_ratio() * tc * prep_eff / cov_eff


def main() -> None:
    q = 4
    m = 8
    amp = 0.999
    hs = block_encoding(q, amp)
    assert hypercube_positive_whitened(hs)

    k = covariance_fisher_matrix(hs)
    eig = np.linalg.eigvalsh(k)
    print("joint K=", k)
    print("joint K eigenvalues=", eig)
    print("Tr K=", np.trace(k), "m/2=", m / 2)
    assert np.allclose(k, amp**2 * np.eye(q), atol=1e-14)
    assert np.trace(k) < m / 2
    assert np.min(eig) < m / (2 * q)

    # Explicit hypercube trace-budget check by averaging signed sums.
    signed_tr2 = []
    for signs in itertools.product((-1.0, 1.0), repeat=q):
        a = sum(s * h for s, h in zip(signs, hs))
        signed_tr2.append(float(np.trace(a @ a)))
        assert np.linalg.norm(a, 2) < 1.0
    avg_tr2 = float(np.mean(signed_tr2))
    sum_tr2 = float(sum(np.trace(h @ h) for h in hs))
    print("E_sign Tr A_s^2=", avg_tr2, "sum Tr H_i^2=", sum_tr2)
    assert abs(avg_tr2 - sum_tr2) < 1e-12
    assert sum_tr2 < m

    # Common detector variance/imprecision-scale nuisance G=I is Fisher-
    # orthogonal to traceless block covariance signals at Sigma0=I.
    g_common = np.eye(m)
    kuu = k
    kug = np.array([[0.5 * np.trace(h @ g_common)] for h in hs], float)
    kgg = np.array([[0.5 * np.trace(g_common @ g_common)]], float)
    kp_common = profiled_fisher(kuu, kug, kgg)
    print("profiled eigenvalues, common-scale nuisance=", np.linalg.eigvalsh(kp_common))
    assert np.max(np.abs(kug)) < 1e-14
    assert np.allclose(kp_common, k, atol=1e-14)

    # An unknown backaction/cross-noise nuisance aligned with H_0 removes that
    # covariance direction exactly after profiling.
    g_aligned = hs[0]
    kug2 = np.array([[0.5 * np.trace(h @ g_aligned)] for h in hs], float)
    kgg2 = np.array([[0.5 * np.trace(g_aligned @ g_aligned)]], float)
    kp_aligned = profiled_fisher(kuu, kug2, kgg2)
    eig_aligned = np.linalg.eigvalsh(kp_aligned)
    print("profiled eigenvalues, aligned covariance nuisance=", eig_aligned)
    assert eig_aligned[0] < 1e-12
    assert np.all(eig_aligned[1:] > 0.99)

    # Accepted shared-shot lower bound at lambda=1.  In the ideal limit
    # lambda_min(K)->1, N_joint must exceed GAMMA_COV.  The explicit a=.999
    # construction is slightly worse.
    n_near = GAMMA_COV / np.min(eig)
    n_ideal = GAMMA_COV
    print("accepted joint cycles near saturation=", n_near)
    print("ideal lower bound accepted joint cycles>", n_ideal)
    assert abs(n_near - 591309.0267444622) < 1e-6

    prep_copies_saved = DELTA_C_ALPHA / FQ_ALPHA
    ratio = ideal_joint_cycle_ratio()
    print("prep single-branch copy equivalents saved=", prep_copies_saved)
    print("necessary equal-efficiency tP/tC >", ratio)
    assert abs(prep_copies_saved - 53.04276160286531) < 1e-10
    assert abs(ratio - 11125.495395928292) < 1e-9

    for f in (10.0, 100.0, 1000.0):
        tc = coherence_floor(f)
        tp0 = critical_prep_cycle(f, 0.0)
        tp1 = critical_prep_cycle(f, 1e-3)
        print(f"gap={f:g} Hz Tcoh={tc:.12g}s tPcrit(no dead)={tp0:.12g}s "
              f"tPcrit(+1ms)={tp1:.12g}s")

    assert abs(coherence_floor(100.0) - 0.007943185543639977) < 1e-15
    assert abs(critical_prep_cycle(100.0, 0.0) - 88.37187419476634) < 1e-6
    assert abs(critical_prep_cycle(100.0, 1e-3) - 99.49736959069463) < 1e-6


if __name__ == "__main__":
    main()
