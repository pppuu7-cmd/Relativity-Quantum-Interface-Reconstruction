# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 267**

## Current scientific state

The active program remains finite Vilkovisky C5 authority improvement. Iterations 261–266 fixed physical multilinear polarization, the null-soft 19-to-15 reduction, exact `Q1/Q2` recursion, project-before-expand `A=K E`, physical `Gamma2[x,y]`, nonzero polarized Einstein `E2/E3`, the exact projected `K0/K1/K2` 2/4/7 primitive library, the 28-primitive null-soft `A3` target, and the exact reduction of the 15 surviving physical `B3[s,a,b]` terms to 8 transpose classes.

Iteration 267 freezes the missing condensed-index/Fourier momentum-routing semantics required before those 8 classes may be instantiated numerically.

For any polarized background Fourier insertion, translation covariance gives:

- `O1[x]`: `p -> p+k_x`;
- `O2[x,y]`: `p -> p+k_x+k_y`;
- `O3[x,y,z]`: `p -> p+k_x+k_y+k_z`;
- `Q0`: zero background shift, but it must be evaluated at the routed orbit momentum at its insertion.

All 8 independent null-soft cubic representatives therefore have common support

`<p+K|X|p>`, with `K=k_s+k_a+k_b`.

Freeze:

`PASS_EXACT_B3_CONDENSED_INDEX_MOMENTUM_SUPPORT`

The Iteration-266 transpose-class reduction remains exact in full operator space, but kernel transpose exchanges endpoints:

`<p+K|X|p>^T = <p|X^T|p+K>`.

When rewritten in canonical forward orientation, the transpose partner carries `-K`. For real backgrounds this is realized by endpoint reversal plus the conjugate Fourier sector `k_s,k_a,k_b -> -k_s,-k_a,-k_b` (with complex conjugation as appropriate). Therefore a raw finite-dimensional matrix transpose at unchanged `p` and unchanged `+k` legs is not the condensed-index kernel transpose.

Guardrail:

`NO_FIXED_PLUS_K_MATRIX_TRANSPOSE_AS_KERNEL_TRANSPOSE`.

This sharpens, but does not revoke,

`PASS_EXACT_NULLSOFT_B3_TRANSPOSE_CLASS_REDUCTION_15_TO_8`.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 266: **0 percentage points**. Momentum support and transpose reconstruction are now frozen at the physical kernel level, preventing a false same-routing local-matrix numerator, but explicit contracted `A/N/Q/B3`, tensor reduction, source projection and complete C5 comparator closure remain open.

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
- Iteration 255 fixes configuration-space Christoffel `Gamma` in `D_iR`.
- Iterations 257–259 fix physical orbit-metric inverse recursion through `Q2`; no independent `N2/Q2` ansatz.
- Iteration 260 fixes exact coefficientwise weighted symmetry of complete same-parent `U1 W`; transpose mismatch is an implementation regression, not a new physical Ward FAIL.
- Iteration 261 fixes physical multilinear polarization before any three-leg numerator claim and the null-soft 19-to-15 reduction.
- Iteration 262 fixes polarized `A` bookkeeping, `Q1/Q2` recursion, and proves `Q3/N3` unnecessary because `A0=0`.
- Iteration 263 fixes project-before-expand `A=K E`, eliminates full unprojected `H3/S5`, and freezes physical `Gamma2[x,y]`.
- Iteration 264 fixes a scoped nonzero, permutation-symmetric physical `E2/E3` certificate and forbids zero-filling nonlinear EOM sectors from `E1[s]=0`.
- Iteration 265 fixes the exact polarized `K0/K1/K2` primitive library as 2/4/7, the null-soft projected `A3` primitive count as 28, and forbids `R2/R3/Gamma3` in this cubic route.
- Iteration 266 fixes the exact null-soft `B3` transpose-class reduction 15-to-8 and forbids double evaluation of abstract transpose partners.
- Iteration 267 fixes condensed-index/Fourier momentum support for all 8 representatives and forbids implementing operator transpose as a raw same-routing matrix transpose.

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

## Iteration 267 authority files

- `candidate_gravity/C5_VD_B3_MOMENTUM_ROUTING_ITERATION267.md`
- `candidate_gravity/code/iteration267_vd_b3_momentum_routing.py`
- `candidate_gravity/results/iteration267_vd_b3_momentum_routing.json`
- `research_log/2026-09-02_iteration_267_vd_b3_momentum_routing.md`
- `recovery/RECOVERY_DELTA_ITERATION_267.md`
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION267.md`

## Exact next gate — Iteration 268

Implement an explicit routed condensed-index/Fourier kernel layer for only the 8 independent null-soft `B3[s,a,b]` representatives. Build physical `K0/K1/K2 -> A1/A2/A3` with explicit endpoint/intermediate momenta. Derive physical polarized `N1/N2` from the same orbit metric and obtain `Q1/Q2` only through exact inverse recursion at their routed momenta. Evaluate the 8 forward `+K` representatives; reconstruct the seven abstract transpose partners by endpoint-reversed kernel transpose / the real-mode `-K` sector, not by a raw same-routing matrix transpose. Then determine whether the assembled physical `B3[s,a,b]` is explicitly nonzero. Tensor reduction remains forbidden until that algebraic nonzero is established. Do not launch Fisher/resources, blind heavy full-C5 integration, or create `ANSATZ-003`.
