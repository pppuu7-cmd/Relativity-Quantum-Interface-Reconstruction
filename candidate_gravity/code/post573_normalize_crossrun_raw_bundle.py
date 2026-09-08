#!/usr/bin/env python3
"""Verify and normalize cross-run raw authorities for the frozen spectral consumer.

Every historical scientific part is SHA-256 checked before merge. BASE/HALF
multipart coordinates are merged only by disjoint (z,phi_index) support into an
80-row synthetic coordinate file; no numerical values are altered or filled.
QUARTER single-part files are SHA-verified then copied to the consumer layout.
"""
from __future__ import annotations
import argparse,hashlib,json,shutil
from pathlib import Path
ap=argparse.ArgumentParser(); ap.add_argument('--basehalf-manifest',type=Path,required=True); ap.add_argument('--quarter-manifest',type=Path,required=True); ap.add_argument('--bundle',type=Path,required=True); ap.add_argument('--flat-basehalf-manifest',type=Path,required=True); a=ap.parse_args()
bh=json.loads(a.basehalf_manifest.read_text()); q=json.loads(a.quarter_manifest.read_text())
flat=[]
for x in bh:
    rows={}; aids=[]; parts=[]
    for pi,p in enumerate(x['artifact_parts']):
        src=a.bundle/'basehalf'/str(x['rank'])/str(pi)/'result.json'
        raw=src.read_bytes(); got=hashlib.sha256(raw).hexdigest(); want=p['scientific_json_sha256'].lower()
        if got!=want: raise SystemExit(('basehalf_part_sha_mismatch',x['rank'],pi,got,want))
        o=json.loads(raw); rr=o.get('rows',[])
        if not rr: raise SystemExit(('basehalf_empty_part',x['rank'],pi))
        seen_z=set()
        for r in rr:
            k=(round(float(r['z']),12),int(r['phi_index'])); seen_z.add(k[0])
            if k in rows: raise SystemExit(('basehalf_duplicate_sample',x['rank'],pi,k))
            rows[k]=r
        exp={round(float(z),12) for z in p.get('expected_z',[])}
        if exp and seen_z!=exp: raise SystemExit(('basehalf_expected_z_drift',x['rank'],pi,sorted(seen_z),sorted(exp)))
        aids.append(int(p['artifact_id'])); parts.append({'artifact_id':int(p['artifact_id']),'sha256':got,'expected_z':p.get('expected_z')})
    if len(rows)!=80 or {k[0] for k in rows}!={-0.86,-0.43,0.0,0.43,0.86}: raise SystemExit(('basehalf_merged_support_drift',x['rank'],len(rows),sorted({k[0] for k in rows})))
    merged={'scientific_gate_pass':True,'classification':'NORMALIZED_EXACT_RAW_MULTIPART_AUTHORITY__TRANSPORT_ONLY','coordinate':{'u':x['u'],'v':x['v']},'rows':[rows[k] for k in sorted(rows)],'source_parts':parts}
    dst=a.bundle/'basehalf'/str(x['rank'])/'result.json'; dst.parent.mkdir(parents=True,exist_ok=True); b=(json.dumps(merged,sort_keys=True,separators=(',',':'))+'\n').encode(); dst.write_bytes(b); sha=hashlib.sha256(b).hexdigest()
    flat.append({'rank':x['rank'],'u':x['u'],'v':x['v'],'artifact_id':aids,'scientific_json_sha256':sha,'source_parts':parts})
for x in q:
    src=a.bundle/'quarter'/str(x['rank'])/'0'/'result.json'; raw=src.read_bytes(); got=hashlib.sha256(raw).hexdigest()
    if got!=x['sha256'].lower(): raise SystemExit(('quarter_sha_mismatch',x['rank'],got,x['sha256']))
    o=json.loads(raw)
    if o.get('scientific_gate_pass') is not True or len(o.get('rows',[]))!=80: raise SystemExit(('quarter_authority_invalid',x['rank'],o.get('classification'),len(o.get('rows',[]))))
    dst=a.bundle/'quarter'/str(x['rank'])/'result.json'; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(src,dst)
a.flat_basehalf_manifest.parent.mkdir(parents=True,exist_ok=True); a.flat_basehalf_manifest.write_text(json.dumps(flat,indent=2,sort_keys=True)+'\n')
print(json.dumps({'basehalf_coordinates':len(flat),'basehalf_source_parts':sum(len(x['source_parts']) for x in flat),'quarter_coordinates':len(q),'zero_fill':False},sort_keys=True))
