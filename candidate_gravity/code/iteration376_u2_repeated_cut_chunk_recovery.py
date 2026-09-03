#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 376.

Prospective resource-recovery of cancelled Iteration 364.
The scientific arithmetic is inherited verbatim from Iteration 364's frozen
channel_derivative implementation. Only the deterministic 48-channel loop is
partitioned into three fixed chunks [0:16], [16:32], [32:48].

No thresholds, quadratures, auxiliary-mass nodes, routing, numerator logic or
normalization are changed. This is a resource architecture change only.
"""
from __future__ import annotations
import contextlib, io, json, os
from collections import defaultdict
from pathlib import Path
import numpy as np

ITERATION=376
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration364_u2_repeated_pole_symmetric_aux_derivative_cut.py'
src=PARENT.read_text()
marker='records=[]; by_bucket=defaultdict(list)'
if src.count(marker)!=1:
    raise RuntimeError('iteration364_loop_marker_drift')
prefix=src.split(marker,1)[0]
ns={'__name__':'iteration376_parent364_prefix','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix,str(PARENT),'exec'),ns,ns)

P359=ns['P359']; channel_derivative=ns['channel_derivative']
CONVERGENCE_TOL=ns['CONVERGENCE_TOL']; SHELL_TOL=ns['SHELL_TOL']; BASE_H=ns['BASE_H']; HALF_H=ns['HALF_H']

all_channels=[]
for fam in P359['result']['families']:
    for ch in fam['timelike_distinct_group_channels']:
        if ch['repeated_pole_reduction_required']:
            all_channels.append((fam,ch))
if len(all_channels)!=48:
    raise RuntimeError(('iteration364_channel_census_drift',len(all_channels)))

chunk=int(os.environ.get('RQIR_CHUNK','0'))
if chunk not in (0,1,2):
    raise RuntimeError(('invalid_chunk',chunk))
start=16*chunk; stop=start+16
selected=all_channels[start:stop]

records=[]; by_bucket=defaultdict(list)
max_conv=0.0; max_shell=0.0; min_uncut=float('inf'); blocked=0
for local_idx,(fam,ch) in enumerate(selected):
    global_idx=start+local_idx
    low,es1,mu1,s,sgn,rg,og=channel_derivative(fam,ch,6,12,BASE_H,0.0)
    high,es2,mu2,_,_,_,_=channel_derivative(fam,ch,8,16,BASE_H,0.0)
    shifted,es3,mu3,_,_,_,_=channel_derivative(fam,ch,8,16,BASE_H,0.5)
    halfstep,es4,mu4,_,_,_,_=channel_derivative(fam,ch,8,16,HALF_H,0.0)
    scale=max(1.0,abs(low),abs(high),abs(shifted),abs(halfstep))
    conv=float(max(abs(high-low),abs(high-shifted),abs(high-halfstep))/scale)
    shell=max(es1,es2,es3,es4)
    status='CONVERGED' if conv<=CONVERGENCE_TOL and shell<=SHELL_TOL else 'BLOCKED_CONVERGENCE'
    if status!='CONVERGED': blocked+=1
    max_conv=max(max_conv,conv); max_shell=max(max_shell,shell); min_uncut=min(min_uncut,mu1,mu2,mu3,mu4)
    q2=float(ch['q2']); qkey=round(q2,12)
    rec={'global_channel_index':global_idx,'route':int(fam['route']),'subterm':int(fam['subterm']),
         'group_pair':list(map(int,ch['group_pair'])),'repeated_group':int(rg),'other_cut_group':int(og),
         'q2':q2,'status':status,'cut_algebraic_sign':float(sgn),
         'D_s_TrU2_repeated_high':[float(high.real),float(high.imag)],
         'D_s_TrU2_repeated_low':[float(low.real),float(low.imag)],
         'D_s_TrU2_repeated_high_phi_shifted':[float(shifted.real),float(shifted.imag)],
         'D_s_TrU2_repeated_halfstep':[float(halfstep.real),float(halfstep.imag)],
         'scaled_convergence_error':conv,'max_cut_shell_abs_error':shell,
         'minimum_sampled_uncut_abs_denominator':min(mu1,mu2,mu3,mu4)}
    records.append(rec); by_bucket[qkey].append(rec)

by_q2={}
for q2,recs in sorted(by_bucket.items()):
    vals=[complex(*r['D_s_TrU2_repeated_high']) for r in recs if r['status']=='CONVERGED']
    sm=sum(vals,0j)
    by_q2[str(q2)]={'chunk_channel_count':len(recs),'converged_channel_count':len(vals),
                    'partial_D_s_TrU2_cut_through_double_pole_sum':[float(sm.real),float(sm.imag)] if len(vals)==len(recs) else None,
                    'status':'CONVERGED' if len(vals)==len(recs) else 'BLOCKED_PARTIAL'}

classified=bool(len(records)==16 and max_shell<=SHELL_TOL and [r['global_channel_index'] for r in records]==list(range(start,stop)))
all_converged=bool(classified and blocked==0 and max_conv<=CONVERGENCE_TOL)
result={
 'iteration':ITERATION,'chunk':chunk,'global_channel_range':[start,stop],'model_readiness_percent':24,
 'scientific_gate_pass':classified,'candidate_residual':False,
 'classification':('PASS_U2_REPEATED_CUT_CHUNK_RESOURCE_RECOVERY__ALL_16_CONVERGED' if all_converged else
                   'PASS_U2_REPEATED_CUT_CHUNK_CLASSIFIED__SOME_CONVERGENCE_BLOCKED' if classified else
                   'FAIL_U2_REPEATED_CUT_CHUNK_RECOVERY_GATE'),
 'parent_authority':'Iteration364 frozen channel_derivative; Iteration364 run was operationally cancelled at 40-minute timeout before artifact',
 'census':{'chunk_channels':len(records),'CONVERGED':len(records)-blocked,'BLOCKED_CONVERGENCE':blocked,
           'max_scaled_convergence_error':max_conv,'max_cut_shell_abs_error':max_shell,'minimum_sampled_uncut_abs_denominator':min_uncut},
 'frozen_arithmetic':{'base_h':BASE_H,'halfstep_h':HALF_H,'low_grid':[6,12],'high_grid':[8,16],
                      'phi_shift_check':0.5,'convergence_threshold':CONVERGENCE_TOL,'shell_threshold':SHELL_TOL},
 'by_q2_partial':by_q2,'channels':records,
 'scope':'RESOURCE_RECOVERY_CHUNK_ONLY__ASSEMBLY_REQUIRES_ALL_THREE_VALIDATED_CHUNKS',
 'guardrails':['NO_CHANGE_TO_ITERATION364_CHANNEL_DERIVATIVE','NO_THRESHOLD_WEAKENING','FIXED_CHANNEL_ORDER_AND_FIXED_16_CHANNEL_CHUNKS',
               'NO_PARTIAL_CHUNK_PROMOTION_TO_FULL_TRU2','DISTINCT_Q2_BUCKETS_NEVER_SUMMED','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'after all chunks 0,1,2 validate, assemble exactly the 48 unique global channel indices and q2-resolved sums; reject overlap, gaps, or provenance mismatch'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not classified:
    raise SystemExit(2)
