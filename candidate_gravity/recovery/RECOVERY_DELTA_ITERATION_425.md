# Recovery Delta — Iteration 425

Date: 2026-09-04

MODEL_READINESS: 24%

## Entry authority

- physical/operator authority: Iteration 411;
- structural authority: Iteration 410;
- numerical-method diagnosis: raw-valid Iterations 419 + 422 under the prospective Iteration-420 interpretation contract;
- source-of-truth reconciliation: Iteration 423;
- conditional high-precision fallback contract: Iteration 424;
- active physical run: Iteration 421, not duplicated.

## Scientific/methodological result

Audited the actual frozen Iteration-407 fixed-mass representation rather than assuming that the auxiliary masses enter only an uncut propagator denominator.

The source shows

`lambda=s^2+u^2+v^2-2su-2sv-2uv`,

so `u,v` change `alpha`, `rho`, and `beta`. `alpha,rho` feed both the traced numerator through `stripped_limit_massive(alpha,rho*n)` and the affine uncut denominator, while `beta` multiplies the complete sphere integral. Therefore the fixed-mass object has the dependency structure

`F(u,v)=1/2 beta(u,v) sum_k c_k(u,v) J_k(cc(u,v),aa(u,v))`.

Consequently an exact mixed derivative must retain the full product/chain rule,

`F_uv=1/2[beta_uv S + beta_u S_v + beta_v S_u + beta S_uv]`,

with

`S_uv=sum_k[c_k,uv J_k + c_k,u J_k,v + c_k,v J_k,u + c_k J_k,uv]`.

A denominator-only reciprocal-squared mixed derivative is therefore algebraically incomplete for this frozen representation. This is a negative methodological result, not a consistency FAIL and not a physical coordinate.

Classification: `PASS_CHANNEL2_FULL_AUXILIARY_MASS_CHAIN_DEPENDENCE_CONTRACT__NON_PROMOTING`.

Frozen guardrail added: if Iteration 421 remains `BLOCKED_CONVERGENCE`, the Iteration-424 80/120-digit fallback must evaluate/differentiate the complete frozen `F(u,v)`. Any future exact/AD representation must include kinematics, traced numerator/phi-mean coefficients, affine moments and the `beta` measure factor. It may not differentiate only the affine denominator.

No smaller `h`, no threshold weakening, no angular-grid escalation, no zero fill, no ANSATZ-003 and no Fisher/resources are authorized.

MODEL_READINESS: 24%

Change: 0 percentage points. A dangerous algebraic shortcut has been excluded, but index 2 has not acquired physical authority and no stable readiness-rubric block has closed.

## Exact next gate

Raw-consume Iteration 421 fail-closed. If it is `CONVERGED`, skip Iteration 424 and execute frozen Iteration-412 exact15 assembly. If it is `BLOCKED_CONVERGENCE`, implement Iteration-424 fixed-node 80/120-digit evaluation of the complete frozen `F(u,v)` subject to the Iteration-425 full-chain derivative contract.
