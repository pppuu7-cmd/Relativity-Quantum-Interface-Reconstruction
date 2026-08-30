#!/usr/bin/env python3
"""RQIR Iteration 098 — source-metrology physical shot certificate.

Converts the retained independent-source Fisher target C_src into accepted
copies, attempted preparations, coherent evolution time and wall-clock time.
The 100-Hz numerical slice is a declared benchmark, not a hardware forecast.
"""
from math import pi, isclose

C_SRC = 225.0

# Repository-retained zero-reset, V=1 Ramsey Fisher/time optima.
PHI_009 = 1.09231
Q_009 = 0.0025234392          # max F_alpha / phi
PHI_014 = 0.9264295097660072
Q_014 = 0.0037632915041337926


def accepted_fisher(phi, q):
    return phi * q


def accepted_copies(C, Fcopy):
    return C / Fcopy


def attempted_copies(C, Fcopy, p):
    assert 0 < p <= 1
    return accepted_copies(C, Fcopy) / p


def wall_time_from_shots(C, phi, q, p, Omega, t_reset=0.0):
    Fcopy = accepted_fisher(phi, q)
    Ntry = attempted_copies(C, Fcopy, p)
    return Ntry * (t_reset + phi / Omega)


def wall_time_from_rate(C, q_reset, p, Omega):
    return C / (p * Omega * q_reset)


def source_rate_floor(T_cap, duty):
    assert 0 <= duty < 1
    m = 1.0 / (1.0 - duty)
    return m * C_SRC / T_cap


def min_pOmega_for_cap(T_cap, duty, q_reset):
    return source_rate_floor(T_cap, duty) / q_reset


def main():
    F9 = accepted_fisher(PHI_009, Q_009)
    F14 = accepted_fisher(PHI_014, Q_014)
    N9 = accepted_copies(C_SRC, F9)
    N14 = accepted_copies(C_SRC, F14)

    # Declared 100-Hz energy-gap benchmark, p=0.5, zero reset, V=1.
    Omega = 2.0 * pi * 100.0
    p = 0.5
    te9 = PHI_009 / Omega
    te14 = PHI_014 / Omega
    T9 = wall_time_from_shots(C_SRC, PHI_009, Q_009, p, Omega)
    T14 = wall_time_from_shots(C_SRC, PHI_014, Q_014, p, Omega)

    # Algebraic consistency with the rate form R_src=p Omega q.
    assert isclose(T9, wall_time_from_rate(C_SRC, Q_009, p, Omega), rel_tol=2e-12)
    assert isclose(T14, wall_time_from_rate(C_SRC, Q_014, p, Omega), rel_tol=2e-12)

    # Seven-day, 5% duty source-only feasibility slice retained from Iteration 091.
    Tcap = 7.0 * 24.0 * 3600.0
    duty = 0.05
    floor = source_rate_floor(Tcap, duty)
    pOm9 = min_pOmega_for_cap(Tcap, duty, Q_009)
    pOm14 = min_pOmega_for_cap(Tcap, duty, Q_014)

    # Stable numerical regressions from repository-retained coefficients.
    assert abs(F9 - 0.002756377872552) < 5e-12
    assert abs(F14 - 0.00348642430328125) < 5e-12
    assert abs(N9 - 81628.8659986) < 2e-4
    assert abs(N14 - 64536.0347529) < 2e-4
    assert abs(te9 - 0.00173846535888708) < 5e-15
    assert abs(te14 - 0.00147445835905461) < 5e-15
    assert abs(T9 - 283.817911647536) < 2e-9
    assert abs(T14 - 190.311391803378) < 2e-9
    assert abs(floor - 3.916040100250626e-4) < 2e-16

    print('PASS Iteration 098 source-metrology shot certificate')
    print('Toy009 F/copy=', F9, 'N_acc=', N9, 'N_try(p=.5)=', 2*N9,
          't_evol@100Hz=', te9, 'T_src=', T9)
    print('Toy014 F/copy=', F14, 'N_acc=', N14, 'N_try(p=.5)=', 2*N14,
          't_evol@100Hz=', te14, 'T_src=', T14)
    print('7d, duty=.05 source floor=', floor)
    print('minimum p*Omega at zero reset/V=1: Toy009=', pOm9, 'Toy014=', pOm14)


if __name__ == '__main__':
    main()
