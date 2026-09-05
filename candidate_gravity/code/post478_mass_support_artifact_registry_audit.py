#!/usr/bin/env python3
"""Collision-safe mass-support raw-artifact registry audit after Iteration 478.

Provenance only. Normalizes historical raw-consumption JSON schemas so future
full-F assembly can bind every certified mass coordinate to exact Actions raw
artifacts. Composite certificates are allowed only when their disjoint z-row
partitions provably cover the frozen 5z x NPHI16 = 80 rows.
"""
from __future__ import annotations
import json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
RES=ROOT/'results'; REC=ROOT/'recovery'
manifest=json.loads((RES/'iteration455_mass_support_queue_manifest.json').read_text())['manifest']
if len(manifest)!=28: raise SystemExit(('manifest_count_drift',len(manifest)))
front=(REC/'CURRENT_QG_FRONT.md').read_text()
if '**MODEL_READINESS:** **24%**' not in front: raise SystemExit('model_readiness_authority_drift')
if not ('Certified occurrence-weighted precision coverage: **`15/32 = 46.875%`**' in front and
        'distinct rank 11' in front and 'u=+5e-6, v=+1e-5' in front):
    raise SystemExit('current_front_advanced_or_drifted__rerun_registry_against_new_authority')

FROZEN_Z=(-0.86,-0.43,0.0,0.43,0.86)
def norm(x): return round(float(x),15)
def ckey(u,v): return (norm(u),norm(v))
def vd(x): return isinstance(x,str) and re.fullmatch(r'sha256:[0-9a-f]{64}',x) is not None
def vs(x): return isinstance(x,str) and re.fullmatch(r'[0-9a-f]{64}',x) is not None

def first_coord(o):
    for key in ('frozen_coordinate','mass_coordinate','mass_node','coordinate'):
        x=o.get(key)
        if isinstance(x,dict) and 'u' in x and 'v' in x: return x,key
    x=o.get('frozen')
    if isinstance(x,dict) and 'u' in x and 'v' in x: return x,'frozen'
    x=o.get('selected_slab',{}).get('mass_point') if isinstance(o.get('selected_slab'),dict) else None
    if isinstance(x,dict) and 'u' in x and 'v' in x: return x,'selected_slab.mass_point'
    return None,None

def provenance(o):
    rp=o.get('raw_provenance') if isinstance(o.get('raw_provenance'),dict) else {}
    pr=o.get('provenance') if isinstance(o.get('provenance'),dict) else {}
    run=o.get('source_run_id',o.get('run_id',o.get('source_run',rp.get('run_id',pr.get('run_id')))))
    job=o.get('source_job_id',o.get('job_id',o.get('source_job',rp.get('job_id',pr.get('job_id')))))
    art=o.get('artifact_id',o.get('source_artifact_id',o.get('source_artifact',rp.get('artifact_id',pr.get('artifact_id')))))
    dig=o.get('artifact_digest',o.get('source_artifact_digest',rp.get('artifact_digest',pr.get('artifact_digest'))))
    sj=o.get('scientific_json_sha256',rp.get('raw_result_sha256',pr.get('scientific_json_sha256')))
    name=o.get('artifact_name',o.get('source_artifact_name'))
    return run,job,art,name,dig,sj

def coverage(o):
    z=None; rows=None; mode='unknown'
    obs=o.get('observed') if isinstance(o.get('observed'),dict) else {}
    if isinstance(o.get('selected_slab'),dict):
        z=o['selected_slab'].get('z'); rows=o['selected_slab'].get('output_rows'); mode='selected_slab'
    if z is None and isinstance(o.get('newly_consumed_z'),list):
        z=o.get('newly_consumed_z'); rows=o.get('new_rows'); mode='newly_consumed_z'
    if z is None and isinstance(o.get('frozen'),dict) and isinstance(o['frozen'].get('z_samples'),list):
        z=o['frozen']['z_samples']; rows=obs.get('sample_count'); mode='frozen_z_samples'
    if rows is None: rows=obs.get('sample_count')
    cls=str(o.get('classification',o.get('raw_classification','')))
    fullz=('FULL_Z' in cls or 'FULL_TRAINING_Z' in str(o.get('authority_type','')).upper())
    if rows==80 and fullz and z is None:
        z=list(FROZEN_Z); mode='full80_inferred_from_frozen_fullz_contract'
    return ([norm(x) for x in z] if isinstance(z,list) else None), rows, mode

