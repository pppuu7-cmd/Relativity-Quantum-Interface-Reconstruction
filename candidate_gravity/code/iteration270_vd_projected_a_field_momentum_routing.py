#!/usr/bin/env python3
"""Iteration 270: exact projected A=K E field-momentum routing certificate.

This is a bookkeeping/routing certificate, not a numerical Vilkovisky vertex
evaluation. It enforces translational support for the contracted field-space
index j in A_{gamma delta}=K^j_{gamma delta} E_j before B3 assembly.
"""
import json

LEGS=("s","a","b")

def Ksum(xs):
    return "+".join(xs) if xs else "0"

A_TERMS={
 "A1[s]":[((),("s",))],
 "A1[a]":[((),("a",))],
 "A1[b]":[((),("b",))],
 "A2[s,a]":[((),("s","a")),(("s",),("a",)),(("a",),("s",))],
 "A2[s,b]":[((),("s","b")),(("s",),("b",)),(("b",),("s",))],
 "A2[a,b]":[((),("a","b")),(("a",),("b",)),(("b",),("a",))],
 "A3[s,a,b]":[
   ((),("s","a","b")),
   (("s",),("a","b")),(("a",),("s","b")),(("b",),("s","a")),
   (("s","a"),("b",)),(("s","b"),("a",)),(("a","b"),("s",))
 ],
}

def survives(S,T):
    return T != ("s",)

routing={}
for A,terms in A_TERMS.items():
    alllegs=A[A.index("[")+1:A.index("]")].split(",")
    entries=[]
    for S,T in terms:
        assert sorted(S+T)==sorted(alllegs)
        entries.append({
          "K_background_legs":list(S),
          "E_legs":list(T),
          "K_background_shift":Ksum(S),
          "contracted_E_momentum":Ksum(T),
          "required_orbit_endpoint_shift":Ksum(S+T),
          "survives_nullsoft":survives(S,T),
        })
    routing[A]=entries

assert sum(e["survives_nullsoft"] for e in routing["A3[s,a,b]"]) == 6
assert sum(e["survives_nullsoft"] for e in routing["A2[s,a]"]) == 2
assert sum(e["survives_nullsoft"] for e in routing["A2[s,b]"]) == 2
assert sum(e["survives_nullsoft"] for e in routing["A2[a,b]"]) == 3
assert sum(e["survives_nullsoft"] for e in routing["A1[s]"]) == 0

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

result={
 "iteration":270,
 "scope":"exact condensed-index/Fourier support bookkeeping for projected A=K E before numerical K/A evaluation",
 "fourier_convention":"background insertions add to orbit endpoint shift, consistent with Iteration 267 p_out=p_in+K_total",
 "identity":"A_{gamma delta}=K^j_{gamma delta} E_j",
 "routing_rule":"for term K_m[S] E_n[T], p_out-p_in = k_S + q_j with q_j=k_T; after contraction this is k_S+k_T",
 "critical_consequence":"K_m cannot be represented as a single-momentum orbit matrix depending only on its explicit background subset S before contraction with E[T]; the contracted field/EOM momentum q_j must remain an explicit routing label",
 "nullsoft_A3_survivors":6,
 "A_routing":routing,
 "B3_forward_representatives":REPS,
 "B3_total_support":"k_s+k_a+k_b",
 "status":[
   "PASS_EXACT_PROJECTED_A_CONTRACTED_FIELD_MOMENTUM_ROUTING",
   "NO_DROP_CONTRACTED_EOM_MOMENTUM_IN_K_KERNEL",
   "NO_PREMATURE_LOCAL_MATRIX_K_TIMES_E_AS_PHYSICAL_A"
 ],
 "classification":"implementation/provenance gate; not a consistency FAIL and not a Candidate Gravity residual"
}
print(json.dumps(result,indent=2,sort_keys=True))
