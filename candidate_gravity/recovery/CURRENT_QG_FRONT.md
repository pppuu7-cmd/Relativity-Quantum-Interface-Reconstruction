# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 287**

## Current scientific state

Iterations 278–280 established translation-closed timelike C5 support with nonzero routed `B3`/orbit trace, non-scaleless raised bubble/triangle support and a rank-3 scalar retarded cut-support basis. Iterations 281–284 rejected an invalid fitted-master shortcut, canonicalized the raised denominator sectors and proved exact numerator degree ceilings (`<=4` bubbles, `<=6` triangles). Iteration 285 corrected the insufficient denominator-only 9/50 numerator bases and certified complete actual-oracle 70/210 fixed-coordinate bases. Iteration 286 completed held-out reconstruction for every non-scaleless bubble and triangle sector.

Iteration 287 now performs the first complete coefficient-level dimensional-regularization tensor reduction of the actual same-parent numerator.

## Iteration 287 — complete raised-bubble tensor reduction

For

`N(l) / [(l^2)^2 ((l+q)^2)]`

all 70 actual-oracle degree-`<=4` polynomial coefficients are mapped to rank-0/2/4 tensor moments and reduced in the convention

`D_q log_R(-q^2)=1`,

after dividing the loop integral by `i*pi^(D/2)`.

### Bubble-a

- `q^2 = 0.41`;
- fit rank `70/70`;
- held-out relative max residual `7.520447097449553e-10`;
- normalized logarithmic/discontinuity coefficient
  `C_a = -0.1247249362037728`;
- loop-reflected coefficient identical;
- reflection residual `0.0`.

### Bubble-b

- `q^2 = 0.21`;
- fit rank `70/70`;
- held-out relative max residual `3.2353465789325438e-9`;
- normalized logarithmic/discontinuity coefficient
  `C_b = +0.10231503679645079`;
- loop-reflected coefficient identical;
- reflection residual `0.0`.

Both non-scaleless hard bubbles therefore survive complete tensor reduction and have opposite sign.

Freeze:

`PASS_COMPLETE_70_MONOMIAL_BUBBLE_TENSOR_MOMENT_REDUCTION_NONZERO`.

The earlier exploratory bubble-a estimate `-0.64977` is superseded and must not be reused; it preceded the Iteration-285 complete-basis correction.

## DR sanity checks

The reduction reproduces:

- scalar numerator: `1/q^2 = 2.4390243902439024` for the bubble-a calibration;
- numerator `l^2`: coefficient `-1`;
- numerator `(l^2)^2`: scaleless value `-1.3877787807814457e-17`.

These checks independently verify the logarithmic residue map and scaleless cancellation.

## Retained Iteration-286 authority

All non-scaleless numerator sectors remain fully reconstructed:

- bubble-a/b: degree `<=4`, complete 70-monomial bases;
- triangles `(0,0.21)`, `(0,0.41)`, `(0.21,0.41)`: degree `<=6`, complete 210-monomial bases;
- held-out relative reconstruction errors remain approximately `10^-9` or smaller for bubbles and `10^-11` for triangles.

The null raised bubbles and the single squared-denominator family remain scaleless in the frozen massless DR treatment.

## Current C5 blocker

`BLOCKED_COMPLETE_TRIANGLE_TENSOR_REDUCTION_AND_SOURCE_WARD_CONTACT_COMPLETION`.

Numerator completeness and raised-bubble reduction are no longer blockers. The immediate remaining coefficient-level problem is the complete degree-6 raised-triangle reduction, including the one-null-leg two-mass branch and routing/reflection checks. Source/Ward/contact completion and the linked hard-channel `T_cut` remain downstream.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 286: **0 percentage points**. A real tensor-reduction blocker has partially closed, but no source-completed linked comparator coordinate or comparator-subtracted robust residual yet exists.

## Classification discipline

Iteration 287 is a scoped C5 coefficient-level PASS. It is not a Candidate Gravity residual, not a novelty certificate, not a consistency PASS/FAIL of the candidate, and not evidence that other comparator classes vanish.

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
- Apply every loop shift/reflection to the primitive numerator before sector summation.
- Retain exact degree ceilings `<=4` for raised bubbles and `<=6` for raised triangles unless parent dynamics changes.
- Full rank of a proposed sampling matrix does not prove basis completeness; held-out actual same-parent oracle residuals are mandatory.
- Do not use the superseded denominator-only 9/50 bases.
- Do not reuse the superseded exploratory `-0.64977` bubble-a estimate.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.

## Iteration 287 authority files

- `candidate_gravity/C5_BUBBLE_TENSOR_REDUCTION_ITERATION287.md`
- `candidate_gravity/code/iteration287_bubble_tensor_moment_reduction.py`
- `candidate_gravity/results/iteration287_bubble_tensor_moment_reduction.json`
- `candidate_gravity/C5_BUBBLE_TENSOR_REDUCTION_PREGATE_ITERATION287.md`

## Exact next gate — Iteration 288

1. Fit/export the complete 210 coefficients for all three raised-triangle sectors.
2. Reduce rank-0/2/4/6 moments with the canonical repeated propagator retained.
3. Calibrate by cancelling the repeated propagator with a numerator `l^2`; all three routings must reproduce the same ordinary one-null two-mass triangle cut.
4. Extract the coefficient-level common hard-channel discontinuity and verify loop reflection.
5. Then decompose the full triangle contribution into the scalar triangle plus induced bubble cut basis before assembling the complete C5 hard-channel cut.
6. Source/Ward/contact completion, comparator quotient, Fisher/resources and `ANSATZ-003` remain downstream/forbidden.
