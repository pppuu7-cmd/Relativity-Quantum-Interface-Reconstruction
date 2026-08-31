# Candidate Gravity — Iteration 185 local quadratic C5 soft2 completion

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Scope

Complete the frozen dimension-12 local quadratic C5 bridge in the joint relation observable

`Y=(K2_rows,S_soft2_full_rows)`

without inferring higher-derivative cubic columns from lower-order values by row-wise powers of `q^2`.

The same six null-soft TT rows and parameter convention from Iterations 183–184 are retained.

## Method

A formal multilinear plane-wave expansion of the metric is constructed through cubic order. Each perturbative monomial is represented by a subset mask of the three external legs. From this single expansion we derive:

1. `g^{-1}` as a formal matrix series;
2. `sqrt(-g)` from the determinant series;
3. Christoffel symbols and Ricci tensor;
4. a recursive fully covariant d'Alembertian acting on a rank-2 tensor;
5. the cubic coefficient of

   `sqrt(-g) R_mn Box^n R^mn`

   for `n=0..4`.

Because the Box is applied recursively to the full rank-2 Ricci series, connection terms, inverse-metric variation and variation of the differential operator itself are included automatically. This is the covariant completion that was missing at Iteration 184.

The `O(k_soft^2)` coefficient is extracted with a symmetric soft second difference and two Richardson levels.

## New dimension-12 columns

For `R_mn Box^2 R^mn`:

`[-1.1165183849,-0.0138751458,-1.6820857577,0.2756448325,0.2663354180,0.2728910445]`

For `R_mn Box^3 R^mn`:

`[0.7133600700,0.0017605282,1.0529592750,-0.1111297369,-0.2235239287,-0.1459711976]`

For `R_mn Box^4 R^mn`:

`[-0.4308356613,0.0013520156,-0.6274976618,0.0431046862,0.1618211492,0.0674407295]`

Maximum soft-extrapolation errors are respectively

`1.99e-10`, `3.04e-10`, `1.58e-10`.

## Source-completed Ward certificate

Using the same metric dynamics and nonlinear Lie contact completion, the maximum absolute residuals are

- n=2: `3.47e-18`;
- n=3: `6.94e-18`;
- n=4: `1.25e-19`.

Maximum relative residuals are below `5.3e-14`.

Status: `PASS_MACHINE_PRECISION_SCOPED`.

## Cross-check against Iteration 184

The formal method reproduces the n=0 and n=1 structures but shifts the previous nested-position-space numerical values by at most

- Ricci2: `2.30e-7`;
- RicciBoxRicci: `6.54e-7`.

This does not indicate a physics inconsistency. Iteration 184's quoted error estimated only the soft Richardson extrapolation; it did not include the independent finite-position step used there to construct derivatives of Ricci. The formal plane-wave calculus removes that hidden discretization.

Therefore the Iteration-185 formal columns should be used for subsequent compensation calculations.

## Hard-conditioned local compensation is now complete

Using the exact Iteration-183 K2-null vector with nonlocal coefficient normalized to +1,

`[3.7228200e-5,-1.0005916758,-0.9961254264,-0.5133412289,-0.1413728260,-0.0661509490,1]`,

the six local components correspond to

`[EH,Ricci2,RicciBoxRicci,RicciBox2Ricci,RicciBox3Ricci,RicciBox4Ricci]`.

Their complete source-completed soft2 compensation piece is

`[0.6749106619,0.0904184173,1.6058813167,-0.8456710924,-0.0817908525,0.0404129788]`.

Thus the remaining nonlocal gate is sharply defined: compute the full `QG-NL-EXP-001` lambda soft2 tangent from its parent action and add this fixed local compensation vector before any quotient/rank claim.

## Retained results

- `C5-NG-013 — COVARIANT_RICCI_BOX2_TO_BOX4_SOFT2_LADDER_IS_NONTRIVIAL_AND_NOT_GENERATED_BY_ROW_WISE_Q2_MULTIPLICATION`;
- `NUM-NG-003 — NESTED_POSITION_SPACE_DIFFERENCING_CAN_UNDERSTATE_TOTAL_OPERATOR_CALCULUS_ERROR_EVEN_WHEN_SOFT_RICHARDSON_ERROR_IS_SMALL`;
- `REL-NG-003 — DIMENSION12_LOCAL_K2_COMPENSATION_NOW_HAS_A_COMPLETE_SOURCE_COMPLETED_SOFT2_VECTOR`.

## Classification

This is a positive comparator-completion result, not a Candidate Gravity residual.

- consistency FAIL: no;
- exact comparator identity: no new identity claimed;
- near-degeneracy: not the classification of the local ladder itself;
- operational BLOCKED: removed for the n=2..4 local ladder;
- novelty certificate: none.

`ANSATZ-003` remains intentionally absent. Fisher/resources remain forbidden.

## Next gate

Iteration 186: compute the full `QG-NL-EXP-001` lambda soft2 tangent, including the operator/Frechet variation implied by the exponential form factor; combine it with the fixed local compensation vector above; then compare the single K2-preserving conditioned nonlocal direction against the zero-K2 curvature-cubic span and the frozen numerical envelope.
