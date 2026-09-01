#!/usr/bin/env python3
"""RQIR Iteration 245: exact bookkeeping for VD composite trace sectors.

This is intentionally algebraic.  It does not commute U1/U2 and does not
perform any physics-dependent propagator cancellation.  It records the
primitive Green-operator content implied by the primary definitions and the
curvature dressing required by e+c<=3.
"""

from dataclasses import dataclass
import json
from pathlib import Path

@dataclass(frozen=True)
class Count:
    n_N: int
    n_G: int
    eom_degree: int

    def __add__(self, other: "Count") -> "Count":
        return Count(self.n_N + other.n_N, self.n_G + other.n_G,
                     self.eom_degree + other.eom_degree)

U1 = Count(2, 0, 1)
U2 = Count(2, 1, 2)

sectors = {
    "Tr_U1": U1,
    "Tr_U2": U2,
    "Tr_U1_sq": U1 + U1,
    "Tr_U1_cu": U1 + U1 + U1,
    "Tr_U1_U2": U1 + U2,
}

out = {
    "iteration": 245,
    "model_readiness_percent": 24,
    "primitive_definitions": {
        "U1": {"n_N": 2, "n_G": 0, "eom_degree": 1},
        "U2": {"n_N": 2, "n_G": 1, "eom_degree": 2},
    },
    "sectors": {},
    "rule": "e+c<=3",
    "classification": "FINITE_FLAT_RESOLVENT_EXPANSION_REQUIRED_NOT_DIRECT_SINGLE_OPERATOR_CPT3",
}

for name, c in sectors.items():
    out["sectors"][name] = {
        "n_N": c.n_N,
        "n_G": c.n_G,
        "eom_degree": c.eom_degree,
        "max_extra_curvature_dressing": 3 - c.eom_degree,
    }

expected = {
    "Tr_U1": (2, 0, 1, 2),
    "Tr_U2": (2, 1, 2, 1),
    "Tr_U1_sq": (4, 0, 2, 1),
    "Tr_U1_cu": (6, 0, 3, 0),
    "Tr_U1_U2": (4, 1, 3, 0),
}
for name, vals in expected.items():
    got = out["sectors"][name]
    assert (got["n_N"], got["n_G"], got["eom_degree"],
            got["max_extra_curvature_dressing"]) == vals

path = Path(__file__).resolve().parents[1] / "results" / "iteration245_vd_composite_trace_bookkeeping.json"
path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(path)
