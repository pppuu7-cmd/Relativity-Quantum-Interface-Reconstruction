#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 422.

Diagnostic-only conditioning audit for the affine-denominator analytic moments
used by the sole unresolved Tr(U1^2) double-double channel 2.

This gate is frozen while Iterations 419/421 are active. It does not evaluate a
new physical D_s coordinate and never calls the expensive stripped numerator.
It isolates whether float64 evaluation of

  J_n(c,a)=integral_{-1}^{1} z^n/(c+a z) dz, n=0..4,

and the fixed degree-4 z interpolation geometry are plausible sources of the
mass-derivative instability.  The exact same affine coefficients from the
Iteration-407 target-specialized kinematics are sampled on the full signed
R=1e-5, multipliers [1,.75,.5,.25] envelope.  Float64 moments are compared to
80-decimal mpmath evaluation of the identical analytic recurrence using the same
(float64-derived) c,a inputs.  Thus this diagnoses arithmetic conditioning only,
not upstream kinematic-input error or traced-numerator error.
"""
from __future__ import annotations
import contextlib, io, json, math
from pathlib import Path
import numpy as np
import mpmath as mp

ITERATION=422
TARGET_INDEX=2
EXPECTED_CLASS=3
EXPECTED_Q2=-1.0
RADIUS=1.0e-5
MULT=(1.0,0.75,0.5,0.25)
MOMENT_MAX_SCALED_DISCREPANCY=1.0e-10
VANDERMONDE_COND_MAX=1.0e3
mp.mp.dps=80

root=Path(__file__).resolve().parent
parent=root/'iteration407_tru1sq_channel4_analytic_spectral_reduction.py'
src=parent.read_text()
for old,new in [
 ('ITERATION=407','ITERATION=422'),
 ('TARGET_INDEX=4','TARGET_INDEX=2'),
 ("if int(ch['class_id'])!=5 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))",
  "if int(ch['class_id'])!=3 or abs(q2+1.0)>1e-12: raise RuntimeError(('target_identity_drift',ch['class_id'],q2))")]:
    if src.count(old)!=1: raise RuntimeError(('iteration407_specialization_drift',old,src.count(old)))
    src=src.replace(old,new,1)
marker="\nstart=time.perf_counter()\nd_base,diag_base=derivative_from_analytic(BASE_H)"
if src.count(marker)!=1: raise RuntimeError(('iteration407_execution_boundary_drift',src.count(marker)))
prefix=src.split(marker,1)[0]+'\n'
ns={'__name__':'iteration422_parent407_prefix','__file__':str(parent)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(prefix,str(parent),'exec'),ns,ns)
ch=ns['ch']; q2=float(ns['q2']); affine_coeffs=ns['affine_coeffs']; float_moments=ns['integral_monomials_over_affine']
if int(ch['class_id'])!=EXPECTED_CLASS or abs(q2-EXPECTED_Q2)>1e-12: raise RuntimeError(('target_identity_drift_after_exec',ch['class_id'],q2))

TRAIN_Z=np.asarray(ns['TRAIN_Z'],float)
V=np.vander(TRAIN_Z,5,increasing=True)
vcond=float(np.linalg.cond(V))

def mpc(z): return mp.mpc(float(complex(z).real),float(complex(z).imag))
def hp_moments(cc0,aa0,degree=4):
    cc,aa=mpc(cc0),mpc(aa0)
    if abs(aa)<mp.mpf('1e-30'):
        return [((mp.mpf('0') if k%2 else mp.mpf(2)/(k+1))/cc) for k in range(degree+1)]
    out=[(mp.log(cc+aa)-mp.log(cc-aa))/aa]
    for k in range(1,degree+1):
        im1=mp.mpf('0') if (k-1)%2 else mp.mpf(2)/k
        out.append((im1-cc*out[-1])/aa)
    return out

def recurrence_cancellation(cc0,aa0,hp):
    cc,aa=mpc(cc0),mpc(aa0); vals=[]
    if abs(aa)<mp.mpf('1e-30'): return [1.0]*4
    for k in range(1,5):
        im1=mp.mpf('0') if (k-1)%2 else mp.mpf(2)/k
        t1=im1; t2=cc*hp[k-1]; den=abs(t1-t2)
        vals.append(float((abs(t1)+abs(t2))/max(den,mp.mpf('1e-80'))))
    return vals

signed=sorted({s*RADIUS*m for m in MULT for s in (-1.0,1.0)})
records=[]; maxerr=0.0; maxcancel=0.0; minendpoint=float('inf'); max_ratio=0.0
for u in signed:
  for v in signed:
    cc,aa=affine_coeffs(float(u),float(v)); fm=float_moments(cc,aa,4); hm=hp_moments(cc,aa,4)
    errs=[]
    for x,y in zip(fm,hm):
        yc=complex(float(mp.re(y)),float(mp.im(y)))
        er=float(abs(complex(x)-yc)/max(1.0,abs(complex(x)),abs(yc))); errs.append(er); maxerr=max(maxerr,er)
    canc=recurrence_cancellation(cc,aa,hm); maxcancel=max(maxcancel,max(canc))
    endpoint=float(min(abs(cc-aa),abs(cc+aa))); minendpoint=min(minendpoint,endpoint)
    ratio=float(abs(aa)/max(abs(cc),1e-300)); max_ratio=max(max_ratio,ratio)
    records.append({'u':float(u),'v':float(v),'c':[float(complex(cc).real),float(complex(cc).imag)],'a':[float(complex(aa).real),float(complex(aa).imag)],'endpoint_min_abs':endpoint,'abs_a_over_abs_c':ratio,'moment_scaled_errors':errs,'max_moment_scaled_error':max(errs),'recurrence_cancellation_factors':canc})

execution_valid=bool(len(records)==64 and np.isfinite(maxerr) and np.isfinite(vcond) and minendpoint>ns['UNCUT_MIN_TOL'])
arithmetic_stable=bool(execution_valid and maxerr<=MOMENT_MAX_SCALED_DISCREPANCY and vcond<=VANDERMONDE_COND_MAX)
result={
 'iteration':ITERATION,'model_readiness_percent':24,'candidate_residual':False,'scientific_gate_pass':execution_valid,
 'classification':('PASS_CHANNEL2_AFFINE_MOMENT_CONDITIONING__FLOAT64_STABLE_DIAGNOSTIC_ONLY' if arithmetic_stable else 'PASS_CHANNEL2_AFFINE_MOMENT_CONDITIONING__ARITHMETIC_SUSPECT_DIAGNOSTIC_ONLY' if execution_valid else 'FAIL_CHANNEL2_AFFINE_MOMENT_CONDITIONING_EXECUTION'),
 'authority_scope':'DIAGNOSTIC_ONLY__NO_PHYSICAL_COORDINATE_PROMOTION',
 'target':{'double_double_global_index':TARGET_INDEX,'class_id':int(ch['class_id']),'q_squared':q2},
 'mass_envelope':{'radius':RADIUS,'multipliers':list(MULT),'signed_node_count_per_axis':len(signed),'pair_count':len(records)},
 'degree4_interpolation_vandermonde_condition_number':vcond,
 'max_float64_vs_80digit_moment_scaled_discrepancy':maxerr,
 'max_analytic_recurrence_cancellation_factor':maxcancel,
 'minimum_affine_endpoint_abs_denominator':minendpoint,
 'max_abs_a_over_abs_c':max_ratio,
 'thresholds':{'moment_scaled_discrepancy_max':MOMENT_MAX_SCALED_DISCREPANCY,'vandermonde_condition_number_max':VANDERMONDE_COND_MAX,'uncut_abs_min':ns['UNCUT_MIN_TOL']},
 'records':records,
 'interpretation':('affine J_n recurrence and degree-4 interpolation geometry are numerically stable at the audited envelope; if channel2 remains unstable, prioritize phi-mean/traced-numerator/radial or mass-derivative cancellation layers' if arithmetic_stable else 'affine-moment/interpolation arithmetic is itself a plausible conditioning contributor and should be upgraded before any physical promotion'),
 'guardrails':['FROZEN_WHILE_ITERATION419_421_ACTIVE','NO_STRIPPED_NUMERATOR_CALLS','NO_PHYSICAL_DS_VALUE','SAME_FLOAT64_C_A_INPUTS_FOR_BOTH_ARITHMETICS','NO_THRESHOLD_WEAKENING','NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES']
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid: raise SystemExit(2)
