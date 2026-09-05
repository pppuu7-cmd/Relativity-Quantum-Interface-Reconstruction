#!/usr/bin/env python3
"""Collision-safe mass-support raw-artifact registry audit after Iteration 478.

This is provenance only.  It does not evaluate F(u,v), alter the Iteration-455
queue, infer u<->v symmetry, or promote physical index 2.  The goal is to make
future full-F assembly fail closed: every locally certified coordinate used by
assembly must bind to an exact raw Actions artifact containing the 5z x NPHI16
MP80/MP120 sample payload (or be explicitly flagged as missing that binding).
"""
from __future__ import annotations
import json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
RES=ROOT/'results'
REC=ROOT/'recovery'
MAN=RES/'iteration455_mass_support_queue_manifest.json'
if not MAN.exists():
    raise SystemExit('iteration455_manifest_missing')
manifest=json.loads(MAN.read_text())['manifest']
if len(manifest)!=28:
    raise SystemExit(('manifest_count_drift',len(manifest)))

# Canonical completed local numerical mass-support iterations named by current
# authority.  Extra files are scanned too, but only records with exact artifact
# provenance and a coordinate are accepted into the registry.
front=(REC/'CURRENT_QG_FRONT.md').read_text()
if '**MODEL_READINESS:** **24%**' not in front:
    raise SystemExit('model_readiness_authority_drift')


def norm(x):
    return round(float(x),15)

def coord_key(u,v):
    return (norm(u),norm(v))

def valid_digest(x):
    return isinstance(x,str) and re.fullmatch(r'sha256:[0-9a-f]{64}',x) is not None

def valid_sha(x):
    return isinstance(x,str) and re.fullmatch(r'[0-9a-f]{64}',x) is not None

entries={}
provenance_files=[]
for p in sorted(RES.glob('*.json')):
    try: o=json.loads(p.read_text())
    except Exception: continue
    # Common authoritative local raw-consumption shape.
    fc=o.get('frozen_coordinate') if isinstance(o,dict) else None
    if not (isinstance(fc,dict) and 'u' in fc and 'v' in fc):
        continue
    run=o.get('source_run_id',o.get('run_id'))
    job=o.get('source_job_id',o.get('job_id'))
    art=o.get('artifact_id',o.get('source_artifact_id'))
    name=o.get('artifact_name',o.get('source_artifact_name'))
    dig=o.get('artifact_digest',o.get('source_artifact_digest'))
    sj=o.get('scientific_json_sha256')
    gate=o.get('scientific_gate_pass')
    promote=o.get('promotes_physical_coordinate')
    if not (isinstance(run,int) and isinstance(job,int) and isinstance(art,int) and isinstance(name,str)
            and valid_digest(dig) and valid_sha(sj) and gate is True and promote is False):
        continue
    k=coord_key(fc['u'],fc['v'])
    rec={
      'path':str(p.relative_to(ROOT.parent)),
      'authoritative_iteration':o.get('authoritative_iteration',o.get('iteration')),
      'source_run_id':run,'source_job_id':job,'artifact_id':art,'artifact_name':name,
      'artifact_digest':dig,'scientific_json_sha256':sj,
      'classification':o.get('classification'),
      'u':float(fc['u']),'v':float(fc['v']),
      'distinct_rank':fc.get('distinct_rank'),
      'source_occurrence_multiplicity':fc.get('source_occurrence_multiplicity'),
      'sample_count':(o.get('observed') or {}).get('sample_count'),
    }
    entries.setdefault(k,[]).append(rec); provenance_files.append(rec['path'])

# Determine current certified set from the authority statement, not by guessing
# from old Iteration-455 states.  Through Iteration 475, ranks 0..10 are locally
# certified; rank 11 is active.  Fail closed if CURRENT_QG_FRONT no longer says
# 15/32 or names a different active rank: in that case this snapshot is stale
# and should be rerun/revised rather than silently interpreted.
authority_snapshot_ok=(
    'Certified occurrence-weighted precision coverage: **`15/32 = 46.875%`**' in front
    and 'distinct rank 11' in front
    and 'u=+5e-6, v=+1e-5' in front
)
if not authority_snapshot_ok:
    raise SystemExit('current_front_advanced_or_drifted__rerun_registry_against_new_authority')
certified_ranks=set(range(0,11))
active_rank=11

