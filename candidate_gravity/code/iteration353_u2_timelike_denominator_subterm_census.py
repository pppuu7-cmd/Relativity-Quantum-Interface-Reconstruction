#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 353.

Expand the 30 matched-timelike physical U2 routes into denominator subterms
before any family quotient or cut integration.

This gate uses only already-frozen algebraic inverse-routing structure:
  * Nupper_0 = Q0 Y0: one ghost propagator;
  * Nupper_1 = Q0_out Y1 - Q0_out N1 Q0_in Y0: additive one-ghost and
    two-ghost denominator subterms;
  * Hinv_0 = -G0: one graviton propagator;
  * Hinv_1 = +G0_out K1 G0_in: two graviton propagators (because Hinv=-K^-1);
  * A_T/A_R and Y carry no inverse free propagator by themselves.

The scientific purpose is to prevent a fixed-momentum route matrix from being
mistaken for a single denominator family. Denominator equivalence alone is NOT
numerator equivalence. This census freezes denominator momentum provenance only.
"""
from __future__ import annotations
import itertools, json
import numpy as np

ITERATION=353
LEGS=('s','a','b')
ORDER=('NL','AT','H','AR','NR','Y')
APPLY=tuple(reversed(ORDER))
q={
 's':np.array([1.0,0.0,0.0,0.0]),
 'a':np.array([-0.4,0.1,0.1,0.0]),
 'b':np.array([-0.6,-0.1,-0.1,0.0]),
}
p0=np.array([.43,-.27,.39,.21])

def canonical(key): return tuple(x for x in LEGS if x in key)
def qkey(key): return sum((q[x] for x in key),np.zeros(4))
def disjoint_union(keys):
    flat=[x for k in keys for x in k]
    if len(flat)!=len(set(flat)): return None
    return canonical(flat)
def ktuple(k): return tuple(float(np.round(x,14)) for x in np.asarray(k,float))

allowed={
 'NL':[(),('s',),('a',),('b',)],
 'AT':[('s',),('a',),('b',),('s','a'),('s','b'),('a','b')],
 'H':[(),('s',),('a',),('b',)],
 'AR':[('s',),('a',),('b',),('s','a'),('s','b'),('a','b')],
 'NR':[(),('s',),('a',),('b',)],
 'Y':[(),('s',),('a',),('b',)],
}
raw=[]
for choice in itertools.product(*[allowed[x] for x in ORDER]):
    a={name:canonical(key) for name,key in zip(ORDER,choice)}
    if disjoint_union(a.values())==LEGS: raw.append(a)
assert len(raw)==30

# Each term is a list of propagator labels (species, incoming momentum).
# Incoming momentum is the argument of the flat inverse propagator.
def factor_subterms(name,key,kin):
    key=canonical(key); kin=np.asarray(kin,float); kout=kin+qkey(key)
    if name in ('AT','AR','Y'):
        return [{'piece':'local_vertex','props':[]}]
    if name in ('NL','NR'):
        if len(key)==0:
            return [{'piece':'Q0_Y0','props':[('ghost',ktuple(kin))]}]
        if len(key)==1:
            return [
              {'piece':'Q0out_Y1','props':[('ghost',ktuple(kout))]},
              {'piece':'minus_Q0out_N1_Q0in_Y0','props':[('ghost',ktuple(kout)),('ghost',ktuple(kin))]},
            ]
        raise ValueError((name,key))
    if name=='H':
        if len(key)==0:
            return [{'piece':'minus_G0','props':[('graviton',ktuple(kin))]}]
        if len(key)==1:
            return [{'piece':'plus_G0out_K1_G0in','props':[('graviton',ktuple(kout)),('graviton',ktuple(kin))]}]
        raise ValueError((name,key))
    raise KeyError(name)

def canonical_signature(props):
    # Exact denominator multiset only; no numerator quotient is claimed.
    return tuple(sorted(props,key=lambda x:(x[0],x[1])))

route_records=[]; all_subterms=[]; max_closure=0.0
for rid,a in enumerate(raw):
    cur=p0.copy(); factor_terms=[]; provenance=[]
    for name in APPLY:
        key=a[name]; kin=cur.copy(); kout=kin+qkey(key)
        terms=factor_subterms(name,key,kin)
        factor_terms.append((name,key,terms))
        provenance.append({'factor':name,'key':list(key),'incoming':kin.tolist(),'outgoing':kout.tolist(),'additive_piece_count':len(terms)})
        cur=kout
    closure=float(np.max(np.abs(cur-p0))); max_closure=max(max_closure,closure)
    expanded=[]
    for choices in itertools.product(*[x[2] for x in factor_terms]):
        props=[]; pieces=[]
        for (name,key,_),term in zip(factor_terms,choices):
            props.extend(term['props']); pieces.append({'factor':name,'key':list(key),'piece':term['piece']})
        sig=canonical_signature(props)
        species={'ghost':sum(1 for x in props if x[0]=='ghost'),'graviton':sum(1 for x in props if x[0]=='graviton')}
        rec={'route':rid,'subterm':len(expanded),'pieces':pieces,'denominator_signature':[[sp,list(k)] for sp,k in sig],
             'ghost_propagator_count':species['ghost'],'graviton_propagator_count':species['graviton'],'total_propagator_count':len(props)}
        expanded.append(rec); all_subterms.append(rec)
    route_records.append({'route':rid,'assignment':{x:list(a[x]) for x in ORDER},'loop_closure_error':closure,'additive_subterm_count':len(expanded),'provenance_apply_order':provenance,'subterms':expanded})

# Census exact denominator multisets without quotienting numerators.
families={}
for r in all_subterms:
    sig=tuple((x[0],tuple(x[1])) for x in r['denominator_signature'])
    families.setdefault(sig,[]).append((r['route'],r['subterm']))
family_records=[]
for i,(sig,members) in enumerate(sorted(families.items(),key=lambda kv:(len(kv[0]),str(kv[0])))):
    family_records.append({'denominator_family':i,'signature':[[sp,list(k)] for sp,k in sig],'propagator_count':len(sig),'member_subterms':[list(x) for x in members],'member_count':len(members),'numerator_equivalence':'NOT_CLAIMED'})

counts={}
for r in all_subterms: counts[str(r['total_propagator_count'])]=counts.get(str(r['total_propagator_count']),0)+1
thresholds={'loop_closure_abs_max':2e-14}
passed=bool(len(raw)==30 and len(all_subterms)>30 and max_closure<=thresholds['loop_closure_abs_max'] and all(r['total_propagator_count']>=3 for r in all_subterms))
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':passed,
 'classification':('PASS_U2_MATCHED_TIMELIKE_DENOMINATOR_SUBTERM_CENSUS_WITH_ADDITIVE_NY_EXPANSION__NUMERATOR_FAMILY_EQUIVALENCE_NEXT' if passed else 'FAIL_U2_TIMELIKE_DENOMINATOR_SUBTERM_CENSUS'),
 'candidate_residual':False,
 'census':{'physical_routes':30,'expanded_additive_subterms':len(all_subterms),'exact_denominator_multisets':len(families),'subterms_by_total_propagator_count':counts,'max_loop_closure_error':max_closure},
 'routes':route_records,'denominator_families':family_records,'thresholds':thresholds,
 'scope':'DENOMINATOR_PROVENANCE_AND_ADDITIVE_INVERSE_EXPANSION_ONLY__NUMERATOR_EQUIVALENCE_NOT_CLAIMED',
 'guardrails':['DENOMINATOR_EQUIVALENCE_IS_NOT_NUMERATOR_EQUIVALENCE','NUPPER1_ADDITIVE_PIECES_MUST_NOT_BE_COLLAPSED','SHIFTED_INCOMING_MOMENTUM_BINDING','NO_CUT_INTEGRATION_FROM_DENOMINATOR_CENSUS_ALONE','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':'for each denominator map/loop-momentum-shift candidate, reconstruct and compare the corresponding physical numerator subterms route-by-route; only proven numerator+denominator equivalences may be merged, then classify local/scaleless/rational versus cut-capable families before integration'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
