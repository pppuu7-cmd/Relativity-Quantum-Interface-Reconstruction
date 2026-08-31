# Iteration 172 — finite relation-level CTP comparator matrix

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Frozen scope

Use the six already frozen amputated kinematic rows and, at each row,

`(Gamma_arr, Gamma_aar, Gamma_aaa, WardLock)`.

The source/field convention remains that of Iterations 148–149 and the `r/a` normalization remains that of Iteration 171.

## Strong generic C4/C5 comparator

Do not restrict an ordinary closed quantum C4 mediator to the EH momentum fingerprint. The conservative fixed structural comparator therefore gives each row an independent cubic amplitude while imposing only the exact closed-unitary relation

`Gamma_aar = 0`,

`Gamma_aaa = Gamma_arr/4`,

and the source-completed consistency condition

`WardLock = 0`.

Across six rows these are six independent generic quantum amplitude directions.

## Fixed C3 supported piece

For `C3-PQCG-NL-001`, Iteration 155 already established the tree nonlinear Einstein drift fingerprint

`B_EH = [0.30003001285313774, -1.461790494216445, -12.034873790942026, -14.434681522564402, 4.867521776975717, -2.7789127642722273]`.

At the supported classical tree level it supplies `Gamma_arr=B_EH` with no quantum `aaa` term. Full diffusion/MSR ordered vertices remain BLOCKED and are not zero-filled.

## Raw matrix certificate

The 24x7 matrix containing six generic closed-unitary row-amplitude columns plus the fixed C3 tree column has

`rank = 7/7`,

singular values approximately

`[19.69366276, 1.03077641 x5, 0.24967744]`,

and

`s_min/s_max = 0.0126780602`.

Thus the fixed classical C3 tree direction is linearly independent of the generic closed-unitary quantum subspace.

## Relation coordinates

Project each row to

1. `R_aar = Gamma_aar`,
2. `R_unit = Gamma_aaa - Gamma_arr/4`,
3. `R_W = WardLock`.

All generic closed-unitary C4/C5 amplitude columns vanish exactly under this map. The supported fixed C3 tree maps to one vector only,

`R_unit = -B_EH/4`,

with norm

`4.917063349196141`.

Therefore the supported relation-level comparator matrix has

`rank = 1`.

## Classification

### CTP-NG-003

`GENERIC_CLOSED_UNITARY_C4_C5_REMOVES_ROW_LOCAL_CUBIC_AMPLITUDE_BUT_NOT_RELATION_VIOLATIONS`.

Arbitrary row-local cubic amplitude is nuisance/shared structure. Only linked CTP relations survive the quotient.

### CTP-NG-004

`FIXED_PQCG_TREE_ADDS_ONE_EH_SHAPED_CLASSICAL_RELATION_DIRECTION`.

The supported classical PQCG tree response supplies one nonunitary relation direction proportional to the already-calibrated EH nonlinear fingerprint.

### NG-FUNNEL-032

`WARD_LOCK_VIOLATION_IS_CONSISTENCY_FAIL_NOT_NOVELTY`.

A nonzero source-completed Ward-lock coordinate is a consistency failure of the declared dynamics/source convention. It must never be promoted as a Candidate Gravity residual.

## What is not established

The 17-dimensional algebraic complement of the current supported 7-dimensional raw comparator span is **not** a novelty certificate. In particular:

- C3 diffusion/MSR ordered `aar/aaa` pieces are BLOCKED;
- nonlocal and asymptotic-safety real-time nonlinear CTP vertices are BLOCKED;
- C4/C5 loop/noise three-point completion is BLOCKED.

Unsupported pieces must not be zero-filled.

## Decision

Iteration 172 closes the first finite relation-level rank/quotient gate. It does not authorize `ANSATZ-003`, Fisher, or resources.

The next useful gate is to derive the fixed C3 diffusion/MSR ordered cubic relation from the same PQCG parent dynamics; if that cannot be completed without an extra stochastic convention, freeze the blocker and move to a source-completed nonlinear nonlocal/AS relation rather than inventing missing columns.
