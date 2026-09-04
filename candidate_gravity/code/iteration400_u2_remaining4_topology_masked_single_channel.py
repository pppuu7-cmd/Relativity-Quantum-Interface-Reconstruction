#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 400.

Targeted recovery of the only four still-unresolved Iteration-384 repeated-cut
Tr U2 global indices: 14,15,16,17. One channel per job. Physical arithmetic is
Iteration-364 channel_derivative verbatim; only resource partition is changed.
Iteration-392 topology mask is binding. No grid, h, numerator, routing, sign,
normalization, or threshold is changed.
"""
from __future__ import annotations
import contextlib, io, json, os, time
from pathlib import Path
import numpy as np

ITERATION=400
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration364_u2_repeated_pole_symmetric_aux_derivative_cut.py'
src=PARENT.read_text(); marker='records=[]; by_bucket=defaultdict(list)'
if src.count(marker)!=1: raise RuntimeError('iteration364_loop_marker_drift')
ns={'__name__':'iteration400_parent364_prefix','__file__':str(PARENT)}
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
FROZEN_NO_UNCUT={4,13,22,27,28,29,30,33,36,39,42,45}
derived={i for i,(_,_,_,uncut) in enumerate(all_channels) if len(uncut)==0}
if derived!=FROZEN_NO_UNCUT: raise RuntimeError(('iteration392_topology_mask_drift',sorted(derived)))

i=int(os.environ['CHANNEL_INDEX'])
if i not in {14,15,16,17}: raise RuntimeError(('not_iteration400_remaining_index',i))
fam,ch,group_count,uncut_groups=all_channels[i]; t0=time.perf_counter()
low,es1,mu1,s,sgn,rg,og=channel_derivative(fam,ch,6,12,BASE_H,0.0)
high,es2,mu2,_,_,_,_=channel_derivative(fam,ch,8,16,BASE_H,0.0)
shifted,es3,mu3,_,_,_,_=channel_derivative(fam,ch,8,16,BASE_H,0.5)
halfstep,es4,mu4,_,_,_,_=channel_derivative(fam,ch,8,16,HALF_H,0.0)
runtime=time.perf_counter()-t0
scale=max(1.0,abs(low),abs(high),abs(shifted),abs(halfstep))
conv=float(max(abs(high-low),abs(high-shifted),abs(high-halfstep))/scale)
shell=float(max(es1,es2,es3,es4)); umin=float(min(mu1,mu2,mu3,mu4))
numeric_finite=bool(np.isfinite(conv) and np.isfinite(shell))
topology_no_uncut=(i in FROZEN_NO_UNCUT)
topology_consistent=bool(topology_no_uncut==(len(uncut_groups)==0))
uncut_ok=bool((topology_no_uncut and np.isinf(umin)) or ((not topology_no_uncut) and np.isfinite(umin) and umin>1e-10))
structural=bool(numeric_finite and shell<=SHELL_TOL and topology_consistent and uncut_ok)
status='CONVERGED' if structural and conv<=CONVERGENCE_TOL else ('BLOCKED_CONVERGENCE' if structural else 'FAIL_EXECUTION')
record={
 'global_channel_index':i,'route':int(fam['route']),'subterm':int(fam['subterm']),
 'group_pair':list(map(int,ch['group_pair'])),'repeated_group':int(rg),'other_cut_group':int(og),'q2':float(ch['q2']),'status':status,
 'cut_algebraic_sign':float(sgn),'D_s_TrU2_repeated_high':[float(high.real),float(high.imag)],
 'D_s_TrU2_repeated_low':[float(low.real),float(low.imag)],
 'D_s_TrU2_repeated_high_phi_shifted':[float(shifted.real),float(shifted.imag)],
 'D_s_TrU2_repeated_halfstep':[float(halfstep.real),float(halfstep.imag)],
 'scaled_convergence_error':conv,'max_cut_shell_abs_error':shell,'minimum_sampled_uncut_abs_denominator':umin,
 'denominator_group_count':int(group_count),'uncut_group_indices':list(map(int,uncut_groups)),
 'topology_no_uncut_denominator':topology_no_uncut,'iteration392_mask_consistent':topology_consistent,
 'uncut_policy_pass':uncut_ok,'runtime_seconds':float(runtime)}
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':structural,'candidate_residual':False,
 'classification':('PASS_U2_REMAINING4_SINGLE_CHANNEL_EXECUTION' if structural else 'FAIL_U2_REMAINING4_SINGLE_CHANNEL_EXECUTION'),
 'source_scientific_iteration':384,'topology_authority_iteration':392,'channel_index':i,'record':record,
 'frozen_arithmetic':{'parent':'Iteration364 channel_derivative verbatim','base_h':BASE_H,'halfstep_h':HALF_H,
  'low_grid':[6,12],'high_grid':[8,16],'phi_shift_check':0.5,'convergence_threshold':CONVERGENCE_TOL,
  'shell_threshold':SHELL_TOL,'finite_uncut_threshold':1e-10,
  'normalization':'D_s_repeated=sphere_mean[d_mu2(beta*cut_sign*num/D_uncut)]'},
 'guardrails':['ITERATION392_TOPOLOGY_MASK_BINDING','NO_PHYSICS_ARITHMETIC_CHANGE','NO_THRESHOLD_WEAKENING','NO_ZERO_FILL',
  'EXACT_48_INDEX_ASSEMBLY_REQUIRED','DISTINCT_Q2_BUCKETS_NEVER_SUMMED','NO_EFFECTIVE_ACTION_WEIGHT_FOLDING',
  'NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'after 14,15,16,17 raw authority exists, merge with 384/390/391/394 exactly once per index and run exact 0..47 U2 assembly'}
print(json.dumps(result,indent=2,sort_keys=True))
if not structural: raise SystemExit(2)
