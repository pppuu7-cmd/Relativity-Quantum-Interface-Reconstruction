#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 352.

Evaluate full matched-timelike physical matrix products and traces for all 30
structurally alive cubic U2 routes established by Iteration 351.

Frozen inputs:
  Iteration 348 physical A1/A2 on the exact timelike common background;
  Iteration 349 matched N/Y and shifted Hinv providers;
  Iteration 345 A_T(Q;k)=A_R(Q;-k-Q)^T;
  Iteration 340 Hinv_VD=-K^-1 and U2=N_L A_T Hinv A_R N_R Y.

No cut integration is performed. This gate only closes route-level physical
matrix authority and separates exact/numerical-zero route products from
nonzero products before denominator-family reduction.
"""
from __future__ import annotations
import contextlib, io, itertools, json, re
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
D=4; DG=4; DF=10
ETA=np.diag([-1.,1.,1.,1.]).astype(complex)
LEGS=('s','a','b'); ORDER=('NL','AT','H','AR','NR','Y'); APPLY=tuple(reversed(ORDER))
Q={'s':np.array([1.0,0.0,0.0,0.0]),'a':np.array([-0.4,0.1,0.1,0.0]),'b':np.array([-0.6,-0.1,-0.1,0.0])}
P0=np.array([.43,-.27,.39,.21])
MODE={'s':(1,0,0),'a':(0,1,0),'b':(0,0,1)}

def canonical(key): return tuple(x for x in LEGS if x in key)
def qkey(key): return sum((Q[x] for x in key),np.zeros(4))
def multi(key):
    z=[0,0,0]
    for x in key:
        for i,v in enumerate(MODE[x]): z[i]+=v
    return tuple(z)
def mdot(k): return complex(np.asarray(k,complex)@ETA@np.asarray(k,complex))
def maxabs(x): return float(np.max(np.abs(x)))
def kt(k): return tuple(np.round(np.asarray(k,float),14))

# Prepare frozen parent source prefixes, changing only fixture and arbitrary input p.
A_PARENT=ROOT/'iteration341_u2_v1_a12_same_parent_geometry.py'
A_SRC=A_PARENT.read_text().split('def geom_x',1)[0]
oldA=r"D=4; M=2; ZERO=\(0,0\)\neta=np\.diag\(\[-1\.,1\.,1\.,1\.\]\)\.astype\(complex\)\nrng=np\.random\.default_rng\(341\)\nhs=\[\]\nfor _ in range\(M\):\n    x=rng\.normal\(size=\(D,D\)\); hs\.append\(0\.08\*\(x\+x\.T\)/2\)\nqs=\[np\.array\(\[\.31,-\.17,\.23,\.11\]\), np\.array\(\[-\.19,\.29,\.13,-\.37\]\)\]\np=np\.array\(\[\.43,-\.27,\.39,\.21\]\)"
newA="""D=4; M=3; ZERO=(0,0,0)
eta=np.diag([-1.,1.,1.,1.]).astype(complex)
rng=np.random.default_rng(319)
hs=[]
for _ in range(M):
    x=rng.normal(size=(D,D)); hs.append(0.12*(x+x.T)/2)
