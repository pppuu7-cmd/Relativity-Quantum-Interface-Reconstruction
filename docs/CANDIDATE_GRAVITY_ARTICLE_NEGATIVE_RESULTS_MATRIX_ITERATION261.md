# Candidate Gravity article / negative-results matrix — Iteration 261

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## New scoped result

### REL-C5-261

**Claim:** The Iteration-257/260 six-term cubic expression for `B=Q A Q` is a correct one-parameter degree-family decomposition, but the physical three-point C5 numerator with distinguishable external legs requires multilinear polarization. For legs `(s,a,b)`, the six degree families expand into 19 explicit leg-resolved terms built from `Q1[x]`, symmetric `Q2[x,y]`, `A1[x]`, symmetric `A2[x,y]`, and complete `A3[x,y,z]`.

**Status:** `PASS_SCOPED_PHYSICAL_B3_MULTILINEAR_POLARIZATION`.

**Provenance:** `candidate_gravity/C5_VD_MULTILINEAR_B3_POLARIZATION_ITERATION261.md`, reproducible code/result.

**Scope:** exact algebraic polarization of the complete same-parent `U1 W` cubic coefficient. This is not yet the numerical/functional C5 comparator coordinate.

### REL-C5-261-NULLSOFT

**Claim:** On the frozen physical null-TT soft branch, Iteration 246 gives `E1[s]=0`; since `A=K E` and `E0=0`, `A1[s]=0`. Exactly four of the 19 polarized cubic terms vanish, leaving 15 surviving terms. Soft-background dressing terms in `Q1[s]`, `A2[s,a]`, `A2[s,b]`, and `A3[s,a,b]` remain allowed and must not be dropped.

**Status:** `PASS_SCOPED_NULLSOFT_POLARIZED_B3_REDUCTION_19_TO_15`.

### REL-GUARD-261

**Claim:** The unpolarized six-term one-parameter expression must not be used directly as the physical distinguishable-leg three-point numerator.

**Status:** `NO_UNPOLARIZED_SIX_TERM_B3_AS_PHYSICAL_THREE_LEG_NUMERATOR`.

## Retained negative/open material

- C3 remains `BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION`, never zero-filled.
- C4 standalone positive two-point spectral/cut information remains mediator-degenerate.
- C5 remains `BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION` with `BLOCKED_NOT_ZERO`.
- Polarized physical `A1[x]`, `A2[x,y]`, complete `A3[s,a,b]`, and the resulting 15-term null-soft `B3[s,a,b]` remain open.
- `T_cut` remains operationally non-executable with current published authority; no proxy substitution is allowed.
- No robust Candidate Gravity residual exists.
- `ANSATZ-003` remains uncreated.
- Fisher/resources remain forbidden.

## Interpretation discipline

Iteration 261 is not a consistency FAIL, not an exact Candidate-vs-GR comparator identity, not regime-specific non-identifiability, near-degeneracy, or a novelty certificate. It is a physical-assembly correction that prevents omitted external-leg allocations and false cancellations before tensor reduction.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 260: 0 percentage points. The physical cubic bookkeeping is sharpened, but no complete comparator coordinate or readiness-rubric block closes.
