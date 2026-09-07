#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
import mpmath as mp

ROOT=Path(__file__).resolve().parent
R=ROOT.parent/'results'
BUNDLE=ROOT.parent/'artifacts'/'post523_independent_base_half_assembly'/'support_bundle'
MAN=json.loads((R/'iteration455_mass_support_queue_manifest.json').read_text())
CLOSE=json.loads((R/'post522_rank27_raw_consumption.json').read_text())
BRIDGE=json.loads((R/'post525_historical_support_provenance_bridge.json').read_text())
if CLOSE.get('classification')!='PASS_RAW_CONSUMED_MANIFEST_RANK27_FULL_Z_MP80_MP120__NON_PROMOTING' or CLOSE.get('support_after_consumption',{}).get('certified_occurrences')!=32:
    raise SystemExit('full support closure prerequisite not raw-valid')
if MAN.get('frozen',{}).get('distinct_coordinate_count')!=28 or MAN.get('frozen',{}).get('occurrence_count')!=32:
    raise SystemExit('iteration455 manifest drift')
if BRIDGE.get('classification')!='PASS_EXACT_HISTORICAL_SUPPORT_PROVENANCE_BRIDGE__NON_PROMOTING' or BRIDGE.get('scientific_gate_pass') is not True:
    raise SystemExit('historical provenance bridge not valid')

def key(u,v): return (round(float(u),14),round(float(v),14))
expected={key(x['u'],x['v']):x for x in MAN['manifest']}

def coord_of(o):
    for name in ('coordinate','target','frozen'):
        q=o.get(name,{})
        if isinstance(q,dict) and 'u' in q and 'v' in q: return key(q['u'],q['v'])
    return None

def recursive_pairs(o):
    found=[]
    def walk(x):
        if isinstance(x,dict):
            aid=x.get('artifact_id'); sha=x.get('scientific_json_sha256')
            if isinstance(aid,int) and isinstance(sha,str) and len(sha)==64:
                found.append({'artifact_id':aid,'scientific_json_sha256':sha.lower(),'artifact_name':x.get('artifact_name')})
            for v in x.values(): walk(v)
        elif isinstance(x,list):
            for v in x: walk(v)
    walk(o)
    uniq={(x['artifact_id'],x['scientific_json_sha256']) for x in found}
    if len(uniq)!=1: return None
    aid,sha=next(iter(uniq)); names={x.get('artifact_name') for x in found if x['artifact_id']==aid and x['scientific_json_sha256']==sha and x.get('artifact_name')}
    return [{'artifact_id':aid,'scientific_json_sha256':sha,'artifact_name':next(iter(names)) if len(names)==1 else None}]

def authorities():
    best={}
    for p in R.glob('*.json'):
        try: o=json.loads(p.read_text())
        except Exception: continue
        k=coord_of(o)
        if k not in expected: continue
        obs=o.get('observed',{})
        if obs.get('scientific_authority_pass') is not True and o.get('scientific_gate_pass') is not True: continue
        parts=recursive_pairs(o)
        if not parts: continue
        try: it=int(o.get('iteration',-1))
        except Exception: continue
        rec={'iteration':it,'authority_file':p.name,'parts':parts}
        if k not in best or it>best[k]['iteration']: best[k]=rec
    for b in BRIDGE.get('authorities',[]):
        k=key(b['u'],b['v'])
        if k not in expected or int(b['rank'])!=int(expected[k]['distinct_rank']): raise SystemExit(('bridge_coordinate_drift',b))
        parts=b.get('parts',[])
        if not parts or any(not isinstance(x.get('artifact_id'),int) or not isinstance(x.get('scientific_json_sha256'),str) or len(x['scientific_json_sha256'])!=64 for x in parts):
            raise SystemExit(('bridge_provenance_invalid',b['rank']))
        best[k]={'iteration':int(BRIDGE['iteration']),'authority_file':'post525_historical_support_provenance_bridge.json','parts':parts,'authority_sources':b.get('authority_sources',[])}
    if set(best)!=set(expected):
        miss=sorted(set(expected)-set(best)); raise SystemExit(('missing_raw_consumed_support_authority',miss,len(best)))
    return best

