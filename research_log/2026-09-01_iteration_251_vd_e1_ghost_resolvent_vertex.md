# Research Log — RQIR Candidate Gravity Iteration 251

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Authority recovered before work

Repository source of truth showed completed Iteration 250 despite `candidate_gravity/recovery/CURRENT_QG_FRONT.md` still naming Iteration 245. Iteration 250 retained `PASS_SCOPED_E1_E2_NO_NEW_LOOP_POLYGON_BEYOND_TRIANGLE` and specified the next gate: build the first explicit `e=1` mixed soft-hard pure-Einstein Vilkovisky numerator block, with a small symbolic/unit certificate preferred to a blind heavy run. No active GitHub Actions were present at startup.

## Work performed

Starting from the frozen 4D, `Lambda=0`, `a=-1/2` DeWitt convention and the primary 2020 pure-Einstein Vilkovisky operator

`N^alpha_beta = delta^alpha_beta Box + R^alpha_beta`,

the first TT-background variation of the ghost operator was derived analytically and independently checked by differentiating the full covariant vector-Laplacian-plus-Ricci operator on the Iterations-248/249 hard TT plane wave.

For `h_mu_nu = epsilon_mu_nu exp(i q.x)` with `q.epsilon=0` and `tr epsilon=0`, the frozen momentum-space vertex is

`delta N^alpha_beta = (epsilon^{mu nu} p_mu p_nu) delta^alpha_beta - (p.q) epsilon^alpha_beta - q_beta p_mu epsilon^{alpha mu} + q^alpha p_mu epsilon^mu_beta`.

The independent finite-difference certificate converges to the analytic matrix. At step `1e-6` the maximum component mismatch is `8.01e-11`; the analytic Frobenius norm is `1.0048840729158761`.

The corresponding resolvent insertion is fixed by

`delta(N^-1) = -N0^-1 (delta N) N0^-1`.

Because `U1` contains two ghost inverses, both placements are mandatory in the `E^(2) K^(1)` cubic metric-order block. This adds a repeated/raised ghost segment but no fourth loop-momentum corner, consistent with the Iteration-250 topology theorem.

## Result

`PASS_SCOPED_E1_GHOST_RESOLVENT_VERTEX_FREEZE_AND_TT_VALIDATION`.

This closes one real component of the 4D pure-Einstein VD numerator library. It does **not** close full `U1`, full C5, or any Candidate Gravity residual.

Retain:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and

`BLOCKED_NOT_ZERO`.

Still required inside the same `E^(2) K^(1)` block are the first variations of `R(DR)` and `Y`; additionally the `E^(3)`, surviving `E^(1)K^(2)`, `e=2`, Ward/source/contact and Lorentzian cut blocks remain.

## Guardrails

- No consistency FAIL was found.
- No exact comparator identity was claimed.
- No blocked comparator was zero-filled.
- No near-degeneracy or regime-specific non-identifiability classification applies to this algebraic unit.
- No novelty certificate exists.
- `ANSATZ-003` remains forbidden.
- Fisher/resources remain forbidden.
- No heavy Action was launched because the upstream numerator library is incomplete.

## Readiness

`MODEL_READINESS: 24%`

Change from Iteration 250: **0 pp**. The first explicit VD ghost-resolvent vertex is closed, but comparator foundation remains `24/25`; robust unique residual remains `0/20`; all downstream rubric blocks remain zero.

## Next exact gate

Iteration 252: derive `delta[R^i_gamma (D_i R^j_delta)] E^(2)_j` and `delta Y * E^(2)` in the same convention, then combine them with both frozen ghost-resolvent placements into the complete `E^(2) K^(1)` contribution to `Tr U1`. Require condensed-index/Ward consistency before tensor reduction or integration.
