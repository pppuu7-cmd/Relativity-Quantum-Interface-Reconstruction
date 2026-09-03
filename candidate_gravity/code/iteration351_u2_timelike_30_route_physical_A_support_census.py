#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 351.

After Iteration 350 established that the matched-timelike rebase breaks the
historical singleton-soft A1=0 condition, rebuild the cubic U2 placement census
from all 30 raw Iteration-308 placements.  This gate uses the exact same
matched-timelike physical A1/A2 provider as Iteration 348 and asks only which
routes are forced to zero by an A_T/A_R component.

It deliberately does NOT multiply N/Y/Hinv providers yet.  Thus a route marked
"A-supported" is eligible for physical substitution, not certified nonzero as a
full Tr U2 numerator.  Unsupported/zero A components would kill a route exactly;
no zero filling or reuse of the old 12-route null-soft pruning is allowed.
"""
from __future__ import annotations
import contextlib, io, itertools, json, re
from pathlib import Path
import numpy as np

ITERATION=351
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
if n!=1: raise RuntimeError(f'Iteration-341 fixture signature drift: {n}')
ns={'__name__':'iteration351_A_provider','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(src,'iteration351_A_provider','exec'),ns,ns)
A=ns['Acoef']; qs=ns['qs']; eta=ns['eta']

LEGS=(0,1,2)
ORDER=('NL','AT','H','AR','NR','Y')
ZERO=(0,0,0)

def key_of(subset):
    return tuple(1 if i in subset else 0 for i in LEGS)

def subset_from_key(key): return tuple(i for i,x in enumerate(key) if x)

def disjoint_union(keys):
    seen=[]
    for k in keys:
        seen.extend(subset_from_key(k))
    return tuple(sorted(seen)) if len(seen)==len(set(seen)) else None

single=[key_of((i,)) for i in LEGS]
pairs=[key_of((i,j)) for i,j in itertools.combinations(LEGS,2)]
allowed={
 'NL':[ZERO]+single,
 'AT':single+pairs,
 'H':[ZERO]+single,
 'AR':single+pairs,
 'NR':[ZERO]+single,
 'Y':[ZERO]+single,
}
raw=[]
for choice in itertools.product(*[allowed[x] for x in ORDER]):
    a={name:key for name,key in zip(ORDER,choice)}
    if disjoint_union(a.values())==LEGS: raw.append(a)
assert len(raw)==30

zero_thr=1e-12
all_A_keys=single+pairs
A_norms={str(k):float(np.max(np.abs(A[k]))) for k in all_A_keys}
A_zero={str(k):bool(A_norms[str(k)]<=zero_thr) for k in all_A_keys}
records=[]; forced_zero=[]; supported=[]
for i,a in enumerate(raw):
    at=a['AT']; ar=a['AR']
    atn=A_norms[str(at)]; arn=A_norms[str(ar)]
    killed=bool(atn<=zero_thr or arn<=zero_thr)
    rec={'route':i,'assignment':{x:list(a[x]) for x in ORDER},
         'AT_max_abs':atn,'AR_max_abs':arn,
         'forced_zero_by_physical_A_support':killed}
    records.append(rec)
    (forced_zero if killed else supported).append(i)

q2=[float(np.real(np.asarray(q)@eta@np.asarray(q))) for q in qs]
old_soft=A_norms[str(key_of((0,)))]
passed=(len(raw)==30 and len(records)==30 and len(supported)+len(forced_zero)==30
        and old_soft>zero_thr and all(np.isfinite(v) for v in A_norms.values()))
classification=(
 'PASS_U2_MATCHED_TIMELIKE_30_ROUTE_PHYSICAL_A_SUPPORT_CENSUS__OLD_12_ROUTE_NULLSOFT_PRUNING_RETIRED__FULL_NY_HINV_SUBSTITUTION_NEXT'
 if passed else 'FAIL_U2_MATCHED_TIMELIKE_30_ROUTE_PHYSICAL_A_SUPPORT_CENSUS')
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':bool(passed),
 'classification':classification,'candidate_residual':False,
 'scope':'PHYSICAL_A_SUPPORT_CENSUS_ONLY__NOT_FULL_TRU2_NUMERATOR_AUTHORITY',
 'fixture':{'q_squared':q2,'metric_tensor_seed':319,'metric_tensor_scale':0.12,
            'matched_timelike_source':'Iterations 348-350'},
 'physical_A_support':{'zero_threshold':zero_thr,'component_max_abs':A_norms,
                       'component_is_zero':A_zero,
                       'historical_designated_soft_A1_max_abs':old_soft},
 'route_census':{'raw_routes':30,'A_supported_routes':len(supported),
                 'forced_zero_routes':len(forced_zero),
                 'supported_route_ids':supported,'forced_zero_route_ids':forced_zero,
                 'routes':records},
 'interpretation':{
   'iteration346_12_route_set':'RETIRED_FOR_MATCHED_TIMELIKE_PHYSICS',
   'A_supported_meaning':'eligible for full physical N/Y/Hinv substitution; not a proof that the full matrix trace is nonzero',
   'full_physical_TrU2_route_authority':'BLOCKED_UNTIL_NY_HINV_ROUTEWISE_SUBSTITUTION'},
 'guardrails':['NO_ZERO_FILL_TIMELIKE_A1','NO_REUSE_ITERATION346_12_ROUTE_SET',
               'A_SUPPORT_IS_NOT_FULL_NUMERATOR_NONZERO_CERTIFICATE',
               'NO_CUT_INTEGRATION_BEFORE_FULL_PHYSICAL_ROUTE_AUTHORITY',
               'NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':'substitute frozen Iteration349 N/Y and shifted Hinv_VD providers route-by-route into every A-supported route with exact cumulative incoming momentum and Iteration345 functional transpose; classify full route traces zero/nonzero and then canonicalize numerator/denominator families'}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
