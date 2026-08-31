# Candidate Gravity — Iteration 183: split-invariant joint K2/soft2 conditioning

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**  
**Status:** relation observable repaired; comparator cubic completion still open

## Why the Iteration-182 blocker should not be solved by choosing an arbitrary W[K2]

Iteration 182 proved that for nonzero quadratic kernel the off-shell split

\[
\Gamma^{(3)}_{\rm soft}=\mathcal W[K^{(2)}]+R^{(1)}:B+\cdots
\]

has a transverse repartition freedom. An internal choice of `W` therefore must not become the physical RQIR discriminator.

The correct RQIR construction is to keep directly source-completed observables and impose the quadratic calibration as a hard relation.

## Frozen split-invariant observable

For the six null-soft rows define

\[
Y=(K_i,S_i),\qquad i=1,\ldots,6,
\]

where

- `K_i` is the calibrated physical TT quadratic inverse kernel on the hard row;
- `S_i` is the **full source-completed** coefficient of the cubic response at `O(k_soft^2)` in the same metric/source convention.

Do not split `S_i` into a separately observable Ward part and transverse part.

For comparator/nuisance parameters `theta`, define tangent blocks

\[
A=\frac{\partial K}{\partial\theta},\qquad
B=\frac{\partial S}{\partial\theta}.
\]

Exact quadratic calibration requires

\[
A\,\delta\theta=0.
\]

If `N_A` spans `ker A`, the allowed cubic comparator tangent after hard calibration is

\[
\boxed{B_{\rm cond}=B N_A}.
\]

This is the relation-level quantity to use before any residual or Fisher calculation.

## Split invariance

Because only the full `S` is used, any internal bookkeeping shift

\[
W\to W+C,\qquad B_{\rm internal}\to B_{\rm internal}-C
\]

leaves the observable unchanged. A deterministic six-row numerical check gives maximum discrepancy

`4.4408920985e-16`.

Retain:

`REL-NG-001 — JOINT_K2_SOFT2_HARD_CONDITIONING_IS_INVARIANT_UNDER_INTERNAL_WARD_TRANSVERSE_REPARTITION`.

This is also closer to the repository's earlier hard-constraint doctrine: exact calibration is eliminated before nuisance profiling rather than encoded as a penalty.

## Quadratic finite-row audit

Use the same six hard invariants

`x=q^2=[0.5076,0.3854,0.4260,0.3153,0.4004,0.2882]`.

The already-authorized local TT quadratic inverse-kernel basis through the frozen dimension-12 convention, including a common EH/normalization direction, is proportional to

\[
[x,x^2,x^3,x^4,x^5,x^6].
\]

On the six rows:

- rank = `6/6`;
- condition number = `2.398198742e7`;
- smallest singular value = `4.42623e-8`.

For the fixed exponential nonlocal model

\[
K_{NL}(x)=x e^{\lambda x},
\]

at `lambda=1`,

\[
\partial_\lambda K_{NL}=x^2 e^x.
\]

Appending this seventh parameter direction to the six local quadratic columns leaves row rank 6, hence produces one parameter-space null direction. Normalizing the nonlocal coefficient to `+1`, the compensating local coefficients are approximately

`[3.72282e-5, -1.00059168, -0.99612543, -0.51334123, -0.14137283, -0.06615095]`.

The quadratic null residual is `1.65e-16`.

Thus the nonlocal quadratic change can be exactly hidden at these six sampled points by a local dimension-12 polynomial completion. This reproduces the finite-sample saturation logic of earlier RQIR work and explains the strong near-degeneracy found in Iteration 181.

Retain:

`NL-NG-006 — SIX_ROW_NONLOCAL_K2_TANGENT_HAS_AN_EXACT_LOCAL_POLYNOMIAL_COMPENSATION_DIRECTION_AT_FROZEN_DIMENSION12_RESOLUTION`.

## New missing C5 requirement

The physical conditional nonlocal discriminator is **not** just the raw nonlocal cubic column. It is the full soft2 cubic response of the one parameter combination that keeps the quadratic kernel fixed.

Therefore the same local quadratic EFT directions used to compensate `delta K` need their source-completed cubic `S_soft2` columns. In particular the `R_{mu nu} Box^n R^{mu nu}` family through the frozen dimension-12 order cannot be omitted from the joint relation quotient merely because the earlier `B_T` calculation focused on operators with `K2=0`.

Retain:

`C5-NG-010 — LOCAL_QUADRATIC_EFT_SOFT2_COMPLETIONS_ARE_REQUIRED_WHEN_THEIR_K2_DIRECTIONS_COMPENSATE_NONLOCAL_CALIBRATION`.

## Funnel rule

`NG-FUNNEL-041 — CONDITION_FULL_SOURCE_COMPLETED_SOFT2_ON_CALIBRATED_K2_INSTEAD_OF_PROMOTING_AN_OFFSHELL_W_B_SPLIT`.

The conceptual `B_T` notation remains useful for zero-`K2` operator sectors, but for general comparators the authoritative relation observable is now the joint `(K2,S_soft2)` hard-conditioned quotient.

## Scientific classification

- joint relation protocol: `FROZEN_SPLIT_INVARIANT`;
- six-row nonlocal quadratic direction: `EXACT_FINITE_SAMPLE_LOCAL_COMPENSATION`;
- conditional nonlocal soft2 direction: `BLOCKED_MISSING_LOCAL_QUADRATIC_AND_NONLOCAL_FULL_SOFT2_CUBIC_COLUMNS`;
- no consistency FAIL;
- no novelty certificate.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

The protocol is now physically better posed, but comparator foundation remains `24/25` until the conditional cubic columns and remaining C3/nonlocal/AS relation boundaries permit one actual full quotient.

## Exact next gate — Iteration 184

Compute the **source-completed soft2 cubic columns of the local quadratic C5 EFT directions** used in the six-row `K2` compensation, starting with `R_{mu nu}R^{mu nu}` and derivative descendants through the frozen dimension-12 order.

Then combine them with the full `QG-NL-EXP-001` soft2 cubic tangent to form the single calibrated nonlocal direction `B_cond`/`S_cond`. Do not compare the raw nonlocal cubic alone.
