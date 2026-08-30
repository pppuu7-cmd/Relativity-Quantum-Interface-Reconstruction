"""RQIR Iteration 066: architecture-independent Toy013 vs Toy009 wall-clock dominance gate.

Uses only ratios already retained by Iteration 065.  No hardware claim is made.
All times are normalized to Toy009 D2 science exposure T_sci,009.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Ratios:
    s_eff_013_over_009: float = 0.04228407350
    calibration_013_over_009: float = 0.1233011369
    ramsey_rate_013_over_009: float = 0.003022


R = Ratios()

SCIENCE_RATIO = 1.0 / R.s_eff_013_over_009
SOURCE_TIME_RATIO = 1.0 / R.ramsey_rate_013_over_009


def total_ratio(x_cal: float, y_src: float, z_common: float = 0.0) -> float:
    """Return T013/T009.

    x_cal = Tcal,009 / Tsci,009
    y_src = Tsrc,009 / Tsci,009
    z_common = Tcommon / Tsci,009, credited equally to both architectures.

    The source ratio assumes equal acceptance, coupling normalization, reset regime,
    and Ramsey visibility. Deviations must be inserted explicitly in a later SI gate.
    """
    t009 = 1.0 + x_cal + y_src + z_common
    t013 = SCIENCE_RATIO + R.calibration_013_over_009 * x_cal + SOURCE_TIME_RATIO * y_src + z_common
    return t013 / t009


def calibration_threshold(y_src: float) -> float:
    """Minimum x_cal for Toy013 to beat Toy009 at given y_src, common costs cancel."""
    numerator = (SCIENCE_RATIO - 1.0) + (SOURCE_TIME_RATIO - 1.0) * y_src
    denominator = 1.0 - R.calibration_013_over_009
    return numerator / denominator


def main() -> None:
    print(f"science_time_ratio_013_009 = {SCIENCE_RATIO:.12f}")
    print(f"calibration_time_ratio_013_009 = {R.calibration_013_over_009:.12f}")
    print(f"ramsey_source_time_ratio_013_009 = {SOURCE_TIME_RATIO:.12f}")
    print(f"x_threshold_at_y0 = {calibration_threshold(0.0):.12f}")
    slope = (SOURCE_TIME_RATIO - 1.0) / (1.0 - R.calibration_013_over_009)
    print(f"threshold_slope_dx_dy = {slope:.12f}")
    for y in (0.0, 0.01, 0.1, 1.0):
        x = calibration_threshold(y)
        print(f"y={y:g}: x_threshold={x:.12f}; check_ratio={total_ratio(x, y):.12f}")

    # Regression checks.
    assert abs(total_ratio(calibration_threshold(0.0), 0.0) - 1.0) < 1e-12
    assert total_ratio(0.0, 0.0) > 1.0
    assert total_ratio(calibration_threshold(0.1) + 1.0, 0.1) < 1.0


if __name__ == "__main__":
    main()
