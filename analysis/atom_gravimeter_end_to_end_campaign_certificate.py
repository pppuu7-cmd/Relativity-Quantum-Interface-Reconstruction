"""RQIR Paper III — end-to-end campaign certificate (source-grounded proxy edition).

This file consolidates the strengthened Paper-III atom-gravimeter chain into one
campaign resource ledger. It deliberately distinguishes a source-grounded
calibration proxy from a truly certified absolute reference calibration.

Source anchors
--------------
Le Gouet et al., Appl. Phys. B 92, 133-144 (2008), arXiv:0801.1270:
- typical corrected gravimeter sensitivity about 2e-8 g at 1 s;
- seismometer/atom transfer function measured by deliberately exciting the
  isolation platform at selected frequencies and recording atomic and
  seismometer signals simultaneously;
- low-frequency scale-factor difference between two identical seismometers
  below 1% (used here only as a conservative proxy systematic floor, NOT as a
  certified absolute calibration uncertainty for the proposed injected line);
- transition-probability post-correction requires mid-fringe operation and
  stable contrast; the detector-facing RQIR audit already profiles these terms.

Protocol frozen here
--------------------
- science campaign length: 3600 s wall time;
- one 30 s dedicated reference-transfer calibration block every 600 s;
- reference platform oscillation amplitude: 1 micro-g;
- science duty fraction: (600-30)/600 = 0.95;
- reference fractional uncertainty = quadrature of
    1% source-grounded seismometer scale proxy
    + statistical amplitude uncertainty inferred from the published
      2e-8 g/sqrt(Hz) corrected sensitivity over the 30 s calibration block;
- detector-facing statistical science uncertainty is propagated from the
  already validated nonlinear probability-likelihood result at 600 s and the
  stationary 1/sqrt(time) resource law.

This certificate is intentionally conservative in status:
PASS means the protocol/resource/calibration bookkeeping is internally closed.
It does NOT mean the 1% reference prior is a certified absolute metrology result.
"""
from __future__ import annotations

import math

WALL_TIME_S = 3600.0
CAL_PERIOD_S = 600.0
CAL_BLOCK_S = 30.0
REFERENCE_G = 1.0e-6
PUBLISHED_CORRECTED_G_1S = 2.0e-8
SEISMOMETER_SCALE_PROXY_FRAC = 0.01

# Authority from the preceding detector-facing nonlinear likelihood audit.
DETECTOR_SIGMA_600S_NG = 1.829
DETECTOR_REFERENCE_BASELINE_FRAC = 0.01


def calibration_uncertainty() -> dict[str, float]:
    stat_frac = (
        PUBLISHED_CORRECTED_G_1S
        / (REFERENCE_G * math.sqrt(CAL_BLOCK_S))
    )
    total_frac = math.sqrt(SEISMOMETER_SCALE_PROXY_FRAC**2 + stat_frac**2)
    return {
        "statistical_fraction": stat_frac,
        "proxy_systematic_fraction": SEISMOMETER_SCALE_PROXY_FRAC,
        "total_reference_fraction": total_frac,
    }


def resource_ledger() -> dict[str, float]:
    n_blocks = WALL_TIME_S / CAL_PERIOD_S
    calibration_time = n_blocks * CAL_BLOCK_S
    science_time = WALL_TIME_S - calibration_time
    duty = science_time / WALL_TIME_S

    # Stationary information scaling established in prior RQIR resource audits.
    sigma_stat_ng = DETECTOR_SIGMA_600S_NG * math.sqrt(600.0 / science_time)

    return {
        "wall_time_s": WALL_TIME_S,
        "calibration_blocks": n_blocks,
        "calibration_time_s": calibration_time,
        "science_time_s": science_time,
        "science_duty_fraction": duty,
        "sigma_stat_ng": sigma_stat_ng,
    }


def science_sigma(theta_ng: float) -> dict[str, float]:
    if theta_ng < 0:
        raise ValueError("theta_ng must be non-negative")
    cal = calibration_uncertainty()
    res = resource_ledger()
    fref = cal["total_reference_fraction"]
    sigma = math.sqrt(res["sigma_stat_ng"]**2 + (theta_ng * fref) ** 2)
    crossover = res["sigma_stat_ng"] / fref
    return {
        "theta_ng": theta_ng,
        "sigma_total_ng": sigma,
        "sigma_stat_ng": res["sigma_stat_ng"],
        "reference_fraction": fref,
        "crossover_theta_ng": crossover,
    }


