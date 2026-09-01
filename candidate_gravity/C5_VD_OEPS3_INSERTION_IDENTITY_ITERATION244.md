# RQIR Candidate Gravity — Exact Vilkovisky `O(epsilon^3)` Insertion Identity

**Iteration:** 244  
**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Question

Iteration 243 proved that on the frozen Minkowski, `Lambda=0`, finite-`R^3` target the Vilkovisky EOM/insertion series is needed only through `O(epsilon^3)`. It left the cubic coefficients and a possible primitive `U3` structure as an authority gap.

Can that gap be closed from primary Vilkovisky-DeWitt reduction authority rather than guessed from the quadratic 4D formula?

## Primary authority

Cho & Kantowski, *Vilkovisky-DeWitt Effective Action for Einstein Gravity on Kaluza-Klein Spacetimes `M^4 x S^N`*, arXiv:hep-th/0004082, derives the `U1,U2` reduction **before** specializing to the Kaluza-Klein backgrounds. In its general gauge-theory Section II, `U1` and `U2` are defined from the gauge generators, Green operators and equations of motion, traces of powers of the nonlocal connection operator are reduced to `U1,U2`, and Eq. (36) gives the resulting unique-action insertion series through fifth power in the EOM.

The published coefficients are

`+ 1/2 Tr U1`

`+ 1/4 Tr U1^2 - 1/2 Tr U2`

`+ 1/6 Tr U1^3 - 1/2 Tr(U1 U2)`

`+ 1/8 Tr U1^4 - 1/2 Tr(U1^2 U2) + 1/4 Tr U2^2`

`+ 1/10 Tr U1^5 - 1/2 Tr(U1^3 U2) + 1/2 Tr(U1 U2^2) + O(E^6)`.

The paper explicitly notes that the expansion is organized by powers of the first derivative `E_i` of the action and that the power required for the divergent application depends on spacetime dimension. Thus the **operator reduction algebra** precedes and is distinct from the later dimension-specific divergence extraction.

Giacchini, de Paula Netto & Shapiro, arXiv:2006.04217, Eq. (14), uses the same Barvinsky-Vilkovisky reduction strategy and writes in its 4D convention

`Gamma_bar^(1) = (i/2) Tr ln H - i Tr ln N - (i/2)(Tr U1 - Tr U2) - (i/4) Tr U1^2 + O(epsilon^3)`.

That paper explicitly points to Cho-Kantowski for `O(epsilon^3)` expressions.

## Exact algebraic identity

Assign noncommutative weighted degrees

`deg(U1)=1`, `deg(U2)=2`.

The entire Cho-Kantowski insertion sequence through the published fifth EOM degree is reproduced exactly by

`-1/2 Tr log(1 - U1 + U2)`

when words are combined only under cyclic trace equivalence.

This was checked in `candidate_gravity/code/iteration244_vd_insertion_series_identity.py` without commuting `U1` and `U2`.

The check reproduces all eleven independent cyclic terms through weighted degree five.

## Mapping to the 2020 4D convention

The 2020 Eq. (14) fixes the sign convention unambiguously. The connection series in that convention is the branch

`Gamma_conn = +(i/2) Tr log(1 - U1 + U2)`.

Its weighted degree `<=2` expansion is

`- i/2 Tr U1 + i/2 Tr U2 - i/4 Tr U1^2`,

which exactly reproduces Eq. (14).

Therefore its cubic part is fixed:

`Gamma_conn^(3) = + i/2 Tr(U1 U2) - i/6 Tr(U1^3)`.

No coefficient is obtained by extrapolating a quadratic pattern; the compact identity is independently certified by the higher-order published series and anchored to the 4D sign convention by Eq. (14).

## Correction to Iteration 243

Iteration 243 conservatively allowed a placeholder primitive topology `Tr(U3_a)` because the exact cubic reduction had not yet been recovered.

That placeholder is now **superseded** for this reduced Vilkovisky construction.

The general reduction through `O(E^5)` closes on `U1` and `U2`; at cubic EOM degree the required connection terms are exactly

- `Tr(U1^3)`;
- `Tr(U1 U2)`.

There is no independently required primitive `U3` operator in this reduced series.

Iteration 243 remains historically correct as an uncertainty ledger at the time it was written; its `U3_a` item must not be propagated as current authority.

## New scoped results

- `C5-CUT-025 — GENERAL_VD_REDUCTION_CLOSES_CUBIC_EOM_SECTOR_ON_U1_CUBED_AND_U1U2`.
- `C5-CUT-026 — CHO_KANTOWSKI_SERIES_EQUALS_NONCOMMUTATIVE_TRACE_LOG_THROUGH_EOM_DEGREE5`.
- `C5-CUT-027 — 4D_EQ14_FIXES_CUBIC_CONNECTION_SIGNS_PLUS_I_OVER2_U1U2_MINUS_I_OVER6_U1CUBED`.
- `C5-NG-021 — ITERATION243_PRIMITIVE_U3_PLACEHOLDER_SUPERSEDED_BY_PRIMARY_OPERATOR_AUTHORITY`.
- `NG-FUNNEL-098 — VD_CUBIC_COEFFICIENT_GAP_CLOSED_COMPOSITE_TRACE_MAP_REMAINS`.

## Classification

`PASS_EXACT_VD_OEPS3_INSERTION_SERIES_IDENTITY`.

The previous blocker

`BLOCKED_FULL_VD_EOM_INSERTION_SERIES_TO_FINITE_CPT3_MAP`

is narrowed to

`BLOCKED_COMPOSITE_U1_U2_TRACES_TO_FINITE_CPT3_MASTER_MAP_AND_PURE_GRAVITY_PROJECTION`.

## Heavy-compute decision

A full heavy finite-CPT3 run is **still not authorized yet**.

The exact cubic insertion coefficients are now known, but the composite traces contain inverse gauge-orbit/graviton operators. The next step must freeze how

- `Tr U1` through curvature dressing `R^2`,
- `Tr U2` and `Tr U1^2` through dressing `R^1`,
- `Tr U1^3` and `Tr(U1 U2)` at leading flat-kernel order

map to reusable finite nonlocal master traces/form factors and to the pure-gravity source-completed observable.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

The C5 authority gap is materially smaller, but the physical finite cubic C5 comparator column has not yet been computed.

## Next gate — Iteration 245

Build the composite-trace master map. Do not perform the full tensor contraction blindly.

1. write `U1,U2` in the frozen 4D pure-Einstein convention in terms of `N^{-1}`, `H^{-1}`, gauge-generator derivatives and EOM insertions;
2. reduce the needed five trace sectors by total curvature order;
3. classify each as a one-, two-, or three-propagator nonlocal master topology;
4. determine which are covered by published CPT form factors and which require new mixed inverse-operator parameter integrals;
5. derive flat-kernel momentum-space representations for the two cubic EOM traces;
6. only then decide the minimal heavy symbolic/numerical workflow.
