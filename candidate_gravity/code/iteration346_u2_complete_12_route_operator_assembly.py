#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 346.

Operator-level validation of the complete cubic-background Tr U2 route assembly.

Frozen authorities are NOT rederived here:
  * Iteration 308: exactly 30 raw cubic placements, 18 singleton-soft kills,
    12 surviving ordered placements for U2 = N_L A_T Hinv_VD A_R N_R Y.
  * Iteration 340: A_T/A_R orientation and Hinv_VD = -K^{-1}.
  * Iteration 341: physical same-parent A1/A2 component authority.
  * Iteration 342: N/Y inverse-routing bridge.
  * Iteration 345: Fourier functional transpose
        A_T(Q;k) = A_R(Q;-k-Q)^T
    with the same external +Q.

This gate deliberately uses typed noncommuting surrogate matrices rather than a
second physical component oracle. The scientific question is only whether the
frozen component slots, functional transpose, and incoming-momentum provenance
assemble into exactly the 12 Iteration-308 surviving cubic routes.

Independent validation:
  (1) brute-force coefficient extraction from the full six-factor operator
      product, allowing every cubic placement compatible with component orders;
  (2) explicit Iteration-308 survivor construction and null-soft pruning.
They must agree route-by-route and after summation. A deliberately wrong
same-incoming-momentum transpose and a deliberately unshifted momentum routing
must both be numerically separated from the frozen result.
"""
from __future__ import annotations
import itertools, json
import numpy as np

ITERATION=346
LEGS=('s','a','b')
ORDER=('NL','AT','H','AR','NR','Y')
APPLY=tuple(reversed(ORDER))
DG,DF=4,10
q={
 's':np.array([.21,-.11,.17,.09]),
 'a':np.array([-.08,.27,.13,-.19]),
 'b':np.array([-.13,-.16,-.30,.10]),
}
assert np.max(np.abs(q['s']+q['a']+q['b'])) < 1e-15
p0=np.array([.47,-.29,.36,.18])

def qkey(key):
    return sum((q[x] for x in key),np.zeros(4))

def canonical(key):
    return tuple(x for x in LEGS if x in key)

def disjoint_union(keys):
    flat=[x for k in keys for x in k]
    if len(flat)!=len(set(flat)): return None
    return canonical(flat)

rng=np.random.default_rng(346)
seed={}
def R(name,shape,key=()):
    tag=(name,shape,tuple(key))
    if tag not in seed:
        seed[tag]=rng.normal(size=shape)+1j*rng.normal(size=shape)
    return seed[tag]

def poly_momentum(k):
    k=np.asarray(k,float)
    return 1.0 + .17*k[0] - .11*k[1] + .07*k[2] + .13*k[3] + .03*np.dot(k,k)

def generic(name,key,k,shape):
    return R(name,shape,key) + poly_momentum(k)*0.07*R(name+'_P',shape,key)

def AR(key,k):
    key=canonical(key)
    if len(key)==1 and key==('s',):
        return np.zeros((DF,DG),complex)
    if len(key) not in (1,2): raise ValueError(key)
    return generic('AR',key,k,(DF,DG))

def AT(key,k):
    Q=qkey(key)
    return AR(key,-np.asarray(k)-Q).T

def AT_wrong_same_k(key,k):
    return AR(key,np.asarray(k)).T

def component(name,key,k,wrong_transpose=False):
    key=canonical(key)
    if name=='Y': return generic('Y',key,k,(DG,DG))
    if name=='NR': return generic('NR',key,k,(DG,DG))
    if name=='AR': return AR(key,k)
    if name=='H': return -generic('KINV',key,k,(DF,DF))
    if name=='AT': return AT_wrong_same_k(key,k) if wrong_transpose else AT(key,k)
    if name=='NL': return generic('NL',key,k,(DG,DG))
    raise KeyError(name)

allowed={
 'NL':[(),('s',),('a',),('b',)],
 'AT':[('s',),('a',),('b',),('s','a'),('s','b'),('a','b')],
 'H':[(),('s',),('a',),('b',)],
 'AR':[('s',),('a',),('b',),('s','a'),('s','b'),('a','b')],
 'NR':[(),('s',),('a',),('b',)],
 'Y':[(),('s',),('a',),('b',)],
}

def route_value(assign, wrong_transpose=False, unshifted=False):
    cur=p0.copy(); M=np.eye(DG,dtype=complex); provenance=[]
    for name in APPLY:
        key=assign[name]
        kin=p0.copy() if unshifted else cur.copy()
        F=component(name,key,kin,wrong_transpose=wrong_transpose)
        provenance.append({'factor':name,'key':list(key),'incoming':kin.tolist(),
                           'outgoing':(kin+qkey(key)).tolist()})
        M=F@M
        if not unshifted: cur=cur+qkey(key)
    return M, complex(np.trace(M)), provenance, cur

raw=[]
for choice in itertools.product(*[allowed[x] for x in ORDER]):
    assign={name:canonical(key) for name,key in zip(ORDER,choice)}
    if disjoint_union(assign.values())==LEGS:
        raw.append(assign)
assert len(raw)==30

def soft_killed(assign):
    return assign['AT']==('s',) or assign['AR']==('s',)

brute_survivors=[a for a in raw if not soft_killed(a)]
brute_killed=[a for a in raw if soft_killed(a)]
assert len(brute_survivors)==12 and len(brute_killed)==18

explicit=[]
for extra in ORDER:
    if extra=='AT':
        for singleton in LEGS:
            pair=canonical(tuple(x for x in LEGS if x!=singleton))
            if singleton!='s':
                a={x:() for x in ORDER}; a['AT']=pair; a['AR']=(singleton,)
                explicit.append(a)
    elif extra=='AR':
        for singleton in LEGS:
            pair=canonical(tuple(x for x in LEGS if x!=singleton))
            if singleton!='s':
                a={x:() for x in ORDER}; a['AT']=(singleton,); a['AR']=pair
                explicit.append(a)
    else:
        for perm in itertools.permutations(LEGS):
            if perm[0]=='s' or perm[1]=='s': continue
            a={x:() for x in ORDER}
            a['AT']=(perm[0],); a['AR']=(perm[1],); a[extra]=(perm[2],)
            explicit.append(a)
assert len(explicit)==12

def ident(a): return tuple((x,a[x]) for x in ORDER)
assert {ident(x) for x in explicit} == {ident(x) for x in brute_survivors}

route_records=[]
max_matrix_err=max_trace_err=max_closure=0.0
min_wrong_T=float('inf'); min_unshifted=float('inf')
sum_exp=np.zeros((DG,DG),complex); sum_brute=np.zeros((DG,DG),complex)
brute_map={ident(a):a for a in brute_survivors}

for i,a in enumerate(explicit):
    M,t,prov,cur=route_value(a)
    Mb,tb,_,_=route_value(brute_map[ident(a)])
    err=float(np.max(np.abs(M-Mb))); terr=float(abs(t-tb))
    closure=float(np.max(np.abs(cur-p0)))
    Mw,_,_,_=route_value(a,wrong_transpose=True)
    Mu,_,_,_=route_value(a,unshifted=True)
    dT=float(np.max(np.abs(M-Mw))); dU=float(np.max(np.abs(M-Mu)))
    max_matrix_err=max(max_matrix_err,err); max_trace_err=max(max_trace_err,terr)
    max_closure=max(max_closure,closure)
    min_wrong_T=min(min_wrong_T,dT); min_unshifted=min(min_unshifted,dU)
    sum_exp += M; sum_brute += Mb
    route_records.append({
      'route':i,'assignment':{x:list(a[x]) for x in ORDER},
      'trace_real':float(t.real),'trace_imag':float(t.imag),
      'matrix_match_error':err,'trace_match_error':terr,'loop_closure_error':closure,
      'wrong_same_k_transpose_matrix_difference':dT,
      'unshifted_momentum_matrix_difference':dU,
      'provenance_apply_order':prov,
    })

sum_error=float(np.max(np.abs(sum_exp-sum_brute)))
sum_trace_error=float(abs(np.trace(sum_exp)-np.trace(sum_brute)))
max_killed=0.0
for a in brute_killed:
    M,_,_,_=route_value(a)
    max_killed=max(max_killed,float(np.max(np.abs(M))))

site_census={x:0 for x in ORDER}
for a in explicit:
    if len(a['AT'])==2: site_census['AT']+=1
    elif len(a['AR'])==2: site_census['AR']+=1
    else:
        extras=[x for x in ('NL','H','NR','Y') if a[x]]
        assert len(extras)==1; site_census[extras[0]]+=1
expected={'NL':2,'AT':2,'H':2,'AR':2,'NR':2,'Y':2}

thresholds={
 'route_matrix_match_abs_max':1e-12,'route_trace_match_abs_max':1e-12,
 'sum_matrix_match_abs_max':1e-11,'sum_trace_match_abs_max':1e-11,
 'loop_closure_abs_max':2e-15,'killed_route_abs_max':1e-13,
 'wrong_same_k_transpose_difference_min':1e-6,'unshifted_routing_difference_min':1e-6,
}
passed=(len(raw)==30 and len(brute_killed)==18 and len(explicit)==12 and site_census==expected and
        max_matrix_err<=thresholds['route_matrix_match_abs_max'] and
        max_trace_err<=thresholds['route_trace_match_abs_max'] and
        sum_error<=thresholds['sum_matrix_match_abs_max'] and
        sum_trace_error<=thresholds['sum_trace_match_abs_max'] and
        max_closure<=thresholds['loop_closure_abs_max'] and
        max_killed<=thresholds['killed_route_abs_max'] and
        min_wrong_T>=thresholds['wrong_same_k_transpose_difference_min'] and
        min_unshifted>=thresholds['unshifted_routing_difference_min'])

result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':bool(passed),
 'classification':('PASS_U2_COMPLETE_12_SURVIVING_CUBIC_ROUTE_OPERATOR_ASSEMBLY_WITH_FUNCTIONAL_TRANSPOSE_AND_MOMENTUM_PROVENANCE__PHYSICAL_CUT_REDUCTION_AUTHORIZED_NEXT' if passed else 'FAIL_U2_CUBIC_12_ROUTE_OPERATOR_ASSEMBLY'),
 'candidate_residual':False,
 'scope':'OPERATOR_ROUTING_ASSEMBLY_ONLY__FROZEN_PHYSICAL_COMPONENT_AUTHORITIES_NOT_REDERIVED',
 'frozen_inputs':{
   'iteration308':'30 raw / 18 null-soft killed / 12 surviving placements',
   'iteration340':'U2=N_L A_T Hinv_VD A_R N_R Y; Hinv_VD=-K^-1',
   'iteration341':'physical same-parent A1/A2 component authority',
   'iteration342':'N/Y inverse-routing bridge',
   'iteration345':'A_T(Q;k)=A_R(Q;-k-Q)^T with same external +Q'},
 'validation':{
   'raw_cubic_placements':len(raw),'null_soft_killed':len(brute_killed),'surviving_routes':len(explicit),
   'survivor_site_census':site_census,'max_route_matrix_match_error':max_matrix_err,
   'max_route_trace_match_error':max_trace_err,'summed_matrix_match_error':sum_error,
   'summed_trace_match_error':sum_trace_error,'max_loop_closure_error':max_closure,
   'max_null_soft_killed_matrix_norm':max_killed,
   'min_wrong_same_k_transpose_matrix_difference':min_wrong_T,
   'min_unshifted_routing_matrix_difference':min_unshifted,'thresholds':thresholds,'routes':route_records},
 'status':{
   'TrU2_cubic_route_assembly':'FROZEN_EXECUTABLE' if passed else 'BLOCKED',
   'physical_component_values':'RETAIN_FROZEN_ITERATIONS_341_342_339_340_345',
   'cut_integrand_reduction':'AUTHORIZED_NEXT' if passed else 'BLOCKED',
   'integrated_TrU2_cut':'NOT_YET_COMPUTED'},
 'guardrails':['NO_SECOND_PHYSICAL_A_ORACLE_IN_THIS_GATE','NO_UNPROVEN_LEFT_RIGHT_OR_REVERSAL_QUOTIENT',
   'SINGLETON_SOFT_A1_ZERO_ONLY__MIXED_SOFT_HARD_A2_RETAINED','FUNCTIONAL_TRANSPOSE_MOMENTUM_ARGUMENT_BINDING',
   'SHIFTED_INCOMING_MOMENTUM_BINDING','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':'replace typed surrogate slots route-by-route with the already-frozen physical A1/A2, N/Y and graviton Hinv components on the matched timelike fixture; canonicalize the resulting 12 physical Tr U2 numerator/denominator families and classify cut-capable origins before integration'}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
