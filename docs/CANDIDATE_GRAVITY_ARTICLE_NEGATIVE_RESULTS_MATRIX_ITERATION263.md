# Candidate Gravity article / negative-results matrix — Iteration 263

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## New scoped results

### REL-C5-263-PROJ

**Claim:** For the same frozen Vilkovisky parent, the physical cubic `A` numerator should be constructed by the exact projected identity `A=K E`, `K=R(DR)`, before expanding the covariant Hessian. Because `E0=0`, `A1/A2/A3` require only `E1/E2/E3` and `K0/K1/K2`. A primary full unprojected `H3=D D S` construction, and therefore an explicit fifth action variation `S5`, is unnecessary for physical cubic `U1 W`.

**Status:** `PASS_EXACT_PROJECT_BEFORE_EXPAND_A_EQUALS_K_E_CUBIC_REDUCTION`.

**Guardrail:** `NO_FULL_UNPROJECTED_H3_OR_S5_REQUIRED_FOR_PHYSICAL_U1W_B3`.

**Provenance:** `candidate_gravity/C5_VD_PROJECTED_HESSIAN_AND_GAMMA2_ITERATION263.md`, reproducible code/result.

### REL-C5-263-GAMMA2

**Claim:** The second polarized configuration-space Christoffel `Gamma2[x,y]` is fixed by the same DeWitt `a=-1/2` metric as the lower-order vertices. An independent 10-dimensional field-space-metric reconstruction agrees with the exact compact-tensor mixed derivative to `9.43e-08` maximum absolute mismatch on tested O(0.5) components.

**Status:** `PASS_SCOPED_FIELDSPACE_CHRISTOFFEL_SECOND_POLARIZED_VARIATION`.

**Guardrail:** `NO_INDEPENDENT_GAMMA2_ANSATZ`.

### REL-C5-263-SOFT

**Claim:** The frozen null-soft condition `E1[s]=0` reduces projected `A3[s,a,b]` to six surviving partitions. It also reduces `A2[s,a]` and `A2[s,b]` to two partitions each. These reductions do not imply vanishing of the surviving `E2/E3`, `K1`, or `K2` pieces.

**Status:** exact scoped null-soft algebraic reduction.

## Retained negative/open material

- C3 remains `BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION`, never zero-filled.
- C4 standalone positive two-point spectral/cut information remains mediator-degenerate.
- C5 remains `BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION` with `BLOCKED_NOT_ZERO`.
- Physical polarized Einstein EOM coefficients `E2[x,y]`, `E3[s,a,b]`, the resulting projected `K/A` blocks, the full 15-term null-soft `B3[s,a,b]`, tensor reduction and source projection remain open.
- `T_cut` remains operationally non-executable with current authority; no proxy substitution is allowed.
- No robust Candidate Gravity residual exists.
- `ANSATZ-003` remains uncreated.
- Fisher/resources remain forbidden.

## Interpretation discipline

Iteration 263 is an exact same-parent algebraic reduction plus a scoped geometric validation. It is not a consistency FAIL, not an exact Candidate-vs-GR comparator identity, not regime-specific non-identifiability, not near-degeneracy, and not a novelty certificate. The negative result that full `H3/S5` is unnecessary is retained as publishable methodology/error-prevention material rather than discarded.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 262: 0 percentage points. A major unnecessary tensor layer is eliminated and `Gamma2` is frozen, but no complete comparator coordinate or robust unique residual has closed.