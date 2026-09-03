#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 385.

Resource-only repair of operationally cancelled Iteration 379.  The complete
one-channel double-double physics arithmetic is imported from Iteration 379
verbatim through the pre-run prefix.  Only independent angular points are
executed in parallel with an ordered fork pool; aggregation order is kept equal
to the serial z-then-phi loop.

A prospectively fixed two-point serial-vs-parallel oracle must agree before the
full pilot is accepted.  No grid, mass stencil, radial Richardson rule, sign,
threshold, numerator, routing, or effective-action weight is changed.
"""
from __future__ import annotations
import contextlib, io, json, math, multiprocessing as mp, os, time
from pathlib import Path
import numpy as np

ITERATION=385
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration379_tru1sq_double_double_one_channel_pilot.py'
src=PARENT.read_text()
marker='start=time.perf_counter()'
if src.count(marker)!=1:
    raise RuntimeError('iteration379_run_marker_drift')
prefix=src.split(marker,1)[0]
ns={'__name__':'iteration385_parent379_prefix','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix,str(PARENT),'exec'),ns,ns)

mixed_derivative_at_unit=ns['mixed_derivative_at_unit']
basis=ns['basis']; BASE_H=ns['BASE_H']; HALF_H=ns['HALF_H']
ANGULAR_CONVERGENCE_TOL=ns['ANGULAR_CONVERGENCE_TOL']; CUT_SHELL_TOL=ns['CUT_SHELL_TOL']
UNCUT_MIN_TOL=ns['UNCUT_MIN_TOL']; RADIAL_EXTRAP_TOL=ns['RADIAL_EXTRAP_TOL']
PROBE_MAX=ns['PROBE_MAX']; ch=ns['ch']; mi=ns['mi']; mj=ns['mj']

WORKERS=min(4,max(1,os.cpu_count() or 1))
ORACLE_TOL=2e-13


def point_task(args):
    zi,z,wz,m,nphi,h,phi_shift=args
    rr=math.sqrt(max(0.0,1.0-float(z)*float(z)))
    phi=2.0*math.pi*(m+phi_shift)/nphi
    n=np.array([rr*math.cos(phi),rr*math.sin(phi),float(z)])
    unit=n[0]*basis[0]+n[1]*basis[1]+n[2]*basis[2]
    d2,sh,un,ra,la=mixed_derivative_at_unit(unit,h)
    return zi,m,d2,sh,un,ra,la


def sphere_parallel(nz,nphi,h,phi_shift,pool):
    zs,ws=np.polynomial.legendre.leggauss(nz)
    tasks=[]
    for zi,(z,wz) in enumerate(zip(zs,ws)):
        for m in range(nphi):
            tasks.append((zi,float(z),float(wz),m,nphi,h,phi_shift))
    vals=pool.map(point_task,tasks,chunksize=1)
    total=0j; max_shell=0.0; min_uncut=float('inf'); max_radial=0.0; min_lam=float('inf')
    p=0
    for zi,(z,wz) in enumerate(zip(zs,ws)):
        row_sum=0j
        for m in range(nphi):
            rzi,rm,d2,sh,un,ra,la=vals[p]; p+=1
            if rzi!=zi or rm!=m: raise RuntimeError('ordered_pool_result_drift')
            row_sum += d2
            max_shell=max(max_shell,sh); min_uncut=min(min_uncut,un)
            max_radial=max(max_radial,ra); min_lam=min(min_lam,la)
        total += float(wz)*(row_sum/nphi)
    return 0.5*total,max_shell,min_uncut,max_radial,min_lam

# Fixed oracle points: first and last angular points of the 4x8 low grid.
zs,ws=np.polynomial.legendre.leggauss(4)
oracle_tasks=[(0,float(zs[0]),float(ws[0]),0,8,BASE_H,0.0),
              (3,float(zs[-1]),float(ws[-1]),7,8,BASE_H,0.0)]

ctx=mp.get_context('fork')
start=time.perf_counter()
with ctx.Pool(processes=WORKERS) as pool:
    serial=[point_task(x) for x in oracle_tasks]
    parallel=pool.map(point_task,oracle_tasks,chunksize=1)
    oracle_err=0.0
    for a,b in zip(serial,parallel):
        if a[:2]!=b[:2]: raise RuntimeError('oracle_index_drift')
        za=a[2:]; zb=b[2:]
        for x,y in zip(za,zb):
            scale=max(1.0,abs(x),abs(y)); oracle_err=max(oracle_err,float(abs(x-y)/scale))
    if oracle_err>ORACLE_TOL:
        raise RuntimeError(('serial_parallel_oracle_failed',oracle_err,ORACLE_TOL))

    low,es1,un1,re1,la1=sphere_parallel(4,8,BASE_H,0.0,pool)
    high,es2,un2,re2,la2=sphere_parallel(6,12,BASE_H,0.0,pool)
    shifted,es3,un3,re3,la3=sphere_parallel(6,12,BASE_H,0.5,pool)
    halfstep,es4,un4,re4,la4=sphere_parallel(6,12,HALF_H,0.0,pool)
runtime=time.perf_counter()-start

scale=max(1.0,abs(low),abs(high),abs(shifted),abs(halfstep))
conv=float(max(abs(high-low),abs(high-shifted),abs(high-halfstep))/scale)
shell=max(es1,es2,es3,es4); umin=min(un1,un2,un3,un4); radial=max(re1,re2,re3,re4); minlam=min(la1,la2,la3,la4)
status='CONVERGED' if conv<=ANGULAR_CONVERGENCE_TOL and shell<=CUT_SHELL_TOL and radial<=RADIAL_EXTRAP_TOL and umin>UNCUT_MIN_TOL else 'BLOCKED_CONVERGENCE'
# Frozen Iteration 375/337 sign: D_s(double-double)=-sphere_mean[d_u d_v G].
ds=-high
execution_valid=bool(np.isfinite(conv) and shell<=CUT_SHELL_TOL and umin>UNCUT_MIN_TOL and minlam>0 and oracle_err<=ORACLE_TOL)
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
 'classification':('PASS_TRU1SQ_DOUBLE_DOUBLE_PARALLEL_ONE_CHANNEL_PILOT__CONVERGED' if status=='CONVERGED' else
                   'PASS_TRU1SQ_DOUBLE_DOUBLE_PARALLEL_ONE_CHANNEL_PILOT__BLOCKED_CONVERGENCE' if execution_valid else
                   'FAIL_TRU1SQ_DOUBLE_DOUBLE_PARALLEL_ONE_CHANNEL_PILOT_EXECUTION'),
 'parent':'Iteration379 pre-run physics prefix verbatim',
 'resource_architecture':{'workers':WORKERS,'multiprocessing_context':'fork','ordered_map':True,
                          'parallelized_object':'independent angular points only','aggregation_order':'serial z then phi preserved'},
 'serial_parallel_oracle':{'fixed_point_count':2,'scaled_max_error':oracle_err,'threshold':ORACLE_TOL},
 'selected_channel_rule':'FIRST_DOUBLE_DOUBLE_CHANNEL_IN_ITERATION372_FROZEN_ORDER',
 'channel':{'class_id':int(ch['class_id']),'q_squared':float(ch['q_squared']),'shift_i':ch['shift_i'],'shift_j':ch['shift_j'],
            'multiplicity_i':mi,'multiplicity_j':mj,'status':status,
            'D_s_TrU1sq_double_double_channel':[float(ds.real),float(ds.imag)],
            'mixed_derivative_low':[float(low.real),float(low.imag)],'mixed_derivative_high':[float(high.real),float(high.imag)],
            'mixed_derivative_high_phi_shifted':[float(shifted.real),float(shifted.imag)],'mixed_derivative_halfstep':[float(halfstep.real),float(halfstep.imag)],
            'scaled_convergence_error':conv,'max_radial_richardson_scaled_error':radial,'max_cut_shell_abs_error':shell,
            'minimum_sampled_uncut_abs_denominator':umin,'minimum_kallen':minlam},
 'runtime_seconds':float(runtime),
 'derivative':{'variables':['cut_group_1_mass_squared','cut_group_2_mass_squared'],'base_h':BASE_H,'halfstep_h':HALF_H,
               'nodes_per_axis':[-2*BASE_H,-BASE_H,BASE_H,2*BASE_H],
               'normalization':'D_s_double_double=-sphere_mean[d_mu1 d_mu2(beta*num/D_uncut)]'},
 'thresholds':{'angular_convergence_scaled_max':ANGULAR_CONVERGENCE_TOL,'radial_richardson_scaled_max':RADIAL_EXTRAP_TOL,
               'cut_shell_abs_max':CUT_SHELL_TOL,'uncut_abs_min':UNCUT_MIN_TOL,'aux_mass_probe_abs_max':PROBE_MAX,
               'serial_parallel_scaled_max':ORACLE_TOL},
 'quadrature':{'pilot_low':[4,8],'pilot_high':[6,12],'pilot_high_phi_shift':0.5,
               'note':'same prospectively frozen Iteration379 pilot grids; only angular execution parallelized'},
 'effective_action_weight':'NOT_FOLDED__MINUS_I_OVER_4_TRU1SQ_SEPARATE',
 'scope':'ONE_PRESELECTED_DOUBLE_DOUBLE_CHANNEL_ONLY__RESOURCE_REPAIR_OF_CANCELLED_ITERATION379',
 'guardrails':['ITERATION375_MIXED_DERIVATIVE_SIGN_BINDING','ITERATION377_KINEMATIC_BINDING','ITERATION379_PHYSICS_ARITHMETIC_UNCHANGED',
               'SERIAL_PARALLEL_ORACLE_REQUIRED','NO_THRESHOLD_WEAKENING','NO_15_CHANNEL_EXTRAPOLATION_FROM_ONE_CHANNEL',
               'DISTINCT_Q2_BUCKETS_NEVER_SUMMED','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'if raw-valid CONVERGED, use measured parallel runtime only to freeze one-channel-per-job or other safe complete-15 architecture with exactly the same arithmetic; if BLOCKED, preserve channel as BLOCKED and strengthen only its numerical treatment without weakening thresholds'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid:
    raise SystemExit(2)
