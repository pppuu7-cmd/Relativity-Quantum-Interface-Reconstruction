#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 356.

Freeze the physical U2 family partition after Iteration 355 and classify the
42 distinct additive numerator+denominator families by propagator origin before
any discontinuity integration.

This is a topology/origin gate only.  `CUT_CAPABLE_TOPOLOGY` means that a
family contains at least two distinct massless propagator momenta whose
separation is timelike on the frozen matched fixture.  It is NOT a certificate
that the integrated discontinuity is nonzero; numerator cancellation, repeated
poles and channel-specific reductions remain to be tested later.
"""
from __future__ import annotations
import contextlib, io, itertools, json, runpy
from collections import Counter
from pathlib import Path
import numpy as np

ITERATION=356
ROOT=Path(__file__).resolve().parent

# Load Iteration 353 only as frozen denominator-provenance machinery.  Suppress
# its printed result because this iteration is a new scientific authority.
with contextlib.redirect_stdout(io.StringIO()):
    P=runpy.run_path(str(ROOT/'iteration353_u2_timelike_denominator_subterm_census.py'), run_name='iteration356_parent353')

LEGS=P['LEGS']; ORDER=P['ORDER']; APPLY=P['APPLY']; q=P['q']; p0=P['p0']
raw=P['raw']; canonical=P['canonical']; qkey=P['qkey']; factor_subterms=P['factor_subterms']

def mdot(v):
    v=np.asarray(v,float)
    return float(-v[0]*v[0]+np.dot(v[1:],v[1:]))

def vkey(v): return tuple(float(np.round(x,12)) for x in np.asarray(v,float))

def expand_route(rid,a):
    cur=np.asarray(p0,float).copy(); factors=[]
    for name in APPLY:
        key=a[name]
        terms=factor_subterms(name,key,cur)
        factors.append((name,key,terms))
        cur=cur+qkey(key)
    out=[]
    for sid,choice in enumerate(itertools.product(*[x[2] for x in factors])):
        props=[]; pieces=[]
        for (name,key,_),term in zip(factors,choice):
            props += [(sp,np.asarray(k,float)) for sp,k in term['props']]
            pieces.append({'factor':name,'key':list(key),'piece':term['piece']})
        out.append({'route':rid,'subterm':sid,'props':props,'pieces':pieces})
    return out

# Frozen external channel invariants.  All are timelike in signature (-,+,+,+).
channel_q2={x:mdot(q[x]) for x in LEGS}
q2_match_tol=2e-12
timelike_tol=1e-12
records=[]
count_by_prop=Counter(); count_by_unique=Counter(); repeated_pattern=Counter(); channel_sets=Counter()
all_subterms=[]
for rid,a in enumerate(raw): all_subterms.extend(expand_route(rid,a))
assert len(all_subterms)==42

for s in all_subterms:
    props=s['props']
    offsets=[(sp,np.asarray(k,float)-np.asarray(p0,float)) for sp,k in props]
    scalar_mult=Counter(vkey(o) for _,o in offsets)
    unique=[np.asarray(k,float) for k in scalar_mult]
    pairs=[]; channels=set()
    for i in range(len(unique)):
        for j in range(i+1,len(unique)):
            d=unique[j]-unique[i]; q2=mdot(d)
            matched=[x for x,val in channel_q2.items() if abs(q2-val)<=q2_match_tol]
            if q2 < -timelike_tol:
                channels.update(matched)
            pairs.append({'delta':list(vkey(d)),'delta_sq':q2,'timelike':bool(q2 < -timelike_tol),'matched_external_channels':matched})
    cut_capable=any(p['timelike'] for p in pairs)
    if len(unique)==1:
        origin='SINGLE_SHIFT_SCALELESS_OR_LOCAL_ORIGIN'
    elif cut_capable:
        origin='CUT_CAPABLE_TOPOLOGY'
    else:
        origin='NO_DIRECT_TIMELIKE_TWO_PROPAGATOR_CUT_SUPPORT_ON_FIXTURE'
    multiplicities=tuple(sorted(scalar_mult.values(),reverse=True))
    repeated=any(x>1 for x in multiplicities)
    count_by_prop[len(props)]+=1; count_by_unique[len(unique)]+=1
    repeated_pattern[str((len(props),multiplicities))]+=1
    channel_sets[str(tuple(sorted(channels)))]+=1
    records.append({
      'route':s['route'],'subterm':s['subterm'],'origin_classification':origin,
      'propagator_count':len(props),'unique_scalar_denominator_shifts':len(unique),
      'scalar_denominator_multiplicities':list(multiplicities),'has_repeated_scalar_pole':repeated,
      'timelike_channels':sorted(channels),'pair_separations':pairs,
      'pieces':s['pieces'],
      'guardrail':'CUT_CAPABLE_TOPOLOGY_IS_NOT_NONZERO_DISCONTINUITY_CERTIFICATE'
    })

n_cut=sum(r['origin_classification']=='CUT_CAPABLE_TOPOLOGY' for r in records)
n_single=sum(r['origin_classification']=='SINGLE_SHIFT_SCALELESS_OR_LOCAL_ORIGIN' for r in records)
n_no=sum(r['origin_classification']=='NO_DIRECT_TIMELIKE_TWO_PROPAGATOR_CUT_SUPPORT_ON_FIXTURE' for r in records)
n_repeated=sum(r['has_repeated_scalar_pole'] for r in records)

# Expected frozen census from the matched triad; these are scientific assertions,
# not tunable fitting targets.  If they fail the gate fails closed.
passed=bool(
    len(records)==42 and n_cut==42 and n_single==0 and n_no==0 and
    count_by_prop==Counter({3:24,4:18}) and
    count_by_unique==Counter({3:30,2:12}) and
    n_repeated==30
)

result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':passed,'candidate_residual':False,
 'classification':('PASS_U2_42_DISTINCT_PHYSICAL_FAMILY_CUT_ORIGIN_CLASSIFICATION__ALL_CUT_CAPABLE_TOPOLOGIES__DISCONTINUITY_NOT_YET_CLAIMED' if passed else 'FAIL_U2_42_FAMILY_CUT_ORIGIN_CLASSIFICATION'),
 'census':{
   'frozen_distinct_numerator_denominator_families':len(records),
   'cut_capable_topologies':n_cut,
   'single_shift_scaleless_or_local_origins':n_single,
   'no_direct_timelike_pair_support':n_no,
   'families_with_repeated_scalar_poles':n_repeated,
   'by_total_propagator_count':dict(sorted(count_by_prop.items())),
   'by_unique_scalar_denominator_shifts':dict(sorted(count_by_unique.items())),
   'repeated_pole_patterns':dict(sorted(repeated_pattern.items())),
   'timelike_channel_set_census':dict(sorted(channel_sets.items())),
   'external_channel_q2':channel_q2
 },
 'thresholds':{'timelike_sq_negative_below':-timelike_tol,'external_q2_match_abs_max':q2_match_tol},
 'families':records,
 'scope':'KINEMATIC_ORIGIN_AND_PROPAGATOR_TOPOLOGY_ONLY__NO_NUMERATOR_INTEGRATION__NO_NONZERO_CUT_CLAIM',
 'guardrails':['ITERATION355_ZERO_NUMERATOR_EQUIVALENT_MERGES_BINDING','KEEP_ALL_42_FAMILIES_DISTINCT','CUT_CAPABLE_IS_NOT_NONZERO_DISCONTINUITY','REPEATED_POLES_REQUIRE_DEDICATED_REDUCTION','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':'derive a family-resolved direct timelike discontinuity reduction that handles the 30 repeated-pole families explicitly (derivative/distributional or equivalent analytic reduction) and the 12 three-simple-shift families separately; obtain zero/nonzero/BLOCKED per family before summing Tr U2'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
