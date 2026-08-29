"""RQIR Iteration 019: branch-specific physical detector Fisher rates.

Replaces the standardized detector sensitivity xi by transparent parametric
rates for the current Iteration-011 Toy009 baseline.

D1: binary-fringe phase information with contrast C, accepted-shot
probability p_acc, four-switch dual-band window, interrogation time T, and
dead time.  At quadrature, an ideal binary fringe contributes ~C^2 phase
Fisher per accepted event.

D2: continuous force-domain information with equivalent-force ASD in the two
bands and detector duty cycle.  The mechanical transfer function is assumed
already absorbed into the equivalent-force PSD.

The script is a resource/scaling model, not a hardware forecast.
"""
from __future__ import annotations

import math
import numpy as np

G = 6.67430e-11
HBAR = 1.054571817e-34
ALPHA = 0.1
L0 = 10e-6

# Iteration-011 accepted balanced Toy009 harmonics (rounded stored values).
H2 = complex(+0.00245460, -0.01049981)
H4 = complex(-0.00395383, -0.01338211)
G2 = complex(+0.00285553, -0.01750306)
G4 = complex(-0.00463232, -0.01567853)


def profile_two_band(p2: float, p4: float) -> float:
    """Two-band information after profiling one relative spectral-tilt nuisance."""
    if p2 <= 0.0 or p4 <= 0.0:
        return 0.0
    return 4.0 * p2 * p4 / (p2 + p4)


def four_switch_windows(a: float) -> tuple[float, float]:
    """pi-periodic +/− sequence: + for a then − for pi-a, repeated."""
    return 2.0 * abs(math.sin(a)) / math.pi, abs(math.sin(2.0 * a)) / math.pi


def optimize_four_switch(n_grid: int = 200_000):
    a_grid = np.linspace(1e-6, math.pi - 1e-6, n_grid)
    best = None
    for a in a_grid:
        w2, w4 = four_switch_windows(float(a))
        score = profile_two_band(abs(H2 * w2) ** 2, abs(H4 * w4) ** 2)
        if best is None or score > best[0]:
            best = (score, float(a), w2, w4)
    return best


FOUR_SWITCH_SEFF, FOUR_SWITCH_A, W2_4, W4_4 = optimize_four_switch()


def d1_phase_scale(mass_product: float, interrogation_s: float) -> float:
    """Common phase amplitude multiplying the dimensionless harmonic response."""
    return 2.0 * ALPHA * G * mass_product * interrogation_s / (HBAR * L0)


def d1_fisher_per_accepted_event(mass_product: float, interrogation_s: float,
                                 contrast: float) -> float:
    amp = d1_phase_scale(mass_product, interrogation_s)
    return contrast**2 * amp**2 * FOUR_SWITCH_SEFF


def d1_fisher_rate(mass_product: float, interrogation_s: float, contrast: float,
                   dead_time_s: float = 0.0, acceptance: float = 1.0) -> float:
    cycle = interrogation_s + dead_time_s
    return acceptance * d1_fisher_per_accepted_event(
        mass_product, interrogation_s, contrast
    ) / cycle


def d1_mass_product_for_aggregate_phase_noise(z: float, sigma_phase: float,
                                              interrogation_s: float) -> float:
    """Strong-calibration mass-product benchmark for aggregate phase noise."""
    return (z * sigma_phase * HBAR * L0 /
            (2.0 * ALPHA * G * interrogation_s * math.sqrt(FOUR_SWITCH_SEFF)))


def accepted_events_for_phase_noise(sigma_phase: float, contrast: float) -> float:
    """Binary-fringe quadrature approximation: Var(phi) >= 1/(N C^2)."""
    return 1.0 / (contrast**2 * sigma_phase**2)


def d1_optimal_interrogation_for_exp_contrast(t2_s: float, dead_time_s: float) -> float:
    """Maximizes exp(-2T/T2) T^2/(T+dead) for C(T)=C0 exp(-T/T2)."""
    d = dead_time_s
    return (t2_s - 2.0*d + math.sqrt((t2_s - 2.0*d)**2 + 16.0*d*t2_s)) / 4.0


