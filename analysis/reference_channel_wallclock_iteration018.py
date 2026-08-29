"""RQIR Iteration 018: reference-channel and wall-clock resource mapping.

This script does not claim a hardware forecast.  It maps the corrected
Iteration-015/016 information requirements into transparent timing/reference
and wall-clock formulas, and derives the two-resource square-root allocation
law for detector shots versus independent preparation metrology.
"""
from __future__ import annotations
import math

# Corrected 90%-retention q=1 calibration allocations from Iteration 015.
BRANCH = {
    "D1": {"sigma_tau": 5.95e-3, "gamma_mean": 1.7219876e6, "gamma_cov": 9.3814709e5},
    "D2": {"sigma_tau": 5.03e-3, "gamma_mean": 2.4144544e6, "gamma_cov": 9.2943956e5},
}
N_MEAN = 14
N_COV = 8
TAU_MAX = 4.99085067
DETECTOR_SNR = 5.0
S_D = DETECTOR_SNR**2
GAIN_STATE_RMS_COEFF = 0.325  # Iteration 017, in sigma_beta per unit fractional gain RMS.


def timing_sigma_seconds(sigma_tau: float, f_gap_hz: float) -> float:
    return sigma_tau / (2.0 * math.pi * f_gap_hz)


def white_jitter_asd_limit(sigma_tau: float, f_gap_hz: float, bandwidth_hz: float) -> float:
    """One-sided white time-jitter ASD whose integrated RMS equals sigma_tau."""
    return timing_sigma_seconds(sigma_tau, f_gap_hz) / math.sqrt(bandwidth_hz)


def independent_edge_jitter_limit(sigma_tau: float, f_gap_hz: float, n_edges: int) -> float:
    """Per-edge RMS if n_edges independent timing errors add in quadrature."""
    return timing_sigma_seconds(sigma_tau, f_gap_hz) / math.sqrt(n_edges)


def calibration_equivalent_shots(gamma_mean: float, gamma_cov: float,
                                 detector_info: float = S_D,
                                 xi_mean: float = 1.0,
                                 xi_cov: float = 1.0) -> float:
    """Standardized independent-shot equivalent.

    xi are per-shot standardized sensitivities, so information/shot = xi^2.
    """
    return detector_info * (N_MEAN * gamma_mean / xi_mean**2
                            + N_COV * gamma_cov / xi_cov**2)


def minimum_coherent_span(f_gap_hz: float) -> float:
    return TAU_MAX / (2.0 * math.pi * f_gap_hz)


def wall_time(n_shots: float, f_gap_hz: float, dead_time_s: float = 0.0,
              success_probability: float = 1.0) -> float:
    cycle = minimum_coherent_span(f_gap_hz) + dead_time_s
    return n_shots * cycle / success_probability


def prep_information_for_retention(r: float, detector_info: float = S_D) -> float:
    return detector_info * r / (1.0 - r)


def prep_shots(r: float, xi_prep: float, detector_info: float = S_D) -> float:
    return prep_information_for_retention(r, detector_info) / xi_prep**2


def optimal_two_resource_fraction(rate_detector: float, rate_prep: float):
    """Wall-clock optimum for F = S*C/(S+C), S=R_D*T_D, C=R_P*T_P.

    Returns detector-time fraction, prep-time fraction, retained fraction C/(S+C),
    and optimized profiled Fisher rate.
    """
    rd = math.sqrt(rate_detector)
    rp = math.sqrt(rate_prep)
    x_d = rp / (rd + rp)
    x_p = rd / (rd + rp)
    retention = rp / (rd + rp)
    rate = (rd * rp / (rd + rp))**2
    return x_d, x_p, retention, rate


def gain_reference_requirement(max_bias_sigma: float) -> tuple[float, float]:
    """Posterior-scale Iteration-017 local gain reference requirement.

    Returns max fractional gain RMS and corresponding reference SNR=1/sigma_g.
    Not a global tolerance for arbitrary source error.
    """
    sigma_g = max_bias_sigma / GAIN_STATE_RMS_COEFF
    return sigma_g, 1.0 / sigma_g


def main():
    f = 100.0
    print("detector SNR/info:", DETECTOR_SNR, S_D)
    print("minimum coherent span at 100 Hz [ms]:", 1e3 * minimum_coherent_span(f))

    for name, p in BRANCH.items():
        st = timing_sigma_seconds(p["sigma_tau"], f)
        print("\n", name)
        print("timing RMS [us]:", st * 1e6)
        for bw in (1.0, 100.0, 1000.0):
            print("white jitter ASD at", bw, "Hz [ns/sqrtHz]:",
                  white_jitter_asd_limit(p["sigma_tau"], f, bw) * 1e9)
        for k in (1, 4, 6, 8):
            print("independent edge RMS K=", k, "[us]:",
                  independent_edge_jitter_limit(p["sigma_tau"], f, k) * 1e6)

        n10 = calibration_equivalent_shots(p["gamma_mean"], p["gamma_cov"],
                                           xi_mean=10.0, xi_cov=10.0)
        print("calibration eq shots at xi_mean=xi_cov=10:", n10)
        print("ideal lower wall time at 100 Hz [h]:", wall_time(n10, f) / 3600.0)
        print("+1 ms dead time, p_success=0.5 [h]:",
              wall_time(n10, f, 1e-3, 0.5) / 3600.0)

    print("\nPreparation amplitude metrology at detector SNR 5")
    for r in (0.8, 0.9, 0.95):
        c = prep_information_for_retention(r)
        print(r, "C_a=", c, "sigma_a=", 1/math.sqrt(c), "N(xi=1)=", prep_shots(r, 1.0))

    print("\nTwo-resource wall-clock optimum")
    for ratio in (1.0, 4.0, 9.0, 81.0, 100.0):
        xd, xp, ret, rate = optimal_two_resource_fraction(1.0, ratio)
        print("Rprep/Rdet=", ratio, "detector fraction=", xd,
              "prep fraction=", xp, "prep retention=", ret,
              "F/T normalized=", rate)

    print("\nLocal gain-reference requirements")
    for b in (0.1, 0.01, 0.001):
        sg, snr = gain_reference_requirement(b)
        print("bias budget", b, "sigma_beta -> sigma_g<=", sg, "reference SNR>=", snr)

    # Regression checks.
    assert abs(timing_sigma_seconds(5.95e-3, 100)*1e6 - 9.46971911397) < 1e-8
    assert abs(timing_sigma_seconds(5.03e-3, 100)*1e6 - 8.00549363752) < 1e-8
    assert abs(minimum_coherent_span(100)*1e3 - 7.943411397) < 1e-6
    assert abs(calibration_equivalent_shots(BRANCH['D1']['gamma_mean'], BRANCH['D1']['gamma_cov'], xi_mean=10, xi_cov=10) - 7.90325078e6) < 1
    assert abs(calibration_equivalent_shots(BRANCH['D2']['gamma_mean'], BRANCH['D2']['gamma_cov'], xi_mean=10, xi_cov=10) - 1.030946952e7) < 1
    _, _, r90, _ = optimal_two_resource_fraction(1.0, 81.0)
    assert abs(r90 - 0.9) < 1e-12


if __name__ == "__main__":
    main()
