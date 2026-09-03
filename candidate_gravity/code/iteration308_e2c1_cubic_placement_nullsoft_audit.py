#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 308.

Exact combinatorial/operator-order audit for the remaining Vilkovisky
connection sector e=2,c<=1 at cubic background order.

Frozen authorities:
  * Iteration 244: Gamma_conn at EOM degree 2 is
        +(i/2) Tr U2 -(i/4) Tr U1^2.
  * Iteration 245 topology authority:
        U1 = N V2 N Y,
        U2 = N V1 H V1 N Y,
    with V2 carrying one EOM degree and the two V1 factors jointly carrying
    two EOM degrees.
  * Iteration 246 / later direct implementation: a singleton null-soft linear
    Einstein/EOM insertion vanishes exactly, E^(1)[h_s]=0.  Mixed quadratic
    soft-hard insertions are NOT set to zero.

At cubic background order, U2 starts at order 2 and needs exactly one extra
background insertion.  Tr U1^2 starts at order 2 and therefore one U1 block
is first order while the other is second order.  We enumerate all distinct-leg
(s,a,b) placements before tensor contraction/routing and apply only the exact
singleton-soft zero rule.

This audit freezes placement classes; it does not invent the missing exact V1
index kernel or H first variation.
"""
from itertools import permutations
import json

LEGS=('s','a','b')

# ---------- U2 = N_L V1_L H V1_R N_R Y ----------
U2_SITES=('N_L','V1_L','H','V1_R','N_R','Y')
u2_raw=[]
u2_survive=[]
u2_killed=[]

for extra in U2_SITES:
    if extra=='V1_L':
        # V1_L receives a quadratic mixed pair; V1_R is singleton.
        for singleton in LEGS:
            pair=tuple(x for x in LEGS if x!=singleton)
            row={'extra_site':extra,'V1_L_legs':pair,'V1_R_legs':(singleton,),
                 'extra_local_legs':(), 'soft_zero_reason':None}
            u2_raw.append(row)
            if singleton=='s':
                row=dict(row); row['soft_zero_reason']='V1_R_SINGLETON_SOFT_E1_ZERO'; u2_killed.append(row)
            else: u2_survive.append(row)
    elif extra=='V1_R':
        for singleton in LEGS:
            pair=tuple(x for x in LEGS if x!=singleton)
            row={'extra_site':extra,'V1_L_legs':(singleton,),'V1_R_legs':pair,
                 'extra_local_legs':(), 'soft_zero_reason':None}
            u2_raw.append(row)
            if singleton=='s':
                row=dict(row); row['soft_zero_reason']='V1_L_SINGLETON_SOFT_E1_ZERO'; u2_killed.append(row)
            else: u2_survive.append(row)
    else:
        # Three singleton insertions: V1_L, V1_R, and the extra local/propagator site.
        for p in permutations(LEGS):
            row={'extra_site':extra,'V1_L_legs':(p[0],),'V1_R_legs':(p[1],),
                 'extra_local_legs':(p[2],), 'soft_zero_reason':None}
            u2_raw.append(row)
            if p[0]=='s':
                row=dict(row); row['soft_zero_reason']='V1_L_SINGLETON_SOFT_E1_ZERO'; u2_killed.append(row)
            elif p[1]=='s':
                row=dict(row); row['soft_zero_reason']='V1_R_SINGLETON_SOFT_E1_ZERO'; u2_killed.append(row)
            else: u2_survive.append(row)

assert len(u2_raw)==30
assert len(u2_survive)==12
assert len(u2_killed)==18

# ---------- Tr U1^2 with U1 = N_L V2 N_R Y ----------
U1_SITES=('N_L','V2','N_R','Y')

def u1_second_order(pair):
    """All order-2 placements inside one U1 block for an unordered leg pair."""
    pair=tuple(pair); assert len(pair)==2
    rows=[]
    # Extra order on the EOM vertex itself: mixed V2^(2)[pair]. Never kill it
    # merely because one member is s; only singleton V2[s] is known zero.
    rows.append({'extra_site':'V2','V2_legs':pair,'extra_local_legs':(),
                 'soft_zero_reason':None})
    # Extra order on one of the other block factors. Then V2 is singleton.
    for site in ('N_L','N_R','Y'):
        for vleg in pair:
            dleg=pair[1] if pair[0]==vleg else pair[0]
            row={'extra_site':site,'V2_legs':(vleg,),
                 'extra_local_legs':(dleg,),'soft_zero_reason':None}
            if vleg=='s': row['soft_zero_reason']='V2_SINGLETON_SOFT_E1_ZERO'
            rows.append(row)
    assert len(rows)==7
    return rows

u1sq_raw=[]; u1sq_survive=[]; u1sq_killed=[]
for singleton in LEGS:
    pair=tuple(x for x in LEGS if x!=singleton)
    for second in u1_second_order(pair):
        for orientation in ('U1_FIRST_SINGLETON','U1_SECOND_SINGLETON'):
            row={'singleton_leg':singleton,'pair_legs':pair,'block_orientation':orientation,
                 'second_order_block':second,'soft_zero_reason':None}
            u1sq_raw.append(row)
            reason=None
            if singleton=='s':
                reason='FIRST_ORDER_U1_HAS_V2_SINGLETON_SOFT_E1_ZERO'
            elif second['soft_zero_reason']:
                reason=second['soft_zero_reason']
            if reason:
                rr=dict(row); rr['soft_zero_reason']=reason; u1sq_killed.append(rr)
            else: u1sq_survive.append(row)

assert len(u1sq_raw)==42
assert len(u1sq_survive)==16
assert len(u1sq_killed)==26

# Cyclic trace identifies the two block orientations of the surviving U1^2 rows.
def cyclic_u1sq_key(row):
    sec=row['second_order_block']
    return (row['singleton_leg'],tuple(row['pair_legs']),sec['extra_site'],
            tuple(sec['V2_legs']),tuple(sec['extra_local_legs']))

u1sq_cyclic={cyclic_u1sq_key(r) for r in u1sq_survive}
assert len(u1sq_cyclic)==8

# Site-resolved survivor census: useful to schedule exact first variations.
def census(rows,key):
    out={}
    for r in rows:
        k=r[key] if key in r else r['second_order_block'][key]
        out[k]=out.get(k,0)+1
    return out

u2_site_survivors=census(u2_survive,'extra_site')
u1sq_site_survivors={}
for r in u1sq_survive:
    k=r['second_order_block']['extra_site']
    u1sq_site_survivors[k]=u1sq_site_survivors.get(k,0)+1

assert u2_site_survivors=={'N_L':2,'V1_L':2,'H':2,'V1_R':2,'N_R':2,'Y':2}
assert u1sq_site_survivors=={'V2':4,'N_L':4,'N_R':4,'Y':4}

result={
 'iteration':308,
 'model_readiness_percent':24,
 'classification':'PASS_E2C1_CUBIC_BACKGROUND_PLACEMENT_AND_NULLSOFT_PRUNING_AUDIT__EXACT_V1_H_KERNEL_IMPLEMENTATION_REMAINS',
 'candidate_residual':False,
 'effective_action_eom_degree2_identity':{
   'Tr_U2_coefficient_multiplying_i':'1/2',
   'Tr_U1_sq_coefficient_multiplying_i':'-1/4',
   'source':'Iteration244 exact noncommutative trace-log identity'
 },
 'factor_sequences':{
   'U1':['N_L','V2','N_R','Y'],
   'U2':['N_L','V1_L','H','V1_R','N_R','Y']
 },
 'U2_cubic_placement':{
   'raw_ordered_primitive_count':len(u2_raw),
   'exact_singleton_soft_killed_count':len(u2_killed),
   'surviving_ordered_primitive_count':len(u2_survive),
   'surviving_by_extra_site':u2_site_survivors,
   'surviving_rows':u2_survive
 },
 'Tr_U1_sq_cubic_placement':{
   'raw_ordered_primitive_count':len(u1sq_raw),
   'exact_singleton_soft_killed_count':len(u1sq_killed),
   'surviving_ordered_primitive_count':len(u1sq_survive),
   'surviving_cyclic_trace_class_count':len(u1sq_cyclic),
   'surviving_by_second_order_extra_site':u1sq_site_survivors,
   'surviving_rows':u1sq_survive
 },
 'proven_zero_rule':'Only a singleton null-soft leg on a linear EOM vertex V1 or V2 is killed through E^(1)[h_s]=0. Mixed V1^(2)[s,h] and V2^(2)[s,h] are retained.',
 'new_required_executable_ingredients':[
   'exact same-parent V1 field-gauge index kernel from the primary U2 definition',
   'flat graviton Green operator H0 in the frozen a=-1/2, Lambda=0 convention',
   'first background variation H1 for the surviving H-dressed U2 classes',
   'V1 first and mixed second background coefficients on the frozen timelike legs',
   'routing-compatible N1 and local Y1 already available from the U1 infrastructure',
   'trace/transpose checks before any scalar master integration'
 ],
 'guardrails':[
   'NO_UNPROVEN_LEFT_RIGHT_OR_REVERSAL_QUOTIENT_APPLIED_TO_U2_SURVIVORS',
   'MIXED_SOFT_HARD_EOM_VERTICES_ARE_NOT_ZERO_FILLED',
   'THIS_AUDIT_DOES_NOT_EVALUATE_TRU2_OR_TRU1SQ_NUMERICALLY',
   'NO_HEAVY_FULL_C5_RUN_AUTHORIZED',
   'NO_SOURCE_WARD_K2_COMPLETION_NO_COMPARATOR_RESIDUAL_NO_ANSATZ003'
 ],
 'next_gate':'derive/freeze the exact primary U2 index formula into an executable V1-H-V1 kernel and implement only the flat V1_1/H0 plus first-background V1_2/H1/N1/Y1 ingredients required by the 12 surviving U2 placements; reuse the already-authoritative U1 primitives for the 8 cyclic Tr U1^2 classes.'
}
print(json.dumps(result,indent=2,sort_keys=True))
