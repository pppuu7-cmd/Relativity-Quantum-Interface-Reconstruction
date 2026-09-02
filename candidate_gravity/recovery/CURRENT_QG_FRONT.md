# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 263**

## Current scientific state

The active program remains finite Vilkovisky C5 authority improvement. Iterations 261–262 established the physical polarized `B3[s,a,b]`, its 15 surviving null-soft terms, the affine `R0/R1` generator library, and exact `Q1/Q2` inverse recursion.

Iteration 263 removes an unnecessary primary tensor layer. Retain the exact same-parent identity

`A = K E`, with `K^j_{gamma delta}=R^i_gamma (D_i R^j_delta)`.

Because flat Einstein `E0=0`, multilinear projected coefficients are

`A1[x]=K0E1[x]`,

`A2[x,y]=K0E2[x,y]+K1[x]E1[y]+K1[y]E1[x]`,

and generic `A3[x,y,z]` contains `K0E3`, three `K1E2`, and three `K2E1` partitions.

For the frozen null-soft leg `E1[s]=0`, physical `A3[s,a,b]` has six surviving projected terms; `A2[s,a]` and `A2[s,b]` each have two, while `A2[a,b]` has three.

This means the physical cubic numerator does **not** require a primary construction of full unprojected `H3=D D S`; that route would expose a fifth action variation `S5` which cancels after gauge projection. The exact projected `A=K E` route needs only `E1/E2/E3` and `K0/K1/K2`, reaching only the fourth action variation through `E3`. The `-RRH` representation remains a regression/cross-check, not the primary construction route.

With frozen affine `R` and `D R=P+Gamma R`, `P=partial R` background-independent,

`D0=P+Gamma0R0`,

`D1[x]=Gamma1[x]R0+Gamma0R1[x]`,

`D2[x,y]=Gamma2[x,y]R0+Gamma1[x]R1[y]+Gamma1[y]R1[x]`,

so `K0,K1,K2` require only `Gamma0/Gamma1/Gamma2` and `R0/R1`. No `Gamma3`, `R2`, or `R3` is required.

The physical second polarized DeWitt field-space Christoffel `Gamma2[x,y]` has now been constructed from the same frozen `a=-1/2` metric and independently validated against a direct 10-dimensional field-space Christoffel reconstruction. On the recorded Lorentzian traceless test directions,

`max|Gamma2_direct-Gamma2_formula| = 9.4322526123e-08`

on maximum component scale `0.500008028696`, with zero tested input-pair and mixed-leg exchange symmetry residuals.

Freeze:

`PASS_EXACT_PROJECT_BEFORE_EXPAND_A_EQUALS_K_E_CUBIC_REDUCTION`

`PASS_SCOPED_FIELDSPACE_CHRISTOFFEL_SECOND_POLARIZED_VARIATION`

`NO_FULL_UNPROJECTED_H3_OR_S5_REQUIRED_FOR_PHYSICAL_U1W_B3`

`NO_INDEPENDENT_GAMMA2_ANSATZ`.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 262: **0 percentage points**. The numerator route is materially shorter and `Gamma2` is closed, but no complete C5 comparator coordinate or robust nonzero residual exists.

## Frozen guardrails retained

- Repository recovery files and recent commits are source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Keep consistency FAIL, exact comparator identity, regime-specific non-identifiability, operational BLOCKED, near-degeneracy and absence of novelty certificate distinct.
- Hard constraints precede profiling/Fisher.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists.
- `e+c<=3` remains the frozen finite-`R^3` truncation rule.
- Null-soft linear Einstein equations kill the `e=3` flat connection sector but not surviving `e=1/e=2` sectors.
- Iteration 252 fixes `Nhat=W N_orb` and the `U1` factorization.
- Iteration 253 fixes complete `A3=K0E3+K1E2+K2E1`; standalone `K1E2` is not a Ward FAIL object.
- Iteration 254 fixes affine `R=L_xi g` in the linear metric split.
- Iteration 255 fixes use of configuration-space Christoffel `Gamma` in `D_iR`.
- Iterations 257–259 fix physical orbit-metric inverse recursion through `Q2`; no independent `N2/Q2` ansatz.
- Iteration 260 fixes exact coefficientwise weighted symmetry of complete same-parent `U1 W`; transpose mismatch is an implementation regression, not a new physical Ward FAIL.
- Iteration 261 fixes physical multilinear polarization before any three-leg numerator claim.
- Iteration 262 fixes the polarized `A` 3/7/13 bookkeeping, `Q1/Q2` recursion, and proves `Q3/N3` unnecessary because `A0=0`.
- Iteration 263 fixes project-before-expand `A=K E` as the primary cubic construction, eliminates the need for full unprojected `H3/S5`, and freezes physical `Gamma2[x,y]` from the same DeWitt metric.

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

## Iteration 263 authority files

- `candidate_gravity/C5_VD_PROJECTED_HESSIAN_AND_GAMMA2_ITERATION263.md`
- `candidate_gravity/code/iteration263_vd_projected_hessian_gamma2.py`
- `candidate_gravity/results/iteration263_vd_projected_hessian_gamma2.json`
- `research_log/2026-09-02_iteration_263_vd_projected_hessian_gamma2.md`
- `recovery/RECOVERY_DELTA_ITERATION_263.md`
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION263.md`

## Exact next gate — Iteration 264

Construct polarized Einstein EOM coefficients `E2[x,y]` and `E3[s,a,b]` in frozen `D=4, Lambda=0, a=-1/2`; combine them with frozen `E1`, `R0/R1`, `P=partial R`, and `Gamma0/Gamma1/Gamma2` to build `K0,K1,K2`, then projected physical `A1,A2,A3`. In parallel derive physical `N1[x],N2[x,y]` from the same orbit metric and obtain `Q1,Q2` only through exact recursion. Assemble the 15 surviving null-soft terms of `B3[s,a,b]`. Tensor reduction remains forbidden until a nonzero physical numerator exists. Do not launch Fisher/resources, blind heavy full-C5 integration, or create `ANSATZ-003`.