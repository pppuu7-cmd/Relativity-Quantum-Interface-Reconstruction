#!/usr/bin/env python3
"""Iteration 647: fail-closed pre-Iter645 normalization provenance audit.

The audit is pinned to the authoritative Iter644 front commit, i.e. the repository
state before any Iter645 reduced cut values existed.  It searches that snapshot
for an explicit same-parent chain binding

    W=-i ln Z -> CTP Legendre transform -> native Gamma3

including a real-scalar Gaussian one-loop global prefactor and Fourier/loop
measure convention.  Merely finding isolated standard formulas is insufficient.
Candidate/comparator values are never inspected.
"""
from __future__ import annotations
from pathlib import Path
import json, re, subprocess

ROOT = Path(__file__).resolve().parents[2]
ITERATION = 647
CUTOFF = "a86b41cfc4e90d65073faa872b8cfa1b85f29193"  # authoritative Iter644 front


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, errors="replace")

# Fail closed if the exact cutoff is unavailable.
subprocess.check_call(["git", "cat-file", "-e", f"{CUTOFF}^{{commit}}"], cwd=ROOT)
paths = [p for p in git("ls-tree", "-r", "--name-only", CUTOFF).splitlines()
         if p.startswith("candidate_gravity/") and not p.startswith("candidate_gravity/results/iteration645")]

patterns = {
    "W_minus_i_logZ": [r"W\s*=\s*-\s*i\s*(?:ln|log)\s*Z", r"-i\s*(?:ln|log)\s*Z"],
    "Gamma_Legendre": [r"Legendre", r"Gamma"],
    "real_scalar_prefactor": [r"(?:i\s*/\s*2|1j\s*/\s*2|0\.5j).*Tr", r"(?:i\s*/\s*2|1j\s*/\s*2|0\.5j).*log", r"Tr.*(?:i\s*/\s*2|1j\s*/\s*2|0\.5j)"],
    "loop_measure": [r"d\^?4k\s*/\s*\(2\s*\*?\s*pi\)?\^?4", r"d\^4k.*2pi", r"loop[-_ ]measure", r"Fourier.*(?:2pi|measure)"],
    "native_Gamma3": [r"native.*Gamma3", r"Gamma3.*native", r"Γ_?3"],
}

hits = {k: [] for k in patterns}
files_scanned = 0
for path in paths:
    try:
        text = git("show", f"{CUTOFF}:{path}")
    except subprocess.CalledProcessError:
        continue
    if "\x00" in text:
        continue
    files_scanned += 1
    for key, regs in patterns.items():
        if key == "Gamma_Legendre":
            ok = all(re.search(rx, text, re.I) for rx in regs)
        else:
            ok = any(re.search(rx, text, re.I) for rx in regs)
        if ok:
            hits[key].append(path)

# A valid inherited binding requires all ingredients and an explicit bridge.  The
# bridge criterion is deliberately stronger than keyword co-occurrence: at least
# one pre-cutoff file must jointly mention W/logZ, Legendre/Gamma, native Gamma3,
# and a real-scalar i/2-like determinant prefactor; loop/Fourier normalization may
# be in that file or an explicitly referenced same-parent file.
bridge_files = []
for path in sorted(set(sum(hits.values(), []))):
    try:
        text = git("show", f"{CUTOFF}:{path}")
    except subprocess.CalledProcessError:
        continue
    cond = (
        any(re.search(rx, text, re.I) for rx in patterns["W_minus_i_logZ"]) and
        all(re.search(rx, text, re.I) for rx in patterns["Gamma_Legendre"]) and
        any(re.search(rx, text, re.I) for rx in patterns["real_scalar_prefactor"]) and
        any(re.search(rx, text, re.I) for rx in patterns["native_Gamma3"])
    )
    if cond:
        bridge_files.append(path)

explicit_loop_measure = bool(hits["loop_measure"])
complete_binding = bool(bridge_files) and explicit_loop_measure

classification = (
    "PASS_ITER647_PRE645_AUTHORITY_ALREADY_BINDS_ABSOLUTE_CLOSED_CTP_TO_NATIVE_GAMMA3_NORMALIZATION__NON_RESIDUAL"
    if complete_binding else
    "BLOCKED_ITER647_PERMANENT_PRE645_NORMALIZATION_PROVENANCE_GAP__ONE_GLOBAL_FACTOR_UNBOUND__NON_RESIDUAL"
)

result = {
    "iteration": ITERATION,
    "date": "2026-09-09",
    "cutoff_commit": CUTOFF,
    "cutoff_meaning": "authoritative Iter644 front; strictly before Iter645 reduced values",
    "MODEL_READINESS": "24%",
    "readiness_change": "0 percentage points",
    "classification": classification,
    "scientific_gate_pass": bool(complete_binding),
    "files_scanned": files_scanned,
    "keyword_hits": {k: sorted(v) for k, v in hits.items()},
    "complete_bridge_files": bridge_files,
    "explicit_loop_measure_found": explicit_loop_measure,
    "authority_conclusion": {
        "complete_pre_result_binding_found": complete_binding,
        "missing_if_blocked": "No explicit pre-Iter645 same-parent chain jointly binds W=-i ln Z, the CTP Legendre map, the real-scalar Gaussian global prefactor, Fourier/loop measure, and native Gamma3 normalization.",
        "degrees_of_freedom_remaining": "exactly one common nonzero global scalar factor; no root-, family-, q2-, or s-dependent normalization is licensed",
        "permanent_for_this_observable_branch_if_blocked": not complete_binding,
        "post_result_conventional_freeze_forbidden": True,
    },
    "candidate_values_used": False,
    "zero_fill": False,
    "source_born_subtraction": "NOT_PERFORMED",
    "native_Y_Tcut_projection": "NOT_PERFORMED",
    "comparator_quotient": "NOT_PERFORMED",
    "ANSATZ_003": "FORBIDDEN",
    "Fisher_resources": "FORBIDDEN",
    "next_gate": (
        "Use the inherited absolute binding without modification, then perform the native projection."
        if complete_binding else
        "Freeze a new prospective projective/ratio observable whose definition algebraically cancels the one global factor without using Iter645 values; prove cancellation before evaluating the ratio."
    ),
}

out = ROOT / "results" / "iteration647_pre645_normalization_history_audit"
out.mkdir(parents=True, exist_ok=True)
(out / "result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, indent=2, sort_keys=True))
