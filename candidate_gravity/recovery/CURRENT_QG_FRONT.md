# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 285**

## Current scientific state

Iterations 278–280 established translation-closed timelike C5 support with nonzero physical routed B3/orbit trace, non-scaleless bubble-a/bubble-b/triangle support and a rank-3 scalar retarded cut-support basis. Iteration 281 rejected a constant fitted-master surrogate. Iteration 282 exactly canonicalized the raised-index denominator sectors. Iteration 283 proved exact numerator degree ceilings: raised bubbles `<=4`, raised triangles `<=6`. Iteration 284 proved affine loop shifts preserve those ceilings and that the proposed denominator-only 9/50 sampling matrices are full rank.

Iteration 285 now evaluates the **actual denominator-stripped same-parent primitive numerator oracle** and shows that the 9/50 basis-sufficiency claim is false, while the exact degree ceilings and denominator canonicalization remain valid.

## Iteration 285 — actual numerator oracle and basis correction

The exact 23 primitive branches are obtained by splitting

- `Q0=-eta/p^2`,
- `Q1=-Q0 N1 Q0`,
- `Q2=Q0(N1 Q0 N1 + N1 Q0 N1 - N2)Q0`

before sector summation.

The primitive oracle reproduces the direct translation-closed B3 object with

- `tr B3 = 0.9605914097678994`;
- `||B3||_F = 1.3106212324929962`;
- primitive-vs-direct matrix residual `1.32e-12`.

Freeze:

`PASS_EXACT_DENOMINATOR_STRIPPED_SAME_PARENT_PRIMITIVE_NUMERATOR_ORACLE`.

### Basis audit

The Iteration-283/284 denominator-only scalar bases fail on held-out oracle points:

- bubble-a, 9 columns: relative max error `0.9481450100`;
- bubble-b, 9 columns: relative max error `0.6811050545`;
- raised triangle `(0,0.41)`, 50 columns: relative max error `33.2055942841`.

Conservative full fixed-coordinate polynomial bases at the already-certified degree ceilings pass:

- bubble-a, degree<=4 / 70 monomials: relative max residual `9.30e-10`;
- bubble-b, degree<=4 / 70 monomials: relative max residual `2.22e-9`;
- raised triangle `(0,0.41)`, degree<=6 / 210 monomials: relative max residual `8.87e-11`.

Freeze:

`C5-NG-018 — DENOMINATOR_TOPOLOGY_DOES_NOT_EXHAUST_SAME_PARENT_NUMERATOR_TENSOR_DEPENDENCE`.

Freeze:

`PASS_ACTUAL_NUMERATOR_ORACLE_AND_FAIL_TOPOLOGY_ONLY_9_50_BASIS_WITH_COMPLETE_70_210_RECONSTRUCTION_CERTIFICATES`.

The reason is structural: the same-parent numerator retains dependence on the null-soft momentum and TT polarization tensors. Propagator topology alone does not determine a complete numerator basis.

## Superseded vs retained

Superseded only:

- Iterations 283-284 claim that basis dimensions 9 and 50 are sufficient for the actual numerator reconstruction.

Retained:

- exact translation closure;
- translation-closed B3 nonzero;
- timelike B3/orbit trace nonzero;
- 23 primitive denominator branches;
- raised bubble/triangle topology and no closed box master;
- canonical raised-index sectors;
- exact numerator degree ceilings `4/6`;
- affine loop-shift degree preservation;
- scalar hard-channel cut support.

## Current C5 blocker

`BLOCKED_COMPLETE_TENSOR_AWARE_NUMERATOR_RECONSTRUCTION_AND_IBP_REDUCTION`.

The bubble sectors now have complete degree<=4 held-out reconstruction certificates. One of three raised-triangle sectors has a complete degree<=6 held-out reconstruction certificate. The remaining two triangle sectors and a complete IBP/tensor-moment or explicitly covariant representation are still required before physical discontinuity coefficients may be frozen.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 284: **0 percentage points**. Iteration 285 is a reconstruction correction and completeness certificate, not yet a linked comparator coordinate or comparator-subtracted residual.

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
- Retain degree ceilings `<=4` for raised bubbles and `<=6` for raised triangles unless the parent dynamics changes.
- Full rank of a proposed sampling matrix does not prove basis completeness; actual same-parent held-out oracle residuals are mandatory.
- Do not use the superseded denominator-only 9/50 bases for tensor/IBP reduction.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full C5 run: NOT AUTHORIZED.

## Iteration 285 authority files

- `candidate_gravity/C5_ACTUAL_NUMERATOR_BASIS_AUDIT_ITERATION285.md`
- `candidate_gravity/code/iteration285_actual_numerator_basis_audit.py`
- `candidate_gravity/results/iteration285_actual_numerator_basis_audit.json`
- `research_log/2026-09-02_iteration_285_actual_numerator_basis_audit.md`
- `candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_285.md`

## Exact next gate — Iteration 286

1. Complete degree<=6 / 210-monomial held-out reconstruction for raised-triangle sectors `(0,0.21)` and `(0.21,0.41)`.
2. Preserve the validated 70-monomial bubble-a and bubble-b reconstructions.
3. Convert all complete polynomial coefficients into an IBP/tensor-moment representation, or construct an explicitly complete covariant basis including the soft momentum and TT polarization tensors and cross-check it against the 70/210 oracle.
4. Only after this completeness step extract the hard-channel logarithmic/discontinuity coefficient functions.
5. Source/Ward/contact completion, Lorentzian comparator quotient, Fisher/resources and `ANSATZ-003` remain downstream/forbidden.
