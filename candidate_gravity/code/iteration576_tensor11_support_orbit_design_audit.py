#!/usr/bin/env python3
"""Iteration576 exact audit of the frozen Iter421 tensor11 support/design.

No scientific values from the active Iter575 matrix are consumed here.
This checks only the prospectively frozen node geometry and fit design.
"""
from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "candidate_gravity/contracts/iteration575_iter421_tensor11_exact_mp_support_manifest.json"
OUT = ROOT / "candidate_gravity/results/iteration576_tensor11_support_orbit_design_audit.json"


def det_fraction(a):
    a = [list(map(Fraction, row)) for row in a]
    n = len(a)
    det = Fraction(1)
    for i in range(n):
        p = next((r for r in range(i, n) if a[r][i] != 0), None)
        if p is None:
            return Fraction(0)
        if p != i:
            a[i], a[p] = a[p], a[i]
            det *= -1
        piv = a[i][i]
        det *= piv
        for j in range(i, n):
            a[i][j] /= piv
        for r in range(i + 1, n):
            f = a[r][i]
            if f:
                for j in range(i, n):
                    a[r][j] -= f * a[i][j]
    return det


def matmul_t_x(rows):
    p = len(rows[0])
    return [[sum(row[i] * row[j] for row in rows) for j in range(p)] for i in range(p)]


def orbit_key(u, v):
    return (abs(Fraction(str(u))), abs(Fraction(str(v))))


def signed_node(u, v):
    return (Fraction(str(u)), Fraction(str(v)))


def full_sign_orbit(key):
    a, b = key
    return {(su*a, sv*b) for su in (-1, 1) for sv in (-1, 1)}


m = json.loads(MANIFEST.read_text())
existing = {signed_node(u, v) for u, v in m["existing_high_precision_support"]["nodes"]}
missing = {signed_node(x["u"], x["v"]) for x in m["missing_high_precision_support"]["nodes_in_first_occurrence_order_of_original_Iter421_F_cache"]}
all_nodes = existing | missing

all_orbits = sorted({orbit_key(u, v) for u, v in all_nodes})
existing_orbits = []
missing_orbits = []
straddled_orbits = []
for key in all_orbits:
    orb = full_sign_orbit(key)
    e = orb <= existing
    n = orb <= missing
    if e:
        existing_orbits.append(key)
    elif n:
        missing_orbits.append(key)
    else:
        straddled_orbits.append(key)

multipliers = [Fraction(1), Fraction(3,4), Fraction(1,2), Fraction(1,4)]
xy = [(r*r, s*s) for r in multipliers for s in multipliers]
X = [[Fraction(1), x, y, x*y] for x, y in xy]
XtX = matmul_t_x(X)
det = det_fraction(XtX)
rank = 4 if det != 0 else None

result = {
    "iteration": 576,
    "date": "2026-09-08",
    "classification": "PASS_ITER421_TENSOR11_SUPPORT_ORBIT_AND_DESIGN_IDENTIFIABILITY_AUDIT_EXACT__NON_PROMOTING",
    "scientific_gate_pass": True,
    "promotes_physical_coordinate": False,
    "MODEL_READINESS": "24%",
    "readiness_change_pp": 0,
    "support": {
        "signed_nodes_total": len(all_nodes),
        "sign_orbits_total": len(all_orbits),
        "existing_signed_nodes": len(existing),
        "missing_signed_nodes": len(missing),
        "existing_complete_sign_orbits": len(existing_orbits),
        "missing_complete_sign_orbits": len(missing_orbits),
        "straddled_sign_orbits": len(straddled_orbits),
        "each_cross_C_uses_single_provenance_class": len(straddled_orbits) == 0,
        "existing_orbits": [[str(a), str(b)] for a,b in existing_orbits],
        "missing_orbits": [[str(a), str(b)] for a,b in missing_orbits],
    },
    "tensor11_design": {
        "observations_Crs": 16,
        "parameters": 4,
        "residual_dof": 12,
        "rank": rank,
        "XtX_det_exact": f"{det.numerator}/{det.denominator}",
        "XtX_det_positive": det > 0,
        "basis": ["1", "x", "y", "x*y"],
        "x_y_values": ["1", "9/16", "1/4", "1/16"],
    },
    "interpretation": [
        "The original tensor11 residual is overdetermined, not saturated: 16 C(r,s) observations fit 4 coefficients, leaving 12 residual degrees of freedom.",
        "The 28 pre-existing and 36 newly requested signed F nodes partition into whole four-sign orbits, so no individual symmetric-cross C(r,s) mixes old and new support provenance.",
        "This is a design/support identifiability result only; it does not evaluate the tensor11 residual and cannot promote physical index2."
    ],
    "guardrails": ["NO_ACTIVE_MATRIX_RESULT_CONSUMED", "NO_NODE_CHANGE", "NO_THRESHOLD_CHANGE", "NO_PHYSICAL_PROMOTION", "NO_ANSATZ003", "NO_FISHER_RESOURCES"]
}
assert len(all_nodes) == 64
assert len(all_orbits) == 16
assert len(existing_orbits) == 7
assert len(missing_orbits) == 9
assert len(straddled_orbits) == 0
assert det == Fraction(276922881, 16777216)
OUT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
