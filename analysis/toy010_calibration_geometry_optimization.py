"""RQIR Toy 010 — calibration geometry co-optimization on fixed Toy 009 source.

This verifier keeps the Toy 009 source Hamiltonian/operator fixed and changes only
finite NP3 calibration geometry:
  * second Newtonian probe position y1;
  * five non-target calibration times.

It demonstrates that calibration geometry rotates the one-dimensional exact null
direction and can improve detector-level two-band Fisher proxies while retaining:
  rank(A)=24/25, state positivity, target mean/noise equality, and nonzero response.

Default mode verifies the accepted design.  Use --search to reproduce the local
random search that found the recorded neighborhood improvement.

This is a finite-dimensional design result, not a global optimum or an
experimental-readiness claim.
"""
from __future__ import annotations

import argparse
import numpy as np

from toy009_detector_aware_source_search import (
    D, ENERGIES, H, EPS, BASE_SEFF_D1, BASE_SEFF_D2,
    herm_vec, mat_from_herm_vec, evolve, sym, comm,
    physical_embedding, harmonic, seff,
)

T_RESPONSE = 3.583928899215236
BASE_Y1 = -3.5955271928522547
BASE_TIMES = np.array([
    0.0,
    3.0709312960670494,
    T_RESPONSE,
    3.73521464966555,
    4.18983,
    4.897032874946426,
    5.657269795944965,
])

# Accepted Toy 010 calibration geometry.
OPT_Y1 = -3.764531439702698
OPT_TIMES = np.array([
    0.0,
    2.99076642,
    T_RESPONSE,
    2.86845279,
    4.17773776,
    4.88882082,
    4.99774842,
])

# Recorded Toy 009 baseline under the inherited Toy 007 calibration.
TOY009_ETA = 0.5688230045520637
TOY009_SMIN = 0.0015122241664651476
TOY009_COND = 3033.407565001479
TOY009_D1 = BASE_SEFF_D1 * 1.2218350306685613
TOY009_D2 = BASE_SEFF_D2 * 1.4035829922637015


def reconstruct_toy009_braw() -> np.ndarray:
    """Reconstruct the accepted Toy 009 raw operator: seed 314159, trial 811."""
    rng = np.random.default_rng(314159)
    out = None
    for trial in range(812):
        x = rng.normal(size=(D, D))
        out = (x + x.T) / 2.0
    assert out is not None
    return out


BRAW = reconstruct_toy009_braw()
B0, GRAD0, RADII, V, VALS, SCALE = physical_embedding(BRAW)
SITE_POSITIONS = SCALE / VALS


def probe(y: float) -> np.ndarray:
    weights = 1.0 / np.abs(SITE_POSITIONS - y)
    return (V @ np.diag(weights) @ V.T).astype(complex)


