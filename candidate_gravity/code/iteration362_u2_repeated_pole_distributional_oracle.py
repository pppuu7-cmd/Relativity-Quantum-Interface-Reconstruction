#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 362.

Validate the frozen Iteration-359 first auxiliary-mass derivative prescription
for a double pole against an independent smooth-test-function regularized direct
distribution oracle. This is a method gate only: no physical repeated-pole U2
channel is integrated here.
"""
from __future__ import annotations
import json, math
import numpy as np
from scipy.integrate import quad

ITERATION=362
PI=math.pi
FD_H=1e-5
FD_TOL=2e-8
RICH_TOL=2e-3

# phi(x)=exp(-x^2)(1+a x+b x^2), so phi'(0)=a.
TESTS=[(0.30,0.10),(-0.70,0.20),(0.11,-0.35),(0.0,0.50)]

def phi(x,a,b):
    return math.exp(-x*x)*(1.0+a*x+b*x*x)

def simple_disc_action(mu2,a,b):
    # Disc 1/(x+mu2+i0) acting on phi = -2 pi i phi(-mu2).
    return -2j*PI*phi(-mu2,a,b)

def auxiliary_double_action(a,b,h=FD_H):
    # - d/d(mu2) simple_disc_action at zero, central finite difference.
    return -(simple_disc_action(h,a,b)-simple_disc_action(-h,a,b))/(2*h)

def analytic_double_action(a,b):
    # Disc (x+i0)^-2 = 2 pi i delta'(x); action = -2 pi i phi'(0).
    return -2j*PI*a

def regularized_direct(eta,a,b):
    # Independent direct smooth regularization of the squared-pole discontinuity.
    def imag_integrand(x):
        z=(1.0/(x+1j*eta)**2-1.0/(x-1j*eta)**2)*phi(x,a,b)
        return float(z.imag)
    im=quad(imag_integrand,-20.0,20.0,epsabs=2e-10,epsrel=2e-10,limit=1200)[0]
    return 1j*im

records=[]; ok=True; max_fd=0.0; max_rich=0.0
for a,b in TESTS:
    target=analytic_double_action(a,b)
    aux=auxiliary_double_action(a,b)
    fd_err=abs(aux-target)/max(1.0,abs(target)); max_fd=max(max_fd,fd_err)
    # O(eta) direct regularization; Richardson removes leading term.
    e=0.0125
    v1=regularized_direct(e,a,b); v2=regularized_direct(e/2.0,a,b)
    rich=2.0*v2-v1
    rich_err=abs(rich-target)/max(1.0,abs(target)); max_rich=max(max_rich,rich_err)
    passed=fd_err<=FD_TOL and rich_err<=RICH_TOL
    ok=ok and passed
    records.append({'a':a,'b':b,'analytic':[target.real,target.imag],
                    'auxiliary_mass_derivative':[aux.real,aux.imag],
                    'direct_regularized_richardson':[rich.real,rich.imag],
                    'scaled_fd_error':fd_err,'scaled_regularized_error':rich_err,'pass':passed})

classification=('PASS_U2_REPEATED_POLE_AUXILIARY_MASS_DERIVATIVE_DISTRIBUTIONAL_ORACLE'
                if ok else 'FAIL_U2_REPEATED_POLE_AUXILIARY_MASS_DERIVATIVE_DISTRIBUTIONAL_ORACLE')
result={'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':bool(ok),
        'candidate_residual':False,'classification':classification,
        'identity':'1/(D+i0)^2 = - d/d(mu2) [1/(D+mu2+i0)] at mu2=0',
        'distribution':'Disc[(x+i0)^-2]=2*pi*i*delta_prime(x)',
        'census':{'tests':len(records),'passed':sum(int(r['pass']) for r in records),
                  'max_scaled_auxiliary_derivative_error':max_fd,
                  'max_scaled_direct_regularized_error':max_rich},
        'thresholds':{'central_difference_h':FD_H,'scaled_auxiliary_derivative_max':FD_TOL,
                      'scaled_direct_regularized_richardson_max':RICH_TOL},
        'records':records,
        'scope':'METHOD_VALIDATION_ONLY__NO_PHYSICAL_REPEATED_POLE_U2_INTEGRATION',
        'guardrails':['SAME_I0_PRESCRIPTION','NO_SIMPLE_CUT_SUBSTITUTION_FOR_DOUBLE_POLES',
                      'NO_ZERO_FILL','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
        'next_gate':('if PASS, apply exactly one auxiliary-mass derivative to the 48 Iteration-359 repeated-pole timelike channels, first classifying massive-simple cut kinematics and uncut-pole separation before normalized physical integration; if FAIL, repeated-pole physical integration remains BLOCKED')}
print(json.dumps(result,indent=2,sort_keys=True))
if not ok: raise SystemExit(2)
