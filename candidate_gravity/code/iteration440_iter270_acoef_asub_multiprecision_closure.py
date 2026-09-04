#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 440.

Prospectively frozen 80/120-digit arithmetic closure of the exact Iteration-270
Acoef/Asub signed finite-difference assembly at the unchanged h1/h2/h3 nodes.
This is non-promoting and separates arithmetic precision from stencil truncation.
"""
from __future__ import annotations
import contextlib, hashlib, io, itertools, json
from pathlib import Path
import numpy as np
import mpmath as mp

ITERATION=440
MODEL_READINESS=24
MP_LEVELS=(80,120)
MP_CROSS_LIMIT=mp.mpf('1e-30')
REQUIRED_SUBSETS=7
REQUIRED_NODES=26

root=Path(__file__).resolve().parent
src270=root/'iteration270_vd_physical_b3_nonzero.py'
raw270=src270.read_bytes(); text270=raw270.decode()
source_checks={
 'A_finite':'def A_finite(amps,modes,p,total_shift):' in text270,
 'Acoef':'def Acoef(M,legs,p,h):' in text270,
 'Asub':'def Asub(M,legs,p,h1=1e-4,h2=5e-4,h3=1e-3):' in text270,
}
if not all(source_checks.values()): raise SystemExit(('iteration270_source_drift',source_checks))

# Reuse only the prospectively frozen arbitrary-precision A_finite implementation
# from Iteration 438. Stop before that script begins result inspection.
src438=root/'iteration438_iter270_a_finite_multiprecision_core.py'
t438=src438.read_text(); marker="subsets=[('s',),('a',),('b',),('s','a'),('s','b'),('a','b'),('s','a','b')]"
if t438.count(marker)!=1: raise SystemExit(('iteration438_boundary_drift',t438.count(marker)))
P={'__name__':'iteration440_parent438_prefix','__file__':str(src438)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(t438.split(marker,1)[0],str(src438),'exec'),P,P)
base=P['base']; A_finite_mp=P['A_finite_mp']; mp_max_scaled_matrix_diff=P['mp_max_scaled_matrix_diff']; np_mp_max_scaled_matrix_diff=P['np_mp_max_scaled_matrix_diff']; mp_fro_norm=P['mp_fro_norm']

# Bind already-consumed prerequisites fail-closed.
resdir=root.parent/'results'
s438=json.loads((resdir/'iteration438_a_finite_multiprecision_core_summary.json').read_text())
s439=json.loads((resdir/'iteration439_acoef_cancellation_diagnostic_summary.json').read_text())
if not (s438.get('scientific_gate_pass') is True and s439.get('scientific_gate_pass') is True):
    raise SystemExit('iteration438_439_prerequisite_not_passed')

subsets=[('s',),('a',),('b',),('s','a'),('s','b'),('a','b'),('s','a','b')]
hstr={1:'1e-4',2:'5e-4',3:'1e-3'}
rows=[]; max_cross=mp.mpf('0'); max_legacy=0.0; all_finite=True; node_count=0
for legs in subsets:
    modes=[base['POS'][x] for x in legs]
    total_shift=sum((np.asarray(base['POS'][x][0],float) for x in legs),np.zeros(4))
    refs={}
    for dps in MP_LEVELS:
        with mp.workdps(dps):
            h=mp.mpf(hstr[len(legs)])
            signed=mp.matrix(4,4)
            for sig in itertools.product((-1,1),repeat=len(legs)):
                node_count += 1 if dps==80 else 0
                A=A_finite_mp([mp.mpf(s)*h for s in sig],modes,base['P0'],total_shift)
                signed += int(np.prod(sig))*A
            refs[dps]=signed/(2*h)**len(legs)
    with mp.workdps(160): cross=mp_max_scaled_matrix_diff(refs[80],refs[120])
    h64=float(hstr[len(legs)]); legacy=base['Acoef'](base['POS'],list(legs),base['P0'],h64)
    legacy_delta=np_mp_max_scaled_matrix_diff(legacy,refs[120])
    finite=bool(np.all(np.isfinite(legacy))) and all(mp.isfinite(refs[d][i,j]) for d in MP_LEVELS for i in range(4) for j in range(4))
    max_cross=max(max_cross,cross); max_legacy=max(max_legacy,legacy_delta); all_finite=all_finite and finite
    rows.append({'legs':list(legs),'h':h64,'mp80_vs_mp120_Acoef_scaled':mp.nstr(cross,30),'binary64_vs_mp120_Acoef_scaled':legacy_delta,'mp120_fro_norm':mp.nstr(mp_fro_norm(refs[120]),30),'finite':finite})

subset_count=len(rows)
gate=bool(max_cross<=MP_CROSS_LIMIT and all_finite and node_count==REQUIRED_NODES and subset_count==REQUIRED_SUBSETS)
classification='PASS_ITER270_ACOEF_ASUB_80_120_DIGIT_ARITHMETIC_CLOSURE__NON_PROMOTING' if gate else 'BLOCKED_ITER270_ACOEF_ASUB_MULTIPRECISION_CLOSURE'
result={
 'iteration':ITERATION,'model_readiness_percent':MODEL_READINESS,'candidate_residual':False,
 'authority_scope':'PARENT_PRECISION_CLOSURE__ITERATION270_ACOEF_ASUB_SIGNED_ASSEMBLY__NON_PROMOTING',
 'classification':classification,'scientific_gate_pass':gate,
 'source_path':str(src270),'source_sha256':hashlib.sha256(raw270).hexdigest(),'source_checks':source_checks,
 'prerequisites':{'iteration438':s438.get('classification'),'iteration439':s439.get('classification')},
 'frozen_inputs':{'M':'POS','P0':[float(x) for x in base['P0']],'subsets':[list(x) for x in subsets],'h_by_subset_size':{'1':1e-4,'2':5e-4,'3':1e-3},'node_count':node_count,'subset_count':subset_count},
 'precision_levels_decimal_digits':list(MP_LEVELS),
 'thresholds':{'mp80_vs_mp120_Acoef_scaled_max':'1e-30','required_node_count':REQUIRED_NODES,'required_subset_count':REQUIRED_SUBSETS},
 'observed':{'max_mp80_vs_mp120_Acoef_scaled':mp.nstr(max_cross,30),'max_binary64_vs_mp120_Acoef_scaled_diagnostic_only':max_legacy,'all_values_finite':all_finite,'node_count':node_count,'subset_count':subset_count},
 'rows':rows,
 'interpretation':'PASS certifies arithmetic closure of the exact frozen Acoef/Asub signed assembly at 80/120 digits. Binary64-vs-mp120 is reported diagnostically only. This gate does not certify finite-difference truncation, alternate-step stability, 368/370, 379/374, 407, Iteration 424, or physical index-2 D_s.',
 'next_gate':'If raw-valid PASS, freeze a separate Acoef/Asub stencil-truncation or algebraic-derivative consistency gate before any outward precision claim.',
 'guardrails':['NO_PHYSICAL_DS_VALUE','UNCHANGED_H1_H2_H3','ARITHMETIC_PRECISION_ONLY','NO_THRESHOLD_WEAKENING','NO_PARENT_DYNAMICS_CHANGE','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
if not gate: raise SystemExit(2)
