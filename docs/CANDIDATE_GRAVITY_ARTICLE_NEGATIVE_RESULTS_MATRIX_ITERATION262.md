# Candidate Gravity article / negative-results matrix — Iteration 262

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## New scoped results

### REL-C5-262-A

**Claim:** Using the exact same-parent representation `A=-RR(D E)` and the affine metric diffeomorphism generator of the frozen linear split, the polarized coefficients require exactly 3 subterms for `A1[x]`, 7 for `A2[x,y]`, and 13 for complete `A3[s,a,b]`. No `R2/R3` vertices occur.

**Status:** `PASS_SCOPED_POLARIZED_A_MINIMAL_3_7_13_LIBRARY`.

**Provenance:** `candidate_gravity/C5_VD_POLARIZED_A_AND_Q_MINIMAL_LIBRARY_ITERATION262.md`, reproducible code/result.

### REL-C5-262-Q

**Claim:** Polarized `Q1[x]` and `Q2[x,y]` are fixed exactly by the same orbit metric through inverse recursion. No independent polarized resolvent ansatz is allowed.

**Status:** `PASS_SCOPED_POLARIZED_Q1_Q2_INVERSE_RECURSION`.

### REL-C5-262-Q3

**Claim:** The flat Einstein background has `A0=0`; therefore the cubic coefficient of `B=QAQ` never requires `Q3`, since every total-degree-three term containing `Q3` multiplies `A0`. Consequently `N3/Q3` need not be constructed for the physical cubic `U1 W` sector.

**Status:** `NO_Q3_OR_N3_REQUIRED_FOR_PHYSICAL_U1W_CUBIC_B3`.

### REL-GUARD-262-SOFT

**Claim:** The frozen null-soft identity `A1[s]=0` applies to the complete three-term polarized sum. It does not justify zeroing `R1[s]`, `H1[s]`, or individual `-RRH` subterms separately.

**Status:** `NO_TERM_BY_TERM_SOFT_ZERO_INSIDE_A1`.

## Retained negative/open material

- C3 remains `BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION`, never zero-filled.
- C4 standalone positive two-point spectral/cut information remains mediator-degenerate.
- C5 remains `BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION` with `BLOCKED_NOT_ZERO`.
- Physical polarized `H1[x]`, `H2[x,y]`, `H3[s,a,b]`, the resulting `A1/A2/A3`, and the 15-term null-soft `B3[s,a,b]` remain open.
- `T_cut` remains operationally non-executable with current published authority; no proxy substitution is allowed.
- No robust Candidate Gravity residual exists.
- `ANSATZ-003` remains uncreated.
- Fisher/resources remain forbidden.

## Interpretation discipline

Iteration 262 is an exact algebraic library reduction. It is not a consistency FAIL, not an exact Candidate-vs-GR comparator identity, not regime-specific non-identifiability, not near-degeneracy, and not a novelty certificate. It converts the next C5 construction from an open-ended vertex search into the finite same-parent set `N1,N2,R1,H1,H2,H3`.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 261: 0 percentage points. The upstream vertex space is reduced, but no complete comparator coordinate or readiness-rubric block closes.
