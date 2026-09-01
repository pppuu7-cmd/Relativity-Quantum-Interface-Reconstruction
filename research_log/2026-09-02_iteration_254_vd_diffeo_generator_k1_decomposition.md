# RQIR research log — Iteration 254

Date: 2026-09-02

Recovered authoritative Candidate Gravity front at Iteration 253 from `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_253.md`, the latest research log and recent commits. GitHub Actions had no active or historical runs in the repository endpoint at the start of this iteration.

Continued the frozen C5 Vilkovisky authority-improvement program without proxy observables or ansatz promotion.

For the covariant metric variable the diffeomorphism generator is the Lie derivative `R_g(xi)=L_xi g`. In the linear background split `g=eta+a eps exp(i q.x)`, its first background variation is

`delta R_mu_nu = (c.q) eps_mu_nu + p_mu eps_{rho nu} c^rho + p_nu eps_{mu rho} c^rho`

up to the common Fourier factor. A deterministic TT finite-difference test reproduces this expression to maximum component error `3.05e-12` at step `1e-5`.

Because `L_xi g` is affine in the covariant metric, `R_,ik=0`. Thus, writing `B_i^j=D_iR^j=partial_iR^j+Gamma^j_ik R^k`, the first variation obeys

`delta B = deltaGamma * R0 + Gamma0 * deltaR`.

Therefore the remaining Iteration-252 kernel variation multiplying `E2` is exactly reduced to

`deltaA[E2] = deltaR * B0 * E2 + R0 * Gamma0 * deltaR * E2 + R0 * deltaGamma * R0 * E2`.

There is no independent `delta(partial R)` vertex in this split. The only genuinely new field-space-geometric vertex in this sub-block is `deltaGamma`.

Freeze `PASS_SCOPED_DIFFEO_GENERATOR_FIRST_VARIATION_AND_K1_DECOMPOSITION`.

Iteration-253 guardrail remains binding: no standalone Ward/symmetry FAIL may be inferred from `K1E2`; the exact cubic target is `K0E3+K1E2+K2E1`.

Umbrella C5 status remains `BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`, `BLOCKED_NOT_ZERO`.

No robust Candidate Gravity residual. `ANSATZ-003` not created. Heavy C5 integration, Fisher and resources not launched.

MODEL_READINESS: 24%

Change from Iteration 253: 0 percentage points. A real numerator-library ambiguity was removed, but no comparator-rubric block or robust residual closed.

Next gate: derive and validate same-parent `deltaGamma`, assemble complete `deltaA[E2]` with both ghost-resolvent placements and `deltaW`, and prepare `K0E3`/`K2E1` before any final cubic Ward certificate.
