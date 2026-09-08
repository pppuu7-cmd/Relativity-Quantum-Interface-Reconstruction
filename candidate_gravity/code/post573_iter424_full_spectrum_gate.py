#!/usr/bin/env python3
"""Collision-safe binding/transport-schema wrapper for the post573 full-spectrum consumer.

Repairs only prerequisite/schema plumbing around the prospectively frozen numerical
consumer. Scientific formulas, support coordinates, Iter407 spectral algebra,
precision levels and Iter424 thresholds are untouched.

Repairs applied fail-closed:
1) bind the actual Iter573 authority filename/classification;
2) bind corrected Iter572 pre-spectral sample-layer classification;
3) consume the canonical Iter527 BASE/HALF manifest schema, where one coordinate
   can contain one or more ``artifact_parts``. Parts are independently SHA-256
   verified and merged by exact (z,phi_index), with duplicate/expected-z/80-row
   checks identical in meaning to the validated Iter527 assembly.
"""
from pathlib import Path
P=Path(__file__).resolve().parent/'post573_iter424_full_spectrum_from_raw_artifacts.py'
s=P.read_text()

# Iter573 race-created authority binding.
old="iteration573_iter424_frozen_clause_authority_mapping.json"
new="iteration573_iter424_authority_mapping_audit.json"
if s.count(old)!=1: raise SystemExit(('iter573_filename_binding_drift',s.count(old)))
s=s.replace(old,new,1)
old_check="if q573.get('scientific_gate_pass') is not True: raise RuntimeError(('iteration573_prerequisite_not_passed',q573.get('classification')))"
new_check="if q573.get('classification')!='PASS_ITER424_AUTHORITY_MAPPING_AUDIT__DIRECT_INHERITED_PASS__TENSOR11_OPERATIONAL_BLOCKED__NON_PROMOTING' or q573.get('status')!='PASS_SCOPED_AUDIT': raise RuntimeError(('iteration573_prerequisite_not_passed',q573.get('classification'),q573.get('status')))"
if s.count(old_check)!=1: raise SystemExit(('iter573_schema_binding_drift',s.count(old_check)))
s=s.replace(old_check,new_check,1)

# Iter572 scope was prospectively corrected from generic raw assembly to explicit
# pre-spectral sample-layer assembly. This changes only the prerequisite label.
old572="if q572.get('classification')!='PASS_COMPLETE_QUARTER_RAW_ASSEMBLY__NON_PROMOTING' or q572.get('scientific_gate_pass') is not True: raise RuntimeError('iteration572_prerequisite_not_passed')"
new572="if q572.get('classification')!='PASS_COMPLETE_QUARTER_RAW_SAMPLE_LAYER_ASSEMBLY__NON_PROMOTING' or q572.get('scientific_gate_pass') is not True: raise RuntimeError(('iteration572_prerequisite_not_passed',q572.get('classification')))"
if s.count(old572)!=1: raise SystemExit(('iter572_schema_binding_drift',s.count(old572)))
s=s.replace(old572,new572,1)

# Canonical BASE/HALF manifest is multipart-aware. Replace only the loader/provenance
# block; downstream spectral_F and Ds algebra are left byte-for-byte as authored.
old_bh="""    bh=json.loads(args.basehalf_manifest.read_text()); raw_bh={}; prov=[]
    for x in bh:
        p=args.bundle/'basehalf'/str(x['rank'])/'result.json'; o=load_json_verified(p,x['scientific_json_sha256']); k=key(x['u'],x['v']); raw_bh[k]=o
        prov.append({'family':'BASE_HALF','rank':x['rank'],'artifact_id':x['artifact_id'],'sha256':x['scientific_json_sha256'],'u':x['u'],'v':x['v']})
"""
new_bh="""    bh=json.loads(args.basehalf_manifest.read_text()); raw_bh={}; prov=[]
    for x in bh:
        parts=x.get('artifact_parts')
        if not isinstance(parts,list) or not parts: raise RuntimeError(('basehalf_artifact_parts_missing',x.get('rank')))
        merged={}; partprov=[]; seen_expected=set()
        for pi,part in enumerate(parts):
            aid=part.get('artifact_id'); want=part.get('scientific_json_sha256')
            if not isinstance(aid,int) or not isinstance(want,str) or len(want)!=64: raise RuntimeError(('basehalf_part_provenance_invalid',x.get('rank'),pi,part))
            p=args.bundle/'basehalf'/str(x['rank'])/str(pi)/'result.json'
            raw=p.read_bytes(); got=hashlib.sha256(raw).hexdigest()
            if got!=want.lower(): raise RuntimeError(('scientific_sha_mismatch',str(p),got,want,aid))
            zobj=json.loads(raw); rows=zobj.get('rows',[])
            if not rows or zobj.get('scientific_gate_pass') is not True: raise RuntimeError(('raw_part_authority_not_pass',x.get('rank'),pi,zobj.get('classification'),len(rows)))
            expected_z={round(float(v),12) for v in part.get('expected_z',[]) if v is not None}
            local_z=set()
            for row in rows:
                zk=round(float(row['z']),12); ph=int(row['phi_index']); rk=(zk,ph); local_z.add(zk)
                if rk in merged: raise RuntimeError(('duplicate_sample_across_parts',x.get('rank'),rk))
                merged[rk]=row
            if expected_z and local_z!=expected_z: raise RuntimeError(('part_z_support_drift',x.get('rank'),pi,sorted(local_z),sorted(expected_z)))
            seen_expected|=expected_z
            partprov.append({'artifact_id':aid,'sha256':got,'expected_z':part.get('expected_z')})
        if len(merged)!=80: raise RuntimeError(('merged_row_count_drift',x.get('rank'),len(merged)))
        zsupport={rk[0] for rk in merged}
        if zsupport!={-0.86,-0.43,0.0,0.43,0.86}: raise RuntimeError(('merged_z_support_drift',x.get('rank'),sorted(zsupport)))
        o={'scientific_gate_pass':True,'rows':[merged[rk] for rk in sorted(merged)]}
        k=key(x['u'],x['v']); raw_bh[k]=o
        prov.append({'family':'BASE_HALF','rank':x['rank'],'artifact_parts':partprov,'u':x['u'],'v':x['v']})
"""
if s.count(old_bh)!=1: raise SystemExit(('basehalf_loader_schema_drift',s.count(old_bh)))
s=s.replace(old_bh,new_bh,1)

ns={'__name__':'__main__','__file__':str(P)}
exec(compile(s,str(P),'exec'),ns,ns)
