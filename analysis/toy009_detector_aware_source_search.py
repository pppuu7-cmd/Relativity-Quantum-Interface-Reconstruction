"""RQIR Toy 009 — detector-aware five-level source search.

Deterministic search over real-symmetric five-level source operators at fixed
energy spectrum (1,2,3,4,6).  Each candidate is converted into a Newtonian
five-site source with nearest source-detector distance normalized to one.

Two stages are reproduced:

1. NP2 detector-only scan (seed 20260829): maximize two-band D1/D2 source
   response under geometry constraints.  This finds a large-gain candidate,
   but it is *not* accepted as the new source because the old NP3 calibration
   nearly removes its response.

2. Fixed-protocol NP3 scan (seed 314159): apply the same finite two-probe/time
   calibration pattern as Toy 007 and search for candidates that improve D1,
   D2, response survival eta_R and normalized conditioning simultaneously.

This is an exploratory finite-dimensional design scan, not a global optimum or
an experimental-readiness calculation.
"""
from __future__ import annotations

import numpy as np

D = 5
ENERGIES = np.array([1., 2., 3., 4., 6.])
H = np.diag(ENERGIES).astype(complex)
EPS = 0.08

# Toy 007 reference values.
BASE_SEFF_D1 = 1.3801727800938793e-4
BASE_SEFF_D2 = 2.445430148774411e-4
BASE_ETA = 0.45768196
BASE_SMIN = 0.0014629182
BASE_COND = 3180.0

Y1 = -3.5955271928522547
T_RESPONSE = 3.583928899215236
TIMES = np.array([
    0.0,
    3.0709312960670494,
    T_RESPONSE,
    3.73521464966555,
    4.18983,
    4.897032874946426,
    5.657269795944965,
])
EXTRA = [
    (0, 1, TIMES[1]),
    (1, 1, TIMES[5]),
    (1, 0, T_RESPONSE),
    (0, 1, T_RESPONSE),
    (1, 0, TIMES[3]),
    (0, 0, TIMES[6]),
    (0, 1, TIMES[6]),
]


def herm_vec(a: np.ndarray) -> np.ndarray:
    out = [a[i, i].real for i in range(D)]
    for i in range(D):
        for j in range(i + 1, D):
            out.extend([
                np.sqrt(2.0) * a[i, j].real,
                np.sqrt(2.0) * a[i, j].imag,
            ])
    return np.asarray(out, dtype=float)


def mat_from_herm_vec(v: np.ndarray) -> np.ndarray:
    a = np.zeros((D, D), dtype=complex)
    k = 0
    for i in range(D):
        a[i, i] = v[k]
        k += 1
    for i in range(D):
        for j in range(i + 1, D):
            a[i, j] = (v[k] + 1j * v[k + 1]) / np.sqrt(2.0)
            a[j, i] = np.conj(a[i, j])
            k += 2
    return a


def evolve(op: np.ndarray, t: float) -> np.ndarray:
    return op * np.exp(1j * (ENERGIES[:, None] - ENERGIES[None, :]) * t)


