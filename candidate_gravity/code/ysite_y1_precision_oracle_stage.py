#!/usr/bin/env python3
"""Frozen Y-site y1 precision + same-h fourth-order oracle stage.

Prospectively frozen by authoritative Iteration 443.  This stage is deliberately
unnumbered until raw consumption assigns a unique authoritative iteration ID.
It does not promote a physical coordinate and does not alter dynamics, routing,
numerator, finite-difference step, or thresholds.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import mpmath as mp
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SRC368 = ROOT / "candidate_gravity/code/iteration368_tru1sq_timelike_full_prepruning_routing.py"
SRC443 = ROOT / "candidate_gravity/code/iteration443_layer368_370_precision_boundary_audit.py"

H = "4e-5"
CROSS_PRECISION_MAX = mp.mpf("1e-30")
CENTRAL_VS_FOURTH_SCALED_MAX = mp.mpf("2e-5")

# Exact frozen Iteration-368 representative fixture construction.  The binary64
# fixture values are authoritative inputs; all Y-site arithmetic below is mp.
rng = np.random.default_rng(319)
Hs = []
for _ in range(3):
    x = rng.normal(size=(4, 4))
    Hs.append(0.12 * (x + x.T) / 2.0)
LEGS = ("s", "a", "b")
QS = (
    np.array([1.0, 0.0, 0.0, 0.0]),
    np.array([-0.4, 0.1, 0.1, 0.0]),
    np.array([-0.6, -0.1, -0.1, 0.0]),
)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mp_from_float(x: float) -> mp.mpf:
    # repr(float) round-trips the frozen binary64 fixture exactly.
    return mp.mpf(repr(float(x)))


def matrix_from_float(a: np.ndarray) -> mp.matrix:
    return mp.matrix([[mp_from_float(a[i, j]) for j in range(4)] for i in range(4)])


def y_down_mp(scale: mp.mpf, hmat: mp.matrix) -> mp.matrix:
    eta = mp.matrix([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    g = eta + scale * hmat
    return mp.sqrt(abs(mp.det(g))) * g


def derivs_for_leg(h_float: np.ndarray, digits: int):
    with mp.workdps(digits):
        h = mp.mpf(H)
        hm = matrix_from_float(h_float)
        ym2 = y_down_mp(-2 * h, hm)
        ym1 = y_down_mp(-h, hm)
        yp1 = y_down_mp(h, hm)
        yp2 = y_down_mp(2 * h, hm)
        central = (yp1 - ym1) / (2 * h)
        fourth = (ym2 - 8 * ym1 + 8 * yp1 - yp2) / (12 * h)
        # Decimal strings preserve the evaluation at the requested precision.
        def dump(m):
            return [[mp.nstr(m[i, j], digits) for j in range(4)] for i in range(4)]
        return dump(central), dump(fourth)


def to_mp_matrix(rows):
    return mp.matrix([[mp.mpf(rows[i][j]) for j in range(4)] for i in range(4)])


def max_abs(m: mp.matrix) -> mp.mpf:
    return max(abs(m[i, j]) for i in range(4) for j in range(4))


def main() -> None:
    rows = []
    max_cross = mp.mpf("0")
    max_repr = mp.mpf("0")
    all_finite = True
    with mp.workdps(140):
        for leg, q, hmat in zip(LEGS, QS, Hs):
            c80s, f80s = derivs_for_leg(hmat, 80)
            c120s, f120s = derivs_for_leg(hmat, 120)
            c80, f80 = to_mp_matrix(c80s), to_mp_matrix(f80s)
            c120, f120 = to_mp_matrix(c120s), to_mp_matrix(f120s)
            cross = max_abs(c80 - c120)
            oracle_cross = max_abs(f80 - f120)
            scale = max(max_abs(c120), max_abs(f120), mp.mpf("1e-30"))
            repr_scaled = max_abs(c120 - f120) / scale
            finite = all(mp.isfinite(z) for m in (c80, f80, c120, f120) for z in m)
            all_finite = all_finite and finite
            max_cross = max(max_cross, cross)
            max_repr = max(max_repr, repr_scaled)
            rows.append({
                "leg": leg,
                "q": [float(x) for x in q],
                "metric_tensor_sha256": hashlib.sha256(np.asarray(hmat, dtype=np.float64).tobytes()).hexdigest(),
                "central_mp80_vs_mp120_max_abs": mp.nstr(cross, 30),
                "fourth_mp80_vs_mp120_max_abs": mp.nstr(oracle_cross, 30),
                "central_vs_fourth_mp120_scaled_max": mp.nstr(repr_scaled, 30),
                "finite": bool(finite),
            })

        passed = bool(all_finite and max_cross <= mp.mpf("1e-30") and max_repr <= mp.mpf("2e-5") and len(rows) == 3)
        result = {
            "stage": "YSITE_Y1_PRECISION_ORACLE_STAGE__POST_ITER443__UNNUMBERED_UNTIL_RAW_CONSUME",
            "authority_scope": "LAYER368_370_YSITE_Y1_PRECISION_AND_FIXED_H_REPRESENTATION__NON_PROMOTING",
            "classification": (
                "PASS_YSITE_Y1_MP80_MP120_AND_FIXED_H_FOURTH_ORDER_ORACLE__NON_PROMOTING"
                if passed else
                "BLOCKED_YSITE_Y1_PRECISION_OR_REPRESENTATION_CLOSURE__NON_PROMOTING"
            ),
            "scientific_gate_pass": passed,
            "promotes_physical_coordinate": False,
            "frozen": {
                "h": H,
                "precision_digits": [80, 120],
                "central_formula": "[y(+h)-y(-h)]/(2h)",
                "fourth_order_formula": "[y(-2h)-8y(-h)+8y(+h)-y(+2h)]/(12h)",
                "pair_labels": list(LEGS),
                "pair_count": 3,
                "fixture_seed": 319,
            },
            "thresholds": {
                "central_mp80_vs_mp120_max_abs": "1e-30",
                "central_vs_fourth_mp120_scaled_max": "2e-5",
                "required_pair_count": 3,
            },
            "observed": {
                "central_mp80_vs_mp120_max_abs": mp.nstr(max_cross, 30),
                "central_vs_fourth_mp120_scaled_max": mp.nstr(max_repr, 30),
                "pair_count": len(rows),
                "all_values_finite": bool(all_finite),
            },
            "rows": rows,
            "source_sha256": {
                str(SRC368.relative_to(ROOT)): sha256_file(SRC368),
                str(SRC443.relative_to(ROOT)): sha256_file(SRC443),
            },
            "guardrails": [
                "SAME_H_ONLY_4E-5",
                "NO_ADAPTIVE_OR_SMALLER_H",
                "NO_THRESHOLD_WEAKENING",
                "NO_ROUTING_OR_NUMERATOR_CHANGE",
                "NO_OUTER_ONLY_MP_AROUND_BINARY64_YSITE",
                "NON_PROMOTING_PARENT_NUMERICAL_GATE",
                "UNSUPPORTED_IS_BLOCKED_NOT_ZERO_FILL",
            ],
            "next_gate_if_pass": "certify post-parent layer368/370 matrix multiplication and trace arithmetic in continuous precision",
            "next_gate_if_blocked": "preserve blocker and localize failing Y-site pair/component without changing h or thresholds",
            "MODEL_READINESS": "24%",
            "readiness_change_pp": 0,
        }
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