def d2_force_scale(mass_product: float) -> float:
    return 2.0 * ALPHA * G * mass_product / L0**2


def d2_fisher_rate(mass_product: float, force_asd_2: float, force_asd_4: float,
                   duty_cycle: float = 1.0) -> float:
    """Continuous two-band profiled Fisher rate [1/s].

    Uses r_n=|Delta F_n|^2/S_F,n with one-sided equivalent-force PSD
    S_F,n=(ASD_n)^2, then the same two-band spectral-tilt profiling law.
    """
    amp = d2_force_scale(mass_product)
    r2 = abs(amp * G2)**2 / force_asd_2**2
    r4 = abs(amp * G4)**2 / force_asd_4**2
    return duty_cycle * profile_two_band(r2, r4)


def wall_time_for_target_fisher(target_fisher: float, rate: float) -> float:
    return math.inf if rate <= 0.0 else target_fisher / rate


def main():
    print("Iteration-011 Toy009 four-switch optimum")
    print("a:", FOUR_SWITCH_A)
    print("|W2|, |W4|:", W2_4, W4_4)
    print("dimensionless profiled S_eff:", FOUR_SWITCH_SEFF)

    # Re-express the historical 1-mrad aggregate phase benchmark.
    mp_1mrad = d1_mass_product_for_aggregate_phase_noise(5.0, 1e-3, 1.0)
    print("\nD1 aggregate sigma_phi=1 mrad, T=1 s, 5 sigma mass product:", mp_1mrad)
    for c in (0.10, 0.66, 1.0):
        n = accepted_events_for_phase_noise(1e-3, c)
        wall = n * (1.0 + 1e-3) / 0.5
        print("contrast", c, "accepted events for 1 mrad:", n,
              "wall days at T=1 s, dead=1 ms, acceptance=0.5:", wall/86400.0)

    # At fixed mass product the coherent interrogation time is a true resource.
    print("\nD1 detector-only rate at the current ~1-mrad mass-product scale")
    for t in (0.01, 0.1, 1.0):
        r = d1_fisher_rate(mp_1mrad, t, 0.66, dead_time_s=1e-3, acceptance=0.5)
        print("T=", t, "s: F/s=", r, "5-sigma wall h=", wall_time_for_target_fisher(25.0, r)/3600.0)

    print("\nD1 exponential-contrast optimum with 1-ms dead time")
    for t2 in (0.01, 0.1, 1.0):
        print("T2=", t2, "s -> T_opt=", d1_optimal_interrogation_for_exp_contrast(t2, 1e-3), "s")

    print("\nD2 detector-only mass product for 5 sigma in declared wall times")
    # Solve via rate proportionality to mass_product^2.
    for asd in (1e-18, 1e-21, 1e-23):
        k = d2_fisher_rate(1.0, asd, asd, duty_cycle=0.5)
        for wall in (3600.0, 86400.0, 30.0*86400.0):
            mp = math.sqrt(25.0/(k*wall))
            print("ASD=", asd, "N/sqrtHz; wall=", wall/3600.0,
                  "h -> mass product=", mp, "kg^2")

    # Regression checks for the stored rounded harmonics.
    assert abs(FOUR_SWITCH_A - 0.90716) < 2e-4
    assert abs(W2_4 - 0.50150) < 2e-4
    assert abs(W4_4 - 0.30892) < 2e-4
    assert abs(FOUR_SWITCH_SEFF - 4.54477e-5) < 2e-9
    assert abs(mp_1mrad - 5.85942e-29) < 2e-34
    assert abs(accepted_events_for_phase_noise(1e-3, 0.66) - 2.295684e6) < 2.0
    assert abs(d1_optimal_interrogation_for_exp_contrast(1.0, 1e-3) - 0.5009960) < 1e-7


if __name__ == "__main__":
    main()
