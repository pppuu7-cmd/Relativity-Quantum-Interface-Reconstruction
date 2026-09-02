# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 283**

## Current scientific state
Iterations 278–280 established a translation-closed timelike continuation family with nonzero physical routed B3/orbit trace, non-scaleless bubble-a/bubble-b/triangle support and a rank-3 scalar retarded cut-support basis. Iteration 281 rejected a constant fitted-master surrogate. Iteration 282 exactly canonicalized the raised-index denominator sectors. Iteration 283 now proves a finite loop-momentum numerator degree/basis bound before any interpolation or IBP.

## Iteration 283 — exact numerator degree and finite-basis bound
On the flat Einstein background, `Q0(p)=-eta/p^2` exactly. In the frozen same-parent dynamics `N1,N2` and polarized `A1,A2,A3` are at most quadratic in routed loop momentum. Exact inverse recursion therefore gives `Q1` numerator degree <=2, sequential `Q2` degree <=4, and `Q2` N2-contact degree <=2.

Expanding all 23 translation-closed primitive B3 branches gives:

- single squared scaleless: 1 branch, numerator degree <=2;
- null raised bubble: 2 branches, degree <=4;
- bubble-a: 4 branches, degree <=4;
- bubble-b: 4 branches, degree <=4;
- raised triangle: 12 branches, degree <=6.

Thus no primitive branch requires numerator degree above six. For scalar orbit-trace reconstruction at fixed external invariants, the Lorentz monomial basis `(l^2)^a prod_i(l.q_i)^b_i` with weighted degree `2a+sum b_i<=d` has ceiling sizes 2 (single), 9 (raised bubble with one independent external q) and 50 (raised triangle with two independent external q's), before symmetry/Gram reductions.

Freeze:

`PASS_EXACT_TRANSLATION_CLOSED_B3_NUMERATOR_DEGREE_AND_FINITE_BASIS_BOUND`.

Guardrail:

`DO_NOT_FIT_CANONICAL_SECTOR_NUMERATORS_WITH_DEGREE_ABOVE_THE_EXACT_2_4_6_BOUNDS_WITHOUT_A_NEW_DYNAMICAL_VERSION`.

This is an exact power-counting/reconstruction-bound result, not a consistency PASS/FAIL, comparator identity, regime-specific non-identifiability, near-degeneracy or novelty certificate.

## Current C5 blocker
`BLOCKED_CANONICAL_SHIFTED_P_DEPENDENT_NUMERATOR_RECONSTRUCTION_AND_TENSOR_IBP_COEFFICIENT_EXTRACTION`.

Operational BLOCKED only. Translation closure, nonzero B3 numerator existence, scalar master support, raised-index canonicalization and finite numerator degree bounds are retained. Missing: actual canonical-shifted p-dependent sector numerators, held-out reconstruction validation and tensor/IBP coefficient functions.

## Stable readiness rubric
- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from previous recorded estimate: **0 percentage points**. Iteration 283 proves the remaining reconstruction is finite and bounded by frozen dynamics, but no linked comparator coordinate or comparator-subtracted residual has yet been produced.

## Retained guardrails
- Repository recovery files and recent commits are source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Keep consistency FAIL, exact comparator identity, regime-specific non-identifiability, operational BLOCKED, near-degeneracy and absence of novelty certificate distinct.
- Hard constraints precede profiling/Fisher.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction.
- `e+c<=3` remains frozen.
- Endpoint transpose means full condensed-index endpoint reversal, never raw same-routing matrix transpose.
- Do not reintroduce box masters from unclosed routing.
- Do not infer master coefficients by fitting pre-integration family traces to scalar cut shapes.
- Do not combine raised triangle numerator branches before canonicalizing the squared-denominator vertex and applying the same loop shift to the numerator.
- Do not enlarge the canonical-sector numerator fit above degree 4 for raised bubbles or degree 6 for raised triangles without a new dynamical version.

## Retained comparator state
### C3
`BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION` — not zero and not consistency FAIL.

### C4
Standalone positive two-point spectral/cut information remains mediator-degenerate.

### C5
Translation closure: exact PASS.  
Closed raised bubble/triangle topology: exact PASS.  
Translation-closed B3 numerator nonzero: scoped PASS.  
Timelike non-scaleless family-resolved orbit trace: scoped PASS.  
Three-dimensional scalar retarded cut-support basis: scoped PASS.  
Constant fitted master-coefficient surrogate: scoped FAIL.  
Raised-index sector canonicalization: exact PASS.  
Finite numerator degree/basis bound: exact PASS.  
Canonical-shifted p-dependent numerator reconstruction and tensor/IBP coefficient extraction: BLOCKED downstream.

### Other routes
Asymptotic-safety, nonlocal and proxy routes retain frozen blockers; no proxy replaces the fixed comparator quotient.

## Candidate state
No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full C5 run: NOT AUTHORIZED.

## Iteration 283 authority files
- `candidate_gravity/C5_NUMERATOR_DEGREE_BASIS_ITERATION283.md`
- `candidate_gravity/code/iteration283_numerator_degree_basis_bound.py`
- `candidate_gravity/results/iteration283_numerator_degree_basis_bound.json`
- `research_log/2026-09-02_iteration_283_numerator_degree_basis_bound.md`
- `recovery/RECOVERY_DELTA_ITERATION_283.md`

## Exact next gate — Iteration 284
Apply the Iteration-282 canonical loop shifts to the actual p-dependent primitive numerators and only then form sector sums. Reconstruct bubble-a and bubble-b sector sums in Lorentz bases of degree <=4 and each raised-triangle canonical vertex sector in a Lorentz basis of degree <=6; validate all reconstructions on held-out loop-momentum points. Only after that perform scoped tensor/IBP reduction to kinematic coefficient functions multiplying the already frozen scalar cut-support basis. Source/Ward/contact completion, Lorentzian comparator quotient, Fisher/resources and `ANSATZ-003` remain downstream/forbidden.
