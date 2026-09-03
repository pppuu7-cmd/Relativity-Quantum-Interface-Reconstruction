#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 382.

One prospectively selected physical U2 cut-through-double-pole channel pilot.
Purpose: recover the cancelled Iteration-364/376 computation by validating one
complete channel with the exact frozen Iteration-364 arithmetic and measuring
runtime before prospectively choosing a smaller full-48 resource architecture.

No physics arithmetic changes: channel_derivative, auxiliary-mass nodes,
quadratures, routing, numerator, normalization, thresholds and q2 convention are
inherited verbatim from Iteration 364.  The selected channel is the first of the
48 channels in the frozen Iteration-359/364 ordering.  No effective-action +i/2
weight is folded in.
"""
from __future__ import annotations
import contextlib, io, json, time
from pathlib import Path
import numpy as np

ITERATION=382
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration364_u2_repeated_pole_symmetric_aux_derivative_cut.py'
src=PARENT.read_text()
marker='records=[]; by_bucket=defaultdict(list)'
if src.count(marker)!=1:
    raise RuntimeError('iteration364_loop_marker_drift')
prefix=src.split(marker,1)[0]
ns={'__name__':'iteration382_parent364_prefix','__file__':str(PARENT)}
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

GLOBAL_INDEX=0
fam,ch=all_channels[GLOBAL_INDEX]
start=time.perf_counter()
low,es1,mu1,s,sgn,rg,og=channel_derivative(fam,ch,6,12,BASE_H,0.0)
high,es2,mu2,_,_,_,_=channel_derivative(fam,ch,8,16,BASE_H,0.0)
shifted,es3,mu3,_,_,_,_=channel_derivative(fam,ch,8,16,BASE_H,0.5)
halfstep,es4,mu4,_,_,_,_=channel_derivative(fam,ch,8,16,HALF_H,0.0)
runtime=time.perf_counter()-start
scale=max(1.0,abs(low),abs(high),abs(shifted),abs(halfstep))
conv=float(max(abs(high-low),abs(high-shifted),abs(high-halfstep))/scale)
shell=float(max(es1,es2,es3,es4)); umin=float(min(mu1,mu2,mu3,mu4))
status='CONVERGED' if conv<=CONVERGENCE_TOL and shell<=SHELL_TOL else 'BLOCKED_CONVERGENCE'
execution_valid=bool(np.isfinite(conv) and np.isfinite(shell) and np.isfinite(umin) and shell<=SHELL_TOL and umin>1e-10)
q2=float(ch['q2'])
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
 'classification':('PASS_U2_REPEATED_CUT_ONE_CHANNEL_PILOT__CONVERGED' if status=='CONVERGED' else
                   'PASS_U2_REPEATED_CUT_ONE_CHANNEL_PILOT__BLOCKED_CONVERGENCE' if execution_valid else
                   'FAIL_U2_REPEATED_CUT_ONE_CHANNEL_PILOT_EXECUTION'),
 'selected_channel_rule':'FIRST_CUT_THROUGH_DOUBLE_POLE_CHANNEL_IN_ITERATION359_364_FROZEN_ORDER',
 'channel':{'global_channel_index':GLOBAL_INDEX,'route':int(fam['route']),'subterm':int(fam['subterm']),
            'group_pair':list(map(int,ch['group_pair'])),'repeated_group':int(rg),'other_cut_group':int(og),
            'q2':q2,'status':status,'cut_algebraic_sign':float(sgn),
            'D_s_TrU2_repeated_high':[float(high.real),float(high.imag)],
            'D_s_TrU2_repeated_low':[float(low.real),float(low.imag)],
            'D_s_TrU2_repeated_high_phi_shifted':[float(shifted.real),float(shifted.imag)],
            'D_s_TrU2_repeated_halfstep':[float(halfstep.real),float(halfstep.imag)],
            'scaled_convergence_error':conv,'max_cut_shell_abs_error':shell,
            'minimum_sampled_uncut_abs_denominator':umin},
 'runtime_seconds':float(runtime),
 'frozen_arithmetic':{'parent':'Iteration364 channel_derivative verbatim','base_h':BASE_H,'halfstep_h':HALF_H,
                      'low_grid':[6,12],'high_grid':[8,16],'phi_shift_check':0.5,
                      'convergence_threshold':CONVERGENCE_TOL,'shell_threshold':SHELL_TOL,
                      'normalization':'D_s_repeated=sphere_mean[d_mu2(beta*cut_sign*num/D_uncut)]'},
 'scope':'ONE_PRESELECTED_U2_CUT_THROUGH_DOUBLE_POLE_CHANNEL_ONLY__PIPELINE_RUNTIME_AND_PHYSICAL_VALUE',
 'guardrails':['ITERATION359_362_363_BINDING','ITERATION364_CHANNEL_DERIVATIVE_VERBATIM','NO_THRESHOLD_WEAKENING',
               'NO_48_CHANNEL_EXTRAPOLATION_FROM_ONE_CHANNEL','DISTINCT_Q2_BUCKETS_NEVER_SUMMED',
               'NO_EFFECTIVE_ACTION_WEIGHT_FOLDING','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('if CONVERGED, use measured runtime only to prospectively freeze a smaller complete-48 chunk architecture with identical arithmetic; if BLOCKED, isolate this channel with analytic/stronger-angular treatment without weakening thresholds')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid:
    raise SystemExit(2)