def calibration_metrics(y1: float, times: np.ndarray) -> dict:
    probes = [probe(0.0), probe(float(y1))]
    rows = [herm_vec(np.eye(D)), herm_vec(H)]

    for k in (0, 1):
        for t in times:
            rows.append(herm_vec(evolve(probes[k], float(t))))

    rows.append(
        herm_vec(sym(evolve(probes[0], T_RESPONSE), probes[0]))
    )

    extra = [
        (0, 1, times[1]),
        (1, 1, times[5]),
        (1, 0, T_RESPONSE),
        (0, 1, T_RESPONSE),
        (1, 0, times[3]),
        (0, 0, times[6]),
        (0, 1, times[6]),
    ]
    for k, l, t in extra:
        rows.append(
            herm_vec(sym(evolve(probes[k], float(t)), probes[l]))
        )

    a = np.vstack(rows)
    _, singular, vh = np.linalg.svd(a, full_matrices=True)
    rank = int(np.sum(singular > 1e-10))
    if rank != 24:
        raise RuntimeError(f"Expected rank 24, found {rank}")

    nv = vh[-1]
    d0 = mat_from_herm_vec(nv)
    d0 /= np.max(np.abs(np.linalg.eigvalsh(d0)))
    rho_plus = np.eye(D) / D + EPS * d0
    rho_minus = np.eye(D) / D - EPS * d0
    delta = rho_plus - rho_minus

    h2 = harmonic(delta, probes[0], probes[0], 2)
    h4 = harmonic(delta, probes[0], probes[0], 4)
    g2 = harmonic(delta, GRAD0, probes[0], 2)
    g4 = harmonic(delta, GRAD0, probes[0], 4)

    c_response = herm_vec(
        comm(evolve(probes[0], T_RESPONSE), probes[0])
    )
    eta = abs(c_response @ nv) / np.linalg.norm(c_response)

    a_norm = a / np.linalg.norm(a, axis=1, keepdims=True)
    sn = np.linalg.svd(a_norm, compute_uv=False)
    nz = sn[sn > 1e-10]
    smin = float(nz[-1])
    condition = float(nz[0] / nz[-1])

    bt = evolve(probes[0], T_RESPONSE)

    def mean(rho, op):
        return np.trace(rho @ op)

    def centered_noise(rho, x, y):
        dx = x - mean(rho, x) * np.eye(D)
        dy = y - mean(rho, y) * np.eye(D)
        return float(np.real(np.trace(rho @ sym(dx, dy))))

    def comm_kernel(rho, x, y):
        return float(np.real(np.trace(rho @ comm(x, y))))

    return {
        "rank": rank,
        "null_vec": nv,
        "delta0": d0,
        "eig_plus": np.linalg.eigvalsh(rho_plus),
        "eig_minus": np.linalg.eigvalsh(rho_minus),
        "residual": float(np.max(np.abs(a @ herm_vec(d0)))),
        "seff_d1": seff(h2, h4),
        "seff_d2": seff(g2, g4),
        "h2": h2, "h4": h4, "g2": g2, "g4": g4,
        "eta": eta, "smin": smin, "condition": condition,
        "mean_plus": float(np.real(mean(rho_plus, bt))),
        "mean_minus": float(np.real(mean(rho_minus, bt))),
        "noise_plus": centered_noise(rho_plus, bt, probes[0]),
        "noise_minus": centered_noise(rho_minus, bt, probes[0]),
        "response_plus": comm_kernel(rho_plus, bt, probes[0]),
        "response_minus": comm_kernel(rho_minus, bt, probes[0]),
    }


def four_switch_best(h2: complex, h4: complex) -> dict:
    # pi-periodic 4-switch family. One positive interval length a per half-period.
    grid = np.linspace(1e-6, np.pi - 1e-6, 300000)
    w2 = 2.0 * np.abs(np.sin(grid)) / np.pi
    w4 = np.abs(np.sin(2.0 * grid)) / np.pi
    p2 = np.abs(h2 * w2) ** 2
    p4 = np.abs(h4 * w4) ** 2
    f = 4.0 * p2 * p4 / (p2 + p4)
    i = int(np.argmax(f))
    return {
        "a": float(grid[i]),
        "w2": float(w2[i]),
        "w4": float(w4[i]),
        "fisher": float(f[i]),
    }


