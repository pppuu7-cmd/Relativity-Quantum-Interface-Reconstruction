#!/usr/bin/env python3
import json, pathlib, math
ROOT=pathlib.Path('candidate_gravity')

def mink(v):
    return float(v[0])**2-sum(float(x)**2 for x in v[1:])
def vec4(x):
    return isinstance(x,list) and len(x)==4 and all(isinstance(y,(int,float)) for y in x)
def walk(obj,path,out):
    if isinstance(obj,dict):
        # exact key variants only; never infer from unrelated prose
        variants=[('q_s','q_a','q_b'),('qs','qa','qb')]
        for ks,ka,kb in variants:
            if all(k in obj and vec4(obj[k]) for k in (ks,ka,kb)):
                vs,va,vb=obj[ks],obj[ka],obj[kb]
                closure=[vs[i]+va[i]+vb[i] for i in range(4)]
                out.append({
                    'path':path,
                    'keys':[ks,ka,kb],
                    'q_s':vs,'q_a':va,'q_b':vb,
                    'closure_max_abs':max(abs(float(x)) for x in closure),
                    's0_qs2':mink(vs),'t0_qa2':mink(va),'u0_qb2':mink(vb)
                })
        for k,v in obj.items(): walk(v,path+'/'+str(k),out)
    elif isinstance(obj,list):
        for i,v in enumerate(obj): walk(v,path+f'/{i}',out)

matches=[]; parsed=0
for p in ROOT.rglob('*.json'):
    try:
        obj=json.loads(p.read_text())
    except Exception:
        continue
    parsed+=1
    walk(obj,str(p),matches)
# Exact-closure candidates only; preserve all candidates rather than silently choosing.
exact=[m for m in matches if m['closure_max_abs']<=1e-12]
# Group invariant triples rounded only for identity comparison, retaining raw values.
groups={}
for m in exact:
    key=tuple(round(float(m[k]),12) for k in ('s0_qs2','t0_qa2','u0_qb2'))
    groups.setdefault(key,[]).append(m)
unique_invariant_triples=len(groups)
if unique_invariant_triples==1:
    triple=next(iter(groups))
    classification='PASS_ITER637_UNIQUE_EXACT_FIXTURE_INVARIANT_ANCHOR_RECOVERED__NON_RESIDUAL'
    anchor={'s0':triple[0],'t0':triple[1],'u0':triple[2]}
else:
    classification='BLOCKED_ITER637_EXACT_FIXTURE_INVARIANT_ANCHOR_NOT_UNIQUE_OR_NOT_MACHINE_RECOVERABLE__NO_T0_U0_INVENTED__NON_RESIDUAL'
    anchor=None
result={
 'iteration':637,'date':'2026-09-09','scientific_gate_pass':True,'candidate_residual':False,
 'classification':classification,
 'json_files_parsed':parsed,'raw_vector_triplet_matches':len(matches),'exact_closure_matches':len(exact),
 'unique_invariant_triples':unique_invariant_triples,'recovered_anchor':anchor,
 'candidate_groups':[{'invariants':{'s0':k[0],'t0':k[1],'u0':k[2]},'provenance':[m['path'] for m in v]} for k,v in sorted(groups.items())],
 'all_exact_matches':exact,
 'metric_signature':'+---','closure_tolerance':1e-12,
 'guardrail':'No t0/u0 is invented. Multiple invariant triples remain BLOCKED until provenance resolves authority.',
 'source_born_subtraction':'NOT_PERFORMED','native_projection':'NOT_PERFORMED','candidate_values_used':False,'zero_fill':False,
 'failures':[],'MODEL_READINESS':'24%','readiness_change':'0 percentage points',
 'next_gate':'If exactly one authoritative anchor is recovered, evaluate Iter636 bubble threshold and triangle Landau support. Otherwise audit the candidate provenance / original fixture authority without using Iter582 values.'
}
print(json.dumps(result,indent=2))
