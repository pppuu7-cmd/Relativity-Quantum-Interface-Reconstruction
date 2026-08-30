#!/usr/bin/env python3
"""RQIR Iteration 077 — apparatus-rate certificate and robust dominance audit.

No absolute detector ASD is assumed.  The script compresses the already-derived
physical Fisher-rate closure into measurable per-architecture certificate
coordinates and verifies the previously retained shared-kernel boundaries.
"""
from dataclasses import dataclass
from math import isclose

Z = 5.0
R_KEEP = 0.90
C_PREP = R_KEEP / (1.0 - R_KEEP) * Z**2


@dataclass(frozen=True)
class Certificate:
    R_beta: float
    gamma_mean: float
    R_cal: tuple
    R_src: float
    duty: float = 0.0

    def components(self):
        assert self.R_beta > 0.0
        assert self.R_src > 0.0
        assert all(r > 0.0 for r in self.R_cal)
        assert 0.0 <= self.duty < 1.0
        t_sci = Z**2 / self.R_beta
        t_cal_rows = tuple(self.gamma_mean / r for r in self.R_cal)
        t_cal = sum(t_cal_rows)
        t_src = C_PREP / self.R_src
        payload = t_sci + t_cal + t_src
        total = payload / (1.0 - self.duty)
        x_rows = tuple(t / t_sci for t in t_cal_rows)
        x = sum(x_rows)
        y = t_src / t_sci
        weights = {
            "science": t_sci / payload,
            "calibration_total": t_cal / payload,
            "source": t_src / payload,
            "calibration_rows": tuple(t / payload for t in t_cal_rows),
        }
        return {
            "t_sci": t_sci,
            "t_cal": t_cal,
            "t_src": t_src,
            "t_total": total,
            "x": x,
            "x_rows": x_rows,
            "y": y,
            "m_duty": 1.0 / (1.0 - self.duty),
            "weights": weights,
        }


def robust_time_interval(cert, frac_rate_error=0.0, duty_error=0.0):
    """Conservative independent interval for a common fractional rate error.

    Lower time uses all rates at +error and duty at its lower bound; upper time
    uses all rates at -error and duty at its upper bound.  This is deliberately
    conservative and is only a branch-selection guardrail, not a covariance
    model for apparatus metrology.
    """
    e = frac_rate_error
    assert 0.0 <= e < 1.0
    d_lo = max(0.0, cert.duty - duty_error)
    d_hi = min(1.0 - 1e-15, cert.duty + duty_error)

    def scaled(factor, duty):
        c = Certificate(
            R_beta=cert.R_beta * factor,
            gamma_mean=cert.gamma_mean,
            R_cal=tuple(r * factor for r in cert.R_cal),
            R_src=cert.R_src * factor,
            duty=duty,
        )
        return c.components()["t_total"]

    return scaled(1.0 + e, d_lo), scaled(1.0 - e, d_hi)


def robustly_dominates(a, b, frac_rate_error=0.0, duty_error=0.0):
    alo, ahi = robust_time_interval(a, frac_rate_error, duty_error)
    blo, bhi = robust_time_interval(b, frac_rate_error, duty_error)
    return ahi < blo


def shared_kernel_regressions():
    # Iteration 074 retained Toy014/Toy009 factors.
    qs14 = 3.53338589945
    qc14 = 3.48482822888
    qp14 = 0.67054046
    intercept_14_vs_9 = (qs14 - 1.0) / (1.0 - qp14)
    slope_14_vs_9 = (qc14 - 1.0) / (1.0 - qp14)

    # Iterations 065-066 retained Toy013/Toy009 factors.
    qs13 = 23.6495663
    qc13 = 0.1233011369
    qp13 = 330.9067
    intercept_13_vs_14 = (qs13 - qs14) / (qc14 - qc13)
    slope_13_vs_14 = (qp13 - qp14) / (qc14 - qc13)

    assert isclose(intercept_14_vs_9, 7.68952053854625, rel_tol=1e-12)
    assert isclose(slope_14_vs_9, 7.5421346999998855, rel_tol=1e-12)
    assert isclose(intercept_13_vs_14, 5.984238665975233, rel_tol=1e-12)
    assert isclose(slope_13_vs_14, 98.2399220663383, rel_tol=1e-12)
    return {
        "toy014_vs_toy009": (intercept_14_vs_9, slope_14_vs_9),
        "toy013_vs_toy014": (intercept_13_vs_14, slope_13_vs_14),
    }


def main():
    print(f"C_prep(Z=5,r=0.9) = {C_PREP:.12f}")
    r = shared_kernel_regressions()
    a, b = r["toy014_vs_toy009"]
    print(f"Toy014<Toy009 shared-kernel boundary: y > {a:.10f} + {b:.10f} x")
    a, b = r["toy013_vs_toy014"]
    print(f"Toy013<Toy014 shared-kernel boundary: x > {a:.10f} + {b:.10f} y")
    print("Iteration 077 regression checks: PASS")


if __name__ == "__main__":
    main()
