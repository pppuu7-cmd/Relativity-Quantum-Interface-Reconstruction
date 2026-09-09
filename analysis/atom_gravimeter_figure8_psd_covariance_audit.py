"""RQIR Paper III — source-traceable Figure-8 PSD covariance audit.

This audit replaces the synthetic AR(1) covariance stress family used in the
first same-apparatus closure with a continuous acceleration-noise PSD envelope
read from Fig. 8 of Le Gouet et al., Appl. Phys. B 92, 133-144 (2008),
arXiv:0801.1270, and propagated through the three-pulse atom-interferometer
acceleration transfer function.

Important provenance rule
-------------------------
The frequency/ASD knots below are a deliberately coarse, human-readable
log-log digitization of the *passive-platform* trace in published Fig. 8. They
are NOT raw experimental data and are never presented as such. Their absolute
scale is not fitted to the paper's integrated sensitivity. As an independent
validation, the propagated curve predicts 6.35e-8 g at 1 s, versus the paper's
6.5e-8 g inferred vibration limit (about 2.3% difference).

The paper further reports:
- vibration correction efficiency about 3, giving typical 2e-8 g at 1 s;
- correlation coefficient up to 0.94 between seismometer acceleration noise
  and atom-interferometer phase noise under minimal-noise conditions;
- best total phase noise 11 mrad/shot;
- quadrature sum of independently evaluated non-vibration contributions
  about 4 mrad/shot;
- a broad crosstalk-related structure near 2 Hz, with horizontal acceleration
  noise up to 6e-7 g/Hz^1/2 and few-percent horizontal/vertical crosstalk.

The covariance is obtained directly from the one-sided continuous phase PSD:

    C_l = integral_0^inf S_phi(f) cos(2 pi f l Tc) df,
    S_phi(f) = [K_g R_a(f)]^2 S_a(f),
    R_a(f) = sinc(f T)^2.

Sampling/aliasing is therefore included automatically in the sampled covariance
through evaluation at shot separations l Tc.

Requires NumPy and SciPy (solve_toeplitz).
"""
from __future__ import annotations

import math
import numpy as np
from scipy.linalg import solve_toeplitz

G0 = 9.80665
LAMBDA = 780e-9
K_EFF = 4.0 * math.pi / LAMBDA
T = 0.050
TC = 0.250
FC = 1.0 / TC
K_G = K_EFF * T**2 * G0

SCIENCE_F_HZ = 0.5
REFERENCE_F_HZ = 1.0
REFERENCE_UG = 1.0
OTHER_PHASE_RMS = 4e-3
REJECTION = 3.0

# Coarse log-log read-off of the passive-platform curve in published Fig. 8.
# End anchors merely regularize extrapolation outside the plotted core range.
PSD_FREQ_HZ = np.array([
    0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50, 0.70, 1.0,
    2.0, 3.0, 5.0, 10.0, 20.0, 30.0, 50.0, 70.0, 100.0, 200.0,
])
PSD_ASD_G = np.array([
    1e-9, 3e-9, 1e-8, 4e-8, 1.2e-7, 1.7e-7, 1.3e-7, 5e-8,
    2e-8, 2e-8, 1.8e-8, 2e-8, 2.2e-8, 2.3e-8, 2.5e-8,
    4e-8, 7e-8, 1e-7, 1e-7,
])


def accel_response(f_hz: np.ndarray | float) -> np.ndarray | float:
    """Normalized low-frequency three-pulse acceleration response."""
    return np.sinc(np.asarray(f_hz) * T) ** 2


