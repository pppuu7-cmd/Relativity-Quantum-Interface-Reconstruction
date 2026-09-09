"""RQIR Paper III — same-apparatus atom-gravimeter closure audit.

This is the first RQIR Paper-III audit tied to one published physical apparatus
rather than dimensionless surrogate units.

Apparatus anchor
----------------
J. Le Gouet et al., "Limits to the sensitivity of a low noise compact atomic
gravimeter", Appl. Phys. B 92, 133-144 (2008), arXiv:0801.1270:
- 87Rb Raman gravimeter near lambda = 780 nm;
- total interferometer time 2T = 100 ms (T = 50 ms);
- repetition rate 4 Hz (Tc = 0.25 s);
- Raman pulse duration about 10 us in the low-noise gravimeter;
- best measured phase noise 11 mrad/shot;
- best short-term acceleration sensitivity 1.4e-8 g at 1 s;
- vibration correction uses a low-noise seismometer on the retroreflection
  mirror, and the authors deliberately drive the isolation platform at chosen
  frequencies while recording atomic and seismometer signals to measure the
  transfer relation.

P. Cheinet et al., IEEE TIM 57, 1141-1148 (2008), arXiv:physics/0510197:
- experimentally validates the three-pulse sensitivity function;
- low-frequency G(w) = -4 i sin^2(w T/2) / w;
- acceleration noise enters through the corresponding interferometer transfer
  function, with sequential sampling at fc = 1/Tc.

RQIR question
-------------
Does non-zero Fisher information on a modulated acceleration-like science
amplitude survive simultaneous profiling of:
- a common multiplicative acceleration scale/readout gain;
- phase offset;
- linear and quadratic drift;
- correlated shot noise;
- finite calibration uncertainty of a same-apparatus acceleration reference?

Important scope boundary
------------------------
The 11 mrad/shot covariance amplitude is measured on the apparatus. The
off-diagonal AR(1) family below is a conservative stress family, NOT claimed to
be the measured full covariance/PSD of the 2008 data. Thus this closes a
same-apparatus scale/transfer/dead-time/noise-amplitude gate, but not yet the
final measured-PSD campaign closure.
"""
from __future__ import annotations

import math
import numpy as np

G0 = 9.80665
LAMBDA = 780e-9
K_EFF = 4.0 * math.pi / LAMBDA
T = 0.050
T_TOTAL = 2.0 * T
TC = 0.250
FC = 1.0 / TC
RAMAN_PULSE = 10e-6
SIGMA_PHASE_SHOT = 11e-3
DUTY = T_TOTAL / TC

# Design choice for the calibrator, not a published amplitude.
# 1 micro-g gives about 0.4 rad, compatible with the paper's statement that
# typical corrected phase excursions are of order 1 rad / 100 ms.
REFERENCE_UG = 1.0
REFERENCE_F_HZ = 1.0
SCIENCE_F_HZ = 0.5

K_ACC = K_EFF * T**2
K_G = K_ACC * G0


def normalized_accel_transfer(f_hz: float) -> float:
    """Low-frequency three-pulse acceleration response normalized to DC.

    From x -> phase = k_eff [x(0)-2x(T)+x(2T)] and a=-w^2 x,
    |H_a(w)|/(k_eff T^2) = [sin(wT/2)/(wT/2)]^2.
    np.sinc(x)=sin(pi x)/(pi x), so the result is sinc(f*T)^2.
    """
    return float(np.sinc(f_hz * T) ** 2)


def published_scale_checks() -> dict[str, float]:
    """Reproduce the paper-level scale and sensitivity numbers."""
    sigma_g_shot = SIGMA_PHASE_SHOT / K_G
    sigma_g_1s = sigma_g_shot / math.sqrt(FC)
    one_mrad_g_1s = 1e-3 / K_G / math.sqrt(FC)
    ref_phase = (
        K_G
        * (REFERENCE_UG * 1e-6)
        * normalized_accel_transfer(REFERENCE_F_HZ)
    )
    return {
        "K_eff_per_m": K_EFF,
        "K_acc_rad_per_mps2": K_ACC,
        "K_g_rad_per_g": K_G,
        "duty_fraction": DUTY,
        "sigma_g_shot": sigma_g_shot,
        "sigma_g_1s": sigma_g_1s,
        "one_mrad_g_1s": one_mrad_g_1s,
        "reference_phase_rad": ref_phase,
    }


