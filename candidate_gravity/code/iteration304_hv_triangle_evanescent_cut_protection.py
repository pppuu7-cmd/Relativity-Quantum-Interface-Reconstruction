#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 304.

HV-like evanescent protection audit for the one-null two-mass TRIANGLE
normalized cut on the frozen timelike row.

Iteration 303 counted 274 polynomial coefficients invisible to the current 4D
loop-momentum oracle.  Here we ask the narrower physical question required by
RQIR: can any such coefficient survive in the normalized discontinuity D_s?

For external states in a barred four-dimensional subspace and
D=4-2*epsilon, a genuine mu^(2r) insertion (mu^2=-hat(l)^2) supplies the
standard angular factor (-epsilon)_r.  A hidden layer also contains a barred
polynomial P_m(bar l).  After Feynman shifting, every pair of barred loop
momenta produces a scalar tensor moment with an additional dimension shift
2*j; positive Feynman-parameter powers from the shift cannot worsen endpoint
IR behaviour.  Therefore the conservative scalar master screen is

    R = r + j,  j=0,...,floor(m/2).

The only denominator families frozen by Iterations 292/303 are ordinary
(1,1,1) and the three placements of raised (2,1,1), all with pair invariant
magnitudes {0,0.016,0.216}.  We evaluate their common timelike normalized cut
semi-analytically using the exact one-null Feynman-parameter factorization.

