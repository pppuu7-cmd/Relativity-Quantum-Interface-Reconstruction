"""RQIR Iteration 125: canonical Paper-III notation/dependency regression.

This checker freezes the final-significance/source-calibration conventions used
by the manuscript-facing front. Historical raw-5sigma/90%-retention numbers
remain valid only when explicitly labeled as such.
"""
from __future__ import annotations

import math


def fixed_retention_final_target(z_final: float, r: float) -> tuple[float, float]:
    """Return (A_raw, C_src) for final F*=z_final^2 at retained fraction r."""
    if z_final <= 0 or not (0.0 < r < 1.0):
        raise ValueError("invalid target")
    f_star = z_final * z_final
    return f_star / r, f_star / (1.0 - r)


def final_fisher(a_raw: float, c_src: float) -> float:
    if a_raw <= 0 or c_src <= 0:
        raise ValueError("positive Fisher required")
    return a_raw * c_src / (a_raw + c_src)


def joint_rate(r1: float, r2: float) -> float:
    """Effective final-Fisher rate for two independent multiplicative bottlenecks."""
    if r1 <= 0 or r2 <= 0:
        raise ValueError("positive rates required")
    return 1.0 / (1.0 / math.sqrt(r1) + 1.0 / math.sqrt(r2)) ** 2


def main() -> None:
    # Historical raw-5sigma regression: valid but NOT a final-5sigma certificate.
    a_hist = 25.0
    c_hist = 225.0
    f_hist = final_fisher(a_hist, c_hist)
    assert abs(f_hist - 22.5) < 1e-14
    assert abs(math.sqrt(f_hist) - 4.743416490252569) < 1e-14

    # Canonical final-5sigma / fixed-90%-retention pair.
    a_raw, c_src = fixed_retention_final_target(5.0, 0.90)
    assert abs(a_raw - 27.77777777777778) < 1e-13
    assert abs(c_src - 250.0) < 1e-12
    assert abs(final_fisher(a_raw, c_src) - 25.0) < 1e-13

    # If retention is optimized rather than fixed, the optimum depends on rates.
    rs, ra = 1.0, 9.0
    r_star = math.sqrt(ra) / (math.sqrt(rs) + math.sqrt(ra))
    assert abs(r_star - 0.75) < 1e-14
    assert abs(joint_rate(rs, ra) - 0.5625) < 1e-14

    # 90% is optimal only for Ra/Rs=81.
    rs, ra = 1.0, 81.0
    r_star = math.sqrt(ra) / (math.sqrt(rs) + math.sqrt(ra))
    assert abs(r_star - 0.9) < 1e-14

    # Canonical architecture-variable identities.
    rd09, rd14 = 2.0, 3.0
    ra09, ra14 = 5.0, 4.0
    d09, d14 = 0.10, 0.20
    u = rd14 / rd09
    v = ra14 / ra09
    z = ra09 / rd09
    delta = (1.0 - d14) / (1.0 - d09)
    assert (u, v, z) == (1.5, 0.8, 2.5)
    assert abs(delta - 8.0 / 9.0) < 1e-14

    print("historical raw-5sigma benchmark final Z", math.sqrt(f_hist))
    print("canonical final-5sigma fixed-retention A_raw,C_src", a_raw, c_src)
    print("90%-retention optimum requires Ra/Rs", 81.0)
    print("canonical architecture variables", u, v, z, delta)


if __name__ == "__main__":
    main()
