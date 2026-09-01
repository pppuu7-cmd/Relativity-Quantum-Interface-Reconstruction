# Recovery delta — RQIR Iteration 254

**Date:** 2026-09-02  
**MODEL_READINESS:** 24%  
**Candidate Gravity authoritative front:** Iteration 254

## New frozen result

In the same frozen `D=4`, `Lambda=0`, `a=-1/2` Candidate Gravity C5 parent and linear covariant-metric split, the diffeomorphism generator is the metric Lie derivative.

Its first TT background variation is

`delta R_mu_nu = (c.q) eps_mu_nu + p_mu eps_{rho nu} c^rho + p_nu eps_{mu rho} c^rho`

up to the common Fourier phase. A reproducible symmetric finite-difference test agrees to `3.05e-12` maximum component error at step `1e-5`.

Because the generator is affine in the covariant metric, `R_,ik=0`. Defining

`B_i^j = D_i R^j = partial_i R^j + Gamma^j_ik R^k`,

one has

`delta B = deltaGamma * R0 + Gamma0 * deltaR`.

Hence the explicit first-order kernel variation multiplying `E2` reduces to

`deltaA[E2] = deltaR * B0 * E2 + R0 * Gamma0 * deltaR * E2 + R0 * deltaGamma * R0 * E2`.

There is no independent `delta(partial R)` vertex in the linear covariant-metric split.

Freeze:

`PASS_SCOPED_DIFFEO_GENERATOR_FIRST_VARIATION_AND_K1_DECOMPOSITION`.

## Guardrail retained

Do not impose a standalone cubic Ward/symmetry FAIL on `K1E2`. Iteration 253 proved that the exact same-parent cubic constraint applies to

`K0E3 + K1E2 + K2E1`.

## Status

Retain

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`,

`BLOCKED_NOT_ZERO`.

This remains an operational/derivational blocker, not a consistency FAIL, exact comparator identity, near-degeneracy, regime-specific non-identifiability, or novelty certificate.

No robust Candidate Gravity residual. `ANSATZ-003` not created. Heavy integration, Fisher and resources remain forbidden.

## Files

- `candidate_gravity/C5_VD_DIFFEO_GENERATOR_K1_DECOMPOSITION_ITERATION254.md`
- `candidate_gravity/code/iteration254_vd_diffeo_generator_k1_decomposition.py`
- `candidate_gravity/results/iteration254_vd_diffeo_generator_k1_decomposition.json`
- `research_log/2026-09-02_iteration_254_vd_diffeo_generator_k1_decomposition.md`
- `recovery/RECOVERY_DELTA_ITERATION_254.md`

## Readiness

`MODEL_READINESS: 24%`

Change from Iteration 253: **0 percentage points**. The explicit middle-partition numerator library is narrower, but no physical comparator coordinate or robust nonzero residual has closed.

## Next gate — Iteration 255

Derive `deltaGamma^j_ik` from the same frozen field-space metric/connection convention, validate it on a pointwise TT background, and assemble the complete `deltaA[E2]` block with both `delta(Nhat^-1)` placements and `deltaW`. Prepare the sibling `K0E3` and `K2E1` partitions before any final cubic Ward/symmetry certificate. Do not launch heavy integration, Fisher/resources, or create `ANSATZ-003`.
