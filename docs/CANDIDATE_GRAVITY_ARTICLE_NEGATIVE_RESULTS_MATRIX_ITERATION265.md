# Candidate Gravity article / negative-results matrix — Iteration 265

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## New scoped results

### REL-C5-265-KLIB

**Claim:** In the frozen affine metric split with same-parent `K=R(P+Gamma R)`, the polarized projected connection generator has a finite primitive library: `K0` contains 2 contractions, each `K1[x]` contains 4, and each `K2[x,y]` contains 7. No `R2`, `R3`, or `Gamma3` is required for physical projected cubic `A3`.

**Status:** `PASS_EXACT_POLARIZED_K0_K1_K2_PRIMITIVE_LIBRARY_2_4_7`.

**Guardrail:** `NO_R2_R3_GAMMA3_IN_PHYSICAL_PROJECTED_A3`.

**Provenance:** `candidate_gravity/C5_VD_POLARIZED_K_PRIMITIVE_LIBRARY_ITERATION265.md`, reproducible code/result.

### REL-C5-265-A3COUNT

**Claim:** With the frozen null-soft condition `E1[s]=0`, projected `A3[s,a,b]` consists of `K0E3 + 3 K1E2 + 2 K2E1`. Substitution of the exact K-library sizes gives exactly 28 primitive K/E contractions before any further tensor, momentum, TT, or source-projection cancellation.

**Status:** `PASS_EXACT_NULLSOFT_PROJECTED_A3_PRIMITIVE_COUNT_28`.

**Interpretation:** finite-library closure only; no claim that all 28 contractions survive physical contraction or integration.

## Retained results

- Iteration 263 project-before-expand `A=K E` reduction remains authoritative.
- Iteration 264 nonzero physical polarized `E2/E3` certificate remains authoritative; `E1[s]=0` does not zero-fill nonlinear sectors.
- `Gamma2[x,y]` remains frozen from the same DeWitt `a=-1/2` metric; no independent `Gamma2` ansatz.
- C3 remains `BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION`.
- C4 standalone positive two-point spectral/cut information remains mediator-degenerate.
- C5 remains `BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION` with `BLOCKED_NOT_ZERO`.
- Explicit physical condensed-index `K/A`, physical polarized `N1/N2`, exact-recursion `Q1/Q2`, the 15-term null-soft `B3[s,a,b]`, tensor reduction and source projection remain open.
- No robust Candidate Gravity residual exists.
- `ANSATZ-003` remains uncreated.
- Fisher/resources remain forbidden.

## Interpretation discipline

Iteration 265 is an exact algebraic finite-library closure plus an implementation regression. It is not a consistency FAIL, exact Candidate-vs-GR comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate. The negative/methodological result is that no higher `R` or `Gamma` background vertices may be introduced to patch the cubic numerator: the frozen same-parent dynamics already fixes the complete `K0/K1/K2` content.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 264: 0 percentage points. A genuine C5 vertex-bookkeeping block is now closed, but the complete physical C5 comparator coordinate and any robust unique residual remain open.
