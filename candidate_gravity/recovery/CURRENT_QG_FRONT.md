# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 261**

## Current scientific state

The active program remains finite Vilkovisky C5 authority improvement. Iteration 261 establishes that the physical three-leg cubic `B3[s,a,b]` must be obtained by multilinear polarization of the one-parameter degree-family formula for `B=Q A Q`.

The one-parameter cubic families remain

`B3 = Q0 A3 Q0 + Q1 A2 Q0 + Q0 A2 Q1 + Q2 A1 Q0 + Q0 A1 Q2 + Q1 A1 Q1`,

but for distinguishable legs `(s,a,b)` these expand to **19 explicit leg-resolved terms**. On the frozen physical null-TT soft branch, Iteration 246 gives `E1[s]=0`; with `E0=0` and `A=K E`, this implies `A1[s]=0`. Exactly four polarized terms vanish, leaving **15 surviving terms**.

Freeze:

`PASS_SCOPED_PHYSICAL_B3_MULTILINEAR_POLARIZATION`

`PASS_SCOPED_NULLSOFT_POLARIZED_B3_REDUCTION_19_TO_15`

`NO_UNPOLARIZED_SIX_TERM_B3_AS_PHYSICAL_THREE_LEG_NUMERATOR`

Soft-background dressing through `Q1[s]`, `A2[s,a]`, `A2[s,b]`, `A3[s,a,b]` and analogous placements must not be dropped.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 260: **0 percentage points**. Physical cubic bookkeeping is corrected, but no complete comparator coordinate or robust nonzero residual exists.

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

## Iteration 261 authority files

- `candidate_gravity/C5_VD_MULTILINEAR_B3_POLARIZATION_ITERATION261.md`
- `candidate_gravity/code/iteration261_vd_multilinear_b3_polarization.py`
- `candidate_gravity/results/iteration261_vd_multilinear_b3_polarization.json`
- `research_log/2026-09-02_iteration_261_vd_multilinear_b3_polarization.md`
- `recovery/RECOVERY_DELTA_ITERATION_261.md`
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION261.md`

## Exact next gate — Iteration 262

Construct polarized same-parent `A1[x]`, `A2[x,y]`, complete `A3[s,a,b]`, and polarized `Q1[x]`, `Q2[x,y]` from the frozen orbit metric. Assemble the **15 surviving null-soft terms** of `B3[s,a,b]`. Tensor reduction remains forbidden until a nonzero physical numerator exists. Do not launch Fisher/resources, blind heavy full-C5 integration or create `ANSATZ-003`.