rows=[]; full_raw=[]; missing_raw=[]; ambiguous=[]
for m in manifest:
    k=coord_key(m['u'],m['v']); refs=entries.get(k,[])
    rank=int(m['distinct_rank'])
    if rank in certified_ranks:
        state='CERTIFIED_CURRENT_FRONT'
        if len(refs)==1:
            registry='EXACT_RAW_ARTIFACT_BOUND'
            full_raw.append(rank)
        elif len(refs)==0:
            registry='CERTIFIED_BUT_EXACT_RAW_ARTIFACT_NOT_BOUND_BY_SCANNED_CANONICAL_RESULT'
            missing_raw.append(rank)
        else:
            # Multiple wrappers for the exact same underlying artifact are not
            # automatically an ambiguity if run/artifact/digest are identical.
            ids={(r['source_run_id'],r['artifact_id'],r['artifact_digest'],r['scientific_json_sha256']) for r in refs}
            if len(ids)==1:
                registry='EXACT_RAW_ARTIFACT_BOUND__DUPLICATE_PROVENANCE_WRAPPERS_SAME_SOURCE'
                full_raw.append(rank)
            else:
                registry='AMBIGUOUS_MULTIPLE_RAW_SOURCES__FAIL_CLOSED'
                ambiguous.append(rank)
    elif rank==active_rank:
        state='ACTIVE_GATE'; registry='NOT_YET_REQUIRED_UNTIL_RAW_VALID_COMPLETION'
    else:
        state='UNTESTED'; registry='NOT_YET_REQUIRED'
    rows.append({
      'distinct_rank':rank,'u':m['u'],'v':m['v'],
      'source_occurrence_multiplicity':m['source_occurrence_multiplicity'],
      'source_labels':m['source_labels'],'authority_state':state,
      'registry_state':registry,'raw_sources':refs,
    })

closed_occ=sum(int(m['source_occurrence_multiplicity']) for m in manifest if int(m['distinct_rank']) in certified_ranks)
bound_occ=sum(int(m['source_occurrence_multiplicity']) for m in manifest if int(m['distinct_rank']) in full_raw)
pass_registry=(len(ambiguous)==0)
classification=('PASS_MASS_SUPPORT_ARTIFACT_REGISTRY_AUDIT__MISSING_BINDINGS_EXPLICIT__NON_PROMOTING'
                if pass_registry else 'BLOCKED_MASS_SUPPORT_ARTIFACT_REGISTRY_AMBIGUITY__NON_PROMOTING')
out={
 'stage':'POST478_MASS_SUPPORT_ARTIFACT_REGISTRY_AUDIT__COLLISION_SAFE',
 'classification':classification,'scientific_gate_pass':pass_registry,
 'promotes_physical_coordinate':False,'MODEL_READINESS':'24%','readiness_change_pp':0,
 'authority_snapshot':{'latest_canonical_iteration':478,'latest_mass_support_authority':475,
                       'certified_ranks':'0..10','active_rank':11,
                       'certified_occurrences':closed_occ,'total_occurrences':32},
 'registry_summary':{
   'certified_distinct_coordinates':len(certified_ranks),
   'certified_distinct_with_exact_raw_binding':len(full_raw),
   'certified_distinct_missing_exact_raw_binding':len(missing_raw),
   'certified_distinct_ambiguous_raw_binding':len(ambiguous),
   'certified_occurrences_with_exact_raw_binding':bound_occ,
   'certified_occurrences_total':closed_occ,
   'full_raw_bound_ranks':full_raw,'missing_raw_bound_ranks':missing_raw,
   'ambiguous_raw_bound_ranks':ambiguous,
   'scanned_provenance_file_count':len(provenance_files)
 },
 'manifest_registry':rows,
 'interpretation':[
   'Only explicit run/job/artifact/digest/scientific-JSON bindings count as raw provenance for future assembly.',
   'A current local precision certificate without an explicit scanned raw-artifact binding remains scientifically valid in its original scope, but future full-F assembly must recover and bind its exact raw sample artifact before use.',
   'No coordinate is inferred from u<->v symmetry and exact BASE/HALF overlaps retain their separate source labels/derivative weights.',
   'This registry does not download or inspect raw sample payloads; payload schema/content verification is a later assembly prerequisite.'
 ],
 'next_gate_if_missing_bindings':'recover exact Actions run/artifact provenance for each missing certified rank from repository history/recovery and bind it without recomputation if raw artifact still exists; do not substitute a neighboring coordinate or regenerated sample',
 'next_gate_if_no_missing_bindings':'build raw-payload schema verifier and MP spectral/full-F assembly harness, but execute physical assembly only after all 28 distinct coordinates are locally certified',
 'guardrails':['NO_FUV_EVALUATION','NO_ACTIVE_RANK11_DUPLICATION','NO_SUPPORT_REORDERING','NO_UV_SWAP_DEDUPLICATION','NO_RECOMPUTE_TO_REPLACE_MISSING_PROVENANCE','NO_THRESHOLD_CHANGE','NO_PHYSICAL_DS_PROMOTION','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(out,indent=2,sort_keys=True))
if not pass_registry: raise SystemExit(2)
