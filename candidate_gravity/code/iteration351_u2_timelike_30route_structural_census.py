#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 351.

Rebuild the matched-timelike cubic U2 route census from all 30 raw Iteration-308
placements after Iteration 350 proved that the former singleton-soft A1 kill is
not preserved by the timelike rebase. This gate is deliberately structural:
it uses the physical Iteration-348 A1/A2 matrices to decide exact component
zeros, but does not yet claim nonzero traced route products. Those products are
the next gate.
"""
from __future__ import annotations
import contextlib, io, itertools, json, re
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration341_u2_v1_a12_same_parent_geometry.py'
src=PARENT.read_text().split('def geom_x',1)[0]
old=r"D=4; M=2; ZERO=\(0,0\)\neta=np\.diag\(\[-1\.,1\.,1\.,1\.\]\)\.astype\(complex\)\nrng=np\.random\.default_rng\(341\)\nhs=\[\]\nfor _ in range\(M\):\n    x=rng\.normal\(size=\(D,D\)\); hs\.append\(0\.08\*\(x\+x\.T\)/2\)\nqs=\[np\.array\(\[\.31,-\.17,\.23,\.11\]\), np\.array\(\[-\.19,\.29,\.13,-\.37\]\)\]\np=np\.array\(\[\.43,-\.27,\.39,\.21\]\)"
new="""D=4; M=3; ZERO=(0,0,0)
eta=np.diag([-1.,1.,1.,1.]).astype(complex)
rng=np.random.default_rng(319)
hs=[]
for _ in range(M):
    x=rng.normal(size=(D,D)); hs.append(0.12*(x+x.T)/2)
qs=[np.array([1.0,0.0,0.0,0.0]),np.array([-0.4,0.1,0.1,0.0]),np.array([-0.6,-0.1,-0.1,0.0])]
p=np.array([.43,-.27,.39,.21])"""
src,n=re.subn(old,new,src,count=1)
if n!=1: raise RuntimeError(f'fixture signature drift: {n}')
ns={'__name__':'iteration351_A','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(src,'iteration351_A','exec'),ns,ns)
A=ns['Acoef']
LEGS=('s','a','b'); ORDER=('NL','AT','H','AR','NR','Y')
mode={'s':(1,0,0),'a':(0,1,0),'b':(0,0,1)}
def key_to_multi(key):
    z=[0,0,0]
    for x in key:
        m=mode[x]
        for i in range(3): z[i]+=m[i]
    return tuple(z)
def canonical(key): return tuple(x for x in LEGS if x in key)
def disjoint_union(keys):
    flat=[x for k in keys for x in k]
    if len(flat)!=len(set(flat)): return None
    return canonical(flat)
allowed={
 'NL':[(),('s',),('a',),('b',)],
 'AT':[('s',),('a',),('b',),('s','a'),('s','b'),('a','b')],
 'H':[(),('s',),('a',),('b',)],
 'AR':[('s',),('a',),('b',),('s','a'),('s','b'),('a','b')],
 'NR':[(),('s',),('a',),('b',)],
 'Y':[(),('s',),('a',),('b',)],
}
raw=[]
for choice in itertools.product(*[allowed[x] for x in ORDER]):
    assign={name:canonical(key) for name,key in zip(ORDER,choice)}
    if disjoint_union(assign.values())==LEGS: raw.append(assign)
assert len(raw)==30
zero_threshold=1e-12
A_norms={}
for klen in (1,2):
  for key in itertools.combinations(LEGS,klen):
    mi=key_to_multi(key); A_norms[str(key)]=float(np.max(np.abs(A[mi])))
structural=[]; killed=[]
for i,a in enumerate(raw):
    an_at=A_norms[str(a['AT'])]; an_ar=A_norms[str(a['AR'])]
    alive=(an_at>zero_threshold and an_ar>zero_threshold)
    rec={'raw_route':i,'assignment':{x:list(a[x]) for x in ORDER},'AT_A_max_abs':an_at,'AR_A_max_abs':an_ar,'structurally_alive_from_physical_A':alive}
    (structural if alive else killed).append(rec)
passed=bool(len(raw)==30 and len(structural)+len(killed)==30 and all(np.isfinite(v) for v in A_norms.values()))
result={
 'iteration':351,'model_readiness_percent':24,'scientific_gate_pass':passed,
 'classification':('PASS_U2_MATCHED_TIMELIKE_30_RAW_ROUTE_STRUCTURAL_CENSUS_WITH_PHYSICAL_A_COMPONENTS__FULL_PHYSICAL_ROUTE_PRODUCTS_NEXT' if passed else 'FAIL_U2_TIMELIKE_30ROUTE_STRUCTURAL_CENSUS'),
 'candidate_residual':False,
 'physical_A_component_max_abs':A_norms,
 'census':{'raw_placements':len(raw),'structurally_alive':len(structural),'structurally_killed_by_exact_A_zero':len(killed),'alive_routes':structural,'killed_routes':killed},
 'scope':'STRUCTURAL_COMPONENT_ZERO_CENSUS_ONLY__NO_CLAIM_THAT_EACH_TRACE_IS_NONZERO',
 'guardrails':['ITERATION350_FORBIDS_REUSING_18_NULL_SOFT_KILLS','NO_ZERO_FILL','FULL_MATRIX_ROUTE_PRODUCTS_REQUIRED_NEXT','NO_CUT_INTEGRATION_YET','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':'evaluate full matched-timelike physical matrix products and traces for every structurally alive route using Iteration348 A1/A2, Iteration349 N/Y/Hinv, exact shifted incoming momentum and Iteration345 functional transpose; then canonicalize numerator/denominator families before cut integration'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
