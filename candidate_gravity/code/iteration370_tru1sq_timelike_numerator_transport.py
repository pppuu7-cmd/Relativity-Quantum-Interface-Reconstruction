#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 370.

Physical numerator-transport test for the six multi-member raw denominator
translation candidates found in Iteration 369.

For each routed cyclic class we evaluate the full same-parent traced physical
integrand from Iteration 368, strip exactly the raw scalar propagator factors
identified in Iteration 369, and compare translated stripped numerators at
held-out loop momenta.  Denominator groups are merged only if a translation
passes the frozen physical numerator threshold.  Apparent repeated-pole
cancellation is deliberately deferred to the next gate.
"""
from __future__ import annotations
import contextlib, io, json
from pathlib import Path
import numpy as np

ITERATION=370
ROOT=Path(__file__).resolve().parent
SRC368=ROOT/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
# Reuse only setup and physical block definitions; do not execute Iteration-368 census/result.
src=SRC368.read_text().split('# Cache expensive same-parent blocks by routed loop momentum.',1)[0]
ns={'__name__':'iteration370_physical_parent','__file__':str(SRC368)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(src,str(SRC368),'exec'),ns,ns)
ETA=ns['ETA']; M=ns['M']; LEGS=ns['LEGS']; first_u1=ns['first_u1']; second_primitive=ns['second_primitive']; second_specs=ns['second_specs']; ksum=ns['ksum']

PROBES=[np.array([.43,-.27,.39,.21]),np.array([.61,.19,-.31,.47]),np.array([.37,.52,.28,-.41])]
TRANSPORT_TOL=2e-4
DENOM_SAFETY_MIN=1e-5
ROUND=12

F_CACHE={}; S_CACHE={}
def pkey(p): return tuple(np.round(np.asarray(p,float),14))
def F(x,p):
    key=(x,pkey(p))
    if key not in F_CACHE: F_CACHE[key]=first_u1(x,np.asarray(p,float))
    return F_CACHE[key]
def S(pair,spec,p):
    sk=(spec['extra_site'],tuple(spec['V2_legs']),tuple(spec['extra_local_legs']))
    key=(tuple(pair),sk,pkey(p))
    if key not in S_CACHE: S_CACHE[key]=second_primitive(pair,spec,np.asarray(p,float))
    return S_CACHE[key]

def amp(row,p):
    s=row['singleton_leg']; pair=row['pair_legs']; qp=ksum(pair)
    return np.trace(F(s,p+qp)@S(pair,row['spec'],p))

def denominator_shifts(row):
    s=row['singleton_leg']; pair=row['pair_legs']; spec=row['spec']; qp=ksum(pair)
    sh=[np.zeros(4),qp.copy()]
    site=spec['extra_site']
    if site=='V2': sh += [qp.copy(),np.zeros(4)]
    else:
        v=spec['V2_legs'][0]; d=spec['extra_local_legs'][0]
        qv=M[v][0]; qd=M[d][0]
        if site=='N_L': sh += [qv+qd,qv,np.zeros(4)]
        elif site=='N_R': sh += [qp.copy(),qd,np.zeros(4)]
        elif site=='Y': sh += [qp.copy(),qd]
        else: raise ValueError(site)
    return sh

def vk(v): return tuple(float(x) for x in np.round(v,ROUND))
def cankey(sh):
    return min(tuple(sorted(vk(s-a) for s in sh)) for a in sh)
def same_multiset(A,B,t):
    return sorted(vk(x) for x in A)==sorted(vk(x+t) for x in B)
def translations(A,B):
    out=[]
    for a in A:
      for b in B:
        t=a-b
        if same_multiset(A,B,t) and not any(np.max(np.abs(t-u))<1e-12 for u in out): out.append(t)
    return sorted(out,key=lambda x:vk(x))
def mdot(v): return complex(np.asarray(v,complex)@ETA@np.asarray(v,complex))
def stripped(row,p):
    sh=denominator_shifts(row); den=1+0j; mind=float('inf')
    for s in sh:
        d=mdot(p+s); den*=d; mind=min(mind,abs(d))
    return amp(row,p)*den,mind

rows=[]
for singleton in LEGS:
    pair=tuple(x for x in LEGS if x!=singleton)
    for i,spec in enumerate(second_specs(pair)):
        r={'class_id':len(rows)+1,'singleton_leg':singleton,'pair_legs':pair,'spec_index':i,'spec':spec}
        r['shifts']=denominator_shifts(r); r['key']=cankey(r['shifts']); rows.append(r)
groups={}
for r in rows: groups.setdefault(r['key'],[]).append(r)
multi=[g for g in groups.values() if len(g)>1]
assert len(rows)==21 and len(groups)==15 and len(multi)==6

comparisons=[]; passed_pairs=0; total_pairs=0; global_min_den=float('inf')
for gi,g in enumerate(multi,1):
    ref=g[0]
    for other in g[1:]:
        total_pairs+=1; candidates=translations(ref['shifts'],other['shifts']); assert candidates
        best=None
        for t in candidates:
            A=[]; B=[]; min_den=float('inf')
            for p in PROBES:
                na,da=stripped(ref,p); nb,db=stripped(other,p-t)  # shifts_B at p-t map to shifts_A at p when t=A-B
                A.append(na); B.append(nb); min_den=min(min_den,da,db)
            scale=max([abs(z) for z in A+B]+[1e-30])
            err=max(abs(a-b) for a,b in zip(A,B))/scale
            cand={'translation':t.tolist(),'max_scaled_numerator_transport_error':float(err),'min_abs_raw_denominator':float(min_den),
                  'ref_values':[[float(z.real),float(z.imag)] for z in A],'other_translated_values':[[float(z.real),float(z.imag)] for z in B]}
            if best is None or cand['max_scaled_numerator_transport_error']<best['max_scaled_numerator_transport_error']: best=cand
        global_min_den=min(global_min_den,best['min_abs_raw_denominator'])
        eq=bool(best['max_scaled_numerator_transport_error']<=TRANSPORT_TOL and best['min_abs_raw_denominator']>=DENOM_SAFETY_MIN)
        passed_pairs+=int(eq)
        comparisons.append({'candidate_group':gi,'ref_class_id':ref['class_id'],'other_class_id':other['class_id'],
                            'denominator_translation_count':len(candidates),'numerator_equivalent':eq,'best_translation_test':best})

# This gate passes scientifically whether equivalences survive or fail: negative quotient results are valid.
gate_pass=bool(total_pairs==6 and global_min_den>=DENOM_SAFETY_MIN and all(np.isfinite(c['best_translation_test']['max_scaled_numerator_transport_error']) for c in comparisons))
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':gate_pass,'candidate_residual':False,
 'classification':('PASS_TRU1SQ_PHYSICAL_NUMERATOR_TRANSPORT_TEST__'+str(passed_pairs)+'_OF_'+str(total_pairs)+'_MULTIMEMBER_DENOMINATOR_PAIRS_EQUIVALENT' if gate_pass else 'BLOCKED_TRU1SQ_NUMERATOR_TRANSPORT_NUMERICAL_PREREQUISITE'),
 'scope':'PHYSICAL_TRACED_NUMERATOR_TRANSPORT_FOR_MULTI_MEMBER_DENOMINATOR_CANDIDATES_ONLY__NO_REPEATED_POLE_CANCELLATION_TEST__NO_CUT',
 'thresholds':{'numerator_transport_scaled_max':TRANSPORT_TOL,'heldout_raw_denominator_abs_min':DENOM_SAFETY_MIN},
 'counts':{'input_cyclic_classes':21,'denominator_candidate_groups':15,'multi_member_groups':6,'tested_pairs':total_pairs,
           'numerator_equivalent_pairs':passed_pairs,'numerator_inequivalent_pairs':total_pairs-passed_pairs},
 'global_min_abs_raw_denominator_on_heldout_probes':global_min_den,'comparisons':comparisons,
 'guardrails':['NEGATIVE_NUMERATOR_EQUIVALENCE_IS_A_VALID_RESULT','MERGE_ONLY_NUMERATOR_PLUS_DENOMINATOR_EQUIVALENT_GROUPS',
               'APPARENT_REPEATED_POLES_NOT_YET_PHYSICAL_POLE_AUTHORITY','NO_CUT_INTEGRATION','NO_ZERO_FILL','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('freeze numerator+denominator families using only passed transport pairs; then test each apparent repeated denominator shift for physical numerator cancellation on the corresponding massless shell before assigning simple/repeated cut topology' if gate_pass else 'preserve BLOCKED and improve only held-out numerical stability without weakening thresholds')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not gate_pass: raise SystemExit(2)
