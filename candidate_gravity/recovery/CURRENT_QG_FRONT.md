# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 282**

## Current scientific state

Iterations 278–280 established a translation-closed timelike continuation family with nonzero physical routed B3/orbit trace, resolved its non-scaleless support into bubble-a, bubble-b and triangle families, and established a rank-3 scalar retarded cut-support basis on the controlled linked timelike slice. Iteration 281 then rejected the invalid shortcut of fitting three kinematics-independent master coefficients directly to the pre-integration family trace.

## Iteration 282 — exact raised-index sector canonicalization

Before reconstructing genuine p-dependent numerators, Iteration 282 removed the remaining loop-routing ambiguity exactly by enumerating all 23 translation-closed primitive B3 denominator branches.

The exact multiplicity/invariant census is:

- 1 single squared scaleless branch: `(2)`;
- 2 null raised bubbles: `(2,1)` with `q^2=0`;
- 4 bubble-b branches: `(2,1)` with `q^2=0.21`;
- 4 bubble-a branches: `(2,1)` with `q^2=0.41`;
- 12 raised triangles: `(2,1,1)` with pairwise edge invariants `(0,0.21,0.41)`.

Thus every nontrivial closed primitive branch has exactly one squared denominator, with no propagator power above two.

For the twelve triangle branches, choosing the doubled propagator as canonical loop origin splits the raised-index numerator problem into exactly three sectors of four branches each, labeled by the two invariant edges incident on the squared denominator:

- `(0,0.21)`: 4;
- `(0,0.41)`: 4;
- `(0.21,0.41)`: 4.

Freeze:

`PASS_EXACT_TRANSLATION_CLOSED_RAISED_INDEX_SECTOR_CANONICALIZATION`.

Guardrail:

`DO_NOT_COMBINE_TRIANGLE_BRANCHES_BEFORE_MAPPING_THE_SQUARED_DENOMINATOR_TO_A_CANONICAL_VERTEX_AND_TRANSFORMING_THE_NUMERATOR_WITH_THE_SAME_LOOP_SHIFT`.

This does not alter the previously frozen scalar-master statement: the nontrivial scalar topology remains two raised bubbles plus one triangle kinematic family. The new result resolves the raised-index numerator routing required before tensor/IBP coefficient extraction.

## Current C5 blocker

`BLOCKED_CANONICAL_SECTOR_P_DEPENDENT_NUMERATOR_RECONSTRUCTION_AND_TENSOR_IBP_COEFFICIENT_EXTRACTION`.

The blocker is operational. Translation closure, nonzero B3 numerator existence, scalar master support, and raised-index routing canonicalization are retained. What remains missing is the genuine p-dependent numerator reconstruction and coefficient extraction.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from previous recorded estimate: **0 percentage points**. Iteration 282 removes an exact routing ambiguity required for a valid C5 IBP reduction, but it does not yet produce a physical linked comparator coordinate or comparator-subtracted residual.

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
Canonical-sector p-dependent numerator reconstruction and tensor/IBP coefficient extraction: BLOCKED downstream.

### Other routes
Asymptotic-safety, nonlocal and proxy routes retain frozen blockers; no proxy replaces the fixed comparator quotient.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full C5 run: NOT AUTHORIZED.

## Iteration 282 authority files

- `candidate_gravity/C5_RAISED_INDEX_CANONICALIZATION_ITERATION282.md`
- `candidate_gravity/code/iteration282_canonical_raised_family_routing.py`
- `candidate_gravity/results/iteration282_canonical_raised_family_routing.json`
- `research_log/2026-09-02_iteration_282_raised_index_canonicalization.md`
- `recovery/RECOVERY_DELTA_ITERATION_282.md`

## Exact next gate — Iteration 283

For bubble-a, bubble-b and each of the three canonical raised-triangle vertex sectors, apply the exact loop shift that places the squared denominator at `l^2` and transform the numerator with the identical shift. Reconstruct each sector-summed p-dependent numerator in a finite Lorentz-covariant tensor/rational basis in `l` and external invariants; validate on held-out loop-momentum points; then tensor/IBP reduce the canonical sector sums to actual kinematic coefficient functions multiplying the frozen scalar cut-support basis. Source/Ward/contact completion, Lorentzian comparator quotient, Fisher/resources and `ANSATZ-003` remain downstream/forbidden.
