"""RQIR Iteration 072: physical resource dominance / rescue-factor audit for Toy012.

This follows Iteration 071's general Fisher-rate wall-clock closure and uses only
physical quantities that survived the Iteration-062/063 detector-metric
correction.

Under shared detector transfer/scheduling kernels, compare each source to
Toy009 by three multiplicative wall-clock factors:

  q_s = T_science(source) / T_science(Toy009)
  q_c = T_cal(source)     / T_cal(Toy009)
  q_p = T_src(source)     / T_src(Toy009)

A candidate with q_s,q_c,q_p > 1 is componentwise dominated in the projected
(science, calibration, independent source-metrology) resource space.  This is
not an apparatus-independent theorem if source geometry changes transfer/PSD,
so the script also computes the minimum source-specific rate gains needed to
rescue each component, as required by RQIR-NG-029.
"""
from __future__ import annotations

# Iteration 062 exact equal-ASD spectral-tilt-profiled D2 information ratios.
SEFF_RATIO_BALANCED = 1.9696285538e-8
SEFF_RATIO_HIGH = 1.2139856294e-4

# Iteration 063 conservative lower bounds from regression guards.  The actual
# 900-point scan values are around 4.7e4 and 5.2e2 respectively; using lower
# bounds makes the dominance claims conservative.
CAL_TIME_RATIO_BALANCED_MIN = 4.4e4
CAL_TIME_RATIO_HIGH_MIN = 490.0

# Independent zero-reset Ramsey Fisher-rate coefficients.
RAMSEY_RATE_009 = 0.0025234392
RAMSEY_RATE_BALANCED = 0.002134292844
# Iteration 055 regression: high-response Toy012 / Toy009 Ramsey rate ratio.
RAMSEY_RATE_RATIO_HIGH = 1.150503


def time_ratio_from_rate_ratio(rate_ratio: float) -> float:
    if rate_ratio <= 0:
        raise ValueError("rate ratio must be positive")
    return 1.0 / rate_ratio


def total_ratio(qs: float, qc: float, qp: float, x: float, y: float) -> float:
    """T_source/T009, normalized by T_sci,009 and excluding controls.

    Baseline Toy009 total is 1+x+y, where x=T_cal,009/T_sci,009 and
    y=T_src,009/T_sci,009.
    """
    return qs + qc * x + qp * y


def high_y_threshold(x: float, qc: float = CAL_TIME_RATIO_HIGH_MIN) -> float:
    """Minimum y for high-response Toy012 to beat Toy009 in projected budget.

    Uses the conservative lower-bound calibration ratio.  If the actual
    calibration ratio is larger, the true threshold is larger.
    """
    qs = 1.0 / SEFF_RATIO_HIGH
    qp = time_ratio_from_rate_ratio(RAMSEY_RATE_RATIO_HIGH)
    denom = 1.0 - qp
    if denom <= 0:
        return float("inf")
    return ((qs - 1.0) + (qc - 1.0) * x) / denom


def main() -> None:
    qs_b = 1.0 / SEFF_RATIO_BALANCED
    qc_b = CAL_TIME_RATIO_BALANCED_MIN
    qp_b = time_ratio_from_rate_ratio(RAMSEY_RATE_BALANCED / RAMSEY_RATE_009)

    qs_h = 1.0 / SEFF_RATIO_HIGH
    qc_h = CAL_TIME_RATIO_HIGH_MIN
    qp_h = time_ratio_from_rate_ratio(RAMSEY_RATE_RATIO_HIGH)

    print("balanced Toy012 conservative time factors", qs_b, qc_b, qp_b)
    print("high-response Toy012 conservative time factors", qs_h, qc_h, qp_h)

    # Balanced Toy012 is componentwise worse in all three retained resources.
    assert qs_b > 5.0e7
    assert qc_b > 1.0
    assert qp_b > 1.0
    for x, y in [(0.0, 0.0), (0.1, 0.1), (1.0, 1.0), (100.0, 100.0)]:
        assert total_ratio(qs_b, qc_b, qp_b, x, y) > 1.0 + x + y

    # Minimum source-specific Fisher-rate gains required just for componentwise
    # parity with Toy009 under the reference factorization.
    print("balanced rescue gains science/cal/source", qs_b, qc_b, qp_b)

    # The high-response point has a modest Ramsey advantage, so it is not
    # mathematically componentwise dominated.  Quantify how source-metrology
    # dominated the baseline must be for that one advantage to overcome its
    # enormous science/calibration penalties.
    y0 = high_y_threshold(0.0)
    slope = high_y_threshold(1.0) - y0
    print("high-response ycrit(x=0)", y0)
    print("high-response ycrit slope per x", slope)
    print("high-response rescue gains science/cal; source already faster", qs_h, qc_h)

    assert 5.07709e7 < qs_b < 5.07711e7
    assert abs(qp_b - 1.18233034754) < 2e-10
    assert 8237.32 < qs_h < 8237.34
    assert abs(qp_h - 0.869185043411) < 2e-10
    assert abs(y0 - 62961.68277) < 0.02
    assert abs(slope - 3738.104669) < 0.02

    # Even with x=0, high-response Toy012 wins only if Toy009 source metrology
    # consumes >~6.3e4 of its own science times under these optimistic shared
    # external-protocol assumptions.
    assert y0 > 6.2e4


if __name__ == "__main__":
    main()