entries={}; files=[]
for p in sorted(RES.glob('*.json')):
    try: o=json.loads(p.read_text())
    except Exception: continue
    if not isinstance(o,dict) or o.get('scientific_gate_pass') is not True or o.get('promotes_physical_coordinate') is not False: continue
    co,shape=first_coord(o)
    if co is None: continue
    run,job,art,name,dig,sj=provenance(o)
    if not (isinstance(run,int) and isinstance(job,int) and isinstance(art,int) and vd(dig) and vs(sj)): continue
    z,rows,covmode=coverage(o)
    rec={
      'path':str(p.relative_to(ROOT.parent)), 'authoritative_iteration':o.get('authoritative_iteration',o.get('iteration')),
      'source_run_id':run,'source_job_id':job,'artifact_id':art,'artifact_name':name,
      'artifact_digest':dig,'scientific_json_sha256':sj,
      'classification':o.get('classification',o.get('raw_classification')),
      'coordinate_shape':shape,'u':float(co['u']),'v':float(co['v']),
      'z_coverage':z,'row_count':rows,'coverage_mode':covmode,
    }
    entries.setdefault(ckey(co['u'],co['v']),[]).append(rec); files.append(rec['path'])

certified=set(range(11)); active=11
rows_out=[]; complete=[]; missing=[]; ambiguous=[]; composite=[]
for m in manifest:
    rank=int(m['distinct_rank']); refs=entries.get(ckey(m['u'],m['v']),[])
    state='CERTIFIED_CURRENT_FRONT' if rank in certified else ('ACTIVE_GATE' if rank==active else 'UNTESTED')
    reg='NOT_YET_REQUIRED'; reason=None
    if rank in certified:
        if not refs:
            reg='CERTIFIED_BUT_RAW_ARTIFACT_BINDING_NOT_FOUND'; missing.append(rank)
        else:
            unique={}
            for r in refs:
                ident=(r['source_run_id'],r['artifact_id'],r['artifact_digest'],r['scientific_json_sha256'])
                unique.setdefault(ident,r)
            rr=list(unique.values())
            full=[r for r in rr if r.get('row_count')==80 and set(r.get('z_coverage') or [])==set(map(norm,FROZEN_Z))]
            if len(full)>=1:
                reg='EXACT_RAW_ARTIFACT_BOUND__FULL_80_ROW_SOURCE'
                complete.append(rank); reason={'full_source_count':len(full),'total_unique_sources':len(rr)}
            else:
                zsets=[]; total=0; good=True
                for r in rr:
                    zs=r.get('z_coverage'); n=r.get('row_count')
                    if not isinstance(zs,list) or not isinstance(n,int): good=False; break
                    zset=set(zs)
                    if any(zset & q for q in zsets): good=False; break
                    if n != 16*len(zset): good=False; break
                    zsets.append(zset); total+=n
                union=set().union(*zsets) if zsets else set()
                if good and union==set(map(norm,FROZEN_Z)) and total==80:
                    reg='EXACT_RAW_ARTIFACT_BOUND__COMPOSITE_DISJOINT_Z_PARTITIONS_80_ROWS'
                    complete.append(rank); composite.append(rank)
                    reason={'unique_sources':len(rr),'z_union':sorted(union),'row_total':total}
                else:
                    reg='AMBIGUOUS_OR_INCOMPLETE_RAW_BINDING__FAIL_CLOSED'; ambiguous.append(rank)
                    reason={'unique_sources':len(rr),'z_union':sorted(set().union(*zsets)) if zsets else [],'row_total':total,'partition_checks_ok':good}
    elif rank==active:
        reg='NOT_YET_REQUIRED_UNTIL_RAW_VALID_COMPLETION'
    rows_out.append({'distinct_rank':rank,'u':m['u'],'v':m['v'],'source_occurrence_multiplicity':m['source_occurrence_multiplicity'],
                     'source_labels':m['source_labels'],'authority_state':state,'registry_state':reg,'registry_reason':reason,'raw_sources':refs})

