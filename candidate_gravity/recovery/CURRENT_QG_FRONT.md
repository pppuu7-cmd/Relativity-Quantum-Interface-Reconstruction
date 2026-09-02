# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 265**

## Current scientific state

The active program remains finite Vilkovisky C5 authority improvement. Iterations 261–264 fixed physical multilinear polarization, reduced the null-soft physical `B3[s,a,b]` to 15 surviving terms, froze exact `Q1/Q2` recursion, established project-before-expand `A=K E`, fixed `Gamma2[x,y]`, and certified nonzero physical polarized Einstein `E2/E3` input on the same null-soft/hard/hard TT family.

Iteration 265 closes the exact projected `K0/K1/K2` bookkeeping implied by the same frozen dynamics

`K = R (P + Gamma R)`,

with affine `R=R0+R1[h]`, background-independent `P=partial R`, and configuration-space `Gamma` from the frozen DeWitt `a=-1/2` metric.

Exact polarization gives

`K0 = R0 P + R0 Gamma0 R0`,

so `K0` has 2 primitive contractions;

`K1[x] = R1[x] P + R1[x] Gamma0 R0 + R0 Gamma1[x] R0 + R0 Gamma0 R1[x]`,

so each `K1[x]` has 4 primitive contractions;

and

`K2[x,y] = R1[x] Gamma1[y] R0 + R1[x] Gamma0 R1[y] + R1[y] Gamma1[x] R0 + R1[y] Gamma0 R1[x] + R0 Gamma2[x,y] R0 + R0 Gamma1[x] R1[y] + R0 Gamma1[y] R1[x]`,

so each `K2[x,y]` has 7 primitive contractions.

Therefore no `R2`, `R3`, or `Gamma3` enters physical projected cubic `A3`.

With frozen `E1[s]=0`,

`A3[s,a,b] = K0E3[s,a,b] + K1[s]E2[a,b] + K1[a]E2[s,b] + K1[b]E2[s,a] + K2[s,a]E1[b] + K2[s,b]E1[a]`.

Substitution of the exact K-library sizes gives

`2 + 3*4 + 2*7 = 28`

primitive K/E contractions before any further tensor, momentum, TT, or source-projection cancellations.

Freeze:

`PASS_EXACT_POLARIZED_K0_K1_K2_PRIMITIVE_LIBRARY_2_4_7`

`PASS_EXACT_NULLSOFT_PROJECTED_A3_PRIMITIVE_COUNT_28`

Guardrail:

`NO_R2_R3_GAMMA3_IN_PHYSICAL_PROJECTED_A3`.

A reproducible noncommuting-matrix regression test confirms the polarized product formulas with centered finite-difference convergence. At `h=1e-4`, the `K1` mismatch is `2.6320710944e-7` and mixed `K2` mismatch is `2.3047781283e-7`. The finite-difference test is a regression only; the 2/4/7 and 28 counts are exact algebraic consequences of the frozen same-parent construction.

This is a finite-library closure, not an explicit physical condensed-index `K/A` tensor, not the final C5 comparator coordinate, and not a Candidate Gravity residual.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 264: **0 percentage points**. The projected K vertex space is now exact and finite, but physical contracted `A/B3`, orbit-metric dressing, tensor reduction and the complete C5 comparator coordinate remain open.

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
- Iteration 262 fixes polarized `A` bookkeeping, `Q1/Q2` recursion, and proves `Q3/N3` unnecessary because `A0=0`.
- Iteration 263 fixes project-before-expand `A=K E` as the primary cubic construction, eliminates full unprojected `H3/S5`, and freezes physical `Gamma2[x,y]`.
- Iteration 264 fixes a scoped nonzero, permutation-symmetric physical `E2/E3` certificate and forbids zero-filling nonlinear EOM sectors from `E1[s]=0`.
- Iteration 265 fixes the exact polarized `K0/K1/K2` primitive library as 2/4/7, the null-soft projected `A3` primitive count as 28, and forbids introducing `R2/R3/Gamma3` into this cubic route.

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

## Iteration 265 authority files

- `candidate_gravity/C5_VD_POLARIZED_K_PRIMITIVE_LIBRARY_ITERATION265.md`
- `candidate_gravity/code/iteration265_vd_polarized_k_primitive_library.py`
- `candidate_gravity/results/iteration265_vd_polarized_k_primitive_library.json`
- `research_log/2026-09-02_iteration_265_vd_polarized_k_primitive_library.md`
- `recovery/RECOVERY_DELTA_ITERATION_265.md`
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION265.md`

## Exact next gate — Iteration 266

Instantiate the 2/4/7 `K0/K1/K2` primitive contractions as physical condensed-index/Fourier kernels on the same frozen `s,a,b` family using `R0/R1` and `Gamma0/Gamma1/Gamma2`; contract them with certified `E1/E2/E3` to obtain explicit physical `A1/A2/A3`. In parallel derive physical polarized `N1/N2` from the same orbit metric and obtain `Q1/Q2` only through exact inverse recursion. Then assemble all 15 surviving null-soft terms of `B3[s,a,b]`. Tensor reduction remains forbidden until an explicitly nonzero physical `B3` exists. Do not launch Fisher/resources, blind heavy full-C5 integration, or create `ANSATZ-003`.
