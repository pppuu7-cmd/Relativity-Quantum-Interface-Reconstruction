#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 439.

Prospectively frozen binary64 conditioning diagnostic for the seven exact
Iteration-270 Acoef signed sums. Non-promoting; no physical amplification ceiling.
"""
from __future__ import annotations
import contextlib, hashlib, io, itertools, json, math
from pathlib import Path
import numpy as np

ITERATION=439
MODEL_READINESS=24
REPRO_LIMIT=1e-12
root=Path(__file__).resolve().parent
src=root/'iteration270_vd_physical_b3_nonzero.py'; raw=src.read_bytes(); text=raw.decode(); prefix=text.split('# A-layer certificates.')[0]
ns={'__name__':'iteration439_parent270'}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(prefix,str(src),'exec'),ns,ns)

subsets=[('s',),('a',),('b',),('s','a'),('s','b'),('a','b'),('s','a','b')]
h_by_n={1:1e-4,2:5e-4,3:1e-3}
rows=[]; node_count=0; max_amp=0.0; max_repro=0.0; all_finite=True
for legs in subsets:
    h=h_by_n[len(legs)]; modes=[ns['POS'][x] for x in legs]; K=ns['ksum'](ns['POS'],legs)
    terms=[]
    for sig in itertools.product((-1,1),repeat=len(legs)):
        A=ns['A_finite']([s*h for s in sig],modes,ns['P0'],K); node_count+=1
        finite=bool(np.all(np.isfinite(A))); all_finite=all_finite and finite
        terms.append((int(np.prod(sig)),A))
    signed=sum((sg*A for sg,A in terms),np.zeros((4,4),complex))
    abs_sum=sum((np.abs(A) for _,A in terms),np.zeros((4,4),float))
    denom=np.abs(signed)
    amp=np.divide(abs_sum,np.maximum(denom,1e-300))
    max_component_amp=float(np.max(amp)); max_amp=max(max_amp,max_component_amp)
    nonzero=denom[denom>0]
    min_nonzero=float(np.min(nonzero)) if nonzero.size else 0.0
    max_signed=float(np.max(denom))
    explicit=signed/(2*h)**len(legs)
    parent=ns['Acoef'](ns['POS'],list(legs),ns['P0'],h)
    scale=np.maximum(np.maximum(np.abs(explicit),np.abs(parent)),1.0)
    repro=float(np.max(np.abs(explicit-parent)/scale)); max_repro=max(max_repro,repro)
    finite=bool(np.all(np.isfinite(explicit)) and np.all(np.isfinite(parent))); all_finite=all_finite and finite
    rows.append({'legs':list(legs),'h':h,'signed_node_count':len(terms),'max_component_cancellation_amplification':max_component_amp,
                 'max_abs_signed_numerator_component':max_signed,'min_nonzero_abs_signed_numerator_component':min_nonzero,
                 'Acoef_fro_norm':float(np.linalg.norm(parent)),'explicit_vs_parent_Acoef_scaled':repro,'finite':finite})

subset_count=len(rows)
gate=bool(all_finite and node_count==26 and subset_count==7 and max_repro<=REPRO_LIMIT)
result={
 'iteration':ITERATION,'model_readiness_percent':MODEL_READINESS,'candidate_residual':False,
 'authority_scope':'DIAGNOSTIC_ONLY__ITERATION270_ACOEF_SIGNED_SUM_CONDITIONING',
 'classification':'PASS_ITER270_ACOEF_CANCELLATION_DIAGNOSTIC__NON_PROMOTING' if gate else 'BLOCKED_ITER270_ACOEF_CANCELLATION_DIAGNOSTIC_EXECUTION',
 'scientific_gate_pass':gate,'source_path':str(src),'source_sha256':hashlib.sha256(raw).hexdigest(),
 'frozen_inputs':{'M':'POS','P0':[float(x) for x in ns['P0']],'subsets':[list(x) for x in subsets],'h_by_subset_size':{'1':1e-4,'2':5e-4,'3':1e-3}},
 'validity_thresholds':{'explicit_vs_parent_Acoef_scaled_max':REPRO_LIMIT,'required_node_count':26,'required_subset_count':7},
 'observed':{'max_component_cancellation_amplification':max_amp,'max_explicit_vs_parent_Acoef_scaled':max_repro,'all_values_finite':all_finite,'node_count':node_count,'subset_count':subset_count},
 'rows':rows,
 'interpretation':'Cancellation amplification is diagnostic only. Large values localize where signed finite-difference combination may amplify lower-layer arithmetic noise; they neither block nor promote physical authority by themselves.',
 'next_gate':'Use this localization together with raw-valid Iteration 438 A_finite precision authority to design the separately frozen 80/120-digit Acoef/Asub derivative closure at unchanged h1/h2/h3.',
 'guardrails':['DIAGNOSTIC_ONLY','NO_CANCELLATION_PHYSICAL_CEILING','NO_PHYSICAL_DS_VALUE','NO_STEP_CHANGE','NO_THRESHOLD_WEAKENING','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
if not gate: raise SystemExit(2)
