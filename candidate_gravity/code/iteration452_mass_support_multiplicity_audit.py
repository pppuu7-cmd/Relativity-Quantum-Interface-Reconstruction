#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 452.

Audit the frozen Iteration-407 mixed-mass support without changing any physical
or numerical gate. The two central4 x central4 evaluations use BASE_H=5e-6 and
HALF_H=2.5e-6. Each has 16 source occurrences, but their coordinate sets overlap.

This script distinguishes source occurrences from distinct F(u,v) coordinates,
so future precision-provenance bookkeeping does not duplicate exact same-mass
sample calculations or misstate coverage. No physical D_s is evaluated here.
"""
from __future__ import annotations
import json

BASE_H=5e-6
HALF_H=2.5e-6
TRAIN_Z=(-0.86,-0.43,0.0,0.43,0.86)
NPHI=16


def nodes(h):
    return (-2*h,-h,h,2*h)


def grid(h,label):
    return [
        {'stencil':label,'i':i,'j':j,'u':u,'v':v}
        for i,u in enumerate(nodes(h))
        for j,v in enumerate(nodes(h))
    ]

base=grid(BASE_H,'BASE')
half=grid(HALF_H,'HALF')
all_occ=base+half
coords=[(r['u'],r['v']) for r in all_occ]
unique=sorted(set(coords))
overlap=sorted(set((r['u'],r['v']) for r in base) & set((r['u'],r['v']) for r in half))
mult={}
for uv in coords:
    mult[uv]=mult.get(uv,0)+1

assert len(base)==16 and len(half)==16 and len(all_occ)==32
assert len(unique)==28
assert len(overlap)==4
assert all(mult[x]==2 for x in overlap)
assert all(mult[x]==1 for x in unique if x not in overlap)

# Iteration 450 closed full z/phi/radial precision provenance at (+5e-6,+5e-6).
# That coordinate appears once in BASE and once in HALF, while F(u,v) itself is
# evaluated by the same mass-only sample path. Therefore one exact-coordinate
# certificate can satisfy both source occurrences without changing a threshold.
closed_uv=(5e-6,5e-6)
closed_occurrences=mult[closed_uv]
rows_per_coordinate=len(TRAIN_Z)*NPHI

result={
 'iteration':452,
 'classification':'PASS_MASS_SUPPORT_SOURCE_OCCURRENCE_MULTIPLICITY_AUDIT__NON_PROMOTING',
 'scientific_gate_pass':True,
 'promotes_physical_coordinate':False,
 'MODEL_READINESS':'24%',
 'readiness_change_pp':0,
 'frozen':{
   'base_h':BASE_H,'half_h':HALF_H,
   'nodes_rule':'[-2h,-h,+h,+2h] nested u-major then v-major',
   'training_z':list(TRAIN_Z),'phi_nodes':NPHI
 },
 'support':{
   'source_occurrence_count':len(all_occ),
   'distinct_mass_coordinate_count':len(unique),
   'overlap_coordinate_count':len(overlap),
   'overlap_coordinates':[list(x) for x in overlap],
   'source_occurrences':all_occ,
   'distinct_coordinates':[list(x) for x in unique]
 },
 'coverage_semantics':{
   'rows_per_distinct_mass_coordinate':rows_per_coordinate,
   'frozen_occurrence_denominator_rows':32*rows_per_coordinate,
   'distinct_coordinate_denominator_rows':28*rows_per_coordinate,
   'iteration450_closed_coordinate':list(closed_uv),
   'iteration450_source_occurrences_covered_by_same_coordinate_certificate':closed_occurrences,
   'iteration450_occurrence_weighted_rows_covered':closed_occurrences*rows_per_coordinate,
   'iteration450_occurrence_weighted_fraction':closed_occurrences/32,
   'iteration450_distinct_coordinate_fraction':1/28,
   'note':'The existing 32-occurrence frozen denominator is retained. Distinct-coordinate accounting is an auxiliary deduplication view, not a weakened gate.'
 },
 'active_gate_guard':{
   'run':'33935454815','coordinate':[-1e-5,-1e-5],
   'source_occurrence_multiplicity':mult[(-1e-5,-1e-5)],
   'do_not_duplicate':True
 },
 'next_source_order_coordinate_if_active_passes':[-1e-5,-5e-6],
 'guardrails':['NO_THRESHOLD_CHANGE','NO_STENCIL_CHANGE','NO_PHYSICAL_DS_PROMOTION','NO_DUPLICATE_ACTIVE_RUN','KEEP_32_SOURCE_OCCURRENCE_DENOMINATOR','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
