#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 275.
Classify translation-closed raised bubbles/triangles by physical invariants and
identify scaleless massless-DR families before tensor reduction.
"""
import itertools, json
from collections import Counter
import numpy as np
ETA=np.diag([-1.,1.,1.,1.])
LEGS=('s','a','b')
K={'s':np.array([1.,0.,0.,1.]),'a':np.array([.25,.6,.3,.15]),'b':np.array([-1.25,-.6,-.3,-1.15])}

def qb(legs,base=frozenset()):
    legs=tuple(legs); base=frozenset(base)
    if len(legs)==0:return [('Q0',[base])]
    if len(legs)==1:
      x=legs[0]; return [(f'Q1[{x}]',[base|{x},base])]
    x,y=legs
    return [(f'Q2_seq_{x}{y}',[base|{x,y},base|{y},base]),(f'Q2_seq_{y}{x}',[base|{x,y},base|{x},base]),(f'Q2_contact_{x}{y}',[base|{x,y},base])]
def sh(S): return tuple(np.round(sum((K[x] for x in S),np.zeros(4)),12))
def msq(q): q=np.array(q); return round(float(q@ETA@q),12)
def label_q(q):
    q=np.array(q)
    for x,k in K.items():
      if np.max(np.abs(q-k))<1e-9 or np.max(np.abs(q+k))<1e-9:return x
    return 'other'

bubbles=[]; triangles=[]; single=0
for ass in itertools.product('LMR',repeat=3):
  L=tuple(LEGS[i] for i,a in enumerate(ass) if a=='L')
  A=tuple(LEGS[i] for i,a in enumerate(ass) if a=='M')
  R=tuple(LEGS[i] for i,a in enumerate(ass) if a=='R')
  if not A or A==('s',):continue
  for ln,ls in qb(L,frozenset(R)|frozenset(A)):
    for rn,rs in qb(R,frozenset()):
      mult=Counter(sh(S) for S in ls+rs); vv=list(mult)
      if len(vv)==1: single+=1
      elif len(vv)==2:
        q=np.array(vv[1])-np.array(vv[0]); bubbles.append((label_q(q),msq(q)))
      elif len(vv)==3:
        inv=tuple(sorted(msq(np.array(vv[j])-np.array(vv[i])) for i in range(3) for j in range(i+1,3)))
        triangles.append(inv)
      else: raise AssertionError('unexpected box-or-higher family after closure')

bc=Counter(bubbles); tc=Counter(triangles)
result={
 'iteration':275,
 'model_readiness_percent':24,
 'single_squared_family_count':single,
 'raised_bubble_invariant_classes':{f'{leg}:q2={q2}':n for (leg,q2),n in sorted(bc.items())},
 'raised_triangle_invariant_classes':{str(k):v for k,v in sorted(tc.items())},
 'massless_DR_scaleless_branch_count':single+bc[('s',0.0)],
 'nontrivial_branch_count_before_tensor_reduction':23-(single+bc[('s',0.0)]),
 'nontrivial_scalar_master_kinematic_families':[
   'raised bubble with q^2=k_a^2=0.41',
   'raised bubble with q^2=k_b^2=0.21',
   'raised triangle with edge invariants (k_s^2,k_b^2,k_a^2)=(0,0.21,0.41)'
 ],
 'classification':'PASS_SCOPED_CLOSED_B3_THREE_NONTRIVIAL_SCALAR_MASTER_KINEMATIC_FAMILIES',
 'guardrail':'SCALAR_FAMILY_COLLAPSE_DOES_NOT_ALLOW_BRANCHWISE DIVERGENCE/LOG CLAIMS BEFORE COMBINED TENSOR_NUMERATOR_REDUCTION',
 'next_gate':'freeze exact numerator polynomial-degree bounds and reconstruct combined coefficients for the two bubble and one triangle kinematic families before evaluating master integrals'
}
assert single==1
assert bc==Counter({('b',0.21):4,('a',0.41):4,('s',0.0):2})
assert tc==Counter({(0.0,0.21,0.41):12})
print(json.dumps(result,indent=2,sort_keys=True))
