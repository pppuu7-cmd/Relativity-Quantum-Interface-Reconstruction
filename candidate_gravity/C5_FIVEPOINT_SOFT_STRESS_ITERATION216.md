# Candidate Gravity — Iteration 216: physical C5 five-point soft stress test

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**  
**Status:** physical on-shell C5 cut compression stress-tested; off-shell linked `T_cut` still BLOCKED

## Starting authority

Iteration 215 produced the first executable IR-subtracted pure-Einstein five-graviton total-s cut on the frozen twelve-point soft grid, with a pointwise conservative numerical error envelope. Its six-column `n<=2` regular+log fit resolved logarithmic structure but left a truncation residual above numerical error.

Iteration 216 asks a target-independent question: what is the first regular+log soft order that describes the **physical finite vector** within its declared numerical error, and how stable is that compression under fixed window changes?

## Primary authority rule

The primary comparator datum is now frozen as

`{ I_finite(epsilon_i), sigma_num(epsilon_i) }`, `i=1..12`.

Any regular+log coefficients are a compression of that physical vector. They are not allowed to replace it as exact comparator authority.

## Full-window result

Define

`F(epsilon)=epsilon I_finite(epsilon)`,

`z=epsilon/epsilon_max`,

`L=log(epsilon/epsilon_ref)`.

### Through n=2

Basis:

`[1,L,z,zL,z^2,z^2L]`.

- condition number: `4264.620104`;
- relative L2 residual: `2.79124e-7`;
- maximum pointwise residual/error: `1209.93`;
- RMS residual/error: `368.37`.

Thus the `n<=2` physical representation is decisively incomplete relative to the declared numerical precision.

### Through n=3

Add `[z^3,z^3L]`.

- condition number: `2.79550e5`;
- relative L2 residual: `5.09786e-10`;
- maximum pointwise residual/error: `0.637404`;
- RMS residual/error: `0.246654`.

Therefore `n<=3` is the **first tested frozen regular+log order that describes every physical grid point within the conservative numerical envelope**.

This is a numerical completeness statement on the frozen finite window, not a theorem that the asymptotic series terminates at `n=3`.

## Fixed window stress test

Relative coefficient changes against the full 12-point `n=3` fit are:

- drop two largest epsilon: `5.47e-4`;
- drop four largest epsilon: `2.96e-3`, but the resulting 8-point/8-parameter interpolation is extremely ill-conditioned and is not used as evidence;
- drop two smallest epsilon: `1.27e-4`;
- drop both endpoints: `2.62e-4`.

A deterministic perturbation bounded pointwise by the declared numerical errors changes the full coefficient vector by `1.17e-3`; a conservative L2 pseudoinverse bound is `4.87e-3`.

Hence the observed window shifts are comparable to or below the conservative coefficient-compression uncertainty.

## Out-of-window prediction

The asymmetry is physically informative.

An `n=3` fit to the ten **larger-epsilon** points predicts the two smallest-epsilon points with maximum error only `0.196` times their numerical error.

By contrast, an `n=3` fit to the ten **smaller-epsilon** points misses the two largest-epsilon points by more than `2.16e4` times their numerical error.

Thus higher-order finite-soft content is genuinely resolved at the large-epsilon edge. A small-epsilon asymptotic fit must not be extrapolated across the entire frozen window and called exact.

## Retained results

- `C5-CUT-016 — N3_REGULAR_LOG_BASIS_IS_THE_FIRST_FROZEN_ORDER_THAT_DESCRIBES_THE_PHYSICAL_FIVE_GRAVITON_CUT_WITHIN_ITS_DECLARED_NUMERICAL_ERROR`;
- `SOFT-NG-009 — REGULAR_LOG_COEFFICIENTS_ARE_COMPRESSION_NOT_PRIMARY_COMPARATOR_AUTHORITY_WHEN_HIGH_EPSILON_HIGHER_ORDER_CONTENT_IS_RESOLVED`;
- `NUM-NG-018 — PHYSICAL_LOOP_COMPARATOR_AUTHORITY_IS_THE_FINITE_VECTOR_PLUS_POINTWISE_ERROR_ENVELOPE_NOT_A_WINDOW_DEPENDENT_ASYMPTOTIC_FIT`;
- `NG-FUNNEL-073 — CANDIDATE_QUOTIENTS_MUST_PROPAGATE_PHYSICAL_COMPARATOR_VECTOR_ERRORS_AND_SOFT_TRUNCATION_SEPARATELY`.

## Comparator implications

The on-shell pure-Einstein nonanalytic control is now numerically robust enough to be used as a **physical positive control**. It still does not replace the off-shell/source-completed linked RQIR object

`T_cut = D Gamma3_ret,soft - W[D K2]`.

The latter remains blocked by the gauge-safe/source-completed C5 specialization. AS and C3 nonlinear real-time cut columns also remain blocked and are never zero-filled.

## Readiness

`MODEL_READINESS: 23%` — unchanged.

This iteration closes representation/robustness uncertainty for the on-shell C5 positive control, but does not close the missing comparator-foundation objects required for a full linked quotient. No `ANSATZ-003`; no Fisher/resources.
