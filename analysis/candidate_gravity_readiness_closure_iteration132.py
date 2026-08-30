#!/usr/bin/env python3
"""RQIR Iteration 132 — Candidate Gravity repository-readiness closure audit.

A PASS certifies that the process/infrastructure needed to START a concrete model is
present. It does not certify any physical Candidate Gravity model or any QG gate.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "candidate_gravity/README.md",
    "candidate_gravity/MODEL_SPEC_TEMPLATE.md",
    "candidate_gravity/MODEL_TO_RQIR_CONTRACT.md",
    "candidate_gravity/GATE_STATUS_TEMPLATE.yaml",
    "candidate_gravity/BASELINE_COMPARATORS.md",
    "candidate_gravity/ASSUMPTIONS_LEDGER_TEMPLATE.md",
    "candidate_gravity/DERIVATION_MAP_TEMPLATE.md",
    "candidate_gravity/MODEL_REGISTRY.md",
    "candidate_gravity/NEW_MODEL_CHECKLIST.md",
    "candidate_gravity/recovery/CURRENT_QG_FRONT.md",
    "candidate_gravity/recovery/RECOVERY_GUIDE.md",
    "docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md",
    "docs/PAPER_I_SCIENTIFIC_CLOSURE_ITERATION078.md",
    "docs/PAPER_II_REFERENCE_LIKELIHOOD_CERTIFICATE_ITERATION079.md",
    "docs/PAPER_III_SCIENTIFIC_CLOSURE_ITERATION128.md",
]

TOKEN_CHECKS = {
    "candidate_gravity/MODEL_TO_RQIR_CONTRACT.md": ["same declared model dynamics", "Paper I contract", "Paper II contract", "Paper III contract"],
    "candidate_gravity/GATE_STATUS_TEMPLATE.yaml": ["QG-001:", "QG-010:", "PASS", "FAIL", "BLOCKED", "promotion_rules"],
    "candidate_gravity/BASELINE_COMPARATORS.md": ["C0", "C1", "C2", "C3", "C5", "C6"],
    "candidate_gravity/recovery/RECOVERY_GUIDE.md": ["FAIL is retained", "model dynamics -> J,N,chi^R", "RTK and DSIR remain separate"],
    "candidate_gravity/NEW_MODEL_CHECKLIST.md": ["ANSATZ", "QG-001", "QG-002", "Paper-I discriminator", "Paper-II profiled", "Paper-III physical resources"],
    "docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md": ["Papers I–III are scientifically closed", "QG-001", "QG-010", "Promotion rule"],
}


def main() -> None:
    failures = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            failures.append(f"missing required authority: {rel}")

    for rel, tokens in TOKEN_CHECKS.items():
        path = ROOT / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                failures.append(f"{rel}: missing required token {token!r}")

    gate_path = ROOT / "candidate_gravity/GATE_STATUS_TEMPLATE.yaml"
    if gate_path.is_file():
        gate_text = gate_path.read_text(encoding="utf-8")
        for i in range(1, 11):
            key = f"QG-{i:03d}:"
            if gate_text.count(key) != 1:
                failures.append(f"expected exactly one gate label {key}")

    registry = ROOT / "candidate_gravity/MODEL_REGISTRY.md"
    if registry.is_file():
        text = registry.read_text(encoding="utf-8")
        if "no concrete model instantiated yet" not in text.lower():
            failures.append("closure must occur before a concrete model is instantiated")

    if failures:
        print("Candidate Gravity readiness closure: FAIL")
        for f in failures:
            print(" -", f)
        raise SystemExit(1)

    print("Candidate Gravity readiness closure: PASS")
    print(f"required authorities checked: {len(REQUIRED)}")
    print("QG gate labels checked: 10")
    print("meaning: repository infrastructure ready to START a model; no physical model gate is passed")


if __name__ == "__main__":
    main()
