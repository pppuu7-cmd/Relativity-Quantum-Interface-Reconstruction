# RECOVERY DELTA — Candidate Gravity Iteration 260

**Date:** 2026-09-02  
**Authoritative iteration:** 260  
**MODEL_READINESS: 24%**

## Delta from Iteration 259

Iteration 259 fixed and directly validated the physical inverse-orbit coefficients through `Q2`. Iteration 260 audits the planned weighted-transpose Ward check before further component work and proves that, for the complete same-parent `U1 W` sector, it is not an independent scientific gate.

Retain

`B(t)=U1(t)W(t)=Q(t)A(t)Q(t)`,

`Q(t)=N_orb(t)^-1`,

`A_{gamma delta}(t)=R^i_gamma(D_iR^j_delta)E_j=-R^i_gamma R^j_delta D_iE_j`.

Because `N_orb(t)` is symmetric for every background amplitude, `Q(t)^T=Q(t)`. Because `D_iE_j=D_iD_jS` is the torsion-free covariant Hessian of the same scalar parent action, the complete same-parent `A(t)^T=A(t)`. Therefore

`B(t)^T=B(t)`

identically. Formal-series coefficient matching gives `B_n^T=B_n` for every `n`, especially `B3^T=B3`.

Retain exactly

`A3=K0E3+K1E2+K2E1`.

The reproducible regression certificate gives

`max|B3-B3^T|=1.0408340855860843e-17`,

with transpose-pair residuals `2.8189256484623115e-18` and `3.550762114890027e-18`.

Freeze:

`PASS_EXACT_U1W_COEFFICIENTWISE_WEIGHTED_WARD_IDENTITY`

and

`NO_INDEPENDENT_TT_TRANSPOSE_GATE_FOR_COMPLETE_U1W_COEFFICIENTS`.

A future TT/component transpose mismatch is therefore an implementation/index/convention regression, not a physical consistency FAIL of the complete same-parent `U1 W` sector.

Retain umbrella blocker:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

`BLOCKED_NOT_ZERO`.

This exact sub-sector identity is not an exact Candidate-vs-GR comparator identity, not a complete C5 Ward/positivity/causality closure, not regime-specific non-identifiability, near-degeneracy, or a novelty certificate.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 259: **0 percentage points**. A real consistency sub-gate is analytically removed as an independent uncertainty, but the physical C5 comparator coordinate and robust algebraic residual remain open, so no readiness-rubric category closes. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate

Construct the physical same-parent `A1,A2,A3`, preserving exactly `A3=K0E3+K1E2+K2E1`, using `A=-R R(D E)` as an independent derivation/cross-check where helpful. Assemble the physical six-term `B3` with frozen `Q0,Q1,Q2`. Treat weighted transpose only as a regression test. Tensor reduction remains forbidden until a nonzero physical numerator exists; Fisher/resources and `ANSATZ-003` remain forbidden.