def apply_ar1_precision(J: np.ndarray, rho: float) -> np.ndarray:
    """Apply inverse AR(1) covariance to J without constructing NxN matrices.

    Marginal shot RMS is fixed to the measured 11 mrad for every rho.
    """
    n = J.shape[0]
    if n < 3:
        raise ValueError("need at least 3 shots")
    if not (-1.0 < rho < 1.0):
        raise ValueError("|rho| must be < 1")
    fac = 1.0 / (SIGMA_PHASE_SHOT**2 * (1.0 - rho**2))
    out = np.empty_like(J)
    out[0] = (J[0] - rho * J[1]) * fac
    out[-1] = (J[-1] - rho * J[-2]) * fac
    out[1:-1] = (
        (1.0 + rho**2) * J[1:-1]
        - rho * (J[:-2] + J[2:])
    ) * fac
    return out


def templates(nshot: int, science_modulated: bool = True) -> dict[str, np.ndarray]:
    t = np.arange(nshot, dtype=float) * TC
    x = np.linspace(-1.0, 1.0, nshot)

    if science_modulated:
        s = np.sin(2.0 * math.pi * SCIENCE_F_HZ * t)
        s *= normalized_accel_transfer(SCIENCE_F_HZ)
    else:
        s = np.ones(nshot)

    q = np.sin(2.0 * math.pi * REFERENCE_F_HZ * t + 0.37)
    q *= normalized_accel_transfer(REFERENCE_F_HZ)

    return {"t": t, "x": x, "science": s, "reference": q}


def design_matrix(
    nshot: int,
    *,
    theta_ng: float = 1.0,
    science_modulated: bool = True,
    use_reference: bool = True,
    reference_unknown: bool = False,
) -> tuple[np.ndarray, tuple[str, ...]]:
    """Linearized phase derivatives.

    theta_ng is the science acceleration amplitude in nano-g.
    gamma is a common multiplicative acceleration-scale/readout nuisance.
    alpha_ug, when included, is the reference amplitude in micro-g.
    """
    z = templates(nshot, science_modulated)
    s, q, x = z["science"], z["reference"], z["x"]
    if not use_reference:
        q = np.zeros_like(q)

    theta_g = theta_ng * 1e-9
    alpha_g = REFERENCE_UG * 1e-6 if use_reference else 0.0

    # d phase / d(theta in nano-g)
    dtheta = K_G * 1e-9 * s

    # derivative with respect to common fractional scale gamma at gamma=0
    dgamma = K_G * (theta_g * s + alpha_g * q)

    cols = [
        dtheta,
        dgamma,
        np.ones(nshot),
        x,
        x**2,
    ]
    names = ["theta_ng", "gamma", "phase_offset", "linear_drift", "quadratic_drift"]

    if reference_unknown:
        # d phase / d(alpha in micro-g)
        dalpha = K_G * 1e-6 * q
        cols.append(dalpha)
        names.append("alpha_ug")

    return np.column_stack(cols), tuple(names)


def fisher(
    nshot: int,
    *,
    rho: float = 0.0,
    theta_ng: float = 1.0,
    science_modulated: bool = True,
    use_reference: bool = True,
    reference_unknown: bool = False,
    reference_prior_fraction: float | None = None,
) -> tuple[np.ndarray, tuple[str, ...]]:
    J, names = design_matrix(
        nshot,
        theta_ng=theta_ng,
        science_modulated=science_modulated,
        use_reference=use_reference,
        reference_unknown=reference_unknown,
    )
    F = J.T @ apply_ar1_precision(J, rho)

    if reference_prior_fraction is not None:
        if not reference_unknown:
            raise ValueError("reference prior only applies when alpha_ug is a parameter")
        if reference_prior_fraction <= 0:
            raise ValueError("reference_prior_fraction must be positive")
        sigma_alpha_ug = REFERENCE_UG * reference_prior_fraction
        F[-1, -1] += 1.0 / sigma_alpha_ug**2

    return 0.5 * (F + F.T), names


