"""RQIR D1 finite-bandwidth control-window budget.

Uses the accepted two-harmonic potential response and the simple bounded
lock-in g(tau)=sign(cos(2 tau)+lambda cos(4 tau)).  Models finite control
bandwidth by convolving the ideal switching function with a normalized
boxcar of fractional period width f.  In Fourier space this multiplies
harmonic n by sinc(n f) (numpy normalized sinc convention).

Also reports a simple multiplicative per-switch contrast budget for the
8-switch sequence.  This is a control-resource model, not a hardware model.
"""
from __future__ import annotations

import numpy as np

H2 = complex(-2.718331363764142e-4, -7.661385084133181e-3)
H4 = complex(1.2094280337234182e-3, -9.061081550557511e-3)
LAMBDA = 1.0460404040404039
N_SWITCH = 8


def seff(w2: float, w4: float) -> float:
    p2 = abs(H2 * w2) ** 2
    p4 = abs(H4 * w4) ** 2
    return 4.0 * p2 * p4 / (p2 + p4)


def ideal_window(n_grid=200000):
    tau = np.linspace(0.0, 2.0 * np.pi, n_grid, endpoint=False)
    g = np.sign(np.cos(2 * tau) + LAMBDA * np.cos(4 * tau))
    w2 = abs(np.mean(g * np.exp(2j * tau)))
    w4 = abs(np.mean(g * np.exp(4j * tau)))
    switches = int(np.sum(g != np.roll(g, 1)))
    return w2, w4, switches


def finite_bandwidth_ratio(f: float, w2: float, w4: float) -> float:
    # Boxcar convolution width = f * source period.
    # Fourier amplitude factor: sin(pi*n*f)/(pi*n*f) = np.sinc(n*f).
    q2 = abs(np.sinc(2.0 * f))
    q4 = abs(np.sinc(4.0 * f))
    return seff(w2 * q2, w4 * q4) / seff(w2, w4)


def per_switch_contrast_for_fisher(target_fisher_fraction: float) -> float:
    # If each switch multiplies signal amplitude by c, total amplitude is c^N,
    # and Fisher information is c^(2N).
    return target_fisher_fraction ** (1.0 / (2.0 * N_SWITCH))


def main():
    w2, w4, switches = ideal_window()
    print("lambda:", LAMBDA)
    print("switches per period:", switches)
    print("ideal bounded |W2|,|W4|:", w2, w4)

    for f in [0.01, 0.025, 0.05, 0.075, 0.10, 0.125, 0.15, 0.20]:
        r = finite_bandwidth_ratio(f, w2, w4)
        print(f"bandwidth smoothing fraction={f:.3f}: Fisher={r:.6f}, SNR={np.sqrt(r):.6f}")

    fs = np.linspace(0.0, 0.24, 2401)
    ratios = np.array([finite_bandwidth_ratio(float(f), w2, w4) for f in fs])
    f50 = float(fs[np.argmin(np.abs(ratios - 0.5))])
    print("approx smoothing fraction for 50% Fisher:", f50)

    for target in [0.5, 0.8, 0.9]:
        c = per_switch_contrast_for_fisher(target)
        print(f"per-switch amplitude factor for {target:.0%} total Fisher: {c:.9f}")

    assert switches == 8
    assert abs(w2 - 0.44022) < 5e-4
    assert abs(w4 - 0.38514) < 5e-4
    assert abs(finite_bandwidth_ratio(0.05, w2, w4) - 0.92097) < 5e-4
    assert abs(finite_bandwidth_ratio(0.10, w2, w4) - 0.69857) < 5e-4
    assert abs(f50 - 0.1325) < 5e-4
    assert abs(per_switch_contrast_for_fisher(0.8) - 0.98615033) < 1e-8


if __name__ == "__main__":
    main()
