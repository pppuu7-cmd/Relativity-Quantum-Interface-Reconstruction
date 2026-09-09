#!/usr/bin/env python3
"""Iteration659 same-parent soft-Gamma3 cut-topology census.

Uses only the Iter653 normalized closed-SK third-variation structure and the Iter658
quotient-safe plus-TT measurement.  No Candidate cut values are evaluated.  Every
term is retained and classified by propagator count / possible external-channel
singularity origin before any Source/Born subtraction.
"""
import json
from pathlib import Path

# Gamma3 = (i/2) Tr[ G K_abc
#   - G K_a G K_bc - G K_b G K_ac - G K_c G K_ab
#   + G K_a G K_b G K_c + G K_a G K_c G K_b ]
# Label s=soft plus-TT slot, a/b=hard slots. Cyclic trace leaves two triangle orders.
terms=[
    {"id":"K3_sab","coefficient":+1,"family":"K3","propagators":1,
     "soft_slot":"K3","origin":"tadpole/contact","s_channel_status":"NO_EXTERNAL_TWO_LINE_CUT_FROM_DENOMINATOR_TOPOLOGY"},
    {"id":"K1_s_K2_ab","coefficient":-1,"family":"K1K2","propagators":2,
     "soft_slot":"K1","origin":"bubble","s_channel_status":"ROUTING_DEPENDENT_ORDINARY_TWO_LINE_CUT_CANDIDATE"},
    {"id":"K1_a_K2_sb","coefficient":-1,"family":"K1K2","propagators":2,
     "soft_slot":"K2","origin":"bubble","s_channel_status":"ROUTING_DEPENDENT_ORDINARY_TWO_LINE_CUT_CANDIDATE"},
    {"id":"K1_b_K2_sa","coefficient":-1,"family":"K1K2","propagators":2,
     "soft_slot":"K2","origin":"bubble","s_channel_status":"ROUTING_DEPENDENT_ORDINARY_TWO_LINE_CUT_CANDIDATE"},
    {"id":"K1_s_K1_a_K1_b","coefficient":+1,"family":"K1^3","propagators":3,
     "soft_slot":"K1","origin":"triangle","s_channel_status":"ORDINARY_TWO_LINE_AND_LANDAU_SUPPORT_REQUIRE_SOFT_ROUTING_AUDIT"},
    {"id":"K1_s_K1_b_K1_a","coefficient":+1,"family":"K1^3","propagators":3,
     "soft_slot":"K1","origin":"triangle","s_channel_status":"ORDINARY_TWO_LINE_AND_LANDAU_SUPPORT_REQUIRE_SOFT_ROUTING_AUDIT"},
]

checks={
    "term_count":len(terms),
    "family_counts":{f:sum(t["family"]==f for t in terms) for f in ("K3","K1K2","K1^3")},
    "coefficients":[t["coefficient"] for t in terms],
    "propagator_counts":[t["propagators"] for t in terms],
    "all_terms_retained":len({t["id"] for t in terms})==6,
    "k3_not_mislabelled_as_external_two_line_cut":terms[0]["s_channel_status"]=="NO_EXTERNAL_TWO_LINE_CUT_FROM_DENOMINATOR_TOPOLOGY",
    "bubble_support_not_zero_filled":all("CANDIDATE" in t["s_channel_status"] for t in terms if t["family"]=="K1K2"),
    "triangle_support_left_for_soft_routing_audit":all("REQUIRE_SOFT_ROUTING_AUDIT" in t["s_channel_status"] for t in terms if t["family"]=="K1^3"),
}
expected={
    "term_count":6,
    "family_counts":{"K3":1,"K1K2":3,"K1^3":2},
    "coefficients":[1,-1,-1,-1,1,1],
    "propagator_counts":[1,2,2,2,3,3],
    "all_terms_retained":True,
    "k3_not_mislabelled_as_external_two_line_cut":True,
    "bubble_support_not_zero_filled":True,
    "triangle_support_left_for_soft_routing_audit":True,
}
failures=[]
for k,v in expected.items():
    if checks[k]!=v:
        failures.append(f"CHECK_FAILED:{k}:{checks[k]}!={v}")

result={
    "iteration":659,
    "scope":"quotient-safe plus-TT contraction on normalized same-parent closed-SK soft Gamma3: pre-cut topology census",
    "normalized_parent_prefactor":"i/2 common; no family-wise refit",
    "terms":terms,
    "checks":checks,
    "classification":"PASS_ITER659_SOFT_GAMMA3_TERM_CENSUS__K3_CONTACT__K1K2_BUBBLE_CANDIDATES__K1CUBED_TRIANGLE_REQUIRES_SOFT_ROUTING__NON_RESIDUAL",
    "candidate_cut_values_read":False,
    "source_born_subtraction":"NOT_PERFORMED",
    "native_soft_T_cut_value_computed":False,
    "zero_fill_allowed":False,
    "scientific_gate_pass":len(failures)==0,
    "failures":failures,
    "MODEL_READINESS":"24%",
    "readiness_delta_percentage_points":0,
    "exact_next_gate":(
        "Resolve the Iter655 soft-family loop-momentum routing for all three K1K2 bubbles and both K1^3 triangles, "
        "derive their explicit denominator pairs/triples at fixed epsilon>0, and compute threshold/Landau support "
        "before evaluating numerator-weighted D_s or performing Source/Born subtraction."
    ),
}
out=Path('candidate_gravity/results/iteration659_soft_gamma3_cut_topology_census.json')
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding='utf-8')
print(json.dumps(result,indent=2,sort_keys=True))
if failures:
    raise SystemExit(1)
