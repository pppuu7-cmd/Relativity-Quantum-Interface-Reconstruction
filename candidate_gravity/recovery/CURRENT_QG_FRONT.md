# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 286**

## Current scientific state

Iterations 278–280 established translation-closed timelike C5 support with nonzero physical routed `B3`/orbit trace, non-scaleless bubble-a/bubble-b/triangle support and a rank-3 scalar retarded cut-support basis. Iteration 281 rejected a constant fitted-master surrogate. Iteration 282 exactly canonicalized raised-index denominator sectors. Iteration 283 proved exact numerator degree ceilings (`<=4` for raised bubbles, `<=6` for raised triangles). Iteration 284 proved affine loop shifts preserve those ceilings. Iteration 285 then evaluated the actual denominator-stripped same-parent primitive numerator oracle and corrected the insufficient denominator-only 9/50 basis claim.

Iteration 286 closes the remaining actual-oracle numerator reconstruction problem for every non-scaleless translation-closed family.

## Iteration 286 — complete non-scaleless numerator reconstruction

Newly certified raised-triangle sectors in complete fixed-coordinate total-degree `<=6` / 210-monomial bases:

- `(0,0.21)`: train rank `210/210`, condition number `6935.030221597978`, held-out relative max residual `2.7698947208544858e-11`;
- `(0.21,0.41)`: train rank `210/210`, condition number `8545.513087076448`, held-out relative max residual `1.0083215501606952e-11`.

Retain from Iteration 285:

- triangle `(0,0.41)`: degree<=6 / 210, held-out relative max residual `8.872284498320589e-11`;
- bubble-a: degree<=4 / 70, held-out relative max residual `9.296403942129201e-10`;
- bubble-b: degree<=4 / 70, held-out relative max residual `2.223469270656875e-9`.

Freeze:

`PASS_COMPLETE_NONSCALELESS_ACTUAL_ORACLE_NUMERATOR_RECONSTRUCTION_ALL_BUBBLE_AND_TRIANGLE_SECTORS`.

The null raised bubbles and single squared-denominator sector remain scaleless in the frozen massless dimensional-regularization treatment.

## Retained Iteration-285 correction

The denominator-only scalar bases of dimensions 9 (bubble) and 50 (triangle) are **not** complete for the actual same-parent numerator because soft momentum and TT polarization structures remain in the numerator. Do not use them for tensor/IBP reduction.

Retain instead:

- exact translation closure;
- nonzero translation-closed and timelike `B3`/orbit trace;
- 23 primitive denominator branches;
- raised bubble/triangle topology with no closed box master;
- canonical repeated-index sectors;
- exact degree ceilings `4/6`;
- actual same-parent oracle;
- complete 70/210 held-out reconstruction certificates.

## Current C5 blocker

`BLOCKED_IBP_TENSOR_MOMENT_REDUCTION_AND_HARD_CHANNEL_COEFFICIENT_EXTRACTION`.

Numerator existence/completeness is no longer the blocker. The remaining task is to export the actual complete polynomial coefficients, map them to tensor moments (or an explicitly complete covariant basis including soft momentum and TT polarizations), perform dimensional-regularization tensor/IBP reduction inside the frozen raised bubble/triangle families, and extract the retarded logarithmic/discontinuity coefficient functions.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 285: **0 percentage points**. A real reconstruction blocker closed, but no linked comparator coordinate or comparator-subtracted robust residual has yet been obtained.

## Classification discipline

Iteration 286 is a scoped numerator-reconstruction PASS. It is not a Candidate Gravity consistency PASS/FAIL, not exact comparator identity, not regime-specific non-identifiability, not near-degeneracy, and not a novelty certificate.

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
- Retain degree ceilings `<=4` for raised bubbles and `<=6` for raised triangles unless parent dynamics changes.
- Full rank of a proposed sampling matrix does not prove basis completeness; held-out actual same-parent oracle residuals are mandatory.
- Do not use superseded 9/50 denominator-only numerator bases.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.

## Iteration 286 authority files

- `candidate_gravity/C5_COMPLETE_TRIANGLE_RECONSTRUCTION_ITERATION286.md`
- `candidate_gravity/code/iteration286_complete_triangle_reconstruction.py`
- `candidate_gravity/results/iteration286_complete_triangle_reconstruction.json`
- `research_log/2026-09-02_iteration_286_complete_non_scaleless_numerator_reconstruction.md`
- `candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_286.md`

## Exact next gate — Iteration 287

1. Export the actual complete 70-monomial bubble-a/bubble-b coefficient vectors rather than only residual metrics.
2. Map them losslessly to symmetric tensor moments of ranks `0..4` for `1/[(l^2)^2((l+q)^2)]`.
3. Perform dimensional-regularization tensor/IBP reduction and extract the retarded logarithmic/discontinuity coefficient, verifying loop-reflection invariance and scaleless cancellations.
4. Repeat for all three degree<=6 / 210 triangle sectors with tensor ranks `0..6`.
5. Only after physical coefficient extraction proceed to source/Ward/contact completion and the Lorentzian comparator quotient. `ANSATZ-003`, Fisher/resources and blind heavy full-C5 remain forbidden.
