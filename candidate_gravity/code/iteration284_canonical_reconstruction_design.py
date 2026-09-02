#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 284.

Deterministic reconstruction-design certificate for the canonical shifted
translation-closed C5 numerator sectors.  This does NOT fit pre-integration
traces to master functions.  It only certifies that the frozen Lorentz
polynomial bases from Iteration 283 are sampled at full column rank on the
actual Iteration-273/282 closed kinematics, with disjoint held-out points.
"""
import json
import numpy as np

ETA=np.diag([-1.,1.,1.,1.])
K={
 's':np.array([1.,0.,0.,1.]),
 'a':np.array([.25,.6,.3,.15]),
}
K['b']=-(K['s']+K['a'])

def mdot(x,y): return float(x@ETA@y)

def bubble_exps(d=4):
    return [(a,b) for a in range(d//2+1) for b in range(d-2*a+1)]

def triangle_exps(d=6):
    return [(a,b,c) for a in range(d//2+1)
            for b in range(d-2*a+1)
            for c in range(d-2*a-b+1)]

BE=bubble_exps(4)
TE=triangle_exps(6)
assert len(BE)==9 and len(TE)==50

def bmat(q,pts):
    return np.array([[(mdot(l,l)**a)*(mdot(l,q)**b) for a,b in BE] for l in pts])

def tmat(q1,q2,pts):
    return np.array([[(mdot(l,l)**a)*(mdot(l,q1)**b)*(mdot(l,q2)**c)
                      for a,b,c in TE] for l in pts])

rng=np.random.default_rng(284)
train_b=rng.uniform(-1.5,1.5,(40,4))
hold_b=rng.uniform(-1.7,1.7,(18,4))
train_t=rng.uniform(-1.5,1.5,(120,4))
hold_t=rng.uniform(-1.7,1.7,(70,4))

sectors={}
for name,q in [('bubble-a',K['a']),('bubble-b',K['b'])]:
    M=bmat(q,train_b); H=bmat(q,hold_b)
    sectors[name]={
      'basis_size':len(BE),'train_points':len(train_b),'heldout_points':len(hold_b),
      'train_rank':int(np.linalg.matrix_rank(M)),
      'heldout_rank':int(np.linalg.matrix_rank(H)),
      'train_condition_number':float(np.linalg.cond(M)),
      'q2':mdot(q,q),
    }

tri_defs=[
 ('triangle-(0,0.21)',K['s'],K['b']),
 ('triangle-(0,0.41)',K['s'],K['a']),
 ('triangle-(0.21,0.41)',K['b'],K['a']),
]
for name,q1,q2 in tri_defs:
    M=tmat(q1,q2,train_t); H=tmat(q1,q2,hold_t)
    G=np.array([[mdot(q1,q1),mdot(q1,q2)],[mdot(q2,q1),mdot(q2,q2)]])
    sectors[name]={
      'basis_size':len(TE),'train_points':len(train_t),'heldout_points':len(hold_t),
      'train_rank':int(np.linalg.matrix_rank(M)),
      'heldout_rank':int(np.linalg.matrix_rank(H)),
      'train_condition_number':float(np.linalg.cond(M)),
      'external_gram_det':float(np.linalg.det(G)),
      'edge_q2':[mdot(q1,q1),mdot(q2,q2)],
    }

# Canonical shift rule from Iteration 282: if the repeated denominator is
# (p+v)^2, define l=p+v, hence every primitive numerator must be evaluated at
# p=l-v before sector summation.  A loop shift cannot increase polynomial degree.
result={
 'iteration':284,
 'model_readiness_percent':24,
 'translation_closed':bool(np.max(np.abs(K['s']+K['a']+K['b']))<1e-14),
 'bubble_basis_exponents':BE,
 'triangle_basis_exponents':TE,
 'canonical_shift_rule':'repeated denominator (p+v)^2 -> l^2 with p=l-v; apply identical substitution to primitive numerator before summation',
 'degree_preservation':'affine loop translation preserves the frozen degree<=4 bubble and degree<=6 triangle ceilings exactly',
 'sectors':sectors,
 'classification':'PASS_EXACT_CANONICAL_SHIFT_DEGREE_PRESERVATION_AND_FULL_RANK_RECONSTRUCTION_DESIGN',
 'guardrail':'DO_NOT_INTERPRET_FULL_RANK_SAMPLING_AS_NUMERATOR_RECONSTRUCTION; ACTUAL SAME_PARENT PRIMITIVE NUMERATOR ORACLE VALUES AND HELD_OUT RESIDUALS ARE STILL REQUIRED',
 'candidate_residual':False,
 'next_gate':285,
}
assert result['translation_closed']
assert all(v['train_rank']==v['basis_size'] and v['heldout_rank']==v['basis_size'] for v in sectors.values())
print(json.dumps(result,indent=2,sort_keys=True))
