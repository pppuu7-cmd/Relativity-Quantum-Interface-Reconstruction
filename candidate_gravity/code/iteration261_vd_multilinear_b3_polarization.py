#!/usr/bin/env python3
import itertools
import json
from pathlib import Path

legs = ("s", "a", "b")
terms = []

# Q0 A3 Q0
terms.append(("Q0", "A3[s,a,b]", "Q0"))

# Q1 A2 Q0 and transpose partner
for x in legs:
    yz = tuple(l for l in legs if l != x)
    terms.append((f"Q1[{x}]", f"A2[{yz[0]},{yz[1]}]", "Q0"))
    terms.append(("Q0", f"A2[{yz[0]},{yz[1]}]", f"Q1[{x}]"))

# Q2 A1 Q0 and transpose partner
for z in legs:
    xy = tuple(l for l in legs if l != z)
    terms.append((f"Q2[{xy[0]},{xy[1]}]", f"A1[{z}]", "Q0"))
    terms.append(("Q0", f"A1[{z}]", f"Q2[{xy[0]},{xy[1]}]"))

# Q1 A1 Q1: left/middle/right slots are distinguished
for x, y, z in itertools.permutations(legs, 3):
    terms.append((f"Q1[{x}]", f"A1[{y}]", f"Q1[{z}]"))

vanishing = [t for t in terms if "A1[s]" in t]
surviving = [t for t in terms if t not in vanishing]

assert len(terms) == 19
assert len(vanishing) == 4
assert len(surviving) == 15

result = {
    "iteration": 261,
    "legs": list(legs),
    "total_polarized_terms": len(terms),
    "vanish_by_null_soft_A1s": len(vanishing),
    "surviving_terms": len(surviving),
    "vanishing_terms": [list(t) for t in vanishing],
    "all_terms": [list(t) for t in terms],
    "status": "PASS_SCOPED_PHYSICAL_B3_MULTILINEAR_POLARIZATION",
    "guardrail": "NO_UNPOLARIZED_SIX_TERM_B3_AS_PHYSICAL_THREE_LEG_NUMERATOR",
    "MODEL_READINESS": "24%"
}

out = Path(__file__).resolve().parents[1] / "results" / "iteration261_vd_multilinear_b3_polarization.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
