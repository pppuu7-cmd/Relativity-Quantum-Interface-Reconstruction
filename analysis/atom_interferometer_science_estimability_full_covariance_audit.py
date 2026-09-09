"""RQIR Paper III — physical atom-interferometer science-estimability audit.

Purpose
-------
Distinguish two notions that were previously conflated:
(1) full apparatus-parameter identifiability, and
(2) estimability of the RQIR science amplitude theta.

The physical scaling is anchored to light-pulse / Ramsey-Borde atom
interferometry. A leading acceleration-like phase scales as

    phi_acc ~ n k a T^2

(or, in the simultaneous-conjugate Ramsey-Borde geometry,
    phi_acc ~ n k a T (T + T'))

while a recoil phase scales as

    phi_rec ~ n^2 (hbar k^2 / 2m) T.

Thus, for a common fractional timebase scale, the fractional calibration
sensitivity vectors are e_acc=(1,2) and e_rec=(2,1) in (k,T).

This script tests these physical directions after simultaneous profiling of
channel-specific phase offsets, linear/quadratic drift, and a full correlated
two-channel covariance. It explicitly checks whether the null space of the
Fisher matrix contains the science direction theta.

Key distinction
---------------
A Fisher matrix may be rank deficient because an apparatus-only combination
is unidentifiable while theta itself remains estimable. Therefore full-rank
calibration is stronger than is necessary for a valid science constraint.

References
----------
Hogan, Johnson & Kasevich, "Light-pulse atom interferometry", arXiv:0806.3261.
Lan et al., Phys. Rev. Lett. 108, 090402 (2012), DOI:
10.1103/PhysRevLett.108.090402. Their simultaneous-conjugate Ramsey-Borde
phase contains a recoil term proportional to n^2 k^2 T and a gravity term
proportional to n k g T(T+T').
Chiarotti et al., PRX Quantum 3, 030348 (2022), DOI:
10.1103/PRXQuantum.3.030348, gives the leading LMT inertial scaling
phi ~ n k g T^2.
"""
from __future__ import annotations

import math
import numpy as np


def ar1(n: int, rho: float) -> np.ndarray:
    if n < 8:
        raise ValueError("n must be >= 8")
    if not (-1.0 < rho < 1.0):
        raise ValueError("|rho| must be < 1")
    j = np.arange(n)
    return rho ** np.abs(j[:, None] - j[None, :])


def paired_covariance(
    n: int,
    rho: float,
    sigma_acc_white: float = 0.7,
    sigma_rec_white: float = 0.8,
    sigma_acc_common: float = 0.6,
    sigma_rec_common: float = 0.5,
) -> np.ndarray:
    """Positive-definite full covariance with cross-channel common mode."""
    R = ar1(n, rho)
    I = np.eye(n)
    Caa = sigma_acc_white**2 * I + sigma_acc_common**2 * R
    Crr = sigma_rec_white**2 * I + sigma_rec_common**2 * R
    Car = sigma_acc_common * sigma_rec_common * R
    C = np.block([[Caa, Car], [Car.T, Crr]])
    if np.min(np.linalg.eigvalsh(C)) <= 0.0:
        raise AssertionError("covariance must be positive definite")
    return C


def profiled_precision(cov: np.ndarray, nuisance: np.ndarray) -> np.ndarray:
    """Precision after exact profiling of additive linear nuisances."""
    Cinv = np.linalg.inv(cov)
    normal = nuisance.T @ Cinv @ nuisance
    return Cinv - Cinv @ nuisance @ np.linalg.solve(normal, nuisance.T @ Cinv)


