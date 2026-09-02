#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 282.

Exact denominator-routing census for the translation-closed B3 primitive
branches.  The purpose is to canonicalize the raised bubble/triangle families
before any p-dependent numerator reconstruction or tensor/IBP reduction.
No loop integration and no fitted master coefficients are used here.
"""
import itertools, json
from collections import Counter
import numpy as np

ETA=np.diag([-1.,1.,1.,1.])
LEGS=('s','a','b')
K={
 's':np.array([1.,0.,0.,1.]),
 'a':np.array([.25,.6,.3,.15]),
 'b':np.array([-1.25,-.6,-.3,-1.15]),
}

def qb(legs,base=frozenset()):
    legs=tuple(legs); base=frozenset(base)
    if len(legs)==0:
        return [('Q0',[base])]
    if len(legs)==1:
        x=legs[0]
        return [(f'Q1[{x}]',[base|{x},base])]
    x,y=legs
    return [
      (f'Q2_seq_{x}{y}',[base|{x,y},base|{y},base]),
      (f'Q2_seq_{y}{x}',[base|{x,y},base|{x},base]),
      (f'Q2_contact_{x}{y}',[base|{x,y},base]),
    ]

def shift(S):
    return sum((K[x] for x in S),np.zeros(4))

def key(v):
    return tuple(np.round(v,12))

def msq(v):
    v=np.array(v)
    return round(float(v@ETA@v),12)

multiplicity_patterns=Counter()
bubble_q2=Counter()
triangle_squared_vertex_sector=Counter()
branch_count=0

for ass in itertools.product('LMR',repeat=3):
    L=tuple(LEGS[i] for i,a in enumerate(ass) if a=='L')
    A=tuple(LEGS[i] for i,a in enumerate(ass) if a=='M')
    R=tuple(LEGS[i] for i,a in enumerate(ass) if a=='R')
    if not A or A==('s',):
        continue
    for _,ls in qb(L,frozenset(R)|frozenset(A)):
      for _,rs in qb(R,frozenset()):
        branch_count += 1
        mult=Counter(key(shift(S)) for S in ls+rs)
        counts=tuple(sorted(mult.values(),reverse=True))
        vv=[np.array(v) for v in mult]
        pair_q2=tuple(sorted(msq(vv[j]-vv[i]) for i in range(len(vv)) for j in range(i+1,len(vv))))
        multiplicity_patterns[(counts,pair_q2)] += 1

        if len(mult)==2:
            squared=np.array(next(v for v,n in mult.items() if n==2))
            simple=np.array(next(v for v,n in mult.items() if n==1))
            bubble_q2[msq(simple-squared)] += 1
        elif len(mult)==3:
            squared=np.array(next(v for v,n in mult.items() if n==2))
            incident=[]
            for v,n in mult.items():
                if n==1:
                    incident.append(msq(np.array(v)-squared))
            triangle_squared_vertex_sector[tuple(sorted(incident))] += 1

result={
 'iteration':282,
 'model_readiness_percent':24,
 'translation_closed':bool(np.max(np.abs(K['s']+K['a']+K['b']))<1e-14),
 'primitive_branch_count':branch_count,
 'denominator_multiplicity_patterns':[
   {'multiplicities':list(k[0]),'pair_q2':list(k[1]),'count':v}
   for k,v in sorted(multiplicity_patterns.items(),key=lambda kv:(len(kv[0][0]),kv[0][1]))
 ],
 'bubble_squared_origin_q2_census':{str(k):v for k,v in sorted(bubble_q2.items())},
 'triangle_squared_vertex_incident_q2_sectors':{str(k):v for k,v in sorted(triangle_squared_vertex_sector.items())},
 'exact_reduction_statement':(
   'Every nontrivial closed primitive branch has exactly one squared denominator. '
   'The 12 triangle branches split into three canonical raised-index sectors of four branches each, '
   'according to the two invariant edges incident on the squared denominator: (0,0.21), '
   '(0,0.41), and (0.21,0.41). Bubble sectors have multiplicity pattern (2,1).'
 ),
 'classification':'PASS_EXACT_TRANSLATION_CLOSED_RAISED_INDEX_SECTOR_CANONICALIZATION',
 'guardrail':'DO_NOT_COMBINE_TRIANGLE_BRANCHES_BEFORE_MAPPING_THE_SQUARED_DENOMINATOR_TO_A_CANONICAL_VERTEX_AND_TRANSFORMING_THE_NUMERATOR_WITH_THE_SAME_LOOP_SHIFT',
 'next_gate':(
   'For bubble-a, bubble-b and the three raised triangle vertex sectors separately, '
   'apply the canonical loop shift that places the squared denominator at l^2, reconstruct the '
   'combined numerator as a finite Lorentz-covariant function of l and external invariants, '
   'validate on held-out loop momenta, then IBP-reduce the sector-summed numerators.'
 )
}
assert branch_count==23
assert multiplicity_patterns==Counter({
 ((2,1,1),(0.0,0.21,0.41)):12,
 ((2,1),(0.21,)):4,
 ((2,1),(0.41,)):4,
 ((2,1),(0.0,)):2,
 ((2,),()):1,
})
assert triangle_squared_vertex_sector==Counter({(0.0,0.21):4,(0.0,0.41):4,(0.21,0.41):4})
print(json.dumps(result,indent=2,sort_keys=True))