def estimability(F: np.ndarray, theta_index: int = 0) -> dict[str, float | int | bool]:
    """Rank/null-space test plus theta sigma when estimable.

    Normalize parameters by Fisher diagonal before eigendecomposition so the
    rank decision is not dominated by unit choices.
    """
    d = np.sqrt(np.clip(np.diag(F), 1e-300, None))
    S = np.diag(1.0 / d)
    Fn = S @ F @ S
    Fn = 0.5 * (Fn + Fn.T)

    w, v = np.linalg.eigh(Fn)
    tol = 1e-9
    pos = w > tol
    null = v[:, ~pos]

    # A normalized-parameter null vector has theta component v[theta_index].
    theta_null_overlap = (
        float(np.linalg.norm(null[theta_index, :])) if null.shape[1] else 0.0
    )
    theta_estimable = theta_null_overlap < 1e-7

    if theta_estimable:
        # Pseudoinverse is safe after the normalized rank check; transform back.
        Fni = np.linalg.pinv(Fn, rcond=tol)
        cov = S @ Fni @ S
        sigma = math.sqrt(max(float(cov[theta_index, theta_index]), 0.0))
        info = 1.0 / sigma**2 if sigma > 0 else math.inf
    else:
        sigma = math.inf
        info = 0.0

    return {
        "rank": int(np.sum(pos)),
        "dimension": int(F.shape[0]),
        "theta_estimable": bool(theta_estimable),
        "theta_null_overlap": theta_null_overlap,
        "sigma_theta_ng": sigma,
        "effective_information_per_ng2": info,
        "min_normalized_eigenvalue": float(np.min(w)),
    }


def case_metrics(seconds: float, **kwargs) -> dict[str, float | int | bool]:
    nshot = int(round(seconds / TC))
    F, _ = fisher(nshot, **kwargs)
    return estimability(F)


def structural_assertions() -> None:
    p = published_scale_checks()

    # Reproduce published sensitivity scale within rounding.
    assert abs(p["sigma_g_1s"] / 1.4e-8 - 1.0) < 0.02
    assert abs(p["one_mrad_g_1s"] / 1.2e-9 - 1.0) < 0.08
    assert abs(p["duty_fraction"] - 0.4) < 1e-12

    # The chosen 1 micro-g reference is deliberately in a moderate phase range.
    assert 0.25 < p["reference_phase_rad"] < 0.6

    # Static science is killed by a free phase offset.
    m = case_metrics(
        60,
        science_modulated=False,
        use_reference=True,
        reference_unknown=False,
    )
    assert not m["theta_estimable"]

    # Modulation alone does not fix absolute scale if gamma is free and there is
    # no calibrated reference.
    m = case_metrics(
        60,
        science_modulated=True,
        use_reference=False,
        reference_unknown=False,
    )
    assert not m["theta_estimable"]

    # A same-apparatus known acceleration reference restores nonzero science info
    # after simultaneous offset, drift, scale, and covariance profiling.
    for rho in [0.0, 0.3, 0.6, 0.9]:
        m = case_metrics(
            60,
            rho=rho,
            science_modulated=True,
            use_reference=True,
            reference_unknown=False,
        )
        assert m["theta_estimable"]
        assert m["effective_information_per_ng2"] > 0.0
        assert math.isfinite(float(m["sigma_theta_ng"]))

    # If reference amplitude is promoted to an unconstrained parameter, the
    # absolute-scale degeneracy reappears.
    m = case_metrics(
        60,
        science_modulated=True,
        use_reference=True,
        reference_unknown=True,
        reference_prior_fraction=None,
    )
    assert not m["theta_estimable"]

    # Finite external calibration closes the local Fisher problem.
    for frac in [1e-2, 1e-3, 1e-4]:
        m = case_metrics(
            60,
            science_modulated=True,
            use_reference=True,
            reference_unknown=True,
            reference_prior_fraction=frac,
        )
        assert m["theta_estimable"]
        assert m["effective_information_per_ng2"] > 0.0


