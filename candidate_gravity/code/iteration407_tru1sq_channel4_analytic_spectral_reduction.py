#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 407.

Prospectively frozen analytic/spectral fixed-mass reduction for the unresolved
Tr(U1^2) double-double global index 4, following raw PASS of Iteration 401.

This gate keeps the Iteration-379/389 physical integrand, central4 x central4
auxiliary-mass stencil, D_s(double-double)=-sphere_mean[d_u d_v G], and the
physical 2e-5 convergence threshold unchanged.  The only replacement is the
angular evaluation: the azimuth mean of the stripped numerator is fit at fixed
mass to the degree-4 polynomial structure validated by Iteration 401, and the
remaining z integral over the single affine uncut denominator is performed
analytically.  Every mass node is fail-closed on held-out z values.  Selected
mass nodes are independently cross-checked against the original integrand by
sparse direct sphere quadrature.
"""
from __future__ import annotations
import contextlib, io, json, math, time
from pathlib import Path
import numpy as np

ITERATION=407
TARGET_INDEX=4
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration379_tru1sq_double_double_one_channel_pilot.py'
src=PARENT.read_text(); marker='start=time.perf_counter()'
if src.count(marker)!=1: raise RuntimeError('iteration379_run_marker_drift')
ns={'__name__':'iteration407_parent379_prefix','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split(marker,1)[0],str(PARENT),'exec'),ns,ns)

P372=ns['P372']; rows=ns['rows']; vk=ns['vk']; mdot=ns['mdot']; BASE_H=ns['BASE_H']; HALF_H=ns['HALF_H']
ANGULAR_CONVERGENCE_TOL=ns['ANGULAR_CONVERGENCE_TOL']; CUT_SHELL_TOL=ns['CUT_SHELL_TOL']; UNCUT_MIN_TOL=ns['UNCUT_MIN_TOL']; RADIAL_EXTRAP_TOL=ns['RADIAL_EXTRAP_TOL']
central4=ns['central4']; stripped_limit_massive=ns['stripped_limit_massive']
parent374=ns['ns']; mbilin=parent374['mbilin']; mproj_orth=parent374['mproj_orth']

dd=[c for c in P372['channels'] if c['singularity_type']=='double-double']
if len(dd)!=15: raise RuntimeError(('double_double_census_drift',len(dd)))
ch=dd[TARGET_INDEX]; row=rows[int(ch['class_id'])]
a=np.asarray(ch['shift_i'],float); b=np.asarray(ch['shift_j'],float); q=b-a
q2=float(np.real(mdot(q))); s=-q2
if int(ch['class_id'])!=5 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))

mult={}; reps={}
for sh in row['shifts']:
    k=vk(sh); mult[k]=mult.get(k,0)+1; reps[k]=np.asarray(sh,float)
ka,kb=vk(a),vk(b)
if mult.get(ka)!=2 or mult.get(kb)!=2: raise RuntimeError(('cut_multiplicity_drift',mult.get(ka),mult.get(kb)))
uncut=[k for k in mult if k not in (ka,kb)]
if len(uncut)!=1 or mult[uncut[0]]!=1: raise RuntimeError(('one_simple_uncut_required',mult))
c=reps[uncut[0]]

rvec=mproj_orth(c-a,q); r2=float(np.real(mdot(rvec)))
if r2<=1e-12: raise RuntimeError(('uncut_transverse_projection_degenerate',r2))
e3=rvec/math.sqrt(r2); base=ns['transverse_basis'](q); es=[]
for seed in base:
    v=np.asarray(seed,float)-mbilin(seed,e3)*e3
    for e in es: v=v-mbilin(v,e)*e
    n2=float(np.real(mdot(v)))
    if n2>1e-12: es.append(v/math.sqrt(n2))
    if len(es)==2: break
if len(es)!=2: raise RuntimeError('aligned_transverse_basis_failed')
e1,e2=es
basis_gram=np.array([[mbilin(x,y) for y in (e1,e2,e3)] for x in (e1,e2,e3)])
basis_orth_error=float(np.max(np.abs(basis_gram-np.eye(3))))
if basis_orth_error>2e-12: raise RuntimeError(('basis_orthogonality_failed',basis_orth_error))

POLY_DEGREE=4
TRAIN_Z=np.array([-0.86,-0.43,0.0,0.43,0.86])
HELDOUT_Z=np.array([-0.71,-0.19,0.27,0.69])
MEAN_NPHI=16
POLY_HELDOUT_REL_TOL=2e-6
DEN_AFFINE_REL_TOL=2e-11
DIRECT_CROSSCHECK_REL_TOL=2e-6
CROSSCHECK_MASS_PAIRS=[(-2*BASE_H,-2*BASE_H),(-BASE_H,BASE_H),(2*BASE_H,BASE_H)]
DIRECT_NZ=6; DIRECT_NPHI=12

def kin(u,v):
    lam=s*s+u*u+v*v-2*s*u-2*s*v-2*u*v
    if lam<=0: raise RuntimeError(('nonpositive_kallen',u,v,lam))
    alpha=-(s+u-v)/(2.0*s); rho=math.sqrt(lam)/(2.0*math.sqrt(s)); beta=math.sqrt(lam)/s
    return alpha,rho,beta,lam

def unit_from(z,phi):
    rr=math.sqrt(max(0.0,1.0-float(z)*float(z)))
    return rr*math.cos(phi)*e1+rr*math.sin(phi)*e2+float(z)*e3

def numerator_at(u,v,z,phi):
    alpha,rho,_,_=kin(u,v); num,raderr=stripped_limit_massive(alpha,rho*unit_from(z,phi))
    return complex(num),float(raderr)

def affine_coeffs(u,v):
    alpha,rho,_,_=kin(u,v); r0=-a+alpha*q+c
    cc=complex(mdot(r0)+rho*rho); aa=complex(2.0*rho*mbilin(r0,e3))
    return cc,aa

def direct_uncut(u,v,z,phi):
    alpha,rho,_,_=kin(u,v); p0=-a+alpha*q+rho*unit_from(z,phi)
    return complex(mdot(p0+c))

def phi_mean_num(u,v,z):
    vals=[]; maxrad=0.0
    for m in range(MEAN_NPHI):
        num,ra=numerator_at(u,v,z,2*math.pi*m/MEAN_NPHI); vals.append(num); maxrad=max(maxrad,ra)
    return sum(vals,0j)/MEAN_NPHI,maxrad

def integral_monomials_over_affine(cc,aa,degree):
    if abs(aa)<1e-14:
        return [complex((0.0 if k%2 else 2.0/(k+1))/cc) for k in range(degree+1)]
    if min(abs(cc-aa),abs(cc+aa))<=UNCUT_MIN_TOL: raise RuntimeError(('analytic_endpoint_uncut_too_small',cc,aa))
    out=[(np.log(cc+aa)-np.log(cc-aa))/aa]
    for k in range(1,degree+1):
        im1=0.0 if (k-1)%2 else 2.0/k
        out.append((im1-cc*out[-1])/aa)
    return out

def analytic_sphere_G(u,v):
    cc,aa=affine_coeffs(u,v); alpha,rho,beta,lam=kin(u,v)
    maxden=0.0
    for z in (-0.73,-0.18,0.41,0.86):
        for frac in (0.07,0.31,0.68):
            d=direct_uncut(u,v,z,2*math.pi*frac); p=cc+aa*z
            maxden=max(maxden,float(abs(d-p)/max(1.0,abs(d),abs(p))))
    train=[]; held=[]; maxrad=0.0
    for z in TRAIN_Z:
        x,ra=phi_mean_num(u,v,float(z)); train.append(x); maxrad=max(maxrad,ra)
    for z in HELDOUT_Z:
        x,ra=phi_mean_num(u,v,float(z)); held.append(x); maxrad=max(maxrad,ra)
    train=np.asarray(train,complex); held=np.asarray(held,complex)
    cr=np.polynomial.polynomial.polyfit(TRAIN_Z,train.real,POLY_DEGREE)
    ci=np.polynomial.polynomial.polyfit(TRAIN_Z,train.imag,POLY_DEGREE)
    pred=np.polynomial.polynomial.polyval(HELDOUT_Z,cr)+1j*np.polynomial.polynomial.polyval(HELDOUT_Z,ci)
    scale=max(1.0,float(np.max(np.abs(held))),float(np.max(np.abs(pred))))
    polyerr=float(np.max(np.abs(pred-held))/scale)
    if maxden>DEN_AFFINE_REL_TOL or polyerr>POLY_HELDOUT_REL_TOL or maxrad>RADIAL_EXTRAP_TOL:
        raise RuntimeError(('fixed_mass_structure_blocked',u,v,maxden,polyerr,maxrad))
    coeff=cr+1j*ci; js=integral_monomials_over_affine(cc,aa,POLY_DEGREE)
    sphere=0.5*beta*sum(complex(coeff[k])*js[k] for k in range(POLY_DEGREE+1))
    endpoint_min=min(abs(cc-aa),abs(cc+aa))
    return sphere,{'u':float(u),'v':float(v),'poly_heldout_scaled_error':polyerr,'den_affine_scaled_error':maxden,
                   'max_radial_richardson_scaled_error':maxrad,'minimum_analytic_uncut_abs_denominator':float(endpoint_min),
                   'minimum_kallen':float(lam),'poly_coeff_real':[float(x) for x in cr],'poly_coeff_imag':[float(x) for x in ci]}

def direct_sparse_sphere_G(u,v):
    zs,ws=np.polynomial.legendre.leggauss(DIRECT_NZ); total=0j; maxrad=0.0; minunc=float('inf')
    alpha,rho,beta,_=kin(u,v)
    for z,w in zip(zs,ws):
        rowv=0j
        for m in range(DIRECT_NPHI):
            phi=2*math.pi*(m+0.317)/DIRECT_NPHI; unit=unit_from(float(z),phi)
            num,ra=stripped_limit_massive(alpha,rho*unit); maxrad=max(maxrad,ra)
            p0=-a+alpha*q+rho*unit; den=complex(mdot(p0+c)); minunc=min(minunc,abs(den)); rowv+=beta*num/den
        total+=float(w)*(rowv/DIRECT_NPHI)
    return 0.5*total,maxrad,minunc

def derivative_from_analytic(h):
    nodes=[-2*h,-h,h,2*h]; vals=np.empty((4,4),complex); diagnostics=[]
    for i,u in enumerate(nodes):
        for j,v in enumerate(nodes): vals[i,j],d=analytic_sphere_G(u,v); diagnostics.append(d)
    first=np.array([central4(vals[:,j],h) for j in range(4)],complex)
    return central4(first,h),diagnostics

start=time.perf_counter()
d_base,diag_base=derivative_from_analytic(BASE_H)
d_half,diag_half=derivative_from_analytic(HALF_H)
scaled_step_error=float(abs(d_base-d_half)/max(1.0,abs(d_base),abs(d_half)))

cross=[]; maxcross=0.0
for u,v in CROSSCHECK_MASS_PAIRS:
    av,_=analytic_sphere_G(u,v); dv,ra,un=direct_sparse_sphere_G(u,v)
    er=float(abs(av-dv)/max(1.0,abs(av),abs(dv))); maxcross=max(maxcross,er)
    cross.append({'u':float(u),'v':float(v),'analytic_sphere_G':[float(av.real),float(av.imag)],
                  'direct_sparse_sphere_G':[float(dv.real),float(dv.imag)],'scaled_error':er,
                  'direct_max_radial_richardson_scaled_error':float(ra),'direct_minimum_sampled_uncut_abs_denominator':float(un)})

all_diag=diag_base+diag_half
maxpoly=max(d['poly_heldout_scaled_error'] for d in all_diag)
maxden=max(d['den_affine_scaled_error'] for d in all_diag)
maxrad=max(d['max_radial_richardson_scaled_error'] for d in all_diag)
minunc=min(d['minimum_analytic_uncut_abs_denominator'] for d in all_diag)
minlam=min(d['minimum_kallen'] for d in all_diag)
execution_valid=bool(maxpoly<=POLY_HELDOUT_REL_TOL and maxden<=DEN_AFFINE_REL_TOL and maxrad<=RADIAL_EXTRAP_TOL and minunc>UNCUT_MIN_TOL and minlam>0 and maxcross<=DIRECT_CROSSCHECK_REL_TOL)
status='CONVERGED' if execution_valid and scaled_step_error<=ANGULAR_CONVERGENCE_TOL else 'BLOCKED_CONVERGENCE'
ds=-d_base
runtime=time.perf_counter()-start
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
 'classification':('PASS_TRU1SQ_CHANNEL4_ANALYTIC_SPECTRAL_REDUCTION__CONVERGED' if status=='CONVERGED' else
                   'PASS_TRU1SQ_CHANNEL4_ANALYTIC_SPECTRAL_REDUCTION__BLOCKED_CONVERGENCE' if execution_valid else
                   'FAIL_TRU1SQ_CHANNEL4_ANALYTIC_SPECTRAL_REDUCTION_EXECUTION'),
 'channel':{'double_double_global_index':TARGET_INDEX,'class_id':int(ch['class_id']),'q_squared':q2,'status':status,
            'D_s_TrU1sq_double_double_channel':[float(ds.real),float(ds.imag)],
            'mixed_derivative_base_h':[float(d_base.real),float(d_base.imag)],'mixed_derivative_halfstep_h':[float(d_half.real),float(d_half.imag)],
            'scaled_mass_step_convergence_error':scaled_step_error},
 'structure_observed':{'max_polynomial_heldout_scaled_error':maxpoly,'max_denominator_affine_scaled_error':maxden,
                       'max_radial_richardson_scaled_error':maxrad,'minimum_analytic_uncut_abs_denominator':minunc,'minimum_kallen':minlam,
                       'max_direct_original_integrand_crosscheck_scaled_error':maxcross,'aligned_basis_orthogonality_error':basis_orth_error},
 'direct_original_integrand_crosschecks':cross,'runtime_seconds':float(runtime),
 'frozen_reduction':{'azimuth_mean_polynomial_degree':POLY_DEGREE,'training_z':TRAIN_Z.tolist(),'heldout_z':HELDOUT_Z.tolist(),
                     'phi_nodes_for_mean':MEAN_NPHI,'mass_stencil':'central4 x central4 unchanged','base_h':BASE_H,'halfstep_h':HALF_H,
                     'z_integral':'analytic monomial recurrence over one affine denominator'},
 'thresholds':{'physical_convergence_scaled_max':ANGULAR_CONVERGENCE_TOL,'polynomial_heldout_scaled_max':POLY_HELDOUT_REL_TOL,
               'denominator_affine_scaled_max':DEN_AFFINE_REL_TOL,'direct_original_integrand_crosscheck_scaled_max':DIRECT_CROSSCHECK_REL_TOL,
               'radial_richardson_scaled_max':RADIAL_EXTRAP_TOL,'uncut_abs_min':UNCUT_MIN_TOL},
 'effective_action_weight':'NOT_FOLDED__MINUS_I_OVER_4_TRU1SQ_SEPARATE',
 'scope':'CHANNEL4_ONLY__ANALYTIC_SPECTRAL_REDUCTION_AFTER_ITERATION401_STRUCTURE_PASS',
 'guardrails':['ITERATION401_STRUCTURE_PASS_REQUIRED','ITERATION403_STENCIL_COMMUTATION_BINDING','NO_THRESHOLD_WEAKENING','NO_BLIND_GRID_ESCALATION',
               'HELDOUT_ORIGINAL_INTEGRAND_CROSSCHECK','DISTINCT_Q2_BUCKETS_NEVER_SUMMED','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('if CONVERGED and raw authority audit passes, replace only double-double blocker index 4 and apply the same prospectively frozen analytic/spectral architecture separately to unresolved indices 2 and 11 with their own held-out checks; if BLOCKED, preserve it and diagnose the failed fixed-mass representation or mass-step convergence without weakening thresholds')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid: raise SystemExit(2)
