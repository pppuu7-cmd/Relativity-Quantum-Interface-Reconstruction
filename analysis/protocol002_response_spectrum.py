"""RQIR Protocol 002 — Toy 007 response spectrum and matched-filter metrics.

Reconstructs the accepted Toy 007 NP3 state pair, evaluates
Delta D_00(t,0) over one 2*pi source period, extracts the exact finite Fourier
content allowed by the Toy 005 Hamiltonian gaps, and reports white-noise
matched-filter diagnostics.

Run from repository root:
    python analysis/protocol002_response_spectrum.py

No experimental sensitivity is assumed here.  The matched-filter comparison is
an operator/waveform calculation under ideal white, stationary readout noise.
"""

from __future__ import annotations

import numpy as np

from toy007_finite_multiprobe_design import (
    comm_kernel,
    comm_op,
    evolve_diagonal_h,
    herm_vec,
    mat_from_herm_vec,
    reconstruct_toy005_source,
    sym_op,
)


def reconstruct_toy007_pair():
    d = 5
    _, h, b, _ = reconstruct_toy005_source(seed=105)
    vals, v = np.linalg.eigh(b.real)
    L = float(vals.max())
    x_sites = L / vals

    def probe_operator(y: float) -> np.ndarray:
        weights = 1.0 / np.abs(x_sites - y)
        return v @ np.diag(weights) @ v.T

    y0 = 0.0
    y1 = -3.5955271928522547
    t_response = 3.583928899215236
    times = np.array([
        0.0,
        3.0709312960670494,
        t_response,
        3.73521464966555,
        4.18983,
        4.897032874946426,
        5.657269795944965,
    ])
    probes = [probe_operator(y0).astype(complex),
              probe_operator(y1).astype(complex)]

    rows = [herm_vec(np.eye(d)), herm_vec(h)]
    for k in (0, 1):
        for t in times:
            rows.append(herm_vec(evolve_diagonal_h(h, probes[k], float(t))))

    rows.append(
        herm_vec(sym_op(evolve_diagonal_h(h, probes[0], t_response), probes[0]))
    )

    extra = [
        (0, 1, times[1]),
        (1, 1, times[5]),
        (1, 0, t_response),
        (0, 1, t_response),
        (1, 0, times[3]),
        (0, 0, times[6]),
        (0, 1, times[6]),
    ]
    for k, l, t in extra:
        rows.append(
            herm_vec(sym_op(evolve_diagonal_h(h, probes[k], float(t)), probes[l]))
        )

    a = np.vstack(rows)
    _, singular, vh = np.linalg.svd(a, full_matrices=True)
    rank = int(np.sum(singular > 1e-10))
    assert rank == 24

    null_vec = vh[-1]
    delta0 = mat_from_herm_vec(null_vec, d)
    delta0 /= np.max(np.abs(np.linalg.eigvalsh(delta0)))

    eps = 0.08
    rho_plus = np.eye(d) / d + eps * delta0
    rho_minus = np.eye(d) / d - eps * delta0
    return h, probes[0], rho_plus, rho_minus


def main():
    h, b0, rho_plus, rho_minus = reconstruct_toy007_pair()

    n_grid = 20001
    tau = np.linspace(0.0, 2.0 * np.pi, n_grid, endpoint=False)

    def delta_d(t: float) -> float:
        bt = evolve_diagonal_h(h, b0, t)
        return (
            comm_kernel(rho_plus, bt, b0)
            - comm_kernel(rho_minus, bt, b0)
        )

    wave = np.array([delta_d(float(t)) for t in tau])

    # Energies {1,2,3,4,6} permit integer gaps 1..5, so the response over
    # one 2*pi period has only DC plus harmonics n=1,...,5.
    a0 = float(np.mean(wave))
    harmonics = []
    for n in range(1, 6):
        a_n = float(2.0 * np.mean(wave * np.cos(n * tau)))
        b_n = float(2.0 * np.mean(wave * np.sin(n * tau)))
        amp = float(np.hypot(a_n, b_n))
        harmonics.append((n, a_n, b_n, amp))

    reconstruction = np.full_like(wave, a0)
    for n, a_n, b_n, _ in harmonics:
        reconstruction += a_n * np.cos(n * tau) + b_n * np.sin(n * tau)

    max_reconstruction_error = float(np.max(np.abs(wave - reconstruction)))
    rms = float(np.sqrt(np.mean(wave**2)))
    l2_norm = float(np.sqrt(2.0 * np.pi) * rms)
    integral_sq = float(l2_norm**2)
    area = float(2.0 * np.pi * a0)
    peak_index = int(np.argmax(np.abs(wave)))
    peak_tau = float(tau[peak_index])
    peak_value = float(wave[peak_index])

    total_power = a0**2 + 0.5 * sum(h[3] ** 2 for h in harmonics)
    power_fractions = {"DC": a0**2 / total_power}
    for n, _, _, amp in harmonics:
        power_fractions[n] = 0.5 * amp**2 / total_power

    # For filters normalized by int_0^(2pi) g(tau)^2 d tau = 1:
    # matched g ~ DeltaD gives signal ||DeltaD||_2.
    # A uniform normalized filter gives |int DeltaD| / sqrt(2*pi).
    uniform_norm_signal = abs(area) / np.sqrt(2.0 * np.pi)
    white_noise_matched_gain = l2_norm / uniform_norm_signal

    print("Response period: 2*pi in dimensionless tau")
    print("DC coefficient a0:", a0)
    print("harmonics: n, cosine a_n, sine b_n, amplitude")
    for row in harmonics:
        print(" ", row)
    print("max Fourier reconstruction error:", max_reconstruction_error)
    print("peak |Delta D| at tau:", peak_tau)
    print("peak Delta D:", peak_value)
    print("RMS Delta D:", rms)
    print("L2 norm over one period:", l2_norm)
    print("integral DeltaD^2 d tau:", integral_sq)
    print("integral DeltaD d tau:", area)
    print("power fractions:", power_fractions)
    print("power fraction n=2+n=4:", power_fractions[2] + power_fractions[4])
    print("white-noise matched/uniform normalized-filter gain:",
          white_noise_matched_gain)

    # Regression values for the recorded Toy 007 design.
    assert max_reconstruction_error < 1e-12
    assert abs(peak_value - (-0.02144121)) < 1e-6
    assert abs(rms - 0.00892108135) < 1e-9
    assert abs(integral_sq - 0.00050005165) < 1e-10
    assert abs((power_fractions[2] + power_fractions[4]) - 0.89423504) < 1e-6
    assert abs(white_noise_matched_gain - 4.6308566) < 1e-6


if __name__ == "__main__":
    main()
