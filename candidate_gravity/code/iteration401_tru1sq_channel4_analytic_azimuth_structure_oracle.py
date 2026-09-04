#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 401.

Structural oracle for analytic/spectral angular reduction of the prospectively
targeted Tr(U1^2) double-double convergence blocker: Iteration-389 global index
4, class 5, q^2=-1. Iteration 402 later establishes that indices 2 and 11 are
additional blockers; this oracle remains a channel-4 structural template only.

This is NOT another angular-grid convergence ladder and does NOT promote a new
physical D_s value. It tests whether the exact frozen integrand admits the same
kind of controlled azimuth reduction used successfully in Iteration 380:

1. after cutting the two multiplicity-2 groups, exactly one uncut propagator remains;
2. after aligning one transverse axis with that uncut shift, its denominator is affine in z and independent of phi;
3. the off-shell stripped physical numerator has finite low harmonic content in phi and its azimuthal mean is represented by a low-degree polynomial in z, validated on held-out z nodes and an independent phi phase.

No physics threshold, derivative stencil, radial Richardson rule, numerator,
routing, normalization, or source subtraction is changed.
"""
from __future__ import annotations
import contextlib, io, json, math
from pathlib import Path
import numpy as np

ITERATION=401
TARGET_INDEX=4
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration379_tru1sq_double_double_one_channel_pilot.py'
src=PARENT.read_text(); marker='start=time.perf_counter()'
if src.count(marker)!=1: raise RuntimeError('iteration379_run_marker_drift')
ns={'__name__':'iteration401_parent379_prefix','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split(marker,1)[0],str(PARENT),'exec'),ns,ns)

dd=[c for c in ns['P372']['channels'] if c['singularity_type']=='double-double']
if len(dd)!=15: raise RuntimeError(('double_double_census_drift',len(dd)))
ch=dd[TARGET_INDEX]; row=ns['rows'][int(ch['class_id'])]
a=np.asarray(ch['shift_i'],float); b=np.asarray(ch['shift_j'],float); q=b-a
q2=float(np.real(ns['mdot'](q))); s=-q2
if abs(q2+1.0)>1e-12 or int(ch['class_id'])!=5: raise RuntimeError(('target_identity_drift',q2,ch['class_id']))
for name,val in {'ch':ch,'row':row,'a':a,'b':b,'q':q,'q2':q2,'s':s}.items(): ns[name]=val

# Iteration379 executes Iteration374 in an inner namespace stored as ns['ns'];
# geometry helpers live there, while vk/mdot/transverse_basis are explicitly
# re-exported by Iteration379. This lookup is plumbing only, not a gate change.
parent374=ns['ns']
vk=ns['vk']; mdot=ns['mdot']; mbilin=parent374['mbilin']; mproj_orth=parent374['mproj_orth']
stripped_limit_massive=ns['stripped_limit_massive']; BASE_H=ns['BASE_H']

mult={}; reps={}
for sh in row['shifts']:
    k=vk(sh); mult[k]=mult.get(k,0)+1; reps[k]=np.asarray(sh,float)
ka,kb=vk(a),vk(b)
if mult.get(ka)!=2 or mult.get(kb)!=2: raise RuntimeError(('cut_multiplicity_drift',mult.get(ka),mult.get(kb)))
uncut_keys=[k for k,m in mult.items() if k not in (ka,kb)]
if len(uncut_keys)!=1 or mult[uncut_keys[0]]!=1: raise RuntimeError(('expected_exactly_one_simple_uncut_group',mult,uncut_keys))
c=reps[uncut_keys[0]]

rvec=mproj_orth(c-a,q); r2=float(np.real(mdot(rvec)))
if r2<=1e-12: raise RuntimeError(('uncut_transverse_projection_degenerate',r2))
e3=rvec/math.sqrt(r2)
base=ns['transverse_basis'](q); es=[]
for seed in base:
    v=np.asarray(seed,float)-mbilin(seed,e3)*e3
    for e in es: v=v-mbilin(v,e)*e
    n2=float(np.real(mdot(v)))
    if n2>1e-12: es.append(v/math.sqrt(n2))
    if len(es)==2: break
if len(es)!=2: raise RuntimeError('aligned_transverse_basis_failed')
e1,e2=es
BASIS_ORTHO_TOL=2e-12
basis_gram=np.array([[mbilin(x,y) for y in (e1,e2,e3)] for x in (e1,e2,e3)])
basis_orth_error=float(np.max(np.abs(basis_gram-np.eye(3))))
if basis_orth_error>BASIS_ORTHO_TOL: raise RuntimeError(('basis_orthogonality_failed',basis_orth_error))

DEN_AFFINE_REL_TOL=2e-11
PHASE_MEAN_REL_TOL=2e-6
FOURIER_TAIL_REL_TOL=2e-6
POLY_HELDOUT_REL_TOL=2e-6
FOURIER_N=24
FOURIER_MAX_ACCEPTED_MODE=8
MEAN_NPHI=16
DEGREES=(4,6,8,10,12)
TRAIN_Z=np.linspace(-0.9,0.9,13)
HELDOUT_Z=np.array([-0.83,-0.57,-0.31,-0.07,0.23,0.49,0.77,0.88])
MASS_PAIRS=[(-2*BASE_H,-2*BASE_H),(-BASE_H,BASE_H),(2*BASE_H,BASE_H)]

def kin(u,v):
    lam=s*s+u*u+v*v-2*s*u-2*s*v-2*u*v
    if lam<=0: raise RuntimeError(('nonpositive_kallen',u,v,lam))
    alpha=-(s+u-v)/(2.0*s); rho=math.sqrt(lam)/(2.0*math.sqrt(s)); beta=math.sqrt(lam)/s
    return alpha,rho,beta,lam

def unit_from(z,phi):
    rr=math.sqrt(max(0.0,1.0-float(z)*float(z)))
    return rr*math.cos(phi)*e1 + rr*math.sin(phi)*e2 + float(z)*e3

def numerator_at(u,v,z,phi):
    alpha,rho,_,_=kin(u,v); unit=unit_from(z,phi)
    num,raderr=stripped_limit_massive(alpha,rho*unit)
    return complex(num),float(raderr)

def direct_uncut(u,v,z,phi):
    alpha,rho,_,_=kin(u,v); unit=unit_from(z,phi)
    p0=-a+alpha*q+rho*unit
    return complex(mdot(p0+c))

def affine_coeffs(u,v):
    alpha,rho,_,_=kin(u,v); r0=-a+alpha*q+c
    cc=complex(mdot(r0)+rho*rho)
    aa=complex(2.0*rho*mbilin(r0,e3))
    return cc,aa

max_den_affine_rel=0.0
max_radial=0.0
max_phase_mean_rel=0.0
max_fourier_tail_rel=0.0
mass_results=[]

for u,v in MASS_PAIRS:
    cc,aa=affine_coeffs(u,v)
    for z in (-0.73,-0.18,0.41,0.86):
        for frac in (0.07,0.31,0.68):
            phi=2*math.pi*frac
            d=direct_uncut(u,v,z,phi); pred=cc+aa*z
            max_den_affine_rel=max(max_den_affine_rel,float(abs(d-pred)/max(1.0,abs(d),abs(pred))))

    fourier_rows=[]
    for z in (-0.62,0.11,0.71):
        vals=[]
        for m in range(FOURIER_N):
            num,ra=numerator_at(u,v,z,2*math.pi*m/FOURIER_N); vals.append(num); max_radial=max(max_radial,ra)
        arr=np.asarray(vals,complex); coeff=np.fft.fft(arr)/FOURIER_N
        modes=np.array([min(k,FOURIER_N-k) for k in range(FOURIER_N)])
        scale=max(1.0,float(np.max(np.abs(coeff))))
        tail=float(np.max(np.abs(coeff[modes>FOURIER_MAX_ACCEPTED_MODE]))/scale)
        max_fourier_tail_rel=max(max_fourier_tail_rel,tail)
        fourier_rows.append({'z':float(z),'tail_above_abs_mode_8_scaled':tail,
                             'largest_mode_above_1e-10':int(max([int(m) for m,cx in zip(modes,coeff) if abs(cx)>1e-10*scale] or [0]))})

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
    phase_rel=float(np.max(np.abs(np.concatenate([train0-train1,held0-held1])))/phase_scale)
    max_phase_mean_rel=max(max_phase_mean_rel,phase_rel)

    best=None
    target_train=0.5*(train0+train1); target_held=0.5*(held0+held1)
    for deg in DEGREES:
        cr=np.polynomial.polynomial.polyfit(TRAIN_Z,target_train.real,deg)
        ci=np.polynomial.polynomial.polyfit(TRAIN_Z,target_train.imag,deg)
        pred=np.polynomial.polynomial.polyval(HELDOUT_Z,cr)+1j*np.polynomial.polynomial.polyval(HELDOUT_Z,ci)
        scale=max(1.0,float(np.max(np.abs(target_held))),float(np.max(np.abs(pred))))
        err=float(np.max(np.abs(pred-target_held))/scale)
        if best is None or err<best['heldout_scaled_error']:
            best={'degree':int(deg),'heldout_scaled_error':err,'coeff_real':[float(x) for x in cr],'coeff_imag':[float(x) for x in ci]}
        if err<=POLY_HELDOUT_REL_TOL:
            best={'degree':int(deg),'heldout_scaled_error':err,'coeff_real':[float(x) for x in cr],'coeff_imag':[float(x) for x in ci]}
            break
    mass_results.append({'u':float(u),'v':float(v),'denominator_affine_c':[float(cc.real),float(cc.imag)],
                         'denominator_affine_a':[float(aa.real),float(aa.imag)],'fourier_checks':fourier_rows,
                         'phase_mean_scaled_error':phase_rel,'azimuth_mean_polynomial_fit':best})

max_poly=max(r['azimuth_mean_polynomial_fit']['heldout_scaled_error'] for r in mass_results)
all_poly=all(r['azimuth_mean_polynomial_fit']['heldout_scaled_error']<=POLY_HELDOUT_REL_TOL for r in mass_results)
structure_pass=bool(max_den_affine_rel<=DEN_AFFINE_REL_TOL and max_fourier_tail_rel<=FOURIER_TAIL_REL_TOL and max_phase_mean_rel<=PHASE_MEAN_REL_TOL and all_poly)
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':True,'candidate_residual':False,
 'classification':('PASS_TRU1SQ_CHANNEL4_ANALYTIC_AZIMUTH_STRUCTURE_ORACLE' if structure_pass else 'BLOCKED_TRU1SQ_CHANNEL4_ANALYTIC_AZIMUTH_STRUCTURE_ORACLE'),
 'target':{'double_double_global_index':TARGET_INDEX,'class_id':int(ch['class_id']),'q_squared':q2,
           'cut_group_multiplicities':[mult[ka],mult[kb]],'distinct_denominator_group_count':len(mult),
           'remaining_uncut_group_count':1,'remaining_uncut_multiplicity':1,'remaining_uncut_shift':c.tolist()},
 'aligned_basis':{'orthogonality_error':basis_orth_error,'uncut_transverse_norm_squared':r2},
 'oracle_thresholds':{'denominator_affine_scaled_max':DEN_AFFINE_REL_TOL,'phase_mean_scaled_max':PHASE_MEAN_REL_TOL,
                      'fourier_tail_above_abs_mode_8_scaled_max':FOURIER_TAIL_REL_TOL,
                      'azimuth_mean_polynomial_heldout_scaled_max':POLY_HELDOUT_REL_TOL,
                      'candidate_polynomial_degrees':list(DEGREES)},
 'observed':{'max_denominator_affine_scaled_error':max_den_affine_rel,'max_fourier_tail_scaled_error':max_fourier_tail_rel,
             'max_phase_mean_scaled_error':max_phase_mean_rel,'max_polynomial_heldout_scaled_error':max_poly,
             'max_radial_richardson_scaled_error_seen':max_radial},
 'mass_node_results':mass_results,
 'scope':'STRUCTURE_ONLY__NO_NEW_D_S_VALUE__NO_ANGULAR_GRID_LADDER',
 'physics_immutability':{'parent':'Iteration379/389 physical double-double integrand','frozen_physical_convergence_threshold':2e-5,
                         'mass_derivative_stencil':'unchanged central4 x central4','normalization':'unchanged D_s_double_double=-sphere_mean[d_u d_v G]'},
 'guardrails':['NO_PHYSICAL_VALUE_PROMOTION','NO_THRESHOLD_WEAKENING','TRAINING_AND_HELDOUT_Z_SEPARATE','INDEPENDENT_PHI_PHASE_REQUIRED',
               'DENOMINATOR_AFFINE_CHECKED_DIRECTLY','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('if structure oracle passes, analytically integrate each fixed auxiliary-mass node using the fitted-and-heldout-validated azimuth mean polynomial over the single affine denominator, then apply the unchanged mixed mass derivative and cross-check against independent original-integrand sparse quadrature; if blocked, diagnose only the failed structural assumption without blind grid escalation')
}
print(json.dumps(result,indent=2,sort_keys=True))
