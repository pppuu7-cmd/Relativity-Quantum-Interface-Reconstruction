#!/usr/bin/env python3
"""RQIR Iteration 325: arbitrary-incoming-momentum H/N numerator routing gate.

Uses the already-frozen Iteration-317 ghost and Iteration-319 graviton physical
same-parent implementations without changing their dynamics.  Their fixed test
loop momentum is replaced at runtime by each p+Q required by the Iteration-324
ordered closed-trace routes.  For every unique (incoming shift, insertion
multiindex) actually used by the cubic determinant topology, the polynomial
insertion coefficient is checked against an independent exact-geometry oracle
using symmetric mixed finite differences.

Only binary Fourier multiindices occur for the closed target (1,1,1), so mixed
finite differences directly return the desired Taylor coefficient.  Unsupported
objects are never zero-filled.
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

def ordered_pairs(): return [(a,b) for a in NZ for b in NZ if add(a,b)==TARGET]
def ordered_triples():
    return [(a,b,c) for a in NZ for b in NZ for c in NZ if add(add(a,b),c)==TARGET]

def insertion_requests():
    req=set()
    for seq in ordered_pairs()+ordered_triples():
        shift=(0,0,0,0)
        for a in seq:
            req.add((shift,a))
            qa=qint(a); shift=tuple(shift[i]+qa[i] for i in range(D))
        assert shift==(0,0,0,0)
    return sorted(req)

REQUESTS=insertion_requests()

def load_frozen_prefix(filename:str, marker:str, p_in:np.ndarray):
    src=(ROOT/filename).read_text()
    src=src.split(marker,1)[0]
    # Both frozen sources have exactly one top-level p=np.array(...) fixture line.
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
    rows=[]; max_by_order={1:0.0,2:0.0,3:0.0}
    for shift,targets in sorted(by_shift.items()):
        p_in=P+np.array(shift,float)/100.0
        ns=load_frozen_prefix(filename,marker,p_in)
        coeffs=ns[dict_name]; direct=ns['direct']
        for a in sorted(set(targets)):
            order=sum(a)
            fd=mixed_coeff_from_direct(direct,a,h)
            err=float(np.max(np.abs(fd-coeffs[a])))
            scale=max(1.0,float(np.max(np.abs(coeffs[a]))))
            rel=err/scale
            max_by_order[order]=max(max_by_order[order],rel)
            rows.append({'shift_int100':list(shift),'p_in':[float(x) for x in p_in],
                         'multiindex':list(a),'order':order,
                         'max_abs_error':err,'scale':scale,'scaled_error':rel})
    passed=all(max_by_order[k] < thresholds[k] for k in (1,2,3))
    return {'kind':kind,'request_count':len(rows),'finite_difference_h':h,
            'max_scaled_error_by_order':{str(k):v for k,v in max_by_order.items()},
            'threshold_by_order':{str(k):thresholds[k] for k in thresholds},
            'requests':rows,'pass':bool(passed)}

# h and thresholds are frozen before this Action is run. They are deliberately
# looser than Iterations 317/319 polynomial-fit thresholds because this gate uses
# subtraction-based mixed finite differences rather than a global degree-4 fit.
ghost=validate_sector('ghost','iteration317_det_ghost_three_mode_routing.py',
    '# Multivariate direct fit.','N',2.0e-4,{1:2e-6,2:3e-4,3:8e-2})
grav=validate_sector('graviton','iteration319_det_graviton_three_mode_routing.py',
    'FIT=indices(4)','H',2.0e-4,{1:3e-6,2:5e-4,3:1.2e-1})

# Every Iteration-324 insertion location must have been tested exactly once after
# duplicate route requests are quotiented by identical (incoming shift,index).
expected_unique=len(REQUESTS)
coverage=(ghost['request_count']==expected_unique and grav['request_count']==expected_unique)
# Require genuinely shifted incoming momenta and cubic H3/N3 at p itself.
nonzero_shift=any(any(x for x in s) for s,a in REQUESTS)
cubic_present=any(a==(1,1,1) for s,a in REQUESTS)
ok=bool(coverage and nonzero_shift and cubic_present and ghost['pass'] and grav['pass'])

result={
 'iteration':325,
 'model_readiness_percent':24,
 'scientific_gate_pass':ok,
 'classification':('PASS_PHYSICAL_HN_ARBITRARY_INCOMING_MOMENTUM_ROUTED_NUMERATOR_CERTIFICATE' if ok else 'FAIL_PHYSICAL_HN_ARBITRARY_INCOMING_MOMENTUM_ROUTED_NUMERATOR_CERTIFICATE'),
 'candidate_residual':False,
 'scope':{
   'target_multiindex':list(TARGET),'closed_triad_q_int100':[list(x) for x in QINT],
   'ordered_pair_count':len(ordered_pairs()),'ordered_triple_count':len(ordered_triples()),
   'unique_incoming_shift_insertion_requests':expected_unique,
   'routing_rule':'evaluate frozen physical insertion K_a at incoming loop momentum p+Q_before_insertion',
   'validation_oracle':'same-parent exact geometry direct operator, symmetric mixed finite differences'
 },
 'checks':{'full_route_request_coverage':coverage,'nonzero_shifted_incoming_momenta_tested':nonzero_shift,
           'genuinely_cubic_111_insertion_tested':cubic_present,'ghost':ghost,'graviton':grav},
 'physical_status':{
   'shifted_denominator_routing_engine':'FROZEN_ITERATION_324',
   'ghost_N123_arbitrary_incoming_momentum':'FROZEN_IF_PASS',
   'graviton_H123_arbitrary_incoming_momentum':'FROZEN_IF_PASS',
   'physical_cubic_determinant_integrand_ready':bool(ok),
   'denominator_family_reduction_ready':bool(ok)
 },
 'guardrails':['NO_ZERO_FILL','NO_THRESHOLD_WEAKENING_AFTER_RUN','NO_SOURCE_BORN_SUBTRACTION_BEFORE_ORIGIN_CLASSIFICATION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5'],
 'next_gate':('assemble the full physical cubic determinant trace with jointly certified shifted denominators and H/N numerators; classify denominator families and pole/cut origins before any Source/Born subtraction' if ok else 'preserve scientific FAIL; diagnose the failing routed H/N insertion without weakening frozen thresholds or changing parent dynamics')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not ok: raise SystemExit(2)
