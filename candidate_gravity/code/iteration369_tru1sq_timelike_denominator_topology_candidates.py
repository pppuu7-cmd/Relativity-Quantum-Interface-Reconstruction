#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 369.

Denominator-topology candidate classification for the 21 routed cyclic Tr(U1^2)
classes frozen by Iteration 368.  This gate uses only the exact propagator-factor
content implied by U1=Q_L A Q_R Y and the seven order-2 Leibniz primitives.

A common loop-momentum translation may identify denominator multisets.  Such an
identification is ONLY a topology candidate: no numerator equivalence, pole
cancellation, cut authority, or family quotient is claimed here.
"""
from __future__ import annotations
import json, numpy as np

ITERATION=369
LEGS=('s','a','b')
Q={'s':np.array([1.,0.,0.,0.]),'a':np.array([-.4,.1,.1,0.]),'b':np.array([-.6,-.1,-.1,0.])}
ROUND=12

def ksum(legs): return sum((Q[x] for x in legs),np.zeros(4))

def specs(pair):
    pair=tuple(pair); out=[{'extra_site':'V2','V2_legs':pair,'extra_local_legs':()}]
    for site in ('N_L','N_R','Y'):
        for v in pair:
            d=pair[1] if pair[0]==v else pair[0]
            out.append({'extra_site':site,'V2_legs':(v,), 'extra_local_legs':(d,)})
    return out

def denominator_shifts(singleton,pair,spec):
    """Canonical orientation A: second block acts first at base loop p."""
    qs=Q[singleton]; qp=ksum(pair)
    # singleton first-order U1 evaluated at p+qp: Q0(p) ... Q0(p+qp)
    sh=[np.zeros(4),qp.copy()]
    site=spec['extra_site']
    if site=='V2':
        sh += [qp.copy(),np.zeros(4)]
    else:
        v=spec['V2_legs'][0]; d=spec['extra_local_legs'][0]
        qv=Q[v]; qd=Q[d]
        if site=='N_L':
            # Q1[d](p+qv) A1[v](p) Q0(p)
            sh += [qv+qd,qv,np.zeros(4)]
        elif site=='N_R':
            # Q0(p+qpair) A1[v](p+qd) Q1[d](p)
            sh += [qp.copy(),qd,np.zeros(4)]
        elif site=='Y':
            # Q0(p+qpair) A1[v](p+qd) Q0(p+qd) Y1[d]
            sh += [qp.copy(),qd]
        else: raise ValueError(site)
    # closure check: qp=-qs
    assert np.max(np.abs(qp+qs))<1e-14
    return sh

def vec_key(v): return tuple(float(x) for x in np.round(v,ROUND))
def translated_canonical(shifts):
    """Translation-invariant multiset key: try every propagator shift as origin."""
    candidates=[]
    for a in shifts:
        rel=sorted(vec_key(s-a) for s in shifts)
        candidates.append(tuple(rel))
    return min(candidates)

rows=[]
for singleton in LEGS:
    pair=tuple(x for x in LEGS if x!=singleton)
    for i,spec in enumerate(specs(pair)):
        sh=denominator_shifts(singleton,pair,spec)
        key=translated_canonical(sh)
        mult={}
        for v in sh: mult[vec_key(v)]=mult.get(vec_key(v),0)+1
        rows.append({'class_id':len(rows)+1,'singleton_leg':singleton,'pair_legs':pair,'spec_index':i,
                     'second_order_spec':spec,'propagator_count':len(sh),
                     'denominator_shift_multiset':[list(vec_key(v)) for v in sh],
                     'raw_multiplicities':{str(k):v for k,v in sorted(mult.items())},
                     'translation_canonical_key':str(key),
                     'contains_repeated_shift':any(v>1 for v in mult.values()),
                     'max_shift_multiplicity':max(mult.values())})

assert len(rows)==21
groups={}
for r in rows: groups.setdefault(r['translation_canonical_key'],[]).append(r['class_id'])
classes=[{'candidate_group_id':i+1,'member_class_ids':ids,'member_count':len(ids)}
         for i,(_,ids) in enumerate(sorted(groups.items()))]
for g in classes:
    for cid in g['member_class_ids']: rows[cid-1]['candidate_group_id']=g['candidate_group_id']

# Internal translation oracle: members of a group must have the same propagator count
# and multiplicity pattern. This does not test physical numerators.
internal_ok=True
for g in classes:
    members=[rows[i-1] for i in g['member_class_ids']]
    signatures={(m['propagator_count'],tuple(sorted(int(v) for v in m['raw_multiplicities'].values()))) for m in members}
    internal_ok &= len(signatures)==1

passed=bool(internal_ok and len(rows)==21 and sum(g['member_count'] for g in classes)==21)
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':passed,'candidate_residual':False,
 'classification':('PASS_TRU1SQ_21_CYCLIC_CLASSES_RAW_DENOMINATOR_TRANSLATION_CANDIDATE_TOPOLOGY' if passed else 'FAIL_TRU1SQ_DENOMINATOR_TOPOLOGY_GATE'),
 'scope':'RAW_PROPAGATOR_DENOMINATOR_TOPOLOGY_ONLY__NO_NUMERATOR_EQUIVALENCE__NO_CUT',
 'authoritative_inputs':['Iteration 368 full 42-placement physical routing and 21 routed cyclic classes','frozen flat orbit inverse Q0/Q1 propagator factor order'],
 'counts':{'input_cyclic_classes':21,'translation_candidate_groups':len(classes),
           'multi_member_candidate_groups':sum(g['member_count']>1 for g in classes),
           'classes_with_repeated_shift':sum(r['contains_repeated_shift'] for r in rows)},
 'candidate_groups':classes,'rows':rows,
 'guardrails':['DENOMINATOR_EQUIVALENCE_IS_NOT_NUMERATOR_EQUIVALENCE','NO_FAMILY_QUOTIENT_IN_THIS_GATE','NO_POLE_CANCELLATION_ASSUMED',
               'NO_CUT_INTEGRATION','NO_ZERO_FILL','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('evaluate the full physical traced numerator for every multi-member denominator candidate at several held-out loop momenta after the exact candidate translation; merge only groups passing a frozen numerator-transport threshold, and separately test apparent repeated poles for numerator cancellation before cut classification' if passed else 'preserve FAIL and diagnose denominator routing only')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
