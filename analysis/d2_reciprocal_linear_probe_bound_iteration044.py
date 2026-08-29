"""RQIR Iteration 044: reciprocal source-probe linear-detector information/backaction bound.

This moves one layer beyond the direct source-monitoring proxy of Iteration 043.
Use a reciprocal linear source-probe coupling with probe susceptibility chi:

    x_p = chi * (g u + F_BA)
    y   = x_p + x_imp

where u is the source coordinate to be estimated, x_imp is detector imprecision,
and F_BA is detector force backaction on the probe. Reciprocity transmits the
probe displacement back to the source, so the detector-induced source force is
proportional to g*chi*F_BA.

For the relevant real quadrature, detector noises obey the normalized quantum
noise inequality

    S_xx S_FF - S_xF^2 >= hbar^2/(4 eta).

The source-referred measurement-noise PSD and source-backaction PSD are

    S_u = (S_xx + chi^2 S_FF + 2 chi S_xF)/(g^2 chi^2)
    S_BA,src = g^2 chi^2 S_FF.

Their product obeys

    S_u S_BA,src >= hbar^2/(4 eta),

independently of g and chi.  Optimal imprecision/backaction correlation can
saturate, but not beat, the bound in this reciprocal linear class.

Using the white-noise convention matched to Iteration 043,

    I_u = T/S_u,
    zeta = S_BA,src*T/hbar^2,

so zeta >= I_u/(4 eta).  Therefore the best reciprocal linear probe reproduces
the same minimum source dephasing at fixed Fisher as the ideal diffusive direct
monitor; transduction can beat technical noise, not the fundamental reciprocal
information/backaction product.
"""
from __future__ import annotations

import math
import numpy as np

import d2_information_backaction_proxy_iteration043 as i43

HBAR = 1.0
XI_SHARED = i43.XI_SHARED_N4
XI_CROSS = i43.XI_MEAN_COV_CROSS


def qnoise_bound(eta: float = 1.0) -> float:
    if not (0 < eta <= 1):
        raise ValueError("eta must be in (0,1]")
    return HBAR * HBAR / (4.0 * eta)


def source_referred_noises(g: float, chi: float, sxx: float,
                            sff: float, sxf: float) -> tuple[float, float]:
    if g == 0 or chi == 0 or sff <= 0:
        raise ValueError("g, chi and sff must be nonzero/positive")
    sy = sxx + chi * chi * sff + 2.0 * chi * sxf
    su = sy / (g * g * chi * chi)
    sba = g * g * chi * chi * sff
    return su, sba


def optimal_noises_at_fixed_sff(chi: float, sff: float,
                                 eta: float = 1.0) -> tuple[float, float]:
    """Quantum-limited detector noises saturating the source-referred bound."""
    q = qnoise_bound(eta)
    sxf = -chi * sff
    sxx = chi * chi * sff + q / sff
    return sxx, sxf


def minimum_zeta_for_fisher(info: float, eta: float = 1.0) -> float:
    return info / (4.0 * eta)


def max_xi_for_response_norm(target: float, eta: float = 1.0) -> float:
    if not (0 < target < 1):
        raise ValueError("target must be in (0,1)")
    lo, hi = 0.0, 10.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        _z, ratio, _align, _c0, _c1 = i43.response_after_parallel_force_monitoring(mid, eta)
        if ratio >= target:
            lo = mid
        else:
            hi = mid
    return lo


def main() -> None:
    # Explicit saturation checks for several arbitrary transductions.
    for g, chi, sff, eta in [
        (0.3, 2.0, 0.7, 1.0),
        (4.0, 0.2, 3.0, 0.8),
        (11.0, 7.0, 0.05, 0.5),
    ]:
        sxx, sxf = optimal_noises_at_fixed_sff(chi, sff, eta)
        su, sba = source_referred_noises(g, chi, sxx, sff, sxf)
        prod = su * sba
        print("saturating", g, chi, eta, "Su*SBA=", prod,
              "bound=", qnoise_bound(eta))
        assert abs(prod - qnoise_bound(eta)) < 1e-12
        assert abs(sxx * sff - sxf * sxf - qnoise_bound(eta)) < 1e-12

    # Random valid detector noises cannot beat the bound.
    rng = np.random.default_rng(20260829)
    for _ in range(2000):
        eta = float(rng.uniform(0.2, 1.0))
        g = float(10 ** rng.uniform(-1, 1))
        chi = float(10 ** rng.uniform(-1, 1))
        sff = float(10 ** rng.uniform(-2, 2))
        sxf = float(rng.normal() * math.sqrt(qnoise_bound(eta)))
        excess = float(10 ** rng.uniform(-4, 2))
        sxx = (sxf * sxf + qnoise_bound(eta)) / sff + excess
        su, sba = source_referred_noises(g, chi, sxx, sff, sxf)
        assert su * sba >= qnoise_bound(eta) - 1e-12

    # The reciprocal bound maps exactly onto the ideal dephasing lower bound
    # used in Iteration 043.
    for xi in (XI_SHARED, XI_CROSS):
        zmin = minimum_zeta_for_fisher(xi * xi, 1.0)
        z43 = i43.zeta_for_information(xi, 1.0)
        assert abs(zmin - z43) < 1e-15

    # Toy009 response-retention consequences at the quantum limit.
    xi_fisher90 = max_xi_for_response_norm(math.sqrt(0.90), 1.0)
    xi_amp90 = max_xi_for_response_norm(0.90, 1.0)
    xi_amp80 = max_xi_for_response_norm(0.80, 1.0)
    print("xi max for 90% raw detector Fisher (sqrt response)=", xi_fisher90)
    print("xi max for 90% response norm=", xi_amp90)
    print("xi max for 80% response norm=", xi_amp80)

    assert abs(xi_fisher90 - 0.7239816836368367) < 2e-12
    assert abs(xi_amp90 - 1.0263611861288113) < 2e-12
    assert abs(xi_amp80 - 1.5026667817532025) < 2e-12

    # Current optimistic shared and wall-time-crossover targets exceed the
    # 90%-raw-detector-Fisher compatible quantum-limited shared-copy strength.
    for label, xi in (("shared-N4", XI_SHARED), ("mean/cov crossover", XI_CROSS)):
        _z, r, align, _c0, _c1 = i43.response_after_parallel_force_monitoring(xi, 1.0)
        raw_fisher_ret = r * r
        print(label, "xi=", xi, "response retention=", r,
              "raw detector Fisher retention=", raw_fisher_ret,
              "alignment=", align)

    r_shared = i43.response_after_parallel_force_monitoring(XI_SHARED, 1.0)[1]
    r_cross = i43.response_after_parallel_force_monitoring(XI_CROSS, 1.0)[1]
    assert abs(r_shared * r_shared - 0.7343881235771952) < 2e-12
    assert abs(r_cross * r_cross - 0.24349302016306754) < 2e-12
    assert XI_SHARED > xi_fisher90
    assert XI_CROSS > xi_fisher90

    # Efficiency tightens the allowed xi at fixed response-retention target as sqrt(eta).
    for eta in (0.8, 0.5, 0.2):
        xi = max_xi_for_response_norm(math.sqrt(0.90), eta)
        expected = xi_fisher90 * math.sqrt(eta)
        print("eta", eta, "xi max for 90% raw detector Fisher", xi)
        assert abs(xi - expected) < 2e-12


if __name__ == "__main__":
    main()
