#!/usr/bin/env python3
"""Iteration 648: prospective projective closed-Gamma3 ordinary-cut shape gate.

The absolute Iter645 branch is permanently blocked by one common nonzero global
factor lambda.  This gate defines, without inspecting Iter645 values, a homogeneous
projective observable on the already pre-registered above-threshold s grid:

  a(s) = -B_s(s) + T_sab(s) + T_sba(s)
  P_ij = a_i conj(a_j) / sum_k |a_k|^2.

The relative coefficients are the closed Tr-log third-derivative coefficients
already frozen structurally (Iter629): the only ordinary s-cut K1K2 singleton has
coefficient -1, while the two closed K1^3 orientations each have coefficient +1.
K3 has no ordinary finite s-cut.  Therefore P is invariant under one common
lambda in C* and does not require the missing absolute normalization.

The sample grid is inherited from Iter645 code commit
4e578063ab89fe56d3238b6bfceeaddc9461e55c, committed before its canonical Action
produced reduced values.  No sample/component/reference denominator is selected
from observed values.
"""
from __future__ import annotations
import contextlib, io, json, math, runpy, subprocess
from pathlib import Path
import numpy as np

ITERATION = 648
ROOT = Path(__file__).resolve().parents[2]
ITER645_CODE_COMMIT = "4e578063ab89fe56d3238b6bfceeaddc9461e55c"
EXPECTED_GRID = (1.96, 2.0, 2.25, 2.5, 3.0, 4.0)
ABOVE_THRESHOLD_GRID = (2.0, 2.25, 2.5, 3.0, 4.0)

subprocess.check_call(["git", "cat-file", "-e", f"{ITER645_CODE_COMMIT}^{{commit}}"], cwd=ROOT)

# Load the frozen evaluator quietly. run_name avoids executing its main().
with contextlib.redirect_stdout(io.StringIO()):
    m645 = runpy.run_path(
        str(ROOT / "candidate_gravity" / "code" / "iteration645_closed_gamma3_reduced_cut_density.py"),
        run_name="iteration648_import_iter645",
    )

failures = []
if tuple(m645["SAMPLES"]) != EXPECTED_GRID:
    failures.append(f"Iter645 pre-registered grid drift: {tuple(m645['SAMPLES'])}")
if abs(float(m645["THRESH"]) - 1.96) > 2e-15:
    failures.append(f"threshold drift: {m645['THRESH']}")

rows = []
assembled = []
for s in ABOVE_THRESHOLD_GRID:
    r = m645["row_at_s"](s)
    d = r["reduced_Ds_density"]
    # Closed cyclic Tr-log ordinary-s-cut assembly, fixed before value inspection.
    a = -float(d["bubble_K1s_K2ab"]) + float(d["triangle_sab"]) + float(d["triangle_sba"])
    if not math.isfinite(a):
        failures.append(f"non-finite assembled density at s={s}")
    assembled.append(a)
    rows.append({
        "s": s,
        "bubble_K1s_K2ab": float(d["bubble_K1s_K2ab"]),
        "triangle_sab": float(d["triangle_sab"]),
        "triangle_sba": float(d["triangle_sba"]),
        "assembled_reduced_closed_Ds": a,
    })

v = np.asarray(assembled, dtype=np.complex128)
norm2 = float(np.vdot(v, v).real)
projector = None
trace_error = None
hermiticity_error = None
idempotence_error = None
scaling_invariance_error = None

if not math.isfinite(norm2) or norm2 <= 1e-30:
    failures.append(f"projective direction undefined: norm2={norm2}")
else:
    P = np.outer(v, np.conjugate(v)) / norm2
    projector = [[{"re": float(z.real), "im": float(z.imag)} for z in row] for row in P]
    trace_error = float(abs(np.trace(P) - 1.0))
    hermiticity_error = float(np.max(np.abs(P - np.conjugate(P.T))))
    idempotence_error = float(np.max(np.abs(P @ P - P)))

    errs = []
    for lam in (2.0 + 0.0j, -3.0 + 0.0j, 1.0 + 2.0j, -0.25 + 0.75j):
        w = lam * v
        Q = np.outer(w, np.conjugate(w)) / float(np.vdot(w, w).real)
        errs.append(float(np.max(np.abs(Q - P))))
    scaling_invariance_error = max(errs)

    if trace_error > 2e-12:
        failures.append(f"projector trace drift {trace_error}")
    if hermiticity_error > 2e-12:
        failures.append(f"projector hermiticity drift {hermiticity_error}")
    if idempotence_error > 2e-12:
        failures.append(f"projector idempotence drift {idempotence_error}")
    if scaling_invariance_error > 2e-12:
        failures.append(f"global-scaling invariance drift {scaling_invariance_error}")

classification = (
    "PASS_ITER648_PROJECTIVE_CLOSED_GAMMA3_GLOBAL_FACTOR_CANCELLATION__NON_RESIDUAL"
    if not failures else
    "BLOCKED_ITER648_PROJECTIVE_DIRECTION_UNAVAILABLE_OR_VALIDATION_FAILED__NON_RESIDUAL"
)

result = {
    "iteration": ITERATION,
    "date": "2026-09-09",
    "MODEL_READINESS": "24%",
    "readiness_change": "0 percentage points",
    "classification": classification,
    "scientific_gate_pass": not failures,
    "candidate_residual": False,
    "prospective_definition": {
        "iter645_code_commit_pre_result": ITER645_CODE_COMMIT,
        "sample_grid_pre_registered": list(EXPECTED_GRID),
        "projective_grid": list(ABOVE_THRESHOLD_GRID),
        "assembled_density": "a(s)=-bubble_K1s_K2ab+triangle_sab+triangle_sba",
        "projector": "P_ij=a_i*conj(a_j)/sum_k|a_k|^2",
        "algebraic_invariance": "For A->lambda A with one common lambda in C*, numerator and denominator both acquire |lambda|^2, hence P is unchanged.",
        "domain": "defined iff the assembled above-threshold vector is nonzero",
        "reference_component_selected_from_values": False,
    },
    "rows": rows,
    "assembled_vector": assembled,
    "norm2": norm2,
    "projector": projector,
    "validation": {
        "trace_error": trace_error,
        "hermiticity_error": hermiticity_error,
        "idempotence_error": idempotence_error,
        "scaling_invariance_error": scaling_invariance_error,
    },
    "absolute_normalization_status": "PERMANENTLY_BLOCKED_FOR_ABSOLUTE_ITER645_BRANCH__NOT_NEEDED_FOR_THIS_PROJECTIVE_GATE",
    "candidate_values_used": False,
    "zero_fill": False,
    "source_born_subtraction": "NOT_PERFORMED",
    "native_Y_Tcut_projection": "NOT_PERFORMED",
    "comparator_quotient": "NOT_PERFORMED",
    "ANSATZ_003": "FORBIDDEN",
    "Fisher_resources": "FORBIDDEN",
    "failures": failures,
    "next_gate": "Audit whether the matched source/Born subtraction entering native T_cut belongs to the same one-common-factor homogeneous class, so that projectivization can commute with the matched subtraction. Do not perform the subtraction until pole/cut origin and normalization class are explicitly classified.",
}

out = ROOT / "results" / "iteration648_projective_closed_gamma3_shape_gate"
out.mkdir(parents=True, exist_ok=True)
(out / "result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, indent=2, sort_keys=True))
if failures:
    raise SystemExit(2)
