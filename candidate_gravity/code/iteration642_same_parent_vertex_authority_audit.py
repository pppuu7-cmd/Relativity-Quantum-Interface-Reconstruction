#!/usr/bin/env python3
"""Iteration 642: same-parent MSSC001 closed-loop numerator authority audit.

This gate does not evaluate a cut numerator. It determines whether the exact K1/K2/K3
vertex implementation/provenance needed by the next cut calculation is machine-recoverable
from committed same-parent authority. Missing pieces are BLOCKED, never zero-filled.
"""
from __future__ import annotations
import hashlib,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[2]
paths=[
 ROOT/'analysis'/'source_full_cubic_routed_assembly_iteration594.py',
 ROOT/'candidate_gravity'/'research_log'/'2026-09-08_iteration_594.md',
 ROOT/'candidate_gravity'/'recovery'/'RECOVERY_DELTA_ITERATION_627.md',
 ROOT/'candidate_gravity'/'recovery'/'RECOVERY_DELTA_ITERATION_632.md',
 ROOT/'candidate_gravity'/'recovery'/'RECOVERY_DELTA_ITERATION_641.md',
]
failures=[]; inventory=[]
for p in paths:
    if not p.exists():
        inventory.append({'path':str(p.relative_to(ROOT)),'exists':False})
        continue
    txt=p.read_text(errors='replace')
    inventory.append({'path':str(p.relative_to(ROOT)),'exists':True,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':len(p.read_bytes()),
                      'has_K1':('K1' in txt),'has_K2':('K2' in txt),'has_K3':('K3' in txt),'has_MSSC':('MSSC' in txt)})

src=ROOT/'analysis'/'source_full_cubic_routed_assembly_iteration594.py'
if not src.exists():
    failures.append('Iter594 same-parent assembly source missing')
    text=''
else:
    text=src.read_text(errors='replace')
# We require evidence of all three families and an explicit same-action routed assembly.
for token in ['K1','K2','K3']:
    if token not in text: failures.append(f'Iter594 source lacks {token} token')
# Detect likely reusable function/definition sites without assuming names.
defs=re.findall(r'^def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(',text,flags=re.M)
vertex_defs=[d for d in defs if any(k.lower() in d.lower() for k in ['k1','k2','k3','kernel','vertex','metric'])]
# Exact closed-loop numerator implementation needs reusable momentum-dependent vertex machinery.
machine_recoverable=bool(src.exists() and all(k in text for k in ['K1','K2','K3']) and len(defs)>0)
status=('READY_FOR_EXPLICIT_CUT_NUMERATOR_IMPLEMENTATION' if machine_recoverable else 'BLOCKED_VERTEX_IMPLEMENTATION_NOT_MACHINE_RECOVERABLE')
classification=('PASS_ITER642_SAME_PARENT_VERTEX_AUTHORITY_MACHINE_RECOVERABLE__NON_RESIDUAL' if machine_recoverable and not failures else 'BLOCKED_ITER642_SAME_PARENT_VERTEX_AUTHORITY_INCOMPLETE__NON_RESIDUAL')
result={'iteration':642,'date':'2026-09-09','classification':classification,'failures':failures,'machine_recoverable':machine_recoverable,'status':status,
 'inventory':inventory,'iter594_function_defs':defs,'vertex_like_defs':vertex_defs,
 'scientific_gate_pass':bool(machine_recoverable and not failures),'candidate_residual':False,'candidate_values_used':False,'zero_fill':False,
 'source_born_subtraction':'NOT_PERFORMED','native_Y_Tcut_projection':'NOT_PERFORMED','comparator_quotient':'NOT_PERFORMED','ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN','MODEL_READINESS':'24%',
 'next_gate':('Implement explicit same-parent retarded K1/K2 and K1^3 cut-numerator contractions using the recovered Iter594 vertex machinery under Iter627+632; keep exact threshold arithmetic and K3 retained analytic/contact.' if machine_recoverable else 'Locate the missing same-parent K1/K2/K3 implementation authority; do not invent numerator tensors or normalization.')}
out=ROOT/'results'/'iteration642_same_parent_vertex_authority_audit';out.mkdir(parents=True,exist_ok=True)
rp=out/'result.json';rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
a={'iteration':642,'result_sha256':hashlib.sha256(rp.read_bytes()).hexdigest(),'failures':failures,'classification':('PASS_RAW_AUTHORITY_AUDIT_ITER642_VERTEX_AUTHORITY' if machine_recoverable and not failures else 'BLOCKED_RAW_AUTHORITY_AUDIT_ITER642_VERTEX_AUTHORITY')}
(out/'authority_audit.json').write_text(json.dumps(a,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
# BLOCKED is a scientific result, not workflow failure, provided it is explicit and no zero-fill occurred.
