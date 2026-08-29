"""RQIR detector branch comparison: D1 matter-wave phase vs D2 mechanical force.

Reconstructs the accepted Toy 007 source/state pair and computes:
- D1 potential-response harmonics H2,H4;
- D1 finite interrogation-window suppression and a simple bounded bang-bang
  dual-harmonic lock-in sequence;
- D2 force-gradient cross-response harmonics G2,G4;
- two-band profiled-shape retention for both branches;
- simple physical 5-sigma scaling benchmarks.

This is a detector-design comparison, not an experimental-readiness claim.
"""
from __future__ import annotations

import numpy as np

from toy007_finite_multiprobe_design import (
    comm_kernel,
    evolve_diagonal_h,
    herm_vec,
    mat_from_herm_vec,
    reconstruct_toy005_source,
    sym_op,
)

G_NEWTON = 6.67430e-11


def reconstruct_pair():
    d = 5
    _, h, b, _ = reconstruct_toy005_source(seed=105)
    vals, v = np.linalg.eigh(b.real)
    L = float(vals.max())
    x_sites = L / vals

    def probe(y: float):
        return (v @ np.diag(1.0 / np.abs(x_sites - y)) @ v.T).astype(complex)

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
    probes = [probe(y0), probe(y1)]

    rows = [herm_vec(np.eye(d)), herm_vec(h)]
    for k in (0, 1):
        for t in times:
            rows.append(herm_vec(evolve_diagonal_h(h, probes[k], float(t))))
    rows.append(herm_vec(sym_op(evolve_diagonal_h(h, probes[0], t_response), probes[0])))
    extra = [
        (0, 1, times[1]), (1, 1, times[5]), (1, 0, t_response),
        (0, 1, t_response), (1, 0, times[3]), (0, 0, times[6]),
        (0, 1, times[6]),
    ]
    for k, l, t in extra:
        rows.append(herm_vec(sym_op(evolve_diagonal_h(h, probes[k], float(t)), probes[l])))

    a = np.vstack(rows)
    _, s, vh = np.linalg.svd(a, full_matrices=True)
    assert int(np.sum(s > 1e-10)) == 24
    delta = mat_from_herm_vec(vh[-1], d)
    delta /= np.max(np.abs(np.linalg.eigvalsh(delta)))
    rho_plus = np.eye(d) / d + 0.08 * delta
    rho_minus = np.eye(d) / d - 0.08 * delta

    # d/dy of 1/|x-y|.  Here y0=0 and all x_sites>0.
    diff = x_sites - y0
    grad_weights = diff / np.abs(diff) ** 3
    grad0 = (v @ np.diag(grad_weights) @ v.T).astype(complex)
    return h, probes[0], grad0, rho_plus, rho_minus


def delta_comm_wave(h, readout, drive, rp, rm, tau):
    out = []
    for t in tau:
        rt = evolve_diagonal_h(h, readout, float(t))
        out.append(comm_kernel(rp, rt, drive) - comm_kernel(rm, rt, drive))
    return np.asarray(out)


def harmonics(wave, tau):
    out = {}
    for n in range(1, 6):
        a = float(2.0 * np.mean(wave * np.cos(n * tau)))
        b = float(2.0 * np.mean(wave * np.sin(n * tau)))
        # Repository convention H_n = a_n + i b_n.
        out[n] = complex(a, b)
    return out


def two_band_metrics(h2, h4):
    p2, p4 = abs(h2) ** 2, abs(h4) ** 2
    total = p2 + p4
    kappa = (p4 - p2) / total
    retention = 1.0 - kappa ** 2
    s_eff = 4.0 * p2 * p4 / total
    return total ** 0.5, kappa, retention, s_eff


