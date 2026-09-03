#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 375.

Validate the auxiliary-mass/distributional bridge needed for the 36 simple-double
and 15 double-double timelike Tr(U1^2) channels frozen by Iteration 372.

For same i0 prescription:
  D1^-2 D2^-1 = - d/d(mu1^2) [(D1+mu1^2)^-1 D2^-1] at mu1^2=0,
  D1^-2 D2^-2 = + d^2/(dmu1^2 dmu2^2)
                    [(D1+mu1^2)^-1 (D2+mu2^2)^-1] at zero.

This is method validation only. No physical Tr(U1^2) channel is integrated.
"""
from __future__ import annotations
import json, math
from functools import lru_cache
import numpy as np
from scipy.integrate import quad

ITERATION=375
PI=math.pi
L=12.0
EPS_LIST=np.array([0.1,0.05,0.025,0.0125,0.00625],float)
FD_H=5e-4
TH={
 'regulated_simple_double_direct_vs_aux_max_abs':1e-8,
 'regulated_double_double_direct_vs_aux_max_abs':2e-9,
 'simple_double_eps0_extrapolation_max_abs':2e-5,
 'double_double_eps0_extrapolation_max_abs':3e-5,
 'exact_shifted_delta_aux_max_abs':2e-9,
}

# F(x,y)=exp(-x^2-y^2) sum c_mn x^m y^n.  At the origin,
# Fx=c10, Fy=c01, Fxy=c11.
TESTS=[
 {'name':'t0','c':{'0,0':1.0,'1,0':0.30,'0,1':-0.20,'1,1':0.40,'2,0':0.15,'0,2':-0.10}},
 {'name':'t1','c':{'0,0':1.0,'1,0':-0.70,'0,1':0.50,'1,1':-0.60,'2,1':0.20,'1,2':-0.10}},
 {'name':'t2','c':{'0,0':1.0,'1,0':1.10,'0,1':0.90,'1,1':0.25,'2,0':-0.40,'0,2':0.30,'2,2':0.05}},
 {'name':'even_control','c':{'0,0':1.0,'2,0':0.35,'0,2':-0.20,'2,2':0.15}},
]

def coeffs(t):
    return {(int(k.split(',')[0]),int(k.split(',')[1])):float(v) for k,v in t['c'].items()}

def split_quad(fun):
    a=quad(fun,-L,0.0,epsabs=2e-12,epsrel=2e-12,limit=600)[0]
    b=quad(fun,0.0,L,epsabs=2e-12,epsrel=2e-12,limit=600)[0]
    return float(a+b)

@lru_cache(None)
def m1(n,mu,eps):
    return split_quad(lambda x:(x**n)*np.exp(-x*x)*eps/(PI*((x+mu)**2+eps**2)))

@lru_cache(None)
def m2(n,eps):
    return split_quad(lambda x:(x**n)*np.exp(-x*x)*(2*x*eps)/(PI*(x*x+eps**2)**2))

def simple_massive(t,mu1,mu2,eps):
    c=coeffs(t)
    return sum(v*m1(m,float(mu1),float(eps))*m1(n,float(mu2),float(eps)) for (m,n),v in c.items())

def direct_sdx(t,eps):
    c=coeffs(t); e=float(eps)
    return sum(v*m2(m,e)*m1(n,0.0,e) for (m,n),v in c.items())

def direct_sdy(t,eps):
    c=coeffs(t); e=float(eps)
    return sum(v*m1(m,0.0,e)*m2(n,e) for (m,n),v in c.items())

def direct_dd(t,eps):
    c=coeffs(t); e=float(eps)
    return sum(v*m2(m,e)*m2(n,e) for (m,n),v in c.items())

def d5(fun,h):
    return (fun(-2*h)-8*fun(-h)+8*fun(h)-fun(2*h))/(12*h)

def dxy5(fun,h):
    return d5(lambda x:d5(lambda y:fun(x,y),h),h)

def exact_F(t,x,y):
    c=coeffs(t)
    return float(np.exp(-x*x-y*y)*sum(v*(x**m)*(y**n) for (m,n),v in c.items()))

rows=[]
max_pair_sd=0.0; max_pair_dd=0.0; max_ext_sd=0.0; max_ext_dd=0.0; max_exact=0.0
for t in TESTS:
    c=coeffs(t); tx=c.get((1,0),0.0); ty=c.get((0,1),0.0); txy=c.get((1,1),0.0)
    eps=0.05
    aux_x=-d5(lambda mu:simple_massive(t,mu,0.0,eps),FD_H)
    aux_y=-d5(lambda mu:simple_massive(t,0.0,mu,eps),FD_H)
    aux_dd=dxy5(lambda u,v:simple_massive(t,u,v,eps),FD_H)
    dx=direct_sdx(t,eps); dy=direct_sdy(t,eps); dd=direct_dd(t,eps)
    ex=abs(dx-aux_x); ey=abs(dy-aux_y); edd=abs(dd-aux_dd)
    max_pair_sd=max(max_pair_sd,ex,ey); max_pair_dd=max(max_pair_dd,edd)

    vx=np.array([direct_sdx(t,e) for e in EPS_LIST]); vy=np.array([direct_sdy(t,e) for e in EPS_LIST]); vd=np.array([direct_dd(t,e) for e in EPS_LIST])
    x0=float(np.polyval(np.polyfit(EPS_LIST,vx,3),0.0)); y0=float(np.polyval(np.polyfit(EPS_LIST,vy,3),0.0)); d0=float(np.polyval(np.polyfit(EPS_LIST,vd,3),0.0))
    extx=abs(x0-tx); exty=abs(y0-ty); extd=abs(d0-txy)
    max_ext_sd=max(max_ext_sd,extx,exty); max_ext_dd=max(max_ext_dd,extd)

    # Exact shifted-delta oracle: simple-simple smeared cut is F(-mu1,-mu2).
    qx=-d5(lambda mu:exact_F(t,-mu,0.0),1e-3)
    qy=-d5(lambda mu:exact_F(t,0.0,-mu),1e-3)
    qdd=dxy5(lambda u,v:exact_F(t,-u,-v),1e-3)
    qerr=max(abs(qx-tx),abs(qy-ty),abs(qdd-txy)); max_exact=max(max_exact,qerr)
    rows.append({'name':t['name'],'targets':{'Fx0':tx,'Fy0':ty,'Fxy0':txy},
      'regulated_eps_0p05':{'simple_double_x_direct':dx,'simple_double_x_aux':aux_x,'simple_double_x_abs_error':ex,
                            'simple_double_y_direct':dy,'simple_double_y_aux':aux_y,'simple_double_y_abs_error':ey,
                            'double_double_direct':dd,'double_double_aux':aux_dd,'double_double_abs_error':edd},
      'eps0_extrapolation':{'simple_double_x':x0,'simple_double_x_abs_error':extx,'simple_double_y':y0,'simple_double_y_abs_error':exty,
                            'double_double':d0,'double_double_abs_error':extd},
      'exact_shifted_delta':{'simple_double_x':qx,'simple_double_y':qy,'double_double':qdd,'max_abs_error':qerr}})

passed=bool(max_pair_sd<TH['regulated_simple_double_direct_vs_aux_max_abs'] and
            max_pair_dd<TH['regulated_double_double_direct_vs_aux_max_abs'] and
            max_ext_sd<TH['simple_double_eps0_extrapolation_max_abs'] and
            max_ext_dd<TH['double_double_eps0_extrapolation_max_abs'] and
            max_exact<TH['exact_shifted_delta_aux_max_abs'])
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':passed,'candidate_residual':False,
 'classification':('PASS_TRU1SQ_SIMPLE_DOUBLE_AND_DOUBLE_DOUBLE_AUXMASS_DISTRIBUTIONAL_ORACLE' if passed else 'FAIL_TRU1SQ_REPEATED_CUT_AUXMASS_DISTRIBUTIONAL_ORACLE'),
 'identities':{
  'simple_double':'D1^-2 D2^-1 = - d_mu1 [(D1+mu1)^-1 D2^-1] at mu1=0',
  'double_double':'D1^-2 D2^-2 = + d_mu1 d_mu2 [(D1+mu1)^-1 (D2+mu2)^-1] at zero'},
 'normalized_disc_convention':'D_s=(advanced-retarded)/(2*pi*i); overall two-line cut normalization inherited downstream from Iteration337',
 'thresholds':TH,
 'max_errors':{'regulated_simple_double_direct_vs_aux':max_pair_sd,'regulated_double_double_direct_vs_aux':max_pair_dd,
               'simple_double_eps0_extrapolation':max_ext_sd,'double_double_eps0_extrapolation':max_ext_dd,'exact_shifted_delta_aux':max_exact},
 'tests':rows,
 'scope':'METHOD_VALIDATION_ONLY__NO_PHYSICAL_TRU1SQ_REPEATED_CUT_VALUE',
 'guardrails':['SAME_I0_ON_ALL_AUXILIARY_MASS_SHIFTS','NO_ORDINARY_SIMPLE_SUBSTITUTION_FOR_DOUBLE_POLES','DISTINCT_Q2_BUCKETS_NEVER_SUMMED',
               'NO_ZERO_FILL','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':('if PASS, perform exact timelike kinematic separation under symmetric auxiliary-mass probes for all 36 simple-double and 15 double-double channels before physical derivative integration; keep q2 buckets and pole orientations explicit')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