ap=argparse.ArgumentParser(); ap.add_argument('--emit-artifact-manifest',action='store_true'); a=ap.parse_args()
auth=authorities()
if a.emit_artifact_manifest:
    out=[]
    for k,m in sorted(expected.items(),key=lambda kv:kv[1]['distinct_rank']):
        o=auth[k]
        out.append({'rank':m['distinct_rank'],'u':m['u'],'v':m['v'],'authority_file':o['authority_file'],'authority_iteration':o['iteration'],'artifact_parts':o['parts']})
    print(json.dumps(out,indent=2,sort_keys=True)); raise SystemExit(0)

c=[Fraction(1),Fraction(-8),Fraction(8),Fraction(-1)]
wbase={}; whalf={}
for h,mul,out in [(Fraction(1),Fraction(1),wbase),(Fraction(1,2),Fraction(4),whalf)]:
    nodes=[-2*h,-h,h,2*h]
    for i,u in enumerate(nodes):
      for j,v in enumerate(nodes): out[(u,v)]=mul*c[i]*c[j]/Fraction(144)
gbb=sum(x*x for x in wbase.values()); ghh=sum(x*x for x in whalf.values()); gbh=sum(wbase.get(k,Fraction(0))*whalf.get(k,Fraction(0)) for k in set(wbase)|set(whalf))
if (gbb,gbh,ghh)!=(Fraction(4225,5184),Fraction(4,81),Fraction(4225,324)): raise SystemExit(('assembly_gram_drift',gbb,gbh,ghh))
if gbb*ghh-gbh*gbh!=Fraction(5948843,559872): raise SystemExit('assembly_determinant_drift')

raw={}; provenance=[]
for k,m in expected.items():
    o=auth[k]; rank=m['distinct_rank']; d={}; partprov=[]
    for pi,part in enumerate(o['parts']):
        q=BUNDLE/str(rank)/str(pi)/'result.json'
        if not q.exists(): raise SystemExit(('artifact_result_missing',rank,pi,str(q)))
        b=q.read_bytes(); got=hashlib.sha256(b).hexdigest(); want=part['scientific_json_sha256'].lower()
        if got!=want: raise SystemExit(('scientific_json_sha256_mismatch',rank,pi,got,want,part['artifact_id']))
        z=json.loads(b); rows=z.get('rows',[])
        if not rows: raise SystemExit(('empty_rows',rank,pi))
        expected_z={round(float(x),12) for x in part.get('expected_z',[])}
        seen_z=set()
        for r in rows:
            zk=round(float(r['z']),12); ph=int(r['phi_index']); kk=(zk,ph); seen_z.add(zk)
            if kk in d: raise SystemExit(('duplicate_sample_across_parts',rank,kk))
            d[kk]={80:mp.mpc(mp.mpf(r['mp80_re']),mp.mpf(r['mp80_im'])),120:mp.mpc(mp.mpf(r['mp120_re']),mp.mpf(r['mp120_im']))}
        if expected_z and seen_z!=expected_z: raise SystemExit(('part_z_support_drift',rank,pi,sorted(seen_z),sorted(expected_z)))
        partprov.append({'artifact_id':part['artifact_id'],'sha256':got,'expected_z':part.get('expected_z')})
    if len(d)!=80: raise SystemExit(('merged_row_count_drift',rank,len(d)))
    if {x[0] for x in d}!={-0.86,-0.43,0.0,0.43,0.86}: raise SystemExit(('merged_z_support_drift',rank,sorted({x[0] for x in d})))
    raw[k]=d; provenance.append({'rank':rank,'authority_file':o['authority_file'],'parts':partprov})

samples=set.intersection(*(set(x) for x in raw.values()))
if len(samples)!=80: raise SystemExit(('common_sample_support_drift',len(samples)))
coef=[mp.mpf(1),mp.mpf(-8),mp.mpf(8),mp.mpf(-1)]
def assembled(h,dps,sample):
    nodes=[-2*h,-h,h,2*h]; total=mp.mpc(0)
    for i,u in enumerate(nodes):
      for j,v in enumerate(nodes): total += coef[i]*coef[j]*raw[key(u,v)][sample][dps]
    return total/(mp.mpf(144)*mp.mpf(h)**2)
