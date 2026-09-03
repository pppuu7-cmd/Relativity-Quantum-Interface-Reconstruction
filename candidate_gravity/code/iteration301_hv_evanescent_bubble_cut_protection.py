#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 301.

HV-split evanescent protection audit for the direct-timelike bubble CUT.

For external momenta in a four-dimensional barred subspace and D=4-2 eps loop
momentum L=bar(L)+hat(L), define mu^2=-hat(L)^2. Standard angular splitting
makes a mu^(2r) insertion proportional to (-eps)_r times the same scalar
bubble in D+2r dimensions (an overall convention sign does not affect the
vanishing/pole-order statements tested here).

This iteration tests the only bubble denominator powers present in Iteration
295/296: ordinary (1,1) and raised (2,1), and r=0,1,2, sufficient for the
bubble numerator degree ceiling <=4. We audit the normalized advanced-minus-
retarded cut itself, because RQIR's linked target uses D_s rather than the full
finite amplitude.
"""
import json, math
import numpy as np
from scipy.special import gamma

EPS=np.array([.04,.02,.01,.005,.0025],float)
S_VALUES=(.016,.216)


def bubble_branch(a,b,r,s,eps,phase):
    D=4.0-2.0*eps+2.0*r
    D2=D/2.0
    alpha=D2-a-b
    Z=s*np.exp(1j*phase*np.pi)
    coeff=(gamma(a+b-D2)*gamma(D2-a)*gamma(D2-b)/
           (gamma(a)*gamma(b)*gamma(D-a-b)))
    return coeff*(Z**alpha)


def bubble_cut(a,b,r,s,eps):
    ret=bubble_branch(a,b,r,s,eps,-1)
    adv=bubble_branch(a,b,r,s,eps,+1)
    return (adv-ret)/(2j*np.pi)


def poch_minus_eps(r,eps):
    if r==0: return 1.0
    z=1.0
    for j in range(r): z*=(-eps+j)
    return z


def laurent_cut(vals):
    y=np.asarray(vals,complex); z=EPS*y
    X=np.column_stack([np.ones_like(EPS),EPS,EPS**2,EPS**3])
    cr=np.linalg.lstsq(X,z.real,rcond=None)[0]
    ci=np.linalg.lstsq(X,z.imag,rcond=None)[0]
    fit=X@cr+1j*(X@ci)
    return {
      'one_over_eps_residue':[float(cr[0]),float(ci[0])],
      'finite_cut_coefficient_if_residue_zero':[float(cr[1]),float(ci[1])],
      'eps_times_cut_fit_max_abs_residual':float(np.max(np.abs(fit-z))),
    }


def zero_limit(vals):
    y=np.asarray(vals,complex)
    X=np.column_stack([np.ones_like(EPS),EPS,EPS**2,EPS**3])
    cr=np.linalg.lstsq(X,y.real,rcond=None)[0]
    ci=np.linalg.lstsq(X,y.imag,rcond=None)[0]
    fit=X@cr+1j*(X@ci)
    return [float(cr[0]),float(ci[0])],float(np.max(np.abs(fit-y)))

rows={}
max_master_cut_pole=0.0
max_evanescent_limit=0.0
for a,b,label in [(1,1,'ordinary_bubble'),(2,1,'raised_bubble')]:
  for r in (0,1,2):
    for s in S_VALUES:
      vals=np.array([bubble_cut(a,b,r,s,float(e)) for e in EPS])
      au=laurent_cut(vals)
      pole=abs(complex(*au['one_over_eps_residue']))
      max_master_cut_pole=max(max_master_cut_pole,pole)
      ev=np.array([poch_minus_eps(r,float(e))*v for e,v in zip(EPS,vals)])
      lim,err=zero_limit(ev)
      if r>0: max_evanescent_limit=max(max_evanescent_limit,abs(complex(*lim)))
      rows[f'{label}__r{r}__s{s}']={
        'powers':[a,b], 'mu_power':2*r, 'dimension_shift':2*r, 's':s,
        'master_cut_scan':[[float(x.real),float(x.imag)] for x in vals],
        'master_cut_laurent':au,
        'mu_factor_scan':[float(poch_minus_eps(r,float(e))) for e in EPS],
        'evanescent_cut_scan':[[float(x.real),float(x.imag)] for x in ev],
        'evanescent_cut_limit':[float(lim[0]),float(lim[1])],
        'evanescent_limit_fit_max_abs_residual':err,
      }

# r=0 masters should be cut-pole-free; r=1,2 dimension-shifted masters should
# also be cut-pole-free. Then every genuine mu^(2r), r>0, contribution vanishes
# in the epsilon->0 normalized cut despite possible full-amplitude rational terms.
passed=max_master_cut_pole<3e-5 and max_evanescent_limit<3e-4
result={
 'iteration':301,
 'model_readiness_percent':24,
 'scope':'HV-like barred-external / D-dimensional-loop evanescent protection of ordinary+raised bubble normalized cuts; numerator degree <=4',
 'formula':'I_D[mu^(2r)] proportional to (-epsilon)_r I_(D+2r); only the O(epsilon) scaling and cut-pole order are used for the protection statement',
 'rows':rows,
 'max_abs_dimension_shifted_master_cut_one_over_eps_residue':max_master_cut_pole,
 'max_abs_mu_evanescent_cut_epsilon_to_zero_limit_r_gt_0':max_evanescent_limit,
 'classification':('PASS_HV_EVANESCENT_BUBBLE_CUT_PROTECTION_THROUGH_MU4__FULL_AMPLITUDE_FINITE_REMAINDER_NOT_PROMOTED'
    if passed else 'BLOCKED_HV_EVANESCENT_BUBBLE_CUT_PROTECTION_AUDIT'),
 'candidate_residual':False,
 'guardrails':[
   'RESULT_IS_FOR_NORMALIZED_DISCONTINUITY_NOT_FULL_FINITE_AMPLITUDE',
   'RESULT_IS_SCOPED_TO_BUBBLE_POWERS_11_AND_21_AND_POLYNOMIAL_NUMERATOR_DEGREE_LE4',
   'TRIANGLE_EVANESCENT_SECTOR_REMAINS_OPEN_BECAUSE_TRIANGLE_CUTS_CAN_CARRY_IR_POLES',
   'COMMON_REGULATOR_EXTERNAL_STATE_CONVENTION_MUST_EVENTUALLY_BE_SHARED_BY_K2_AND_GAMMA3',
   'NO_CANDIDATE_RESIDUAL_OR_SOURCE_COMPLETION_CLAIM'
 ],
 'next_gate':'if corrected Iteration296 is independently schema-valid, combine it with this theorem to promote the four bubble-family normalized cut coefficients within the stated HV-like cut scope; do not promote the full finite amplitude. Then derive the evanescent-sensitive triangle cut basis before triangle finite-cut promotion.'
}
assert passed,result
print(json.dumps(result,indent=2,sort_keys=True))
