"""RQIR Toy 010 — noisy calibration + source-preparation Fisher analysis.

Builds a local Gaussian Fisher model around the accepted Toy 010 exact-NP3
construction.  The detector data are the real/imaginary quadratures of the
D1 n=2 and n=4 ordered-response harmonics.

Parameters:
  beta : interface-response amplitude of interest;
  a    : amplitude of the prepared source difference along the exact null
         direction;
  u    : 24 orthogonal Hermitian source-state nuisance coordinates.

The exact gravitational NP3 calibration cannot see `a` because A n = 0.
An independent preparation calibration contributes Fisher C_a on `a`.
Row-normalized gravitational calibration contributes strength gamma on the
24 orthogonal directions.

Detector information is normalized so the detector-only beta Fisher is one.
Thus all reported Fisher values are retention fractions of detector-limited
information under the declared local model.
"""
from __future__ import annotations

import numpy as np

from toy010_calibration_geometry_optimization import (
    D, EPS, OPT_Y1, OPT_TIMES, T_RESPONSE,
    H, herm_vec, mat_from_herm_vec, evolve, sym,
    harmonic, probe, GRAD0,
)


def build_model():
    probes = [probe(0.0), probe(OPT_Y1)]
    rows = [herm_vec(np.eye(D)), herm_vec(H)]
    for k in (0, 1):
        for t in OPT_TIMES:
            rows.append(herm_vec(evolve(probes[k], float(t))))
    rows.append(
        herm_vec(sym(evolve(probes[0], T_RESPONSE), probes[0]))
    )
    extra = [
        (0, 1, OPT_TIMES[1]),
        (1, 1, OPT_TIMES[5]),
        (1, 0, T_RESPONSE),
        (0, 1, T_RESPONSE),
        (1, 0, OPT_TIMES[3]),
        (0, 0, OPT_TIMES[6]),
        (0, 1, OPT_TIMES[6]),
    ]
    for k, l, t in extra:
        rows.append(
            herm_vec(sym(evolve(probes[k], float(t)), probes[l]))
        )

    a = np.vstack(rows)
    a_norm = a / np.linalg.norm(a, axis=1, keepdims=True)
    _, _, vh = np.linalg.svd(a, full_matrices=True)
    n = vh[-1]
    q = vh[:-1].T  # 25 x 24 orthonormal complement of the null direction

    # Nominal physical state-difference amplitude used in Toy 010.
    d0 = mat_from_herm_vec(n)
    d0 /= np.max(np.abs(np.linalg.eigvalsh(d0)))
    theta0 = 2.0 * EPS * herm_vec(d0)

    # Linear D1 detector map from Hermitian state-difference coordinates to
    # four real quadratures: Re/Im H2, Re/Im H4.
    b = np.zeros((4, D * D), dtype=float)
    for j in range(D * D):
        e = np.zeros(D * D)
        e[j] = 1.0
        op = mat_from_herm_vec(e)
        h2 = harmonic(op, probes[0], probes[0], 2)
        h4 = harmonic(op, probes[0], probes[0], 4)
        b[:, j] = [h2.real, h2.imag, h4.real, h4.imag]

    s = b @ theta0
    detector_fisher = float(s @ s)
    b /= np.sqrt(detector_fisher)
    s = b @ theta0

    return {
        "A": a,
        "A_norm": a_norm,
        "n": n,
        "Q": q,
        "B": b,
        "s": s,
        "Bu": b @ q,
        "Ac": a_norm @ q,
    }


def profiled_beta_fisher(model: dict, gamma: float, c_a: float) -> float:
    """Return F_beta after profiling source amplitude and 24 state nuisances."""
    s = model["s"]
    bu = model["Bu"]
    ac = model["Ac"]

    # Parameter order: beta, a, u_1..u_24.
    j = np.column_stack([s, s, bu])
    f = j.T @ j

    # Independent nongravitational source-preparation information on a.
    f[1, 1] += c_a

    # Row-normalized gravitational calibration information on u.
    f[2:, 2:] += gamma * (ac.T @ ac)

    nuisance = f[1:, 1:]
    cross = f[0, 1:]
    return float(
        f[0, 0]
        - cross @ np.linalg.pinv(nuisance, rcond=1e-12) @ cross.T
    )


def gamma_for_target(model: dict, c_a: float, target: float):
    grid = np.logspace(-2, 10, 2000)
    vals = np.array([
        profiled_beta_fisher(model, float(g), c_a) for g in grid
    ])
    idx = np.where(vals >= target)[0]
    return None if len(idx) == 0 else float(grid[int(idx[0])])


def main():
    model = build_model()
    s_norm = float(model["s"] @ model["s"])
    svals = np.linalg.svd(model["A_norm"], compute_uv=False)
    smin = float(svals[-1])

    print("detector-only normalized beta Fisher:", s_norm)
    print("row-normalized calibration s_min:", smin)
    print("conditioning information scale 1/s_min^2:", 1.0 / smin**2)

    print("\nNo source-amplitude preparation calibration (C_a=0):")
    for gamma in [0.0, 1.0, 1e2, 1e4, 1e6, 1e8]:
        print(gamma, profiled_beta_fisher(model, gamma, 0.0))

    print("\nFinite source-preparation calibration:")
    for c_a in [1.0, 9.0, 19.0, 99.0, 1e6]:
        vals = [
            profiled_beta_fisher(model, g, c_a)
            for g in [1e4, 1e5, 2e5, 1e6, 1e8]
        ]
        print("C_a=", c_a, "F(gamma)=", vals,
              "asymptotic=", c_a / (1.0 + c_a))

    print("\nGamma requirements:")
    for c_a in [9.0, 99.0, 1e6]:
        print("C_a=", c_a)
        for target in [0.5, 0.8, 0.9, 0.95]:
            print(" target", target,
                  "gamma", gamma_for_target(model, c_a, target))

    # Core regression / theorem checks.
    assert abs(s_norm - 1.0) < 1e-12
    assert abs(smin - 0.00221100896) < 2e-9

    # Exact null-amplitude degeneracy: gravitational calibration alone cannot
    # distinguish beta from source amplitude a.
    for gamma in [0.0, 1.0, 1e2, 1e4, 1e6, 1e8]:
        assert abs(profiled_beta_fisher(model, gamma, 0.0)) < 1e-9

    # With very strong orthogonal calibration, only the beta-a degeneracy
    # remains, giving the analytic limit C_a/(1+C_a).
    for c_a in [1.0, 9.0, 19.0, 99.0]:
        f = profiled_beta_fisher(model, 1e12, c_a)
        assert abs(f - c_a / (1.0 + c_a)) < 2e-4


if __name__ == "__main__":
    main()
