"""RQIR Iteration 027: D2 calibration/preparation resource frontier.

Builds directly on Iteration 026 and asks a narrower, experimentally meaningful
question: for a target profiled Fisher retention r*=0.90, how much independent
source-preparation Fisher C_a is required as a function of a common calibration
exposure multiplier lambda for each D2 calibration branch?

No SI-time conversion is made here.  The code instead outputs the Pareto frontier
C_a*(lambda), the minimum calibration multiplier attainable with asymptotically
strong source metrology, and ideal source-copy equivalents C_a/F_Q using the
Iteration-020 QFI F_Q=13.2707.

Wall-clock conversion must later use branch-specific physical rates:
  T_null   = lambda (K_pot + K_cov) + C_a/R_P
  T_force  = lambda (K_force + K_cov) + C_a/R_P
  T_aug    = lambda (K_pot + K_force + K_cov) + C_a/R_P
where K_* are the lambda=1 calibration times derived from the measurement-level
row Fisher rates and R_P is physical preparation Fisher per second.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import numpy as np

TARGET = 0.90
FQ = 13.2707


def load_i26():
    here = Path(__file__).resolve().parent
    path = here / "d2_calibration_branch_fisher_iteration026.py"
    spec = importlib.util.spec_from_file_location("rqir_i26", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def min_ca(mod, pack, kind: str, scale: float, target: float = TARGET) -> float:
    A, labels, G, theta0, B, s, Z, Zu, _sv = pack
    f = lambda ca: mod.profiled(A, labels, G, theta0, B, s, Zu, kind, ca, scale)
    if f(0.0) >= target:
        return 0.0
    if f(1e12) < target:
        return np.inf
    lo, hi = 0.0, 1.0
    while f(hi) < target:
        hi *= 10.0
        if hi > 1e12:
            return np.inf
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if f(mid) >= target:
            hi = mid
        else:
            lo = mid
    return hi


def min_lambda_with_strong_prep(mod, pack, kind: str, target: float = TARGET) -> float:
    A, labels, G, theta0, B, s, Z, Zu, _sv = pack
    f = lambda lam: mod.profiled(A, labels, G, theta0, B, s, Zu, kind, 1e12, lam)
    lo, hi = 1e-6, 100.0
    assert f(hi) >= target
    for _ in range(100):
        mid = np.sqrt(lo * hi)
        if f(mid) >= target:
            hi = mid
        else:
            lo = mid
    return hi


def main():
    mod = load_i26()
    pack = mod.build()
    scales = [0.1, 0.3, 1.0, 1.001, 1.01, 1.05, 1.1, 1.2, 1.5, 2.0, 3.0, 4.89, 10.0, 100.0]

    print("target", TARGET, "FQ", FQ)
    for kind in ["null", "native_replace", "augmented"]:
        print("\nbranch", kind)
        lam_min = min_lambda_with_strong_prep(mod, pack, kind)
        print("lambda_min_with_strong_prep", lam_min)
        for lam in scales:
            ca = min_ca(mod, pack, kind, lam)
            copies = ca / FQ if np.isfinite(ca) else np.inf
            print(f"lambda={lam:.6g} Ca90={ca:.12g} ideal_copy_equiv={copies:.12g}")

    # Regression guards for the new frontier.
    ca_np3_105 = min_ca(mod, pack, "null", 1.05)
    ca_force_1 = min_ca(mod, pack, "native_replace", 1.0)
    ca_aug_1 = min_ca(mod, pack, "augmented", 1.0)
    lam_np3 = min_lambda_with_strong_prep(mod, pack, "null")
    lam_force = min_lambda_with_strong_prep(mod, pack, "native_replace")
    lam_aug = min_lambda_with_strong_prep(mod, pack, "augmented")

    assert 190.0 < ca_np3_105 < 200.0
    assert 12.5 < ca_force_1 < 13.5
    assert 11.3 < ca_aug_1 < 12.1
    assert 0.999 < lam_np3 < 1.002
    assert 0.35 < lam_force < 0.36
    assert 0.17 < lam_aug < 0.18


if __name__ == "__main__":
    main()
