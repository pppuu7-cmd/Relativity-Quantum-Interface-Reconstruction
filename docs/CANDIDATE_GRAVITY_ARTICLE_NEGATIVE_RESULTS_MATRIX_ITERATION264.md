# Candidate Gravity article / negative-results matrix — Iteration 264

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## New scoped results

### REL-C5-264-E2E3

**Claim:** On one null-soft TT leg and two distinct spacelike hard TT legs, multilinear derivatives of the exact 4D Einstein tensor give nonzero polarized `E2[s,a]`, `E2[s,b]`, `E2[a,b]`, and genuinely three-leg `E3[s,a,b]`. The cubic coefficient is permutation symmetric within numerical accuracy.

**Status:** `PASS_SCOPED_POLARIZED_EINSTEIN_E2_E3_NONZERO_AND_SYMMETRIC`.

**Guardrail:** `DO_NOT_ZERO_E2_OR_E3_FROM_E1_SOFT_ZERO`.

**Provenance:** `candidate_gravity/C5_VD_POLARIZED_EINSTEIN_E2_E3_ITERATION264.md`, reproducible code/result.

### REL-C5-264-NEGATIVE-SOFT

**Claim:** The linear null-soft equation `E1[s]=0` does not eliminate the surviving nonlinear Einstein inputs needed by physical projected `A3[s,a,b]`. In particular the `K0E3` sector and surviving `K1E2` sectors cannot be zero-filled from the linear soft equation.

**Status:** exact interpretation of the scoped nonzero vertex certificate; not a complete C5 residual.

## Retained results

- Iteration 263 project-before-expand `A=K E` reduction remains authoritative.
- `Gamma2[x,y]` remains frozen from the same DeWitt `a=-1/2` metric; no independent `Gamma2` ansatz.
- C3 remains `BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION`.
- C4 standalone positive two-point spectral/cut information remains mediator-degenerate.
- C5 remains `BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION` with `BLOCKED_NOT_ZERO`.
- Physical `K0/K1/K2`, projected `A1/A2/A3`, physical `N1/N2`, `Q1/Q2`, the 15-term null-soft `B3[s,a,b]`, tensor reduction and source projection remain open.
- No robust Candidate Gravity residual exists.
- `ANSATZ-003` remains uncreated.
- Fisher/resources remain forbidden.

## Interpretation discipline

Iteration 264 is a scoped physical nonlinear-Einstein vertex certificate. It is not a consistency FAIL, exact Candidate-vs-GR comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate. The negative result is methodological: nonlinear `E2/E3` sectors must be retained even when the soft external leg solves the linearized Einstein equation.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 263: 0 percentage points. The physical Einstein EOM portion of the C5 numerator is now explicitly nonzero and symmetry-checked, but the complete comparator coordinate and any robust unique residual remain open.
