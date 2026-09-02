# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 284**

## Current scientific state
Iterations 278–280 established translation-closed timelike C5 support with nonzero physical routed B3/orbit trace, non-scaleless bubble-a/bubble-b/triangle support and a rank-3 scalar retarded cut-support basis. Iteration 281 rejected a constant fitted-master surrogate. Iteration 282 exactly canonicalized the raised-index denominator sectors. Iteration 283 proved exact numerator degree ceilings and finite Lorentz basis sizes. Iteration 284 now proves that the canonical loop shifts preserve those degree ceilings and that every non-scaleless canonical-sector reconstruction matrix has full rank on independent train and held-out loop-momentum samples.

## Iteration 284 — canonical shift and reconstruction-design certificate
For a repeated denominator `(p+v)^2`, define `l=p+v`, hence apply `p=l-v` to the **same primitive numerator before sector summation**. This affine loop translation cannot increase degree, so the frozen ceilings remain degree <=4 for raised bubbles and <=6 for raised triangles.

The scalar Lorentz bases are therefore exactly the Iteration-283 finite bases:

- raised bubble: `(l^2)^a(l.q)^b`, `2a+b<=4`, dimension 9;
- raised triangle: `(l^2)^a(l.q1)^b(l.q2)^c`, `2a+b+c<=6`, dimension 50.

On the actual translation-closed kinematics, deterministic disjoint sampling gives:

- bubble-a: train rank 9/9, held-out rank 9/9;
- bubble-b: train rank 9/9, held-out rank 9/9;
- triangle `(0,0.21)`: train/held-out rank 50/50;
- triangle `(0,0.41)`: train/held-out rank 50/50;
- triangle `(0.21,0.41)`: train/held-out rank 50/50.

All three triangle sectors have nonzero external two-vector Gram determinant `det G=-0.01`.

Freeze:
`PASS_EXACT_CANONICAL_SHIFT_DEGREE_PRESERVATION_AND_FULL_RANK_RECONSTRUCTION_DESIGN`.

Guardrail:
`DO_NOT_INTERPRET_FULL_RANK_SAMPLING_AS_NUMERATOR_RECONSTRUCTION; ACTUAL SAME_PARENT PRIMITIVE_NUMERATOR_ORACLE_VALUES_AND_HELD_OUT_RESIDUALS_ARE_STILL_REQUIRED`.

This is an exact reconstruction-design result, not consistency PASS/FAIL, comparator identity, regime-specific non-identifiability, near-degeneracy, robust residual, or novelty certificate.

## Current C5 blocker
`BLOCKED_ACTUAL_CANONICAL_SHIFTED_SAME_PARENT_NUMERATOR_ORACLE_AND_HELDOUT_RECONSTRUCTION`.

Operational BLOCKED only. Translation closure, nonzero B3 numerator existence, scalar master support, raised-index canonicalization, finite numerator degree bounds, degree-preserving canonical shifts and full-rank reconstruction geometry are retained. Missing: actual denominator-stripped same-parent primitive numerator values, sector-summed coefficient extraction, held-out reconstruction residuals, and tensor/IBP coefficient functions.

## Stable readiness rubric
- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from previous recorded estimate: **0 percentage points**. Iteration 284 closes the reconstruction geometry but does not yet produce a linked comparator coordinate or comparator-subtracted residual.

## Retained guardrails
- Repository recovery files and recent commits are source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Keep consistency FAIL, exact comparator identity, regime-specific non-identifiability, operational BLOCKED, near-degeneracy and absence of novelty certificate distinct.
- Hard constraints precede profiling/Fisher.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction.
- Endpoint transpose means full condensed-index endpoint reversal, never raw same-routing matrix transpose.
- Do not reintroduce box masters from unclosed routing.
- Do not infer master coefficients by fitting pre-integration family traces to scalar cut shapes.
- Do not combine raised triangle numerator branches before canonicalizing the squared-denominator vertex and applying the same loop shift to the numerator.
- Do not enlarge the canonical-sector numerator fit above degree 4 for raised bubbles or degree 6 for raised triangles without a new dynamical version.
- Full-rank sampling is not a numerator reconstruction certificate; actual same-parent oracle values and held-out residuals are mandatory.

## Candidate state
No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full C5 run: NOT AUTHORIZED.

## Iteration 284 authority files
- `candidate_gravity/C5_CANONICAL_RECONSTRUCTION_DESIGN_ITERATION284.md`
- `candidate_gravity/code/iteration284_canonical_reconstruction_design.py`
- `candidate_gravity/results/iteration284_canonical_reconstruction_design.json`
- `research_log/2026-09-02_iteration_284_canonical_reconstruction_design.md`
- `recovery/RECOVERY_DELTA_ITERATION_284.md`

## Exact next gate — Iteration 285
Evaluate the actual denominator-stripped primitive numerator matrices from the frozen same-parent `N1/N2/A1/A2/A3` dynamics at the Iteration-282 canonical shifted loop momenta. Sum only after each primitive numerator has undergone the same canonical shift. Solve bubble sectors in the frozen 9-dimensional basis and each raised-triangle sector in the frozen 50-dimensional basis using rank-revealing QR/SVD, and require held-out residuals consistent with the finite-difference numerical envelope. Only after successful held-out validation perform scoped tensor/IBP reduction to physical kinematic coefficient functions multiplying the frozen scalar cut-support basis. Source/Ward/contact completion, Lorentzian comparator quotient, Fisher/resources and `ANSATZ-003` remain downstream/forbidden.
