#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 359.

Independent companion to the already-running Iteration 358.
Classify the 30 repeated-pole U2 families by exact loop-momentum multiplicity
pattern and freeze the only allowed ordinary-to-repeated cut reduction contract.

No discontinuity value is computed here.  In particular, this gate does not
replace a repeated pole by an ordinary simple Cutkosky delta.  Instead it records
the derivative order required by the distributional identity

  Disc[(D+i0)^(-m)] \propto delta^(m-1)(D)/(m-1)!

with the overall sign/2pi*i convention intentionally inherited from the frozen
repository simple-cut normalization at the later integration stage.
"""
from __future__ import annotations
import contextlib, io, json, math, runpy
from collections import Counter
from pathlib import Path
import numpy as np

ITERATION=359
ROOT=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    P355=runpy.run_path(str(ROOT/'iteration355_u2_heldout_physical_numerator_transport.py'), run_name='iteration359_parent355')
    P356=runpy.run_path(str(ROOT/'iteration356_u2_family_origin_topology_classification.py'), run_name='iteration359_parent356')

raw=P355['raw']; enumerate_subterms=P355['enumerate_subterms']; mdot=P355['mdot']
PREF=np.array([.43,-.27,.39,.21],dtype=float)
ROUND=12
TIMELIKE_TOL=2e-12

records=[]
pattern_counter=Counter()
max_mult=0
required_derivative_orders=Counter()
typed_repeated_channels=0

for fam in P356['records']:
    if not fam['has_repeated_pole_momentum']:
        continue
    route=int(fam['route']); subterm=int(fam['subterm'])
    s=enumerate_subterms(raw[route],PREF)[subterm]
    offsets=[]
    for sp,k in s['props']:
        off=np.asarray(k,float)-PREF
        offsets.append((sp,off))
    keys=[tuple(np.round(off,ROUND)) for _,off in offsets]
    counts=Counter(keys)
    multiplicities=sorted(counts.values(),reverse=True)
    max_mult=max(max_mult,max(multiplicities))
    pattern=tuple(multiplicities)
    pattern_counter[str(pattern)]+=1

    groups=[]
    for key,m in sorted(counts.items()):
        members=[idx for idx,k in enumerate(keys) if k==key]
        species=[offsets[idx][0] for idx in members]
        groups.append({'offset':list(key),'multiplicity':m,'members':members,'species':species,
                       'required_delta_derivative_order':m-1})
        if m>1:
            required_derivative_orders[m-1]+=1

    channels=[]
    # Collapse propagators to distinct momentum groups.  A timelike cut between
    # two groups is typed by the multiplicity carried by each cut denominator.
    for ia in range(len(groups)):
        for ib in range(ia+1,len(groups)):
            a=np.asarray(groups[ia]['offset'],float)
            b=np.asarray(groups[ib]['offset'],float)
            q=b-a
            q2=float(np.real(mdot(q)))
            if q2 < -TIMELIKE_TOL:
                ma=int(groups[ia]['multiplicity']); mb=int(groups[ib]['multiplicity'])
                ordinary=(ma==1 and mb==1)
                if not ordinary:
                    typed_repeated_channels+=1
                channels.append({'group_pair':[ia,ib],'q2':q2,
                                 'multiplicity_pair':[ma,mb],
                                 'derivative_orders':[ma-1,mb-1],
                                 'ordinary_simple_pair':ordinary,
                                 'repeated_pole_reduction_required':not ordinary})

    records.append({'route':route,'subterm':subterm,'propagator_count':len(offsets),
                    'distinct_momentum_offsets':len(groups),
                    'multiplicity_pattern':multiplicities,'groups':groups,
                    'timelike_distinct_group_channels':channels})

# Algebraic/distributional contract. For D_mu = D+mu^2,
# d^(m-1)/d(mu^2)^(m-1) [1/D_mu] = (-1)^(m-1)(m-1)!/D_mu^m.
# Therefore a repeated propagator can be generated from an auxiliary simple pole
# before taking the cut. This is an exact algebraic identity away from the pole
# and defines the distributional extension once the same i0 prescription is kept.
contract=[]
for m in range(2,max_mult+1):
    order=m-1
    coefficient=(-1)**order/math.factorial(order)
    contract.append({'pole_multiplicity':m,'auxiliary_mass_derivative_order':order,
                     'reconstruction_coefficient':coefficient,
                     'identity':f"1/(D+i0)^{m} = ({coefficient}) * d^{order}/d(mu2)^{order} [1/(D+mu2+i0)] at mu2=0"})

passed=bool(len(records)==30 and max_mult>=2 and typed_repeated_channels>0 and all(r['timelike_distinct_group_channels'] for r in records))
classification=('PASS_U2_REPEATED_POLE_MULTIPLICITY_AND_DERIVATIVE_DISTRIBUTIONAL_REDUCTION_CONTRACT'
                if passed else 'FAIL_U2_REPEATED_POLE_MULTIPLICITY_CONTRACT')
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':passed,
 'candidate_residual':False,'classification':classification,
 'census':{'repeated_pole_families':len(records),'maximum_pole_multiplicity':max_mult,
           'family_multiplicity_patterns':dict(pattern_counter),
           'repeated_group_count_by_required_delta_derivative_order':{str(k):v for k,v in sorted(required_derivative_orders.items())},
           'typed_timelike_distinct_group_channels_requiring_repeated_reduction':typed_repeated_channels},
 'derivative_contract':contract,
 'families':records,
 'scope':'REPEATED_POLE_METHOD_CONTRACT_ONLY__NO_DISCONTINUITY_VALUE__NO_SIMPLE_CUT_ZERO_FILL',
 'guardrails':['ITERATION357_REPEATED_FAMILIES_ONLY','AUXILIARY_MASS_DERIVATIVE_BEFORE_CUT','SAME_I0_PRESCRIPTION_REQUIRED',
               'OVERALL_DISC_SIGN_AND_2PII_INHERIT_REPOSITORY_NORMALIZATION_AT_INTEGRATION','REPEATED_POLE_NEVER_ORDINARY_SIMPLE_DELTA',
               'NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':('derive channel-resolved repeated-pole cut integrands by introducing one auxiliary mass-squared parameter per repeated distinct momentum group, applying the recorded derivative orders to the simple-massive cut representation, and only then taking mu2->0; validate against an independent distributional test-function oracle before physical integration')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed:
    raise SystemExit(2)
