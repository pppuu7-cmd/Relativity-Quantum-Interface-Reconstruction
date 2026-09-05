#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 455.

Deterministic source-order manifest for the frozen Iteration-407 auxiliary-mass
support. This is a provenance/queue audit only. It does not evaluate F(u,v),
does not alter any frozen numerical threshold, and cannot promote physical
index 2.
"""
from __future__ import annotations
import json
from collections import Counter

BASE_H=5e-6
HALF_H=2.5e-6

def nodes(h):
    return [-2*h,-h,h,2*h]

base=[(u,v) for u in nodes(BASE_H) for v in nodes(BASE_H)]
half=[(u,v) for u in nodes(HALF_H) for v in nodes(HALF_H)]
occurrences=[('BASE',i,p) for i,p in enumerate(base)] + [('HALF',i,p) for i,p in enumerate(half)]
counts=Counter(p for _,_,p in occurrences)
first_order=[]
for level,i,p in occurrences:
    if p not in first_order:
        first_order.append(p)

certified={(5e-6,5e-6),(-1e-5,-1e-5)}
active=(-1e-5,-5e-6)
manifest=[]
for rank,p in enumerate(first_order):
    if p in certified:
        state='CERTIFIED'
    elif p==active:
        state='ACTIVE_GATE'
    else:
        state='UNTESTED'
    labels=[{'level':level,'local_index':i} for level,i,q in occurrences if q==p]
    manifest.append({
        'distinct_rank':rank,
        'u':p[0],'v':p[1],
        'source_occurrence_multiplicity':counts[p],
        'source_labels':labels,
        'state':state,
    })

active_rank=first_order.index(active)
next_after_active=first_order[active_rank+1]
result={
    'iteration':455,
    'classification':'PASS_FROZEN_MASS_SUPPORT_SOURCE_ORDER_MANIFEST__NON_PROMOTING',
    'scientific_gate_pass':True,
    'promotes_physical_coordinate':False,
    'MODEL_READINESS':'24%',
    'readiness_change_pp':0,
    'frozen':{
        'base_h':BASE_H,'half_h':HALF_H,
        'central4_node_rule':'[-2h,-h,+h,+2h]',
        'source_order':'BASE 4x4 u-major/v-major, then HALF 4x4 u-major/v-major',
        'occurrence_count':len(occurrences),
        'distinct_coordinate_count':len(first_order),
    },
    'audit':{
        'multiplicity_two_coordinates':[{'u':p[0],'v':p[1]} for p in first_order if counts[p]==2],
        'multiplicity_two_count':sum(1 for p in first_order if counts[p]==2),
        'certified_coordinates':[{'u':p[0],'v':p[1],'multiplicity':counts[p]} for p in first_order if p in certified],
        'certified_occurrence_weight':sum(counts[p] for p in certified),
        'active_coordinate':{'u':active[0],'v':active[1],'distinct_rank':active_rank,'multiplicity':counts[active]},
        'next_coordinate_if_active_passes':{'u':next_after_active[0],'v':next_after_active[1],'distinct_rank':active_rank+1,'multiplicity':counts[next_after_active]},
    },
    'manifest':manifest,
    'guardrails':[
        'NO_FUV_EVALUATION_IN_THIS_ITERATION','NO_ACTIVE_RUN_DUPLICATION',
        'NO_UV_SWAP_DEDUPLICATION','ONLY_EXACT_BASE_HALF_COORDINATE_OVERLAPS_SHARE_CERTIFICATES',
        'NO_THRESHOLD_CHANGE','NO_PHYSICAL_DS_PROMOTION','NO_ANSATZ003','NO_FISHER_RESOURCES'
    ],
    'next_gate':'raw-consume active run 33940931120; if PASS advance only to manifest next_coordinate_if_active_passes'
}
assert len(occurrences)==32
assert len(first_order)==28
assert sum(1 for p in first_order if counts[p]==2)==4
assert sum(counts[p] for p in certified)==3
assert next_after_active==(-1e-5,5e-6)
print(json.dumps(result,indent=2,sort_keys=True))
