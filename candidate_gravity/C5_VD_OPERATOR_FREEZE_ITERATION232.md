# RQIR Candidate Gravity — Iteration 232

## Pure-Einstein Vilkovisky operator authority freeze and CPT3 compatibility gate

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

### Scope

This iteration starts from authoritative Iteration 231 and asks a narrower question: can a single published pure-Einstein Vilkovisky–DeWitt operator convention be frozen in a form directly acceptable to third-order covariant perturbation theory (CPT3), without replacing the unique-action operator by an ordinary gauge-fixed Hessian?

Primary authority: B. L. Giacchini, T. de Paula Netto, I. L. Shapiro, *Vilkovisky unique effective action in quantum gravity*, Phys. Rev. D 102, 106006 (2020), arXiv:2006.04217.

### Frozen convention

The authority defines the gravitational configuration-space metric, in the simplest background parametrization, by

`G^{mu nu;alpha beta} = 1/2 (delta^{mu nu;alpha beta} + a g^{mu nu} g^{alpha beta})`,

with nondegeneracy condition `a != -1/D`. Vilkovisky's prescription fixes `a=-1/2` for quantum Einstein gravity by matching the field-space metric to the highest-derivative term of the minimal bilinear action. In `D=4`, `-1/2 != -1/4`, so the metric is nondegenerate.

The paper uses the nonsingular DeWitt gauge. With `a=-1/2`, the local graviton operator becomes minimal Laplace type,

`H = -(1 Box + Pi)`,

and the FP ghost operator

`N^alpha_beta = delta^alpha_beta Box + (1+2a) nabla^alpha nabla_beta + R^alpha_beta`

becomes minimal because `1+2a=0`.

This part of the Iteration-232 gate therefore **passes**: a published, same-paper pure-Einstein convention exists in which the local graviton and ghost differential operators are both minimal Laplace type.

### Critical obstruction

The full one-loop Vilkovisky unique action in the same authority is not only

`(i/2) Tr ln H - i Tr ln N`.

Its off-shell gauge/parametrization completion also contains the connection/gauge-orbit terms customarily denoted `U1`, `U2`, and `U1^2` in the generalized Schwinger–DeWitt reduction. These are nonlocal composite operators built from the gauge generators, equations of motion, the inverse ghost/graviton operators, and the Vilkovisky connection.

The 2020 calculation evaluates these extra traces only to the background-dimension order required for the one-loop UV pole. It does not supply a finite third-order nonlocal `R^3` form-factor map for the complete set

`{Tr ln H, Tr ln N, Tr U1, Tr U2, Tr U1^2}`.

Therefore the pair of minimal local Laplace-type operators `H,N` is **not by itself** a CPT3-complete representation of the off-shell unique action. Feeding only `H,N` into generic CPT3 would omit precisely the connection sector that restores the required off-shell gauge/parametrization authority.

### Published divergent target retained as unit test

For dimensional regularization, Eq. (60) of the same authority gives the unique-action one-loop pole

`Gamma_div = - mu^(D-4)/[(4 pi)^2 (D-4)] int sqrt(|g|) [53/45 Riemann^2 - 61/90 Ricci^2 + 25/36 R^2 + 8 Lambda R + 12 Lambda^2]`.

This remains the required unit/convention target for any future implementation. The reproducible algebra-only certificate in `candidate_gravity/code/iteration232_vd_operator_freeze_check.py` verifies the frozen `a=-1/2` minimal-ghost condition and records these exact rational targets.

### New classification

Retain umbrella status:

`BLOCKED_C5_VD_NONLOCAL_CUBIC_SPECIALIZATION`.

Replace the Iteration-231 substatus by the sharper minimal missing object:

`BLOCKED_COMPLETE_VD_CONNECTION_TRACE_TO_FINITE_CPT3_MAP`.

The obstruction is no longer the inability to freeze a local graviton+ghost operator convention. That convention **is** freezeable and minimal. The unresolved object is the finite CPT3-compatible treatment of the complete Vilkovisky connection/gauge-orbit trace sector together with `H,N` in one coefficient convention.

### Scoped results

- `C5-CUT-016 — PURE_EINSTEIN_VD_AUTHORITY_FIXES_A_NONDEGENERATE_A_MINUS_ONE_HALF_DEWITT_CONVENTION_WITH_MINIMAL_LOCAL_GRAVITON_AND_GHOST_OPERATORS`.
- `C5-CUT-017 — MINIMAL_H_AND_N_DO_NOT_EQUAL_THE_FULL_OFFSHELL_VILKOVISKY_ONE_LOOP_OPERATOR_BECAUSE_CONNECTION_TRACE_TERMS_U1_U2_AND_U1_SQUARED_ARE_REQUIRED`.
- `C5-CUT-018 — THE_NEW_MINIMAL_C5_BLOCKER_IS_THE_COMPLETE_VD_CONNECTION_TRACE_TO_FINITE_CPT3_FORM_FACTOR_MAP`.
- `REL-NG-012 — REPRODUCING_ONLY_THE_H_PLUS_GHOST_HEAT_KERNEL_IS_NOT_A_UNIQUE_ACTION_CERTIFICATE_OFF_SHELL`.
- `NG-FUNNEL-088 — A_FINITE_R3_RESULT_FROM_H_PLUS_N_ALONE_MUST_NOT_BE_PROMOTED_AS_THE_RQIR_C5_UNIQUE_ACTION_COMPARATOR`.

### Classification guardrails

This is an **operational/scientific BLOCKED** result. It is not a consistency FAIL of Einstein quantum gravity, not an exact comparator identity, not near-degeneracy, not evidence for a zero C5 column, and not a Candidate Gravity novelty certificate.

### Candidate state

Robust Candidate Gravity residual: none.  
`ANSATZ-003`: not created.  
Fisher/resources: forbidden.  
Heavy finite CPT3 run: not authorized yet.

### Readiness

`MODEL_READINESS: 24%`

Change from Iteration 231: **0 percentage points**. A substantial part of comparator authority is now frozen more tightly, but the complete finite C5 comparator coordinate remains unavailable; therefore comparator foundation stays `24/25` and robust unique residual stays `0/20`.

### Exact next gate

Iteration 233 should audit the Barvinsky–Vilkovisky generalized Schwinger–DeWitt/CPT literature for a finite nonlocal treatment of the specific `U1`, `U2`, `U1^2` trace structures appearing in the 2020 pure-Einstein unique-action reduction. The gate is binary:

1. if those traces can be mapped, in the same convention, to a controlled third-order curvature form-factor basis, implement the divergent Eq. (60) reproduction before any finite `R^3` extraction;
2. if the literature supplies only UV/local universal traces and not finite third-order nonlocal form factors for these composite connection operators, freeze `BLOCKED_COMPLETE_VD_CONNECTION_TRACE_TO_FINITE_CPT3_MAP` and return effort to the AS linked-relation branch rather than inventing a representative.
