# RQIR Research Log — Iteration 170

**Date:** 2026-08-31  
**Branch:** Candidate Gravity / linear spectral funnel closure  
**MODEL_READINESS: 24%**

## Starting point

Iteration 169 left a five-dimensional timelike absorptive shape remainder after profiling the leading `O(p^4)` C5 constant massless-loop shape and the conservative `O(p^6)` C5 envelope `[x,x log x]`.

## Stronger question

Before computing finite-frequency asymptotic-safety data or scanning threshold masses, ask whether any positive shape in a single physical TT two-point response can be gravity-specific against C4.

## Generalization of Iteration 141

Iteration 141 proved exact Gaussian C4 equivalence for the special positive spectral continuum `KL-002`.

The proof never depended on its exponential density. For a physical conserved-traceless TT response with positive KL measure

`chi_R = Z0 D_R(0) + int dmu2 rho_TT(mu2) D_R(mu2)`, `rho_TT>=0`,

introduce independent positive-norm massive spin-2 fields with coupling density `sqrt(rho_TT)`.

Their direct-integral retarded response is identical to `chi_R` by construction.

With matching Gaussian state/covariance the Hadamard kernel and complete Gaussian CTP influence functional are also identical.

## Consequence

Thresholds, poles, branch cuts and arbitrary positive finite-frequency spectral shapes in the current linear TT sector remain C4-degenerate.

Therefore the five-dimensional Iteration-169 C5-null remainder is not a Candidate Gravity residual merely because a vector survives C5 or AS subtraction.

A non-positive spectral function does not fix this problem automatically: it instead triggers positivity, gauge-invariance, physical-observable, ghost and unitarity gates.

## Retained results

- `C4-NG-008 — POSITIVE_LINEAR_TT_SPECTRAL_RESPONSE_IS_EXACTLY_REPRESENTABLE_BY_ORDINARY_MEDIATOR_CONTINUUM`;
- `ABS-SHAPE-005 — FINITE_FREQUENCY_LINEAR_SPECTRAL_SHAPE_CANNOT_CERTIFY_GRAVITY_SPECIFIC_NOVELTY_AGAINST_C4`;
- `NG-FUNNEL-030 — LINEAR_SPECTRAL_RESIDUAL_REQUIRES_A_LINKED_NONLINEAR_OR_POST_GAUSSIAN_GRAVITY_RELATION_FOR_PROMOTION`.

## Numerical illustration

A six-node positive spectral tower evaluated on the eight timelike rows agrees with the same measure written as an explicit mediator sum to maximum floating-point difference `2.84e-14`.

This is illustration only; the equivalence is analytic.

## Strategic consequence

Do not spend heavy-compute budget reproducing the full Lorentzian-AS spectral curve merely to search for a gravity-specific **linear** residual. That curve remains valuable for comparator characterization and publication, but C4 already makes the linear spectral route non-promotable under positive spectral assumptions.

Return to the post-Gaussian Model→RQIR contract. The next search target must link the two-point sector to at least one higher object from the same dynamics, e.g. `C3sym`, `chi2R`, Ward/soft/constraint relation, or equivalent CTP three-point structure.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

Closing a false-positive search branch is valuable but does not produce a robust Candidate Gravity residual or parent dynamics. Comparator foundation remains `24/25` because the next required comparator problem is multi-point.

## Next gate

Iteration 171 should freeze a minimal **linked multi-point residual protocol** rather than another linear spectral shape:

1. retain the calibrated/positive linear TT spectral kernel as a shared input, not novelty;
2. add one symmetric connected three-point coordinate and one ordered second-order retarded coordinate tied to the same parent kernel/coupling;
3. construct fixed finite C3/C4/C5 comparator relation blocks in that linked coordinate space;
4. use Ward/soft/source completion as hard relations;
5. search for residual only in the quotient of those linked relations, never in the two-point spectrum alone.
