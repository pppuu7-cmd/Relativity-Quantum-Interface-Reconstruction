"""RQIR Paper III — detector-facing transition-probability likelihood audit.

This audit upgrades the same-apparatus Figure-8 PSD calculation from a Gaussian
phase observable to the measured atom-interferometer output probability

    P = 1/2 [1 + C cos(Phi)]

near mid-fringe.  It profiles detector and apparatus nuisances simultaneously
while retaining the source-traceable physical phase covariance from
`atom_gravimeter_figure8_psd_covariance_audit.py`.

Source anchors
--------------
Le Gouet et al., Appl. Phys. B 92, 133-144 (2008), arXiv:0801.1270 report:
- transition probability measured at mid-fringe P=0.5;
- technical detection floor sigma_P ~ 3e-4 for >5e6 atoms;
- sigma_phi = 2 sigma_P / C;
- sensitivity close to 1 mrad/shot from the detection, implying an effective
  working contrast C ~ 0.6 (used here as an approximate source-derived anchor);
- post-correction requires operation near mid-fringe, phase excursions below a
  few tens of degrees, and stable contrast.

The colored phase covariance comes from the coarse source-traceable digitization
of their passive-platform Fig. 8 already validated in the preceding RQIR audit.

Likelihood approximation
------------------------
The measured probability is treated as Gaussian because the source-grounded
technical detection floor is itself an empirical probability-noise standard
deviation.  Correlated phase noise is propagated through the *local nonlinear
probability slope* for every shot:

    C_P = D C_phi D + sigma_P^2 I,
    D_ii = d P_i / d Phi_i.

The Fisher calculation deliberately uses mean information only and freezes this
covariance at the nominal/stress point.  It therefore does NOT gain artificial
science information from parameter-dependence of the noise amplitude.

Nuisances profiled together
---------------------------
- common acceleration scale/readout phase gain gamma;
- phase offset + linear/quadratic phase drift;
- absolute contrast + linear/quadratic contrast drift;
- centered probability readout gain + linear gain drift;
- probability readout offset;
- injected reference amplitude alpha when not fixed.

An apparatus-only rank deficiency is permitted if every Fisher null direction
has zero overlap with the RQIR science amplitude theta.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.linalg import matmul_toeplitz
from scipy.sparse.linalg import LinearOperator, cg

from atom_gravimeter_figure8_psd_covariance_audit import (
    K_G,
    TC,
    REFERENCE_UG,
    SCIENCE_F_HZ,
    REFERENCE_F_HZ,
    accel_response,
    total_covariance_lags,
)

SIGMA_P = 3.0e-4
DETECTION_PHASE_TARGET = 1.0e-3
C0 = 2.0 * SIGMA_P / DETECTION_PHASE_TARGET  # ~0.6 source-implied contrast


def templates(nshot: int, science_modulated: bool = True) -> tuple[np.ndarray, ...]:
    t = np.arange(nshot, dtype=float) * TC
    x = np.linspace(-1.0, 1.0, nshot)
    if science_modulated:
        science = np.sin(2.0 * math.pi * SCIENCE_F_HZ * t)
        science *= float(accel_response(SCIENCE_F_HZ))
    else:
        science = np.ones(nshot)
    reference = np.sin(2.0 * math.pi * REFERENCE_F_HZ * t + 0.37)
    reference *= float(accel_response(REFERENCE_F_HZ))
    return t, x, science, reference


def detector_mean_jacobian(
    nshot: int,
    *,
    theta_ng: float = 1.0,
    alpha_ug: float = REFERENCE_UG,
    science_modulated: bool = True,
    use_reference: bool = True,
    reference_unknown: bool = True,
    gamma: float = 0.0,
    phase_offset: float = 0.0,
    phase_linear: float = 0.0,
    phase_quadratic: float = 0.0,
    contrast: float = C0,
    contrast_linear: float = 0.0,
    contrast_quadratic: float = 0.0,
    read_gain: float = 0.0,
    read_gain_linear: float = 0.0,
    read_offset: float = 0.0,
) -> tuple[np.ndarray, np.ndarray, tuple[str, ...], np.ndarray]:
    """Return probability mean, mean Jacobian, names, and local dP/dPhi.

    read_gain is defined for the centered probability (P-1/2), making it a
    conservative detector-gain nuisance rather than obtaining gain information
    trivially from the fixed 1/2 population baseline.
    """
    _, x, s, q = templates(nshot, science_modulated=science_modulated)
    if not use_reference:
        q = np.zeros_like(q)
        alpha_ug = 0.0

    theta_g = theta_ng * 1.0e-9
    alpha_g = alpha_ug * 1.0e-6
    physical_phase = K_G * (1.0 + gamma) * (theta_g * s + alpha_g * q)
    phase = (
        math.pi / 2.0
        + physical_phase
        + phase_offset
        + phase_linear * x
        + phase_quadratic * x**2
    )

    cshape = 1.0 + contrast_linear * x + contrast_quadratic * x**2
    C = contrast * cshape
    gain = 1.0 + read_gain + read_gain_linear * x

    fringe = 0.5 + 0.5 * C * np.cos(phase)
    mean = 0.5 + read_offset + gain * (fringe - 0.5)

    # Local phase-noise slope and phase derivatives.
    slope = -0.5 * gain * C * np.sin(phase)
    dtheta = slope * K_G * (1.0 + gamma) * 1.0e-9 * s
    dgamma = slope * K_G * (theta_g * s + alpha_g * q)

    trig = np.cos(phase)
    columns = [
        dtheta,
        dgamma,
        slope,
        slope * x,
        slope * x**2,
        gain * 0.5 * cshape * trig,
        gain * 0.5 * contrast * x * trig,
        gain * 0.5 * contrast * x**2 * trig,
        fringe - 0.5,
        x * (fringe - 0.5),
        np.ones(nshot),
    ]
    names = [
        "theta_ng",
        "gamma",
        "phase_offset",
        "phase_linear",
        "phase_quadratic",
        "contrast",
        "contrast_linear",
        "contrast_quadratic",
        "read_gain",
        "read_gain_linear",
        "read_offset",
    ]

    if reference_unknown:
        dalpha = slope * K_G * (1.0 + gamma) * 1.0e-6 * q
        columns.append(dalpha)
        names.append("alpha_ug")

    return mean, np.column_stack(columns), tuple(names), slope


def probability_precision_action(
    phase_lags: np.ndarray,
    slope: np.ndarray,
) -> tuple[LinearOperator, LinearOperator]:
    """Return covariance LinearOperator and Jacobi preconditioner."""
    n = slope.size

    def matvec(v: np.ndarray) -> np.ndarray:
        colored = matmul_toeplitz(
            (phase_lags, phase_lags), slope * v, check_finite=False
        )
        return slope * colored + SIGMA_P**2 * v

    cov = LinearOperator((n, n), matvec=matvec, dtype=float)
    diagonal = slope**2 * phase_lags[0] + SIGMA_P**2
    preconditioner = LinearOperator(
        (n, n), matvec=lambda v: v / diagonal, dtype=float
    )
    return cov, preconditioner


def detector_fisher(
    nshot: int,
    *,
    reference_prior_fraction: float | None = None,
    **mean_kwargs,
) -> tuple[np.ndarray, tuple[str, ...], list[int]]:
    _, J, names, slope = detector_mean_jacobian(nshot, **mean_kwargs)
    phase_lags = total_covariance_lags(nshot)
    cov, preconditioner = probability_precision_action(phase_lags, slope)

    cinv_j = np.empty_like(J)
    solver_info: list[int] = []
    for j in range(J.shape[1]):
        sol, info = cg(
            cov,
            J[:, j],
            M=preconditioner,
            rtol=1.0e-9,
            atol=0.0,
            maxiter=3000,
        )
        cinv_j[:, j] = sol
        solver_info.append(int(info))

    F = J.T @ cinv_j
    F = 0.5 * (F + F.T)

    if reference_prior_fraction is not None:
        if "alpha_ug" not in names:
            raise ValueError("reference prior requested but alpha is not a parameter")
        if reference_prior_fraction <= 0.0:
            raise ValueError("reference prior must be positive")
        i = names.index("alpha_ug")
        sigma_alpha = REFERENCE_UG * reference_prior_fraction
        F[i, i] += 1.0 / sigma_alpha**2

    return F, names, solver_info


def estimability(F: np.ndarray, names: tuple[str, ...]) -> dict[str, object]:
    """Rank/null-space test in parameter-normalized Fisher coordinates."""
    d = np.sqrt(np.clip(np.diag(F), 1.0e-300, None))
    scale = np.diag(1.0 / d)
    Fn = scale @ F @ scale
    Fn = 0.5 * (Fn + Fn.T)
    eigenvalues, eigenvectors = np.linalg.eigh(Fn)
    positive = eigenvalues > 1.0e-8
    null = eigenvectors[:, ~positive]
    theta_index = names.index("theta_ng")
    theta_overlap = (
        float(np.linalg.norm(null[theta_index, :])) if null.shape[1] else 0.0
    )
    theta_estimable = theta_overlap < 1.0e-6

    if theta_estimable:
        covariance = scale @ np.linalg.pinv(Fn, rcond=1.0e-8) @ scale
        sigma_theta = math.sqrt(max(float(covariance[theta_index, theta_index]), 0.0))
    else:
        sigma_theta = math.inf

    return {
        "rank": int(np.sum(positive)),
        "dimension": int(F.shape[0]),
        "nullity": int(F.shape[0] - np.sum(positive)),
        "theta_estimable": bool(theta_estimable),
        "theta_null_overlap": theta_overlap,
        "sigma_theta_ng": sigma_theta,
        "normalized_eigenvalues": eigenvalues,
    }


def campaign(seconds: float, **kwargs) -> dict[str, object]:
    nshot = int(round(seconds / TC))
    F, names, solver_info = detector_fisher(nshot, **kwargs)
    if any(info != 0 for info in solver_info):
        raise RuntimeError(f"CG did not converge: {solver_info}")
    result = estimability(F, names)
    result["shots"] = nshot
    return result


def calibration_floor_scan(theta_ng: float = 100.0) -> list[dict[str, float]]:
    """Expose the detector-facing statistical/calibration transition."""
    # Very tight prior is used as a practical statistical-only baseline.
    base = campaign(
        60.0,
        theta_ng=theta_ng,
        reference_unknown=True,
        reference_prior_fraction=1.0e-6,
    )
    stat = float(base["sigma_theta_ng"])
    rows = []
    for frac in [0.10, 0.03, 0.01, 0.003, 0.001]:
        result = campaign(
            60.0,
            theta_ng=theta_ng,
            reference_unknown=True,
            reference_prior_fraction=frac,
        )
        predicted = math.sqrt(stat**2 + (theta_ng * frac) ** 2)
        measured = float(result["sigma_theta_ng"])
        rows.append(
            {
                "fraction": frac,
                "sigma_theta_ng": measured,
                "quadrature_prediction_ng": predicted,
                "relative_error": abs(measured / predicted - 1.0),
            }
        )
    return rows


def structural_assertions() -> None:
    assert abs(C0 - 0.6) < 1.0e-12

    # Static science remains lost to a free phase offset even with reference.
    m = campaign(
        60.0,
        science_modulated=False,
        use_reference=True,
        reference_unknown=True,
        reference_prior_fraction=0.01,
    )
    assert not m["theta_estimable"]

    # Modulation alone cannot close the absolute common phase scale.
    m = campaign(
        60.0,
        science_modulated=True,
        use_reference=False,
        reference_unknown=False,
    )
    assert not m["theta_estimable"]

    # Unknown reference with no external calibration keeps theta non-estimable.
    m = campaign(
        60.0,
        science_modulated=True,
        use_reference=True,
        reference_unknown=True,
        reference_prior_fraction=None,
    )
    assert not m["theta_estimable"]

    # Finite source-reference calibration restores theta estimability even though
    # apparatus-only contrast/readout null directions are allowed to remain.
    for frac in [0.10, 0.01, 0.001]:
        m = campaign(
            60.0,
            science_modulated=True,
            use_reference=True,
            reference_unknown=True,
            reference_prior_fraction=frac,
        )
        assert m["theta_estimable"]
        assert m["rank"] < m["dimension"]
        assert math.isfinite(float(m["sigma_theta_ng"]))

    # Stress true detector state inside the source-described mid-fringe regime.
    detector_stresses = [
        {"contrast": 0.48},                       # 20% lower contrast
        {"contrast_linear": 0.10},              # 10% campaign contrast drift
        {"contrast_quadratic": 0.10},
        {"read_gain_linear": 0.05},             # 5% readout-gain drift
        {"phase_offset": 0.20},                 # ~11.5 degrees
        {"phase_linear": 0.20},
        {
            "contrast": 0.48,
            "contrast_linear": 0.10,
            "contrast_quadratic": 0.05,
            "read_gain_linear": 0.05,
            "phase_offset": 0.15,
            "phase_linear": 0.10,
            "phase_quadratic": 0.05,
        },
    ]
    for stress in detector_stresses:
        m = campaign(
            60.0,
            reference_unknown=True,
            reference_prior_fraction=0.01,
            **stress,
        )
        assert m["theta_estimable"]

    # Physical detector-facing calibration floor follows the expected scale law.
    for row in calibration_floor_scan(theta_ng=100.0):
        assert row["relative_error"] < 0.01


def print_audit() -> None:
    print("RQIR detector-facing probability-likelihood audit")
    print(f"source detection floor sigma_P = {SIGMA_P:.6g}")
    print(f"source-implied effective working contrast C0 = {C0:.6g}")
    print(f"2 sigma_P / C0 = {2.0 * SIGMA_P / C0:.6g} rad")

    cases = [
        (
            "static science + 1% ref prior",
            dict(
                science_modulated=False,
                use_reference=True,
                reference_unknown=True,
                reference_prior_fraction=0.01,
            ),
        ),
        (
            "modulated science, no reference",
            dict(
                science_modulated=True,
                use_reference=False,
                reference_unknown=False,
            ),
        ),
        (
            "modulated + unknown uncalibrated ref",
            dict(
                science_modulated=True,
                use_reference=True,
                reference_unknown=True,
            ),
        ),
        (
            "modulated + 10% ref prior",
            dict(
                science_modulated=True,
                use_reference=True,
                reference_unknown=True,
                reference_prior_fraction=0.10,
            ),
        ),
        (
            "modulated + 1% ref prior",
            dict(
                science_modulated=True,
                use_reference=True,
                reference_unknown=True,
                reference_prior_fraction=0.01,
            ),
        ),
    ]

    print("\n60-s detector gate:")
    for name, kwargs in cases:
        m = campaign(60.0, **kwargs)
        sigma = float(m["sigma_theta_ng"])
        sigma_text = "inf" if not math.isfinite(sigma) else f"{sigma:.6g} ng"
        print(
            f"{name:40s} theta={m['theta_estimable']} "
            f"rank={m['rank']}/{m['dimension']} sigma={sigma_text}"
        )

    print("\nResource scaling, theta=1 ng, unknown reference:")
    for seconds in [60.0, 600.0]:
        for frac in [0.10, 0.01, 0.001]:
            m = campaign(
                seconds,
                theta_ng=1.0,
                reference_unknown=True,
                reference_prior_fraction=frac,
            )
            print(
                f"t={seconds:6.0f}s ref={100*frac:6.3f}% "
                f"sigma_theta={float(m['sigma_theta_ng']):.7g} ng"
            )

    print("\nDetector-facing calibration-floor check at theta=100 ng, 60 s:")
    for row in calibration_floor_scan(theta_ng=100.0):
        print(
            f"ref={100*row['fraction']:6.3f}% "
            f"sigma={row['sigma_theta_ng']:.7g} ng "
            f"quadrature={row['quadrature_prediction_ng']:.7g} ng "
            f"rel.err={row['relative_error']:.3%}"
        )

    print("\nDecision:")
    print("NONLINEAR TRANSITION-PROBABILITY SCIENCE ESTIMABILITY: PASS")
    print("CONTRAST/READOUT APPARATUS-ONLY NULL MODES: PRESENT BUT THETA-ORTHOGONAL")
    print("UNCALIBRATED REFERENCE ABSOLUTE SCALE: FAIL")
    print("FINITE REFERENCE CALIBRATION: PASS WITH EXPLICIT CALIBRATION FLOOR")
    print("FINAL RAW CAMPAIGN / CERTIFIED REFERENCE METROLOGY: STILL OPEN")


def main() -> None:
    structural_assertions()
    print_audit()


if __name__ == "__main__":
    main()
