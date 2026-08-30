#!/usr/bin/env python3
"""RQIR Iteration 100 — single-platform cross-spectral apparatus audit.

This script is a deterministic certificate/guardrail check, not a hardware
forecast.  It encodes the minimum distinction between (i) a measured spatial
2x2 spectral matrix and (ii) the RQIR temporal f,2f force-coordinate spectral
matrix needed by the D2 science likelihood.

External anchor: Gosling et al., Phys. Rev. Research 6, 013129 (2024), which
experimentally measures PSDs and x-y cross-correlation spectra in one levitated
nanoparticle platform and gives the calibrated force-domain relation
S_xy = Re[chi_x^* chi_y] S_ff^dir cos(Psi) sin(Psi).
"""
from dataclasses import dataclass
from math import sqrt, isclose


@dataclass(frozen=True)
class CertificateCut:
    name: str
    status: str  # CLOSED, PARTIAL, OPEN


def rho_from_matrix(sxx: float, syy: float, sxy: float) -> float:
    assert sxx > 0 and syy > 0
    rho = sxy / sqrt(sxx * syy)
    assert abs(rho) <= 1.0 + 1e-12
    return rho


def rqir_two_band_rate(r2: float, r4: float, rho: float) -> float:
    assert r2 > 0 and r4 > 0 and abs(rho) < 1
    return 4.0 * r2 * r4 / (r2 + r4 + 2.0 * rho * sqrt(r2 * r4))


def force_cross_spectrum_gain(chix_re, chix_im, chiy_re, chiy_im):
    # Re[chi_x^* chi_y]
    return chix_re * chiy_re + chix_im * chiy_im


def main():
    # Algebraic regression of the calibrated cross-spectrum relation.
    gx = force_cross_spectrum_gain(1.0, 2.0, 3.0, -0.5)
    assert isclose(gx, 2.0, rel_tol=0, abs_tol=1e-15)

    # PSD matrix positivity / correlation regression.
    sxx, syy, sxy = 4.0, 9.0, 3.0
    rho = rho_from_matrix(sxx, syy, sxy)
    assert isclose(rho, 0.5, rel_tol=0, abs_tol=1e-15)

    # Same numerical rho is admissible in the RQIR f,2f law ONLY after a
    # physical coordinate map has established that the matrix entries refer to
    # the two temporal science bands in one input-referred force coordinate.
    rate = rqir_two_band_rate(2.0, 8.0, rho)
    assert isclose(rate, 64.0 / 14.0, rel_tol=1e-15)

    cuts = [
        CertificateCut('same-platform PSD + cross-spectrum measurement', 'CLOSED'),
        CertificateCut('force-domain susceptibility/calibration relation', 'PARTIAL'),
        CertificateCut('exact temporal f,2f input-referred force matrix', 'OPEN'),
        CertificateCut('seven RQIR calibration Fisher blocks/rates', 'OPEN'),
        CertificateCut('Toy009/Toy014 source-preparation throughput', 'OPEN'),
        CertificateCut('campaign duty/control/characterization-rate envelope', 'OPEN'),
    ]

    assert sum(c.status == 'CLOSED' for c in cuts) == 1
    assert sum(c.status == 'PARTIAL' for c in cuts) == 1
    assert sum(c.status == 'OPEN' for c in cuts) == 4

    print('PASS Iteration 100 single-platform cross-spectral audit')
    print('illustrative spatial rho =', rho)
    print('illustrative mapped f,2f rate (mapping assumed only for regression) =', rate)
    for c in cuts:
        print(f'{c.status:7s}  {c.name}')


if __name__ == '__main__':
    main()
