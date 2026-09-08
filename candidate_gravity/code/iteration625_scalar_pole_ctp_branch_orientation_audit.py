#!/usr/bin/env python3
"""Iteration 625: scalar-pole CTP/retarded branch-orientation audit.

Iter608/615 use one algebraic/Feynman-like K+i0 pole rule with K=m^2-r^2.
The native observable is retarded/CTP. Before assuming one common N_native can
map all six source roots, audit the sign of the internal scalar energy r^0 at
each frozen Iter614/615 root.

For a scalar retarded denominator, the infinitesimal prescription is energy
oriented: in p^2-m^2 variables it is +i0*sign(r^0) (equivalently in
K=m^2-p^2 variables the sign is reversed). Thus roots of opposite r^0 cannot
be converted from a common Feynman K+i0 rule by one universal sign unless the
full CTP measurement map assigns a non-retarded component to that internal
line. This audit does NOT choose the CTP component.
"""
from __future__ import annotations
import contextlib, io, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CROOT = ROOT / "candidate_gravity/code"

# Inherit the exact Iter368 fixture rather than retyping mode energies.
p368 = CROOT / "iteration368_tru1sq_timelike_full_prepruning_routing.py"
src = p368.read_text()
marker = "# Cache expensive same-parent blocks by routed loop momentum."
if src.count(marker) != 1:
    raise SystemExit("Iter368 setup boundary drift")
ns = {"__name__": "iteration625_parent368_fixture", "__file__": str(p368)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split(marker, 1)[0], str(p368), "exec"), ns, ns)
M = ns["M"]
q0 = {k: float(M[k][0][0]) for k in ("s", "a", "b")}

r615 = json.loads((ROOT / "candidate_gravity/results/iteration615_native_s_source_pole_coefficient_audit.json").read_text())
rows = []
failures = []
for row in r615["root_rows"]:
    label = row["root_denominator"]
    s = float(row["s"])
    if not (label.startswith("D_") and label[-1] in "+-"):
        failures.append(f"unparsed denominator label {label}")
        continue
    leg = label[2]
    branch = label[-1]
    # Iter613: D_i^+ = m^2-(p0+q_i)^2 ; D_i^- = m^2-(p0-q_i)^2.
    internal_r0 = math.sqrt(s) + (q0[leg] if branch == "+" else -q0[leg])
    if abs(internal_r0) < 1e-14:
        failures.append(f"zero-energy pole orientation undefined at {label}, s={s}")
    rows.append({
        "root_denominator": label,
        "s": s,
        "internal_r0": internal_r0,
        "energy_sign": 1 if internal_r0 > 0 else -1 if internal_r0 < 0 else 0,
        "iter615_source_coefficient": row["aggregate_normalized_internal_scalar_cut_coefficient"],
    })

positive = sum(r["energy_sign"] > 0 for r in rows)
negative = sum(r["energy_sign"] < 0 for r in rows)
if positive != 5 or negative != 1:
    failures.append(f"unexpected energy-sign census +{positive}/-{negative}")
negative_rows = [r for r in rows if r["energy_sign"] < 0]
if len(negative_rows) != 1 or negative_rows[0]["root_denominator"] != "D_s^-" or abs(negative_rows[0]["s"] - 0.09) > 1e-14:
    failures.append("unexpected negative-energy root identity")

passed = not failures
result = {
    "iteration": 625,
    "date": "2026-09-08",
    "scientific_gate_pass": passed,
    "candidate_residual": False,
    "classification": (
        "PASS_ITER625_INTERNAL_SCALAR_ENERGY_SIGN_CENSUS__CTP_LINE_TYPE_ASSIGNMENT_REQUIRED_BEFORE_ONE_COMMON_N_NATIVE_RETARDED_BINDING__NON_RESIDUAL"
        if passed else "BLOCKED_ITER625_KINEMATIC_ORIENTATION_AUTHORITY_DRIFT"
    ),
    "root_rows": rows,
    "energy_sign_census": {"positive": positive, "negative": negative},
    "key_result": (
        "five supported roots have positive internal scalar energy, while D_s^-(s=0.09) has negative internal scalar energy. A naive replacement of the common Iter608 K+i0 pole rule by a retarded scalar propagator would therefore introduce a root-dependent prescription/sign."
    ),
    "scope": (
        "this does not invalidate Iter608/615 in their frozen algebraic/Feynman-like pole convention and does not prove the actual CTP measurement uses a retarded scalar line; it proves that the CTP component/branch assignment must be explicit before a one-common-N_native retarded bridge is authoritative"
    ),
    "conditional_retarded_warning": (
        "if all internal scalar lines were mapped to the retarded scalar propagator, a single common multiplicative N_native would not preserve the current six-root sign pattern because one root has opposite internal-energy orientation"
    ),
    "forbidden_shortcuts": [
        "do not flip D_s^-(0.09) by hand",
        "do not keep a common sign by ignoring energy orientation",
        "do not declare Iter615 wrong",
        "do not perform native projection until the combined CTP measurement map specifies the scalar-line component at every retained source family/root"
    ],
    "failures": failures,
    "MODEL_READINESS": "24%",
    "next_gate": (
        "freeze the combined CTP measurement bridge including r/a or +/- contour assignment for each internal scalar source line; only then determine whether the six Iter615 coefficients map by one common N_native or require recomputation in the correct CTP component"
    )
}
print(json.dumps(result, indent=2, sort_keys=True))
if failures:
    raise SystemExit(2)
