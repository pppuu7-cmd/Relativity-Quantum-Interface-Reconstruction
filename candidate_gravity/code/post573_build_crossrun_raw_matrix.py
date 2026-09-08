#!/usr/bin/env python3
"""Build a collision-safe matrix for official cross-run artifact transport.

No scientific computation. Reads the committed BASE/HALF exact multipart manifest
and the committed post573 QUARTER manifest, resolves each artifact ID to its
historical workflow run using public GitHub artifact metadata, and emits a
matrix for actions/download-artifact@v5.
"""
from __future__ import annotations
import argparse,json,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parent
ap=argparse.ArgumentParser(); ap.add_argument('--basehalf-manifest',type=Path,required=True); ap.add_argument('--quarter-manifest',type=Path,required=True); ap.add_argument('--repo',default='pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction'); a=ap.parse_args()
bh=json.loads(a.basehalf_manifest.read_text()); q=json.loads(a.quarter_manifest.read_text())
items=[]
for x in bh:
    for pi,p in enumerate(x['artifact_parts']):
        items.append({'family':'basehalf','rank':str(x['rank']),'part':str(pi),'artifact_id':int(p['artifact_id']),'sha256':p['scientific_json_sha256'],'u':x['u'],'v':x['v']})
for x in q:
    items.append({'family':'quarter','rank':str(x['rank']),'part':'0','artifact_id':int(x['artifact_id']),'sha256':x['sha256'],'u':x['u'],'v':x['v']})
seen=set()
for x in items:
    k=(x['family'],x['rank'],x['part'])
    if k in seen: raise SystemExit(('transport_key_duplicate',k))
    seen.add(k)
    req=urllib.request.Request(f'https://api.github.com/repos/{a.repo}/actions/artifacts/{x["artifact_id"]}',headers={'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2026-03-10','User-Agent':'rqir-actions'})
    with urllib.request.urlopen(req,timeout=60) as r: m=json.load(r)
    if int(m['id'])!=x['artifact_id'] or m.get('expired') is True: raise SystemExit(('artifact_metadata_invalid',x['artifact_id'],m.get('expired')))
    x['run_id']=int(m['workflow_run']['id']); x['artifact_name']=str(m['name']); x['slot']=f"{x['family']}__{x['rank']}__{x['part']}"
print(json.dumps({'include':items},separators=(',',':')))
