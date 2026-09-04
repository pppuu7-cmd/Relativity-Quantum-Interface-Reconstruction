#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 394.

Second/final topology-aware recovery matrix for the seven Iteration-384 chunks
not covered by Iteration 390: 24-25, 26-27, 32-33, 36-37, 38-39, 42-43,
44-45. Physical channel_derivative arithmetic is imported verbatim from
Iteration 364. No grid, derivative step, numerator, routing, sign or threshold
is changed.

The structural wrapper is strengthened by the prospectively frozen Iteration-392
theorem: +Infinity is valid iff the selected two-group cut leaves zero uncut
denominator groups; otherwise a finite minimum >1e-10 is mandatory.
"""
from __future__ import annotations
import contextlib, io, json, os, time
from collections import defaultdict
from pathlib import Path
import numpy as np

ITERATION=394
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration364_u2_repeated_pole_symmetric_aux_derivative_cut.py'
src=PARENT.read_text(); marker='records=[]; by_bucket=defaultdict(list)'
if src.count(marker)!=1: raise RuntimeError('iteration364_loop_marker_drift')
ns={'__name__':'iteration394_parent364_prefix','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split(marker,1)[0],str(PARENT),'exec'),ns,ns)
P359=ns['P359']; channel_derivative=ns['channel_derivative']
CONVERGENCE_TOL=ns['CONVERGENCE_TOL']; SHELL_TOL=ns['SHELL_TOL']; BASE_H=ns['BASE_H']; HALF_H=ns['HALF_H']

all_channels=[]
for fam in P359['result']['families']:
    groups=fam['groups']
    for ch in fam['timelike_distinct_group_channels']:
        if ch['repeated_pole_reduction_required']:
            pair=list(map(int,ch['group_pair']))
            uncut=[g for g in range(len(groups)) if g not in set(pair)]
            all_channels.append((fam,ch,len(groups),uncut))
if len(all_channels)!=48: raise RuntimeError(('channel_census_drift',len(all_channels)))

# Exact Iteration-392 frozen no-uncut mask, asserted again from Iteration-359 topology.
FROZEN_NO_UNCUT={4,13,22,27,28,29,30,33,36,39,42,45}
derived={i for i,(_,_,_,uncut) in enumerate(all_channels) if len(uncut)==0}
if derived!=FROZEN_NO_UNCUT:
    raise RuntimeError(('iteration392_topology_mask_drift',sorted(derived)))

start_i=int(os.environ['START_INDEX']); end_i=int(os.environ['END_INDEX'])
if not (0<=start_i<48 and end_i==start_i+2 and end_i<=48 and start_i%2==0):
    raise RuntimeError(('invalid_chunk',start_i,end_i))
allowed={(24,26),(26,28),(32,34),(36,38),(38,40),(42,44),(44,46)}
if (start_i,end_i) not in allowed:
    raise RuntimeError(('not_a_frozen_iteration394_recovery_chunk',start_i,end_i))

records=[]; bucket_sums=defaultdict(complex); execution_valid=True; t0=time.perf_counter()
for global_index in range(start_i,end_i):
    fam,ch,group_count,uncut_groups=all_channels[global_index]; c0=time.perf_counter()
    low,es1,mu1,s,sgn,rg,og=channel_derivative(fam,ch,6,12,BASE_H,0.0)
    high,es2,mu2,_,_,_,_=channel_derivative(fam,ch,8,16,BASE_H,0.0)
    shifted,es3,mu3,_,_,_,_=channel_derivative(fam,ch,8,16,BASE_H,0.5)
    halfstep,es4,mu4,_,_,_,_=channel_derivative(fam,ch,8,16,HALF_H,0.0)
    runtime=time.perf_counter()-c0
    scale=max(1.0,abs(low),abs(high),abs(shifted),abs(halfstep))
    conv=float(max(abs(high-low),abs(high-shifted),abs(high-halfstep))/scale)
    shell=float(max(es1,es2,es3,es4)); umin=float(min(mu1,mu2,mu3,mu4))
    numeric_finite=bool(np.isfinite(conv) and np.isfinite(shell))
    topology_no_uncut=(global_index in FROZEN_NO_UNCUT)
    topology_consistent=bool(topology_no_uncut==(len(uncut_groups)==0))
    uncut_ok=bool((topology_no_uncut and np.isinf(umin)) or
                  ((not topology_no_uncut) and np.isfinite(umin) and umin>1e-10))
    structural=bool(numeric_finite and shell<=SHELL_TOL and topology_consistent and uncut_ok)
    execution_valid = execution_valid and structural
    status='CONVERGED' if structural and conv<=CONVERGENCE_TOL else ('BLOCKED_CONVERGENCE' if structural else 'FAIL_EXECUTION')
    q2=float(ch['q2'])
    if status=='CONVERGED': bucket_sums[q2]+=high
    records.append({
      'global_channel_index':global_index,'route':int(fam['route']),'subterm':int(fam['subterm']),
      'group_pair':list(map(int,ch['group_pair'])),'repeated_group':int(rg),'other_cut_group':int(og),'q2':q2,'status':status,
      'cut_algebraic_sign':float(sgn),'D_s_TrU2_repeated_high':[float(high.real),float(high.imag)],
      'D_s_TrU2_repeated_low':[float(low.real),float(low.imag)],
      'D_s_TrU2_repeated_high_phi_shifted':[float(shifted.real),float(shifted.imag)],
      'D_s_TrU2_repeated_halfstep':[float(halfstep.real),float(halfstep.imag)],
      'scaled_convergence_error':conv,'max_cut_shell_abs_error':shell,
      'minimum_sampled_uncut_abs_denominator':umin,'denominator_group_count':int(group_count),
      'uncut_group_indices':list(map(int,uncut_groups)),'topology_no_uncut_denominator':topology_no_uncut,
      'iteration392_mask_consistent':topology_consistent,'uncut_policy_pass':uncut_ok,'runtime_seconds':float(runtime)})

result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
 'classification':('PASS_U2_REMAINING7_TOPOLOGY_MASKED_RECOVERY_CHUNK_EXECUTION' if execution_valid else 'FAIL_U2_REMAINING7_TOPOLOGY_MASKED_RECOVERY_CHUNK_EXECUTION'),
 'source_scientific_iteration':384,'topology_authority_iteration':392,
 'frozen_no_uncut_indices':sorted(FROZEN_NO_UNCUT),
 'classification_repair':'INFINITY_ALLOWED_IFF_ITERATION392_MASK_SAYS_EMPTY_UNCUT_SET',
 'chunk':{'start_index':start_i,'end_index_exclusive':end_i,'expected_indices':list(range(start_i,end_i))},
 'records':records,'converged_count':sum(r['status']=='CONVERGED' for r in records),
 'blocked_convergence_count':sum(r['status']=='BLOCKED_CONVERGENCE' for r in records),
 'runtime_seconds':float(time.perf_counter()-t0),
 'partial_q2_sums_of_converged_channels_only':{str(q):[float(z.real),float(z.imag)] for q,z in sorted(bucket_sums.items())},
 'frozen_arithmetic':{'parent':'Iteration364 channel_derivative verbatim','base_h':BASE_H,'halfstep_h':HALF_H,
   'low_grid':[6,12],'high_grid':[8,16],'phi_shift_check':0.5,'convergence_threshold':CONVERGENCE_TOL,
   'shell_threshold':SHELL_TOL,'finite_uncut_threshold':1e-10,
   'normalization':'D_s_repeated=sphere_mean[d_mu2(beta*cut_sign*num/D_uncut)]'},
 'guardrails':['ITERATION392_TOPOLOGY_MASK_BINDING','NO_PHYSICS_ARITHMETIC_CHANGE','NO_THRESHOLD_WEAKENING','NO_ZERO_FILL',
   'EXACT_48_INDEX_ASSEMBLY_REQUIRED','DISTINCT_Q2_BUCKETS_NEVER_SUMMED','NO_EFFECTIVE_ACTION_WEIGHT_FOLDING',
   'NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'merge these raw-valid records with original Iteration384, Iteration391, and Iteration390 authority exactly once per global index; assemble q2 sums only after exact 0..47 coverage'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid: raise SystemExit(2)
