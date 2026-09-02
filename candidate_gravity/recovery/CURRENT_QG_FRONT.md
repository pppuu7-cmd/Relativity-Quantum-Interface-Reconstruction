# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 264**

## Current scientific state

The active program remains finite Vilkovisky C5 authority improvement. Iterations 261–263 fixed physical multilinear polarization, reduced the null-soft physical `B3[s,a,b]` to 15 surviving terms, froze exact `Q1/Q2` recursion, established project-before-expand `A=K E`, and fixed `Gamma2[x,y]` from the same DeWitt `a=-1/2` metric.

Iteration 264 closes a scoped physical nonlinear-Einstein EOM vertex certificate on one null-soft TT leg `s` and two distinct spacelike hard TT legs `a,b`. For

`g=eta+t_s h_s+t_a h_a+t_b h_b`,

multilinear coefficients are defined directly by amplitude derivatives of the exact Einstein tensor with no factorial convention:

`E2[x,y]=d_x d_y G[g]|0`,

`E3[x,y,z]=d_x d_y d_z G[g]|0`.

The soft leg satisfies `k_s^2=0` and `E1[s]=0` to numerical precision. At centered-difference step `3e-4`:

`||E2[s,a]||_F = 0.7456115521460782`,

`||E2[s,b]||_F = 0.7140951693123437`,

`||E2[a,b]||_F = 0.6270097790259529`,

`||E3[s,a,b]||_F = 0.5815260517855062`,

`max|E3[s,a,b]| = 0.4644883431881889`.

The values converge stably over steps `1e-2 ... 3e-4`. The all-six external-leg permutation residual for `E3` is `4.39e-10`, and output tensor symmetry residual is `1.57e-10` at `3e-4`.

Freeze:

`PASS_SCOPED_POLARIZED_EINSTEIN_E2_E3_NONZERO_AND_SYMMETRIC`

Guardrail:

`DO_NOT_ZERO_E2_OR_E3_FROM_E1_SOFT_ZERO`.

Therefore the Iteration-263 six-term projected `A3[s,a,b]` target is genuinely nontrivial: the `K0E3` sector and surviving `K1E2` sectors are not eliminated by the linear null-soft equation.

This is a scoped vertex certificate, not a complete symbolic tensor library, not the final C5 comparator coordinate, and not a Candidate Gravity residual.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 263: **0 percentage points**. The physical nonlinear Einstein EOM portion of the C5 numerator is now explicitly nonzero and permutation-consistent, but the full projected `K/A` numerator, orbit-metric dressing, tensor reduction and final C5 coordinate remain open.

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

## Iteration 264 authority files

- `candidate_gravity/C5_VD_POLARIZED_EINSTEIN_E2_E3_ITERATION264.md`
- `candidate_gravity/code/iteration264_polarized_einstein_e2_e3.py`
- `candidate_gravity/results/iteration264_polarized_einstein_e2_e3.json`
- `research_log/2026-09-02_iteration_264_polarized_einstein_e2_e3.md`
- `recovery/RECOVERY_DELTA_ITERATION_264.md`
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION264.md`

## Exact next gate — Iteration 265

Construct physical `K0/K1/K2` on the same polarized three-leg family from frozen `R0/R1`, `P=partial R`, and `Gamma0/Gamma1/Gamma2`; combine them with frozen/certified `E1/E2/E3` to assemble physical `A1/A2/A3`. In parallel derive physical polarized `N1/N2` from the same orbit metric and obtain `Q1/Q2` only through exact recursion. Assemble all 15 surviving null-soft terms of `B3[s,a,b]`. Tensor reduction remains forbidden until an explicitly nonzero physical numerator exists. Do not launch Fisher/resources, blind heavy full-C5 integration, or create `ANSATZ-003`.