closed_occ=sum(int(m['source_occurrence_multiplicity']) for m in manifest if int(m['distinct_rank']) in certified)
bound_occ=sum(int(m['source_occurrence_multiplicity']) for m in manifest if int(m['distinct_rank']) in complete)
passed=(not missing and not ambiguous and len(complete)==11 and bound_occ==15)
out={
 'stage':'POST478_MASS_SUPPORT_ARTIFACT_REGISTRY_AUDIT_V4__COLLISION_SAFE',
 'classification':('PASS_ALL_CURRENT_CERTIFIED_MASS_SUPPORT_RAW_ARTIFACT_BINDINGS_RECOVERED__NON_PROMOTING' if passed else 'BLOCKED_CURRENT_CERTIFIED_MASS_SUPPORT_RAW_ARTIFACT_REGISTRY_INCOMPLETE__NON_PROMOTING'),
 'scientific_gate_pass':passed,'promotes_physical_coordinate':False,'MODEL_READINESS':'24%','readiness_change_pp':0,
 'authority_snapshot':{'latest_canonical_iteration':478,'latest_mass_support_authority':475,'certified_ranks':'0..10','active_rank':11,'certified_occurrences':closed_occ,'total_occurrences':32},
 'registry_summary':{'certified_distinct_coordinates':11,'complete_raw_bound_distinct':len(complete),'missing_raw_bound_distinct':len(missing),'ambiguous_raw_bound_distinct':len(ambiguous),
                     'complete_raw_bound_ranks':complete,'composite_raw_bound_ranks':composite,'missing_raw_bound_ranks':missing,'ambiguous_raw_bound_ranks':ambiguous,
                     'certified_occurrences_with_complete_raw_binding':bound_occ,'certified_occurrences_total':closed_occ,'normalized_provenance_file_count':len(files)},
 'manifest_registry':rows_out,
 'interpretation':[
   'Historical raw-consumption schemas were normalized, including top-level provenance objects; artifact_name is not required because run/job/artifact_id/digest/scientific-SHA is an exact binding.',
   'A full local certificate requires exactly 80 frozen rows (5 z x 16 phi) either from one full-z artifact or a provably disjoint composite partition.',
   'Rank 10 is intentionally composite: Iteration449 contributes 48 rows at z={-0.86,0,+0.86}; Iteration450 contributes 32 rows at z={-0.43,+0.43}.',
   'No u<->v symmetry, neighboring coordinate substitution, recomputation, threshold change, or physical promotion is used.'
 ],
 'next_gate_if_pass':'verify raw artifact payload schemas/downloadability and freeze an assembly-input registry; full-F assembly remains forbidden until all 28 distinct coordinates are locally certified',
 'next_gate_if_blocked':'recover only the exact missing/ambiguous historical artifact binding from repository history; do not regenerate samples as a provenance substitute',
 'guardrails':['NO_FUV_EVALUATION','NO_ACTIVE_RANK11_DUPLICATION','NO_SUPPORT_REORDERING','NO_UV_SWAP_DEDUPLICATION','NO_RECOMPUTE_TO_REPLACE_PROVENANCE','NO_THRESHOLD_CHANGE','NO_PHYSICAL_DS_PROMOTION','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(out,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