def passive_asd(f_hz: np.ndarray | float, crosstalk_boost: float = 1.0) -> np.ndarray:
    """Log-log interpolated Fig.-8 passive-platform ASD, in g/sqrt(Hz).

    crosstalk_boost > 1 smoothly stresses the published broad ~2-Hz structure.
    This is a robustness test, not a claim that the nominal Fig.-8 trace is
    missing that exact multiplicative factor.
    """
    f = np.asarray(f_hz, dtype=float)
    clipped = np.clip(f, PSD_FREQ_HZ[0], PSD_FREQ_HZ[-1])
    base = 10.0 ** np.interp(
        np.log10(clipped), np.log10(PSD_FREQ_HZ), np.log10(PSD_ASD_G)
    )
    if crosstalk_boost <= 1.0:
        return base
    # Broad one-octave log-Gaussian stress centered at 2 Hz.
    width = math.log(2.0)
    bump = 1.0 + (crosstalk_boost - 1.0) * np.exp(
        -0.5 * (np.log(np.maximum(f, 1e-12) / 2.0) / width) ** 2
    )
    return base * bump


def integration_grid() -> np.ndarray:
    low = np.linspace(0.0005, 0.05, 120, endpoint=False)
    high = np.geomspace(0.05, 500.0, 24000)
    return np.unique(np.r_[low, high])


def vibration_covariance_lags(
    nlags: int,
    *,
    rejection: float = REJECTION,
    crosstalk_boost: float = 1.0,
) -> np.ndarray:
    if nlags < 1:
        raise ValueError("nlags must be positive")
    if rejection <= 0.0:
        raise ValueError("rejection must be positive")
    f = integration_grid()
    asd = passive_asd(f, crosstalk_boost=crosstalk_boost) / rejection
    sphi = (K_G * accel_response(f) * asd) ** 2
    lags = np.arange(nlags, dtype=float)[:, None]

    # Chunk frequency integration to keep memory bounded for long campaigns.
    out = np.zeros(nlags)
    chunk = 2000
    for start in range(0, f.size - 1, chunk):
        stop = min(start + chunk + 1, f.size)
        fs = f[start:stop]
        ss = sphi[start:stop]
        phase = 2.0 * math.pi * lags * (TC * fs[None, :])
        out += np.trapezoid(ss[None, :] * np.cos(phase), fs, axis=1)
    return out


def total_covariance_lags(
    nlags: int,
    *,
    rejection: float = REJECTION,
    crosstalk_boost: float = 1.0,
    other_phase_rms: float = OTHER_PHASE_RMS,
) -> np.ndarray:
    c = vibration_covariance_lags(
        nlags, rejection=rejection, crosstalk_boost=crosstalk_boost
    )
    c[0] += other_phase_rms**2
    return c


def mean_variance_from_lags(c: np.ndarray, n: int) -> float:
    if n > len(c):
        raise ValueError("need at least n covariance lags")
    val = n * c[0]
    for lag in range(1, n):
        val += 2.0 * (n - lag) * c[lag]
    return float(val / n**2)


def source_reproduction_checks() -> dict[str, float]:
    uncorrected = vibration_covariance_lags(4, rejection=1.0)
    sigma_uncorrected_g_1s = math.sqrt(mean_variance_from_lags(uncorrected, 4)) / K_G

    corrected_vib = vibration_covariance_lags(4, rejection=REJECTION)
    sigma_corrected_vib_g_1s = math.sqrt(mean_variance_from_lags(corrected_vib, 4)) / K_G

    total = total_covariance_lags(4, rejection=REJECTION)
    sigma_total_g_1s = math.sqrt(mean_variance_from_lags(total, 4)) / K_G

    return {
        "uncorrected_vibration_g_1s": sigma_uncorrected_g_1s,
        "paper_uncorrected_vibration_g_1s": 6.5e-8,
        "uncorrected_relative_error": abs(sigma_uncorrected_g_1s / 6.5e-8 - 1.0),
        "corrected_vibration_g_1s": sigma_corrected_vib_g_1s,
        "total_with_4mrad_g_1s": sigma_total_g_1s,
        "paper_typical_corrected_g_1s": 2.0e-8,
        "typical_corrected_relative_error": abs(sigma_total_g_1s / 2.0e-8 - 1.0),
    }


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


