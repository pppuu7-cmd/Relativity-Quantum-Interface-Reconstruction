"""RQIR D1 low-switch verifier for Toy 009.

Compares the accepted Toy 007 eight-switch bounded lock-in with two lower-switch
Toy 009 sensitivity functions.  The purpose is to test whether the detector-
aware source redesign can reduce control burden without sacrificing the
profiled two-band Fisher information.

The four-switch sequence is analytic and pi-periodic.  The six-switch durations
were obtained by a deterministic exploratory optimization and are verified
here directly.  No hardware implementation is assumed.
"""
from __future__ import annotations

import numpy as np

# Toy 007 potential response.
H2_007 = complex(-2.718331363764142e-4, -7.661385084133181e-3)
H4_007 = complex(1.2094280337234182e-3, -9.061081550557511e-3)
LAMBDA_007 = 1.0460404040404039

# Toy 009 accepted NP3 candidate (search seed 314159, trial 811).
H2_009 = complex(-0.0016758666233300326, 0.007924911102414358)
H4_009 = complex(0.004341884378570778, 0.009954205685359138)

# Four-switch pi-periodic optimum: + for duration a, - for pi-a, repeated.
A4 = 0.912594123325455

# Six alternating-sign interval durations over one 2*pi period.
DUR6 = np.array([
    0.26889934,
    0.92358018,
    1.02554630,
    2.11604722,
    1.02553678,
    0.92357548,
])
DUR6 *= (2.0 * np.pi) / DUR6.sum()


def seff(h2: complex, h4: complex, w2: float, w4: float) -> float:
    p2 = abs(h2 * w2) ** 2
    p4 = abs(h4 * w4) ** 2
    return 4.0 * p2 * p4 / (p2 + p4)


def numeric_window(g: np.ndarray, tau: np.ndarray, n: int) -> float:
    return float(abs(np.mean(g * np.exp(1j * n * tau))))


def toy007_window(n_grid: int = 400000):
    tau = np.linspace(0.0, 2.0 * np.pi, n_grid, endpoint=False)
    g = np.sign(np.cos(2 * tau) + LAMBDA_007 * np.cos(4 * tau))
    return numeric_window(g, tau, 2), numeric_window(g, tau, 4)


def four_switch_window():
    # For even n, |W_n| = 4 |sin(n a / 2)| / (n pi).
    w2 = 2.0 * abs(np.sin(A4)) / np.pi
    w4 = abs(np.sin(2.0 * A4)) / np.pi
    return float(w2), float(w4)


def alternating_window(durations: np.ndarray, n: int) -> float:
    edges = np.concatenate([[0.0], np.cumsum(durations)])
    total = 0j
    for j in range(len(durations)):
        sign = 1.0 if j % 2 == 0 else -1.0
        a, b = edges[j], edges[j + 1]
        total += sign * (np.exp(1j * n * b) - np.exp(1j * n * a)) / (1j * n)
    return float(abs(total / (2.0 * np.pi)))


def main():
    w2_old, w4_old = toy007_window()
    f_old = seff(H2_007, H4_007, w2_old, w4_old)

    w2_4, w4_4 = four_switch_window()
    f4 = seff(H2_009, H4_009, w2_4, w4_4)

    w2_6 = alternating_window(DUR6, 2)
    w4_6 = alternating_window(DUR6, 4)
    f6 = seff(H2_009, H4_009, w2_6, w4_6)

    print("Toy007 8-switch |W2|,|W4|:", w2_old, w4_old)
    print("Toy009 4-switch |W2|,|W4|:", w2_4, w4_4)
    print("Toy009 6-switch |W2|,|W4|:", w2_6, w4_6)
    print("Fisher ratio Toy009 4-switch / Toy007 8-switch:", f4 / f_old)
    print("Fisher ratio Toy009 6-switch / Toy007 8-switch:", f6 / f_old)
    print("SNR ratio 4-switch:", np.sqrt(f4 / f_old))
    print("SNR ratio 6-switch:", np.sqrt(f6 / f_old))

    # Rescale the previous revised D1 five-sigma mass-product illustration.
    old_mass_product = 8.1e-29
    mp4 = old_mass_product / np.sqrt(f4 / f_old)
    mp6 = old_mass_product / np.sqrt(f6 / f_old)
    print("illustrative mass-product 4-switch [kg^2]:", mp4)
    print("illustrative mass-product 6-switch [kg^2]:", mp6)
    print("equal-mass illustration 4-switch [kg]:", np.sqrt(mp4))
    print("equal-mass illustration 6-switch [kg]:", np.sqrt(mp6))

    # Same per-switch contrast factor c<=1 always favors the lower-switch
    # Toy009 designs even more strongly than these c=1 ratios.
    for c in [1.0, 0.995, 0.99, 0.98]:
        r4 = (f4 * c ** 8) / (f_old * c ** 16)
        r6 = (f6 * c ** 12) / (f_old * c ** 16)
        print(f"c={c:.3f}: effective Fisher ratios 4/old8={r4:.6f}, 6/old8={r6:.6f}")

    assert abs(w2_old - 0.44019) < 5e-4
    assert abs(w4_old - 0.38516) < 5e-4
    assert abs(w2_4 - 0.5036256) < 1e-6
    assert abs(w4_4 - 0.3080656) < 1e-6
    assert abs(w2_6 - 0.4597413) < 2e-5
    assert abs(w4_6 - 0.3638237) < 2e-5
    assert abs(f4 / f_old - 1.1274608) < 2e-5
    assert abs(f6 / f_old - 1.2373142) < 2e-5


if __name__ == "__main__":
    main()
