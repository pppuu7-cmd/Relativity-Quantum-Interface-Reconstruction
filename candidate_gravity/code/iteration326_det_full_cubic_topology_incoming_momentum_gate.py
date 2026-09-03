#!/usr/bin/env python3
"""RQIR Iteration 326: full cubic-topology arbitrary-incoming-momentum H/N gate.

This is a new gate version after Iteration 325 exposed a coverage defect: the
pair/triple route inventory did not include the singleton cubic logdet term
Tr(G0 K3), so the (1,1,1) H3/N3 insertion could not be tested.  No physical
kernel, finite-difference step, or frozen threshold is changed here.

The full cubic logdet topology is now represented by:
  singleton: Tr(G0 K3)
  ordered pairs: -1/2 Tr(G0 K_a G0 K_b), a+b=(1,1,1)
  ordered triples: +1/3 Tr(G0 K_a G0 K_b G0 K_c), a+b+c=(1,1,1)
with every K insertion evaluated at the actual incoming p+Q_before_insertion.
"""
from __future__ import annotations
import contextlib, io, itertools, json, re
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
TARGET=(1,1,1)
D=4
QINT=[(27,-19,31,11),(-13,37,17,-29),(-14,-18,-48,18)]
P=np.array([.61,-.33,.24,.52],float)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def qint(a): return tuple(sum(a[r]*QINT[r][mu] for r in range(3)) for mu in range(D))
def nonzero_subindices(target):
    return [a for a in itertools.product(*(range(x+1) for x in target)) if any(a)]
NZ=nonzero_subindices(TARGET)

def singleton(): return [(TARGET,)]
def ordered_pairs(): return [(a,b) for a in NZ for b in NZ if add(a,b)==TARGET]
def ordered_triples():
    return [(a,b,c) for a in NZ for b in NZ for c in NZ if add(add(a,b),c)==TARGET]
def topology_sequences(): return singleton()+ordered_pairs()+ordered_triples()

def insertion_requests():
    req=set(); route_rows=[]
    for seq in topology_sequences():
        shift=(0,0,0,0); loc=[]
        for a in seq:
            req.add((shift,a)); loc.append((shift,a))
            qa=qint(a); shift=tuple(shift[i]+qa[i] for i in range(D))
        if shift!=(0,0,0,0): raise AssertionError((seq,shift))
        route_rows.append((seq,tuple(loc)))
    return sorted(req),route_rows

REQUESTS,ROUTES=insertion_requests()

def load_frozen_prefix(filename:str, marker:str, p_in:np.ndarray):
    src=(ROOT/filename).read_text().split(marker,1)[0]
    src,n=re.subn(r'^p=np\.array\([^\n]+\)$','p=P_IN.copy()',src,count=1,flags=re.M)
    if n!=1: raise RuntimeError(f'failed to replace p fixture in {filename}: {n}')
    ns={'P_IN':np.array(p_in,float)}
    with contextlib.redirect_stdout(io.StringIO()): exec(compile(src,filename,'exec'),ns,ns)
    return ns

def mixed_coeff_from_direct(direct,a,h):
    active=[r for r,x in enumerate(a) if x]
    if any(x not in (0,1) for x in a) or not active: raise ValueError(a)
    acc=None
    for signs in itertools.product((-1.0,1.0), repeat=len(active)):
        t=np.zeros(3,float); w=1.0
        for r,s in zip(active,signs): t[r]=s*h; w*=s
        v=np.asarray(direct(t))
        acc=w*v if acc is None else acc+w*v
    return acc/((2*h)**len(active))

def validate_sector(kind,filename,marker,dict_name,h,thresholds):
    by_shift={}
    for shift,a in REQUESTS: by_shift.setdefault(shift,[]).append(a)
    rows=[]; max_by_order={1:0.0,2:0.0,3:0.0}; counts={1:0,2:0,3:0}
    for shift,targets in sorted(by_shift.items()):
        p_in=P+np.array(shift,float)/100.0
        ns=load_frozen_prefix(filename,marker,p_in)
        coeffs=ns[dict_name]; direct=ns['direct']
        for a in sorted(set(targets)):
            order=sum(a); counts[order]+=1
            fd=mixed_coeff_from_direct(direct,a,h)
            err=float(np.max(np.abs(fd-coeffs[a])))
            scale=max(1.0,float(np.max(np.abs(coeffs[a]))))
            rel=err/scale; max_by_order[order]=max(max_by_order[order],rel)
            rows.append({'shift_int100':list(shift),'p_in':[float(x) for x in p_in],
                         'multiindex':list(a),'order':order,
                         'max_abs_error':err,'scale':scale,'scaled_error':rel})
    order_coverage=all(counts[k]>0 for k in (1,2,3))
    passed=order_coverage and all(max_by_order[k] < thresholds[k] for k in (1,2,3))
    return {'kind':kind,'request_count':len(rows),'finite_difference_h':h,
            'request_count_by_order':{str(k):counts[k] for k in counts},
            'all_orders_present':order_coverage,
            'max_scaled_error_by_order':{str(k):v for k,v in max_by_order.items()},
            'threshold_by_order':{str(k):thresholds[k] for k in thresholds},
            'requests':rows,'pass':bool(passed)}

