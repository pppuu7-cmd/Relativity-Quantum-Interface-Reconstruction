# Candidate Gravity article / negative-results matrix — Iteration 266

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## New scoped result

### REL-C5-266-B3TRANSPOSE

**Claim:** On the frozen null-soft three-leg family, the 15 surviving physical polarized `B3[s,a,b]` terms contain only 8 independent transpose classes once exact same-parent coefficient symmetry is imposed. One class is self-transpose (`Q0 A3 Q0`); the remaining fourteen terms form seven exact pairs `X` and `X^T`.

**Status:** `PASS_EXACT_NULLSOFT_B3_TRANSPOSE_CLASS_REDUCTION_15_TO_8`.

**Guardrail:** `NO_DOUBLE_EVALUATION_OF_TRANSPOSE_PAIRED_B3_TERMS`.

**Provenance:** `candidate_gravity/C5_VD_NULLSOFT_B3_TRANSPOSE_CLASSES_ITERATION266.md`, reproducible code/result.

**Interpretation:** exact elimination of duplicated condensed-index/Fourier work only. It is not a new physical Ward gate and does not prove the physical numerator is nonzero.

## Retained results

- Iteration 260 exact coefficientwise weighted symmetry remains authoritative; transpose mismatch is an implementation regression.
- Iteration 261 physical polarization and 19-to-15 null-soft reduction remain authoritative.
- Iterations 257-262 exact same-parent `Q1/Q2` recursion and symmetry remain frozen; no independent resolvent ansatz.
- Iterations 263-265 project-before-expand `A=K E`, `Gamma2`, nonzero physical Einstein `E2/E3`, and the exact 2/4/7 `K` primitive library remain authoritative.
- C3 remains `BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION`.
- C4 standalone positive two-point spectral/cut information remains mediator-degenerate.
- C5 remains `BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION` with `BLOCKED_NOT_ZERO`.
- Explicit physical condensed-index `A1/A2/A3`, physical polarized `N1/N2`, exact-recursion `Q1/Q2`, nonzero assembled `B3`, tensor reduction and source projection remain open.
- No robust Candidate Gravity residual exists.
- `ANSATZ-003` remains uncreated.
- Fisher/resources remain forbidden.

## Negative/methodological significance

A direct implementation that independently evaluates all 15 surviving null-soft cubic terms performs seven redundant calculations and creates extra opportunities for convention drift. The frozen same-parent structure permits exactly 8 independent representatives and reconstructs the other seven by transpose. This is a methodological reduction, not a novelty certificate for Candidate Gravity.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 265: 0 percentage points. The physical evaluation workload is reduced without weakening any gate, but neither the final C5 comparator coordinate nor a robust unique residual has been obtained.