def d1_window_scan(h2, h4):
    # One complete dimensionless source period.
    tau = np.linspace(0.0, 2.0 * np.pi, 200000, endpoint=False)
    # Passive uniform phase integration: all nonzero integer harmonics cancel.
    w2_rect = abs(np.mean(np.exp(2j * tau)))
    w4_rect = abs(np.mean(np.exp(4j * tau)))

    # Simple bounded dual-band lock-in: g(tau)=sign(cos2tau + lambda cos4tau).
    best = None
    e2 = np.exp(2j * tau)
    e4 = np.exp(4j * tau)
    for lam in np.linspace(1.001, 1.099, 199):
        g = np.sign(np.cos(2 * tau) + lam * np.cos(4 * tau))
        w2 = abs(np.mean(g * e2))
        w4 = abs(np.mean(g * e4))
        p2 = abs(h2 * w2) ** 2
        p4 = abs(h4 * w4) ** 2
        s_eff = 4.0 * p2 * p4 / (p2 + p4)
        if best is None or s_eff > best[0]:
            best = (s_eff, lam, w2, w4)
    return w2_rect, w4_rect, best


def main():
    h, b0, grad0, rp, rm = reconstruct_pair()
    tau = np.linspace(0.0, 2.0 * np.pi, 20001, endpoint=False)
    hb = harmonics(delta_comm_wave(h, b0, b0, rp, rm, tau), tau)
    hg = harmonics(delta_comm_wave(h, grad0, b0, rp, rm, tau), tau)

    bnorm, bkappa, bret, bseff = two_band_metrics(hb[2], hb[4])
    gnorm, gkappa, gret, gseff = two_band_metrics(hg[2], hg[4])
    w2rect, w4rect, best = d1_window_scan(hb[2], hb[4])
    mod_seff, lam, w2, w4 = best
    snr_window_retention = np.sqrt(mod_seff / bseff)

    # Physical benchmarks, same alpha,L,T,5sigma assumptions used in Protocol 002B.
    alpha = 0.1
    L0 = 10e-6
    T = 1.0
    z = 5.0

    # Revised D1 from Protocol 002B ideal mprod=3.36e-29 kg^2.
    d1_ideal_mprod = 3.36e-29
    d1_mod_mprod = d1_ideal_mprod / snr_window_retention

    # D2 force-readout benchmark using equal equivalent-force ASD in both bands.
    force_asd = 1e-21  # optimistic design point, not claimed achieved ASD
    d2_mprod = (
        z * force_asd * L0 ** 2 /
        (2 * alpha * G_NEWTON * gnorm * np.sqrt(T) * np.sqrt(gret))
    )

    print("D1 H2,H4:", hb[2], hb[4])
    print("D1 H24,kappa,shape retention:", bnorm, bkappa, bret)
    print("D2 gradient G2,G4:", hg[2], hg[4])
    print("D2 G24,kappa,shape retention:", gnorm, gkappa, gret)
    print("D2/D1 dimensionless two-band norm:", gnorm / bnorm)
    print("uniform full-period |W2|,|W4|:", w2rect, w4rect)
    print("best bang-bang lambda,|W2|,|W4|:", lam, w2, w4)
    print("D1 two-band information retention vs ideal:", mod_seff / bseff)
    print("D1 SNR retention vs ideal:", snr_window_retention)
    print("revised D1 5sigma m_s*m_p [kg^2]:", d1_mod_mprod)
    print("revised D1 equal mass [kg]:", np.sqrt(d1_mod_mprod))
    print("D2 5sigma m_s*m_p at 1 zN/sqrtHz [kg^2]:", d2_mprod)
    print("D2 equal mass illustration [kg]:", np.sqrt(d2_mprod))
    print("D2/D1 required mass-product ratio:", d2_mprod / d1_mod_mprod)

    assert abs(bnorm - 0.0119304916) < 1e-9
    assert abs(bkappa - 0.17420112) < 1e-7
    assert abs(gnorm - 0.0156730970) < 1e-9
    assert abs(gkappa - (-0.06700759)) < 1e-7
    assert w2rect < 1e-12 and w4rect < 1e-12
    assert abs(lam - 1.04604) < 2e-3
    assert abs(snr_window_retention - 0.41475) < 5e-4
    assert abs(d2_mprod - 2.39528e-18) < 1e-23


if __name__ == "__main__":
    main()
