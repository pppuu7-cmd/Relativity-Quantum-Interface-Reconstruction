#!/usr/bin/env python3
"""RQIR Iteration 068 — physical Fisher-rate closure.

Converts the preparation Fisher C_a and row-normalized mean-calibration gamma
into accepted-copy / wall-clock rate formulae while separating two quantities
that older documents both denoted alpha:

  alpha_h : fractional hidden-source preparation amplitude (a = 0.08 alpha_h)
  eps_drv : pump/drive impulse area entering detector response

No hardware forecast and no new-physics claim.
"""

from math import isclose

# Source-of-truth constants retained from prior iterations.
S_EFF_D2_009 = 5.779507196013e-4
S_EFF_RATIO_013_009 = 0.04228407350
GAMMA_MEAN_009 = 1.830264703e6
F_E_ALPHA_009 = 0.0093918844       # per ideal accepted energy-population copy
F_Q_ALPHA_009 = 0.0849323916       # ideal accepted-copy QFI ceiling


def preparation_fisher_required(raw_detector_fisher: float, retention: float) -> float:
    """Exact beta-alpha_h two-parameter lower bound C = r/(1-r) * S."""
    if not (0.0 < retention < 1.0):
        raise ValueError("retention must lie in (0,1)")
    return retention / (1.0 - retention) * raw_detector_fisher


def accepted_copies(C_required: float, fisher_per_accepted_copy: float) -> float:
    return C_required / fisher_per_accepted_copy


def accepted_mean_layer_cycles(gamma: float, single_cycle_row_fisher: float) -> float:
    """Accepted cycles required by one independently scheduled row-normalized layer."""
    return gamma / single_cycle_row_fisher


def mean_campaign_time(gamma: float, fisher_rates: list[float]) -> float:
    """Conservative wall time for independent layers with rates in Fisher/s."""
    return gamma * sum(1.0 / rate for rate in fisher_rates)


def science_fisher_rate(q_drv: float, s_eff: float, acceptance: float, attempt_time_s: float) -> float:
    """D2 beta Fisher/s for independent cycles after declared spectral-tilt profiling."""
    i_cycle = q_drv * q_drv * s_eff
    return acceptance * i_cycle / attempt_time_s


def calibration_to_science_ratio(
    gamma: float,
    calibration_rates: list[float],
    science_rate: float,
    z_target: float,
) -> float:
    """x = T_cal/T_sci with T_sci=Z^2/R_beta."""
    return gamma * sum(1.0 / r for r in calibration_rates) * science_rate / (z_target * z_target)


def main() -> None:
    z = 5.0
    retention = 0.90
    raw_detector_fisher = z * z  # Delta beta = 1 benchmark.

    c_prep = preparation_fisher_required(raw_detector_fisher, retention)
    n_energy = accepted_copies(c_prep, F_E_ALPHA_009)
    n_qfi = accepted_copies(c_prep, F_Q_ALPHA_009)
    science_penalty_013 = 1.0 / S_EFF_RATIO_013_009

    # Regression against Iteration 042 homogeneous xi_mu=3, seven-layer parallel family.
    xi_mu = 3.0
    n_7layer = 7.0 * accepted_mean_layer_cycles(GAMMA_MEAN_009, xi_mu * xi_mu)

    print(f"Toy013/Toy009 D2 science-time penalty = {science_penalty_013:.10f}")
    print(f"C_prep required at Z=5, r=0.90 = {c_prep:.12f}")
    print(f"Toy009 accepted energy-population copies = {n_energy:.10f}")
    print(f"Toy009 ideal-QFI accepted-copy lower bound = {n_qfi:.10f}")
    print(f"At p=0.5: energy attempts = {n_energy/0.5:.10f}")
    print(f"At p=0.5: QFI-ceiling attempts = {n_qfi/0.5:.10f}")
    print(f"Toy009 seven-layer accepted cycles at xi_mu=3 = {n_7layer:.10f}")

    # Exact/near-exact regression gates.
    assert isclose(science_penalty_013, 23.649566307749417, rel_tol=1e-13)
    assert isclose(c_prep, 225.0, rel_tol=1e-14)
    assert isclose(n_energy, 23956.85364270455, rel_tol=1e-13)
    assert isclose(n_qfi, 2649.1659514271823, rel_tol=1e-13)
    assert isclose(n_7layer, 1423539.2134444444, rel_tol=1e-13)


if __name__ == "__main__":
    main()