def design_matrix(
    nshot: int,
    *,
    theta_ng: float = 1.0,
    science_modulated: bool = True,
    use_reference: bool = True,
    reference_unknown: bool = False,
) -> np.ndarray:
    _, x, s, q = templates(nshot, science_modulated)
    if not use_reference:
        q = np.zeros_like(q)
    theta_g = theta_ng * 1e-9
    alpha_g = REFERENCE_UG * 1e-6 if use_reference else 0.0
    cols = [
        K_G * 1e-9 * s,
        K_G * (theta_g * s + alpha_g * q),
        np.ones(nshot),
        x,
        x**2,
    ]
    if reference_unknown:
        cols.append(K_G * 1e-6 * q)
    return np.column_stack(cols)


def fisher(
    nshot: int,
    *,
    crosstalk_boost: float = 1.0,
    science_modulated: bool = True,
    use_reference: bool = True,
    reference_unknown: bool = False,
) -> np.ndarray:
    c = total_covariance_lags(nshot, crosstalk_boost=crosstalk_boost)
    J = design_matrix(
        nshot,
        science_modulated=science_modulated,
        use_reference=use_reference,
        reference_unknown=reference_unknown,
    )
    cinv_j = solve_toeplitz((c, c), J, check_finite=False)
    F = J.T @ cinv_j
    return 0.5 * (F + F.T)


def estimability(F: np.ndarray, reference_prior_fraction: float | None = None) -> dict[str, object]:
    F = F.copy()
    if reference_prior_fraction is not None:
        if reference_prior_fraction <= 0.0:
            raise ValueError("reference prior must be positive")
        F[-1, -1] += 1.0 / (REFERENCE_UG * reference_prior_fraction) ** 2

    d = np.sqrt(np.clip(np.diag(F), 1e-300, None))
    S = np.diag(1.0 / d)
    Fn = S @ F @ S
    Fn = 0.5 * (Fn + Fn.T)
    w, v = np.linalg.eigh(Fn)
    positive = w > 1e-9
    null = v[:, ~positive]
    overlap = float(np.linalg.norm(null[0, :])) if null.shape[1] else 0.0
    theta_estimable = overlap < 1e-7
    if theta_estimable:
        cov = S @ np.linalg.pinv(Fn, rcond=1e-9) @ S
        sigma = math.sqrt(max(float(cov[0, 0]), 0.0))
    else:
        sigma = math.inf
    return {
        "rank": int(np.sum(positive)),
        "dimension": int(F.shape[0]),
        "theta_estimable": bool(theta_estimable),
        "theta_null_overlap": overlap,
        "sigma_theta_ng": sigma,
        "normalized_eigenvalues": w,
    }


def campaign(seconds: float, **kwargs) -> dict[str, object]:
    nshot = int(round(seconds / TC))
    prior = kwargs.pop("reference_prior_fraction", None)
    return estimability(fisher(nshot, **kwargs), reference_prior_fraction=prior)


def structural_assertions() -> None:
    r = source_reproduction_checks()
    # The coarse Fig.-8 trace must reproduce the paper's independent integrated
    # vibration forecast without an amplitude fit.
    assert r["uncorrected_relative_error"] < 0.05
    # Published factor-3 rejection + independent 4-mrad budget should reproduce
    # the paper's typical corrected scale at the ~10% level.
    assert r["typical_corrected_relative_error"] < 0.12

    assert not campaign(
        60.0, science_modulated=False, use_reference=True
    )["theta_estimable"]
    assert not campaign(
        60.0, science_modulated=True, use_reference=False
    )["theta_estimable"]

    good = campaign(
        60.0, science_modulated=True, use_reference=True
    )
    assert good["theta_estimable"] and math.isfinite(float(good["sigma_theta_ng"]))

    bad_ref = campaign(
        60.0,
        science_modulated=True,
        use_reference=True,
        reference_unknown=True,
    )
    assert not bad_ref["theta_estimable"]

    for frac in [1e-2, 1e-3, 1e-4]:
        good_ref = campaign(
            60.0,
            science_modulated=True,
            use_reference=True,
            reference_unknown=True,
            reference_prior_fraction=frac,
        )
        assert good_ref["theta_estimable"]

    # Robustness to a substantially enhanced broad 2-Hz crosstalk structure.
    for boost in [1.0, 2.0, 3.0, 5.0]:
        stressed = campaign(
            60.0,
            crosstalk_boost=boost,
            science_modulated=True,
            use_reference=True,
            reference_unknown=True,
            reference_prior_fraction=1e-3,
        )
        assert stressed["theta_estimable"]
        assert math.isfinite(float(stressed["sigma_theta_ng"]))


