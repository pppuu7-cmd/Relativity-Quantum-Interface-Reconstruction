# RQIR Candidate Gravity — Iteration 252

## U1 orbit-metric / ghost-matrix notation audit and TT gauge-weight variation

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Why this audit was required

Iteration 251 correctly differentiated the minimal vector ghost operator, but its prose used `N` for the operator that the primary paper denotes by `Nhat`. Before combining the remaining `E^(2)K^(1)` pieces this distinction must be frozen because the Vilkovisky definition contains the inverse orbit metric `N_orb^{-1}`, while the explicitly minimal operator in Eq. (53) is `Nhat = Y^up N_orb`.

Primary authority: Giacchini–de Paula Netto–Shapiro, *Vilkovisky unique effective action in quantum gravity*, Phys. Rev. D 102, 106006 (2020), especially Eqs. (5), (14), (16), (53)–(56).

## Exact matrix factorization

Let

`N_orb_{alpha beta} = R^i_alpha G_ij R^j_beta`

and

`Nhat^alpha_beta = Y^{alpha gamma} N_orb_{gamma beta}`.

Writing `W = Y^up`, one has

`Nhat = W N_orb`,

hence

`N_orb^{-1} = Nhat^{-1} W`.

The second inverse orbit metric in Eq. (16) is followed by `Y_down = W^{-1}`, therefore

`N_orb^{-1} Y_down = Nhat^{-1}`.

Consequently the exact operator orientation is

`U1 = Nhat^{-1} W [R.(D R).E] Nhat^{-1}`.

This is the key result of the audit. It shows that the two first-order `delta(Nhat^{-1})` placements computed in Iteration 251 are genuine and remain mandatory. The separate gauge-weight variation is not a third ghost-resolvent correction; it belongs to the single explicit factor `W` between the first resolvent and the `R(DR)E` kernel.

A deterministic matrix certificate gives maximum factorization error `1.11e-16`.

## TT variation of the explicit gauge-weight factor

For the DeWitt gauge used in the paper, the contravariant weight has the metric-density structure, up to the already frozen overall sign/normalization convention,

`W^{mu nu} proportional to sqrt(|g|) g^{mu nu}`.

With

`g_mu_nu = eta_mu_nu + a epsilon_mu_nu exp(i q.x)`

and TT conditions

`q_mu epsilon^{mu nu}=0`, `epsilon^mu_mu=0`,

the determinant variation vanishes at first order:

`delta sqrt(|g|) = (1/2) sqrt(|g|) epsilon^mu_mu = 0`.

Therefore

`delta W^{mu nu} / normalization = -epsilon^{mu nu}`.

On the exact hard TT polarization used in Iterations 248–251, symmetric finite differentiation of `sqrt(|g|) g^{-1}` at step `1e-6` agrees with `-epsilon^{mu nu}` to maximum component error

`5.44e-11`.

Classification:

`PASS_SCOPED_U1_ORBIT_GHOST_WEIGHT_FACTORIZATION_AND_TT_DELTA_WEIGHT`.

## Correct first-order E^(2)K^(1) decomposition

Defining `Ghat = Nhat^{-1}` and `A[E] = R.(D R).E`, the first-order kernel variation multiplying `E^(2)` is now frozen as

`delta U1|_{E2 K1} =`

`delta Ghat * W0 * A0[E2] * Ghat0`

`+ Ghat0 * delta W * A0[E2] * Ghat0`

`+ Ghat0 * W0 * delta A[E2] * Ghat0`

`+ Ghat0 * W0 * A0[E2] * delta Ghat`.

The first and fourth terms are the two Iteration-251 resolvent placements. The second term is closed by this iteration. The third term,

`delta[R^i_gamma (D_i R^j_delta)] E^(2)_j`,

remains the only missing first-order kernel factor before the complete `E^(2)K^(1)` numerator can undergo condensed-index/Ward testing.

## Scientific status

This iteration is a scoped algebraic/notation PASS, not a comparator coordinate and not a Candidate Gravity residual. It preserves rather than weakens the Iteration-251 ghost-resolvent result, while preventing an index-orientation mistake in the next assembly step.

Retain blocker:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`,

with `BLOCKED_NOT_ZERO`.

Heavy full C5 integration remains **not authorized**.

## Readiness

`MODEL_READINESS: 24%`

Change from Iteration 251: **0 percentage points**. The remaining `E^(2)K^(1)` ambiguity is reduced to one explicit kernel-variation block, but the physical C5 comparator is not yet complete.

## Exact next gate — Iteration 253

Derive and validate

`delta[R^i_gamma (D_i R^j_delta)] E^(2)_j`

in the same `D=4`, `Lambda=0`, `a=-1/2`, TT convention. Then assemble all four terms above and require a condensed-index/Ward consistency test before any tensor reduction or heavy loop integration. Do not create `ANSATZ-003`; do not run Fisher/resources.
