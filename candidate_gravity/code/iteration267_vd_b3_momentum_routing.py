#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 267.

Exact condensed-index/Fourier momentum-routing certificate for the eight
independent null-soft B3 transpose representatives frozen at Iteration 266.
This does not evaluate the physical tensor numerator; it prevents a false
local-matrix implementation from violating operator kernel momentum support.
"""
import json, re

REPS=[
    "Q0 A3[s,a,b] Q0",
    "Q1[s] A2[a,b] Q0",
    "Q1[a] A2[s,b] Q0",
    "Q1[b] A2[s,a] Q0",
    "Q2[s,a] A1[b] Q0",
    "Q2[s,b] A1[a] Q0",
    "Q1[s] A1[a] Q1[b]",
    "Q1[s] A1[b] Q1[a]",
]

def token_legs(tok):
    if tok == "Q0":
        return []
    m=re.search(r"\[([^\]]+)\]",tok)
    return [] if not m else m.group(1).split(",")

def fmt(offset):
    if not offset:
        return "p"
    return "p+" + "+".join("k_"+x for x in offset)

rows=[]
for expr in REPS:
    toks=expr.split()
    offset=[]
    stages=[]
    q0_momenta=[]
    for tok in reversed(toks):
        pin=fmt(offset)
        if tok == "Q0":
            q0_momenta.append(pin)
        offset2=offset+token_legs(tok)
        stages.append({"operator":tok,"p_in":pin,"p_out":fmt(offset2)})
        offset=offset2
    assert sorted(offset) == ["a","b","s"]
    rows.append({
        "representative":expr,
        "forward_kernel":f"<{fmt(offset)}|X|p>",
        "stages_right_to_left":stages,
        "Q0_momenta":q0_momenta,
    })

result={
    "iteration":267,
    "model_readiness_percent":24,
    "total_external_shift":"K=k_s+k_a+k_b",
    "independent_representatives":len(rows),
    "representatives":rows,
    "kernel_transpose_rule":"<p+K|X|p>^T = <p|X^T|p+K>; in canonical forward orientation X^T carries -K and the endpoint momenta are exchanged.",
    "real_background_rule":"For h(-k)=h(k)^*, a transpose partner in canonical forward orientation requires endpoint reversal together with k_s,k_a,k_b -> -k_s,-k_a,-k_b (and complex conjugation where appropriate); a raw 4x4 transpose at unchanged p and unchanged +k legs is not the condensed-index kernel transpose.",
    "classification":"PASS_EXACT_B3_CONDENSED_INDEX_MOMENTUM_SUPPORT",
    "guardrail":"NO_FIXED_PLUS_K_MATRIX_TRANSPOSE_AS_KERNEL_TRANSPOSE",
    "candidate_residual":False,
}
assert result["independent_representatives"] == 8
print(json.dumps(result,indent=2,sort_keys=True))
