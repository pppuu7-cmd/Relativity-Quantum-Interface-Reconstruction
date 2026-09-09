"""RQIR Paper III — traceable Raman-chirp reference metrology audit.

Purpose
-------
Replace the earlier mechanical-shaker absolute-reference *proxy* with a
metrologically traceable acceleration-equivalent reference generated inside the
Raman phase channel itself.

For a three-pulse Raman atom gravimeter with Raman frequency-difference chirp
alpha_nu in Hz/s,

    DeltaPhi = (k_eff * g - 2*pi*alpha_nu) * T^2.

Therefore a programmed differential chirp Delta(alpha_nu) is exactly equivalent
(at this leading inertial-response level) to

    a_ref = 2*pi*Delta(alpha_nu) / k_eff.

This reference shares the same T^2 interferometer scale as the acceleration
science phase and does not require a calibrated mechanical shaker amplitude.
It can be coded shot-by-shot around the nominal gravity-compensation chirp.

Source authorities
------------------
1. Standard Raman atom-gravimeter phase/chirp relation:
   DeltaPhi = (k_eff*g - 2*pi*alpha_nu) T^2.
2. Zhang et al., AIP Advances 15 (2025), DOI 10.1063/5.0252751,
   "A method for the precise and absolute measurement of microwave chirp rates
   in cold-atom gravimeters": absolute chirp-rate measurement precision better
   than 1 mHz/s using time/frequency instruments synchronized to an atomic clock.
3. Hu et al., Rev. Sci. Instrum. 86, 096108 (2015), DOI 10.1063/1.4930562:
   direct DDS chirp-rate relative instability 5.7e-11 at 1 s.
4. BIPM CIPM Recommendation 2 (2015): 87Rb D2 780-nm d/f crossover
   f = 384 227 981.9 MHz with relative standard uncertainty 5e-10.

Conservative differential-metrology rule
----------------------------------------
The 2025 <1 mHz/s figure refers to absolute measurement of a full gravimeter
chirp near 25.1 MHz/s.  RQIR needs the *difference* between two chirp settings,
only ~25 Hz/s for a 1 micro-g reference.  We therefore do NOT divide 1 mHz/s by
25 MHz/s.  Instead we assign 2 mHz/s uncertainty directly to the DIFFERENTIAL
chirp, conservatively allowing two independently measured settings at about the
1 mHz/s level plus margin.  This is the quantity relevant to the reference.

Scope boundary
--------------
This audit closes a traceable reference-metrology ARCHITECTURE for a Paper-III
resource/design forecast.  It does not claim that the historical SYRTE 2008
apparatus itself used the 2025 calibration method or that raw same-apparatus
chirp records exist in this repository.  A final campaign/provenance certificate
must preserve that distinction.
"""
from __future__ import annotations

import math

C_LIGHT = 299_792_458.0
G0 = 9.80665
RB_D2_FREQ_HZ = 384_227_981.9e6
RB_D2_REL_U = 5.0e-10
LAMBDA_RB_D2 = C_LIGHT / RB_D2_FREQ_HZ
K_EFF = 4.0 * math.pi / LAMBDA_RB_D2

REFERENCE_G = 1.0e-6  # 1 micro-g acceleration-equivalent reference
DIFFERENTIAL_CHIRP_U_HZ_PER_S = 2.0e-3  # conservative differential 2 mHz/s
DDS_REL_INSTABILITY_1S = 5.7e-11

# Earlier mechanical-reference campaign proxy retained only for comparison.
OLD_MECHANICAL_PROXY_FRACTION = 0.010646
OLD_ONE_HOUR_SIGMA_NG_AT_3420S = 0.766
OLD_SCIENCE_SECONDS = 3420.0
FULL_HOUR_SECONDS = 3600.0


def nominal_gravity_chirp_hz_per_s() -> float:
    """Raman frequency-difference chirp that compensates g."""
    return K_EFF * G0 / (2.0 * math.pi)


def reference_chirp_offset_hz_per_s(reference_g: float = REFERENCE_G) -> float:
    """Differential chirp required for an acceleration reference in units of g."""
    return K_EFF * (reference_g * G0) / (2.0 * math.pi)


def reference_fractional_uncertainty(
    differential_u_hz_per_s: float = DIFFERENTIAL_CHIRP_U_HZ_PER_S,
    reference_g: float = REFERENCE_G,
) -> dict[str, float]:
    """Combine differential chirp and optical-wave-vector uncertainty."""
    delta = reference_chirp_offset_hz_per_s(reference_g)
    chirp_fraction = differential_u_hz_per_s / abs(delta)
    total = math.hypot(chirp_fraction, RB_D2_REL_U)
    return {
        "delta_chirp_hz_per_s": delta,
        "differential_chirp_u_hz_per_s": differential_u_hz_per_s,
        "chirp_fraction": chirp_fraction,
        "k_eff_fraction": RB_D2_REL_U,
        "total_fraction": total,
    }


def full_hour_statistical_sigma_ng() -> float:
    """Recover a full-hour science forecast when calibration blocks are removed."""
    return OLD_ONE_HOUR_SIGMA_NG_AT_3420S * math.sqrt(
        OLD_SCIENCE_SECONDS / FULL_HOUR_SECONDS
    )