def scaled(x,y): return abs(x-y)/max(mp.mpf(1),abs(x),abs(y))
rows=[]; max_bmp=mp.mpf(0); max_hmp=mp.mpf(0); max_step=mp.mpf(0); finite=True
with mp.workdps(150):
  for s in sorted(samples):
    b80=assembled(5e-6,80,s); b120=assembled(5e-6,120,s); h80=assembled(2.5e-6,80,s); h120=assembled(2.5e-6,120,s)
    db=scaled(b80,b120); dh=scaled(h80,h120); ds80=scaled(-b80,-h80); ds120=scaled(-b120,-h120)
    max_bmp=max(max_bmp,db); max_hmp=max(max_hmp,dh); max_step=max(max_step,ds80,ds120)
    ok=all(mp.isfinite(x.real) and mp.isfinite(x.imag) for x in (b80,b120,h80,h120)); finite=finite and ok
    rows.append({'z':s[0],'phi_index':s[1],'base80':[mp.nstr(b80.real,40),mp.nstr(b80.imag,40)],'base120':[mp.nstr(b120.real,40),mp.nstr(b120.imag,40)],'half80':[mp.nstr(h80.real,40),mp.nstr(h80.imag,40)],'half120':[mp.nstr(h120.real,40),mp.nstr(h120.imag,40)],'ds_base120':[mp.nstr(-b120.real,40),mp.nstr(-b120.imag,40)],'base_mp_scaled':mp.nstr(db,30),'half_mp_scaled':mp.nstr(dh,30),'base_half_scaled_mp80':mp.nstr(ds80,30),'base_half_scaled_mp120':mp.nstr(ds120,30),'finite':ok})
passed=bool(finite and len(rows)==80 and max_bmp<=mp.mpf('2e-6') and max_hmp<=mp.mpf('2e-6') and max_step<=mp.mpf('2e-5'))
res={'stage':'POST523_INDEPENDENT_BASE_HALF_MP80_MP120_CENTRAL4_ASSEMBLY','classification':('PASS_INDEPENDENT_BASE_HALF_ASSEMBLY__NON_PROMOTING' if passed else 'BLOCKED_INDEPENDENT_BASE_HALF_ASSEMBLY__NON_PROMOTING'),'scientific_gate_pass':passed,'promotes_physical_coordinate':False,'MODEL_READINESS':'24%','readiness_change_pp':0,'target':{'double_double_index':2,'class_id':3,'q_squared':-1.0},'frozen':{'base_h':5e-6,'half_h':2.5e-6,'nodes_rule':'[-2h,-h,+h,+2h]','central4_coefficients':[1,-8,8,-1],'ds_binding':'ds=-d_base','precision_digits':[80,120],'distinct_coordinates':28,'source_occurrences':32,'sample_count':80,'no_richardson_promotion':True},'conditioning':{'gram_base_base':'4225/5184','gram_base_half':'4/81','gram_half_half':'4225/324','gram_determinant':'5948843/559872','rank':2},'thresholds':{'assembled_base_mp_scaled_max':'2e-6','assembled_half_mp_scaled_max':'2e-6','base_half_mass_step_scaled_max':'2e-5','all_finite':True},'observed':{'assembled_base_mp_scaled_max':mp.nstr(max_bmp,30),'assembled_half_mp_scaled_max':mp.nstr(max_hmp,30),'base_half_mass_step_scaled_max':mp.nstr(max_step,30),'all_finite':finite,'sample_count':len(rows)},'artifact_provenance':sorted(provenance,key=lambda x:x['rank']),'rows':rows,'next_gate_if_pass':'raw-consume, then frozen Iteration-424 reevaluation on identical parent/mass nodes','next_gate_if_blocked':'preserve BLOCKED and localize first assembled z/phi/precision or BASE-vs-HALF failure without threshold weakening','guardrails':['FULL_RAW_VALIDATED_SUPPORT_REQUIRED','VERIFY_EACH_SCIENTIFIC_JSON_SHA256','INDEPENDENT_BASE_HALF_ROWS','DS_EQUALS_MINUS_D_BASE','NO_RICHARDSON_PROMOTION','NO_THRESHOLD_WEAKENING','UNSUPPORTED_IS_BLOCKED','NO_ZERO_FILL','NO_PHYSICAL_PROMOTION','NO_ANSATZ003','NO_FISHER_RESOURCES']}
print(json.dumps(res,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
