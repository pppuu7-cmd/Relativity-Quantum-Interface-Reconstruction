# RQIR Candidate Gravity — C5 Vilkovisky Finite-Cubic Bookkeeping

**Iteration:** 243  
**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Purpose

Iteration 233 established that the published 4D Vilkovisky unique-action reduction

`Gamma1 = (i/2) Tr ln H - i Tr ln N - (i/2)(Tr U1 - Tr U2) - (i/4) Tr U1^2 + O(epsilon^3)`

is truncated at `O(epsilon^2)` because that is sufficient for the **D=4 divergent part**, not because higher insertions vanish.

Iteration 242 selected C5 full-Vilkovisky finite-CPT3 completion as the highest-priority authority-improvement route.

The present iteration asks a narrower question: **how much of the full EOM/insertion series is actually required for the frozen finite curvature-cubic target?**

## Frozen scope

- flat/Minkowski expansion;
- `Lambda = 0`;
- target: finite one-loop effective action through total curvature order `O(R^3)`;
- same pure-Einstein Vilkovisky convention retained from Iterations 231–233.

On this scope the Einstein equations of motion satisfy schematically

`epsilon_i = S_,i = O(R)`

around flat space.

Introduce a bidegree:

- `e` = explicit EOM/insertion degree (`epsilon^e`);
- `c` = additional background-curvature degree coming from kernels, covariant derivatives, commutators, potentials and propagator/vertex dressing.

A term can contribute to finite curvature-cubic order only when

`e + c <= 3`.

## Finite truncation theorem

Therefore:

- `e=0` determinant sector requires background expansion through `c=3`;
- `e=1` connection sector requires dressing only through `c=2`;
- `e=2` sector requires dressing only through `c=1`;
- `e=3` sector is needed only at leading `c=0` flat-kernel order;
- **all `e>=4` Vilkovisky EOM-insertion terms are irrelevant to the frozen `O(R^3)` target.**

This is a scoped curvature-counting theorem. It does not apply unchanged at nonzero cosmological-constant background where `epsilon` may carry a lower effective curvature order.

## Required one-loop sectors

### A. Determinants

`(i/2) Tr ln H - i Tr ln N`

Need full generalized-curvature expansion through third order. This is the sector for which generic Barvinsky–Vilkovisky CPT3 form factors are directly relevant once the pure-gravity minimal operators are frozen.

### B. Linear EOM sector

Published leading structure:

`-(i/2) Tr U1`.

Because `U1=O(epsilon)=O(R)`, its composite inverse-operator kernel needs background curvature dressing through `O(R^2)`.

### C. Quadratic EOM sector

Published structures:

`+(i/2) Tr U2 - (i/4) Tr U1^2`.

They are `O(R^2)` before further dressing, so only **one additional curvature order** is needed.

### D. Cubic EOM sector

Only the leading flat-kernel form is required.

At the level of trace topology and cyclicity, total EOM degree three can contain:

1. primitive degree-three structures `Tr(U3_a)` — there may be more than one independent primitive operator;
2. mixed composite `Tr(U1 U2)` (`Tr(U2 U1)` is trace-cyclically equivalent);
3. cubic composite `Tr(U1^3)`.

The presence of these topology classes is a bookkeeping statement, **not** a derivation of their exact coefficients or primitive operator content.

## What cannot be inferred

It would be unsafe to reconstruct the cubic coefficients by guessing an underlying `ln(1-U1+U2+...)` pattern from Eq. (14). Eq. (14) is only the expansion through `O(epsilon^2)`; multiple inequivalent exact operator functions agree through quadratic order and differ at cubic order.

Therefore the coefficients of

- `Tr(U1 U2)`,
- `Tr(U1^3)`,
- and the primitive `Tr(U3_a)` structures

remain **unknown until the full Vilkovisky reduction is obtained from primary authority or rederived from the exact one-loop operator definition**.

## New scoped results

- `C5-CUT-022 — FINITE_R3_REQUIRES_VD_EOM_SERIES_ONLY_THROUGH_OEPSILON3_ON_MINKOWSKI_LAMBDA0`.
- `C5-CUT-023 — OEPSILON1_2_SECTORS_REQUIRE_ONLY_R2_R1_BACKGROUND_DRESSING_RESPECTIVELY`.
- `C5-CUT-024 — OEPSILON3_NEEDS_ONLY_LEADING_FLAT_KERNELS_FOR_THE_FROZEN_R3_TARGET`.
- `C5-NG-020 — UV_TRUNCATED_QUADRATIC_VD_FORMULA_DOES_NOT_FIX_CUBIC_TRACE_COEFFICIENTS`.
- `NG-FUNNEL-097 — AUTHORITY_IMPROVEMENT_C5_IS_FINITE_BOOKKEEPING_PROBLEM_NOT_INFINITE_INSERTION_PROBLEM`.

## Classification

`FINITE_CUBIC_VD_BOOKKEEPING_CLOSED_OEPS3_FORMULA_STILL_BLOCKED`.

This is progress relative to Iteration 233: the required insertion order is now finite and proven. But the actual cubic connection formula remains blocked.

## Heavy-compute decision

**Do not launch the heavy finite-CPT3 tensor calculation yet.**

A heavy run would still be scientifically underdetermined without the exact `O(epsilon^3)` Vilkovisky reduction and coefficients.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

## Next gate — Iteration 244

Recover or rederive the exact **`O(epsilon^3)` one-loop Vilkovisky reduced operator formula**.

Priority:

1. inspect Cho–Kantowski 1991 and the Barvinsky–Vilkovisky generalized Schwinger-DeWitt formalism for explicit cubic EOM terms;
2. determine whether the operator-level `O(epsilon^3)` formula is dimension-independent even if its six-dimensional UV application is not;
3. if primary formula is inaccessible/incomplete, derive the cubic term directly from exact Eq. (11) using the physical-configuration-space projector/Schur-complement algebra, with Eq. (14) reproduced as a mandatory quadratic check;
4. only after the exact cubic coefficients and primitive operators are frozen may the finite CPT3 specialization proceed.