def calibration_floor_ng(theta_ng: float) -> float:
    return abs(theta_ng) * reference_fractional_uncertainty()["total_fraction"]


def total_sigma_ng(theta_ng: float) -> float:
    stat = full_hour_statistical_sigma_ng()
    floor = calibration_floor_ng(theta_ng)
    return math.hypot(stat, floor)


def crossover_theta_ng() -> float:
    """Science amplitude where statistical and reference-calibration terms match."""
    stat = full_hour_statistical_sigma_ng()
    frac = reference_fractional_uncertainty()["total_fraction"]
    return stat / frac


def structural_assertions() -> None:
    # Nominal gravity chirp should be the familiar ~25.1 MHz/s scale.
    assert 25.0e6 < nominal_gravity_chirp_hz_per_s() < 25.3e6

    # A 1 micro-g differential reference is about 25 Hz/s, not 25 MHz/s.
    delta = reference_chirp_offset_hz_per_s()
    assert 25.0 < delta < 25.3

    u = reference_fractional_uncertainty()

    # Conservative 2 mHz/s DIFFERENTIAL uncertainty gives ~8e-5 fractional
    # reference uncertainty. Optical k_eff uncertainty is negligible here.
    assert 7.0e-5 < u["total_fraction"] < 9.0e-5
    assert u["chirp_fraction"] / u["k_eff_fraction"] > 1.0e5

    # This should improve the previous mechanical 1.0646% proxy by >100x.
    improvement = OLD_MECHANICAL_PROXY_FRACTION / u["total_fraction"]
    assert improvement > 100.0

    # Eliminating dedicated 180-s calibration blocks recovers the full hour.
    stat = full_hour_statistical_sigma_ng()
    assert 0.73 < stat < 0.77

    # At theta=100 ng the calibration floor should be negligible vs statistics.
    assert calibration_floor_ng(100.0) < 0.01
    assert abs(total_sigma_ng(100.0) / stat - 1.0) < 1.0e-3

    # Calibration becomes comparable only near O(10 micro-g) for this 1h design.
    cross = crossover_theta_ng()
    assert 8.0e3 < cross < 12.0e3


def report() -> dict[str, float]:
    u = reference_fractional_uncertainty()
    stat = full_hour_statistical_sigma_ng()
    return {
        "rb_d2_wavelength_m": LAMBDA_RB_D2,
        "k_eff_per_m": K_EFF,
        "nominal_gravity_chirp_hz_per_s": nominal_gravity_chirp_hz_per_s(),
        "reference_chirp_offset_hz_per_s": u["delta_chirp_hz_per_s"],
        "reference_fractional_uncertainty": u["total_fraction"],
        "reference_percent_uncertainty": 100.0 * u["total_fraction"],
        "improvement_over_mechanical_proxy": (
            OLD_MECHANICAL_PROXY_FRACTION / u["total_fraction"]
        ),
        "full_hour_science_duty": 1.0,
        "full_hour_statistical_sigma_ng": stat,
        "calibration_floor_at_100ng": calibration_floor_ng(100.0),
        "calibration_floor_at_1000ng": calibration_floor_ng(1000.0),
        "crossover_theta_ng": crossover_theta_ng(),
    }


def print_audit() -> None:
    r = report()
    print("RQIR chirp-reference metrology audit")
    print(f"Rb D2 lambda = {r['rb_d2_wavelength_m']:.12g} m")
    print(f"k_eff = {r['k_eff_per_m']:.12g} 1/m")
    print(
        "nominal gravity-compensation chirp = "
        f"{r['nominal_gravity_chirp_hz_per_s']:.9g} Hz/s"
    )
    print(
        "1 micro-g differential chirp = "
        f"{r['reference_chirp_offset_hz_per_s']:.9g} Hz/s"
    )
    print(
        "conservative differential reference uncertainty = "
        f"{r['reference_fractional_uncertainty']:.9g} "
        f"({r['reference_percent_uncertainty']:.6g}%)"
    )
    print(
        "improvement over old mechanical proxy = "
        f"{r['improvement_over_mechanical_proxy']:.6g}x"
    )
    print(
        "full-hour science duty = "
        f"{100*r['full_hour_science_duty']:.3f}%"
    )
    print(
        "full-hour statistical sigma = "
        f"{r['full_hour_statistical_sigma_ng']:.6g} ng"
    )
    print(
        "calibration floor at theta=100 ng = "
        f"{r['calibration_floor_at_100ng']:.6g} ng"
    )
    print(
        "calibration floor at theta=1000 ng = "
        f"{r['calibration_floor_at_1000ng']:.6g} ng"
    )
    print(
        "statistical/calibration crossover = "
        f"{r['crossover_theta_ng']:.6g} ng"
    )
    print("TRACEABLE CHIRP-REFERENCE METROLOGY ARCHITECTURE: PASS")
    print("HISTORICAL SAME-APPARATUS RAW CHIRP RECORD: NOT CLAIMED")


def main() -> None:
    structural_assertions()
    print_audit()


if __name__ == "__main__":
    main()
