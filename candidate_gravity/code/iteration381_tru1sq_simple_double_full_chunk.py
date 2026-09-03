#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 381.

Full-sector physical simple-double Tr(U1^2) discontinuity evaluator, executed in
prospectively frozen three-channel chunks.  The architecture is frozen only
after raw Iteration-378 pilot validation (runtime ~21.9 min/channel), while all
physics/arithmetic is identical to Iteration 378.

No channel is inferred from the pilot.  Every one of the 36 frozen
Iteration-372 simple-double channels is evaluated independently.  Chunk
artifacts have only chunk authority; full-sector authority requires later
assembly with exactly 36 unique frozen channel indices, no gaps/overlaps and
raw sentinel validation for every chunk.
"""
from __future__ import annotations
import argparse, contextlib, io, json, math, time
from collections import defaultdict
from pathlib import Path
import numpy as np

ITERATION=381
ROOT=Path(__file__).resolve().parent
SRC374=ROOT/'iteration374_tru1sq_simple_simple_normalized_discontinuity.py'
src=SRC374.read_text().split('records=[]; by_q=defaultdict(list)',1)[0]
ns={'__name__':'iteration381_parent374_prefix','__file__':str(SRC374)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(src,str(SRC374),'exec'),ns,ns)

P372=ns['P372']; rows=ns['rows']; stripped=ns['stripped']; vk=ns['vk']; mdot=ns['mdot']; transverse_basis=ns['transverse_basis']
HS=ns['HS']; ANGULAR_CONVERGENCE_TOL=ns['ANGULAR_CONVERGENCE_TOL']; CUT_SHELL_TOL=ns['CUT_SHELL_TOL']; UNCUT_MIN_TOL=ns['UNCUT_MIN_TOL']; RADIAL_EXTRAP_TOL=ns['RADIAL_EXTRAP_TOL']
BASE_H=5e-6; HALF_H=2.5e-6; PROBE_MAX=1e-5
LOW=(6,12); HIGH=(8,16); HIGH_PHI_SHIFT=0.5

sd=[c for c in P372['channels'] if c['singularity_type']=='simple-double']
if len(sd)!=36: raise RuntimeError(('simple_double_census_drift',len(sd)))


def central4(vals,h):
    return (vals[0]-8.0*vals[1]+8.0*vals[2]-vals[3])/(12.0*h)


def evaluate_channel(global_index,ch):
    row=rows[int(ch['class_id'])]
    a=np.asarray(ch['shift_i'],float); b=np.asarray(ch['shift_j'],float); q=b-a
    mi=int(ch['multiplicity_i']); mj=int(ch['multiplicity_j'])
    if sorted((mi,mj))!=[1,2]: raise RuntimeError(('selected_channel_not_simple_double',global_index,mi,mj))
    q2=float(np.real(mdot(q))); s=-q2; basis=transverse_basis(q)

    def stripped_limit_massive(alpha,vvec):
        mids=[]
        for hh in HS:
            vals=[]
            for sign in (+1,-1):
                ph=-a+alpha*q+(1.0+sign*hh)*vvec
                z,_=stripped(row,ph); vals.append(complex(z))
            mids.append(0.5*(vals[0]+vals[1]))
        ext_coarse=(4.0*mids[1]-mids[0])/3.0
        ext_fine=(4.0*mids[2]-mids[1])/3.0
        scale=max(1.0,abs(ext_fine),abs(ext_coarse),*(abs(z) for z in mids))
        err=float(abs(ext_fine-ext_coarse)/scale)
        return ext_fine,err

    def G_at_mu(mu,unit):
        u=mu if mi==2 else 0.0; v=mu if mj==2 else 0.0
        lam=s*s+u*u+v*v-2*s*u-2*s*v-2*u*v
        if lam<=0: raise RuntimeError(('nonpositive_kallen',global_index,mu,lam))
        alpha=-(s+u-v)/(2.0*s); rho=math.sqrt(lam)/(2.0*math.sqrt(s)); beta=math.sqrt(lam)/s
        vvec=rho*unit; p0=-a+alpha*q+vvec
        shell=max(abs(mdot(p0+a)+u),abs(mdot(p0+b)+v))
        num,raderr=stripped_limit_massive(alpha,vvec)
        d=1+0j; min_uncut=float('inf')
        for sh in row['shifts']:
            if vk(sh) in (vk(a),vk(b)): continue
            du=mdot(p0+np.asarray(sh,float)); min_uncut=min(min_uncut,abs(du)); d*=du
        if abs(d)<UNCUT_MIN_TOL: raise RuntimeError(('uncut_pole_encountered',global_index,abs(d)))
        return beta*num/d,float(shell),float(min_uncut),float(raderr),float(lam)

    def sphere_derivative(nz,nphi,h,phi_shift=0.0):
        mus=[-2*h,-h,h,2*h]
        if max(abs(x) for x in mus)>PROBE_MAX*(1+1e-12): raise RuntimeError(('probe_envelope_exceeded',mus))
        zs,ws=np.polynomial.legendre.leggauss(nz)
        total=0j; max_shell=0.0; min_uncut=float('inf'); max_radial=0.0; min_lam=float('inf')
        for z,wz in zip(zs,ws):
            rr=math.sqrt(max(0.0,1.0-float(z)*float(z))); row_sum=0j
            for m in range(nphi):
                phi=2.0*math.pi*(m+phi_shift)/nphi
                n=np.array([rr*math.cos(phi),rr*math.sin(phi),float(z)])
                unit=n[0]*basis[0]+n[1]*basis[1]+n[2]*basis[2]
                vals=[]
                for mu in mus:
                    g,sh,un,ra,la=G_at_mu(mu,unit); vals.append(g)
                    max_shell=max(max_shell,sh); min_uncut=min(min_uncut,un); max_radial=max(max_radial,ra); min_lam=min(min_lam,la)
                row_sum+=central4(vals,h)
            total+=float(wz)*(row_sum/nphi)
        return 0.5*total,max_shell,min_uncut,max_radial,min_lam

    start=time.perf_counter()
    low,es1,un1,re1,la1=sphere_derivative(*LOW,BASE_H,0.0)
    high,es2,un2,re2,la2=sphere_derivative(*HIGH,BASE_H,0.0)
    shifted,es3,un3,re3,la3=sphere_derivative(*HIGH,BASE_H,HIGH_PHI_SHIFT)
    halfstep,es4,un4,re4,la4=sphere_derivative(*HIGH,HALF_H,0.0)
    runtime=time.perf_counter()-start
    scale=max(1.0,abs(low),abs(high),abs(shifted),abs(halfstep))
    conv=float(max(abs(high-low),abs(high-shifted),abs(high-halfstep))/scale)
    shell=max(es1,es2,es3,es4); umin=min(un1,un2,un3,un4); radial=max(re1,re2,re3,re4); minlam=min(la1,la2,la3,la4)
    status='CONVERGED' if conv<=ANGULAR_CONVERGENCE_TOL and shell<=CUT_SHELL_TOL and radial<=RADIAL_EXTRAP_TOL and umin>UNCUT_MIN_TOL else 'BLOCKED_CONVERGENCE'
    execution_valid=bool(np.isfinite(conv) and shell<=CUT_SHELL_TOL and umin>UNCUT_MIN_TOL and minlam>0)
    return {
      'global_simple_double_index':int(global_index),'class_id':int(ch['class_id']),'q_squared':float(ch['q_squared']),
      'shift_i':ch['shift_i'],'shift_j':ch['shift_j'],'multiplicity_i':mi,'multiplicity_j':mj,'status':status,
      'execution_valid':execution_valid,'D_s_TrU1sq_simple_double_channel':[float(high.real),float(high.imag)],
      'derivative_low':[float(low.real),float(low.imag)],'derivative_high':[float(high.real),float(high.imag)],
      'derivative_high_phi_shifted':[float(shifted.real),float(shifted.imag)],'derivative_halfstep':[float(halfstep.real),float(halfstep.imag)],
      'scaled_convergence_error':conv,'max_radial_richardson_scaled_error':radial,'max_cut_shell_abs_error':shell,
      'minimum_sampled_uncut_abs_denominator':umin,'minimum_kallen':minlam,'runtime_seconds':float(runtime)
    }

ap=argparse.ArgumentParser(); ap.add_argument('--start',type=int,required=True); ap.add_argument('--end',type=int,required=True); args=ap.parse_args()
if not (0<=args.start<args.end<=36): raise RuntimeError(('invalid_chunk',args.start,args.end))
if args.end-args.start!=3: raise RuntimeError(('chunk_size_must_be_three',args.start,args.end))
records=[evaluate_channel(i,sd[i]) for i in range(args.start,args.end)]
execution_valid=all(r['execution_valid'] for r in records)
converged=sum(r['status']=='CONVERGED' for r in records); blocked=len(records)-converged
by_q=defaultdict(list)
for r in records: by_q[str(r['q_squared'])].append(r['D_s_TrU1sq_simple_double_channel'])
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
 'classification':f'PASS_TRU1SQ_SIMPLE_DOUBLE_FULL_CHUNK__CONVERGED_{converged}__BLOCKED_{blocked}' if execution_valid else 'FAIL_TRU1SQ_SIMPLE_DOUBLE_FULL_CHUNK_EXECUTION',
 'chunk':{'start_inclusive':args.start,'end_exclusive':args.end,'size':3,'frozen_total_simple_double_channels':36},
 'channels':records,'q2_coordinates_present':sorted(by_q.keys()),
 'runtime_seconds':float(sum(r['runtime_seconds'] for r in records)),
 'derivative':{'variable':'double_cut_group_mass_squared','base_h':BASE_H,'halfstep_h':HALF_H,
               'base_nodes':[-2*BASE_H,-BASE_H,BASE_H,2*BASE_H],'normalization':'D_s_simple_double=+sphere_mean[d_mu(beta*num/D_uncut)]'},
 'thresholds':{'angular_convergence_scaled_max':ANGULAR_CONVERGENCE_TOL,'radial_richardson_scaled_max':RADIAL_EXTRAP_TOL,
               'cut_shell_abs_max':CUT_SHELL_TOL,'uncut_abs_min':UNCUT_MIN_TOL,'aux_mass_probe_abs_max':PROBE_MAX},
 'quadrature':{'low':list(LOW),'high':list(HIGH),'high_phi_shift':HIGH_PHI_SHIFT},
 'effective_action_weight':'NOT_FOLDED__MINUS_I_OVER_4_TRU1SQ_SEPARATE',
 'scope':'THREE_CHANNEL_CHUNK_ONLY__FULL_SECTOR_REQUIRES_EXACT_36_CHANNEL_ASSEMBLY',
 'architecture_binding':'12_FIXED_CHUNKS_OF_3__FROZEN_FROM_RAW_ITERATION378_RUNTIME__IDENTICAL_ARITHMETIC',
 'guardrails':['ITERATION375_SIGN_BINDING','ITERATION377_KINEMATIC_BINDING','ITERATION378_RAW_PILOT_BINDING','NO_THRESHOLD_WEAKENING',
               'NO_CHUNK_EXTRAPOLATION','DISTINCT_Q2_BUCKETS_NEVER_SUMMED','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'after all 12 raw chunk artifacts validate, assemble exactly 36 unique frozen indices with no gaps/overlaps; BLOCKED channels remain BLOCKED and are not zero-filled'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid: raise SystemExit(2)
