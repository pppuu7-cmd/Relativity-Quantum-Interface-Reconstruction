#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 397.

Prospectively frozen next-level angular-resolution gate for the sole unresolved
physical Tr U1^2 double-double channel (global index 4, q^2=-1).

Iteration 395 is preserved as BLOCKED_CONVERGENCE because its new 8x16 base
value differs from the older 6x12 high value by 2.792425135668121e-05 > the
unchanged 2e-5 threshold, even though its 8x16 internal phi-shift and h/2
checks pass.

This is a new version, not a post-hoc relaxation. Physics arithmetic and every
threshold remain frozen. Only angular resolution advances prospectively from
8x16 to 10x20. Convergence is tested against the preserved 8x16 base, a 10x20
half-phi shift, and a 10x20 h/2 derivative evaluation. The old 6x12 datum is
retained as provenance/diagnostic but is not reused as the adjacent-grid
criterion for this new resolution level.
"""
from __future__ import annotations
import contextlib, io, json, math, multiprocessing as mp, time
from pathlib import Path
import numpy as np

ITERATION=397
TARGET_INDEX=4
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parent.parent
p395=json.loads((REPO/'candidate_gravity/results/iteration395_tru1sq_double_double_channel4_stronger_angular_raw.json').read_text())
if not (p395.get('iteration')==395 and p395.get('channel_index')==4 and p395.get('status')=='BLOCKED_CONVERGENCE'):
    raise RuntimeError('iteration395_blocked_authority_drift')
PREV_BASE=complex(*p395['new_8x16']['mixed_derivative_base'])
PREV_SHIFT=complex(*p395['new_8x16']['mixed_derivative_phi_shifted'])
PREV_HALF=complex(*p395['new_8x16']['mixed_derivative_halfstep'])
OLD6=float(p395['old_6x12_mixed_derivative_high'])
SOURCE_RAW_SHA='605d121616c36eb144b657d45de7be8a4dfd0d167402ec06eb48308daa8e5634'

PARENT=ROOT/'iteration395_tru1sq_double_double_channel4_stronger_angular.py'
src=PARENT.read_text()
# Import only the frozen Iteration-395 definitions.  The earlier implementation
# searched for the shorter token ``start=time.perf_counter()`` and therefore
# also matched Iteration-395's own marker string.  Anchor the actual execution
# statement instead; this is an implementation repair only, not a gate change.
run_anchor='\nstart=time.perf_counter(); ctx=mp.get_context(\'fork\')'
if src.count(run_anchor)!=1: raise RuntimeError('iteration395_run_anchor_drift')
ns={'__name__':'iteration397_parent395_prefix','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split(run_anchor,1)[0],str(PARENT),'exec'),ns,ns)

point_task=ns['point_task']; sphere_parallel=ns['sphere_parallel']
# The frozen helper was defined by exec in a synthetic namespace. Linux fork
# preserves its globals, but multiprocessing pickles the callable by
# module/name. Publish only that callable in __main__ so workers can resolve it.
# This changes execution plumbing only; no scientific arithmetic/gate changes.
point_task.__module__='__main__'
point_task.__qualname__='point_task'
globals()['point_task']=point_task
BASE_H=ns['BASE_H']; HALF_H=ns['HALF_H']; TOL=ns['TOL']; SHELL_TOL=ns['SHELL_TOL']
UNCUT_MIN_TOL=ns['UNCUT_MIN_TOL']; RADIAL_TOL=ns['RADIAL_TOL']; ORACLE_TOL=ns['ORACLE_TOL']
WORKERS=min(4,max(1,mp.cpu_count() or 1))

start=time.perf_counter(); ctx=mp.get_context('fork')
with ctx.Pool(processes=WORKERS) as pool:
    zs,_=np.polynomial.legendre.leggauss(10)
    oracle_tasks=[(0,float(zs[0]),0,20,BASE_H,0.0),(9,float(zs[-1]),19,20,BASE_H,0.0)]
    serial=[point_task(x) for x in oracle_tasks]; parallel=pool.map(point_task,oracle_tasks,chunksize=1)
    oracle_err=0.0
    for aa,bb in zip(serial,parallel):
        if aa[:2]!=bb[:2]: raise RuntimeError('oracle_index_drift')
        for x,y in zip(aa[2:],bb[2:]):
            oracle_err=max(oracle_err,float(abs(x-y)/max(1.0,abs(x),abs(y))))
    if oracle_err>ORACLE_TOL: raise RuntimeError(('serial_parallel_oracle_failed',oracle_err))
    base,es1,un1,re1,la1=sphere_parallel(10,20,BASE_H,0.0,pool)
    shifted,es2,un2,re2,la2=sphere_parallel(10,20,BASE_H,0.5,pool)
    halfstep,es3,un3,re3,la3=sphere_parallel(10,20,HALF_H,0.0,pool)
runtime=time.perf_counter()-start

scale=max(1.0,abs(PREV_BASE),abs(base),abs(shifted),abs(halfstep))
components={
 'new_10x20_base_vs_prev_8x16_base':float(abs(base-PREV_BASE)/scale),
 'new_10x20_base_vs_new_shifted':float(abs(base-shifted)/scale),
 'new_10x20_base_vs_new_halfstep':float(abs(base-halfstep)/scale),
}
conv=max(components.values()); shell=max(es1,es2,es3); umin=min(un1,un2,un3); radial=max(re1,re2,re3); minlam=min(la1,la2,la3)
uncut_ok=bool(np.isinf(umin) or (np.isfinite(umin) and umin>UNCUT_MIN_TOL))
execution_valid=bool(np.isfinite(conv) and shell<=SHELL_TOL and radial<=RADIAL_TOL and uncut_ok and minlam>0 and oracle_err<=ORACLE_TOL)
status='CONVERGED' if execution_valid and conv<=TOL else ('BLOCKED_CONVERGENCE' if execution_valid else 'FAIL_EXECUTION')
ds=-base
out={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
 'classification':('PASS_TRU1SQ_DOUBLE_DOUBLE_CHANNEL4_NEXT_ANGULAR_LEVEL__CONVERGED' if status=='CONVERGED' else
                   'PASS_TRU1SQ_DOUBLE_DOUBLE_CHANNEL4_NEXT_ANGULAR_LEVEL__STILL_BLOCKED' if execution_valid else
                   'FAIL_TRU1SQ_DOUBLE_DOUBLE_CHANNEL4_NEXT_ANGULAR_LEVEL_EXECUTION'),
 'channel_index':TARGET_INDEX,'source_iteration':395,'source_raw_sha256':SOURCE_RAW_SHA,'q_squared':-1.0,'class_id':5,'status':status,
 'D_s_TrU1sq_double_double_channel':[float(ds.real),float(ds.imag)] if status=='CONVERGED' else None,
 'diagnostic_candidate_value_not_authority_if_blocked':[float(ds.real),float(ds.imag)],
 'provenance_angular_sequence':{
   'old_6x12_mixed_derivative_high':OLD6,
   'iteration395_8x16_base':[float(PREV_BASE.real),float(PREV_BASE.imag)],
   'iteration395_8x16_phi_shifted':[float(PREV_SHIFT.real),float(PREV_SHIFT.imag)],
   'iteration395_8x16_halfstep':[float(PREV_HALF.real),float(PREV_HALF.imag)]},
 'new_10x20':{'mixed_derivative_base':[float(base.real),float(base.imag)],
              'mixed_derivative_phi_shifted':[float(shifted.real),float(shifted.imag)],
              'mixed_derivative_halfstep':[float(halfstep.real),float(halfstep.imag)]},
 'scaled_convergence_components':components,'scaled_convergence_error':conv,'frozen_threshold':TOL,
 'max_radial_richardson_scaled_error':radial,'max_cut_shell_abs_error':shell,
 'minimum_sampled_uncut_abs_denominator':umin,'minimum_kallen':minlam,
 'serial_parallel_oracle':{'scaled_max_error':oracle_err,'threshold':ORACLE_TOL},'runtime_seconds':float(runtime),
 'physics_immutability':{'derivative_h':BASE_H,'derivative_halfstep_h':HALF_H,
                         'radial_rule':'unchanged Iteration379/385/389/395',
                         'normalization':'D_s_double_double=-sphere_mean[d_mu1 d_mu2(beta*num/D_uncut)]',
                         'only_change':'prospective angular quadrature level 8x16 -> 10x20; threshold unchanged'},
 'interpretation':('If CONVERGED this resolves only channel 4 and may replace its Iteration389 BLOCKED record in the exact-15 assembly. '
                   'If BLOCKED_CONVERGENCE, no further blind grid escalation is authorized; move to analytic/spectral angular reduction.'),
 'guardrails':['NEW_VERSION_NOT_POSTHOC_GATE_EDIT','NO_THRESHOLD_WEAKENING','ONLY_BLOCKED_CHANNEL4_RERUN','ADJACENT_GRID_8x16_TO_10x20',
               'NO_ZERO_FILL','NO_EFFECTIVE_ACTION_WEIGHT_FOLDING','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('if CONVERGED, exact-15 double-double assembly after remaining Iteration389 records resolve; '
              'if still BLOCKED, analytic/spectral angular reduction for channel4 only')
}
print(json.dumps(out,indent=2,sort_keys=True))
if not execution_valid: raise SystemExit(2)
