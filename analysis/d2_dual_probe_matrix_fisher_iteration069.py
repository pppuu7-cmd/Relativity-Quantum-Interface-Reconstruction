"""RQIR Iteration 069: same-time dual-probe matrix-Fisher calibration gate.

Purpose
-------
Close the next physical-resource step after Iteration 068 without assuming that
the two same-time probe channels provide independent SNR.  Each time layer is
modelled as a two-output Gaussian readout with a full 2x2 noise covariance (or,
in the spectral form, a 2x2 one-sided output PSD matrix).

The normalized white-noise benchmark is deliberately parameterized rather than
promoted to a particular apparatus.  It gives exact correlation penalties and
reproduces the Iteration-042 independent-channel limit at rho=0.

No new-physics claim is made by this script.
"""
from __future__ import annotations

import math
import numpy as np

GAMMA_MEAN_TOY009 = 1.830264703e6
GAMMA_MEAN_TOY012 = 1.2086865e6
TOY009_PHASES = np.array([0., 3.09855988, 3.45849306, 2.93830159,
                          4.13016958, 4.84480925, 4.99085067])
TOY012_PHASES = np.array([0., 1.038867458294, 2.985962997881,
                          4.875819177097, 4.150899563476,
                          1.623915172581, 5.275220686287])


def white_dual_probe_fisher(xi1: float, xi2: float, rho: float) -> np.ndarray:
    """Per accepted cycle Fisher block for row coordinates (u1,u2).

    Normalized output covariance is [[1,rho],[rho,1]].  xi1,xi2 are the
    single-channel score amplitudes that would give Fisher xi_i^2 if the
    channels were independent.
    """
    if xi1 <= 0 or xi2 <= 0:
        raise ValueError("xi1 and xi2 must be positive")
    if not (-1.0 < rho < 1.0):
        raise ValueError("rho must lie strictly between -1 and 1")
    J = np.diag([xi1, xi2])
    C = np.array([[1.0, rho], [rho, 1.0]])
    return J.T @ np.linalg.inv(C) @ J


def symmetric_eigenvalues(xi: float, rho: float) -> tuple[float, float]:
    F = white_dual_probe_fisher(xi, xi, rho)
    ev = np.linalg.eigvalsh(F)
    return float(ev[0]), float(ev[1])


def guaranteed_cycles_per_layer(gamma: float, xi: float, rho: float) -> float:
    """Cycles required to guarantee Fisher >= gamma in every 2D row direction."""
    lmin, _ = symmetric_eigenvalues(xi, rho)
    return gamma / lmin


def wall_time_hours(gamma: float, phases: np.ndarray, xi: float, rho: float,
                    gap_hz: float = 100.0, acceptance: float = 0.5,
                    dead_time_s: float = 1e-3) -> float:
    if gap_hz <= 0 or not (0 < acceptance <= 1) or dead_time_s < 0:
        raise ValueError("invalid acquisition parameters")
    n_attempts_per_layer = guaranteed_cycles_per_layer(gamma, xi, rho) / acceptance
    durations = phases / (2.0 * math.pi * gap_hz) + dead_time_s
    return n_attempts_per_layer * float(np.sum(durations)) / 3600.0


def spectral_matrix_fisher(Jf: np.ndarray, Sf: np.ndarray, df: float) -> np.ndarray:
    """Discrete one-sided PSD approximation to 4 int J^H S^-1 J df.

    Jf shape: (nf, 2, np), Sf shape: (nf, 2, 2).  Complex transfer functions
    are allowed.  The real part is returned because the Fisher matrix is real.
    """
    if Jf.ndim != 3 or Sf.ndim != 3 or Jf.shape[0] != Sf.shape[0]:
        raise ValueError("incompatible spectral array shapes")
    out = np.zeros((Jf.shape[2], Jf.shape[2]), dtype=np.complex128)
    for k in range(Jf.shape[0]):
        out += Jf[k].conj().T @ np.linalg.inv(Sf[k]) @ Jf[k]
    return (4.0 * df * out).real


def main() -> None:
    xi = 3.0
    rhos = (0.0, 0.25, 0.5, 0.75, 0.9)

    print("symmetric dual-probe Fisher, xi=3")
    for rho in rhos:
        lmin, lmax = symmetric_eigenvalues(xi, rho)
        inflation = xi * xi / lmin
        n9 = 7.0 * guaranteed_cycles_per_layer(GAMMA_MEAN_TOY009, xi, rho)
        n12 = 7.0 * guaranteed_cycles_per_layer(GAMMA_MEAN_TOY012, xi, rho)
        t9 = wall_time_hours(GAMMA_MEAN_TOY009, TOY009_PHASES, xi, rho)
        t12 = wall_time_hours(GAMMA_MEAN_TOY012, TOY012_PHASES, xi, rho)
        print(rho, lmin, lmax, inflation, n9, n12, t9, t12)

    # Exact analytic regression: for equal channel sensitivities,
    # eigenvalues are xi^2/(1+|rho|) and xi^2/(1-|rho|).
    for rho in (-0.9, -0.5, 0.0, 0.5, 0.9):
        lmin, lmax = symmetric_eigenvalues(xi, rho)
        assert abs(lmin - xi * xi / (1.0 + abs(rho))) < 1e-12
        assert abs(lmax - xi * xi / (1.0 - abs(rho))) < 1e-11

    # rho=0 must reproduce the Iteration-042 accepted-cycle count.
    n9_rho0 = 7.0 * guaranteed_cycles_per_layer(GAMMA_MEAN_TOY009, xi, 0.0)
    assert abs(n9_rho0 - 1423539.2134444444) < 1e-6

    # 100 Hz, p=.5, dead=1 ms wall-clock benchmarks.
    assert abs(wall_time_hours(GAMMA_MEAN_TOY009, TOY009_PHASES, xi, 0.0)
               - 5.009460939620266) < 1e-12
    assert abs(wall_time_hours(GAMMA_MEAN_TOY012, TOY012_PHASES, xi, 0.0)
               - 2.8913348975226874) < 1e-12
    assert abs(wall_time_hours(GAMMA_MEAN_TOY009, TOY009_PHASES, xi, 0.5)
               - 7.514191409430399) < 1e-12


if __name__ == "__main__":
    main()
