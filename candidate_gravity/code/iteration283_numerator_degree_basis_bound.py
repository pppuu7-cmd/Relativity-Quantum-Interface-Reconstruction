#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 283.

Exact loop-momentum power-counting census for the translation-closed primitive
B3 branches after the Iteration-282 raised-index canonicalization.

Frozen facts used:
  Q0(p) = -eta/p^2 on the flat Einstein background;
  N1,N2 are polynomials of degree <=2 in the routed loop momentum p;
  every polarized A1,A2,A3 coefficient is polynomial of degree <=2 in p;
  Q1 = -Q0 N1 Q0;
  Q2 = Q0(N1 Q0 N1 + N1 Q0 N1 - N2)Q0.

Therefore the primitive branch numerator degree can be bounded before any fit.
No master coefficient, source projection or loop integral is inferred here.
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
        return [('Q0',[base],0)]
    if len(legs)==1:
        x=legs[0]
        return [(f'Q1[{x}]',[base|{x},base],2)]
    x,y=legs
    return [
      (f'Q2_seq_{x}{y}',[base|{x,y},base|{y},base],4),
      (f'Q2_seq_{y}{x}',[base|{x,y},base|{x},base],4),
      (f'Q2_contact_{x}{y}',[base|{x,y},base],2),
    ]

def shift(S):
    return sum((K[x] for x in S),np.zeros(4))

def key(v): return tuple(np.round(v,12))
def msq(v):
    v=np.array(v); return round(float(v@ETA@v),12)

def scalar_basis_count(max_degree,n_external):
    # Lorentz-scalar monomials: (l^2)^a prod_i(l.q_i)^b_i,
    # with weighted degree 2a+sum b_i <= max_degree.
    count=0
    for a in range(max_degree//2+1):
        rem=max_degree-2*a
        # number of weak compositions of total <= rem into n_external slots
        if n_external==0:
            count += 1
        elif n_external==1:
            count += rem+1
        elif n_external==2:
            count += (rem+1)*(rem+2)//2
        else:
            raise ValueError('not needed here')
    return count

rows=[]
for ass in itertools.product('LMR',repeat=3):
    L=tuple(LEGS[i] for i,a in enumerate(ass) if a=='L')
    A=tuple(LEGS[i] for i,a in enumerate(ass) if a=='M')
    R=tuple(LEGS[i] for i,a in enumerate(ass) if a=='R')
    if not A or A==('s',):
        continue
    for lname,ls,ldeg in qb(L,frozenset(R)|frozenset(A)):
      for rname,rs,rdeg in qb(R,frozenset()):
        mult=Counter(key(shift(S)) for S in ls+rs)
        vv=[np.array(v) for v in mult]
        counts=tuple(sorted(mult.values(),reverse=True))
        pair_q2=tuple(sorted(msq(vv[j]-vv[i]) for i in range(len(vv)) for j in range(i+1,len(vv))))
        if counts==(2,1,1): family='triangle'
        elif counts==(2,1):
            family={0.0:'bubble_null',0.21:'bubble_b',0.41:'bubble_a'}[pair_q2[0]]
        else: family='single_scaleless'
        # Every physical A_M coefficient has routed p-degree <=2.
        degree=ldeg+2+rdeg
        rows.append({'family':family,'degree_bound':degree,'L':L,'A':A,'R':R,
                     'left_Q_branch':lname,'right_Q_branch':rname})

census=Counter((r['family'],r['degree_bound']) for r in rows)
result={
 'iteration':283,
 'model_readiness_percent':24,
 'primitive_branch_count':len(rows),
 'family_degree_census':[{'family':f,'max_numerator_degree':d,'count':n}
   for (f,d),n in sorted(census.items())],
 'exact_family_degree_bounds':{
   'single_scaleless':2,
   'bubble_null':4,
   'bubble_a':4,
   'bubble_b':4,
   'triangle':6,
 },
 'minimal_scalar_trace_reconstruction_basis_at_fixed_invariants':{
   'single_degree2_no_external_q':scalar_basis_count(2,0),
   'raised_bubble_degree4_one_external_q':scalar_basis_count(4,1),
   'raised_triangle_degree6_two_external_q':scalar_basis_count(6,2),
 },
 'classification':'PASS_EXACT_TRANSLATION_CLOSED_B3_NUMERATOR_DEGREE_AND_FINITE_BASIS_BOUND',
 'guardrail':'DO_NOT_FIT_CANONICAL_SECTOR_NUMERATORS_WITH_DEGREE_ABOVE_THE_EXACT_2_4_6_BOUNDS_WITHOUT_A_NEW_DYNAMICAL_VERSION',
 'next_gate':('Apply the Iteration-282 canonical loop shifts to the actual p-dependent branch numerators, '
              'reconstruct bubble sector sums in the degree<=4 Lorentz basis and triangle sector sums in '
              'the degree<=6 Lorentz basis, validate on held-out p points, then perform scoped tensor/IBP reduction.')
}
assert len(rows)==23
assert census==Counter({('triangle',6):12,('bubble_a',4):4,('bubble_b',4):4,('bubble_null',4):2,('single_scaleless',2):1})
assert result['minimal_scalar_trace_reconstruction_basis_at_fixed_invariants']=={
 'single_degree2_no_external_q':2,
 'raised_bubble_degree4_one_external_q':9,
 'raised_triangle_degree6_two_external_q':50,
}
print(json.dumps(result,indent=2,sort_keys=True))