def resource_table() -> list[dict[str, float]]:
    rows = []
    for rho in [0.0, 0.3, 0.6, 0.9]:
        for seconds in [60.0, 600.0, 3600.0]:
            m = case_metrics(
                seconds,
                rho=rho,
                science_modulated=True,
                use_reference=True,
                reference_unknown=True,
                reference_prior_fraction=1e-3,
            )
            rows.append(
                {
                    "rho": rho,
                    "seconds": seconds,
                    "shots": seconds / TC,
                    "sigma_theta_ng": float(m["sigma_theta_ng"]),
                    "information": float(m["effective_information_per_ng2"]),
                }
            )
    return rows


def print_audit() -> None:
    p = published_scale_checks()
    print("RQIR same-apparatus atom-gravimeter audit")
    print(f"k_eff = {p['K_eff_per_m']:.9g} 1/m")
    print(f"k_eff*T^2 = {p['K_acc_rad_per_mps2']:.9g} rad/(m/s^2)")
    print(f"duty = {p['duty_fraction']:.3f}; fc = {FC:.3f} Hz")
    print(f"measured 11 mrad/shot -> {p['sigma_g_1s']:.6g} g @ 1 s")
    print(f"1 mrad/shot -> {p['one_mrad_g_1s']:.6g} g @ 1 s")
    print(f"chosen 1 micro-g reference phase = {p['reference_phase_rad']:.6g} rad")
    print(
        "transfer factors: science="
        f"{normalized_accel_transfer(SCIENCE_F_HZ):.9g}, "
        f"reference={normalized_accel_transfer(REFERENCE_F_HZ):.9g}"
    )

    cases = [
        ("static science + known ref", dict(science_modulated=False, use_reference=True)),
        ("modulated science, no ref", dict(science_modulated=True, use_reference=False)),
        ("modulated science + known ref", dict(science_modulated=True, use_reference=True)),
        (
            "modulated science + unknown ref",
            dict(science_modulated=True, use_reference=True, reference_unknown=True),
        ),
        (
            "modulated science + 0.1% ref prior",
            dict(
                science_modulated=True,
                use_reference=True,
                reference_unknown=True,
                reference_prior_fraction=1e-3,
            ),
        ),
    ]
    print("\n60 s gate cases (rho=0.3):")
    for name, kw in cases:
        m = case_metrics(60, rho=0.3, **kw)
        sigma = m["sigma_theta_ng"]
        sigma_txt = "inf" if not math.isfinite(float(sigma)) else f"{sigma:.6g}"
        print(
            f"{name:40s} estimable={m['theta_estimable']} "
            f"rank={m['rank']}/{m['dimension']} sigma={sigma_txt} ng"
        )

    print("\nResource forecast with measured 11 mrad shot RMS and 0.1% ref prior:")
    print("rho  seconds  shots   sigma_theta[ng]   I_eff[1/ng^2]")
    for r in resource_table():
        print(
            f"{r['rho']:3.1f} {r['seconds']:8.0f} {r['shots']:6.0f} "
            f"{r['sigma_theta_ng']:16.8g} {r['information']:16.8g}"
        )

    print("\nDecision:")
    print("SAME-APPARATUS ACCELERATION INFORMATION AFTER NUISANCE PROFILING: PASS")
    print("UNMODULATED SCIENCE WITH FREE OFFSET: FAIL")
    print("UNCALIBRATED ABSOLUTE SCALE/REFERENCE: FAIL")
    print("MEASURED FULL PSD/CROSS-PSD CAMPAIGN CLOSURE: STILL OPEN")


def main() -> None:
    structural_assertions()
    print_audit()


if __name__ == "__main__":
    main()
