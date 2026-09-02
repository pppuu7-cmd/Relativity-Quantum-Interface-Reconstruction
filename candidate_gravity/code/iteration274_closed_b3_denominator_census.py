#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 274.

Exact denominator census for the Iteration-273 translation-closed null-soft B3.
The only input beyond frozen inverse recursion is k_s+k_a+k_b=0.
"""
import itertools, json
from collections import Counter
import numpy as np

LEGS=('s','a','b')
K={
 's':np.array([1.,0.,0.,1.]),
 'a':np.array([.25,.6,.3,.15]),
 'b':np.array([-1.25,-.6,-.3,-1.15]),
}

def qbranches(legs,base=frozenset()):
    legs=tuple(legs); base=frozenset(base)
    if len(legs)==0:return [('Q0',[base])]
    if len(legs)==1:
        x=legs[0]; return [(f'Q1[{x}]',[base|{x},base])]
    if len(legs)==2:
        x,y=legs
        return [
          (f'Q2_seq_{x}{y}',[base|{x,y},base|{y},base]),
          (f'Q2_seq_{y}{x}',[base|{x,y},base|{x},base]),
          (f'Q2_contact_{x}{y}',[base|{x,y},base]),
        ]
    raise ValueError('Q3 forbidden because A0=0')

def origin(L,A,R,lname,rname):
    if len(A)==3:return 'A3_Q0Q0'
    if len(A)==2:return 'Q1_A2_Q0'
    if len(A)==1:
        if len(L)==2 or len(R)==2:
            name=lname if len(L)==2 else rname
            return 'Q2_contact_A1' if 'contact' in name else 'Q2_sequential_A1'
        return 'Q1_A1_Q1'

def shift(S):
    return tuple(np.round(sum((K[x] for x in S),np.zeros(4)),12))

rows=[]
for assign in itertools.product('LMR',repeat=3):
    L=tuple(LEGS[i] for i,a in enumerate(assign) if a=='L')
    A=tuple(LEGS[i] for i,a in enumerate(assign) if a=='M')
    R=tuple(LEGS[i] for i,a in enumerate(assign) if a=='R')
    if not A or A==('s',): continue
    baseL=frozenset(R)|frozenset(A)
    for lname,lsh in qbranches(L,baseL):
      for rname,rsh in qbranches(R,frozenset()):
        vecs=[shift(S) for S in lsh+rsh]
        mult=Counter(vecs)
        rows.append({
          'origin':origin(L,A,R,lname,rname),
          'L':L,'A':A,'R':R,
          'left_branch':lname,'right_branch':rname,
          'q0_factor_count':len(vecs),
          'distinct_denominator_count':len(mult),
          'denominator_power_pattern':sorted(mult.values(),reverse=True),
          'routed_shifts':vecs,
        })

class_counts=Counter((r['distinct_denominator_count'],tuple(r['denominator_power_pattern'])) for r in rows)
origin_classes=Counter((r['origin'],r['distinct_denominator_count'],tuple(r['denominator_power_pattern'])) for r in rows)
result={
 'iteration':274,
 'model_readiness_percent':24,
 'translation_closed':bool(np.max(np.abs(K['s']+K['a']+K['b']))<1e-14),
 'primitive_branch_count':len(rows),
 'closed_family_counts':{
   'one_distinct_squared_Q0':class_counts[(1,(2,))],
   'raised_bubble_power_2_1':class_counts[(2,(2,1))],
   'raised_triangle_power_2_1_1':class_counts[(3,(2,1,1))],
   'four_distinct_box_or_higher':sum(v for (d,p),v in class_counts.items() if d>=4),
 },
 'origin_breakdown':{
   'A3_Q0Q0_one_distinct_squared':origin_classes[('A3_Q0Q0',1,(2,))],
   'Q1_A2_Q0_raised_bubble':origin_classes[('Q1_A2_Q0',2,(2,1))],
   'Q2_contact_A1_raised_bubble':origin_classes[('Q2_contact_A1',2,(2,1))],
   'Q2_sequential_A1_raised_triangle':origin_classes[('Q2_sequential_A1',3,(2,1,1))],
   'Q1_A1_Q1_raised_triangle':origin_classes[('Q1_A1_Q1',3,(2,1,1))],
 },
 'classification':'PASS_EXACT_TRANSLATION_CLOSED_B3_RAISED_BUBBLE_TRIANGLE_DENOMINATOR_REDUCTION',
 'topology_statement':'After imposing k_s+k_a+k_b=0, every primitive branch contains one repeated Q0 shift. No four-distinct scalar denominator family survives; the nontrivial closed families are raised bubbles and raised triangles.',
 'guardrail':'THE_SINGLE_DISTINCT_Q0^2_A3_BRANCH_IS_SCALELESS_AT_THE_SCALAR_DENOMINATOR_LEVEL_IN_MASSLESS_DIMENSIONAL_REGULARIZATION, BUT DO_NOT DROP IT BEFORE NUMERATOR/REGULATOR CHECK',
 'next_gate':'reconstruct the closed B3(p) numerator over the raised-bubble/triangle basis and determine polynomial tensor degree before master reduction',
 'rows':rows,
}
assert result['translation_closed']
assert len(rows)==23
assert result['closed_family_counts']=={
 'one_distinct_squared_Q0':1,
 'raised_bubble_power_2_1':10,
 'raised_triangle_power_2_1_1':12,
 'four_distinct_box_or_higher':0,
}
print(json.dumps(result,indent=2,sort_keys=True))
