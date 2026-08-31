# Candidate Gravity — Iteration 203: shared-Wilson cross-polarization derivative-tower audit

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Motivation

Iteration 202 proved that the declared local `RiemannChain Box^n` family can saturate either twelve-row v3 polarization protocol separately when sufficiently many derivative orders are admitted. However, a physical C5 theory has one set of Wilson coefficients. It cannot choose separate coefficients merely because the TT polarization setting changes.

Therefore stack the two frozen protocols vertically:

`Y_stack=(Y_A,Y_B)`

and require the same coefficient `c_n` for operator `O_n` in both halves.

## Shared-family form

For the Riemann-chain family,

`S_A(i)=r_A(i) f(x_i)`,

`S_B(i)=r_B(i) f(x_i)`,

with the same scalar analytic function

`f(x)=c_0 + (2/3) sum_{n>=1} c_n (-x)^n`.

Thus at every hard node

`r_B(i) S_A(i) - r_A(i) S_B(i) = 0`.

These are twelve exact cross-polarization relations for this family, independent of derivative order.

## Rank result

Using Box powers `n=0,...,11`, the stacked matrix has shape `24 x 12` and rank

`12`.

Hence its left-null dimension is `12`.

The twelve row-pair relation functionals above have rank 12 and annihilate the 12-column tower to maximum floating error `9.03e-16`.

The stacked singular values are

`[16.4732983, 4.49246017, 0.331783354, 0.0687120905, 8.94270e-3, 8.10814e-4, 7.54949e-5, 9.18125e-6, 6.81965e-7, 2.79950e-8, 2.40646e-10, 1.80034e-12]`.

The very large condition number (`~9.15e12`) is a finite-noise warning, not a change to exact rank.

## Scientific meaning

### `REL-NG-016 — SHARED_WILSON_RIEMANN_DERIVATIVE_TOWER_HAS_TWELVE_EXACT_CROSS_POLARIZATION_RELATIONS_ON_V3_A_PLUS_B`

The family cannot independently interpolate the two polarization responses at a common hard node. Their ratio is locked by the two base carriers.

### `C5-NG-020 — SINGLE_ANALYTIC_TENSOR_FAMILY_SATURATES_EACH_12ROW_PROTOCOL_SEPARATELY_BUT_ONLY_RANK12_ON_THE_COMMON_COEFFICIENT_24ROW_STACK`

Finite-point interpolation is much less destructive when physical comparator coefficients are shared across genuinely different observable settings.

### `NG-FUNNEL-058 — PHYSICAL_COMPARATOR_COEFFICIENTS_MUST_BE_SHARED_ACROSS_POLARIZATION_PROTOCOLS_BEFORE DECLARING FINITE INTERPOLATION DEGENERACY OR RESIDUAL`

Neither independent nuisance fits nor union-rank counting are the correct physical comparator for one theory measured in multiple settings.

## Critical limitation

These twelve relations are exact only for the single declared Riemann-chain derivative family.

They are **not yet full-C5 null relations**. General gravitational EFT has higher-dimension local operators of arbitrary dimension, and derivative/tensor contractions beyond `Box^n` on one Riemann factor can generate different polarization carriers. Modern gravitational EFT operator-basis work explicitly constructs independent structures after EOM/IBP redundancies and extends systematically to higher dimension.

Therefore the correct status is

`FULL_ALL_ORDERS_C5_TENSOR_BASIS = BLOCKED`.

No cross-polarization residual may be promoted until that risk is bounded.

## Protocol consequence

Iteration 201's separate A/B robustness remains useful as an anti-overfitting check, but Iteration 202 shows that allowing unlimited independent local-EFT fits in each protocol is too permissive. Before candidate construction, a new shared-coefficient joint protocol may be preregistered as the primary physical comparator test, with separate A/B residual checks retained as robustness diagnostics rather than independent Wilson refits.

No such candidate test is performed here.

## Readiness

`MODEL_READINESS: 23%`, unchanged from Iteration 202.

The cross-polarization relation is promising, but comparator foundation remains reopened by the unbounded full C5 tensor remainder and by AS/C3 real-time nonlinear blockers.

## Next gate

Iteration 204 should attack the C5 remainder in one of two rigorous ways:

1. derive a controlled low-energy EFT truncation/remainder bound on a newly preregistered `x << 1` protocol; or
2. enumerate the independent parity-even cubic/higher-derivative tensor carriers relevant to the null-soft two-hard-TT cross-polarization relation, using a nonredundant gravitational EFT/amplitude basis, and test whether more than one independent carrier survives.

In parallel continue AS and C3 authority searches. No `ANSATZ-003`, Fisher or resource work.
