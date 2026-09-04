#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 390.

Topology-aware recovery for only the Iteration-384 chunks that failed/cancelled
before raw authority.  The physical channel_derivative arithmetic is imported
verbatim from Iteration 364/384.  The sole classification repair is that
minimum_sampled_uncut_abs_denominator=+Infinity is accepted when the cut
exhausts all denominator groups: there is then no uncut propagator to approach a
pole.  Finite umin values still must exceed the unchanged 1e-10 threshold.

Environment START_INDEX/END_INDEX selects one prospectively frozen two-channel
chunk.  No grid, derivative step, sign, numerator, routing or threshold changes.
"""
from __future__ import annotations
import contextlib, io, json, os, time
from collections import defaultdict
from pathlib import Path
import numpy as np

ITERATION=390
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration364_u2_repeated_pole_symmetric_aux_derivative_cut.py'
src=PARENT.read_text(); marker='records=[]; by_bucket=defaultdict(list)'
if src.count(marker)!=1: raise RuntimeError('iteration364_loop_marker_drift')
ns={'__name__':'iteration390_parent364_prefix','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split(marker,1)[0],str(PARENT),'exec'),ns,ns)
P359=ns['P359']; channel_derivative=ns['channel_derivative']
CONVERGENCE_TOL=ns['CONVERGENCE_TOL']; SHELL_TOL=ns['SHELL_TOL']; BASE_H=ns['BASE_H']; HALF_H=ns['HALF_H']
all_channels=[]
for fam in P359['result']['families']:
    for ch in fam['timelike_distinct_group_channels']:
        if ch['repeated_pole_reduction_required']: all_channels.append((fam,ch))
if len(all_channels)!=48: raise RuntimeError(('channel_census_drift',len(all_channels)))
start_i=int(os.environ['START_INDEX']); end_i=int(os.environ['END_INDEX'])
if not (0<=start_i<48 and end_i==start_i+2 and end_i<=48 and start_i%2==0):
    raise RuntimeError(('invalid_chunk',start_i,end_i))
allowed={(4,6),(14,16),(16,18),(22,24),(28,30),(30,32)}
if (start_i,end_i) not in allowed:
    raise RuntimeError(('not_a_prospectively_frozen_recovery_chunk',start_i,end_i))
records=[]; bucket_sums=defaultdict(complex); execution_valid=True; t0=time.perf_counter()
for global_index in range(start_i,end_i):
    fam,ch=all_channels[global_index]; c0=time.perf_counter()
    low,es1,mu1,s,sgn,rg,og=channel_derivative(fam,ch,6,12,BASE_H,0.0)
    high,es2,mu2,_,_,_,_=channel_derivative(fam,ch,8,16,BASE_H,0.0)
    shifted,es3,mu3,_,_,_,_=channel_derivative(fam,ch,8,16,BASE_H,0.5)
    halfstep,es4,mu4,_,_,_,_=channel_derivative(fam,ch,8,16,HALF_H,0.0)
    runtime=time.perf_counter()-c0
    scale=max(1.0,abs(low),abs(high),abs(shifted),abs(halfstep))
    conv=float(max(abs(high-low),abs(high-shifted),abs(high-halfstep))/scale)
    shell=float(max(es1,es2,es3,es4)); umin=float(min(mu1,mu2,mu3,mu4))
    numeric_finite=bool(np.isfinite(conv) and np.isfinite(shell))
    uncut_ok=bool(np.isinf(umin) or (np.isfinite(umin) and umin>1e-10))
    structural=bool(numeric_finite and shell<=SHELL_TOL and uncut_ok)
    execution_valid = execution_valid and structural
    status='CONVERGED' if structural and conv<=CONVERGENCE_TOL else ('BLOCKED_CONVERGENCE' if structural else 'FAIL_EXECUTION')
    q2=float(ch['q2'])
    if status=='CONVERGED': bucket_sums[q2]+=high
    records.append({'global_channel_index':global_index,'route':int(fam['route']),'subterm':int(fam['subterm']),
      'group_pair':list(map(int,ch['group_pair'])),'repeated_group':int(rg),'other_cut_group':int(og),'q2':q2,'status':status,
      'cut_algebraic_sign':float(sgn),'D_s_TrU2_repeated_high':[float(high.real),float(high.imag)],
      'D_s_TrU2_repeated_low':[float(low.real),float(low.imag)],
      'D_s_TrU2_repeated_high_phi_shifted':[float(shifted.real),float(shifted.imag)],
      'D_s_TrU2_repeated_halfstep':[float(halfstep.real),float(halfstep.imag)],
      'scaled_convergence_error':conv,'max_cut_shell_abs_error':shell,
      'minimum_sampled_uncut_abs_denominator':umin,'uncut_topology_status':('NO_UNCUT_DENOMINATOR' if np.isinf(umin) else 'FINITE_UNCUT_DENOMINATOR'),
      'runtime_seconds':float(runtime)})
result={'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
 'classification':('PASS_U2_REPEATED_CUT_TOPOLOGY_AWARE_RECOVERY_CHUNK_EXECUTION' if execution_valid else 'FAIL_U2_REPEATED_CUT_TOPOLOGY_AWARE_RECOVERY_CHUNK_EXECUTION'),
 'source_scientific_iteration':384,'classification_repair':'ALLOW_POSITIVE_INFINITY_UMIN_IFF_NO_UNCUT_DENOMINATOR_EXISTS',
 'chunk':{'start_index':start_i,'end_index_exclusive':end_i,'expected_indices':list(range(start_i,end_i))},'records':records,
 'converged_count':sum(r['status']=='CONVERGED' for r in records),'blocked_convergence_count':sum(r['status']=='BLOCKED_CONVERGENCE' for r in records),
 'runtime_seconds':float(time.perf_counter()-t0),'partial_q2_sums_of_converged_channels_only':{str(q):[float(z.real),float(z.imag)] for q,z in sorted(bucket_sums.items())},
 'frozen_arithmetic':{'parent':'Iteration364 channel_derivative verbatim','base_h':BASE_H,'halfstep_h':HALF_H,'low_grid':[6,12],'high_grid':[8,16],
  'phi_shift_check':0.5,'convergence_threshold':CONVERGENCE_TOL,'shell_threshold':SHELL_TOL,
  'finite_uncut_threshold':1e-10,'normalization':'D_s_repeated=sphere_mean[d_mu2(beta*cut_sign*num/D_uncut)]'},
 'guardrails':['ONLY_CLASSIFICATION_WRAPPER_CHANGED','NO_PHYSICS_ARITHMETIC_CHANGE','NO_THRESHOLD_WEAKENING','NO_ZERO_FILL','EXACT_48_INDEX_ASSEMBLY_REQUIRED',
  'DISTINCT_Q2_BUCKETS_NEVER_SUMMED','NO_EFFECTIVE_ACTION_WEIGHT_FOLDING','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'merge only raw-valid recovered records with unique original/recovery channel indices; complete q2 sums only after all 48 channels are resolved'}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid: raise SystemExit(2)