def print_audit() -> None:
    r = source_reproduction_checks()
    print("RQIR Figure-8 physical PSD covariance audit")
    print(
        "Fig-8 coarse digitization -> uncorrected vibration: "
        f"{r['uncorrected_vibration_g_1s']:.6g} g @1s "
        f"(paper 6.5e-8; rel.err={r['uncorrected_relative_error']:.3%})"
    )
    print(
        "factor-3 correction + 4 mrad independent floor: "
        f"{r['total_with_4mrad_g_1s']:.6g} g @1s "
        f"(paper typical 2e-8; rel.err={r['typical_corrected_relative_error']:.3%})"
    )

    cases = [
        ("static science + known ref", dict(science_modulated=False, use_reference=True)),
        ("modulated science, no ref", dict(science_modulated=True, use_reference=False)),
        ("modulated science + known ref", dict(science_modulated=True, use_reference=True)),
        (
            "modulated + unknown ref",
            dict(science_modulated=True, use_reference=True, reference_unknown=True),
        ),
        (
            "modulated + 0.1% ref prior",
            dict(
                science_modulated=True,
                use_reference=True,
                reference_unknown=True,
                reference_prior_fraction=1e-3,
            ),
        ),
    ]
    print("\n60-s physical-covariance gate:")
    for name, kw in cases:
        m = campaign(60.0, **kw)
        sigma = float(m["sigma_theta_ng"])
        st = "inf" if not math.isfinite(sigma) else f"{sigma:.6g} ng"
        print(
            f"{name:38s} estimable={m['theta_estimable']} "
            f"rank={m['rank']}/{m['dimension']} sigma={st}"
        )

    print("\n0.1% reference prior, nominal Fig-8 covariance:")
    for seconds in [60.0, 600.0, 3600.0]:
        m = campaign(
            seconds,
            science_modulated=True,
            use_reference=True,
            reference_unknown=True,
            reference_prior_fraction=1e-3,
        )
        print(f"{seconds:6.0f} s : sigma_theta = {m['sigma_theta_ng']:.6g} ng")

    print("\n2-Hz crosstalk stress, 60 s:")
    for boost in [1.0, 2.0, 3.0, 5.0]:
        m = campaign(
            60.0,
            crosstalk_boost=boost,
            science_modulated=True,
            use_reference=True,
            reference_unknown=True,
            reference_prior_fraction=1e-3,
        )
        print(f"boost x{boost:g}: sigma_theta = {m['sigma_theta_ng']:.6g} ng")

    print("\nDecision:")
    print("SOURCE-TRACEABLE PHYSICAL PSD/COVARIANCE GATE: PASS")
    print("FIG-8 INTEGRATED VIBRATION SCALE REPRODUCTION: PASS")
    print("PUBLISHED CORRECTION-SCALE REPRODUCTION: PASS")
    print("SCIENCE INFORMATION UNDER PHYSICAL COLORED NOISE: PASS")
    print("ACTUAL REFERENCE-METROLOGY UNCERTAINTY / CONTRAST CAMPAIGN: STILL OPEN")


def main() -> None:
    structural_assertions()
    print_audit()


if __name__ == "__main__":
    main()
