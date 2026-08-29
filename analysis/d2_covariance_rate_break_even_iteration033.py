"""RQIR Iteration 033: D2 covariance-rate / preparation-metrology break-even audit.

This is a resource-layer continuation of Iteration 032.  It does not invent an
SI apparatus.  It maps the documented Fisher benefit of added D2 covariance
rows onto the physical stationary-Gaussian covariance Fisher rate and derives
exact break-even inequalities against independent source-preparation Fisher.

Convention retained from Iteration 022:
    q_cov = eta_duty * B_eff * kappa_eff**2
for a scalar, approximately white log-PSD calibration coordinate.  For a
multi-channel spectral matrix this scalar q_cov is the corresponding integrated
matrix Fisher rate.
"""
from __future__ import annotations
import math

GC = 0.929e6
FQ = 13.2707

# Iteration-032 y_ref=-4, lambda=1 documented 90%-retention preparation costs.
CA_RELCOV_ONLY = 5.82122
CA_BEST4 = 0.5889578884945835
CA_ALL8 = 0.06708337269483168


def scalar_cov_rate(bandwidth_hz: float, kappa: float, duty: float = 1.0) -> float:
    """Stationary scalar covariance/log-PSD Fisher rate, 1/s."""
    return duty * bandwidth_hz * kappa * kappa


def bundle_time(nrows: int, q_per_row: float, gamma_cov: float = GC) -> float:
    return nrows * gamma_cov / q_per_row


def break_even_q_over_rp(nrows: int, delta_ca: float, gamma_cov: float = GC) -> float:
    """Equal-row-rate threshold q_cov/R_P for covariance to beat prep Fisher."""
    return nrows * gamma_cov / delta_ca


def required_kappa(threshold_q_over_rp: float, prep_rate: float,
                   bandwidth_hz: float, duty: float = 1.0) -> float:
    q_req = threshold_q_over_rp * prep_rate
    return math.sqrt(q_req / (duty * bandwidth_hz))


def main() -> None:
    d_first4 = CA_RELCOV_ONLY - CA_BEST4
    d_second4 = CA_BEST4 - CA_ALL8
    d_all8 = CA_RELCOV_ONLY - CA_ALL8

    th_first4 = break_even_q_over_rp(4, d_first4)
    th_second4 = break_even_q_over_rp(4, d_second4)
    th_all8 = break_even_q_over_rp(8, d_all8)

    print("DeltaCa first best four:", d_first4)
    print("DeltaCa second four:", d_second4)
    print("DeltaCa all eight:", d_all8)
    print("equal-row q_cov/R_P break-even first4:", th_first4)
    print("equal-row q_cov/R_P break-even second4:", th_second4)
    print("equal-row q_cov/R_P break-even all8:", th_all8)

    # Transparent rate illustrations only; not apparatus forecasts.
    B = 1.0e3
    for tprep in (1.0, 100.0, 1.0e4):
        rp = FQ / tprep  # ideal accepted-copy QFI, p*eta=1
        k1 = required_kappa(th_first4, rp, B)
        k2 = required_kappa(th_second4, rp, B)
        print(f"tprep={tprep:g}s R_P={rp:.12g}/s kappa_first4={k1:.9g} kappa_second4={k2:.9g}")

    # Regression values defining the Iteration-033 arithmetic.
    assert abs(d_first4 - 5.232262111505417) < 1e-12
    assert abs(d_second4 - 0.5218745157997519) < 1e-12
    assert abs(th_first4 - 710209.068431176) < 1e-6
    assert abs(th_second4 - 7120485.648365831) < 1e-5
    assert abs(th_all8 - 1291592.550085246) < 1e-6
    assert abs(required_kappa(th_first4, FQ, 1e3) - 97.08229233196755) < 1e-10
    assert abs(required_kappa(th_first4, FQ/1e4, 1e3) - 0.9708229233196757) < 1e-12


if __name__ == "__main__":
    main()
