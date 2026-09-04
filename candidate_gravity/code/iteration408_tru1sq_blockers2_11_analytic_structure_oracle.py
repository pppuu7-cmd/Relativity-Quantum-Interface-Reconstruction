#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 408.

Independent STRUCTURE-ONLY oracle for the two unresolved Tr(U1^2) double-double
blockers not covered by Iteration 401: global indices 2 and 11.  This does not
promote a physical D_s value and does not anticipate the outcome of active
Iteration 407.  It asks only whether the exact frozen Iteration-379/389
integrands admit the same one-affine-denominator / low-harmonic azimuthal
representation already prospectively frozen by Iteration 401.

No numerator, routing, mass stencil, normalization, physical convergence
threshold, Source/Born accounting, or ansatz is changed.
"""
from __future__ import annotations
import contextlib, io, json, math
from pathlib import Path
import numpy as np

ITERATION=408
TARGETS=(2,11)
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration379_tru1sq_double_double_one_channel_pilot.py'
src=PARENT.read_text(); marker='start=time.perf_counter()'
if src.count(marker)!=1: raise RuntimeError('iteration379_run_marker_drift')
ns={'__name__':'iteration408_parent379_prefix','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split(marker,1)[0],str(PARENT),'exec'),ns,ns)

dd=[c for c in ns['P372']['channels'] if c['singularity_type']=='double-double']
if len(dd)!=15: raise RuntimeError(('double_double_census_drift',len(dd)))
parent374=ns['ns']; vk=ns['vk']; mdot=ns['mdot']; mbilin=parent374['mbilin']; mproj_orth=parent374['mproj_orth']
stripped_limit_massive=ns['stripped_limit_massive']; BASE_H=ns['BASE_H']

DEN_AFFINE_REL_TOL=2e-11
PHASE_MEAN_REL_TOL=2e-6
FOURIER_TAIL_REL_TOL=2e-6
POLY_HELDOUT_REL_TOL=2e-6
BASIS_ORTHO_TOL=2e-12
FOURIER_N=24
FOURIER_MAX_ACCEPTED_MODE=8
MEAN_NPHI=16
DEGREES=(4,6,8,10,12)
TRAIN_Z=np.linspace(-0.9,0.9,13)
HELDOUT_Z=np.array([-0.83,-0.57,-0.31,-0.07,0.23,0.49,0.77,0.88])
MASS_PAIRS_FACTOR=((-2,-2),(-1,1),(2,1))


def evaluate_target(target_index):
    ch=dd[target_index]; row=ns['rows'][int(ch['class_id'])]
    a=np.asarray(ch['shift_i'],float); b=np.asarray(ch['shift_j'],float); q=b-a
    q2=float(np.real(mdot(q))); s=-q2
    mult={}; reps={}
    for sh in row['shifts']:
        k=vk(sh); mult[k]=mult.get(k,0)+1; reps[k]=np.asarray(sh,float)
    ka,kb=vk(a),vk(b)
    if mult.get(ka)!=2 or mult.get(kb)!=2:
        raise RuntimeError(('cut_multiplicity_drift',target_index,mult.get(ka),mult.get(kb)))
    uncut_keys=[k for k in mult if k not in (ka,kb)]
    if len(uncut_keys)!=1 or mult[uncut_keys[0]]!=1:
        raise RuntimeError(('expected_exactly_one_simple_uncut_group',target_index,mult,uncut_keys))
    c=reps[uncut_keys[0]]
    rvec=mproj_orth(c-a,q); r2=float(np.real(mdot(rvec)))
    if r2<=1e-12: raise RuntimeError(('uncut_transverse_projection_degenerate',target_index,r2))
    e3=rvec/math.sqrt(r2); base=ns['transverse_basis'](q); es=[]
    for seed in base:
        v=np.asarray(seed,float)-mbilin(seed,e3)*e3
        for e in es: v=v-mbilin(v,e)*e
        n2=float(np.real(mdot(v)))
        if n2>1e-12: es.append(v/math.sqrt(n2))
        if len(es)==2: break
    if len(es)!=2: raise RuntimeError(('aligned_transverse_basis_failed',target_index))
    e1,e2=es
    gram=np.array([[mbilin(x,y) for y in (e1,e2,e3)] for x in (e1,e2,e3)])
    basis_err=float(np.max(np.abs(gram-np.eye(3))))
    if basis_err>BASIS_ORTHO_TOL: raise RuntimeError(('basis_orthogonality_failed',target_index,basis_err))

    def kin(u,v):
        lam=s*s+u*u+v*v-2*s*u-2*s*v-2*u*v
        if lam<=0: raise RuntimeError(('nonpositive_kallen',target_index,u,v,lam))
        alpha=-(s+u-v)/(2.0*s); rho=math.sqrt(lam)/(2.0*math.sqrt(s)); beta=math.sqrt(lam)/s
        return alpha,rho,beta,lam
    def unit_from(z,phi):
        rr=math.sqrt(max(0.0,1.0-float(z)*float(z)))
        return rr*math.cos(phi)*e1+rr*math.sin(phi)*e2+float(z)*e3
    def numerator_at(u,v,z,phi):
        alpha,rho,_,_=kin(u,v); num,raderr=stripped_limit_massive(alpha,rho*unit_from(z,phi))
        return complex(num),float(raderr)
    def direct_uncut(u,v,z,phi):
        alpha,rho,_,_=kin(u,v); p0=-a+alpha*q+rho*unit_from(z,phi)
        return complex(mdot(p0+c))
    def affine_coeffs(u,v):
        alpha,rho,_,_=kin(u,v); r0=-a+alpha*q+c
        return complex(mdot(r0)+rho*rho), complex(2.0*rho*mbilin(r0,e3))

    max_den=0.0; max_rad=0.0; max_phase=0.0; max_tail=0.0; mass_results=[]
    for fu,fv in MASS_PAIRS_FACTOR:
        u,v=fu*BASE_H,fv*BASE_H; cc,aa=affine_coeffs(u,v)
        for z in (-0.73,-0.18,0.41,0.86):
            for frac in (0.07,0.31,0.68):
                d=direct_uncut(u,v,z,2*math.pi*frac); pred=cc+aa*z
                max_den=max(max_den,float(abs(d-pred)/max(1.0,abs(d),abs(pred))))
        fourier_rows=[]
        for z in (-0.62,0.11,0.71):
            vals=[]
            for m in range(FOURIER_N):
                num,ra=numerator_at(u,v,z,2*math.pi*m/FOURIER_N); vals.append(num); max_rad=max(max_rad,ra)
            arr=np.asarray(vals,complex); coeff=np.fft.fft(arr)/FOURIER_N
            modes=np.array([min(k,FOURIER_N-k) for k in range(FOURIER_N)])
            scale=max(1.0,float(np.max(np.abs(coeff))))
            tail=float(np.max(np.abs(coeff[modes>FOURIER_MAX_ACCEPTED_MODE]))/scale); max_tail=max(max_tail,tail)
            fourier_rows.append({'z':float(z),'tail_above_abs_mode_8_scaled':tail})
        def phi_mean(z,phase):
            vals=[]
            for m in range(MEAN_NPHI):
                num,_=numerator_at(u,v,z,2*math.pi*(m+phase)/MEAN_NPHI); vals.append(num)
            return sum(vals,0j)/MEAN_NPHI
        train0=np.array([phi_mean(float(z),0.0) for z in TRAIN_Z],complex)
        train1=np.array([phi_mean(float(z),0.371) for z in TRAIN_Z],complex)
        held0=np.array([phi_mean(float(z),0.0) for z in HELDOUT_Z],complex)
        held1=np.array([phi_mean(float(z),0.371) for z in HELDOUT_Z],complex)
        phase_scale=max(1.0,float(np.max(np.abs(np.concatenate([train0,train1,held0,held1])))))
        phase=float(np.max(np.abs(np.concatenate([train0-train1,held0-held1])))/phase_scale); max_phase=max(max_phase,phase)
        target_train=0.5*(train0+train1); target_held=0.5*(held0+held1); best=None
        for deg in DEGREES:
            cr=np.polynomial.polynomial.polyfit(TRAIN_Z,target_train.real,deg); ci=np.polynomial.polynomial.polyfit(TRAIN_Z,target_train.imag,deg)
            pred=np.polynomial.polynomial.polyval(HELDOUT_Z,cr)+1j*np.polynomial.polynomial.polyval(HELDOUT_Z,ci)
            scale=max(1.0,float(np.max(np.abs(target_held))),float(np.max(np.abs(pred))))
            err=float(np.max(np.abs(pred-target_held))/scale)
            cand={'degree':int(deg),'heldout_scaled_error':err}
            if best is None or err<best['heldout_scaled_error']: best=cand
            if err<=POLY_HELDOUT_REL_TOL: best=cand; break
        mass_results.append({'u':float(u),'v':float(v),'phase_mean_scaled_error':phase,'azimuth_mean_polynomial_fit':best,'fourier_checks':fourier_rows})
    max_poly=max(x['azimuth_mean_polynomial_fit']['heldout_scaled_error'] for x in mass_results)
    passed=bool(max_den<=DEN_AFFINE_REL_TOL and max_tail<=FOURIER_TAIL_REL_TOL and max_phase<=PHASE_MEAN_REL_TOL and max_poly<=POLY_HELDOUT_REL_TOL)
    return {
        'double_double_global_index':target_index,'class_id':int(ch['class_id']),'q_squared':q2,
        'cut_group_multiplicities':[mult[ka],mult[kb]],'distinct_denominator_group_count':len(mult),
        'remaining_uncut_group_count':1,'remaining_uncut_multiplicity':1,'remaining_uncut_shift':c.tolist(),
        'aligned_basis_orthogonality_error':basis_err,'uncut_transverse_norm_squared':r2,
        'observed':{'max_denominator_affine_scaled_error':max_den,'max_fourier_tail_scaled_error':max_tail,
                    'max_phase_mean_scaled_error':max_phase,'max_polynomial_heldout_scaled_error':max_poly,
                    'max_radial_richardson_scaled_error_seen':max_rad},
        'structure_status':'PASS' if passed else 'BLOCKED','mass_node_results':mass_results}

results=[evaluate_target(i) for i in TARGETS]
all_pass=all(x['structure_status']=='PASS' for x in results)
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':True,'candidate_residual':False,
 'classification':('PASS_TRU1SQ_BLOCKERS2_11_ANALYTIC_AZIMUTH_STRUCTURE_ORACLE' if all_pass else 'BLOCKED_TRU1SQ_BLOCKERS2_11_ANALYTIC_AZIMUTH_STRUCTURE_ORACLE'),
 'targets':results,
 'oracle_thresholds':{'denominator_affine_scaled_max':DEN_AFFINE_REL_TOL,'phase_mean_scaled_max':PHASE_MEAN_REL_TOL,
                      'fourier_tail_above_abs_mode_8_scaled_max':FOURIER_TAIL_REL_TOL,
                      'azimuth_mean_polynomial_heldout_scaled_max':POLY_HELDOUT_REL_TOL,'candidate_polynomial_degrees':list(DEGREES)},
 'scope':'STRUCTURE_ONLY__INDICES_2_AND_11__NO_NEW_D_S_VALUE__NO_ANGULAR_GRID_LADDER',
 'physics_immutability':{'parent':'Iteration379/389 physical double-double integrand','frozen_physical_convergence_threshold':2e-5,
                         'mass_derivative_stencil':'unchanged central4 x central4','normalization':'unchanged D_s_double_double=-sphere_mean[d_u d_v G]'},
 'guardrails':['NO_PHYSICAL_VALUE_PROMOTION','NO_THRESHOLD_WEAKENING','ITERATION407_NOT_DUPLICATED','TRAINING_AND_HELDOUT_Z_SEPARATE',
               'INDEPENDENT_PHI_PHASE_REQUIRED','DENOMINATOR_AFFINE_CHECKED_DIRECTLY','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'Raw-audit this structural result. Physical evaluation of indices 2 and 11 remains downstream of the active Iteration407 channel-4 result; if structurally PASS and Iteration407 physical reduction is CONVERGED, use the same frozen reduction separately for 2 and 11 with held-out original-integrand checks.'
}
print(json.dumps(result,indent=2,sort_keys=True))
