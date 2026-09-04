#!/usr/bin/env python3
"""Iteration 443: source-level precision-boundary audit for the frozen 368/370 layer.

This is a non-promoting, fail-closed audit.  It does not change the physics,
finite-difference nodes, routing, numerator, or any acceptance threshold.
Its purpose is to prove which numerical objects remain outside the already
closed Iteration-270 Q0/Q1/Acoef/Asub precision certificate before a genuine
80/120-digit port of the 368/370 layer is attempted.
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC368 = ROOT / "candidate_gravity/code/iteration368_tru1sq_timelike_full_prepruning_routing.py"
SRC370 = ROOT / "candidate_gravity/code/iteration370_tru1sq_physical_numerator_transport.py"
OUT = ROOT / "candidate_gravity/results/iteration443_layer368_370_precision_boundary_audit.json"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> None:
    s368 = SRC368.read_text(encoding="utf-8")
    s370 = SRC370.read_text(encoding="utf-8")

    # Fail closed if the historical frozen implementation no longer exposes
    # the independently differentiated Y-site or if its original step changes.
    y1_def = re.search(r"def\s+y1\s*\([^\)]*h\s*=\s*4e-5[^\)]*\)\s*:", s368)
    y1_plus = re.search(r"y_down\([^\n]*scale\s*=\s*\+?h", s368)
    y1_minus = re.search(r"y_down\([^\n]*scale\s*=\s*-h", s368)
    y1_central = ("2*h" in s368) or ("2 * h" in s368)

    # Post-parent contraction/trace arithmetic is a distinct retained numerical
    # boundary.  We deliberately do not treat Iteration-270 parent closure as
    # a certificate for these NumPy operations.
    has_matmul = "@" in s368
    has_trace = ("np.trace" in s368) or ("numpy.trace" in s368)
    has_complex_numpy = ("dtype=complex" in s368) or ("dtype=np.complex" in s368) or ("np.complex" in s368)

    # Iteration 370 transports the physical numerator through the 368 layer;
    # it must therefore inherit, not silently erase, this precision boundary.
    inherits_368 = ("iteration368" in s370) or ("exec(" in s370 and "368" in s370)

    checks = {
        "frozen_y1_default_h_4e-5_present": bool(y1_def),
        "y1_uses_y_down_plus_h": bool(y1_plus),
        "y1_uses_y_down_minus_h": bool(y1_minus),
        "y1_has_central_two_h_denominator": bool(y1_central),
        "post_parent_matrix_multiplication_present": bool(has_matmul),
        "post_parent_trace_present": bool(has_trace),
        "numpy_complex_arithmetic_present": bool(has_complex_numpy),
        "iteration370_inherits_iteration368_layer": bool(inherits_368),
    }
    scientific_gate_pass = all(checks.values())

    result = {
        "iteration": 443,
        "scope": "layer368_370_precision_boundary_source_audit",
        "classification": (
            "PASS_ITER443_LAYER368_370_PRECISION_BOUNDARY_AUDIT__NON_PROMOTING"
            if scientific_gate_pass
            else "FAIL_ITER443_LAYER368_370_PRECISION_BOUNDARY_AUDIT__OPERATIONAL"
        ),
        "scientific_gate_pass": scientific_gate_pass,
        "promotes_physical_coordinate": False,
        "changes_dynamics": False,
        "changes_thresholds": False,
        "source_sha256": {
            str(SRC368.relative_to(ROOT)): sha256_text(s368),
            str(SRC370.relative_to(ROOT)): sha256_text(s370),
        },
        "checks": checks,
        "frozen_findings": {
            "unclosed_y_site_object": "y1 = [y_down(+h)-y_down(-h)]/(2h)",
            "frozen_y1_h": 4.0e-5,
            "unclosed_post_parent_arithmetic": [
                "binary64/NumPy matrix products",
                "binary64/NumPy trace contractions",
            ],
            "interpretation": (
                "Iteration-270 Q0/Q1/Acoef/Asub closure is necessary but not sufficient "
                "for a continuous precision certificate of layer 368/370."
            ),
        },
        "prospective_next_gate": {
            "object": "Y-site y1 and then post-parent contractions/trace",
            "same_h_only": 4.0e-5,
            "precision_digits": [80, 120],
            "y1_cross_precision_threshold": 1.0e-30,
            "y1_central_vs_same_h_fourth_order_threshold": 2.0e-5,
            "fourth_order_formula": "[f(-2h)-8f(-h)+8f(+h)-f(+2h)]/(12h)",
            "must_cover": "all distinct frozen Y-site input pairs used by the 368/370 representative/transport probe set",
            "forbidden": [
                "smaller/adapted h",
                "threshold weakening",
                "changed routing",
                "changed numerator",
                "outer-only high precision around binary64 Y-site values",
            ],
        },
        "MODEL_READINESS": "24%",
        "readiness_change_pp": 0,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not scientific_gate_pass:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
