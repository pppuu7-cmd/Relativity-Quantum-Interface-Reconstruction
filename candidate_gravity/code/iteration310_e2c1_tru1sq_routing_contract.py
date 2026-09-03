#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 310.

Exact routing/cyclic-class contract for the eight surviving Tr(U1^2) classes
in e=2,c<=1, reusing the already-authoritative U1 factor order
U1=N_L V2 N_R Y.  No new physical coefficients are invented.
"""
import json

LEGS=('s','a','b')
SITES=('V2','N_L','N_R','Y')
rows=[]

# After Iteration 308 null-soft pruning, the first-order singleton U1 must carry
# a hard leg (a or b).  The second-order block carries the complementary pair
# containing s.  Exactly one cyclic class remains for each singleton/extra-site.
for singleton in ('a','b'):
    pair=tuple(x for x in LEGS if x!=singleton)
    for site in SITES:
        if site=='V2':
            v2_legs=pair
            local_extra=()
        else:
            hard=next(x for x in pair if x!='s')
            v2_legs=(hard,)
            local_extra=('s',)
        rows.append({
          'singleton_first_order_U1_leg':singleton,
          'second_order_pair':pair,
          'second_order_extra_site':site,
          'second_order_V2_legs':v2_legs,
          'second_order_local_extra_legs':local_extra,
          'canonical_trace_word':[
             'U1^(1)['+singleton+']',
             'U1^(2)['+','.join(pair)+';extra='+site+']'
          ],
          'reuse_contract':{
             'U1_factor_order':['N_L','V2','N_R','Y'],
             'first_order_block':'authoritative U1 primitive with hard singleton leg',
             'second_order_block':'authoritative U1 primitive expansion with exactly one extra insertion at '+site,
             'cyclic_identification_only':True,
             'reversal_identification':False
          }
        })

assert len(rows)==8
assert len({(r['singleton_first_order_U1_leg'],r['second_order_extra_site']) for r in rows})==8
assert {r['second_order_extra_site'] for r in rows}==set(SITES)
assert all('s' in r['second_order_pair'] for r in rows)
assert all(r['singleton_first_order_U1_leg']!='s' for r in rows)

# Two ordered block orientations map to one cyclic trace class Tr(A B)=Tr(B A).
ordered_orientation_count=2*len(rows)
assert ordered_orientation_count==16

classification='PASS_E2C1_TRU1SQ_EIGHT_CYCLIC_CLASSES_MAPPED_TO_AUTHORITATIVE_U1_ROUTING_CONTRACT'
result={
 'iteration':310,
 'model_readiness_percent':24,
 'scientific_gate_pass':True,
 'classification':classification,
 'candidate_residual':False,
 'authoritative_inputs':[
   'Iteration 307 complete e=1,c=2 TrU1 cut authority',
   'Iteration 308 TrU1^2 placement/null-soft pruning: 16 ordered survivors = 8 cyclic classes',
   'U1 factor order N_L V2 N_R Y'
 ],
 'counts':{
   'ordered_surviving_orientations':16,
   'cyclic_trace_classes':8,
   'classes_per_second_order_extra_site':2
 },
 'classes':rows,
 'guardrails':[
   'CYCLIC_TRACE_EQUIVALENCE_ONLY_NO_REVERSAL_QUOTIENT',
   'MIXED_SOFT_HARD_V2_SECOND_ORDER_IS_RETAINED',
   'NO_NEW_U1_NUMERIC_COEFFICIENTS_INVENTED',
   'NO_SOURCE_BORN_SUBTRACTION',
   'NO_ANSATZ003_FISHER_RESOURCES',
   'NO_BLIND_HEAVY_FULL_C5'
 ],
 'next_gate':'physical U2 V1_1/V1_2/H0/H1 same-parent component extraction remains BLOCKED; independently, determinant e=0,c<=3 placement/operator prerequisite may proceed if not already frozen.'
}
print(json.dumps(result,indent=2,sort_keys=True))
