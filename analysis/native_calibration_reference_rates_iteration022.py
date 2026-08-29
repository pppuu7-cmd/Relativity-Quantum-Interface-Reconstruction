"""RQIR Iteration 022 — native Fisher rates for calibration/reference channels.

Purpose
-------
Replace the remaining standardized calibration/reference sensitivities by explicit
measurement-model Fisher rates.  This is a resource-model layer, not a hardware
forecast.  Hardware transduction coefficients and PSDs remain explicit inputs.

Conventions
-----------
* D1 binary phase readout at quadrature: per accepted event phase Fisher = C^2.
* Gaussian covariance channel: I_ab = 1/2 Tr[Sigma^-1 Sigma_,a Sigma^-1 Sigma_,b]
  per statistically independent sample.  For a unit log-variance parameter this
  is 1/2 per scalar Gaussian sample; with ~2 B T independent real modes the
  Fisher rate is approximately B.
* Timing reference measures delta-t with Gaussian event uncertainty sigma_t.
  For delta-tau = omega_gap delta-t, per-event Fisher on delta-tau is
  1/(omega_gap sigma_t)^2.
* Additive-offset reference with row-normalized Gaussian uncertainty sigma_b has
  per-event Fisher 1/sigma_b^2.
* Fractional-gain reference with known-reference per-event SNR has Fisher
  SNR^2 on delta-g to leading order.

The formulas below intentionally keep transduction gains explicit.  Setting a
transduction to unity is only a transparent unit-coupling benchmark.
"""
from __future__ import annotations

import math


def d1_mean_rate(contrast: float, transduction_rad_per_unit: float,
                 cycle_s: float, acceptance: float = 1.0) -> float:
    """Row-normalized mean-calibration Fisher rate [1/(unit^2 s)]."""
    return acceptance * (contrast * transduction_rad_per_unit) ** 2 / cycle_s


def gaussian_logvariance_rate(bandwidth_hz: float, duty: float = 1.0,
                              sensitivity: float = 1.0) -> float:
    """Approximate Fisher rate for a log-variance/log-PSD-like row.

    For one scalar Gaussian DOF I(log V)=1/2 and ~2 B T real independent modes,
    so I/T ~= B.  sensitivity is d(log V)/d(row_coordinate).
    """
    return duty * bandwidth_hz * sensitivity ** 2


def timing_tau_rate(sigma_t_event_s: float, cycle_s: float, f_gap_hz: float,
                    acceptance: float = 1.0) -> float:
    omega = 2.0 * math.pi * f_gap_hz
    return acceptance / (cycle_s * (omega * sigma_t_event_s) ** 2)


def additive_offset_rate(sigma_b_event: float, cycle_s: float,
                         acceptance: float = 1.0) -> float:
    return acceptance / (cycle_s * sigma_b_event ** 2)


def fractional_gain_rate(reference_snr_event: float, cycle_s: float,
                         acceptance: float = 1.0) -> float:
    return acceptance * reference_snr_event ** 2 / cycle_s


def time_to_precision(target_sigma: float, fisher_rate: float) -> float:
    """Wall time to reach Gaussian prior sigma when information grows linearly."""
    return 1.0 / (target_sigma ** 2 * fisher_rate)


def timing_time_ratio(sigma_t_event_s: float, sigma_t_target_s: float,
                      cycle_s: float, acceptance: float = 1.0) -> float:
    """Equivalent direct timing formula; f_gap cancels when units are consistent."""
    return cycle_s / acceptance * (sigma_t_event_s / sigma_t_target_s) ** 2


def sequential_rows_time(gamma_per_row: float, n_rows: int,
                         row_rate: float) -> float:
    return n_rows * gamma_per_row / row_rate


def main() -> None:
    # Current corrected Iteration-015 uniform row weights at the 90% benchmark.
    gm_d1, gc_d1 = 1.7219876e6, 9.3814709e5
    gm_d2, gc_d2 = 2.4144544e6, 9.2943956e5

    # Current coherence floor at f_gap=100 Hz from tau_max=4.99085067.
    tau_max = 4.99085067
    f_gap = 100.0
    t_coh = tau_max / (2.0 * math.pi * f_gap)
    dead = 1.0e-3
    cycle = t_coh + dead
    acceptance = 0.5

    # Transparent D1 unit-coupling benchmark: one row unit -> 1 rad phase,
    # contrast 0.66.  This is not a hardware claim.
    r_mean = d1_mean_rate(0.66, 1.0, cycle, acceptance)
    t_d1_mean = sequential_rows_time(gm_d1, 14, r_mean)
    t_d2_mean_if_same_readout = sequential_rows_time(gm_d2, 14, r_mean)

    # Unit log-variance sensitivity, 1 kHz independent-mode bandwidth.
    r_cov = gaussian_logvariance_rate(1000.0, duty=1.0, sensitivity=1.0)
    t_d1_cov = sequential_rows_time(gc_d1, 8, r_cov)
    t_d2_cov = sequential_rows_time(gc_d2, 8, r_cov)

    print('coherence floor [ms]=', 1e3 * t_coh)
    print('D1 unit-coupling mean-cal sequential [h]=', t_d1_mean / 3600.0)
    print('D2-weight unit-coupling mean-cal sequential [h]=', t_d2_mean_if_same_readout / 3600.0)
    print('D1 1-kHz logvariance sequential [h]=', t_d1_cov / 3600.0)
    print('D2 1-kHz logvariance sequential [h]=', t_d2_cov / 3600.0)

    # Timing-control targets from Iteration 016/018.
    for name, target_us in [('D1', 9.47), ('D2', 8.01)]:
        target = target_us * 1e-6
        for event_us in (1.0, 10.0, 50.0):
            event = event_us * 1e-6
            rtau = timing_tau_rate(event, cycle, f_gap, acceptance)
            target_tau = 2.0 * math.pi * f_gap * target
            t1 = time_to_precision(target_tau, rtau)
            t2 = timing_time_ratio(event, target, cycle, acceptance)
            assert abs(t1 - t2) <= 1e-12 * max(1.0, t2)
            print(name, 'event jitter us=', event_us, 'timing-ref wall s=', t1)

    # Regression guards for the documented transparent benchmarks.
    assert 7.9e-3 < t_coh < 8.0e-3
    assert 270.0 < t_d1_mean / 3600.0 < 280.0
    assert 380.0 < t_d2_mean_if_same_readout / 3600.0 < 390.0
    assert 2.0 < t_d1_cov / 3600.0 < 2.2
    assert 2.0 < t_d2_cov / 3600.0 < 2.2


if __name__ == '__main__':
    main()