def sym(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return (a @ b + b @ a) / 2.0


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return (a @ b - b @ a) / (2j)


def frequency_components(b: np.ndarray) -> dict[int, np.ndarray]:
    out: dict[int, np.ndarray] = {}
    for i in range(D):
        for j in range(D):
            w = int(round(float(ENERGIES[i] - ENERGIES[j])))
            out.setdefault(w, np.zeros((D, D), dtype=complex))[i, j] = b[i, j]
    return out


def time_components(xw: dict[int, np.ndarray]) -> list[np.ndarray]:
    ops: list[np.ndarray] = []
    if 0 in xw:
        ops.append((xw[0] + xw[0].conj().T) / 2.0)
    for w in sorted(k for k in xw if k > 0):
        xp = xw[w]
        xm = xw.get(-w, np.zeros_like(xp))
        c = xp + xm
        s = 1j * (xp - xm)
        ops.append((c + c.conj().T) / 2.0)
        ops.append((s + s.conj().T) / 2.0)
    return ops


def np2_null_direction(b: np.ndarray) -> tuple[int, np.ndarray, np.ndarray]:
    bw = frequency_components(b)
    mean_ops = time_components(bw)
    sw = {w: (x @ b + b @ x) / 2.0 for w, x in bw.items()}
    rows = [herm_vec(np.eye(D)), herm_vec(H)]
    rows += [herm_vec(x) for x in mean_ops]
    rows += [herm_vec(x) for x in time_components(sw)]
    a = np.vstack(rows)
    _, singular, vh = np.linalg.svd(a, full_matrices=True)
    rank = int(np.sum(singular > 1e-9))
    return rank, vh[rank:], a


def physical_embedding(braw: np.ndarray):
    ev = np.linalg.eigvalsh(braw)
    bpos = braw + (-ev.min() + 1.0) * np.eye(D)
    vals, v = np.linalg.eigh(bpos)
    scale = float(vals.max())
    radii = scale / vals
    b0 = (bpos / scale).astype(complex)
    grad0 = (v @ np.diag((vals / scale) ** 2) @ v.T).astype(complex)
    return b0, grad0, np.sort(radii), v, vals, scale


def harmonic(delta: np.ndarray, readout: np.ndarray, pump: np.ndarray, n: int) -> complex:
    rw = np.zeros_like(readout, dtype=complex)
    for i in range(D):
        for j in range(D):
            if int(round(ENERGIES[i] - ENERGIES[j])) == n:
                rw[i, j] = readout[i, j]
    z = np.trace(delta @ ((rw @ pump - pump @ rw) / (2j)))
    return 2.0 * z


def seff(h2: complex, h4: complex) -> float:
    p2 = abs(h2) ** 2
    p4 = abs(h4) ** 2
    return 4.0 * p2 * p4 / (p2 + p4)


def geometry_ok(radii: np.ndarray) -> bool:
    return bool(radii.max() <= 6.0 and np.min(np.diff(radii)) >= 0.1)


def np2_metrics(braw: np.ndarray):
    rank, null, a = np2_null_direction(braw)
    if rank != 24 or len(null) != 1:
        return None
    b0, grad0, radii, _, _, _ = physical_embedding(braw)
    if not geometry_ok(radii):
        return None
    d0 = mat_from_herm_vec(null[0])
    d0 /= np.max(np.abs(np.linalg.eigvalsh(d0)))
    delta = 2.0 * EPS * d0
    h2 = harmonic(delta, b0, b0, 2)
    h4 = harmonic(delta, b0, b0, 4)
    g2 = harmonic(delta, grad0, b0, 2)
    g4 = harmonic(delta, grad0, b0, 4)
    return {
        "seff_d1": seff(h2, h4),
        "seff_d2": seff(g2, g4),
        "h2": h2, "h4": h4, "g2": g2, "g4": g4,
        "radii": radii,
        "delta0": d0,
        "constraint_residual": float(np.max(np.abs(a @ herm_vec(d0)))),
    }


def np3_metrics(braw: np.ndarray):
    b0, grad0, radii, v, vals, scale = physical_embedding(braw)
    if not geometry_ok(radii):
        return None

    def probe(y: float) -> np.ndarray:
        weights = 1.0 / np.abs((scale / vals) - y)
        return (v @ np.diag(weights) @ v.T).astype(complex)

    probes = [probe(0.0), probe(Y1)]
    rows = [herm_vec(np.eye(D)), herm_vec(H)]
    for k in (0, 1):
        for t in TIMES:
            rows.append(herm_vec(evolve(probes[k], float(t))))
    rows.append(herm_vec(sym(evolve(probes[0], T_RESPONSE), probes[0])))
    for k, l, t in EXTRA:
        rows.append(herm_vec(sym(evolve(probes[k], float(t)), probes[l])))

    a = np.vstack(rows)
    _, singular, vh = np.linalg.svd(a, full_matrices=True)
    rank = int(np.sum(singular > 1e-10))
    if rank != 24:
        return None

    nv = vh[-1]
    d0 = mat_from_herm_vec(nv)
    d0 /= np.max(np.abs(np.linalg.eigvalsh(d0)))
    rp = np.eye(D) / D + EPS * d0
    rm = np.eye(D) / D - EPS * d0
    if min(np.min(np.linalg.eigvalsh(rp)), np.min(np.linalg.eigvalsh(rm))) <= 0:
        return None
    delta = rp - rm

    h2 = harmonic(delta, probes[0], probes[0], 2)
    h4 = harmonic(delta, probes[0], probes[0], 4)
    g2 = harmonic(delta, grad0, probes[0], 2)
    g4 = harmonic(delta, grad0, probes[0], 4)

    c_response = herm_vec(comm(evolve(probes[0], T_RESPONSE), probes[0]))
    eta = abs(c_response @ nv) / np.linalg.norm(c_response)

    an = a / np.linalg.norm(a, axis=1, keepdims=True)
    sn = np.linalg.svd(an, compute_uv=False)
    nz = sn[sn > 1e-10]
    smin = float(nz[-1])
    condition = float(nz[0] / nz[-1])

    bt = evolve(probes[0], T_RESPONSE)
    mean_p = np.trace(rp @ bt)
    mean_m = np.trace(rm @ bt)
    dp = bt - mean_p * np.eye(D)
    dm = bt - mean_m * np.eye(D)
    m0p = np.trace(rp @ probes[0])
    m0m = np.trace(rm @ probes[0])
    d0p = probes[0] - m0p * np.eye(D)
    d0m = probes[0] - m0m * np.eye(D)
    noise_p = float(np.real(np.trace(rp @ sym(dp, d0p))))
    noise_m = float(np.real(np.trace(rm @ sym(dm, d0m))))
    resp_p = float(np.real(np.trace(rp @ comm(bt, probes[0]))))
    resp_m = float(np.real(np.trace(rm @ comm(bt, probes[0]))))

    return {
        "seff_d1": seff(h2, h4),
        "seff_d2": seff(g2, g4),
        "h2": h2, "h4": h4, "g2": g2, "g4": g4,
        "eta": eta,
        "smin": smin,
        "condition": condition,
        "radii": radii,
        "eig_plus": np.linalg.eigvalsh(rp),
        "eig_minus": np.linalg.eigvalsh(rm),
        "constraint_residual": float(np.max(np.abs(a @ herm_vec(d0)))),
        "target_mean_difference": float(abs(mean_p - mean_m)),
        "target_noise_difference": float(abs(noise_p - noise_m)),
        "response_plus": resp_p,
        "response_minus": resp_m,
    }


def run_np2_scan(n_trials: int = 5000):
    rng = np.random.default_rng(20260829)
    best = None
    for trial in range(n_trials):
        x = rng.normal(size=(D, D))
        braw = (x + x.T) / 2.0
        m = np2_metrics(braw)
        if m is None:
            continue
        score = np.sqrt((m["seff_d1"] / BASE_SEFF_D1) *
                        (m["seff_d2"] / BASE_SEFF_D2))
        if best is None or score > best[0]:
            best = (score, trial, m)
    return best


def run_np3_scan(n_trials: int = 5000):
    rng = np.random.default_rng(314159)
    best = None
    accepted = 0
    for trial in range(n_trials):
        x = rng.normal(size=(D, D))
        braw = (x + x.T) / 2.0
        m = np3_metrics(braw)
        if m is None:
            continue
        # Accept only simultaneous non-degradation of the two calibration
        # diagnostics that were weak in Toy 007.
        if m["eta"] < BASE_ETA or m["smin"] < BASE_SMIN:
            continue
        accepted += 1
        if best is None or m["seff_d1"] > best[0]:
            best = (m["seff_d1"], trial, m)
    return accepted, best


def main():
    np2 = run_np2_scan()
    assert np2 is not None
    _, trial2, m2 = np2
    print("NP2 detector-only best trial:", trial2)
    print("  D1 Fisher gain:", m2["seff_d1"] / BASE_SEFF_D1)
    print("  D2 Fisher gain:", m2["seff_d2"] / BASE_SEFF_D2)
    print("  radii:", m2["radii"])

    accepted, np3 = run_np3_scan()
    assert np3 is not None
    _, trial3, m3 = np3
    print("NP3 non-degraded candidates:", accepted)
    print("NP3 accepted best trial:", trial3)
    print("  D1 Fisher gain:", m3["seff_d1"] / BASE_SEFF_D1)
    print("  D2 Fisher gain:", m3["seff_d2"] / BASE_SEFF_D2)
    print("  eta_R:", m3["eta"])
    print("  normalized s_min:", m3["smin"])
    print("  condition:", m3["condition"])
    print("  radii:", m3["radii"])
    print("  H2,H4:", m3["h2"], m3["h4"])
    print("  G2,G4:", m3["g2"], m3["g4"])
    print("  eig(rho+):", m3["eig_plus"])
    print("  eig(rho-):", m3["eig_minus"])
    print("  equality residual:", m3["constraint_residual"])
    print("  target mean/noise differences:",
          m3["target_mean_difference"], m3["target_noise_difference"])
    print("  target response +/-:", m3["response_plus"], m3["response_minus"])

    # Regression checks for the recorded scans.
    assert trial2 == 2641
    assert abs(m2["seff_d1"] / BASE_SEFF_D1 - 5.3624939) < 1e-5
    assert abs(m2["seff_d2"] / BASE_SEFF_D2 - 4.1741392) < 1e-5
    assert accepted == 1
    assert trial3 == 811
    assert abs(m3["seff_d1"] / BASE_SEFF_D1 - 1.2218350) < 1e-5
    assert abs(m3["seff_d2"] / BASE_SEFF_D2 - 1.4035830) < 1e-5
    assert abs(m3["eta"] - 0.5688230) < 1e-6
    assert abs(m3["smin"] - 0.0015122242) < 1e-9
    assert m3["constraint_residual"] < 1e-12
    assert m3["target_mean_difference"] < 1e-12
    assert m3["target_noise_difference"] < 1e-12


if __name__ == "__main__":
    main()
