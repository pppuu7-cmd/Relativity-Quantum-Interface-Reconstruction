#!/usr/bin/env python3
"""RQIR Iteration 133: structural gate audit for ANSATZ-PQG-EFT-001.

This script does not claim to prove perturbative quantum gravity. It checks the
repository-level logic frozen before the first model: QG-001/QG-002 are supplied,
and a model declared identical to comparator C5 must fail QG-007 novelty.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "candidate_gravity/models/ANSATZ-PQG-EFT-001/MODEL.md"
GATES = ROOT / "candidate_gravity/models/ANSATZ-PQG-EFT-001/GATE_STATUS.yaml"
ASSUMPTIONS = ROOT / "candidate_gravity/models/ANSATZ-PQG-EFT-001/ASSUMPTIONS_LEDGER.md"
DERIVATIONS = ROOT / "candidate_gravity/models/ANSATZ-PQG-EFT-001/DERIVATION_MAP.md"
COMPARATORS = ROOT / "candidate_gravity/BASELINE_COMPARATORS.md"

for p in (MODEL, GATES, ASSUMPTIONS, DERIVATIONS, COMPARATORS):
    assert p.exists(), f"missing authority: {p.relative_to(ROOT)}"

model = MODEL.read_text(encoding="utf-8")
gates = GATES.read_text(encoding="utf-8")
comparators = COMPARATORS.read_text(encoding="utf-8")

# Core model-definition checks.
for token in ("g_mn = eta_mn + kappa h_mn", "Einstein-Hilbert", "scalar", "S_int^(1)", "J_mn", "N_mn,ab", "chi^R_mn,ab"):
    assert token in model, f"missing model token: {token}"

# Gate-state checks.
assert re.search(r"QG-001:\s*\n\s*status: PASS", gates)
assert re.search(r"QG-002:\s*\n\s*status: PASS", gates)
assert re.search(r"QG-007:\s*\n\s*status: FAIL", gates)
assert "REFERENCE_DEGENERACY_C5" in gates
assert "promotion_allowed: false" in gates

# Comparator-registry check: C5 must exist as a declared comparator class.
assert "C5" in comparators and ("perturbative" in comparators.lower() or "quantum gravity" in comparators.lower())

# Logical negative result: identical theory class has zero independent class label.
# Encode beta as difference in class indicator between ansatz and C5.
class_indicator_ansatz = 1
class_indicator_c5 = 1
beta_class = class_indicator_ansatz - class_indicator_c5
assert beta_class == 0

print("Iteration 133 structural audit: PASS")
print("QG-001: PASS")
print("QG-002: PASS")
print("QG-007: FAIL (exact reference degeneracy with C5)")
print("promotion_allowed: false")
