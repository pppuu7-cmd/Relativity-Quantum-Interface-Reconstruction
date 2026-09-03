#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 384.

Complete-48 physical U2 cut-through-double-pole recovery, prospectively split
into immutable two-channel chunks after Iteration 382 measured a single frozen
channel at ~341 s.  Physics arithmetic is inherited verbatim from Iteration 364.
Only resource partition changes.

Environment:
  START_INDEX inclusive, even in {0,2,...,46}
  END_INDEX   exclusive, exactly START_INDEX+2

Each chunk emits both records even if one is BLOCKED_CONVERGENCE.  Execution
failure is reserved for structural/numerical-invalid conditions.  No +i/2
effective-action weight is folded.
"""
from __future__ import annotations
import contextlib, io, json, os, time
from collections import defaultdict
from pathlib import Path
import numpy as np

ITERATION=384
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration364_u2_repeated_pole_symmetric_aux_derivative_cut.py'
src=PARENT.read_text()
marker='records=[]; by_bucket=defaultdict(list)'
if src.count(marker)!=1:
    raise RuntimeError('iteration364_loop_marker_drift')
prefix=src.split(marker,1)[0]
ns={'__name__':'iteration384_parent364_prefix','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix,str(PARENT),'exec'),ns,ns)

P359=ns['P359']; channel_derivative=ns['channel_derivative']
CONVERGENCE_TOL=ns['CONVERGENCE_TOL']; SHELL_TOL=ns['SHELL_TOL']
BASE_H=ns['BASE_H']; HALF_H=ns['HALF_H']

all_channels=[]
for fam in P359['result']['families']:
    for ch in fam['timelike_distinct_group_channels']:
        if ch['repeated_pole_reduction_required']:
            all_channels.append((fam,ch))
if len(all_channels)!=48:
    raise RuntimeError(('iteration364_channel_census_drift',len(all_channels)))

start_i=int(os.environ['START_INDEX']); end_i=int(os.environ['END_INDEX'])
if not (0 <= start_i < 48 and end_i == start_i+2 and end_i <= 48 and start_i % 2 == 0):
    raise RuntimeError(('invalid_prospective_chunk',start_i,end_i))

records=[]; bucket_sums=defaultdict(complex); t0=time.perf_counter(); execution_valid=True
for global_index in range(start_i,end_i):
    fam,ch=all_channels[global_index]
    c0=time.perf_counter()
    low,es1,mu1,s,sgn,rg,og=channel_derivative(fam,ch,6,12,BASE_H,0.0)
    high,es2,mu2,_,_,_,_=channel_derivative(fam,ch,8,16,BASE_H,0.0)
    shifted,es3,mu3,_,_,_,_=channel_derivative(fam,ch,8,16,BASE_H,0.5)
    halfstep,es4,mu4,_,_,_,_=channel_derivative(fam,ch,8,16,HALF_H,0.0)
    runtime=time.perf_counter()-c0
    scale=max(1.0,abs(low),abs(high),abs(shifted),abs(halfstep))
    conv=float(max(abs(high-low),abs(high-shifted),abs(high-halfstep))/scale)
    shell=float(max(es1,es2,es3,es4)); umin=float(min(mu1,mu2,mu3,mu4))
    finite=bool(np.isfinite(conv) and np.isfinite(shell) and np.isfinite(umin))
    structural=bool(finite and shell<=SHELL_TOL and umin>1e-10)
    execution_valid = execution_valid and structural
    status='CONVERGED' if structural and conv<=CONVERGENCE_TOL else ('BLOCKED_CONVERGENCE' if structural else 'FAIL_EXECUTION')
    q2=float(ch['q2'])
    if status=='CONVERGED':
        bucket_sums[q2] += high
    records.append({
        'global_channel_index':global_index,
        'route':int(fam['route']),'subterm':int(fam['subterm']),
        'group_pair':list(map(int,ch['group_pair'])),'repeated_group':int(rg),'other_cut_group':int(og),
        'q2':q2,'status':status,'cut_algebraic_sign':float(sgn),
        'D_s_TrU2_repeated_high':[float(high.real),float(high.imag)],
        'D_s_TrU2_repeated_low':[float(low.real),float(low.imag)],
        'D_s_TrU2_repeated_high_phi_shifted':[float(shifted.real),float(shifted.imag)],
        'D_s_TrU2_repeated_halfstep':[float(halfstep.real),float(halfstep.imag)],
        'scaled_convergence_error':conv,'max_cut_shell_abs_error':shell,
        'minimum_sampled_uncut_abs_denominator':umin,'runtime_seconds':float(runtime)
    })

total_runtime=time.perf_counter()-t0
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
 'classification':('PASS_U2_REPEATED_CUT_FULL48_TWO_CHANNEL_CHUNK_EXECUTION' if execution_valid else
                   'FAIL_U2_REPEATED_CUT_FULL48_TWO_CHANNEL_CHUNK_EXECUTION'),
 'chunk':{'start_index':start_i,'end_index_exclusive':end_i,'expected_indices':list(range(start_i,end_i))},
 'records':records,
 'converged_count':sum(r['status']=='CONVERGED' for r in records),
 'blocked_convergence_count':sum(r['status']=='BLOCKED_CONVERGENCE' for r in records),
 'runtime_seconds':float(total_runtime),
 'partial_q2_sums_of_converged_channels_only':{
    str(q):[float(z.real),float(z.imag)] for q,z in sorted(bucket_sums.items())
 },
 'frozen_arithmetic':{'parent':'Iteration364 channel_derivative verbatim','base_h':BASE_H,'halfstep_h':HALF_H,
                      'low_grid':[6,12],'high_grid':[8,16],'phi_shift_check':0.5,
                      'convergence_threshold':CONVERGENCE_TOL,'shell_threshold':SHELL_TOL,
                      'normalization':'D_s_repeated=sphere_mean[d_mu2(beta*cut_sign*num/D_uncut)]'},
 'scope':'TWO_PROSPECTIVELY_FIXED_OF_48_U2_CUT_THROUGH_DOUBLE_POLE_CHANNELS__NO_EFFECTIVE_ACTION_WEIGHT',
 'guardrails':['ITERATION359_362_363_BINDING','ITERATION364_CHANNEL_DERIVATIVE_VERBATIM','ITERATION382_RESOURCE_AUTHORITY_ONLY',
               'NO_THRESHOLD_WEAKENING','EXACT_48_INDEX_ASSEMBLY_REQUIRED','BLOCKED_NEVER_ZERO_FILLED',
               'DISTINCT_Q2_BUCKETS_NEVER_SUMMED','NO_EFFECTIVE_ACTION_WEIGHT_FOLDING','NO_SOURCE_BORN_SUBTRACTION',
               'NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'after all 24 raw chunks exist, validate exact indices 0..47 once each; preserve every nonconverged channel as BLOCKED; assemble q2 sums only if all required channels in that q2 bucket are CONVERGED'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid:
    raise SystemExit(2)
