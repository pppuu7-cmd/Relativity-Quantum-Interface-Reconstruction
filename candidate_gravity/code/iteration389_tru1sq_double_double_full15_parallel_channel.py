#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 389.

Complete 15-channel physical Tr(U1^2) double-double evaluation, one prospectively
indexed channel per process/job.  Physics arithmetic is identical to the raw-
validated Iteration 385 pilot: Iteration-379 pre-run parent, the Iteration-375
mixed auxiliary-mass derivative sign, Iteration-377 kinematics, unchanged
4x8/6x12 angular grids, h and h/2 mass stencils, radial Richardson rule and
thresholds.  Only independent angular points are parallelized through an
ordered four-worker fork pool, with the same serial-vs-parallel oracle.

CHANNEL_INDEX must be an integer 0..14 in the frozen Iteration-372 double-double
ordering.  No effective-action weight is folded and no q^2 buckets are summed
inside this per-channel evaluator.
"""
from __future__ import annotations
import contextlib, io, json, math, multiprocessing as mp, os, time
from pathlib import Path
import numpy as np

ITERATION=389
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration379_tru1sq_double_double_one_channel_pilot.py'
src=PARENT.read_text()
marker='start=time.perf_counter()'
if src.count(marker)!=1:
    raise RuntimeError('iteration379_run_marker_drift')
prefix=src.split(marker,1)[0]
ns={'__name__':'iteration389_parent379_prefix','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix,str(PARENT),'exec'),ns,ns)

idx=int(os.environ.get('CHANNEL_INDEX','-1'))
dd=[c for c in ns['P372']['channels'] if c['singularity_type']=='double-double']
if len(dd)!=15:
    raise RuntimeError(('double_double_census_drift',len(dd)))
if not (0 <= idx < 15):
    raise RuntimeError(('channel_index_out_of_range',idx))

# Rebind the Iteration-379 global channel state prospectively to the selected
# frozen double-double channel.  The inherited functions resolve these names in
# ns dynamically, so no physics function is rewritten.
ch=dd[idx]
row=ns['rows'][int(ch['class_id'])]
a=np.asarray(ch['shift_i'],float); b=np.asarray(ch['shift_j'],float); q=b-a
mi=int(ch['multiplicity_i']); mj=int(ch['multiplicity_j'])
if (mi,mj)!=(2,2):
    raise RuntimeError(('selected_channel_not_double_double',idx,mi,mj))
q2=float(np.real(ns['mdot'](q))); s=-q2
basis=ns['transverse_basis'](q)
for name,val in {'ch':ch,'row':row,'a':a,'b':b,'q':q,'mi':mi,'mj':mj,'q2':q2,'s':s,'basis':basis}.items():
    ns[name]=val

mixed_derivative_at_unit=ns['mixed_derivative_at_unit']
BASE_H=ns['BASE_H']; HALF_H=ns['HALF_H']
ANGULAR_CONVERGENCE_TOL=ns['ANGULAR_CONVERGENCE_TOL']
CUT_SHELL_TOL=ns['CUT_SHELL_TOL']; UNCUT_MIN_TOL=ns['UNCUT_MIN_TOL']
RADIAL_EXTRAP_TOL=ns['RADIAL_EXTRAP_TOL']; PROBE_MAX=ns['PROBE_MAX']
WORKERS=min(4,max(1,os.cpu_count() or 1)); ORACLE_TOL=2e-13


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
            if rzi!=zi or rm!=m:
                raise RuntimeError('ordered_pool_result_drift')
            row_sum += d2
            max_shell=max(max_shell,sh); min_uncut=min(min_uncut,un)
            max_radial=max(max_radial,ra); min_lam=min(min_lam,la)
        total += float(wz)*(row_sum/nphi)
    return 0.5*total,max_shell,min_uncut,max_radial,min_lam


zs,ws=np.polynomial.legendre.leggauss(4)
oracle_tasks=[(0,float(zs[0]),float(ws[0]),0,8,BASE_H,0.0),
              (3,float(zs[-1]),float(ws[-1]),7,8,BASE_H,0.0)]
ctx=mp.get_context('fork')
start=time.perf_counter()
with ctx.Pool(processes=WORKERS) as pool:
    serial=[point_task(x) for x in oracle_tasks]
    parallel=pool.map(point_task,oracle_tasks,chunksize=1)
    oracle_err=0.0
    for aa,bb in zip(serial,parallel):
        if aa[:2]!=bb[:2]:
            raise RuntimeError('oracle_index_drift')
        for x,y in zip(aa[2:],bb[2:]):
            scale=max(1.0,abs(x),abs(y))
            oracle_err=max(oracle_err,float(abs(x-y)/scale))
    if oracle_err>ORACLE_TOL:
        raise RuntimeError(('serial_parallel_oracle_failed',oracle_err,ORACLE_TOL))

    low,es1,un1,re1,la1=sphere_parallel(4,8,BASE_H,0.0,pool)
    high,es2,un2,re2,la2=sphere_parallel(6,12,BASE_H,0.0,pool)
    shifted,es3,un3,re3,la3=sphere_parallel(6,12,BASE_H,0.5,pool)
    halfstep,es4,un4,re4,la4=sphere_parallel(6,12,HALF_H,0.0,pool)
runtime=time.perf_counter()-start

scale=max(1.0,abs(low),abs(high),abs(shifted),abs(halfstep))
conv=float(max(abs(high-low),abs(high-shifted),abs(high-halfstep))/scale)
shell=max(es1,es2,es3,es4); umin=min(un1,un2,un3,un4)
radial=max(re1,re2,re3,re4); minlam=min(la1,la2,la3,la4)
# Infinity is valid when the selected cut exhausts all denominator groups.
uncut_ok=bool(np.isinf(umin) or umin>UNCUT_MIN_TOL)
status='CONVERGED' if (conv<=ANGULAR_CONVERGENCE_TOL and shell<=CUT_SHELL_TOL and
                       radial<=RADIAL_EXTRAP_TOL and uncut_ok) else 'BLOCKED_CONVERGENCE'
# Frozen Iterations 375/337 sign.
ds=-high
execution_valid=bool(np.isfinite(conv) and shell<=CUT_SHELL_TOL and uncut_ok and minlam>0 and oracle_err<=ORACLE_TOL)
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
 'classification':('PASS_TRU1SQ_DOUBLE_DOUBLE_FULL15_CHANNEL__CONVERGED' if status=='CONVERGED' else
                   'PASS_TRU1SQ_DOUBLE_DOUBLE_FULL15_CHANNEL__BLOCKED_CONVERGENCE' if execution_valid else
                   'FAIL_TRU1SQ_DOUBLE_DOUBLE_FULL15_CHANNEL_EXECUTION'),
 'channel_index':idx,'frozen_channel_count':len(dd),'parent':'Iteration379 pre-run physics prefix verbatim',
 'resource_architecture':{'workers':WORKERS,'multiprocessing_context':'fork','ordered_map':True,
                          'parallelized_object':'independent angular points only','aggregation_order':'serial z then phi preserved'},
 'serial_parallel_oracle':{'fixed_point_count':2,'scaled_max_error':oracle_err,'threshold':ORACLE_TOL},
 'channel':{'class_id':int(ch['class_id']),'q_squared':float(ch['q_squared']),'shift_i':ch['shift_i'],'shift_j':ch['shift_j'],
            'multiplicity_i':mi,'multiplicity_j':mj,'status':status,
            'D_s_TrU1sq_double_double_channel':[float(ds.real),float(ds.imag)],
            'mixed_derivative_low':[float(low.real),float(low.imag)],'mixed_derivative_high':[float(high.real),float(high.imag)],
            'mixed_derivative_high_phi_shifted':[float(shifted.real),float(shifted.imag)],
            'mixed_derivative_halfstep':[float(halfstep.real),float(halfstep.imag)],
            'scaled_convergence_error':conv,'max_radial_richardson_scaled_error':radial,
            'max_cut_shell_abs_error':shell,'minimum_sampled_uncut_abs_denominator':umin,'minimum_kallen':minlam},
 'runtime_seconds':float(runtime),
 'derivative':{'variables':['cut_group_1_mass_squared','cut_group_2_mass_squared'],'base_h':BASE_H,'halfstep_h':HALF_H,
               'nodes_per_axis':[-2*BASE_H,-BASE_H,BASE_H,2*BASE_H],
               'normalization':'D_s_double_double=-sphere_mean[d_mu1 d_mu2(beta*num/D_uncut)]'},
 'thresholds':{'angular_convergence_scaled_max':ANGULAR_CONVERGENCE_TOL,'radial_richardson_scaled_max':RADIAL_EXTRAP_TOL,
               'cut_shell_abs_max':CUT_SHELL_TOL,'uncut_abs_min':UNCUT_MIN_TOL,
               'aux_mass_probe_abs_max':PROBE_MAX,'serial_parallel_scaled_max':ORACLE_TOL},
 'quadrature':{'low':[4,8],'high':[6,12],'high_phi_shift':0.5,
               'note':'identical to raw-valid Iteration385 pilot; no grid or threshold change'},
 'effective_action_weight':'NOT_FOLDED__MINUS_I_OVER_4_TRU1SQ_SEPARATE',
 'scope':'ONE_OF_15_PROSPECTIVELY_INDEXED_DOUBLE_DOUBLE_CHANNELS__FULL_SECTOR_MATRIX',
 'guardrails':['ITERATION375_MIXED_DERIVATIVE_SIGN_BINDING','ITERATION377_KINEMATIC_BINDING',
               'ITERATION385_RAW_VALID_RESOURCE_ORACLE_BINDING','NO_THRESHOLD_WEAKENING','NO_ZERO_FILL',
               'DISTINCT_Q2_BUCKETS_NEVER_SUMMED','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'assemble q2-resolved double-double sums only after all 15 indexed raw artifacts are present; any BLOCKED_CONVERGENCE remains blocked and prevents the affected q2 bucket from closing'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid:
    raise SystemExit(2)
