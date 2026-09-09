"""RQIR Paper III — physical atom-interferometer self-calibration audit.

This audit maps the abstract apparatus self-calibration criterion onto leading
light-pulse atom-interferometer (AI) phase scalings. It is deliberately a
structural/identifiability test, not a forecast for a particular apparatus.

Physical leading-order channels
-------------------------------
For an acceleration-like science amplitude theta, a 3-pulse/LMT light-pulse AI
has the leading scaling

    phi_acc = s * n * k_eff * T**2 * theta,

where s is the momentum-transfer sign/reversal, n is an LMT order (or an
equivalent known momentum multiplier), k_eff is the effective wave vector, and
T is an interrogation time. Thus common fractional calibration errors obey

    d phi / d kappa_k = theta * K,
    d phi / d kappa_T = 2 * theta * K,

with K = s*n*k_eff*T**2. Changing s, n, or T only changes K and therefore does
NOT separate theta from a common multiplicative scale in the science channel.

A known injected acceleration/reference r_j changes the channel to

    phi_acc,j = K_j * (theta + r_j).

It can identify the combined acceleration-scale mode
    gamma_acc = kappa_k + 2*kappa_T
when r_j varies independently enough after covariance/nuisance projection, but
kappa_k and kappa_T themselves remain mutually degenerate because their
derivative columns are still in the fixed ratio 1:2.

A recoil-like calibration observable has a different leading scaling

    phi_rec ~ n**2 * k_eff**2 * T,

so its fractional scale direction is
    gamma_rec = 2*kappa_k + kappa_T.

The exponent vectors (1,2) and (2,1) are linearly independent. If both
calibration combinations carry nonzero Fisher information, their 2x2
calibration Fisher determinant is

    det F_cal = 9 * I_acc * I_rec > 0.

Therefore an acceleration/reference channel plus an independent recoil-like
channel can, in principle, self-calibrate k_eff and T at first order. This is
an identifiability statement only; actual resource closure still requires
apparatus-specific covariance, contrast, dead time, transfer functions, and
calibration uncertainties.

References used for the physical scalings:
- Hogan, Johnson & Kasevich, "Light-pulse atom interferometry",
  arXiv:0806.3261.
- Lan et al., Phys. Rev. Lett. 108, 090402 (2012):
  Ramsey-Borde/LMT phase contains recoil ~ n^2 k^2 T and gravity ~ n k g T(...)
- "Practical Limits for Large-Momentum-Transfer Clock Atom Interferometers",
  PRX Quantum 3, 030348 (2022): leading inertial phase ~ n k g T^2.
"""
from __future__ import annotations

import math
import numpy as np


def ar1_covariance(n: int, rho: float, sigma: float = 1.0) -> np.ndarray:
    if n < 4:
        raise ValueError("n must be >= 4")
    if not (-1.0 < rho < 1.0):
        raise ValueError("rho must satisfy |rho| < 1")
    idx = np.arange(n)
    return sigma**2 * rho ** np.abs(idx[:, None] - idx[None, :])


def nuisance_precision_projector(cov: np.ndarray, nuisance: np.ndarray) -> np.ndarray:
    """Precision-space projector after profiling additive linear nuisances."""
    cinv = np.linalg.inv(cov)
    normal = nuisance.T @ cinv @ nuisance
    return cinv - cinv @ nuisance @ np.linalg.solve(normal, nuisance.T @ cinv)


def projected_gram(g: np.ndarray, h: np.ndarray, proj: np.ndarray) -> tuple[float, float, float, float]:
    gg = float(g @ proj @ g)
    gh = float(g @ proj @ h)
    hh = float(h @ proj @ h)
    det = gg * hh - gh * gh
    return gg, gh, hh, det


def orthogonal_information(g: np.ndarray, h: np.ndarray, proj: np.ndarray) -> float:
    """Information in h that is not parallel to g in the profiled metric."""
    gg = float(g @ proj @ g)
    gh = float(g @ proj @ h)
    hh = float(h @ proj @ h)
    if gg <= 0.0:
        raise AssertionError("science direction must retain positive information")
    value = hh - gh * gh / gg
    scale = max(abs(hh), abs(gh * gh / gg), 1.0)
    if abs(value) <= 1e-12 * scale:
        return 0.0
    return value


