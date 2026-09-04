#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 395.

Targeted recovery for the sole currently observed Iteration-389 double-double
BLOCKED_CONVERGENCE channel (global double-double index 4). No other channel is
rerun. The Iteration-389/385 physical arithmetic is unchanged: same mixed
auxiliary-mass derivative, h and h/2, radial Richardson rule, signs,
normalization and thresholds.

Only angular resolution is strengthened from the frozen old high 6x12 result to
an 8x16 grid. We compute 8x16 at base h, half-phi shift, and halfstep h/2. The
new base result must agree within the unchanged 2e-5 scaled threshold with:
  (a) the raw-valid old 6x12 high value,
  (b) the new 8x16 half-phi-shift value,
  (c) the new 8x16 h/2 value.
Otherwise the channel remains BLOCKED_CONVERGENCE.
"""
from __future__ import annotations
import contextlib, io, json, math, multiprocessing as mp, time
from pathlib import Path
import numpy as np

ITERATION=395
TARGET_INDEX=4
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parent.parent
blocked=json.loads((REPO/'candidate_gravity/results/iteration389_double_double_channel4_blocked_convergence.json').read_text())
if not (blocked.get('iteration')==389 and blocked.get('channel_index')==TARGET_INDEX and blocked.get('status')=='BLOCKED_CONVERGENCE'):
    raise RuntimeError('iteration389_channel4_blocked_authority_drift')
OLD_HIGH=float(blocked['mixed_derivative_high'])
OLD_RAW_SHA=blocked['actions']['raw_result_sha256']

PARENT=ROOT/'iteration379_tru1sq_double_double_one_channel_pilot.py'
src=PARENT.read_text(); marker='start=time.perf_counter()'
if src.count(marker)!=1: raise RuntimeError('iteration379_run_marker_drift')
ns={'__name__':'iteration395_parent379_prefix','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split(marker,1)[0],str(PARENT),'exec'),ns,ns)

dd=[c for c in ns['P372']['channels'] if c['singularity_type']=='double-double']
if len(dd)!=15: raise RuntimeError(('double_double_census_drift',len(dd)))
ch=dd[TARGET_INDEX]
row=ns['rows'][int(ch['class_id'])]
a=np.asarray(ch['shift_i'],float); b=np.asarray(ch['shift_j'],float); q=b-a
mi=int(ch['multiplicity_i']); mj=int(ch['multiplicity_j'])
if (mi,mj)!=(2,2): raise RuntimeError('target_not_double_double')
q2=float(np.real(ns['mdot'](q))); s=-q2; basis=ns['transverse_basis'](q)
for name,val in {'ch':ch,'row':row,'a':a,'b':b,'q':q,'mi':mi,'mj':mj,'q2':q2,'s':s,'basis':basis}.items(): ns[name]=val

mixed_derivative_at_unit=ns['mixed_derivative_at_unit']
BASE_H=ns['BASE_H']; HALF_H=ns['HALF_H']; TOL=ns['ANGULAR_CONVERGENCE_TOL']
SHELL_TOL=ns['CUT_SHELL_TOL']; UNCUT_MIN_TOL=ns['UNCUT_MIN_TOL']; RADIAL_TOL=ns['RADIAL_EXTRAP_TOL']
WORKERS=min(4,max(1,mp.cpu_count() or 1)); ORACLE_TOL=2e-13


def point_task(args):
    zi,z,m,nphi,h,phi_shift=args
    rr=math.sqrt(max(0.0,1.0-float(z)*float(z)))
    phi=2.0*math.pi*(m+phi_shift)/nphi
    n=np.array([rr*math.cos(phi),rr*math.sin(phi),float(z)])
    unit=n[0]*basis[0]+n[1]*basis[1]+n[2]*basis[2]
    d2,sh,un,ra,la=mixed_derivative_at_unit(unit,h)
    return zi,m,d2,sh,un,ra,la


def sphere_parallel(nz,nphi,h,phi_shift,pool):
    zs,ws=np.polynomial.legendre.leggauss(nz)
    tasks=[(zi,float(z),m,nphi,h,phi_shift) for zi,z in enumerate(zs) for m in range(nphi)]
    vals=pool.map(point_task,tasks,chunksize=1)
    total=0j; max_shell=0.0; min_uncut=float('inf'); max_radial=0.0; min_lam=float('inf'); p=0
    for zi,wz in enumerate(ws):
        row_sum=0j
        for m in range(nphi):
            rzi,rm,d2,sh,un,ra,la=vals[p]; p+=1
            if (rzi,rm)!=(zi,m): raise RuntimeError('ordered_pool_result_drift')
            row_sum+=d2; max_shell=max(max_shell,sh); min_uncut=min(min_uncut,un)
            max_radial=max(max_radial,ra); min_lam=min(min_lam,la)
        total+=float(wz)*(row_sum/nphi)
    return 0.5*total,max_shell,min_uncut,max_radial,min_lam

start=time.perf_counter(); ctx=mp.get_context('fork')
with ctx.Pool(processes=WORKERS) as pool:
    # Fixed new-grid oracle points.
    zs,_=np.polynomial.legendre.leggauss(8)
    oracle_tasks=[(0,float(zs[0]),0,16,BASE_H,0.0),(7,float(zs[-1]),15,16,BASE_H,0.0)]
    serial=[point_task(x) for x in oracle_tasks]; parallel=pool.map(point_task,oracle_tasks,chunksize=1)
    oracle_err=0.0
    for aa,bb in zip(serial,parallel):
        if aa[:2]!=bb[:2]: raise RuntimeError('oracle_index_drift')
        for x,y in zip(aa[2:],bb[2:]):
            oracle_err=max(oracle_err,float(abs(x-y)/max(1.0,abs(x),abs(y))))
    if oracle_err>ORACLE_TOL: raise RuntimeError(('serial_parallel_oracle_failed',oracle_err))
    base,es1,un1,re1,la1=sphere_parallel(8,16,BASE_H,0.0,pool)
    shifted,es2,un2,re2,la2=sphere_parallel(8,16,BASE_H,0.5,pool)
    halfstep,es3,un3,re3,la3=sphere_parallel(8,16,HALF_H,0.0,pool)
runtime=time.perf_counter()-start

old=complex(OLD_HIGH,0.0)
scale=max(1.0,abs(old),abs(base),abs(shifted),abs(halfstep))
components={
 'new_base_vs_old_6x12_high':float(abs(base-old)/scale),
 'new_base_vs_new_shifted':float(abs(base-shifted)/scale),
 'new_base_vs_new_halfstep':float(abs(base-halfstep)/scale),
}
conv=max(components.values()); shell=max(es1,es2,es3); umin=min(un1,un2,un3); radial=max(re1,re2,re3); minlam=min(la1,la2,la3)
uncut_ok=bool(np.isinf(umin) or (np.isfinite(umin) and umin>UNCUT_MIN_TOL))
execution_valid=bool(np.isfinite(conv) and shell<=SHELL_TOL and radial<=RADIAL_TOL and uncut_ok and minlam>0 and oracle_err<=ORACLE_TOL)
status='CONVERGED' if execution_valid and conv<=TOL else ('BLOCKED_CONVERGENCE' if execution_valid else 'FAIL_EXECUTION')
ds=-base
out={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
 'classification':('PASS_TRU1SQ_DOUBLE_DOUBLE_CHANNEL4_STRONGER_ANGULAR__CONVERGED' if status=='CONVERGED' else
                   'PASS_TRU1SQ_DOUBLE_DOUBLE_CHANNEL4_STRONGER_ANGULAR__STILL_BLOCKED' if execution_valid else
                   'FAIL_TRU1SQ_DOUBLE_DOUBLE_CHANNEL4_STRONGER_ANGULAR_EXECUTION'),
 'channel_index':TARGET_INDEX,'source_iteration':389,'source_raw_sha256':OLD_RAW_SHA,'q_squared':q2,'class_id':int(ch['class_id']),'status':status,
 'D_s_TrU1sq_double_double_channel':[float(ds.real),float(ds.imag)] if status=='CONVERGED' else None,
 'diagnostic_candidate_value_not_authority_if_blocked':[float(ds.real),float(ds.imag)],
 'old_6x12_mixed_derivative_high':OLD_HIGH,
 'new_8x16':{'mixed_derivative_base':[float(base.real),float(base.imag)],
             'mixed_derivative_phi_shifted':[float(shifted.real),float(shifted.imag)],
             'mixed_derivative_halfstep':[float(halfstep.real),float(halfstep.imag)]},
 'scaled_convergence_components':components,'scaled_convergence_error':conv,'frozen_threshold':TOL,
 'max_radial_richardson_scaled_error':radial,'max_cut_shell_abs_error':shell,
 'minimum_sampled_uncut_abs_denominator':umin,'minimum_kallen':minlam,
 'serial_parallel_oracle':{'scaled_max_error':oracle_err,'threshold':ORACLE_TOL},'runtime_seconds':float(runtime),
 'physics_immutability':{'derivative_h':BASE_H,'derivative_halfstep_h':HALF_H,'radial_rule':'unchanged Iteration379/385/389',
                         'normalization':'D_s_double_double=-sphere_mean[d_mu1 d_mu2(beta*num/D_uncut)]',
                         'only_change':'angular quadrature strengthened from old 6x12 high to new 8x16'},
 'guardrails':['NO_THRESHOLD_WEAKENING','ONLY_BLOCKED_CHANNEL4_RERUN','OLD_RAW_HIGH_INCLUDED_IN_CONVERGENCE_TEST','NO_ZERO_FILL',
               'NO_EFFECTIVE_ACTION_WEIGHT_FOLDING','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('if CONVERGED, replace only channel4 BLOCKED entry in the eventual 15-channel assembly with this authority; if still BLOCKED, move only channel4 to stronger/analytic angular reduction')
}
print(json.dumps(out,indent=2,sort_keys=True))
if not execution_valid: raise SystemExit(2)
