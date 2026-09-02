#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 293.

Held-out complete-coordinate polynomial reconstruction of every non-scaleless
weight-completed [Tr U1]_{sab} denominator sector from Iteration 292.

Each primitive denominator set is mapped to one canonical routing using only an
allowed loop translation and optional global reflection p -> -p.  Numerators are
then summed in that common routing and fitted at the exact conservative degree
ceilings:
  ordinary bubble <=2, ordinary triangle <=4,
  raised bubble <=4, raised triangle <=6.

Coefficients are exported for the subsequent DR tensor/Laurent reduction.
"""
import importlib.util, json, math
from pathlib import Path
from collections import Counter
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('i292',HERE/'iteration292_complete_tru1_denominator_census.py')
i292=importlib.util.module_from_spec(spec); spec.loader.exec_module(i292)
D=i292.D; numerator=i292.numerator; vk=i292.vk

NONSC=[
 'ordinary_bubble_a','ordinary_bubble_b','ordinary_tri_(0.0,0.21,0.41)',
 'raised_bubble_a','raised_bubble_b',
 'raised_tri_(0.0, 0.21)','raised_tri_(0.0, 0.41)','raised_tri_(0.21, 0.41)'
]
DEG={
 'ordinary_bubble_a':2,'ordinary_bubble_b':2,
 'ordinary_tri_(0.0,0.21,0.41)':4,
 'raised_bubble_a':4,'raised_bubble_b':4,
 'raised_tri_(0.0, 0.21)':6,'raised_tri_(0.0, 0.41)':6,'raised_tri_(0.21, 0.41)':6,
}


def exponents(deg):
    return [(a,b,c,d) for a in range(deg+1)
            for b in range(deg+1-a)
            for c in range(deg+1-a-b)
            for d in range(deg+1-a-b-c)]

def mon(exps,l):
    l=np.asarray(l,float)
    return np.array([np.prod([l[i]**e[i] for i in range(4)]) for e in exps],float)

def multiset_key(vs):
    return sorted(vk(v) for v in vs)

def same_multiset(a,b,tol=2e-10):
    aa=sorted(np.asarray(x,float) for x in a, key=lambda z: tuple(np.round(z,12)))
    bb=sorted(np.asarray(x,float) for x in b, key=lambda z: tuple(np.round(z,12)))
    return len(aa)==len(bb) and all(np.max(np.abs(x-y))<tol for x,y in zip(aa,bb))

def route_to_target(d,target):
    # Under p=sigma*l+delta, denominator shift v becomes sigma*(delta+v).
    for sigma in (1.0,-1.0):
      for v in d['den']:
       for t in target:
        delta=sigma*np.asarray(t,float)-np.asarray(v,float)
        got=[sigma*(delta+np.asarray(x,float)) for x in d['den']]
        if same_multiset(got,target):
            return sigma,delta
    raise RuntimeError(('no canonical route',d['sector'],d['den'],target))

SECD={s:[d for d in D if d['sector']==s] for s in NONSC}
ROUTES={}
TARGET={}
for s,ds in SECD.items():
    target=[np.asarray(v,float) for v in ds[0]['den']]
    TARGET[s]=target
    ROUTES[s]=[route_to_target(d,target) for d in ds]


def sector_num(s,l):
    z=0j
    for d,(sigma,delta) in zip(SECD[s],ROUTES[s]):
        p=sigma*np.asarray(l,float)+delta
        z += numerator(d,p)
    return z


def fit_sector(s,seed):
    deg=DEG[s]; exps=exponents(deg); n=len(exps)
    rng=np.random.default_rng(seed)
    # Distinct training/holdout boxes guard against accidental interpolation.
    tr=rng.uniform(-0.92,0.92,(n+18,4))
    ho=rng.uniform(-1.08,1.08,(max(28,n//7),4))
    yc=np.array([sector_num(s,l) for l in tr]); zc=np.array([sector_num(s,l) for l in ho])
    imag=max(float(np.max(np.abs(yc.imag))),float(np.max(np.abs(zc.imag))))
    y=yc.real; z=zc.real
    X=np.array([mon(exps,l) for l in tr]); H=np.array([mon(exps,l) for l in ho])
    c=np.linalg.lstsq(X,y,rcond=None)[0]
    r=H@c-z
    rel=float(np.max(np.abs(r))/max(np.max(np.abs(z)),1e-30))
    return {
      'degree_ceiling':deg,'basis_size':n,'train_rank':int(np.linalg.matrix_rank(X)),
      'condition_number':float(np.linalg.cond(X)),
      'heldout_max_abs':float(np.max(np.abs(r))),
      'heldout_rms':float(np.sqrt(np.mean(r*r))),
      'heldout_relative_max':rel,'max_oracle_imag_abs':imag,
      'primitive_branch_count':len(SECD[s]),
      'canonical_denominator_shifts':[np.asarray(v,float).tolist() for v in TARGET[s]],
      'route_reflection_count':sum(1 for sig,_ in ROUTES[s] if sig<0),
      'monomial_exponents':[list(e) for e in exps],
      'coefficients':[float(x) for x in c],
    }

rows={s:fit_sector(s,2930+i) for i,s in enumerate(NONSC)}
maxrel=max(v['heldout_relative_max'] for v in rows.values())
maximag=max(v['max_oracle_imag_abs'] for v in rows.values())
fullrank=all(v['train_rank']==v['basis_size'] for v in rows.values())
classification=('PASS_COMPLETE_WEIGHT_COMPLETED_TRU1_NUMERATOR_RECONSTRUCTION_ALL_EIGHT_NONSCALAR_SECTORS'
                if fullrank and maxrel<2e-5 and maximag<2e-5 else
                'BLOCKED_TRU1_NUMERATOR_RECONSTRUCTION_AUDIT')
result={
 'iteration':293,'model_readiness_percent':24,
 'sector_count':len(rows),'sectors':rows,
 'max_heldout_relative_error':maxrel,
 'max_oracle_imag_abs':maximag,
 'all_training_matrices_full_rank':fullrank,
 'classification':classification,'candidate_residual':False,
 'guardrails':[
   'CANONICALIZATION_USES_ONLY_LOOP_TRANSLATION_AND_GLOBAL_REFLECTION',
   'COEFFICIENTS_ARE_FOR_WEIGHT_COMPLETED_TRU1_NOT_TRACE_B3',
   'TENSOR_REDUCTION_MAY_PROCEED_ONLY_FROM_THE_EXPORTED_COMPLETE_FAMILY_COEFFICIENTS'
 ],
 'next_gate':'perform corrected DR tensor reduction of ordinary and raised bubble/triangle sectors, include the -i/2 Tr U1 effective-action prefactor only after master normalization is fixed, and repeat the Laurent IR-pole audit'
}
assert classification.startswith('PASS_COMPLETE'), result
print(json.dumps(result,indent=2,sort_keys=True))
