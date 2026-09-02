#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 273 exact symbolic denominator census.

Expands the 15 null-soft B3 Leibniz partitions through the frozen exact Q1/Q2
inverse recursion and imposes translation closure k_s+k_a+k_b=0 only after
constructing routed Q0 arguments.  It counts Q0 factors and distinct momentum
shifts.  No master integral or numerical B3 value is assumed.
"""
import itertools, json
from collections import Counter

LEGS=('s','a','b')
ZERO=(0,0,0)

def add(base, labels):
    x=list(base)
    for lab in labels:
        x[LEGS.index(lab)] += 1
    return tuple(x)

def qbranches(labels, base=ZERO):
    labels=tuple(labels)
    if len(labels)==0:
        return [[base]]
    if len(labels)==1:
        x=labels[0]
        return [[add(base,(x,)), base]]
    if len(labels)==2:
        x,y=labels
        tot=add(base,(x,y))
        return [
            [tot, add(base,(y,)), base], # N1[x] Q0 N1[y]
            [tot, add(base,(x,)), base], # N1[y] Q0 N1[x]
            [tot, base],                 # -N2[x,y]
        ]
    raise ValueError('Q3 is forbidden because A0=0')

def closed(v):
    # k_b=-(k_s+k_a), so c_s k_s+c_a k_a+c_b k_b
    # -> (c_s-c_b) k_s + (c_a-c_b) k_a.
    return (v[0]-v[2], v[1]-v[2])

branches=[]
for assign in itertools.product('LMR', repeat=3):
    L=tuple(LEGS[i] for i,a in enumerate(assign) if a=='L')
    M=tuple(LEGS[i] for i,a in enumerate(assign) if a=='M')
    R=tuple(LEGS[i] for i,a in enumerate(assign) if a=='R')
    if not M or M==('s',):
        continue
    left_base=add(ZERO,R+M)
    for lb in qbranches(L,left_base):
        for rb in qbranches(R,ZERO):
            routed=lb+rb
            c=[closed(v) for v in routed]
            branches.append({
                'L':L,'A':M,'R':R,
                'q0_factor_count':len(routed),
                'closed_distinct_denominator_count':len(set(c)),
                'closed_shifts_sa_basis':c,
            })

joint=Counter((b['q0_factor_count'],b['closed_distinct_denominator_count']) for b in branches)
result={
    'iteration':273,
    'model_readiness_percent':24,
    'translation_closure':'k_s+k_a+k_b=0',
    'surviving_nullsoft_partition_count':15,
    'primitive_branch_count':len(branches),
    'joint_q0_factor_vs_distinct_denominator_census':{
        f'{q0}_Q0__{d}_distinct':n for (q0,d),n in sorted(joint.items())
    },
    'max_distinct_closed_denominators':max(b['closed_distinct_denominator_count'] for b in branches),
    'classification':'PASS_EXACT_TRANSLATION_CLOSED_B3_DENOMINATOR_TOPOLOGY_REDUCTION',
    'topology_interpretation':{
        'raised_triangle_branches':joint[(4,3)],
        'raised_bubble_branches':joint[(3,2)],
        'single_denominator_squared_branches':joint[(2,1)],
        'four_distinct_denominator_branches':sum(n for (q0,d),n in joint.items() if d>=4),
    },
    'candidate_residual':False,
    'guardrail':'TOPOLOGY CLOSURE DOES NOT PROVE TRANSLATION-CLOSED B3 NONZERO OR A FINAL C5 COMPARATOR COORDINATE',
    'next_gate':'execute/refine the K=0 physical B3 rerun across loop momentum p; if stably nonzero, reconstruct its finite p-dependent numerator basis and then reduce only within the certified raised bubble/triangle families'
}

assert len(branches)==23
assert joint[(4,3)]==12
assert joint[(3,2)]==10
assert joint[(2,1)]==1
assert result['max_distinct_closed_denominators']==3
assert result['topology_interpretation']['four_distinct_denominator_branches']==0
print(json.dumps(result,indent=2,sort_keys=True))
