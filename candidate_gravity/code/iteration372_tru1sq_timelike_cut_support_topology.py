#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 372.

Timelike two-line cut-support and singularity-type classification for all 21
physically distinct Tr(U1^2) families after Iteration 371 proved that every
apparent multiplicity-two raw denominator factor survives as a physical double
pole (36/36 tests, no cancellations, no BLOCKED cases).

This gate is topology/kinematics only. It enumerates unique denominator momentum
shifts with their physical multiplicities and all unordered pairs whose shift
difference is one of the three exact timelike external invariants q^2=-1,-0.14,
-0.34. Each channel is typed simple-simple, simple-double, or double-double.
No cut integral or ordinary-simple substitution is performed here.
"""
from __future__ import annotations
import json, numpy as np

ITERATION=372
ETA=np.diag([-1.,1.,1.,1.])
LEGS=('s','a','b')
Q={'s':np.array([1.,0.,0.,0.]),'a':np.array([-.4,.1,.1,0.]),'b':np.array([-.6,-.1,-.1,0.])}
TARGETS=[-1.0,-0.14,-0.34]
Q2_TOL=1e-12
ROUND=12

def ksum(legs): return sum((Q[x] for x in legs),np.zeros(4))
def specs(pair):
    pair=tuple(pair); out=[{'extra_site':'V2','V2_legs':pair,'extra_local_legs':()}]
    for site in ('N_L','N_R','Y'):
        for v in pair:
            d=pair[1] if pair[0]==v else pair[0]
            out.append({'extra_site':site,'V2_legs':(v,), 'extra_local_legs':(d,)})
    return out

def shifts(singleton,pair,spec):
    qp=ksum(pair); sh=[np.zeros(4),qp.copy()]
    site=spec['extra_site']
    if site=='V2': sh += [qp.copy(),np.zeros(4)]
    else:
        v=spec['V2_legs'][0]; d=spec['extra_local_legs'][0]
        qv=Q[v]; qd=Q[d]
        if site=='N_L': sh += [qv+qd,qv,np.zeros(4)]
        elif site=='N_R': sh += [qp.copy(),qd,np.zeros(4)]
        elif site=='Y': sh += [qp.copy(),qd]
        else: raise ValueError(site)
    return sh

def vk(v): return tuple(float(x) for x in np.round(v,ROUND))
def q2(v): return float(np.asarray(v,float)@ETA@np.asarray(v,float))
def target_q2(x):
    vals=[abs(x-t) for t in TARGETS]; i=int(np.argmin(vals))
    return TARGETS[i] if vals[i]<=Q2_TOL else None

families=[]; channels=[]
for singleton in LEGS:
    pair=tuple(x for x in LEGS if x!=singleton)
    for si,spec in enumerate(specs(pair)):
        cid=len(families)+1; raw=shifts(singleton,pair,spec)
        mult={}
        for s in raw: mult[vk(s)]=mult.get(vk(s),0)+1
        uniq=[np.array(k,float) for k in sorted(mult)]
        famch=[]
        for i in range(len(uniq)):
          for j in range(i+1,len(uniq)):
            dq=uniq[i]-uniq[j]; s2=q2(dq); tq=target_q2(s2)
            if tq is None: continue
            mi,mj=mult[vk(uniq[i])],mult[vk(uniq[j])]
            typ='simple-simple' if (mi,mj)==(1,1) else ('double-double' if mi==2 and mj==2 else 'simple-double')
            row={'class_id':cid,'q_squared':tq,'shift_i':uniq[i].tolist(),'shift_j':uniq[j].tolist(),
                 'multiplicity_i':mi,'multiplicity_j':mj,'singularity_type':typ}
            famch.append(row); channels.append(row)
        families.append({'class_id':cid,'singleton_leg':singleton,'pair_legs':pair,'spec_index':si,'spec':spec,
                         'unique_denominator_groups':len(uniq),'raw_factor_count':len(raw),
                         'max_multiplicity':max(mult.values()),'timelike_channels':famch,'timelike_channel_count':len(famch)})

assert len(families)==21
from collections import Counter
cnt=Counter(c['singularity_type'] for c in channels); qcnt=Counter(str(c['q_squared']) for c in channels)
# All repeated factors were physical by Iteration 371, so any multiplicity 2 here is authoritative double-pole topology.
no_channel=[f['class_id'] for f in families if not f['timelike_channels']]
passed=bool(channels and all(f['max_multiplicity']<=2 for f in families))
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':passed,'candidate_residual':False,
 'classification':('PASS_TRU1SQ_21_PHYSICAL_FAMILIES_TIMELIKE_CUT_SUPPORT_AND_SINGULARITY_TOPOLOGY' if passed else 'FAIL_TRU1SQ_CUT_SUPPORT_TOPOLOGY_GATE'),
 'scope':'TIMELIKE_TWO_LINE_CUT_SUPPORT_AND_POLE_MULTIPLICITY_ONLY__NO_INTEGRATION',
 'authoritative_inputs':['Iteration 370 all 21 cyclic classes physically distinct','Iteration 371 36/36 repeated factors survive as physical double poles'],
 'counts':{'physical_families':21,'timelike_channels':len(channels),'families_without_timelike_channel':len(no_channel),
           'simple_simple_channels':cnt['simple-simple'],'simple_double_channels':cnt['simple-double'],'double_double_channels':cnt['double-double'],
           'channels_by_q_squared':dict(qcnt)},
 'families_without_timelike_channel':no_channel,'families':families,'channels':channels,
 'guardrails':['REPEATED_MULTIPLICITY_FROM_ITERATION371_IS_PHYSICAL','SIMPLE_CUT_FORMULA_FORBIDDEN_ON_ANY_CHANNEL_CONTAINING_DOUBLE_POLE',
               'NO_CUT_INTEGRATION_IN_THIS_GATE','NO_ZERO_FILL','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('split TrU1sq channels by singularity type; certify on-shell regularity and all uncut-denominator separation for simple-simple channels, while simple-double/double-double channels require the already-frozen auxiliary-mass derivative/distributional machinery generalized to their exact multiplicities before normalized integration')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