def sequence(nshot: int) -> dict[str, np.ndarray]:
    """Dimensionless schedule preserving the physical power-law geometry."""
    j = np.arange(nshot)
    sign = np.where(j % 2 == 0, 1.0, -1.0)
    lmt = np.where((j // 4) % 2 == 0, 1.0, 2.0)
    T = np.where((j // 2) % 2 == 0, 1.0, 1.25)
    Tprime = 0.08 * T
    qref = np.where((j // 8) % 2 == 0, 1.0, -1.0)
    clock = np.linspace(-1.0, 1.0, nshot)

    # Acceleration / gravity-like channel: n*k*a*T*(T+T').
    Kacc = sign * lmt * T * (T + Tprime)

    # Recoil-like calibration channel: n^2*k^2*T. Constants hbar/(2m)
    # are suppressed because this is a structural identifiability audit.
    Krec = lmt**2 * T

    return {
        "clock": clock,
        "lmt": lmt,
        "T": T,
        "Tprime": Tprime,
        "qref": qref,
        "Kacc": Kacc,
        "Krec": Krec,
    }


def additive_nuisance(nshot: int) -> np.ndarray:
    """Separate offset + linear + quadratic drift in each channel."""
    t = sequence(nshot)["clock"]
    A = np.column_stack([np.ones(nshot), t, t**2])
    Z = np.zeros_like(A)
    return np.block([[A, Z], [Z, A]])


def fisher_metrics(F: np.ndarray, theta_index: int = 0) -> dict[str, float | int | bool]:
    """Rank plus estimability of theta from the Fisher null space."""
    F = 0.5 * (F + F.T)
    eigval, eigvec = np.linalg.eigh(F)
    scale = max(float(np.max(np.abs(eigval))), 1.0)
    tol = 1e-10 * scale
    positive = eigval > tol
    rank = int(np.sum(positive))
    null = eigvec[:, ~positive]
    theta_null_overlap = (
        float(np.linalg.norm(null[theta_index, :])) if null.shape[1] else 0.0
    )
    theta_estimable = theta_null_overlap < 1e-8

    if theta_estimable:
        e = np.zeros(F.shape[0])
        e[theta_index] = 1.0
        theta_variance = float(e @ np.linalg.pinv(F, rcond=1e-12) @ e)
        theta_sigma = math.sqrt(max(theta_variance, 0.0))
    else:
        theta_sigma = math.inf

    positive_eigs = eigval[positive]
    condition_nonzero = (
        float(np.max(positive_eigs) / np.min(positive_eigs))
        if positive_eigs.size
        else math.inf
    )
    return {
        "rank": rank,
        "dimension": int(F.shape[0]),
        "full_rank": rank == F.shape[0],
        "theta_null_overlap": theta_null_overlap,
        "theta_estimable": theta_estimable,
        "theta_sigma": theta_sigma,
        "condition_nonzero": condition_nonzero,
    }


def common_clock_fisher(
    *,
    nshot: int = 96,
    rho: float = 0.7,
    theta: float = 0.2,
    reference_amplitude: float = 0.4,
    reference_mode: str = "known_modulated",
    include_recoil: bool = True,
    recoil_gain: float = 1.0,
) -> np.ndarray:
    """Fisher for [theta, kappa_k, kappa_clock] (+ alpha if unknown ref)."""
    s = sequence(nshot)
    K = s["Kacc"]
    R = recoil_gain * s["Krec"]
    q = s["qref"]
    z = np.zeros(nshot)

    if reference_mode == "none":
        ref = np.zeros(nshot)
        unknown_alpha = False
    elif reference_mode == "known_modulated":
        ref = reference_amplitude * q
        unknown_alpha = False
    elif reference_mode == "unknown_modulated":
        ref = reference_amplitude * q
        unknown_alpha = True
    else:
        raise ValueError("unknown reference_mode")

    base = K * (theta + ref)
    dtheta = np.r_[K, z]
    dk = np.r_[base, 2.0 * R if include_recoil else z]
    dt = np.r_[2.0 * base, R if include_recoil else z]
    columns = [dtheta, dk, dt]
    if unknown_alpha:
        columns.append(np.r_[K * q, z])
    J = np.column_stack(columns)

    C = paired_covariance(nshot, rho)
    P = profiled_precision(C, additive_nuisance(nshot))
    return J.T @ P @ J


def split_timing_fisher(
    *,
    nshot: int = 96,
    rho: float = 0.7,
    theta: float = 0.2,
    reference_amplitude: float = 0.4,
) -> np.ndarray:
    """Fisher for [theta,kappa_k,kappa_T,kappa_Tprime] with known reference.

    This tests a stricter model where T and T' have independent fractional
    calibration errors rather than a shared timebase scale.
    """
    s = sequence(nshot)
    T = s["T"]
    Tp = s["Tprime"]
    K = s["Kacc"]
    R = s["Krec"]
    q = s["qref"]
    z = np.zeros(nshot)
    base = K * (theta + reference_amplitude * q)

    # For f=T(T+T'):
    # d ln f / d ln T  = (2T + T')/(T + T')
    # d ln f / d ln T' = T'/(T + T')
    eT = (2.0 * T + Tp) / (T + Tp)
    eTp = Tp / (T + Tp)
    assert np.allclose(eT + eTp, 2.0)

    J = np.column_stack([
        np.r_[K, z],
        np.r_[base, 2.0 * R],
        np.r_[eT * base, R],
        np.r_[eTp * base, z],
    ])
    C = paired_covariance(nshot, rho)
    P = profiled_precision(C, additive_nuisance(nshot))
    return J.T @ P @ J


def prior_assisted_unknown_reference(
    sigma_alpha: float,
    *,
    nshot: int = 96,
    rho: float = 0.7,
) -> np.ndarray:
    if sigma_alpha <= 0.0:
        raise ValueError("sigma_alpha must be positive")
    F = common_clock_fisher(
        nshot=nshot,
        rho=rho,
        reference_mode="unknown_modulated",
        include_recoil=True,
    )
    P = np.zeros_like(F)
    P[3, 3] = 1.0 / sigma_alpha**2
    return F + P


def structural_assertions() -> None:
    # 1) Recoil alone does not repair the theta-vs-acceleration-scale degeneracy.
    m = fisher_metrics(common_clock_fisher(reference_mode="none", include_recoil=True))
    assert not m["theta_estimable"]
    assert m["rank"] == 2 and m["dimension"] == 3

    # 2) A calibrated modulated acceleration reference makes theta estimable,
    # even if k and T are not separately identifiable.
    m = fisher_metrics(
        common_clock_fisher(reference_mode="known_modulated", include_recoil=False)
    )
    assert m["theta_estimable"]
    assert not m["full_rank"]
    assert m["rank"] == 2 and m["dimension"] == 3

    # 3) Adding recoil closes the two common scale parameters as well.
    m = fisher_metrics(
        common_clock_fisher(reference_mode="known_modulated", include_recoil=True)
    )
    assert m["theta_estimable"] and m["full_rank"]
    assert m["rank"] == 3

    # 4) If the injected-reference amplitude is itself unconstrained, the
    # degeneracy returns and it mixes with theta.
    m = fisher_metrics(
        common_clock_fisher(reference_mode="unknown_modulated", include_recoil=True)
    )
    assert not m["theta_estimable"]
    assert m["rank"] == 3 and m["dimension"] == 4

    # 5) If T and T' carry independent scale errors, acceleration+recoil only
    # constrain two calibration combinations; one apparatus-only null mode
    # remains. Crucially theta is still estimable with a known reference.
    m = fisher_metrics(split_timing_fisher())
    assert m["theta_estimable"]
    assert not m["full_rank"]
    assert m["rank"] == 3 and m["dimension"] == 4

    # 6) Strong correlated noise does not alter structural rank/estimability.
    for rho in [0.0, 0.5, 0.9, 0.98]:
        m = fisher_metrics(
            common_clock_fisher(
                rho=rho,
                reference_mode="known_modulated",
                include_recoil=True,
            )
        )
        assert m["theta_estimable"] and m["full_rank"]

    # 7) A prior on unknown reference amplitude restores theta only as
    # PRIOR-ASSISTED closure, never as apparatus self-calibration.
    for sigma_alpha in [0.5, 0.05, 0.005]:
        m = fisher_metrics(prior_assisted_unknown_reference(sigma_alpha))
        assert m["theta_estimable"] and m["full_rank"]


def scenario_table() -> list[tuple[str, dict[str, float | int | bool]]]:
    cases = [
        (
            "no_ref + recoil",
            common_clock_fisher(reference_mode="none", include_recoil=True),
        ),
        (
            "known_mod_ref, no_recoil",
            common_clock_fisher(
                reference_mode="known_modulated", include_recoil=False
            ),
        ),
        (
            "known_mod_ref + recoil",
            common_clock_fisher(
                reference_mode="known_modulated", include_recoil=True
            ),
        ),
        (
            "unknown_mod_ref + recoil",
            common_clock_fisher(
                reference_mode="unknown_modulated", include_recoil=True
            ),
        ),
        (
            "known_ref + recoil, split T/Tprime",
            split_timing_fisher(),
        ),
    ]
    return [(name, fisher_metrics(F)) for name, F in cases]


def print_audit() -> None:
    print("RQIR Paper III physical AI science-estimability audit")
    print("scenario | rank | theta_estimable | full_calibration | theta_sigma")
    for name, m in scenario_table():
        sigma = m["theta_sigma"]
        sigma_text = "inf" if not math.isfinite(float(sigma)) else f"{float(sigma):.8g}"
        print(
            f"{name:38s} | {m['rank']}/{m['dimension']} | "
            f"{str(m['theta_estimable']):5s} | "
            f"{str(m['full_rank']):5s} | {sigma_text}"
        )

    print("\nStructural conclusions")
    print("recoil without calibrated acceleration reference: SCIENCE NON_IDENTIFIABLE")
    print("known modulated reference, no recoil: THETA ESTIMABLE / CALIBRATION PARTIAL")
    print("known modulated reference + recoil: THETA ESTIMABLE / COMMON-CLOCK FULL RANK")
    print("unknown reference amplitude + recoil: SCIENCE NON_IDENTIFIABLE")
    print("independent T and T' scales: THETA ESTIMABLE / ONE APPARATUS-ONLY NULL MODE")
    print("correlated covariance rho<=0.98: STRUCTURAL RESULT STABLE")
    print("unknown reference + finite prior: PRIOR-ASSISTED CLOSURE")
    print("RQIR science-estimability gate: PASS WITH EXPLICIT FAILURE DOMAINS")


def main() -> None:
    structural_assertions()
    print_audit()


if __name__ == "__main__":
    main()
