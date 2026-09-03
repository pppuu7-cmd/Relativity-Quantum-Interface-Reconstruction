#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 362.

Independent smooth-test-function validation of the Iteration-359 auxiliary-mass
reduction for the unique U2 double poles.

Frozen convention:
    D_s F = (F_advanced - F_retarded)/(2*pi*i).
For one real denominator x and regulator eps>0,
    K1_eps(x,mu2) = eps / [pi ((x+mu2)^2+eps^2)],
    K2_eps(x)     = 2 x eps / [pi (x^2+eps^2)^2].
Thus K2_eps = - d/d(mu2) K1_eps |_{mu2=0}, matching
    1/(D+i0)^2 = - d/d(mu2) 1/(D+mu2+i0) |_{mu2=0}.

This gate validates sign, normalization and derivative order against smooth test
functions before any physical repeated-pole U2 integration.  It does not compute
physical U2 discontinuities and does not touch the ordinary-simple zero result.
"""
from __future__ import annotations
import json, math
import numpy as np
from scipy.integrate import quad

ITERATION=362
PI=math.pi
L=12.0
EPS_LIST=np.array([0.1,0.05,0.025,0.0125,0.00625],float)
FD_H=5.0e-4
PAIR_THRESHOLD=1.0e-8
EXTRAP_THRESHOLD=5.0e-6
EXACT_DELTA_THRESHOLD=1.0e-9

# f(x)=exp(-x^2)*(1+a x+b x^2+c x^3); f'(0)=a.
TESTS=[
    {'name':'t0','a':0.30,'b':0.20,'c':0.10},
    {'name':'t1','a':-0.70,'b':0.10,'c':-0.20},
    {'name':'t2','a':1.10,'b':-0.40,'c':0.05},
    {'name':'even_control','a':0.0,'b':0.35,'c':0.0},
]

def f(x,t):
    return np.exp(-x*x)*(1.0+t['a']*x+t['b']*x*x+t['c']*x*x*x)

def integrate_split(fun):
    a=quad(fun,-L,0.0,epsabs=2e-12,epsrel=2e-12,limit=600)[0]
    b=quad(fun,0.0,L,epsabs=2e-12,epsrel=2e-12,limit=600)[0]
    return float(a+b)

def simple_reg(mu2,eps,t):
    return integrate_split(lambda x: f(x,t)*eps/(PI*((x+mu2)*(x+mu2)+eps*eps)))

def repeated_reg_direct(eps,t):
    return integrate_split(lambda x: f(x,t)*(2.0*x*eps)/(PI*(x*x+eps*eps)**2))

def derivative5(fun,h):
    return (fun(-2*h)-8.0*fun(-h)+8.0*fun(h)-fun(2*h))/(12.0*h)

rows=[]
max_pair=0.0
max_extrap=0.0
max_exact_delta=0.0
for t in TESTS:
    target=float(t['a'])

    # Independent regulated check: adaptive integration of the direct double-pole
    # kernel versus a five-point finite difference of the regulated simple-pole
    # smeared integral.  No analytic derivative is used in the finite-difference arm.
    direct_mid=repeated_reg_direct(0.05,t)
    aux_mid=-derivative5(lambda mu: simple_reg(mu,0.05,t),FD_H)
    pair_err=abs(direct_mid-aux_mid)
    max_pair=max(max_pair,pair_err)

    # Distribution-limit check: direct advanced-retarded double-pole kernels at a
    # sequence of eps values are extrapolated cubically to eps=0 and compared with
    # the exact smooth-distribution action f'(0).
    direct_vals=np.array([repeated_reg_direct(float(e),t) for e in EPS_LIST],float)
    coeff=np.polyfit(EPS_LIST,direct_vals,3)
    extrap=float(np.polyval(coeff,0.0))
    extrap_err=abs(extrap-target)
    max_extrap=max(max_extrap,extrap_err)

    # Exact shifted-delta oracle, independent of the regulated integration:
    # D_s(simple massive) smeared against f is f(-mu2), hence the repeated pole is
    # -d/dmu2 f(-mu2)|0 = f'(0).
    exact_aux=-derivative5(lambda mu: float(f(-mu,t)),1.0e-3)
    exact_delta_err=abs(exact_aux-target)
    max_exact_delta=max(max_exact_delta,exact_delta_err)

    rows.append({
        'name':t['name'],'target_fprime0':target,
        'regulated_eps_0p05_direct_double':direct_mid,
        'regulated_eps_0p05_aux_mass_fd':aux_mid,
        'regulated_pair_abs_error':pair_err,
        'eps_sequence':EPS_LIST.tolist(),
        'direct_double_values':direct_vals.tolist(),
        'cubic_eps_to_zero_extrapolated':extrap,
        'extrapolated_abs_error_to_fprime0':extrap_err,
        'exact_shifted_delta_aux_value':exact_aux,
        'exact_shifted_delta_abs_error':exact_delta_err,
    })

passed=bool(max_pair<PAIR_THRESHOLD and max_extrap<EXTRAP_THRESHOLD and max_exact_delta<EXACT_DELTA_THRESHOLD)
classification=('PASS_U2_REPEATED_POLE_AUXILIARY_MASS_DERIVATIVE_SMOOTH_DISTRIBUTION_ORACLE'
                if passed else 'FAIL_U2_REPEATED_POLE_AUXILIARY_MASS_DERIVATIVE_SMOOTH_DISTRIBUTION_ORACLE')
result={
    'iteration':ITERATION,
    'model_readiness_percent':24,
    'scientific_gate_pass':passed,
    'candidate_residual':False,
    'classification':classification,
    'frozen_identity':'1/(D+i0)^2 = - d/d(mu2) [1/(D+mu2+i0)] at mu2=0',
    'normalized_disc_convention':'D_s=(advanced-retarded)/(2*pi*i)',
    'thresholds':{
        'regulated_direct_vs_aux_fd_max_abs':PAIR_THRESHOLD,
        'cubic_eps0_extrapolation_to_exact_distribution_max_abs':EXTRAP_THRESHOLD,
        'exact_shifted_delta_aux_max_abs':EXACT_DELTA_THRESHOLD,
    },
    'max_errors':{
        'regulated_direct_vs_aux_fd':max_pair,
        'cubic_eps0_extrapolation_to_exact_distribution':max_extrap,
        'exact_shifted_delta_aux':max_exact_delta,
    },
    'tests':rows,
    'scope':'METHOD_VALIDATION_ONLY__NO_PHYSICAL_REPEATED_POLE_U2_VALUE',
    'guardrails':['ITERATION359_DOUBLE_POLE_ONLY','SAME_I0','NO_ORDINARY_SIMPLE_SUBSTITUTION_FOR_REPEATED_POLES',
                  'NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
    'next_gate':('if PASS, construct the physical channel-resolved simple-massive cut for the 48 repeated-pole typed channels, take the single auxiliary-mass derivative family-by-family, then mu2->0 with independent convergence checks; keep q2 buckets separate'),
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed:
    raise SystemExit(2)
