# RQIR Candidate Gravity — Iteration 254

## First background variation of the diffeomorphism generator and scoped `K1 E2` decomposition

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Frozen parent

Keep the same Candidate Gravity C5 parent and conventions already frozen upstream: `D=4`, `Lambda=0`, DeWitt gauge parameter `a=-1/2`, linear covariant-metric background split for the present local generator calculation, and the exact Iteration-252 factorization

`U1 = Nhat^-1 W [R.(D R).E] Nhat^-1`.

No proxy observable, no new ansatz, and no change of parameter convention is introduced.

## Diffeomorphism generator

For the covariant metric variable,

`R_g(xi)_{mu nu} = (L_xi g)_{mu nu}`

and, with

`g_mu_nu = eta_mu_nu + a eps_mu_nu exp(i q.x)`,

`xi^mu = c^mu exp(i p.x)`,

the first background variation, stripping the common Fourier factor `i exp(i(p+q).x)`, is

`delta R_mu_nu = (c.q) eps_mu_nu + p_mu eps_{rho nu} c^rho + p_nu eps_{mu rho} c^rho`.

For the frozen TT test polarization used by the reproducible certificate,

`q_mu eps^{mu nu}=0`, `eps^mu_mu=0`,

and a symmetric finite-difference test of the full Lie derivative reproduces the analytic first variation with maximum component error `3.05e-12` at step `1e-5`.

Freeze the scoped result:

`PASS_SCOPED_DIFFEO_GENERATOR_FIRST_VARIATION`.

## Important structural simplification

In the linear covariant-metric split the Lie derivative is affine in the metric. Therefore

`R^j_{delta,ik}=0`

and hence the explicit background variation of the ordinary field derivative vanishes:

`delta(partial_i R^j_delta)=0`.

Define

`B^j_{i delta} = D_i R^j_delta = partial_i R^j_delta + Gamma^j_{ik} R^k_delta`.

Then at first background order

`delta B^j_{i delta} = (delta Gamma^j_{ik}) R0^k_delta + Gamma0^j_{ik} delta R^k_delta`.

Consequently the missing Iteration-252 kernel variation multiplying `E^(2)` decomposes exactly as

`delta A_gamma delta[E2] =`

`(delta R^i_gamma) B0^j_{i delta} E2_j`

`+ R0^i_gamma Gamma0^j_{ik} (delta R^k_delta) E2_j`

`+ R0^i_gamma (delta Gamma^j_{ik}) R0^k_delta E2_j`.

Equivalently, there is **no independent `delta(partial R)` vertex** in this split. The only genuinely new background-dependent field-space-geometric object not already reduced to `delta R` is the first variation of the same-parent field-space Christoffel symbol, `delta Gamma`.

Freeze:

`PASS_SCOPED_DIFFEO_GENERATOR_FIRST_VARIATION_AND_K1_DECOMPOSITION`.

## Relation to Iteration 253 Ward guardrail

This result does not authorize a standalone symmetry/Ward FAIL for `K1 E2`. The exact cubic Ward target remains the complete same-parent sum

`K0 E3 + K1 E2 + K2 E1`.

The present decomposition only narrows the explicit numerator library needed for the middle partition.

## Scientific status

This is a scoped algebraic and numerical PASS. It is not:

- a C5 comparator coordinate;
- an exact comparator identity;
- a Candidate Gravity residual;
- a consistency PASS for the full cubic Vilkovisky sector;
- a reason to run Fisher/resources.

Retain the umbrella status

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`,

`BLOCKED_NOT_ZERO`.

The blocker is now narrower: for this sub-block, the remaining genuinely new geometric vertex is `delta Gamma`, followed by assembly with the two `delta(Nhat^-1)` placements, `delta W`, and the already explicit `delta R` pieces.

## Reproducibility

- `candidate_gravity/code/iteration254_vd_diffeo_generator_k1_decomposition.py`
- `candidate_gravity/results/iteration254_vd_diffeo_generator_k1_decomposition.json`

## Readiness

`MODEL_READINESS: 24%`

Change from Iteration 253: **0 percentage points**. The `K1 E2` numerator ambiguity is reduced, but no physical comparator coordinate or robust nonzero residual has closed.

## Exact next gate

Derive `delta Gamma^j_{ik}` from the same frozen field-space metric/connection convention, validate it in a pointwise TT background check, and assemble the complete `delta A[E2]` block together with both `delta(Nhat^-1)` placements and `delta W`. In parallel prepare the minimal same-parent `K0E3` and `K2E1` siblings required before any final cubic Ward/symmetry certificate. Heavy tensor integration, Fisher/resources and `ANSATZ-003` remain forbidden.
