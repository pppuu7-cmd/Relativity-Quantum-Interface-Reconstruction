#!/usr/bin/env python3
"""Iteration 582: q2-resolved e=2 connection effective-action assembly.

Consumes only raw-valid Iter581 complete Tr(U1^2) and authoritative Iter406
complete Tr(U2), then applies the already-frozen weights
+(i/2) TrU2 -(i/4) TrU1^2 q2-by-q2. Distinct q2 buckets are never summed.
This is connection-sector bookkeeping, not a comparator residual and not the
full Source/Ward/contact+K2 matched observable.
"""
import contextlib
import io
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
u1=json.loads((ROOT/'results'/'iteration581_frozen_iter412_exact15_raw_consumption.json').read_text())
if u1.get('classification')!='PASS_RAW_CONSUMED_FROZEN_ITER412_TRU1SQ_EXACT15' or u1.get('scientific_gate_pass') is not True:
    raise RuntimeError('iteration581_exact15_authority_missing')

# Re-execute authoritative Iter406 algebraic assembly from its frozen source and
# validate its identity rather than retyping a new TrU2 estimator.
code=(ROOT/'code'/'iteration406_u2_complete_operator_coordinate.py').read_text()
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    exec(compile(code,str(ROOT/'code'/'iteration406_u2_complete_operator_coordinate.py'),'exec'),{'__name__':'__main__'})
u2=json.loads(buf.getvalue())
if u2.get('classification')!='PASS_TRU2_COMPLETE_TIMELIKE_OPERATOR_COORDINATE_Q2_RESOLVED' or u2.get('scientific_gate_pass') is not True:
    raise RuntimeError('iteration406_tru2_authority_missing')

keys=('-1.0','-0.34','-0.14')
outq={}
for q in keys:
    a=u2['D_s_TrU2_complete_q2'][q]
    b=u1['D_s_TrU1sq_complete_q2'][q]
    if not (isinstance(a,list) and len(a)==2 and isinstance(b,list) and len(b)==2):
        raise RuntimeError(('coordinate_shape',q))
    A=complex(float(a[0]),float(a[1])); B=complex(float(b[0]),float(b[1]))
    if not all(math.isfinite(x) for x in (A.real,A.imag,B.real,B.imag)):
        raise RuntimeError(('nonfinite_input',q))
    val=0.5j*A-0.25j*B
    outq[q]=[float(val.real),float(val.imag)]

out={
 'iteration':582,
 'date':'2026-09-08',
 'classification':'PASS_E2_CONNECTION_EFFECTIVE_ACTION_Q2_RESOLVED__TRU2_PLUS_TRU1SQ',
 'scientific_gate_pass':True,
 'candidate_residual':False,
 'model_readiness_percent':24,
 'source_authorities':{
   'TrU2_iteration':406,
   'TrU2_classification':u2['classification'],
   'TrU1sq_iteration':581,
   'TrU1sq_classification':u1['classification'],
 },
 'formula':'D_s Gamma_e2_connection = +(i/2) D_s TrU2 - (i/4) D_s TrU1sq',
 'D_s_Gamma_e2_connection_q2':outq,
 'q2_buckets_kept_distinct':True,
 'scope':'CONNECTION_SECTOR_ONLY__NOT_FULL_SOURCE_WARD_CONTACT_K2',
 'guardrails':['DISTINCT_Q2_BUCKETS_NEVER_SUMMED','NO_SOURCE_BORN_SUBTRACTION','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES','NOT_A_COMPARATOR_RESIDUAL'],
 'next_gate':'raw-consume this artifact; then audit/freeze full D_s Gamma_e2 bookkeeping and construct concrete Source/Ward/contact+K2 matched observable before any fixed comparator quotient',
}
print(json.dumps(out,indent=2,sort_keys=True))
