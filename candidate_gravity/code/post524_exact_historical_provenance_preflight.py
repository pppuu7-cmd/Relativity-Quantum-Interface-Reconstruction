#!/usr/bin/env python3
from __future__ import annotations
import json,re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
R=ROOT.parent/'results'
MAN=json.loads((R/'iteration455_mass_support_queue_manifest.json').read_text())
CLOSE=json.loads((R/'post522_rank27_raw_consumption.json').read_text())
if CLOSE.get('classification')!='PASS_RAW_CONSUMED_MANIFEST_RANK27_FULL_Z_MP80_MP120__NON_PROMOTING' or CLOSE.get('support_after_consumption',{}).get('certified_occurrences')!=32:
    raise SystemExit('full support closure prerequisite not raw-valid')
if MAN.get('frozen',{}).get('distinct_coordinate_count')!=28 or MAN.get('frozen',{}).get('occurrence_count')!=32:
    raise SystemExit('iteration455 manifest drift')

def key(u,v): return (round(float(u),14),round(float(v),14))
expected={key(x['u'],x['v']):x for x in MAN['manifest']}

def coord_of(o):
    for name in ('coordinate','target','frozen'):
        q=o.get(name,{})
        if isinstance(q,dict) and 'u' in q and 'v' in q:
            return key(q['u'],q['v'])
    return None

def walk(x,path='$'):
    if isinstance(x,dict):
        yield path,x
        for k,v in x.items():
            yield from walk(v,f'{path}.{k}')
    elif isinstance(x,list):
        for i,v in enumerate(x): yield from walk(v,f'{path}[{i}]')

def exact_provenance(o):
    found=[]
    for path,d in walk(o):
        aid=d.get('artifact_id'); sha=d.get('scientific_json_sha256')
        if isinstance(aid,int) and isinstance(sha,str) and re.fullmatch(r'[0-9a-fA-F]{64}',sha):
            found.append((aid,sha.lower(),d.get('artifact_name'),path))
    pairs={(a,s) for a,s,_,_ in found}
    if len(pairs)!=1: return None
    aid,sha=next(iter(pairs))
    paths=sorted({p for a,s,_,p in found if (a,s)==(aid,sha)})
    names=sorted({n for a,s,n,_ in found if (a,s)==(aid,sha) and isinstance(n,str)})
    return {'artifact_id':aid,'scientific_json_sha256':sha,'artifact_name':names[0] if len(names)==1 else None,'source_paths':paths}

best={}
for p in R.glob('*.json'):
    try: o=json.loads(p.read_text())
    except Exception: continue
    k=coord_of(o)
    if k not in expected: continue
    obs=o.get('observed',{})
    if obs.get('scientific_authority_pass') is not True and o.get('scientific_gate_pass') is not True: continue
    prov=exact_provenance(o)
    if prov is None: continue
    try: it=int(o.get('iteration',-1))
    except Exception: continue
    rec={'rank':expected[k]['distinct_rank'],'u':expected[k]['u'],'v':expected[k]['v'],'authority_file':p.name,'authority_iteration':it,**prov}
    if k not in best or it>best[k]['authority_iteration']: best[k]=rec

missing=sorted(set(expected)-set(best),key=lambda k: expected[k]['distinct_rank'])
out={
 'schema':'rqir_exact_historical_provenance_preflight_v1',
 'iteration':525,
 'classification':'PASS_EXACT_28_OF_28_HISTORICAL_PROVENANCE_PREFLIGHT__NON_PROMOTING' if not missing else f'BLOCKED_EXACT_HISTORICAL_PROVENANCE_PREFLIGHT_{len(best)}_OF_28__NON_PROMOTING',
 'scientific_gate_pass':not missing,
 'promotes_physical_coordinate':False,
 'MODEL_READINESS':'24%',
 'readiness_change_pp':0,
 'resolved_distinct_coordinates':len(best),
 'required_distinct_coordinates':28,
 'authorities':[best[k] for k in sorted(best,key=lambda k: expected[k]['distinct_rank'])],
 'unresolved_coordinates':[{'rank':expected[k]['distinct_rank'],'u':expected[k]['u'],'v':expected[k]['v']} for k in missing],
 'method':'exact committed PASS-authority coordinate plus unique recursively located artifact_id/scientific_json_sha256 pair; no symmetry/coverage/neighbor inference',
 'guardrails':['EXACT_COMMITTED_AUTHORITY_ONLY','UNIQUE_ARTIFACT_SHA_PAIR_PER_RECORD','NO_SYMMETRY_INFERENCE','NO_ZERO_FILL','NO_THRESHOLD_WEAKENING','NO_ASSEMBLY_IN_PREFLIGHT','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(out,indent=2,sort_keys=True))
if missing: raise SystemExit(2)
