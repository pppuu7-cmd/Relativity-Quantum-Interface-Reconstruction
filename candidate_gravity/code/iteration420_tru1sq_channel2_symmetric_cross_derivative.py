#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 420.

Prospectively frozen better-conditioned auxiliary-mass mixed-derivative
representation for the sole remaining Tr(U1^2) double-double blocker,
global index 2 / class 3 / q^2=-1.

This gate is frozen while Iteration 419 is still running and therefore does not
use its numerical outcome.  It does not shrink the mass step, change the
physical integrand, angular representation, sign, normalization, or any frozen
scientific threshold.

For the already-validated fixed-mass analytic sphere function F(u,v), use the
symmetric cross quotient

 C(u,v)=[F(u,v)-F(u,-v)-F(-u,v)+F(-u,-v)]/(4uv)
       = F_uv(0,0)+O(u^2+v^2).

The largest radius is the already-used/certified auxiliary-mass envelope
R=1e-5.  Dimensionless squared radii make the extrapolation well-conditioned.
A tensor degree-(2,2) fit, a tensor degree-(1,1) fit, an inner-radius degree-
(1,1) fit, and an independent diagonal-in-radius quadratic extrapolation must
all agree under the unchanged physical 2e-5 scaled threshold before any
physical promotion.  Every fixed-mass node retains the Iteration-407 structural
checks and selected nodes retain the original-integrand sparse cross-check.
"""
from __future__ import annotations
import contextlib, io, json, math, time
from pathlib import Path
import numpy as np

ITERATION=420
TARGET_INDEX=2
EXPECTED_CLASS=3
EXPECTED_Q2=-1.0
RADIUS=1.0e-5
RADII_MULT=np.array([1.0,0.75,0.5,0.25],float)
PHYSICAL_TOL=2.0e-5
DESIGN_COND_MAX=1.0e3
SYNTHETIC_TOL=1.0e-12

root=Path(__file__).resolve().parent
parent=root/'iteration407_tru1sq_channel4_analytic_spectral_reduction.py'
src=parent.read_text()
for old,new in [
    ('ITERATION=407','ITERATION=420'),
    ('TARGET_INDEX=4','TARGET_INDEX=2'),
    ("if int(ch['class_id'])!=5 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))",
     "if int(ch['class_id'])!=3 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))"),
]:
    if src.count(old)!=1: raise RuntimeError(('iteration407_specialization_drift',old,src.count(old)))
    src=src.replace(old,new,1)
marker="\nstart=time.perf_counter()\nd_base,diag_base=derivative_from_analytic(BASE_H)"
if src.count(marker)!=1: raise RuntimeError(('iteration407_execution_boundary_drift',src.count(marker)))
prefix=src.split(marker,1)[0]+'\n'
ns={'__name__':'iteration420_parent407_prefix','__file__':str(parent)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix,str(parent),'exec'),ns,ns)

analytic_sphere_G=ns['analytic_sphere_G']; direct_sparse_sphere_G=ns['direct_sparse_sphere_G']
ch=ns['ch']; q2=float(ns['q2'])
if int(ch['class_id'])!=EXPECTED_CLASS or abs(q2-EXPECTED_Q2)>1e-12:
    raise RuntimeError(('target_identity_drift_after_exec',ch['class_id'],q2))
if abs(float(ns['ANGULAR_CONVERGENCE_TOL'])-PHYSICAL_TOL)>1e-18:
    raise RuntimeError(('physical_threshold_drift',ns['ANGULAR_CONVERGENCE_TOL']))

cache={}; all_diag=[]
def F(u,v):
    key=(float(u),float(v))
    if key not in cache:
        val,diag=analytic_sphere_G(*key); cache[key]=complex(val); all_diag.append(diag)
    return cache[key]

def fsum_complex(terms):
    return complex(math.fsum(complex(x).real for x in terms),math.fsum(complex(x).imag for x in terms))

def cross_ratio(r,s):
    num=fsum_complex([F(r,s),-F(r,-s),-F(-r,s),F(-r,-s)])
    return num/(4.0*r*s)

def design(points,degree):
    return np.asarray([[x**i*y**j for i in range(degree+1) for j in range(degree+1)] for x,y,_ in points],float)

def fit_intercept(points,degree):
    X=design(points,degree); y=np.asarray([z for _,_,z in points],complex)
    cr=np.linalg.lstsq(X,y.real,rcond=None)[0]; ci=np.linalg.lstsq(X,y.imag,rcond=None)[0]
    pred=X@cr+1j*(X@ci)
    resid=float(np.max(np.abs(pred-y))/max(1.0,float(np.max(np.abs(y))),float(np.max(np.abs(pred)))))
    return complex(cr[0],ci[0]),resid,float(np.linalg.cond(X))

# Synthetic exact-recovery oracle on the identical design.  The mixed derivative
# is the intercept of C(x,y); use a represented tensor-(2,2) polynomial.
def synthetic_oracle():
    syn=[]
    for mr in RADII_MULT:
        for ms in RADII_MULT:
            x=float(mr*mr); y=float(ms*ms)
            c=0.3141592653589793 + 0.17*x -0.09*y +0.04*x*y +0.013*x*x -0.021*y*y +0.007*x*x*y -0.005*x*y*y +0.003*x*x*y*y
            syn.append((x,y,complex(c,0.0)))
    z,res,cond=fit_intercept(syn,2)
    err=float(abs(z-0.3141592653589793))
    return {'recovered_intercept':float(z.real),'absolute_error':err,'fit_residual_scaled':res,'design_condition_number':cond}

start=time.perf_counter()
points=[]
for mr in RADII_MULT:
    for ms in RADII_MULT:
        r=float(RADIUS*mr); s=float(RADIUS*ms)
        points.append((float(mr*mr),float(ms*ms),cross_ratio(r,s)))

intercept22,res22,cond22=fit_intercept(points,2)
intercept11,res11,cond11=fit_intercept(points,1)
inner=[p for p in points if p[0] < 1.0-1e-15 and p[1] < 1.0-1e-15]
intercept11_inner,res11_inner,cond11_inner=fit_intercept(inner,1)

# Independent diagonal C(r,r) extrapolation in t=(r/R)^2 through quadratic.
diag_pts=[]
for mr in RADII_MULT:
    t=float(mr*mr); z=next(p[2] for p in points if abs(p[0]-t)<1e-15 and abs(p[1]-t)<1e-15)
    diag_pts.append((t,z))
Xd=np.asarray([[1.0,t,t*t] for t,_ in diag_pts],float); yd=np.asarray([z for _,z in diag_pts],complex)
cdr=np.linalg.lstsq(Xd,yd.real,rcond=None)[0]; cdi=np.linalg.lstsq(Xd,yd.imag,rcond=None)[0]
intercept_diag=complex(cdr[0],cdi[0]); pred_d=Xd@cdr+1j*(Xd@cdi)
diag_res=float(np.max(np.abs(pred_d-yd))/max(1.0,float(np.max(np.abs(yd))),float(np.max(np.abs(pred_d)))))
cond_diag=float(np.linalg.cond(Xd))

scale=max(1.0,abs(intercept22),abs(intercept11),abs(intercept11_inner),abs(intercept_diag))
stability={
 'deg22_vs_deg11':float(abs(intercept22-intercept11)/scale),
 'deg22_vs_inner_deg11':float(abs(intercept22-intercept11_inner)/scale),
 'deg22_vs_diagonal':float(abs(intercept22-intercept_diag)/scale),
}
max_stability=max(stability.values())

# Frozen parent structural checks over every actual fixed-mass evaluation.
maxpoly=float(max(d['poly_heldout_scaled_error'] for d in all_diag)); maxden=float(max(d['den_affine_scaled_error'] for d in all_diag))
maxrad=float(max(d['max_radial_richardson_scaled_error'] for d in all_diag)); minunc=float(min(d['minimum_analytic_uncut_abs_denominator'] for d in all_diag)); minlam=float(min(d['minimum_kallen'] for d in all_diag))

# Independent original-integrand checks at prospectively selected nodes.
crosschecks=[]; maxcross=0.0
for mr,ms in ((1.0,1.0),(1.0,-0.75),(-0.5,0.25)):
    u=RADIUS*mr; v=RADIUS*ms; av=F(u,v); dv,ra,un=direct_sparse_sphere_G(u,v)
    er=float(abs(av-dv)/max(1.0,abs(av),abs(dv))); maxcross=max(maxcross,er)
    crosschecks.append({'u':u,'v':v,'analytic_sphere_G':[float(av.real),float(av.imag)],'direct_sparse_sphere_G':[float(dv.real),float(dv.imag)],'scaled_error':er,'direct_max_radial_richardson_scaled_error':float(ra),'direct_minimum_sampled_uncut_abs_denominator':float(un)})

syn=synthetic_oracle()
max_fit_res=max(res22,res11_inner,diag_res)
max_cond=max(cond22,cond11,cond11_inner,cond_diag,syn['design_condition_number'])
structure_ok=bool(maxpoly<=2e-6 and maxden<=2e-11 and maxrad<=ns['RADIAL_EXTRAP_TOL'] and minunc>ns['UNCUT_MIN_TOL'] and minlam>0.0 and maxcross<=2e-6)
method_ok=bool(syn['absolute_error']<=SYNTHETIC_TOL and max_cond<=DESIGN_COND_MAX)
physical_stability_ok=bool(max_stability<=PHYSICAL_TOL and max_fit_res<=PHYSICAL_TOL)
execution_valid=bool(structure_ok and method_ok)
status='CONVERGED' if execution_valid and physical_stability_ok else 'BLOCKED_CONVERGENCE'
ds=-intercept22
result={
 'iteration':ITERATION,'model_readiness_percent':24,'candidate_residual':False,'scientific_gate_pass':execution_valid,
 'classification':('PASS_TRU1SQ_CHANNEL2_SYMMETRIC_CROSS_DERIVATIVE__CONVERGED' if status=='CONVERGED' else 'PASS_TRU1SQ_CHANNEL2_SYMMETRIC_CROSS_DERIVATIVE__BLOCKED_CONVERGENCE' if execution_valid else 'FAIL_TRU1SQ_CHANNEL2_SYMMETRIC_CROSS_DERIVATIVE_EXECUTION'),
 'channel':{'double_double_global_index':TARGET_INDEX,'class_id':int(ch['class_id']),'q_squared':q2,'status':status,'D_s_TrU1sq_double_double_channel':[float(ds.real),float(ds.imag)] if status=='CONVERGED' else None,'diagnostic_D_s_not_authority':[float(ds.real),float(ds.imag)] if status!='CONVERGED' else None},
 'representation':{'formula':'[F(u,v)-F(u,-v)-F(-u,v)+F(-u,-v)]/(4uv)','radius':RADIUS,'radius_multipliers':RADII_MULT.tolist(),'primary_fit':'dimensionless tensor degree (2,2); physical intercept=-D_s','node_count':len(cache)},
 'intercepts':{'tensor22':[float(intercept22.real),float(intercept22.imag)],'tensor11':[float(intercept11.real),float(intercept11.imag)],'inner_tensor11':[float(intercept11_inner.real),float(intercept11_inner.imag)],'diagonal_quadratic':[float(intercept_diag.real),float(intercept_diag.imag)]},
 'stability_scaled':stability,'max_stability_scaled':float(max_stability),'fit_residuals_scaled':{'tensor22':res22,'tensor11':res11,'inner_tensor11':res11_inner,'diagonal_quadratic':diag_res},'max_required_fit_residual_scaled':float(max_fit_res),
 'design_condition_numbers':{'tensor22':cond22,'tensor11':cond11,'inner_tensor11':cond11_inner,'diagonal':cond_diag},'max_design_condition_number':float(max_cond),'synthetic_oracle':syn,
 'structure_observed':{'max_polynomial_heldout_scaled_error':maxpoly,'max_denominator_affine_scaled_error':maxden,'max_radial_richardson_scaled_error':maxrad,'minimum_analytic_uncut_abs_denominator':minunc,'minimum_kallen':minlam,'max_direct_original_integrand_crosscheck_scaled_error':maxcross},
 'direct_original_integrand_crosschecks':crosschecks,'runtime_seconds':float(time.perf_counter()-start),
 'thresholds':{'physical_stability_scaled_max':PHYSICAL_TOL,'fit_residual_scaled_max':PHYSICAL_TOL,'design_condition_number_max':DESIGN_COND_MAX,'synthetic_absolute_error_max':SYNTHETIC_TOL,'polynomial_heldout_scaled_max':2e-6,'denominator_affine_scaled_max':2e-11,'direct_original_integrand_crosscheck_scaled_max':2e-6,'radial_richardson_scaled_max':ns['RADIAL_EXTRAP_TOL'],'uncut_abs_min':ns['UNCUT_MIN_TOL']},
 'effective_action_weight':'NOT_FOLDED__MINUS_I_OVER_4_TRU1SQ_SEPARATE',
 'guardrails':['FROZEN_BEFORE_ITERATION419_RESULT','NO_SMALLER_MASS_STEP','NO_ANGULAR_GRID_ESCALATION','NO_THRESHOLD_WEAKENING','NO_ZERO_FILL','ITERATION377_407_STRUCTURAL_ENVELOPE_FAIL_CLOSED','HELDOUT_ORIGINAL_INTEGRAND_CROSSCHECK','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('if CONVERGED and raw authority audit passes, replace only double-double index 2 and execute frozen Iteration412 exact15 assembly; if BLOCKED, preserve index 2 and move to true higher-precision/factorized node evaluation rather than further finite-difference shrinking')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid: raise SystemExit(2)
