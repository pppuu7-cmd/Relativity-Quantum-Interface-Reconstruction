"""RQIR Paper III — reference-calibration floor and resource-scaling audit.

This audit builds on the physical atom-interferometer full-covariance model in
atom_interferometer_science_estimability_full_covariance_audit.py.

For a modulated reference channel

    mu ~ (1 + gamma) [theta + alpha q],

an unconstrained alpha produces an exact science/gain/reference degeneracy.
If alpha instead has a Gaussian calibration prior sigma_alpha, high-statistics
data determine theta/alpha while the absolute scale inherits a calibration
floor.  The expected asymptotic relation is

    sigma_theta^2(N) = A/N + (theta/alpha)^2 sigma_alpha^2 + o(1/N),

for a stationary sequence/noise pattern.  The second term cannot be beaten by
more shots; it is a resource-closure boundary, not ordinary statistical noise.
"""
from __future__ import annotations

import math
import numpy as np

from atom_interferometer_science_estimability_full_covariance_audit import (
    common_clock_fisher,
    fisher_metrics,
    prior_assisted_unknown_reference,
)


THETA = 0.2
ALPHA = 0.4
NSHOTS = np.array([48, 96, 192, 384], dtype=int)


def known_reference_scaling(rho: float = 0.7) -> dict[str, float]:
    sigmas = []
    for n in NSHOTS:
        F = common_clock_fisher(
            nshot=int(n),
            rho=rho,
            theta=THETA,
            reference_amplitude=ALPHA,
            reference_mode="known_modulated",
            include_recoil=False,
        )
        m = fisher_metrics(F)
        assert m["theta_estimable"]
        sigmas.append(float(m["theta_sigma"]))

    sigmas = np.asarray(sigmas)
    invariant = sigmas * np.sqrt(NSHOTS)
    spread = float(np.max(invariant) / np.min(invariant) - 1.0)
    return {
        "sqrtN_invariant_mean": float(np.mean(invariant)),
        "sqrtN_invariant_fractional_spread": spread,
        "sigma_N48": float(sigmas[0]),
        "sigma_N384": float(sigmas[-1]),
    }


def unknown_reference_without_prior(rho: float = 0.7) -> None:
    for n in NSHOTS:
        F = common_clock_fisher(
            nshot=int(n),
            rho=rho,
            theta=THETA,
            reference_amplitude=ALPHA,
            reference_mode="unknown_modulated",
            include_recoil=True,
        )
        m = fisher_metrics(F)
        assert not m["theta_estimable"]
        assert math.isinf(float(m["theta_sigma"]))


def fit_prior_floor(sigma_alpha: float, rho: float = 0.7) -> dict[str, float]:
    if sigma_alpha <= 0.0:
        raise ValueError("sigma_alpha must be positive")

    variances = []
    for n in NSHOTS:
        F = prior_assisted_unknown_reference(
            sigma_alpha,
            nshot=int(n),
            rho=rho,
        )
        m = fisher_metrics(F)
        assert m["theta_estimable"]
        variances.append(float(m["theta_sigma"]) ** 2)

    x = 1.0 / NSHOTS.astype(float)
    slope, intercept = np.polyfit(x, np.asarray(variances), 1)
    fitted_floor = math.sqrt(max(float(intercept), 0.0))
    predicted_floor = abs(THETA / ALPHA) * sigma_alpha
    rel_error = abs(fitted_floor - predicted_floor) / predicted_floor

    return {
        "sigma_alpha": sigma_alpha,
        "statistical_coefficient_A": float(slope),
        "variance_intercept": float(intercept),
        "fitted_sigma_theta_floor": fitted_floor,
        "predicted_sigma_theta_floor": predicted_floor,
        "relative_floor_error": rel_error,
    }


def structural_assertions() -> None:
    known = known_reference_scaling()
    # Stationary repeated pattern gives the expected N^{-1/2} law.
    assert known["sqrtN_invariant_fractional_spread"] < 0.01

    # No amount of N removes the exact unknown-reference degeneracy.
    unknown_reference_without_prior()

    # Prior-assisted closure exposes the calibration floor.  The finite-N fit
    # should recover |theta/alpha| sigma_alpha to within 10 percent even for
    # the smallest prior tested here.
    slopes = []
    for sigma_alpha in [0.2, 0.05, 0.01]:
        result = fit_prior_floor(sigma_alpha)
        assert result["relative_floor_error"] < 0.10
        assert result["statistical_coefficient_A"] > 0.0
        slopes.append(result["statistical_coefficient_A"])

    # The same statistical coefficient appears for different calibration
    # priors; only the N-independent intercept changes.
    assert max(slopes) / min(slopes) - 1.0 < 1e-8


def print_audit() -> None:
    known = known_reference_scaling()
    print("RQIR atom-interferometer reference-calibration floor audit")
    print(
        "known calibrated reference: sigma_theta*sqrt(N) = "
        f"{known['sqrtN_invariant_mean']:.9g} "
        f"(fractional spread {known['sqrtN_invariant_fractional_spread']:.3g})"
    )
    print("unknown reference, no prior: SCIENCE NON_IDENTIFIABLE FOR ALL N")
    print("sigma_alpha | fitted floor | predicted floor | relative error | A")
    for sigma_alpha in [0.2, 0.05, 0.01]:
        r = fit_prior_floor(sigma_alpha)
        print(
            f"{sigma_alpha:10.4g} | "
            f"{r['fitted_sigma_theta_floor']:.9g} | "
            f"{r['predicted_sigma_theta_floor']:.9g} | "
            f"{r['relative_floor_error']:.6g} | "
            f"{r['statistical_coefficient_A']:.9g}"
        )
    print("resource law: sigma_theta^2 = A/N + calibration_floor^2: PASS")
    print("statistical -> calibration-limited transition: EXPLICIT")
    print("RQIR reference-calibration resource gate: PASS WITH FAILURE DOMAIN")


def main() -> None:
    structural_assertions()
    print_audit()


if __name__ == "__main__":
    main()
