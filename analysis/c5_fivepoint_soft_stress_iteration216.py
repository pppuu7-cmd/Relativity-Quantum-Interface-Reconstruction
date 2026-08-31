#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 216.

Stress-test the physical pure-Einstein five-graviton finite cut stored by
Iteration 215.  No Candidate Gravity target enters this script.

Authority rules:
  * use the frozen Iteration-210 12-point epsilon grid;
  * fit F(epsilon)=epsilon*I_finite(epsilon);
  * compare regular+log bases through n=2 and n=3;
  * use the Iteration-215 pointwise conservative numerical errors;
  * test fixed window removals and out-of-window prediction;
  * never promote fitted coefficients above the underlying physical vector.
"""
from pathlib import Path
import json
import numpy as np

ITERATION = 216
src = json.loads(Path("results/c5_fivepoint_finite_cut_extractor_iteration215.json").read_text())
eps = np.asarray(src["epsilon_grid"], float)
cut = np.asarray(src["finite_ir_subtracted_cut_real"], float) + 1j*np.asarray(src["finite_ir_subtracted_cut_imag"], float)
err = np.asarray(src["conservative_abs_error"], float)
F = eps * cut
Ferr = eps * err
eps_max = float(np.max(eps))
eps_ref = float(np.sqrt(np.min(eps)*np.max(eps)))
z = eps/eps_max
L = np.log(eps/eps_ref)

def design(order, idx):
    cols=[]
    for n in range(order+1):
        cols.extend([z[idx]**n, z[idx]**n*L[idx]])
    return np.column_stack(cols)

def fit(order, idx):
    X=design(order,idx); y=F[idx]
    c=np.linalg.lstsq(X,y,rcond=None)[0]
    pred=X@c
    resid=pred-y
    return {
        "coeff":c,
        "relative_l2_residual":float(np.linalg.norm(resid)/np.linalg.norm(y)),
        "condition_number":float(np.linalg.cond(X)),
        "max_residual_over_pointwise_error":float(np.max(np.abs(resid)/Ferr[idx])),
        "rms_residual_over_pointwise_error":float(np.sqrt(np.mean((np.abs(resid)/Ferr[idx])**2))),
    }

all_idx=np.arange(len(eps))
f2=fit(2,all_idx); f3=fit(3,all_idx)

# Fixed target-independent window audits.
windows={
    "full12":all_idx,
    "inner10_drop_two_largest_epsilon":np.arange(2,12),
    "inner8_drop_four_largest_epsilon":np.arange(4,12),
    "outer10_drop_two_smallest_epsilon":np.arange(0,10),
    "middle10_drop_both_endpoints":np.arange(1,11),
}
window_audit={}
base3=f3["coeff"]
for name,idx in windows.items():
    if len(idx)<8: continue
    ff=fit(3,idx)
    window_audit[name]={
        "n_points":int(len(idx)),
        "epsilon_min":float(np.min(eps[idx])),
        "epsilon_max":float(np.max(eps[idx])),
        "condition_number":ff["condition_number"],
        "relative_l2_fit_residual":ff["relative_l2_residual"],
        "relative_coefficient_shift_vs_full12":float(np.linalg.norm(ff["coeff"]-base3)/np.linalg.norm(base3)),
    }

# Fixed extrapolation checks: train on one contiguous 10-point window and predict
# the two withheld edge points.
def prediction(order, train, test):
    ff=fit(order,train)
    pred=design(order,test)@ff["coeff"]
    resid=pred-F[test]
    return {
        "relative_l2_prediction_error":float(np.linalg.norm(resid)/np.linalg.norm(F[test])),
        "max_prediction_error_over_pointwise_numerical_error":float(np.max(np.abs(resid)/Ferr[test])),
    }

prediction_audit={
    "n3_inner10_predict_two_largest_epsilon":prediction(3,np.arange(2,12),np.arange(0,2)),
    "n3_outer10_predict_two_smallest_epsilon":prediction(3,np.arange(0,10),np.arange(10,12)),
    "n3_middle10_predict_both_endpoints":prediction(3,np.arange(1,11),np.array([0,11])),
}

# Conservative coefficient sensitivity: a deterministic complex perturbation
# bounded pointwise by the declared numerical error, plus a norm upper bound.
X3=design(3,all_idx)
noise=Ferr*(np.sin(np.arange(12)+0.3)+1j*np.cos(np.arange(12)+0.7))
c3_pert=np.linalg.lstsq(X3,F+noise,rcond=None)[0]
coef_det_sensitivity=float(np.linalg.norm(c3_pert-base3)/np.linalg.norm(base3))
coef_norm_bound=float(np.linalg.norm(np.linalg.pinv(X3),2)*np.linalg.norm(Ferr)/np.linalg.norm(base3))

basis3_names=[]
for n in range(4):
    basis3_names += [f"z^{n}" if n else "1", f"z^{n}*L" if n else "L"]

out={
    "iteration":ITERATION,
    "date":"2026-09-01",
    "model_readiness_percent":23,
    "source_result":"results/c5_fivepoint_finite_cut_extractor_iteration215.json",
    "primary_authority":"the 12-point physical finite-cut vector plus pointwise conservative numerical error; fitted coefficients are compression only",
    "n2_full_window":{
        "basis":["1","L","z","zL","z^2","z^2L"],
        "condition_number":f2["condition_number"],
        "relative_l2_residual":f2["relative_l2_residual"],
        "max_residual_over_pointwise_error":f2["max_residual_over_pointwise_error"],
        "rms_residual_over_pointwise_error":f2["rms_residual_over_pointwise_error"],
    },
    "n3_full_window":{
        "basis":basis3_names,
        "condition_number":f3["condition_number"],
        "relative_l2_residual":f3["relative_l2_residual"],
        "max_residual_over_pointwise_error":f3["max_residual_over_pointwise_error"],
        "rms_residual_over_pointwise_error":f3["rms_residual_over_pointwise_error"],
        "coefficients":[{"real":float(x.real),"imag":float(x.imag)} for x in base3],
        "deterministic_pointwise_error_perturbation_relative_coefficient_change":coef_det_sensitivity,
        "conservative_l2_coefficient_error_bound":coef_norm_bound,
    },
    "window_audit_n3":window_audit,
    "prediction_audit":prediction_audit,
    "classification":{
        "n2_basis":"FAIL_NUMERICAL_COMPLETENESS_PHYSICAL_C5_VECTOR",
        "n3_basis":"PASS_WITHIN_DECLARED_POINTWISE_NUMERICAL_ERROR_ON_FULL_FROZEN_WINDOW",
        "n3_coefficients_as_exact_global_formula":"NO_COMPRESSION_ONLY",
        "large_epsilon_asymptotic_prediction_from_inner_window":"FAIL_HIGHER_ORDER_CONTENT_RESOLVED",
        "small_epsilon_prediction_from_outer_window":"PASS_WITHIN_POINTWISE_NUMERICAL_ERROR",
        "primary_C5_comparator_datum":"PHYSICAL_12_POINT_VECTOR_PLUS_ERROR_ENVELOPE",
        "off_shell_source_completed_T_cut":"STILL_BLOCKED",
        "candidate_residual":"NONE",
        "ANSATZ_003":"NOT_CREATED",
        "Fisher_resources":"FORBIDDEN",
    },
    "retained_results":[
        "C5-CUT-016 — N3_REGULAR_LOG_BASIS_IS_THE_FIRST_FROZEN_ORDER_THAT_DESCRIBES_THE_PHYSICAL_FIVE_GRAVITON_CUT_WITHIN_ITS_DECLARED_NUMERICAL_ERROR",
        "SOFT-NG-009 — REGULAR_LOG_COEFFICIENTS_ARE_COMPRESSION_NOT_PRIMARY_COMPARATOR_AUTHORITY_WHEN_HIGH_EPSILON_HIGHER_ORDER_CONTENT_IS_RESOLVED",
        "NUM-NG-018 — PHYSICAL_LOOP_COMPARATOR_AUTHORITY_IS_THE_FINITE_VECTOR_PLUS_POINTWISE_ERROR_ENVELOPE_NOT_A_WINDOW_DEPENDENT_ASYMPTOTIC_FIT",
        "NG-FUNNEL-073 — CANDIDATE_QUOTIENTS_MUST_PROPAGATE_PHYSICAL_COMPARATOR_VECTOR_ERRORS_AND_SOFT_TRUNCATION_SEPARATELY"
    ],
    "readiness_change":"unchanged at 23%; the physical C5 cut representation is now stress-tested, but the off-shell/source-completed C5 linked cut and AS/C3 nonlinear cuts remain open",
    "next_gate":"Use the physical 12-point C5 vector plus error as the on-shell nonanalytic control; separately determine whether any gauge-safe source-completed off-shell T_cut relation can be bounded or constructed, while continuing AS/C3 cut authority audits."
}

Path("results/c5_fivepoint_soft_stress_iteration216.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2,sort_keys=True))
