#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 411.

Apply the already-frozen Iteration-407 analytic/spectral physical reduction
separately to the only remaining Tr(U1^2) double-double blockers, indices 2 and
11, after raw structural PASS of Iteration 410.

Scientific arithmetic is inherited from Iteration 407 by a fail-closed source
specialization: only iteration id, target index, target identity assertion, and
human-readable CHANNEL4 labels are specialized. The parent physical integrand,
central4 x central4 mass stencil, sign/normalization, held-out original-integrand
cross-checks, and all thresholds remain unchanged.
"""
from __future__ import annotations
import os
from pathlib import Path

ITERATION = 411
TARGET = int(os.environ.get("RQIR_TARGET_INDEX", "-1"))
EXPECTED = {
    2: (3, -1.0),
    11: (16, -0.34),
}
if TARGET not in EXPECTED:
    raise RuntimeError(("unsupported_iteration411_target", TARGET))
expected_class, expected_q2 = EXPECTED[TARGET]

root = Path(__file__).resolve().parent
parent = root / "iteration407_tru1sq_channel4_analytic_spectral_reduction.py"
src = parent.read_text()

replacements = [
    ("ITERATION=407", "ITERATION=411"),
    ("TARGET_INDEX=4", f"TARGET_INDEX={TARGET}"),
    (
        "if int(ch['class_id'])!=5 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))",
        f"if int(ch['class_id'])!={expected_class} or abs(q2-({expected_q2!r}))>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))",
    ),
    ("CHANNEL4", f"CHANNEL{TARGET}"),
    ("channel-4", f"channel-{TARGET}"),
    ("channel 4", f"channel {TARGET}"),
    ("index 4", f"index {TARGET}"),
]

for old, new in replacements[:3]:
    if src.count(old) != 1:
        raise RuntimeError(("iteration407_specialization_drift", old, src.count(old)))
    src = src.replace(old, new, 1)
for old, new in replacements[3:]:
    src = src.replace(old, new)

# The specialized Iteration-407 program prints the scientific JSON and exits
# nonzero only if its unchanged execution-validity checks fail.
ns = {
    "__name__": "__main__",
    "__file__": str(parent),
}
exec(compile(src, str(parent), "exec"), ns, ns)
