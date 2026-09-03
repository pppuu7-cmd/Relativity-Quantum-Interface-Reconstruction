#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 379.

One prospectively selected physical double-double Tr(U1^2) channel pilot.
Purpose: validate the complete mixed auxiliary-mass derivative integration
pipeline and measure runtime before scaling to all 15 double-double channels.

Selection rule: first double-double channel in the frozen Iteration-372 ordering.
Physical stripped numerator and radial extrapolation are inherited from the same
Iteration-370/374 parent as the simple-simple and simple-double sectors.
Iteration 375 fixes the mixed derivative sign/order and Iteration 377 certifies
the auxiliary-mass kinematics. The reduced one-loop -i/4 coefficient is not
folded into this Tr(U1^2) coordinate.
"""
from __future__ import annotations
import contextlib, io, json, math, time
from pathlib import Path
import numpy as np

ITERATION=379
ROOT=Path(__file__).resolve().parent
SRC374=ROOT/'iteration374_tru1sq_simple_simple_normalized_discontinuity.py'
src=SRC374.read_text().split('records=[]; by_q=defaultdict(list)',1)[0]
ns={'__name__':'iteration379_parent374_prefix','__file__':str(SRC374)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(src,str(SRC374),'exec'),ns,ns)

P372=ns['P372']; rows=ns['rows']; stripped=ns['stripped']; vk=ns['vk']; mdot=ns['mdot']; transverse_basis=ns['transverse_basis']
HS=ns['HS']; ANGULAR_CONVERGENCE_TOL=ns['ANGULAR_CONVERGENCE_TOL']; CUT_SHELL_TOL=ns['CUT_SHELL_TOL']; UNCUT_MIN_TOL=ns['UNCUT_MIN_TOL']; RADIAL_EXTRAP_TOL=ns['RADIAL_EXTRAP_TOL']
BASE_H=5e-6; HALF_H=2.5e-6; PROBE_MAX=1e-5

dd=[c for c in P372['channels'] if c['singularity_type']=='double-double']
if len(dd)!=15: raise RuntimeError(('double_double_census_drift',len(dd)))
ch=dd[0]
row=rows[int(ch['class_id'])]
a=np.asarray(ch['shift_i'],float); b=np.asarray(ch['shift_j'],float); q=b-a
mi=int(ch['multiplicity_i']); mj=int(ch['multiplicity_j'])
if (mi,mj)!=(2,2): raise RuntimeError(('selected_channel_not_double_double',mi,mj))
q2=float(np.real(mdot(q))); s=-q2; basis=transverse_basis(q)


def central4(vals,h):
    return (vals[0]-8.0*vals[1]+8.0*vals[2]-vals[3])/(12.0*h)


def stripped_limit_massive(alpha,vvec):
    mids=[]
    for h in HS:
        vals=[]
        for sign in (+1,-1):
            ph=-a+alpha*q+(1.0+sign*h)*vvec
            z,_=stripped(row,ph); vals.append(complex(z))
        mids.append(0.5*(vals[0]+vals[1]))
    ext_coarse=(4.0*mids[1]-mids[0])/3.0
    ext_fine=(4.0*mids[2]-mids[1])/3.0
    scale=max(1.0,abs(ext_fine),abs(ext_coarse),*(abs(z) for z in mids))
    err=float(abs(ext_fine-ext_coarse)/scale)
    return ext_fine,err


def G_at_masses(u,v,unit):
    lam=s*s+u*u+v*v-2*s*u-2*s*v-2*u*v
    if lam<=0: raise RuntimeError(('nonpositive_kallen',u,v,lam))
    alpha=-(s+u-v)/(2.0*s); rho=math.sqrt(lam)/(2.0*math.sqrt(s)); beta=math.sqrt(lam)/s
    vvec=rho*unit; p0=-a+alpha*q+vvec
    shell=max(abs(mdot(p0+a)+u),abs(mdot(p0+b)+v))
    num,raderr=stripped_limit_massive(alpha,vvec)
    d=1+0j; min_uncut=float('inf')
    for sh in row['shifts']:
        if vk(sh) in (vk(a),vk(b)): continue
        du=mdot(p0+np.asarray(sh,float)); min_uncut=min(min_uncut,abs(du)); d*=du
    if abs(d)<UNCUT_MIN_TOL: raise RuntimeError(('uncut_pole_encountered',abs(d)))
    return beta*num/d,float(shell),float(min_uncut),float(raderr),float(lam)


def mixed_derivative_at_unit(unit,h):
    nodes=[-2*h,-h,h,2*h]
    if max(abs(x) for x in nodes)>PROBE_MAX*(1+1e-12): raise RuntimeError(('probe_envelope_exceeded',nodes))
    vals=np.empty((4,4),dtype=complex); max_shell=0.0; min_uncut=float('inf'); max_radial=0.0; min_lam=float('inf')
    for i,u in enumerate(nodes):
        for j,v in enumerate(nodes):
            g,sh,un,ra,la=G_at_masses(u,v,unit); vals[i,j]=g
            max_shell=max(max_shell,sh); min_uncut=min(min_uncut,un); max_radial=max(max_radial,ra); min_lam=min(min_lam,la)
    first=np.array([central4(vals[:,j],h) for j in range(4)],dtype=complex)
    return central4(first,h),max_shell,min_uncut,max_radial,min_lam


def sphere_mixed_derivative(nz,nphi,h,phi_shift=0.0):
    zs,ws=np.polynomial.legendre.leggauss(nz)
    total=0j; max_shell=0.0; min_uncut=float('inf'); max_radial=0.0; min_lam=float('inf')
    for z,wz in zip(zs,ws):
        rr=math.sqrt(max(0.0,1.0-float(z)*float(z))); row_sum=0j
        for m in range(nphi):
            phi=2.0*math.pi*(m+phi_shift)/nphi
            n=np.array([rr*math.cos(phi),rr*math.sin(phi),float(z)])
            unit=n[0]*basis[0]+n[1]*basis[1]+n[2]*basis[2]
            d2,sh,un,ra,la=mixed_derivative_at_unit(unit,h); row_sum+=d2
            max_shell=max(max_shell,sh); min_uncut=min(min_uncut,un); max_radial=max(max_radial,ra); min_lam=min(min_lam,la)
        total+=float(wz)*(row_sum/nphi)
    return 0.5*total,max_shell,min_uncut,max_radial,min_lam

start=time.perf_counter()
low,es1,un1,re1,la1=sphere_mixed_derivative(4,8,BASE_H,0.0)
high,es2,un2,re2,la2=sphere_mixed_derivative(6,12,BASE_H,0.0)
shifted,es3,un3,re3,la3=sphere_mixed_derivative(6,12,BASE_H,0.5)
halfstep,es4,un4,re4,la4=sphere_mixed_derivative(6,12,HALF_H,0.0)
runtime=time.perf_counter()-start
scale=max(1.0,abs(low),abs(high),abs(shifted),abs(halfstep))
conv=float(max(abs(high-low),abs(high-shifted),abs(high-halfstep))/scale)
shell=max(es1,es2,es3,es4); umin=min(un1,un2,un3,un4); radial=max(re1,re2,re3,re4); minlam=min(la1,la2,la3,la4)
status='CONVERGED' if conv<=ANGULAR_CONVERGENCE_TOL and shell<=CUT_SHELL_TOL and radial<=RADIAL_EXTRAP_TOL and umin>UNCUT_MIN_TOL else 'BLOCKED_CONVERGENCE'
# Iteration 375 gives two propagator minus signs -> plus derivative of the simple integrand;
# Iteration 337 contributes D_s(simple)=-mean(G), hence D_s(double-double)=-mean[d_u d_v G].
ds=-high
execution_valid=bool(np.isfinite(conv) and shell<=CUT_SHELL_TOL and umin>UNCUT_MIN_TOL and minlam>0)
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
 'classification':('PASS_TRU1SQ_DOUBLE_DOUBLE_ONE_CHANNEL_PILOT__CONVERGED' if status=='CONVERGED' else
                   'PASS_TRU1SQ_DOUBLE_DOUBLE_ONE_CHANNEL_PILOT__BLOCKED_CONVERGENCE' if execution_valid else
                   'FAIL_TRU1SQ_DOUBLE_DOUBLE_ONE_CHANNEL_PILOT_EXECUTION'),
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
               'cut_shell_abs_max':CUT_SHELL_TOL,'uncut_abs_min':UNCUT_MIN_TOL,'aux_mass_probe_abs_max':PROBE_MAX},
 'quadrature':{'pilot_low':[4,8],'pilot_high':[6,12],'pilot_high_phi_shift':0.5,
               'note':'resource-aware one-channel pilot; no full-sector promotion from this grid alone'},
 'effective_action_weight':'NOT_FOLDED__MINUS_I_OVER_4_TRU1SQ_SEPARATE',
 'scope':'ONE_PRESELECTED_DOUBLE_DOUBLE_CHANNEL_ONLY__MIXED_DERIVATIVE_RUNTIME_AND_PIPELINE_PILOT',
 'guardrails':['ITERATION375_MIXED_DERIVATIVE_SIGN_BINDING','ITERATION377_KINEMATIC_BINDING','NO_THRESHOLD_WEAKENING',
               'NO_15_CHANNEL_EXTRAPOLATION_FROM_ONE_CHANNEL','FULL_SECTOR_GRID_MUST_BE_PROSPECTIVELY_FROZEN_AFTER_PILOT',
               'DISTINCT_Q2_BUCKETS_NEVER_SUMMED','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('if CONVERGED, use measured runtime and convergence margin to prospectively freeze the full-sector angular grid and fixed chunk size for all 15 double-double channels; if BLOCKED, strengthen only this pilot analytically/numerically without weakening thresholds')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid: raise SystemExit(2)
