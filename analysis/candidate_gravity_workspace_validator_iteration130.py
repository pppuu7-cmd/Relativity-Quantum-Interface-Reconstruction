#!/usr/bin/env python3
"""RQIR Iteration 130 — structural validator for Candidate Gravity workspace.

This validator intentionally checks infrastructure, not physical truth. A PASS means
that the repository has the mandatory templates/contracts required to start a model;
it does not pass QG-001...QG-010 for any concrete candidate.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "candidate_gravity/README.md": ["Model lifecycle", "ANSATZ", "QGxxx"],
    "candidate_gravity/MODEL_SPEC_TEMPLATE.md": ["Physical state space", "Dynamics", "Required limits", "Falsification"],
    "candidate_gravity/MODEL_TO_RQIR_CONTRACT.md": ["Source hierarchy", "Paper I contract", "Paper II contract", "Paper III contract"],
    "candidate_gravity/GATE_STATUS_TEMPLATE.yaml": ["QG-001", "QG-010", "PASS", "BLOCKED"],
    "candidate_gravity/BASELINE_COMPARATORS.md": ["C0", "C1", "C2", "C3", "C5", "Decision rule"],
    "candidate_gravity/ASSUMPTIONS_LEDGER_TEMPLATE.md": ["Assumption", "SUPERSEDED", "renormalization"],
    "candidate_gravity/DERIVATION_MAP_TEMPLATE.md": ["Dynamics", "source hierarchy", "F_beta|theta", "Failure provenance"],
}


def main() -> None:
    failures = []
    for rel, tokens in REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            failures.append(f"missing {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                failures.append(f"{rel}: missing token {token!r}")

    gate = (ROOT / "candidate_gravity/GATE_STATUS_TEMPLATE.yaml").read_text(encoding="utf-8")
    for i in range(1, 11):
        key = f"QG-{i:03d}:"
        if gate.count(key) != 1:
            failures.append(f"gate template must contain exactly one {key}")

    if failures:
        print("Candidate Gravity workspace validator: FAIL")
        for failure in failures:
            print(" -", failure)
        raise SystemExit(1)

    print("Candidate Gravity workspace validator: PASS")
    print(f"checked {len(REQUIRED)} canonical infrastructure files and QG-001...QG-010 uniqueness")


if __name__ == "__main__":
    main()
