# RQIR Candidate Gravity — Iteration 186

**Date:** 2026-08-31  
**Authoritative iteration:** 186  
**MODEL_READINESS: 24%**

## Starting authority

Restarted strictly from Iteration 185 after reading `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_185.md`, the latest research log, and recent commits. No prior Actions calculation was duplicated.

## Scientific target

Compute the full source-completed `QG-NL-EXP-001` lambda soft2 tangent at `lambda=1`, combine it with the frozen exact-`K2` local compensation, and quotient the resulting single conditioned nonlocal direction by the frozen Iteration-178 zero-`K2` local-C5 rank-4 curvature-cubic span.

## Result

For `F(Box)=(exp(-lambda Box)-1)/Box`, `d_lambda F|_1=-exp(-Box)`. Because all frozen external legs are TT, `R^(1)=0`; the cubic scalar piece `-(1/2)R dF R` is an exact protocol zero, including the `delta Box` terms. The remaining Ricci-tensor tangent was evaluated by the Iteration-185 exact covariant multilinear Box recursion through `Box^14`.

Series convergence is strong: `max|N14-N13|=1.51e-14`. The action calculator reproduces the Iteration-185 `Box^2..Box^4` columns exactly to stored precision.

Raw nonlocal lambda soft2:

`[4.0151619898,0.1885142177,6.8958645469,-2.1606040754,-0.6546536227,-0.7636291997]`.

After adding the frozen local hard-calibration compensation:

`S_cond=[4.6900726517,0.2789326350,8.5017458637,-3.0062751678,-0.7364444751,-0.7232162209]`.

Projection on the exact local rank-4 span leaves

`r=[0.0268839979,-0.1639003715,0.5945393888,-1.9589856765,1.8687871851,1.0763391630]`,

`||r||_2=2.9781805828`, `max|r|=1.9589856765`.

Frozen numerical envelope: `5.2625580e-6`; margin `||r||/envelope=5.659188e5`. Relative residual norm is `0.2913946` of `||S_cond||`.

## Classification

- `QG-NL-EXP-001`: **RESOLVED INDEPENDENT COMPARATOR DIRECTION** in the scoped hard-conditioned relation space.
- Relation to local C5: **not in the zero-K2 rank-4 local span** on the frozen rows.
- This is not Candidate Gravity novelty; it is comparator authority.
- Not consistency FAIL.
- Not exact comparator identity.
- Not near-degeneracy.
- No candidate residual has yet been tested against the augmented full comparator quotient.

Retain:

- `NL-NG-005 — FULL_QG_NL_EXP_001_LAMBDA_SOFT2_TANGENT_IS_RESOLVABLE_AFTER_EXACT_K2_COMPENSATION`;
- `REL-NG-004 — K2_PRESERVING_NONLOCAL_DIRECTION_SURVIVES_THE_FROZEN_ZERO_K2_LOCAL_C5_RANK4_QUOTIENT`;
- `NG-FUNNEL-040 — A_RESOLVED_NONLOCAL_COMPARATOR_DIRECTION_IS_NUISANCE_AUTHORITY_NOT_CANDIDATE_NOVELTY`.

## Readiness

Rubric remains:

- comparator foundation: `24/25`;
- robust unique residual discovery: `0/20`;
- frozen parent dynamics/ANSATZ: `0/20`;
- consistency/positivity/Ward/causality: `0/15`;
- identifiability/Fisher: `0/10`;
- resource/experiment closure: `0/10`.

`MODEL_READINESS: 24%`

Change from Iteration 185: **unchanged**. The nonlocal comparator is materially strengthened, but the comparator foundation cannot be awarded its final point while asymptotic-safety real-time/source-completed relation data and C3 ordered completion remain unresolved. There is still no robust candidate residual.

## Promotion/resource state

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Exact next gate

Iteration 187: freeze the augmented conditioned comparator span `span(V4,S_cond)` and audit the asymptotic-safety comparator directly in the same joint `(K2,S_soft2)` relation protocol. Do not infer a Lorentzian source-completed tangent from Euclidean symmetric-point data unless the published/reconstructed action uniquely determines it. If it does not, record `BLOCKED_AS_REALTIME_RELATION_COMPLETION` and preserve AS as unsupported rather than zero; then continue to the remaining C3 ordered-completion gate.