qs=[np.array([1.0,0.0,0.0,0.0]),np.array([-0.4,0.1,0.1,0.0]),np.array([-0.6,-0.1,-0.1,0.0])]
p=P_IN.copy()"""
A_SRC,n=re.subn(oldA,newA,A_SRC,count=1)
if n!=1: raise RuntimeError(f'A fixture signature drift: {n}')

G_PARENT=ROOT/'iteration317_det_ghost_three_mode_routing.py'
G_SRC=G_PARENT.read_text().split('# Independent exact-geometry oracle',1)[0]
G_SRC,n=re.subn(r"rng=np\.random\.default_rng\(317\)","rng=np.random.default_rng(319)",G_SRC,count=1)
if n!=1: raise RuntimeError('ghost seed signature drift')
G_SRC,n=re.subn(r"hs\.append\(0\.2\*\(x\+x\.T\)/2\.0\)","hs.append(0.12*(x+x.T)/2.0)",G_SRC,count=1)
if n!=1: raise RuntimeError('ghost scale signature drift')
G_SRC,n=re.subn(r"qs=\[.*?\]\np=np\.array\([^\n]+\)","qs=[np.array([1.0,0.0,0.0,0.0]),np.array([-0.4,0.1,0.1,0.0]),np.array([-0.6,-0.1,-0.1,0.0])]\np=P_IN.copy()",G_SRC,count=1,flags=re.S)
if n!=1: raise RuntimeError('ghost q/p signature drift')

H_PARENT=ROOT/'iteration319_det_graviton_three_mode_routing.py'
H_SRC=H_PARENT.read_text().split('FIT=indices(4)',1)[0]
H_SRC,n=re.subn(r"qs=\[np\.array\([^\n]+\),np\.array\([^\n]+\),np\.array\([^\n]+\)\]","qs=[np.array([1.0,0.0,0.0,0.0]),np.array([-0.4,0.1,0.1,0.0]),np.array([-0.6,-0.1,-0.1,0.0])]",H_SRC,count=1)
if n!=1: raise RuntimeError('graviton q signature drift')
H_SRC,n=re.subn(r"p=np\.array\([^\n]+\)","p=P_IN.copy()",H_SRC,count=1)
if n!=1: raise RuntimeError('graviton p signature drift')

A_CACHE={}; G_CACHE={}; H_CACHE={}
def load(src,label,k):
    ns={'P_IN':np.asarray(k,float),'__name__':label,'__file__':label}
    with contextlib.redirect_stdout(io.StringIO()): exec(compile(src,label,'exec'),ns,ns)
    return ns
def Ast(k):
    z=kt(k)
    if z not in A_CACHE: A_CACHE[z]=load(A_SRC,'iteration352_A',k)
    return A_CACHE[z]
def Gst(k):
    z=kt(k)
    if z not in G_CACHE: G_CACHE[z]=load(G_SRC,'iteration352_G',k)
    return G_CACHE[z]
def Hst(k):
    z=kt(k)
    if z not in H_CACHE: H_CACHE[z]=load(H_SRC,'iteration352_H',k)
    return H_CACHE[z]

def AR(key,k):
    key=canonical(key)
    if len(key) not in (1,2): raise ValueError(('AR',key))
    return np.asarray(Ast(k)['Acoef'][multi(key)],complex)
def AT(key,k):
    key=canonical(key); qq=qkey(key)
    return AR(key,-np.asarray(k)-qq).T

def ghost_Q0(k):
    # Independently frozen flat ghost identity from Iterations 317/349.
    return np.linalg.inv((-mdot(k))*np.eye(D,dtype=complex))
def ghost_N1(key,k):
    if len(key)!=1: raise ValueError(key)
    return np.asarray(Gst(k)['N'][multi(key)],complex)
def Yupper(key):
    if len(key)==0: return -ETA
    if len(key)!=1: raise ValueError(key)
    return -np.asarray(Gst(P0)['G'][multi(key)],complex)
def Ylower(key):
    if len(key)==0: return -ETA
    if len(key)!=1: raise ValueError(key)
    r=LEGS.index(key[0]); return -np.asarray(Gst(P0)['hs'][r],complex)
def Nupper(key,k):
    key=canonical(key)
    if len(key)==0: return ghost_Q0(k)@Yupper(())
    if len(key)!=1: raise ValueError(key)
    qq=qkey(key); Q0i=ghost_Q0(k); Q0o=ghost_Q0(np.asarray(k)+qq)
    Q1=-Q0o@ghost_N1(key,k)@Q0i
    return Q0o@Yupper(key)+Q1@Yupper(())

def Hinv(key,k):
    key=canonical(key); st=Hst(k); K0=np.asarray(st['H'][st['ZERO']],complex); G0=np.linalg.inv(K0)
    if len(key)==0: return -G0
    if len(key)!=1: raise ValueError(key)
    qq=qkey(key); K1=np.asarray(st['H'][multi(key)],complex)
    sto=Hst(np.asarray(k)+qq); K0o=np.asarray(sto['H'][sto['ZERO']],complex); G0o=np.linalg.inv(K0o)
    G1=-G0o@K1@G0
    return -G1

def component(name,key,k):
    key=canonical(key)
    if name=='Y': return Ylower(key)
    if name in ('NR','NL'): return Nupper(key,k)
    if name=='AR': return AR(key,k)
    if name=='AT': return AT(key,k)
    if name=='H': return Hinv(key,k)
    raise KeyError(name)

def component_wrong_AT(name,key,k):
    if name=='AT': return AR(key,k).T
    return component(name,key,k)

allowed={
 'NL':[(),('s',),('a',),('b',)],
 'AT':[('s',),('a',),('b',),('s','a'),('s','b'),('a','b')],
 'H':[(),('s',),('a',),('b',)],
 'AR':[('s',),('a',),('b',),('s','a'),('s','b'),('a','b')],
 'NR':[(),('s',),('a',),('b',)],
 'Y':[(),('s',),('a',),('b',)],
}
def disjoint_union(keys):
    flat=[x for k in keys for x in k]
    if len(flat)!=len(set(flat)): return None
    return canonical(flat)
raw=[]
for choice in itertools.product(*[allowed[x] for x in ORDER]):
    a={name:canonical(key) for name,key in zip(ORDER,choice)}
    if disjoint_union(a.values())==LEGS: raw.append(a)
assert len(raw)==30

def route_value(assign,wrong_at=False,unshifted=False):
    cur=P0.copy(); M=np.eye(DG,dtype=complex); prov=[]
    for name in APPLY:
        key=assign[name]; kin=P0.copy() if unshifted else cur.copy()
        F=(component_wrong_AT(name,key,kin) if wrong_at else component(name,key,kin))
        M=F@M
        prov.append({'factor':name,'key':list(key),'incoming':kin.tolist(),'outgoing':(kin+qkey(key)).tolist(),'factor_max_abs':maxabs(F)})
        if not unshifted: cur=cur+qkey(key)
    return M,complex(np.trace(M)),prov,cur

routes=[]; max_closure=0.; nonzero=0; zero=0; min_wrong=float('inf'); min_unshift=float('inf')
zero_threshold=1e-12
for i,a in enumerate(raw):
    M,t,prov,cur=route_value(a)
    norm=maxabs(M); trabs=float(abs(t)); iszero=norm<=zero_threshold
    nonzero+=int(not iszero); zero+=int(iszero)
    cl=maxabs(cur-P0); max_closure=max(max_closure,cl)
    Mw,_,_,_=route_value(a,wrong_at=True)
    Mu,_,_,_=route_value(a,unshifted=True)
    dT=maxabs(M-Mw); dU=maxabs(M-Mu)
    min_wrong=min(min_wrong,dT); min_unshift=min(min_unshift,dU)
    routes.append({'route':i,'assignment':{x:list(a[x]) for x in ORDER},'matrix_max_abs':norm,'trace_abs':trabs,'trace_real':float(t.real),'trace_imag':float(t.imag),'matrix_zero_under_threshold':iszero,'loop_closure_error':cl,'wrong_same_k_transpose_difference':dT,'unshifted_routing_difference':dU,'provenance_apply_order':prov})

thresholds={'route_zero_abs':zero_threshold,'loop_closure_abs_max':2e-14,'wrong_transpose_global_difference_min':1e-9,'unshifted_global_difference_min':1e-9}
passed=bool(len(routes)==30 and max_closure<=thresholds['loop_closure_abs_max'] and min_wrong>=thresholds['wrong_transpose_global_difference_min'] and min_unshift>=thresholds['unshifted_global_difference_min'] and all(np.isfinite(r['matrix_max_abs']) and np.isfinite(r['trace_abs']) for r in routes))
result={
 'iteration':352,'model_readiness_percent':24,'scientific_gate_pass':passed,
 'classification':('PASS_U2_MATCHED_TIMELIKE_FULL_PHYSICAL_30_ROUTE_MATRIX_PRODUCTS_WITH_SHIFTED_ROUTING_AND_FUNCTIONAL_TRANSPOSE__FAMILY_REDUCTION_NEXT' if passed else 'FAIL_U2_TIMELIKE_FULL_PHYSICAL_30_ROUTE_PRODUCTS'),
 'candidate_residual':False,'census':{'raw_routes':30,'matrix_nonzero_routes':nonzero,'matrix_zero_routes':zero,'zero_threshold':zero_threshold},
 'validation':{'max_loop_closure_error':max_closure,'min_wrong_same_k_transpose_difference':min_wrong,'min_unshifted_routing_difference':min_unshift,'A_cache_states':len(A_CACHE),'ghost_cache_states':len(G_CACHE),'graviton_cache_states':len(H_CACHE),'thresholds':thresholds,'routes':routes},
 'scope':'FULL_PHYSICAL_ROUTE_MATRIX_PRODUCTS_AND_TRACES__NO_CUT_INTEGRATION',
 'guardrails':['NO_REUSE_OF_ITERATION346_NULL_SOFT_18_KILLS','NO_ZERO_FILL','ITERATION345_FUNCTIONAL_TRANSPOSE_BINDING','SHIFTED_INCOMING_MOMENTUM_BINDING','HINV_VD_MINUS_KINV_BINDING','NO_CUT_INTEGRATION_BEFORE_FAMILY_REDUCTION','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':'canonicalize the physical 30-route numerator/denominator families under allowed loop-momentum shifts without assuming numerator equivalence; classify local/scaleless/rational versus cut-capable origins before any Tr U2 cut integration'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