# EXACTLY the same h and frozen thresholds as Iteration 325. They are not
# weakened after observing Iteration 325; only topology coverage is corrected.
ghost=validate_sector('ghost','iteration317_det_ghost_three_mode_routing.py',
    '# Multivariate direct fit.','N',2.0e-4,{1:2e-6,2:3e-4,3:8e-2})
grav=validate_sector('graviton','iteration319_det_graviton_three_mode_routing.py',
    'FIT=indices(4)','H',2.0e-4,{1:3e-6,2:5e-4,3:1.2e-1})

expected_unique=len(REQUESTS)
coverage=(ghost['request_count']==expected_unique and grav['request_count']==expected_unique)
nonzero_shift=any(any(x for x in s) for s,a in REQUESTS)
cubic_req=((0,0,0,0),TARGET) in REQUESTS
route_closure=all(
    tuple(sum(qint(a)[mu] for a in seq) for mu in range(D))==(0,0,0,0)
    for seq,_ in ROUTES)
# Frozen cubic topology cardinality: 1 singleton + 6 ordered pairs + 6 ordered triples.
topology_cardinality=(len(singleton())==1 and len(ordered_pairs())==6 and len(ordered_triples())==6 and len(ROUTES)==13)
ok=bool(coverage and nonzero_shift and cubic_req and route_closure and topology_cardinality and ghost['pass'] and grav['pass'])

result={
 'iteration':326,
 'model_readiness_percent':24,
 'scientific_gate_pass':ok,
 'classification':('PASS_PHYSICAL_HN_ARBITRARY_INCOMING_MOMENTUM_FULL_CUBIC_TOPOLOGY_CERTIFICATE' if ok else 'FAIL_PHYSICAL_HN_ARBITRARY_INCOMING_MOMENTUM_FULL_CUBIC_TOPOLOGY_CERTIFICATE'),
 'candidate_residual':False,
 'iteration325_resolution':'new gate version; adds missing singleton Tr(G0 K3) topology only; physical kernels, h, and thresholds unchanged',
 'scope':{
   'target_multiindex':list(TARGET),'closed_triad_q_int100':[list(x) for x in QINT],
   'singleton_count':len(singleton()),'ordered_pair_count':len(ordered_pairs()),'ordered_triple_count':len(ordered_triples()),
   'full_cubic_topology_sequence_count':len(ROUTES),'unique_incoming_shift_insertion_requests':expected_unique,
   'routing_rule':'evaluate frozen physical insertion K_a at incoming loop momentum p+Q_before_insertion',
   'validation_oracle':'same-parent exact geometry direct operator, symmetric mixed finite differences'
 },
 'checks':{'full_route_request_coverage':coverage,'nonzero_shifted_incoming_momenta_tested':nonzero_shift,
           'genuinely_cubic_111_insertion_tested':cubic_req,'all_routes_close':route_closure,
           'full_cubic_topology_cardinality':topology_cardinality,'ghost':ghost,'graviton':grav},
 'physical_status':{
   'shifted_denominator_routing_engine':'FROZEN_ITERATION_324',
   'ghost_N123_arbitrary_incoming_momentum':'FROZEN_IF_PASS',
   'graviton_H123_arbitrary_incoming_momentum':'FROZEN_IF_PASS',
   'full_cubic_HN_routing_layer_ready':bool(ok),
   'physical_cubic_determinant_trace_assembly_ready':bool(ok),
   'integrated_determinant_coefficient_ready':False
 },
 'guardrails':['NO_ZERO_FILL','NO_THRESHOLD_WEAKENING_AFTER_RUN','ITERATION325_NOT_RETROACTIVELY_EDITED','NO_SOURCE_BORN_SUBTRACTION_BEFORE_ORIGIN_CLASSIFICATION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5'],
 'next_gate':('assemble the physical cubic graviton-minus-ghost determinant trace with certified shifted denominators and routed H/N numerators; enumerate denominator families and classify pole/cut origins before any Source/Born subtraction' if ok else 'freeze this scoped FAIL and diagnose the failing full-topology routed insertion without threshold weakening or parent-dynamics changes')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not ok: raise SystemExit(2)
