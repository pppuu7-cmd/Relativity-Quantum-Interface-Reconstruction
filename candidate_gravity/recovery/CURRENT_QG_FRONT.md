# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 266**

## Current scientific state

The active program remains finite Vilkovisky C5 authority improvement. Iterations 261–265 fixed physical multilinear polarization, reduced the null-soft physical `B3[s,a,b]` from 19 to 15 surviving terms, froze exact `Q1/Q2` recursion, established project-before-expand `A=K E`, fixed physical `Gamma2[x,y]`, certified nonzero physical polarized Einstein `E2/E3`, and closed the exact projected `K0/K1/K2` primitive library as 2/4/7 with a 28-primitive null-soft `A3` target.

Iteration 266 removes a further exact duplication before physical condensed-index/Fourier evaluation. Retain frozen same-parent coefficient symmetry

`Qn^T = Qn`, `An^T = An`, `Q2[x,y]=Q2[y,x]`, `A2[x,y]=A2[y,x]`,

and frozen null-soft `A1[s]=0`.

The 15 surviving physical polarized `B3[s,a,b]` terms split into exactly 8 transpose classes:

- one self-transpose class `Q0 A3[s,a,b] Q0`;
- three `Q1 A2` transpose pairs;
- two surviving `Q2 A1` transpose pairs;
- two surviving `Q1 A1 Q1` transpose pairs.

Therefore

`B3[s,a,b] = Q0 A3[s,a,b] Q0 + Sum_{r=1}^7 (X_r + X_r^T)`

and only 8 independent physical representatives require direct kernel evaluation. The other seven surviving terms must be reconstructed by transpose rather than recomputed independently.

Freeze:

`PASS_EXACT_NULLSOFT_B3_TRANSPOSE_CLASS_REDUCTION_15_TO_8`

Guardrail:

`NO_DOUBLE_EVALUATION_OF_TRANSPOSE_PAIRED_B3_TERMS`.

This is an exact same-parent algebraic reduction of duplicated work. It is not an explicit physical `A/N/Q/B3` tensor, not a nonzero C5 numerator, not the final C5 comparator coordinate, and not a Candidate Gravity residual.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 265: **0 percentage points**. The cubic physical evaluation set is reduced from 15 survivors to 8 independent transpose representatives, but explicit contracted `A/N/Q/B3`, tensor reduction, source projection and the complete C5 comparator coordinate remain open.

## Frozen guardrails retained

- Repository recovery files and recent commits are source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Keep consistency FAIL, exact comparator identity, regime-specific non-identifiability, operational BLOCKED, near-degeneracy and absence of novelty certificate distinct.
- Hard constraints precede profiling/Fisher.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists.
- `e+c<=3` remains the frozen finite-`R^3` truncation rule.
- Iteration 252 fixes `Nhat=W N_orb` and the `U1` factorization.
- Iteration 253 fixes complete `A3=K0E3+K1E2+K2E1`; standalone `K1E2` is not a Ward FAIL object.
- Iteration 254 fixes affine `R=L_xi g` in the linear metric split.
- Iteration 255 fixes use of configuration-space Christoffel `Gamma` in `D_iR`.
- Iterations 257–259 fix physical orbit-metric inverse recursion through `Q2`; no independent `N2/Q2` ansatz.
- Iteration 260 fixes exact coefficientwise weighted symmetry of complete same-parent `U1 W`; transpose mismatch is an implementation regression, not a new physical Ward FAIL.
- Iteration 261 fixes physical multilinear polarization before any three-leg numerator claim and the null-soft 19-to-15 reduction.
- Iteration 262 fixes polarized `A` bookkeeping, `Q1/Q2` recursion, and proves `Q3/N3` unnecessary because `A0=0`.
- Iteration 263 fixes project-before-expand `A=K E`, eliminates full unprojected `H3/S5`, and freezes physical `Gamma2[x,y]`.
- Iteration 264 fixes a scoped nonzero, permutation-symmetric physical `E2/E3` certificate and forbids zero-filling nonlinear EOM sectors from `E1[s]=0`.
- Iteration 265 fixes the exact polarized `K0/K1/K2` primitive library as 2/4/7, the null-soft projected `A3` primitive count as 28, and forbids `R2/R3/Gamma3` in this cubic route.
- Iteration 266 fixes the exact null-soft `B3` transpose-class reduction 15-to-8 and forbids double evaluation of transpose partners.

## Retained comparator state

### C3
`BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION` — not zero and not consistency FAIL.

### C4
Standalone positive two-point spectral/cut information remains mediator-degenerate.

### C5
`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

`BLOCKED_NOT_ZERO`.

### Other routes
Asymptotic-safety, nonlocal and proxy routes retain their frozen blockers; no proxy replaces the frozen comparator identity.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Heavy full C5 run: NOT AUTHORIZED.

## Iteration 266 authority files

- `candidate_gravity/C5_VD_NULLSOFT_B3_TRANSPOSE_CLASSES_ITERATION266.md`
- `candidate_gravity/code/iteration266_vd_nullsoft_b3_transpose_classes.py`
- `candidate_gravity/results/iteration266_vd_nullsoft_b3_transpose_classes.json`
- `research_log/2026-09-02_iteration_266_vd_nullsoft_b3_transpose_classes.md`
- `recovery/RECOVERY_DELTA_ITERATION_266.md`
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION266.md`

## Exact next gate — Iteration 267

Instantiate only the 8 independent null-soft `B3[s,a,b]` transpose representatives. Build physical condensed-index/Fourier `K0/K1/K2` from the frozen 2/4/7 library and contract them with certified `E1/E2/E3` to obtain explicit `A1/A2/A3`. Derive physical polarized `N1/N2` from the same orbit metric and obtain `Q1/Q2` only through exact inverse recursion. Reconstruct the seven transpose partners rather than evaluating them independently, then determine whether the assembled physical `B3[s,a,b]` is explicitly nonzero. Tensor reduction remains forbidden until that algebraic nonzero is established. Do not launch Fisher/resources, blind heavy full-C5 integration, or create `ANSATZ-003`.