def run_search() -> tuple:
    """Reproduce the recorded local search around the inherited Toy 009 geometry."""
    base = calibration_metrics(BASE_Y1, BASE_TIMES)
    rng = np.random.default_rng(2026082903)
    best = None

    # Stage 1: broad local perturbation.
    for _ in range(50000):
        y = BASE_Y1 * np.exp(rng.normal(0.0, 0.35))
        times = BASE_TIMES.copy()
        for idx in (1, 3, 4, 5, 6):
            times[idx] = (times[idx] + rng.normal(0.0, 0.35)) % (2.0 * np.pi)
        if np.min(np.diff(np.sort(times))) < 0.02:
            continue
        m = calibration_metrics(y, times)
        ratios = np.array([
            m["seff_d1"] / base["seff_d1"],
            m["seff_d2"] / base["seff_d2"],
            m["eta"] / base["eta"],
            m["smin"] / base["smin"],
        ])
        if np.all(ratios >= 1.0):
            score = float(np.exp(np.mean(np.log(ratios))))
            if best is None or score > best[0]:
                best = (score, y, times.copy(), ratios, m)

    if best is None:
        raise RuntimeError("Broad local search found no non-degraded candidate")

    # Stage 2: deterministic short refinement.
    rng = np.random.default_rng(2026082904)
    for sd in (0.12, 0.05):
        center = best
        for _ in range(2500):
            y = center[1] * np.exp(rng.normal(0.0, sd * 0.5))
            times = center[2].copy()
            for idx in (1, 3, 4, 5, 6):
                times[idx] = (times[idx] + rng.normal(0.0, sd)) % (2.0 * np.pi)
            if np.min(np.diff(np.sort(times))) < 0.02:
                continue
            m = calibration_metrics(y, times)
            ratios = np.array([
                m["seff_d1"] / base["seff_d1"],
                m["seff_d2"] / base["seff_d2"],
                m["eta"] / base["eta"],
                m["smin"] / base["smin"],
            ])
            if np.all(ratios >= 1.0):
                score = float(np.exp(np.mean(np.log(ratios))))
                if score > best[0]:
                    best = (score, y, times.copy(), ratios, m)
    return best


def main(search: bool = False):
    base = calibration_metrics(BASE_Y1, BASE_TIMES)
    opt = calibration_metrics(OPT_Y1, OPT_TIMES)

    overlap = abs(base["null_vec"] @ opt["null_vec"])
    angle_deg = float(np.degrees(np.arccos(np.clip(overlap, -1.0, 1.0))))
    four = four_switch_best(opt["h2"], opt["h4"])

    print("Toy 009 source radii:", RADII)
    print("Toy 010 y1:", OPT_Y1)
    print("Toy 010 times:", OPT_TIMES)
    print("rank:", opt["rank"])
    print("D1 gain vs Toy009:", opt["seff_d1"] / base["seff_d1"])
    print("D2 gain vs Toy009:", opt["seff_d2"] / base["seff_d2"])
    print("D1 gain vs Toy007:", opt["seff_d1"] / BASE_SEFF_D1)
    print("D2 gain vs Toy007:", opt["seff_d2"] / BASE_SEFF_D2)
    print("eta:", opt["eta"], "smin:", opt["smin"], "cond:", opt["condition"])
    print("null-vector rotation deg:", angle_deg)
    print("H2,H4:", opt["h2"], opt["h4"])
    print("G2,G4:", opt["g2"], opt["g4"])
    print("eigenvalues rho+:", opt["eig_plus"])
    print("eigenvalues rho-:", opt["eig_minus"])
    print("max equality residual:", opt["residual"])
    print("mean +/-:", opt["mean_plus"], opt["mean_minus"])
    print("noise +/-:", opt["noise_plus"], opt["noise_minus"])
    print("response +/-:", opt["response_plus"], opt["response_minus"])
    print("best 4-switch:", four)

    assert opt["rank"] == 24
    assert opt["residual"] < 1e-12
    assert min(opt["eig_plus"].min(), opt["eig_minus"].min()) > 0.0
    assert abs(opt["mean_plus"] - opt["mean_minus"]) < 1e-12
    assert abs(opt["noise_plus"] - opt["noise_minus"]) < 1e-12
    assert opt["seff_d1"] > base["seff_d1"]
    assert opt["seff_d2"] > base["seff_d2"]
    assert opt["eta"] > base["eta"]
    assert opt["smin"] > base["smin"]
    assert abs(opt["eta"] - 0.60017429) < 2e-7
    assert abs(opt["smin"] - 0.002211009) < 2e-9
    assert abs(opt["seff_d1"] - 2.8310544e-4) < 2e-10
    assert abs(opt["seff_d2"] - 5.4370610e-4) < 2e-10

    if search:
        best = run_search()
        print("search best score:", best[0])
        print("search y1:", best[1])
        print("search times:", best[2])
        print("search ratios D1,D2,eta,smin:", best[3])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--search", action="store_true")
    args = parser.parse_args()
    main(search=args.search)