This is a cut-protection theorem in the explicit HV-like external-state scope.
It is NOT a same-parent full finite-amplitude scheme conversion.
"""
import json
import numpy as np
from scipy.special import gamma, beta, hyp2f1

EPS=np.array([.04,.02,.01,.005,.0025,.00125],float)
S1=0.016
S2=0.216
NULL_EDGE=(0,1)


def poch_minus_eps(r,eps):
    if r==0:
        return 1.0
    z=1.0
    for j in range(r):
        z*=(-eps+j)
    return z


def triangle_cut(powers,R,eps,ski=S1,skj=S2):
    """Normalized common timelike cut for a one-null scalar triangle.

    Vertices 0 and 1 are connected by the null invariant.  Vertex 2 is the
    opposite vertex, with hard edge magnitudes ski and skj to vertices 0,1.
    The loop normalization is i*pi^(D/2).  The overall sign is calibrated below
    against the exact ordinary-triangle cut used in Iteration 288.
    """
    D=4.0-2.0*eps+2.0*R
    D2=D/2.0
    A=float(sum(powers))
    alpha=D2-A
    i,j=NULL_EDGE
    k=2
    pi,pj,pk=(float(powers[i]),float(powers[j]),float(powers[k]))

    # F=t(1-t)[v*ski+(1-v)*skj].  The t integral is beta; the v integral is
    # beta*2F1 exactly.  Positive ski,skj are the hard invariant magnitudes.
    J=(skj**alpha)*beta(pi,pj)*hyp2f1(-alpha,pi,pi+pj,1.0-ski/skj)
    pref=gamma(A-D2)/(gamma(powers[0])*gamma(powers[1])*gamma(powers[2]))
    tint=beta(pk+alpha,pi+pj+alpha)
    # advanced-retarded over 2*pi*i; sign fixed by Iteration-288 calibration.
    val=-pref*tint*J*np.sin(np.pi*alpha)/np.pi
    return float(np.real(val))


def laurent_one_over_eps(vals):
    y=np.asarray(vals,float)
    z=EPS*y
    X=np.column_stack([np.ones_like(EPS),EPS,EPS**2,EPS**3,EPS**4])
    c=np.linalg.lstsq(X,z,rcond=None)[0]
    fit=X@c
    return {
      'one_over_eps_residue':float(c[0]),
      'finite_cut_if_residue_zero':float(c[1]),
      'eps_times_cut_fit_max_abs_residual':float(np.max(np.abs(fit-z))),
    }


def zero_limit(vals):
    y=np.asarray(vals,float)
    X=np.column_stack([np.ones_like(EPS),EPS,EPS**2,EPS**3,EPS**4])
    c=np.linalg.lstsq(X,y,rcond=None)[0]
    fit=X@c
    return float(c[0]),float(np.max(np.abs(fit-y)))

# Exact r=0 ordinary triangle calibration from Iteration 288.
cal_scan=np.array([triangle_cut((1,1,1),0,float(e)) for e in EPS])
cal_limit,cal_fit_res=zero_limit(cal_scan)
cal_target=-np.log(S1/S2)/(S2-S1)
cal_abs_res=abs(cal_limit-cal_target)

# Hard-edge interchange covariance: swap vertices 0<->1 and S1<->S2.
def swapped_powers(p):
    return (p[1],p[0],p[2])

family_specs={
  'ordinary_triangle':{
    'powers':(1,1,1),
    'hidden_layers':[(1,2),(2,0)], # (mu power index r, barred degree ceiling m)
  },
  'raised_triangle_repeat_null_vertex_0':{
    'powers':(2,1,1),
    'hidden_layers':[(1,4),(2,2),(3,0)],
  },
  'raised_triangle_repeat_null_vertex_1':{
    'powers':(1,2,1),
    'hidden_layers':[(1,4),(2,2),(3,0)],
  },
  'raised_triangle_repeat_opposite_vertex':{
    'powers':(1,1,2),
    'hidden_layers':[(1,4),(2,2),(3,0)],
  },
}

masters={}
layers={}
max_master_pole=0.0
max_evan_limit=0.0
max_evan_fit_res=0.0
max_swap_res=0.0
screen_count=0

for fname,spec in family_specs.items():
    p=spec['powers']
    needed_R=sorted({r+j for r,m in spec['hidden_layers'] for j in range(m//2+1)})
    for R in needed_R:
        vals=np.array([triangle_cut(p,R,float(e)) for e in EPS])
        lau=laurent_one_over_eps(vals)
        pole=abs(lau['one_over_eps_residue'])
        max_master_pole=max(max_master_pole,pole)
        swap=max(abs(triangle_cut(p,R,float(e),S1,S2)-
                     triangle_cut(swapped_powers(p),R,float(e),S2,S1)) for e in EPS)
        max_swap_res=max(max_swap_res,swap)
        masters[f'{fname}__R{R}']={
          'powers':list(p),
          'effective_dimension_shift':2*R,
          'master_cut_scan':vals.tolist(),
          'master_cut_laurent':lau,
          'hard_edge_swap_covariance_max_abs_residual':float(swap),
        }

    for r,m in spec['hidden_layers']:
        for j in range(m//2+1):
            R=r+j
            vals=np.array([triangle_cut(p,R,float(e)) for e in EPS])
            ev=np.array([poch_minus_eps(r,float(e))*v for e,v in zip(EPS,vals)])
            lim,err=zero_limit(ev)
            max_evan_limit=max(max_evan_limit,abs(lim))
            max_evan_fit_res=max(max_evan_fit_res,err)
            screen_count+=1
            layers[f'{fname}__mu{2*r}__bar_deg_le{m}__tensor_pairs_{j}']={
              'mu_power':2*r,
              'barred_degree_ceiling':m,
              'barred_loop_tensor_pair_count':j,
              'effective_dimension_shift':2*R,
              'mu_factor_scan':[float(poch_minus_eps(r,float(e))) for e in EPS],
              'dimension_shifted_master_cut_scan':vals.tolist(),
              'evanescent_cut_scan':ev.tolist(),
              'evanescent_cut_epsilon_to_zero_limit':float(lim),
              'evanescent_limit_fit_max_abs_residual':float(err),
            }

# Thresholds are deliberately much looser than observed numerical residuals.
passed=(cal_abs_res<2e-6 and max_swap_res<2e-8 and
        max_master_pole<2e-6 and max_evan_limit<2e-6 and
        max_evan_fit_res<5e-7 and screen_count==21)

result={
 'iteration':304,
 'model_readiness_percent':24,
 'scope':'HV-like barred external states; normalized common timelike cut only; one-null two-mass ordinary and all three raised triangle placements on frozen s=0.016 row',
 'frozen_invariant_magnitudes':[0.0,S1,S2],
 'formula':'hidden mu^(2r) P_m(bar l): angular factor (-epsilon)_r times scalar dimension-shift screens R=r+j for j=0..floor(m/2); positive Feynman-parameter powers cannot worsen endpoint IR degree',
 'ordinary_triangle_calibration':{
   'epsilon_scan':cal_scan.tolist(),
   'epsilon_to_zero_limit':float(cal_limit),
   'exact_iteration288_target':float(cal_target),
   'abs_residual':float(cal_abs_res),
   'fit_max_abs_residual':float(cal_fit_res),
 },
 'master_screens':masters,
 'hidden_layer_screens':layers,
 'hidden_tensor_screen_count':screen_count,
 'max_abs_dimension_shifted_triangle_master_cut_one_over_eps_residue_R_ge_1':float(max_master_pole),
 'max_abs_hidden_evanescent_triangle_cut_epsilon_to_zero_limit':float(max_evan_limit),
 'max_hidden_evanescent_limit_fit_abs_residual':float(max_evan_fit_res),
 'max_hard_edge_swap_covariance_abs_residual':float(max_swap_res),
 'classification':('PASS_HV_TRIANGLE_EVANESCENT_CUT_PROTECTION_ALL_274_HIDDEN_POLYNOMIAL_COEFFICIENTS_CUT_NULL_WITHIN_SCOPE'
   if passed else 'BLOCKED_HV_TRIANGLE_EVANESCENT_CUT_PROTECTION_AUDIT'),
 'candidate_residual':False,
 'guardrails':[
   'CUT_NULL_DOES_NOT_MEAN_THE_274_HIDDEN_COEFFICIENTS_ARE_ZERO',
   'RESULT_PROTECTS_NORMALIZED_DISCONTINUITY_ONLY_NOT_FULL_FINITE_AMPLITUDE',
   'ASSUMES_SAME_PARENT_D_DIMENSIONAL_NUMERATOR_COEFFICIENTS_ARE_REGULAR_AT_D_EQ_4_NO_ARTIFICIAL_1_OVER_D_MINUS_4_SINGULARITIES',
   'DO_NOT_IMPORT_ITERATION289_WEIGHTED_B3_PROXY_TRIANGLE_COEFFICIENTS',
   'ACTUAL_DIRECT_TIMELIKE_VISIBLE_TRIANGLE_NUMERATOR_COEFFICIENTS_FROM_ITERATION295_STILL_REQUIRE_INTEGRATION_AND_LAURENT_AUDIT',
   'NO_SOURCE_WARD_K2_COMPLETION_NO_COMPARATOR_RESIDUAL_NO_ANSATZ003'
 ],
 'next_gate':'evaluate the four actual direct-timelike visible triangle numerator families from Iteration295 in the same normalized-cut convention using raw epsilon scans and Laurent fits; because Iteration304 protects D_s from all 274 hidden HV-like evanescent polynomial coefficients, the 4D visible numerator reconstruction may be used for the triangle CUT within this scope, but not for the full finite amplitude.'
}
assert passed,result
print(json.dumps(result,indent=2,sort_keys=True))
