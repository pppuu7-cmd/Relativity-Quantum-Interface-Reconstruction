#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 354.

Identify candidate equivalence classes among Iteration-353 U2 denominator
subterms under a single common loop-momentum translation. This is deliberately
NOT a family merge: species and denominator multiplicity must match, and every
candidate map remains tagged NUMERATOR_TEST_REQUIRED.

The next gate must reconstruct physical additive numerators at multiple held-out
loop momenta and verify transport under each proposed shift before any merge.
"""
from __future__ import annotations
import itertools, json
import numpy as np

ITERATION=354
LEGS=('s','a','b'); ORDER=('NL','AT','H','AR','NR','Y'); APPLY=tuple(reversed(ORDER))
q={'s':np.array([1.,0.,0.,0.]),'a':np.array([-.4,.1,.1,0.]),'b':np.array([-.6,-.1,-.1,0.])}
p0=np.array([.43,-.27,.39,.21])
def canonical(k): return tuple(x for x in LEGS if x in k)
def qkey(k): return sum((q[x] for x in k),np.zeros(4))
def kt(x): return tuple(float(np.round(v,12)) for v in np.asarray(x,float))
def disjoint_union(keys):
 f=[x for k in keys for x in k]
 if len(f)!=len(set(f)): return None
 return canonical(f)
allowed={'NL':[(),('s',),('a',),('b',)],'AT':[('s',),('a',),('b',),('s','a'),('s','b'),('a','b')],
'H':[(),('s',),('a',),('b',)],'AR':[('s',),('a',),('b',),('s','a'),('s','b'),('a','b')],
'NR':[(),('s',),('a',),('b',)],'Y':[(),('s',),('a',),('b',)]}
raw=[]
for choice in itertools.product(*[allowed[x] for x in ORDER]):
 a={n:canonical(k) for n,k in zip(ORDER,choice)}
 if disjoint_union(a.values())==LEGS: raw.append(a)
assert len(raw)==30

def factor_terms(name,key,kin):
 key=canonical(key); kout=kin+qkey(key)
 if name in ('AT','AR','Y'): return [('local',[])]
 if name in ('NL','NR'):
  if not key: return [('Q0Y0',[('ghost',kin)])]
  return [('QoutY1',[('ghost',kout)]),('minus_QoutN1QinY0',[('ghost',kout),('ghost',kin)])]
 if name=='H':
  if not key: return [('minus_G0',[('graviton',kin)])]
  return [('plus_GoutK1Gin',[('graviton',kout),('graviton',kin)])]
 raise KeyError(name)

subs=[]
for rid,a in enumerate(raw):
 cur=p0.copy(); fterms=[]
 for name in APPLY:
  key=a[name]; fterms.append((name,key,factor_terms(name,key,cur))); cur=cur+qkey(key)
 assert np.max(np.abs(cur-p0))<2e-14
 for sid,choice in enumerate(itertools.product(*[x[2] for x in fterms])):
  props=[]; pieces=[]
  for (name,key,_),(piece,ps) in zip(fterms,choice):
   props += [(sp,np.asarray(k,float)) for sp,k in ps]
   pieces.append((name,key,piece))
  # Sort by species then momentum. A common translation C means each offset k_i-k_ref is invariant.
  props_sorted=sorted(props,key=lambda x:(x[0],kt(x[1])))
  ref=props_sorted[0][1]
  relative=tuple((sp,kt(k-ref)) for sp,k in props_sorted)
  absolute=tuple((sp,kt(k)) for sp,k in props_sorted)
  subs.append({'route':rid,'subterm':sid,'pieces':[(n,list(k),p) for n,k,p in pieces],
               'absolute_signature':absolute,'relative_translation_signature':relative,'reference_momentum':kt(ref)})

classes={}
for s in subs: classes.setdefault(s['relative_translation_signature'],[]).append(s)
records=[]; multi=0
for cid,(sig,members) in enumerate(sorted(classes.items(),key=lambda kv:(len(kv[0]),str(kv[0])))):
 maps=[]
 base=members[0]
 for m in members:
  shift=np.asarray(m['reference_momentum'])-np.asarray(base['reference_momentum'])
  maps.append({'route':m['route'],'subterm':m['subterm'],'shift_from_base':list(map(float,shift)),'status':'NUMERATOR_TEST_REQUIRED'})
 if len(members)>1: multi+=1
 records.append({'candidate_class':cid,'propagator_count':len(sig),'relative_signature':[[sp,list(off)] for sp,off in sig],
                 'member_count':len(members),'members':maps,'numerator_equivalence':'NOT_CLAIMED'})

# Verify every proposed shift exactly transports denominator multisets with species fixed.
max_map_err=0.0
for rec in records:
 ms=rec['members']; base=next(s for s in subs if s['route']==ms[0]['route'] and s['subterm']==ms[0]['subterm'])
 b=base['absolute_signature']
 for m in ms:
  obj=next(s for s in subs if s['route']==m['route'] and s['subterm']==m['subterm'])
  sh=np.asarray(m['shift_from_base'])
  if len(b)!=len(obj['absolute_signature']): max_map_err=max(max_map_err,1.0); continue
  for (sp0,k0),(sp1,k1) in zip(b,obj['absolute_signature']):
   if sp0!=sp1: max_map_err=max(max_map_err,1.0)
   else: max_map_err=max(max_map_err,float(np.max(np.abs(np.asarray(k0)+sh-np.asarray(k1)))))
thresholds={'denominator_translation_map_abs_max':2e-12}
passed=bool(len(subs)==42 and max_map_err<=thresholds['denominator_translation_map_abs_max'])
result={'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':passed,
'classification':('PASS_U2_DENOMINATOR_COMMON_TRANSLATION_CANDIDATE_CENSUS__HELDOUT_PHYSICAL_NUMERATOR_TRANSPORT_TESTS_NEXT' if passed else 'FAIL_U2_DENOMINATOR_TRANSLATION_CANDIDATE_CENSUS'),
'candidate_residual':False,'census':{'additive_subterms':len(subs),'translation_candidate_classes':len(classes),'multi_member_candidate_classes':multi,'max_denominator_translation_map_error':max_map_err},
'candidate_classes':records,'scope':'DENOMINATOR_TRANSLATION_CANDIDATES_ONLY__NO_NUMERATOR_EQUIVALENCE_AND_NO_FAMILY_MERGE','thresholds':thresholds,
'guardrails':['DENOMINATOR_EQUIVALENCE_IS_NOT_NUMERATOR_EQUIVALENCE','ALL_MULTI_MEMBER_CLASSES_REQUIRE_HELDOUT_PHYSICAL_NUMERATOR_TESTS','NO_CUT_INTEGRATION','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
'next_gate':'reconstruct each additive physical numerator subterm as a function of loop momentum and test every multi-member denominator-translation candidate at multiple held-out momenta; merge only maps passing fixed numerator transport thresholds, otherwise preserve separate families'}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
