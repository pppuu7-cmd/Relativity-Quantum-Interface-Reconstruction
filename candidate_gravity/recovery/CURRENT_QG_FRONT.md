# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 281**

## Current scientific state

Repository recent commits are source of truth and supersede the previously stale Iteration-274 display. The factual chain advanced through Iterations 278–280 before this authority consolidation.

Iteration 278 certified a translation-closed timelike continuation family with nonzero physical routed `B3`/orbit trace on all eight sampled rows. Iteration 279 resolved the non-scaleless orbit trace into `bubble-a`, `bubble-b`, and `triangle` families, while retaining scaleless sectors separately. Iteration 280 established a rank-3 scalar retarded cut-support basis on the controlled linked timelike slice:

`1/s`, `1/(s+0.2)`, `log(s/(s+0.2))/(s-(s+0.2))`.

These are scalar master-function support directions only; they are not yet the C5 tensor coefficient vector or a candidate residual.

## Iteration 281 — constant master-coefficient shortcut rejected

A diagnostic test asked whether the Iteration-279 non-scaleless pre-integration family trace could already be represented by three kinematics-independent coefficients multiplying the Iteration-280 scalar support functions.

The least-squares best fit is

`(-0.18793735, -21.47800082, 7.01934896)`

with relative L2 residual

`0.08675993597017234`

and maximum absolute residual

`3.39573961`.

Freeze:

`FAIL_SCOPED_CONSTANT_MASTER_COEFFICIENT_SURROGATE_ON_TIMELIKE_SLICE`.

This is a scoped negative result and implementation guardrail, not a consistency FAIL. It forbids collapsing the genuine p-dependent tensor/IBP problem into three fitted constants. The actual C5 coefficients must remain kinematic functions derived from the family-resolved p-dependent numerators.

## Current C5 blocker

`BLOCKED_P_DEPENDENT_FAMILY_NUMERATOR_RECONSTRUCTION_AND_TENSOR_IBP_COEFFICIENT_EXTRACTION`.

The blocker is operational. The translation-closed numerator existence and scalar master-support rank are retained; what is missing is the genuine coefficient extraction.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from previous recorded estimate: **0 percentage points**. The iteration closes an invalid shortcut but does not yet produce a physical linked comparator coordinate or comparator-subtracted residual.

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
P-dependent family numerator reconstruction and tensor/IBP coefficient extraction: BLOCKED downstream.

### Other routes
Asymptotic-safety, nonlocal and proxy routes retain frozen blockers; no proxy replaces the fixed comparator quotient.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full C5 run: NOT AUTHORIZED.

## Iteration 281 authority files

- `candidate_gravity/C5_MASTER_COEFFICIENT_NONCONSTANCY_ITERATION281.md`
- `candidate_gravity/code/iteration281_master_coefficient_constancy_test.py`
- `candidate_gravity/results/iteration281_master_coefficient_constancy_test.json`
- `research_log/2026-09-02_iteration_281_master_coefficient_nonconstancy.md`
- `recovery/RECOVERY_DELTA_ITERATION_281.md`

## Exact next gate — Iteration 282

For `bubble-a`, `bubble-b`, and `triangle` separately, reconstruct the combined p-dependent numerator in a finite Lorentz-covariant tensor/rational basis on the translation-closed timelike family and validate it on held-out loop-momentum points. Then perform one-loop tensor/IBP reduction only inside the already-frozen raised bubble/triangle topology to obtain actual coefficient functions multiplying the Iteration-280 scalar cut-support basis. Source/Ward/contact completion, Lorentzian comparator quotient, Fisher/resources and `ANSATZ-003` remain downstream/forbidden.
