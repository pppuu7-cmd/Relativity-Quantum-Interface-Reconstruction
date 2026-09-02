# RQIR Candidate Gravity research log — Iteration 260

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

Started from authoritative Iteration 259 after reading `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_259.md`, the Iteration-259 research log, recent commits, and GitHub Actions. Recent commits confirmed Iteration 259 as the actual front. Actions reported zero workflow runs, so no computation was duplicated.

## Work performed

1. Retained the Iteration-256 weighted factorization `B(t)=U1(t)W(t)=Q(t)A(t)Q(t)` with `Q=N_orb^-1` and the Iteration-253 exact identity `A=-R R (D E)`.
2. Audited whether the planned physical TT weighted-transpose test after assembling `A1,A2,A3` is an independent scientific gate.
3. Since the physical orbit metric is symmetric for every background amplitude, `N_orb(t)^T=N_orb(t)`, its inverse obeys `Q(t)^T=Q(t)` wherever defined.
4. Since `D_iE_j=D_iD_jS` is the torsion-free covariant Hessian of the same scalar parent action, the complete same-parent `A(t)` obeys `A(t)^T=A(t)` for every background amplitude.
5. Therefore `B(t)^T=[Q A Q]^T=Q A Q=B(t)` identically. Equality of formal power series implies coefficientwise `B_n^T=B_n`, in particular `B3^T=B3`.
6. Retained exactly `A3=K0E3+K1E2+K2E1`; no standalone `K1E2` Ward diagnosis is allowed.
7. Added a reproducible seeded matrix regression certificate using the exact inverse recursion. It returns `max|B3-B3^T|=1.0408340855860843e-17`, with the two transpose-pair residuals `2.8189256484623115e-18` and `3.550762114890027e-18`.

Freeze:

`PASS_EXACT_U1W_COEFFICIENTWISE_WEIGHTED_WARD_IDENTITY`

and guardrail

`NO_INDEPENDENT_TT_TRANSPOSE_GATE_FOR_COMPLETE_U1W_COEFFICIENTS`.

Interpretation: a future component-level TT transpose mismatch is an implementation/index/convention regression to debug, not evidence of a physical Ward failure of the complete same-parent `U1 W` sector. This does not close the full C5 Ward/positivity/causality program.

Retain

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and `BLOCKED_NOT_ZERO`.

No robust Candidate Gravity residual exists. `ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 259: **0 percentage points**. An actual consistency sub-uncertainty was removed analytically, but no complete physical C5 comparator coordinate, robust algebraic residual, or full consistency/positivity/Ward/causality rubric block closed. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate

Construct the physical same-parent values of `A1,A2,A3`, preserving `A3=K0E3+K1E2+K2E1`. Use `A=-R R (D E)` as an independent derivation/cross-check against direct `R.(D R).E` where it reduces component work. Then assemble the physical six-term `B3` with the frozen physical `Q0,Q1,Q2`. Weighted transpose is thereafter a regression check, not a separate scientific gate. Only after a nonzero physical numerator exists may tensor reduction proceed. No Fisher/resources, heavy full-C5 run, or `ANSATZ-003`.