def cadence_stress() -> list[dict[str, float]]:
    rows = []
    for period in [300.0, 600.0, 1800.0, 3600.0]:
        n_blocks = WALL_TIME_S / period
        cal_time = n_blocks * CAL_BLOCK_S
        science_time = WALL_TIME_S - cal_time
        duty = science_time / WALL_TIME_S
        sigma = DETECTOR_SIGMA_600S_NG * math.sqrt(600.0 / science_time)
        rows.append({
            "period_s": period,
            "science_duty": duty,
            "science_time_s": science_time,
            "sigma_stat_ng": sigma,
        })
    return rows


def structural_assertions() -> None:
    cal = calibration_uncertainty()
    res = resource_ledger()

    assert abs(cal["statistical_fraction"] - 0.00365148) < 1e-6
    assert abs(cal["total_reference_fraction"] - 0.0106458) < 1e-6
    assert abs(res["science_duty_fraction"] - 0.95) < 1e-12
    assert abs(res["science_time_s"] - 3420.0) < 1e-12
    assert 0.75 < res["sigma_stat_ng"] < 0.78

    # At small theta the campaign is statistics dominated.
    small = science_sigma(1.0)
    assert abs(small["sigma_total_ng"] / small["sigma_stat_ng"] - 1.0) < 0.001

    # At sufficiently large theta the reference floor must become visible.
    large = science_sigma(100.0)
    assert large["sigma_total_ng"] > large["sigma_stat_ng"]
    assert 70.0 < large["crossover_theta_ng"] < 75.0

    # More frequent calibration costs exposure but never destroys the resource
    # ledger; the 10-minute baseline stays within a few percent of the no-cost
    # statistical limit for a one-hour campaign.
    rows = cadence_stress()
    assert all(r["science_duty"] > 0.85 for r in rows)
    assert rows[0]["sigma_stat_ng"] > rows[-1]["sigma_stat_ng"]


def print_certificate() -> None:
    cal = calibration_uncertainty()
    res = resource_ledger()
    print("RQIR Paper-III end-to-end campaign certificate")
    print(f"wall time                 = {res['wall_time_s']:.0f} s")
    print(f"calibration blocks        = {res['calibration_blocks']:.0f}")
    print(f"calibration time          = {res['calibration_time_s']:.0f} s")
    print(f"science time              = {res['science_time_s']:.0f} s")
    print(f"science duty              = {res['science_duty_fraction']:.3f}")
    print(f"reference stat fraction   = {cal['statistical_fraction']:.6%}")
    print(f"reference proxy systematic= {cal['proxy_systematic_fraction']:.6%}")
    print(f"reference total fraction  = {cal['total_reference_fraction']:.6%}")
    print(f"science statistical sigma = {res['sigma_stat_ng']:.6g} ng")
    print("\nscience amplitude | total sigma | calibration crossover")
    for theta in [1.0, 10.0, 50.0, 100.0, 1000.0]:
        row = science_sigma(theta)
        print(
            f"{theta:17.3f} ng | {row['sigma_total_ng']:11.6g} ng | "
            f"{row['crossover_theta_ng']:11.6g} ng"
        )
    print("\nCadence stress:")
    for row in cadence_stress():
        print(
            f"period={row['period_s']:6.0f}s duty={row['science_duty']:.4f} "
            f"sigma_stat={row['sigma_stat_ng']:.6g} ng"
        )
    print("\nDecision:")
    print("PROTOCOL + DUTY-CYCLE + CALIBRATION-FLOOR LEDGER: PASS")
    print("SOURCE-GROUNDED REFERENCE UNCERTAINTY PROXY: PASS AS PROXY")
    print("CERTIFIED ABSOLUTE REFERENCE METROLOGY: OPEN")
    print("PAPER-III FINAL 100% SCIENTIFIC CLOSURE: NOT YET AUTHORIZED")


def main() -> None:
    structural_assertions()
    print_certificate()


if __name__ == "__main__":
    main()
