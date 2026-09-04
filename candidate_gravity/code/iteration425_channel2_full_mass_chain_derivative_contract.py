#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 425.

Prospective source-level audit of the auxiliary-mass dependence of the frozen
Iteration-407 analytic sphere representation used by the sole unresolved
Tr(U1^2) double-double target.  This iteration promotes no physical D_s.

Purpose: forbid an algebraically incomplete fallback that differentiates only
the affine uncut denominator.  In the frozen representation the auxiliary
masses also enter Kallen kinematics, alpha/rho/beta, the traced numerator and
therefore the fitted phi-mean polynomial coefficients.
"""
from pathlib import Path
import json

ITERATION=425
root=Path(__file__).resolve().parent
parent=root/'iteration407_tru1sq_channel4_analytic_spectral_reduction.py'
src=parent.read_text()

required={
 'kin_mass_dependence': "lam=s*s+u*u+v*v-2*s*u-2*s*v-2*u*v",
 'alpha_mass_dependence': "alpha=-(s+u-v)/(2.0*s)",
 'rho_mass_dependence': "rho=math.sqrt(lam)/(2.0*math.sqrt(s))",
 'beta_mass_dependence': "beta=math.sqrt(lam)/s",
 'numerator_uses_kinematics': "stripped_limit_massive(alpha,rho*unit_from(z,phi))",
 'affine_denominator_uses_kinematics': "alpha,rho,_,_=kin(u,v); r0=-a+alpha*q+c",
 'sphere_measure_uses_beta': "sphere=0.5*beta*sum(complex(coeff[k])*js[k] for k in range(POLY_DEGREE+1))",
}
observed={k:(v in src) for k,v in required.items()}
if not all(observed.values()):
    raise SystemExit(('parent_source_dependency_drift',observed))

formula=(
 "F(u,v)=1/2 beta(u,v) sum_k c_k(u,v) J_k(cc(u,v),aa(u,v)); "
 "F_uv=1/2[beta_uv S + beta_u S_v + beta_v S_u + beta S_uv], "
 "S_uv=sum_k[c_k,uv J_k + c_k,u J_k,v + c_k,v J_k,u + c_k J_k,uv]"
)
result={
 'iteration':ITERATION,
 'model_readiness_percent':24,
 'scientific_gate_pass':True,
 'candidate_residual':False,
 'classification':'PASS_CHANNEL2_FULL_AUXILIARY_MASS_CHAIN_DEPENDENCE_CONTRACT__NON_PROMOTING',
 'source_parent':'iteration407_tru1sq_channel4_analytic_spectral_reduction.py',
 'observed_dependencies':observed,
 'exact_chain_structure':formula,
 'negative_method_result':'DENOMINATOR_ONLY_MIXED_DERIVATIVE_IS_ALGEBRAICALLY_INCOMPLETE',
 'reason':(
   'u,v enter lambda and hence alpha,rho,beta; alpha/rho enter stripped_limit_massive '
   'and the affine denominator, while beta multiplies the sphere integral. Therefore '
   'a correct exact/AD fallback must differentiate the full frozen F(u,v), including '
   'kinematics, numerator/phi-mean coefficients, affine moments, and measure factor.'
 ),
 'guardrails':[
   'NO_PHYSICAL_DS_PROMOTION','NO_DENOMINATOR_ONLY_SHORTCUT','NO_SMALLER_H',
   'NO_THRESHOLD_WEAKENING','NO_ANGULAR_GRID_ESCALATION','NO_ANSATZ003','NO_FISHER_RESOURCES'
 ],
 'next_gate':(
   'Raw-consume Iteration 421. If CONVERGED, execute frozen Iteration 412 exact15 and '
   'do not invoke fallback. If BLOCKED_CONVERGENCE, implement Iteration 424 80/120-digit '
   'fixed-node fallback on the complete frozen F(u,v); any exact/AD derivative must obey '
   'this full-chain contract rather than differentiating only the affine denominator.'
 )
}
print(json.dumps(result,indent=2,sort_keys=True))
