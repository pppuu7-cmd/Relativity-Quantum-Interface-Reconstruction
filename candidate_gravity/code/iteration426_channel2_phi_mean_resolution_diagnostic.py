#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 426.

Diagnostic-only phi-mean resolution audit for the sole unresolved Tr(U1^2)
double-double channel 2 / class 3 / q^2=-1.

Iteration 419 excluded summation-level binary64 cancellation as a material
explanation of the observed mass-step drift, and Iteration 422 excluded the
affine analytic moments / degree-4 interpolation geometry as dominant arithmetic
sources.  This gate isolates the remaining fixed-mass phi-mean layer without
changing the physical gate: the frozen degree-4 representation is evaluated at
16 and 32 equispaced phi nodes on the same signed symmetric-cross corners at
R=1e-5 and R/2.  The prospectively frozen materiality threshold is the unchanged
physical 2e-5 scaled tolerance.

This iteration is diagnostic only.  It promotes no D_s coordinate and cannot
replace Iteration 421 or the prospectively frozen Iteration 424 fallback.
"""
from __future__ import annotations
import contextlib, io, json, math, time
from pathlib import Path
import numpy as np

ITERATION=426
TARGET_INDEX=2
EXPECTED_CLASS=3
EXPECTED_Q2=-1.0
RADIUS=1.0e-5
RADII_MULT=(1.0,0.5)
NPHI_BASE=16
NPHI_AUDIT=32
PHYSICAL_TOL=2.0e-5
REPRO_TOL=1.0e-13

root=Path(__file__).resolve().parent
parent=root/'iteration407_tru1sq_channel4_analytic_spectral_reduction.py'
src=parent.read_text()
for old,new in [
    ('ITERATION=407','ITERATION=426'),
    ('TARGET_INDEX=4','TARGET_INDEX=2'),
    ("if int(ch['class_id'])!=5 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))",
     "if int(ch['class_id'])!=3 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))"),
]:
    if src.count(old)!=1:
        raise RuntimeError(('iteration407_specialization_drift',old,src.count(old)))
    src=src.replace(old,new,1)
marker="\nstart=time.perf_counter()\nd_base,diag_base=derivative_from_analytic(BASE_H)"
if src.count(marker)!=1:
    raise RuntimeError(('iteration407_execution_boundary_drift',src.count(marker)))
prefix=src.split(marker,1)[0]+'\n'
ns={'__name__':'iteration426_parent407_prefix','__file__':str(parent)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix,str(parent),'exec'),ns,ns)

ch=ns['ch']; q2=float(ns['q2'])
if int(ch['class_id'])!=EXPECTED_CLASS or abs(q2-EXPECTED_Q2)>1e-12:
    raise RuntimeError(('target_identity_drift_after_exec',ch['class_id'],q2))
if abs(float(ns['ANGULAR_CONVERGENCE_TOL'])-PHYSICAL_TOL)>1e-18:
    raise RuntimeError(('physical_threshold_drift',ns['ANGULAR_CONVERGENCE_TOL']))
if int(ns['MEAN_NPHI'])!=NPHI_BASE:
    raise RuntimeError(('parent_phi_node_count_drift',ns['MEAN_NPHI']))

TRAIN_Z=np.asarray(ns['TRAIN_Z'],float)
HELDOUT_Z=np.asarray(ns['HELDOUT_Z'],float)
POLY_DEGREE=int(ns['POLY_DEGREE'])
numerator_at=ns['numerator_at']; affine_coeffs=ns['affine_coeffs']; kin=ns['kin']
integral_monomials_over_affine=ns['integral_monomials_over_affine']
parent_analytic_sphere_G=ns['analytic_sphere_G']


def phi_mean_num_n(u,v,z,nphi):
    vals=[]; maxrad=0.0
    for m in range(nphi):
        num,ra=numerator_at(u,v,z,2.0*math.pi*m/nphi)
        vals.append(num); maxrad=max(maxrad,float(ra))
    return complex(math.fsum(complex(x).real for x in vals)/nphi,
                   math.fsum(complex(x).imag for x in vals)/nphi),maxrad


def sphere_nphi(u,v,nphi):
    cc,aa=affine_coeffs(u,v); _,_,beta,lam=kin(u,v)
    train=[]; held=[]; maxrad=0.0
    for z in TRAIN_Z:
        x,ra=phi_mean_num_n(u,v,float(z),nphi); train.append(x); maxrad=max(maxrad,ra)
    for z in HELDOUT_Z:
        x,ra=phi_mean_num_n(u,v,float(z),nphi); held.append(x); maxrad=max(maxrad,ra)
    train=np.asarray(train,complex); held=np.asarray(held,complex)
    cr=np.polynomial.polynomial.polyfit(TRAIN_Z,train.real,POLY_DEGREE)
    ci=np.polynomial.polynomial.polyfit(TRAIN_Z,train.imag,POLY_DEGREE)
    pred=np.polynomial.polynomial.polyval(HELDOUT_Z,cr)+1j*np.polynomial.polynomial.polyval(HELDOUT_Z,ci)
    scale=max(1.0,float(np.max(np.abs(held))),float(np.max(np.abs(pred))))
    polyerr=float(np.max(np.abs(pred-held))/scale)
    coeff=cr+1j*ci; js=integral_monomials_over_affine(cc,aa,POLY_DEGREE)
    sphere=0.5*beta*sum(complex(coeff[k])*js[k] for k in range(POLY_DEGREE+1))
    return complex(sphere),{
        'poly_heldout_scaled_error':polyerr,
        'max_radial_richardson_scaled_error':float(maxrad),
        'minimum_analytic_uncut_abs_denominator':float(min(abs(cc-aa),abs(cc+aa))),
        'minimum_kallen':float(lam),
        'poly_coeff_real':[float(x) for x in cr],
        'poly_coeff_imag':[float(x) for x in ci],
    }


def fsum_complex(terms):
    return complex(math.fsum(complex(x).real for x in terms),
                   math.fsum(complex(x).imag for x in terms))

cache={}; diagnostics=[]
def F(u,v,nphi):
    key=(float(u),float(v),int(nphi))
    if key not in cache:
        val,d=sphere_nphi(*key); cache[key]=val
        diagnostics.append({'u':key[0],'v':key[1],'nphi':key[2],**d})
    return cache[key]


def cross_ratio(r,nphi):
    num=fsum_complex([F(r,r,nphi),-F(r,-r,nphi),-F(-r,r,nphi),F(-r,-r,nphi)])
    return num/(4.0*r*r)

start=time.perf_counter()
records=[]; max_cross_delta=0.0
for mr in RADII_MULT:
    r=RADIUS*mr
    c16=cross_ratio(r,NPHI_BASE); c32=cross_ratio(r,NPHI_AUDIT)
    scale=max(1.0,abs(c16),abs(c32))
    delta=float(abs(c16-c32)/scale); max_cross_delta=max(max_cross_delta,delta)
    records.append({
        'radius':float(r),'radius_multiplier':float(mr),
        'cross_ratio_nphi16':[float(c16.real),float(c16.imag)],
        'cross_ratio_nphi32':[float(c32.real),float(c32.imag)],
        'scaled_nphi16_vs_nphi32_delta':delta,
    })

# Exact reproduction oracle: our nphi=16 implementation must reproduce the
# frozen parent evaluator at one preselected corner before the diagnostic is read.
u0=RADIUS; v0=-RADIUS
ours=F(u0,v0,NPHI_BASE); parent_val,parent_diag=parent_analytic_sphere_G(u0,v0)
repro_delta=float(abs(ours-parent_val)/max(1.0,abs(ours),abs(parent_val)))

fixed_pairs={(d['u'],d['v']) for d in diagnostics}
fixed_deltas=[]; max_fixed_delta=0.0
for u,v in sorted(fixed_pairs):
    if (u,v,NPHI_BASE) in cache and (u,v,NPHI_AUDIT) in cache:
        a=cache[(u,v,NPHI_BASE)]; b=cache[(u,v,NPHI_AUDIT)]
        er=float(abs(a-b)/max(1.0,abs(a),abs(b))); max_fixed_delta=max(max_fixed_delta,er)
        fixed_deltas.append({'u':u,'v':v,'scaled_nphi16_vs_nphi32_delta':er})

maxpoly=max(d['poly_heldout_scaled_error'] for d in diagnostics)
maxrad=max(d['max_radial_richardson_scaled_error'] for d in diagnostics)
minunc=min(d['minimum_analytic_uncut_abs_denominator'] for d in diagnostics)
minlam=min(d['minimum_kallen'] for d in diagnostics)
execution_valid=bool(
    repro_delta<=REPRO_TOL and
    maxpoly<=ns['POLY_HELDOUT_REL_TOL'] and
    maxrad<=ns['RADIAL_EXTRAP_TOL'] and
    minunc>ns['UNCUT_MIN_TOL'] and minlam>0.0 and
    len(records)==len(RADII_MULT)
)
phi_material=bool(execution_valid and max_cross_delta>PHYSICAL_TOL)
classification=(
    'PASS_CHANNEL2_PHI_MEAN_RESOLUTION__MATERIAL_DIAGNOSTIC_ONLY' if phi_material else
    'PASS_CHANNEL2_PHI_MEAN_RESOLUTION__STABLE_DIAGNOSTIC_ONLY' if execution_valid else
    'FAIL_CHANNEL2_PHI_MEAN_RESOLUTION_DIAGNOSTIC_EXECUTION'
)
result={
    'iteration':ITERATION,
    'model_readiness_percent':24,
    'candidate_residual':False,
    'scientific_gate_pass':execution_valid,
    'classification':classification,
    'authority_scope':'DIAGNOSTIC_ONLY__NO_PHYSICAL_COORDINATE_PROMOTION',
    'target':{'double_double_global_index':TARGET_INDEX,'class_id':int(ch['class_id']),'q_squared':q2},
    'prospective_decision_rule':{
        'metric':'max symmetric-cross nphi16 vs nphi32 scaled delta at R and R/2',
        'material_if_greater_than':PHYSICAL_TOL,
        'meaning':'phi-mean resolution is a material fixed-mass contributor at the unchanged physical tolerance' if phi_material else 'phi-mean resolution is not material at the unchanged physical tolerance'
    },
    'records':records,
    'max_cross_scaled_nphi16_vs_nphi32_delta':float(max_cross_delta),
    'max_fixed_mass_scaled_nphi16_vs_nphi32_delta':float(max_fixed_delta),
    'fixed_mass_deltas':fixed_deltas,
    'reproduction_oracle':{'corner':[u0,v0],'parent_vs_reimplemented_nphi16_scaled_delta':repro_delta,'max_allowed':REPRO_TOL},
    'structure_observed':{
        'max_polynomial_heldout_scaled_error':float(maxpoly),
        'max_radial_richardson_scaled_error':float(maxrad),
        'minimum_analytic_uncut_abs_denominator':float(minunc),
        'minimum_kallen':float(minlam),
    },
    'thresholds':{
        'physical_materiality_scaled':PHYSICAL_TOL,
        'reproduction_scaled_max':REPRO_TOL,
        'polynomial_heldout_scaled_max':float(ns['POLY_HELDOUT_REL_TOL']),
        'radial_richardson_scaled_max':float(ns['RADIAL_EXTRAP_TOL']),
        'uncut_abs_min':float(ns['UNCUT_MIN_TOL']),
    },
    'runtime_seconds':float(time.perf_counter()-start),
    'interpretation':(
        'If MATERIAL, prioritize phi-mean/fixed-mass numerator resolution in any Iteration-424 implementation. '
        'If STABLE, phi-node resolution is not a dominant explanation at the physical tolerance and the remaining '
        'priority becomes traced-numerator/radial/high-precision full-chain mass differentiation.'
    ),
    'guardrails':[
        'DIAGNOSTIC_ONLY','ITERATION421_REMAINS_PHYSICAL_AUTHORITY_PATH','NO_PHYSICAL_DS_VALUE',
        'NO_THRESHOLD_WEAKENING','NO_SMALLER_MASS_STEP','NO_ZERO_FILL','NO_ANGULAR_GRID_ESCALATION_FOR_PHYSICAL_PROMOTION',
        'NO_ANSATZ003','NO_FISHER_RESOURCES'
    ]
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid:
    raise SystemExit(2)
