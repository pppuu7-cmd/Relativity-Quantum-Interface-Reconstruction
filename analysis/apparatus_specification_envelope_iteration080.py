"""RQIR Iteration 080 — apparatus specification envelope.

Converts the Iteration-077 apparatus-rate certificate into necessary and
sufficient rate-space specifications for a declared wall-clock cap, without
inventing an absolute detector ASD.

All rates are Fisher rates in the already declared physical parameter
coordinate, not raw event rates.
"""
from __future__ import annotations

from dataclasses import dataclass

Z = 5.0
C_PREP = 225.0


@dataclass(frozen=True)
class Architecture:
    name: str
    gamma_mean: float
    coherence_ms_100hz: float
    timing_target_us_100hz: float


TOY009 = Architecture("Toy009", 1.830264703e6, 7.94319, 9.19001)
TOY014 = Architecture("Toy014", 5.6776851e6, 6.81327, 3.97715)


def harmonic_mean_rate(rates):
    rates = list(map(float, rates))
    return len(rates) / sum(1.0 / r for r in rates)


def total_time_seconds(R_beta, cal_rates, R_src, gamma_mean, duty=0.0):
    if not (0.0 <= duty < 1.0):
        raise ValueError("duty must satisfy 0 <= duty < 1")
    payload = Z**2 / R_beta + gamma_mean * sum(1.0 / r for r in cal_rates) + C_PREP / R_src
    return payload / (1.0 - duty)


def specification(cap_days, architecture, fractions=(1/3, 1/3, 1/3), duty=0.0):
    """Return necessary component floors and a sufficient allocated specification."""
    fs, fc, fp = map(float, fractions)
    if min(fs, fc, fp) <= 0 or abs(fs + fc + fp - 1.0) > 1e-12:
        raise ValueError("positive fractions must sum to one")
    if not (0.0 <= duty < 1.0):
        raise ValueError("duty must satisfy 0 <= duty < 1")

    T = float(cap_days) * 86400.0
    m = 1.0 / (1.0 - duty)
    gamma = architecture.gamma_mean

    necessary = {
        "R_beta": m * Z**2 / T,
        "H_cal": m * 7.0 * gamma / T,
        "R_src": m * C_PREP / T,
    }
    sufficient = {
        "R_beta": m * Z**2 / (fs * T),
        "H_cal": m * 7.0 * gamma / (fc * T),
        "R_src": m * C_PREP / (fp * T),
    }
    return necessary, sufficient


def main():
    # Harmonic-mean compression is exactly equivalent to seven independently
    # acquired calibration-layer times.
    test_rates = [2.0, 3.0, 5.0, 7.0, 11.0, 13.0, 17.0]
    H = harmonic_mean_rate(test_rates)
    lhs = TOY009.gamma_mean * sum(1.0 / r for r in test_rates)
    rhs = 7.0 * TOY009.gamma_mean / H
    assert abs(lhs - rhs) / lhs < 1e-15

    # Equal-third examples are transparent requirements, not forecasts.
    for days in [1, 7, 30]:
        n009, s009 = specification(days, TOY009)
        n014, s014 = specification(days, TOY014)
        print(f"\ncap={days} d, duty=0, equal-third allocation")
        print("Toy009 sufficient:", s009)
        print("Toy014 sufficient:", s014)
        print("componentwise necessary Toy009:", n009)
        print("componentwise necessary Toy014:", n014)

    # Exact allocated boundary closes the requested wall-clock cap.
    cap_days = 7.0
    _, spec = specification(cap_days, TOY009)
    cal_rates = [spec["H_cal"]] * 7
    T = total_time_seconds(spec["R_beta"], cal_rates, spec["R_src"], TOY009.gamma_mean)
    assert abs(T - cap_days * 86400.0) < 1e-7

    # Componentwise necessary floors are NOT jointly sufficient: setting all
    # three at their individual floors costs 3*T_cap.
    nec, _ = specification(cap_days, TOY009)
    T_bad = total_time_seconds(
        nec["R_beta"], [nec["H_cal"]] * 7, nec["R_src"], TOY009.gamma_mean
    )
    assert abs(T_bad - 3.0 * cap_days * 86400.0) < 1e-7

    print("\nharmonic-mean identity: PASS")
    print("allocated envelope closes cap: PASS")
    print("NG-031 component-floor trap:", T_bad / (cap_days * 86400.0), "x cap")
    print("Iteration-080 apparatus specification envelope: PASS")


if __name__ == "__main__":
    main()
