#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 427.

Prospective exact chain-rule reduction for the frozen Iteration-407 fixed-mass
sphere representation used by the unresolved Tr(U1^2) channel 2.

Iteration 425 established that auxiliary masses enter the complete frozen
function through beta(u,v) and through alpha(u,v),rho(u,v) in both numerator and
affine moments.  This iteration derives the exact mixed-mass derivative at
u=v=0 before the active Iteration-421 physical result is known.

Write
    F(u,v) = 1/2 beta(u,v) H(alpha(u,v),rho(u,v)),
where H contains the complete degree-4 phi-mean numerator coefficients and all
affine analytic moments.  For s=-q^2>0 the exact chain rule reduces to

    D_s := -F_uv(0,0)
         = H/s^2 + H_{alpha alpha}/(8 s^2) - H_{rho rho}/(8 s).

For the target q^2=-1 (s=1):
    D_s = H + (H_{alpha alpha}-H_{rho rho})/8.

All H_alpha, H_rho and H_{alpha rho} terms cancel identically.  This promotes no
physical coordinate; it prospectively supplies a better-conditioned coordinate
system for an Iteration-424 fallback if Iteration 421 returns BLOCKED_CONVERGENCE.
"""
from pathlib import Path
import json
import sympy as sp

ITERATION=427
TARGET_INDEX=2
EXPECTED_CLASS=3
EXPECTED_Q2=-1.0

# Source audit: the frozen representation factors exactly as beta/2 times a
# quantity whose remaining auxiliary-mass dependence is through alpha,rho.
root=Path(__file__).resolve().parent
parent=root/'iteration407_tru1sq_channel4_analytic_spectral_reduction.py'
src=parent.read_text()
required={
    'lambda':'lam=s*s+u*u+v*v-2*s*u-2*s*v-2*u*v',
    'alpha':'alpha=-(s+u-v)/(2.0*s)',
    'rho':'rho=math.sqrt(lam)/(2.0*math.sqrt(s))',
    'beta':'beta=math.sqrt(lam)/s',
    'numerator_through_alpha_rho':'stripped_limit_massive(alpha,rho*unit_from(z,phi))',
    'affine_through_alpha_rho':'alpha,rho,_,_=kin(u,v); r0=-a+alpha*q+c',
    'measure_factorization':'sphere=0.5*beta*sum(complex(coeff[k])*js[k] for k in range(POLY_DEGREE+1))',
}
observed={k:(v in src) for k,v in required.items()}
if not all(observed.values()):
    raise SystemExit(('parent_source_dependency_drift',observed))

s,u,v=sp.symbols('s u v', positive=True, real=True)
lam=s*s+u*u+v*v-2*s*u-2*s*v-2*u*v
alpha=-(s+u-v)/(2*s)
rho=sp.sqrt(lam)/(2*sp.sqrt(s))
beta=sp.sqrt(lam)/s
zero={u:0,v:0}

# Exact kinematic derivatives at u=v=0.
def at0(expr):
    return sp.simplify(expr.subs(zero))
kin={
    'alpha_0':at0(alpha), 'alpha_u':at0(sp.diff(alpha,u)), 'alpha_v':at0(sp.diff(alpha,v)), 'alpha_uv':at0(sp.diff(alpha,u,v)),
    'rho_0':at0(rho), 'rho_u':at0(sp.diff(rho,u)), 'rho_v':at0(sp.diff(rho,v)), 'rho_uv':at0(sp.diff(rho,u,v)),
    'beta_0':at0(beta), 'beta_u':at0(sp.diff(beta,u)), 'beta_v':at0(sp.diff(beta,v)), 'beta_uv':at0(sp.diff(beta,u,v)),
}

H0,Ha,Hr,Haa,Har,Hrr=sp.symbols('H0 Ha Hr Haa Har Hrr')
Hu=Ha*kin['alpha_u']+Hr*kin['rho_u']
Hv=Ha*kin['alpha_v']+Hr*kin['rho_v']
Huv=(
    Haa*kin['alpha_u']*kin['alpha_v']
    +Har*(kin['alpha_u']*kin['rho_v']+kin['rho_u']*kin['alpha_v'])
    +Hrr*kin['rho_u']*kin['rho_v']
    +Ha*kin['alpha_uv']+Hr*kin['rho_uv']
)
Fuv=sp.simplify(sp.Rational(1,2)*(
    kin['beta_uv']*H0 + kin['beta_u']*Hv + kin['beta_v']*Hu + kin['beta_0']*Huv
))
Ds=sp.simplify(-Fuv)
expected=sp.simplify(H0/s**2 + Haa/(8*s**2) - Hrr/(8*s))
identity_ok=bool(sp.simplify(Ds-expected)==0)
coeffs={name:str(sp.simplify(sp.diff(Ds,sym))) for name,sym in [('H',H0),('H_alpha',Ha),('H_rho',Hr),('H_alphaalpha',Haa),('H_alpharho',Har),('H_rhorho',Hrr)]}
expected_coeffs={
    'H':'s**(-2)',
    'H_alpha':'0',
    'H_rho':'0',
    'H_alphaalpha':'1/(8*s**2)',
    'H_alpharho':'0',
    'H_rhorho':'-1/(8*s)',
}
coefficient_ok=all(sp.simplify(sp.diff(Ds,sym)-target)==0 for sym,target in [
    (H0,1/s**2),(Ha,0),(Hr,0),(Haa,1/(8*s**2)),(Har,0),(Hrr,-1/(8*s))
])

target_s=sp.Integer(1)
target_formula=sp.simplify(Ds.subs(s,target_s))
target_expected=sp.simplify(H0+(Haa-Hrr)/8)
target_ok=bool(sp.simplify(target_formula-target_expected)==0)
execution_valid=bool(identity_ok and coefficient_ok and target_ok)

result={
    'iteration':ITERATION,
    'model_readiness_percent':24,
    'candidate_residual':False,
    'scientific_gate_pass':execution_valid,
    'classification':('PASS_CHANNEL2_EXACT_MASS_TO_KINEMATIC_CHAIN_REDUCTION__NON_PROMOTING' if execution_valid else 'FAIL_CHANNEL2_EXACT_MASS_TO_KINEMATIC_CHAIN_REDUCTION'),
    'authority_scope':'EXACT_ANALYTIC_CONTRACT__NO_PHYSICAL_COORDINATE_PROMOTION',
    'target':{'double_double_global_index':TARGET_INDEX,'class_id':EXPECTED_CLASS,'q_squared':EXPECTED_Q2,'s':1.0},
    'source_parent':parent.name,
    'observed_dependencies':observed,
    'kinematic_derivatives_general_s':{k:str(v) for k,v in kin.items()},
    'exact_general_formula':'D_s=-F_uv=H/s^2 + H_alphaalpha/(8*s^2) - H_rhorho/(8*s)',
    'exact_target_formula':'q^2=-1 => s=1 => D_s=H+(H_alphaalpha-H_rhorho)/8',
    'derived_coefficients':coeffs,
    'exact_cancellations':['H_alpha','H_rho','H_alpharho'],
    'identity_checks':{'general_chain_identity':identity_ok,'coefficient_identity':coefficient_ok,'target_s1_identity':target_ok},
    'interpretation':(
        'The complete auxiliary-mass mixed derivative can be evaluated without a mixed u,v finite-difference. '
        'At the target it is exactly a combination of H itself and pure second derivatives in alpha and rho. '
        'If Iteration 421 is BLOCKED_CONVERGENCE, an Iteration-424 high-precision/AD implementation should prefer '
        'this exact full-chain coordinate reduction, while still differentiating the complete H including numerator '
        'coefficients and affine moments.'
    ),
    'guardrails':[
        'PROSPECTIVE_BEFORE_ITERATION421_RESULT','NO_PHYSICAL_DS_VALUE','NO_DENOMINATOR_ONLY_SHORTCUT',
        'FULL_H_INCLUDES_NUMERATOR_AND_AFFINE_MOMENTS','NO_THRESHOLD_WEAKENING','NO_SMALLER_MASS_STEP',
        'NO_ZERO_FILL','NO_ANSATZ003','NO_FISHER_RESOURCES'
    ]
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid:
    raise SystemExit(2)