def physical_sequence(nshot: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Dimensionless sequence using reversal, timing and LMT changes.

    Exact SI values are intentionally absent: only rank/geometry matters here.
    """
    j = np.arange(nshot)
    sign = np.where(j % 2 == 0, 1.0, -1.0)
    timing = np.where((j // 2) % 2 == 0, 1.0, 1.25)
    lmt = np.where((j // 4) % 2 == 0, 1.0, 2.0)
    k_eff = 1.0
    K = sign * lmt * k_eff * timing**2
    t = np.linspace(-1.0, 1.0, nshot)
    return t, K, timing


def acceleration_scale_identifiability(
    nshot: int,
    rho: float,
    reference: np.ndarray,
    theta: float = 0.2,
) -> dict[str, float | str]:
    """Profile offset/drift and test theta vs combined acceleration-scale gain."""
    t, K, _ = physical_sequence(nshot)
    if reference.shape != (nshot,):
        raise ValueError("reference must have shape (nshot,)")

    nuisance = np.column_stack([np.ones(nshot), t, t**2])
    proj = nuisance_precision_projector(ar1_covariance(nshot, rho), nuisance)

    dtheta = K
    dgamma_acc = K * (theta + reference)
    gg, gh, hh, det = projected_gram(dtheta, dgamma_acc, proj)
    i_orth = orthogonal_information(dtheta, dgamma_acc, proj)

    return {
        "science_info": gg,
        "gain_info_raw": hh,
        "gram_det": det,
        "gain_info_orthogonal_to_science": i_orth,
        "classification": "SELF_CALIBRATING_COMBINED_GAIN" if i_orth > 0.0 else "NON_IDENTIFIABLE",
    }


def full_science_jacobian(
    nshot: int,
    reference: np.ndarray,
    theta: float = 0.2,
) -> np.ndarray:
    """Columns [theta, kappa_k, kappa_T, phase0, drift1, drift2]."""
    t, K, _ = physical_sequence(nshot)
    base = K * (theta + reference)
    return np.column_stack([
        K,
        base,
        2.0 * base,
        np.ones(nshot),
        t,
        t**2,
    ])


def calibration_fisher(I_acc: float, I_rec: float) -> np.ndarray:
    """Fisher for [kappa_k, kappa_T] from two independent scale combinations."""
    if I_acc < 0.0 or I_rec < 0.0:
        raise ValueError("information values must be non-negative")
    e_acc = np.array([1.0, 2.0])
    e_rec = np.array([2.0, 1.0])
    return I_acc * np.outer(e_acc, e_acc) + I_rec * np.outer(e_rec, e_rec)


def structural_assertions() -> None:
    n = 96
    theta = 0.2

    zero_ref = np.zeros(n)
    for rho in [0.0, 0.5, 0.9]:
        result = acceleration_scale_identifiability(n, rho, zero_ref, theta)
        assert result["classification"] == "NON_IDENTIFIABLE"

    constant_ref = np.full(n, 0.4)
    for rho in [0.0, 0.5, 0.9]:
        result = acceleration_scale_identifiability(n, rho, constant_ref, theta)
        assert result["classification"] == "NON_IDENTIFIABLE"

    j = np.arange(n)
    modulated_ref = 0.4 * np.where((j // 8) % 2 == 0, 1.0, -1.0)
    for rho in [0.0, 0.5, 0.9]:
        result = acceleration_scale_identifiability(n, rho, modulated_ref, theta)
        assert result["classification"] == "SELF_CALIBRATING_COMBINED_GAIN"
        assert result["gain_info_orthogonal_to_science"] > 0.0

    jac = full_science_jacobian(n, modulated_ref, theta)
    assert np.allclose(jac[:, 2], 2.0 * jac[:, 1], rtol=0.0, atol=0.0)
    assert np.linalg.matrix_rank(jac, tol=1e-10) < jac.shape[1]

    for I_acc, I_rec in [(1.0, 1.0), (3.0, 0.2), (0.05, 20.0)]:
        F = calibration_fisher(I_acc, I_rec)
        det = float(np.linalg.det(F))
        assert math.isclose(det, 9.0 * I_acc * I_rec, rel_tol=1e-12, abs_tol=1e-12)
        assert np.linalg.matrix_rank(F, tol=1e-12) == 2

    assert np.linalg.matrix_rank(calibration_fisher(1.0, 0.0), tol=1e-12) == 1
    assert np.linalg.matrix_rank(calibration_fisher(0.0, 1.0), tol=1e-12) == 1


def print_audit() -> None:
    n = 96
    theta = 0.2
    j = np.arange(n)
    refs = {
        "none": np.zeros(n),
        "constant": np.full(n, 0.4),
        "modulated": 0.4 * np.where((j // 8) % 2 == 0, 1.0, -1.0),
    }
    print("RQIR physical atom-interferometer self-calibration audit")
    print("reference rho orthogonal_gain_info classification")
    for name, ref in refs.items():
        for rho in [0.0, 0.5, 0.9]:
            result = acceleration_scale_identifiability(n, rho, ref, theta)
            print(
                f"{name:9s} {rho:3.1f} "
                f"{result['gain_info_orthogonal_to_science']:.9g} "
                f"{result['classification']}"
            )

    print("science-only k-reversal / T / LMT variation: NON_IDENTIFIABLE")
    print("constant known reference: NON_IDENTIFIABLE")
    print("modulated known acceleration reference: COMBINED GAIN SELF-CALIBRATING")
    print("separate k_eff vs T calibration from acceleration channel alone: NON_IDENTIFIABLE")
    print("acceleration exponent vector: (1,2)")
    print("recoil exponent vector:       (2,1)")
    print("det F_cal = 9 I_acc I_rec: PASS")
    print("acceleration + recoil calibration geometry: FULL RANK")
    print("RQIR physical AI identifiability audit: PASS WITH EXPLICIT FAILURE DOMAINS")


def main() -> None:
    structural_assertions()
    print_audit()


if __name__ == "__main__":
    main()
