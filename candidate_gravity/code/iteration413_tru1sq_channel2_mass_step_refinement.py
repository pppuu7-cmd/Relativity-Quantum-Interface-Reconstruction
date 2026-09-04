#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 413.

Prospectively freeze one numerical mass-step refinement for the sole remaining
Tr(U1^2) double-double physical blocker, global index 2 / class 3 / q^2=-1,
after Iteration 411 passed all structural/direct-integrand checks but failed the
unchanged 2e-5 mass-step convergence gate.

This is NOT angular-grid escalation and does not weaken any threshold.  It uses
the exact Iteration-407/411 analytic/spectral integrand, central4 x central4
stencil, sign and normalization, but evaluates the next single halving pair
h=2.5e-6 and h/2=1.25e-6.  The coarser value is exactly the half-step scale of
Iteration 411, providing a deterministic continuation rather than a new fit.
"""
from __future__ import annotations
from pathlib import Path

ITERATION = 413
TARGET = 2
EXPECTED_CLASS = 3
EXPECTED_Q2 = -1.0
REFINED_BASE_H = 2.5e-6
REFINED_HALF_H = 1.25e-6

root = Path(__file__).resolve().parent
parent = root / "iteration407_tru1sq_channel4_analytic_spectral_reduction.py"
src = parent.read_text()

# Fail closed on parent-source drift before specialization.
required = [
    ("ITERATION=407", "ITERATION=413"),
    ("TARGET_INDEX=4", "TARGET_INDEX=2"),
    (
        "if int(ch['class_id'])!=5 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))",
        "if int(ch['class_id'])!=3 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))",
    ),
]
for old, new in required:
    if src.count(old) != 1:
        raise RuntimeError(("iteration407_specialization_drift", old, src.count(old)))
    src = src.replace(old, new, 1)

anchor = "P372=ns['P372']; rows=ns['rows']; vk=ns['vk']; mdot=ns['mdot']; BASE_H=ns['BASE_H']; HALF_H=ns['HALF_H']"
if src.count(anchor) != 1:
    raise RuntimeError(("iteration407_mass_step_anchor_drift", src.count(anchor)))
replacement = anchor + "\nif abs(BASE_H-5e-6)>1e-18 or abs(HALF_H-2.5e-6)>1e-18: raise RuntimeError(('parent_mass_step_drift',BASE_H,HALF_H))\nBASE_H=2.5e-6; HALF_H=1.25e-6"
src = src.replace(anchor, replacement, 1)

for old, new in [
    ("CHANNEL4", "CHANNEL2"),
    ("channel-4", "channel-2"),
    ("channel 4", "channel 2"),
    ("index 4", "index 2"),
    ("ITERATION401_STRUCTURE_PASS_REQUIRED", "ITERATION410_INDEX2_STRUCTURE_PASS_REQUIRED"),
]:
    src = src.replace(old, new)

old_next = "if CONVERGED and raw authority audit passes, replace only double-double blocker index 2 and apply the same prospectively frozen analytic/spectral architecture separately to unresolved indices 2 and 11 with their own held-out checks; if BLOCKED, preserve it and diagnose the failed fixed-mass representation or mass-step convergence without weakening thresholds"
new_next = "if CONVERGED and raw authority audit passes, remove only blocker index 2 and unlock frozen Iteration-412 exact15 assembly; if BLOCKED, preserve index 2 and move to a dedicated auxiliary-mass derivative representation/error analysis without threshold weakening or angular-grid escalation"
src = src.replace(old_next, new_next)

ns = {"__name__": "__main__", "__file__": str(parent)}
exec(compile(src, str(parent), "exec"), ns, ns)
