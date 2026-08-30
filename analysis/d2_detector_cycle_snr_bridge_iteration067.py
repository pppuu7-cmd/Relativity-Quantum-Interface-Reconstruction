"""RQIR Iteration 067: bridge physical two-band D2 S_eff to cycle-level SNR/repetition count.

This script deliberately does NOT infer wall-clock seconds from a demodulated phase-noise
number alone.  It exposes the missing acquisition model (cycle duration, estimator bandwidth,
acceptance/dead time and inter-cycle covariance) as a separate gate.
"""
from math import ceil

S_EFF_013 = 2.4438110707e-5
RATIO_013_009 = 0.04228407350
S_EFF_009 = S_EFF_013 / RATIO_013_009


def fisher_per_independent_cycle(q: float, s_eff: float) -> float:
    """Whitened D2 beta Fisher per statistically independent cycle.

    q is the detector leverage 2*|alpha|*Gamma_G/sigma_phi for one declared cycle,
    after putting the two harmonic quadratures in the same whitened coordinate used
    to define S_eff.  If q is instead inferred from an already averaged demodulated
    estimate, the result is NOT a physical shot count.
    """
    return q*q*s_eff


def cycles_for_z(z: float, q: float, s_eff: float) -> float:
    return z*z / fisher_per_independent_cycle(q, s_eff)


def wallclock_lower_bound(z: float, q: float, s_eff: float, cycle_s: float,
                          acceptance: float = 1.0, dead_s: float = 0.0) -> float:
    """Independent-cycle white-noise lower bound only.

    Correlated drift, coherence loss, controls and nuisance re-profiling must be added
    separately.  acceptance is the retained-cycle probability.
    """
    n = cycles_for_z(z, q, s_eff)
    return n * (cycle_s + dead_s) / acceptance


if __name__ == "__main__":
    print(f"S_eff Toy009 = {S_EFF_009:.13e}")
    print(f"S_eff Toy013 = {S_EFF_013:.13e}")
    print(f"science exposure ratio 013/009 = {S_EFF_009/S_EFF_013:.10f}")
    print("\n5-sigma independent-cycle counts versus per-cycle whitened leverage q:")
    for q in (1, 3, 5, 10, 30, 100):
        n9 = cycles_for_z(5.0, q, S_EFF_009)
        n13 = cycles_for_z(5.0, q, S_EFF_013)
        print(f"q={q:>3}: Toy009={n9:12.6f}, Toy013={n13:12.6f}, ratio={n13/n9:.8f}")

    # Algebraic sanity checks.
    assert abs(S_EFF_009 - 5.779507196013175e-4) < 1e-16
    assert abs(cycles_for_z(5, 10, S_EFF_009) - 432.5628319529652) < 1e-9
    assert abs(cycles_for_z(5, 10, S_EFF_013) - 10229.923376539518) < 1e-8
    assert abs((S_EFF_009/S_EFF_013) - 23.6495663) < 5e-7
