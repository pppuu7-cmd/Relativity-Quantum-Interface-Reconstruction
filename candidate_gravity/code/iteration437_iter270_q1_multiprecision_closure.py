#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 437.

80/120-digit closure of the exact Iteration-270 Q1 formula using the raw-valid
Iteration-436 arbitrary-precision parent implementation for N1 and norb.
Non-promoting; thresholds were frozen before workflow result inspection.
"""
from __future__ import annotations
import contextlib, hashlib, io, json
from pathlib import Path
import numpy as np
import mpmath as mp

ITERATION=437
MP_LEVELS=(80,120)
MP_CROSS_LIMIT=mp.mpf('1e-40')
Q0_BINARY64_REPRO_LIMIT=1e-12
LEGACY_Q1_PHYSICAL_REFERENCE=2e-5
MODEL_READINESS=24

root=Path(__file__).resolve().parent
src436=root/'iteration436_iter270_n1_multiprecision_closure.py'
text436=src436.read_text(); marker='rows=[]'
if text436.count(marker)!=1:
    raise SystemExit(('iteration436_execution_boundary_drift',text436.count(marker)))
parent={'__name__':'iteration437_parent436_prefix','__file__':str(src436)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(text436.split(marker,1)[0],str(src436),'exec'),parent,parent)

base=parent['ns']
if not Path(base['__file__'] if '__file__' in base else str(root/'iteration270_vd_physical_b3_nonzero.py')):
    pass
src270=root/'iteration270_vd_physical_b3_nonzero.py'; raw270=src270.read_bytes(); text270=raw270.decode()
source_checks={
    'Q1_signature':'def Q1(M,x,p,h=3e-5):' in text270,
    'Q1_formula':'return -Q0(p+k)@N1(M,x,p,h)@Q0(p)' in text270,
    'Q0_signature':'def Q0(p): return np.linalg.inv(N0(p))' in text270,
    'N0_signature':'def N0(p): return norb([],[],p)' in text270,
    'iteration436_N1_authority_file':(root.parent/'results'/'iteration436_n1_multiprecision_closure_summary.json').exists(),
}
if not all(source_checks.values()):
    raise SystemExit(('source_or_prerequisite_drift',source_checks))
summary436=json.loads((root.parent/'results'/'iteration436_n1_multiprecision_closure_summary.json').read_text())
if not (summary436.get('scientific_gate_pass') is True and summary436.get('iteration')==436 and
        summary436.get('classification')=='PASS_ITER270_N1_80_120_DIGIT_CLOSURE__LEGACY_REPRODUCED__NON_PROMOTING'):
    raise SystemExit(('iteration436_not_raw_bound_pass',summary436.get('classification')))

mp_vec_from_np=parent['mp_vec_from_np']
mp_max_scaled_matrix_diff=parent['mp_max_scaled_matrix_diff']
np_mp_max_scaled_matrix_diff=parent['np_mp_max_scaled_matrix_diff']
norb_mp=parent['norb_mp']
evaluate_leg_at_precision=parent['evaluate_leg_at_precision']
mp_fro_norm=parent['mp_fro_norm']


def q0_mp(p_np):
    return norb_mp([],[],p_np)**-1


def evaluate_q1_at_precision(x,dps):
    with mp.workdps(dps):
        p=np.asarray(base['P0'],float); k=np.asarray(base['POS'][x][0],float)
        q0p=q0_mp(p); q0pk=q0_mp(p+k)
        n1=evaluate_leg_at_precision(x,dps)[2]
        q1=-(q0pk*n1*q0p)
        return q0p,q0pk,n1,q1

rows=[]; q0_rows=[]
max_q0_cross=mp.mpf('0'); max_q0_binary64=0.0; max_q1_cross=mp.mpf('0'); max_q1_binary64=0.0
all_finite=True

# Q0(P0) and every shifted Q0(P0+k_x) are independently certified.
q0_inputs=[('P0',np.asarray(base['P0'],float))]
for x in base['LEGS']:
    q0_inputs.append((f'P0_plus_K_{x}',np.asarray(base['P0'],float)+np.asarray(base['POS'][x][0],float)))
for label,p in q0_inputs:
    refs={}
    for dps in MP_LEVELS:
        with mp.workdps(dps): refs[dps]=q0_mp(p)
    with mp.workdps(160): cross=mp_max_scaled_matrix_diff(refs[80],refs[120])
    q064=base['Q0'](p); legacy=np_mp_max_scaled_matrix_diff(q064,refs[120])
    max_q0_cross=max(max_q0_cross,cross); max_q0_binary64=max(max_q0_binary64,legacy)
    finite=bool(np.all(np.isfinite(q064))) and all(mp.isfinite(refs[d][i,j]) for d in MP_LEVELS for i in range(4) for j in range(4))
    all_finite=all_finite and finite
    q0_rows.append({'input':label,'momentum':[float(z) for z in p],
                    'mp80_vs_mp120_Q0_scaled':mp.nstr(cross,30),
                    'binary64_vs_mp120_Q0_scaled':legacy,'finite':bool(finite)})

for x in base['LEGS']:
    refs={d:evaluate_q1_at_precision(x,d) for d in MP_LEVELS}
    with mp.workdps(160): cross=mp_max_scaled_matrix_diff(refs[80][3],refs[120][3])
    q164=base['Q1'](base['POS'],x,base['P0'],3e-5)
    legacy=np_mp_max_scaled_matrix_diff(q164,refs[120][3])
    max_q1_cross=max(max_q1_cross,cross); max_q1_binary64=max(max_q1_binary64,legacy)
    finite=bool(np.all(np.isfinite(q164))) and all(mp.isfinite(refs[d][k][i,j]) for d in MP_LEVELS for k in (0,1,2,3) for i in range(4) for j in range(4))
    all_finite=all_finite and finite
    rows.append({'leg':x,'h':3e-5,
                 'mp80_vs_mp120_Q1_scaled':mp.nstr(cross,30),
                 'binary64_vs_mp120_Q1_scaled':legacy,
                 'mp120_Q1_fro_norm':mp.nstr(mp_fro_norm(refs[120][3]),30),
                 'finite':bool(finite)})

q0_closed=bool(max_q0_cross<=MP_CROSS_LIMIT and max_q0_binary64<=Q0_BINARY64_REPRO_LIMIT)
q1_closed=bool(max_q1_cross<=MP_CROSS_LIMIT)
legacy_q1_reproduced=bool(max_q1_binary64<=LEGACY_Q1_PHYSICAL_REFERENCE)
gate=bool(q0_closed and q1_closed and all_finite)
if gate and legacy_q1_reproduced:
    classification='PASS_ITER270_Q1_80_120_DIGIT_CLOSURE__LEGACY_REPRODUCED__NON_PROMOTING'
elif gate:
    classification='PASS_ITER270_Q1_80_120_DIGIT_CLOSURE__LEGACY_DRIFT_MATERIAL__NON_PROMOTING'
else:
    classification='BLOCKED_ITER270_Q1_MULTIPRECISION_CLOSURE'

result={
    'iteration':ITERATION,'model_readiness_percent':MODEL_READINESS,'candidate_residual':False,
    'authority_scope':'PARENT_PRECISION_CLOSURE__ITERATION270_Q1_ONLY__NON_PROMOTING',
    'classification':classification,'scientific_gate_pass':gate,
    'source_path':str(src270),'source_sha256':hashlib.sha256(raw270).hexdigest(),'source_checks':source_checks,
    'prerequisite_iteration436':{'classification':summary436.get('classification'),'raw_scientific_json_sha256':summary436.get('provenance',{}).get('raw_scientific_json_sha256')},
    'frozen_inputs':{'M':'POS','legs':list(base['LEGS']),'P0':[float(x) for x in base['P0']],'h':3e-5,
                     'shifted_Q0_inputs':[r['momentum'] for r in q0_rows[1:]]},
    'precision_levels_decimal_digits':list(MP_LEVELS),
    'thresholds':{'mp80_vs_mp120_Q0_scaled_max':'1e-40','binary64_vs_mp120_Q0_scaled_max':Q0_BINARY64_REPRO_LIMIT,
                  'mp80_vs_mp120_Q1_scaled_max':'1e-40','legacy_binary64_vs_mp120_Q1_physical_reference':LEGACY_Q1_PHYSICAL_REFERENCE},
    'observed':{'max_mp80_vs_mp120_Q0_scaled':mp.nstr(max_q0_cross,30),'max_binary64_vs_mp120_Q0_scaled':max_q0_binary64,
                'max_mp80_vs_mp120_Q1_scaled':mp.nstr(max_q1_cross,30),'max_binary64_vs_mp120_Q1_scaled':max_q1_binary64,
                'legacy_Q1_reproduced_within_2e-5':legacy_q1_reproduced,'all_values_finite':all_finite},
    'q0_rows':q0_rows,'q1_rows':rows,
    'interpretation':('PASS certifies Q1 numerical realization at the exact frozen Iteration-270 Q1 momenta using raw-bound Iteration-436 N1 and independently certified Q0(P0), Q0(P0+k_x). It does not certify A_finite/Acoef/Asub or downstream Candidate-Gravity physical coordinates.'),
    'next_gate':('if raw-valid PASS, close A_finite/Acoef/Asub deepest parent arithmetic next; if blocked, preserve Q1 and diagnose the failed Q0/Q1 precision subcriterion without changing h or inputs'),
    'guardrails':['NO_PHYSICAL_DS_VALUE','Q1_ONLY','ITERATION436_N1_PREREQUISITE','NO_THRESHOLD_WEAKENING','NO_H_CHANGE','NO_PARENT_DYNAMICS_CHANGE','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
if not gate: raise SystemExit(2)
