"""RQIR Iteration 028: D2 calibration/preparation wall-clock phase diagram.

Uses the exact Iteration-027 Pareto frontiers C_a*(lambda) and minimizes the
physical dimensionless wall-clock cost for each D2 calibration branch.

Define
  x = K_force / K_pot,
  y = K_cov   / K_pot,
  z = R_P K_pot,
where K_* are the lambda=1 calibration times and R_P is source-preparation
Fisher per second.  Dividing total time by K_pot gives

  tau_null  = lambda (1+y)   + C_a/z,
  tau_force = lambda (x+y)   + C_a/z,
  tau_aug   = lambda (1+x+y) + C_a/z.

For each branch we minimize tau along the 90%-retention Pareto frontier from
Iteration 027.  No SI hardware rates are invented.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import numpy as np


def load_i27():
    here = Path(__file__).resolve().parent
    path = here / "d2_calibration_resource_frontier_iteration027.py"
    spec = importlib.util.spec_from_file_location("rqir_i27", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def branch_factor(kind: str, x: float, y: float) -> float:
    if kind == "null":
        return 1.0 + y
    if kind == "native_replace":
        return x + y
    if kind == "augmented":
        return 1.0 + x + y
    raise ValueError(kind)


def optimum(mod, pack, kind: str, x: float, y: float, z: float):
    if x <= 0 or y < 0 or z <= 0:
        raise ValueError("require x>0, y>=0, z>0")
    lam0 = mod.min_lambda_with_strong_prep(mod.load_i26(), pack, kind)
    # Cover the near-threshold divergence and the asymptotic preparation limit.
    lams = np.geomspace(lam0 * (1.0 + 1e-7), 1e3, 1400)
    factor = branch_factor(kind, x, y)
    best = (np.inf, np.nan, np.nan)
    for lam in lams:
        ca = mod.min_ca(mod.load_i26(), pack, kind, float(lam))
        if not np.isfinite(ca):
            continue
        tau = factor * lam + ca / z
        if tau < best[0]:
            best = (float(tau), float(lam), float(ca))
    return best


def winner(mod, pack, x: float, y: float, z: float):
    out = {k: optimum(mod, pack, k, x, y, z)
           for k in ["null", "native_replace", "augmented"]}
    return min(out, key=lambda k: out[k][0]), out


def transition_brackets(mod, pack, y: float, z: float):
    xs = np.geomspace(1e-3, 1e3, 1200)
    ws = [winner(mod, pack, float(x), y, z)[0] for x in xs]
    out = []
    for i in range(1, len(xs)):
        if ws[i] != ws[i-1]:
            out.append((float(xs[i-1]), float(xs[i]), ws[i-1], ws[i]))
    return out


def main():
    mod = load_i27()
    i26 = mod.load_i26()
    pack = i26.build()

    print("dimensionless coordinates: x=K_force/K_pot, y=K_cov/K_pot, z=R_P*K_pot")
    samples = [
        (0.1, 0.1, 0.1),
        (0.1, 0.1, 1.0),
        (0.1, 0.1, 10.0),
        (1.0, 1.0, 1.0),
        (1.0, 1.0, 10.0),
        (10.0, 0.1, 1.0),
        (10.0, 1.0, 10.0),
    ]
    for x, y, z in samples:
        w, out = winner(mod, pack, x, y, z)
        print(f"\n(x,y,z)=({x:g},{y:g},{z:g}) winner={w}")
        for k, (tau, lam, ca) in out.items():
            print(f"  {k:14s} tau={tau:.9g} lambda={lam:.9g} Ca={ca:.9g}")

    for y in [0.1, 1.0, 10.0]:
        for z in [0.1, 1.0, 10.0, 100.0]:
            print(f"transitions y={y:g} z={z:g}: {transition_brackets(mod, pack, y, z)}")

    # Regression guards: qualitatively distinct resource regimes.
    assert winner(mod, pack, 0.1, 0.1, 0.1)[0] == "augmented"
    assert winner(mod, pack, 0.1, 0.1, 10.0)[0] == "native_replace"
    assert winner(mod, pack, 10.0, 0.1, 1.0)[0] == "null"
    assert winner(mod, pack, 1.0, 1.0, 1.0)[0] == "augmented"


if __name__ == "__main__":
    main()
