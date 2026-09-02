# RQIR Candidate Gravity research log — Iteration 261

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

Started from authoritative Iteration 260 after reading `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_260.md`, the Iteration-260 research log, recent commits, and GitHub Actions. Recent commits confirmed Iteration 260 as the actual front. Actions reported zero workflow runs, so no computation was duplicated.

## Work performed

1. Audited the Iteration-257/260 one-parameter six-family cubic expansion of `B=Q A Q` before constructing physical three-leg tensor coefficients.
2. Identified a necessary distinction between one-parameter degree bookkeeping and the polarized trilinear coefficient for distinguishable external legs `(s,a,b)`.
3. Derived the full polarized coefficient `B3[s,a,b]` in terms of `Q1[x]`, symmetric `Q2[x,y]`, `A1[x]`, symmetric `A2[x,y]`, and complete symmetric `A3[x,y,z]`.
4. The six degree families expand to 19 explicit leg-resolved terms: 1 `Q0 A3 Q0`, 6 `Q1 A2` terms, 6 `Q2 A1` terms, and 6 ordered `Q1 A1 Q1` terms.
5. Used the frozen Iteration-246 null-soft theorem `E1[s]=0` and `E0=0` to infer `A1[s]=K0 E1[s]=0`.
6. Exactly four of the 19 terms therefore vanish: the two `Q2[a,b] A1[s]` placements and the two `Q1[a] A1[s] Q1[b]` orderings. Fifteen physical null-soft terms survive.
7. Explicitly retained soft-background dressing terms such as `Q1[s] A2[a,b]`, `A2[s,a]`, `A2[s,b]`, `A3[s,a,b]`, and `Q1[s] A1[a] Q1[b]`; the null-soft theorem does not eliminate the surviving `e=1/e=2` sectors.
8. Added a reproducible enumeration certificate and stored its JSON result.

Freeze:

`PASS_SCOPED_PHYSICAL_B3_MULTILINEAR_POLARIZATION`

and guardrail

`NO_UNPOLARIZED_SIX_TERM_B3_AS_PHYSICAL_THREE_LEG_NUMERATOR`.

Interpretation: the Iteration-257/260 six-term formula remains correct as one-parameter degree-family bookkeeping, but it must be polarized before being used as the physical three-point C5 numerator. This prevents omitted leg allocations, false cancellations and normalization errors.

Retain:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and `BLOCKED_NOT_ZERO`.

No robust Candidate Gravity residual exists. `ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 260: **0 percentage points**. A necessary physical-assembly ambiguity is removed, but the physical C5 comparator coordinate, robust algebraic residual and all downstream readiness blocks remain open. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate

Construct the **polarized** same-parent tensors `A1[x]`, `A2[x,y]`, and complete `A3[s,a,b]`; derive polarized `Q1[x]`, `Q2[x,y]` only from the frozen physical orbit metric; then assemble the 15 surviving null-soft terms of `B3[s,a,b]`. Weighted transpose remains a regression test. Tensor reduction is forbidden until a nonzero physical numerator exists. Fisher/resources, blind heavy full-C5 integration and `ANSATZ-003` remain forbidden.
