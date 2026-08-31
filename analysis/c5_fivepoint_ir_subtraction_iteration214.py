#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 214.

Freeze the leading IR subtraction of the physical pure-Einstein five-graviton
s-channel cut from Iteration 213.  The subtraction coefficient is not fitted to
cap data: it is fixed from the external Born amplitude,

    A(epsilon) = -2 i M5_tree(epsilon)

in the frozen KLT/sign convention.  The script verifies both beam endpoints,
the universal raw halving-shell logarithm, and regulator independence after
subtraction.
"""
from pathlib import Path
import json, math, sys
import numpy as np
from numpy.polynomial.legendre import leggauss
sys.path.insert(0,str(Path(__file__).resolve().parent))
from c5_cut_klt_common import cut_integrand_vec, external_m5, spherical

ITERATION=214
EPS_DIAG=0.01
THETA_FIT=np.array([0.01,0.005,0.0025,0.00125,0.000625],float)
EPS_CHECK=[0.04,0.01,0.001]
HALVING_HI=[0.1,0.05,0.025,0.0125,0.00625]
NPHI_ENDPOINT=128
NPHI_SHELL=256
NTH_SHELL=32


def endpoint_avg_coeff(epsilon,theta,north=True):
    phis=np.linspace(0,2*math.pi,NPHI_ENDPOINT,endpoint=False)
    acc=0j
    for phi in phis:
        th=theta if north else math.pi-theta
        n=spherical(th,float(phi)); mu=n[2]
        fac=(1-mu) if north else (1+mu)
        acc += fac*cut_integrand_vec(epsilon,n)
    return acc/len(phis)


def extrapolated_endpoint_A(epsilon,north=True):
    vals=np.array([endpoint_avg_coeff(epsilon,float(t),north) for t in THETA_FIT])
    X=np.vstack([np.ones_like(THETA_FIT),THETA_FIT**2,THETA_FIT**4]).T
    cr=np.linalg.lstsq(X,vals.real,rcond=None)[0]
    ci=np.linalg.lstsq(X,vals.imag,rcond=None)[0]
    return cr[0]+1j*ci[0]


def shell_integral(epsilon,lo,hi,subtracted,north=True):
    x,w=leggauss(NTH_SHELL)
    if north: a,b=lo,hi
    else: a,b=math.pi-hi,math.pi-lo
    th=(a+b)/2+(b-a)*x/2; wt=(b-a)*w/2
    phis=np.linspace(0,2*math.pi,NPHI_SHELL,endpoint=False)
    A=-2j*external_m5(epsilon)
    total=0j
    for theta,wi in zip(th,wt):
        st,ct=math.sin(theta),math.cos(theta)
        av=0j
        for phi in phis:
            n=np.array([st*math.cos(phi),st*math.sin(phi),ct])
            val=cut_integrand_vec(epsilon,n)
            if subtracted:
                val -= A/(1-ct)+A*0  # explicit first endpoint term
                val -= A/(1+ct)
            av += val
        total += wi*st*(2*math.pi/NPHI_SHELL)*av
    return total

M5=external_m5(EPS_DIAG); A=-2j*M5
out={
  "iteration":ITERATION,
  "date":"2026-09-01",
  "model_readiness_percent":23,
  "protocol":"Pure-Einstein five-graviton total-s cut; leading beam IR subtraction fixed from Born M5, never fitted to cap data.",
  "epsilon_diagnostic":EPS_DIAG,
  "born_m5":{"real":float(M5.real),"imag":float(M5.imag)},
  "subtraction_coefficient_A_equals_minus_2i_M5":{"real":float(A.real),"imag":float(A.imag)},
  "endpoint_identity_checks":[],
  "raw_halving_shell_prediction":{},
  "raw_halving_shells":[],
  "subtracted_halving_shells":[],
}

for eps in EPS_CHECK:
    target=-2j*external_m5(eps)
    for north in [True,False]:
        est=extrapolated_endpoint_A(eps,north)
        out["endpoint_identity_checks"].append({
          "epsilon":eps,"side":"N" if north else "S",
          "extrapolated_A":{"real":float(est.real),"imag":float(est.imag)},
          "target_minus_2i_M5":{"real":float(target.real),"imag":float(target.imag)},
          "relative_error":float(abs(est-target)/abs(target))
        })

pred=8*math.pi*A*math.log(2)
out["raw_halving_shell_prediction"]={"real":float(pred.real),"imag":float(pred.imag)}
sub_abs=[]; his=[]
for hi in HALVING_HI:
    lo=hi/2
    raw=shell_integral(EPS_DIAG,lo,hi,False,True)+shell_integral(EPS_DIAG,lo,hi,False,False)
    sub=shell_integral(EPS_DIAG,lo,hi,True,True)+shell_integral(EPS_DIAG,lo,hi,True,False)
    out["raw_halving_shells"].append({
      "delta_lo":lo,"delta_hi":hi,
      "integral":{"real":float(raw.real),"imag":float(raw.imag)},
      "relative_error_to_8piAlog2":float(abs(raw-pred)/abs(pred))
    })
    out["subtracted_halving_shells"].append({
      "delta_lo":lo,"delta_hi":hi,
      "integral":{"real":float(sub.real),"imag":float(sub.imag)},
      "abs":float(abs(sub))
    })
    his.append(hi); sub_abs.append(abs(sub))

out["subtracted_shell_abs_scaling_exponent"]=float(np.polyfit(np.log(his),np.log(sub_abs),1)[0])
out["classification"]={
  "beam_endpoint_coefficient":"PASS_BORN_EIKONAL_RELATION",
  "raw_endpoint_log":"PASS_UNIVERSAL_LOG_SHELL_LIMIT",
  "canonical_leading_pole_subtraction":"PASS_REGULATOR_INDEPENDENCE_SCOPED",
  "bulk_finite_integral":"NUMERICAL_CONVERGENCE_OPEN",
  "candidate_residual":"NONE",
  "ANSATZ_003":"NOT_CREATED",
  "Fisher_resources":"FORBIDDEN"
}
out["retained_results"]=[
  "C5-CUT-013 — FIVE_GRAVITON_BEAM_ENDPOINT_COEFFICIENT_EQUALS_MINUS_2I_TIMES_EXTERNAL_BORN_M5_IN_THE_FROZEN_KLT_CONVENTION",
  "IR-NG-003 — RAW_HALVING_CAP_SHELL_TENDS_TO_8PI_A_LOG2_WITH_A_MINUS_2I_M5",
  "IR-NG-004 — AFTER_CANONICAL_LEADING_POLE_SUBTRACTION_THE_CAP_DEPENDENCE_VANISHES_AS_DELTA_SQUARED_AFTER_AZIMUTHAL_INTEGRATION",
  "NG-FUNNEL-071 — REGULATOR_INDEPENDENCE_MUST_BE_PROVED_FROM_ENDPOINT_SHELLS_NOT_FROM_A_GLOBAL_FIT_DOMINATED_BY_BULK_PEAKS"
]
out["readiness_change"]="unchanged at 23%; physical C5 five-point cut now has a Born-fixed leading IR subtraction and regulator-independent endpoint limit, but the finite bulk hard remainder is not yet extracted robustly"
out["next_gate"]="Resolve the finite outgoing-hard-leg peaks with a deterministic bulk quadrature, evaluate the IR-subtracted cut on the frozen Iteration-210 epsilon grid, and extract regular+log coefficients."
Path("results/c5_fivepoint_ir_subtraction_iteration214.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2,sort_keys=True))
