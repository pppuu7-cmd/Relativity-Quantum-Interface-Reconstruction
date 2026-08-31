# Recovery Delta — RQIR Iteration 160

**Date:** 2026-08-31  
**MODEL_READINESS: 22%**  
**Authoritative change:** AS blocker refined from generic off-symmetric-data insufficiency to missing retarded Green-function / in-in prescription.

## Previous front

Iteration 159 froze `AS-FRG-TT-001` and correctly prohibited use of the published momentum-symmetric Euclidean TT three-graviton dressing as the full off-symmetric Lorentzian RQIR tangent.

## New authorities

- `candidate_gravity/ASYMPTOTIC_SAFETY_ACTION_AUDIT_ITERATION160.md`;
- `candidate_gravity/comparators/AS-FRG-TT-001.md` updated;
- `analysis/as_action_formfactor_audit_iteration160.py`;
- `results/as_action_formfactor_audit_iteration160.json`;
- `research_log/2026-08-31_iteration_160_as_action_causal_completion.md`;
- `recovery/RECOVERY_DELTA_ITERATION_160.md`.

## Refined result

The primary AS source reconstructs a covariant **Euclidean** background effective action through curvature-squared order with momentum-dependent form factors `f_R2(Delta)` and `f_Ricci2(Delta)`.

Consequently, within that truncation, off-symmetric Euclidean background vertices are derivable in principle from the action. Iteration 159's warning remains valid for the symmetric-point dressing itself, but the action-level data are richer than that one-dimensional projection.

The six RQIR triplets are all spacelike. The published analytic form-factor fits were evaluated on all 18 individual leg magnitudes as an action-data coverage diagnostic:

- `f_Ricci2` range: `-0.04680592285494515 ... -0.0037039902546036896`;
- `f_R2` range: `0.261312950235091 ... 0.6649777144616807`.

These are Euclidean comparator-data values only, not `chi2R` values.

## Remaining physical blocker

The Lorentzian nonlocal operators require a Green-function prescription. The primary source discusses the Green-function problem and possible constructions such as expansion about a flat-space Feynman propagator, without freezing the RQIR-specific retarded/in-in prescription.

Therefore:

`AS six-probe chi2R = BLOCKED_AS_RETARDED_GREEN_FUNCTION_PRESCRIPTION`.

Do not:

- select retarded continuation merely for convenience;
- use Euclidean fit values as ordered response;
- zero-fill unsupported AS coordinates;
- count this as an AS consistency failure.

## New retained identifiers

- `AS-NG-002 — EUCLIDEAN_ACTION_SUFFICIENT_CAUSAL_COMPLETION_NOT_FIXED`;
- `NG-FUNNEL-017 — NONLOCAL_EFFECTIVE_ACTION_REQUIRES_CAUSAL_RESPONSE_PRESCRIPTION`.

## Readiness

`MODEL_READINESS: 22%` — unchanged.

Accounting:

- comparator foundation `19/25`;
- robust unique residual `3/20`;
- parent dynamics `0/20`;
- candidate consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

No new retarded comparator column entered the complete quotient, so readiness does not increase.

## Exact restart instruction

Resume at **Iteration 161**.

Test the local IR derivative expansion of the same AS effective action against the existing local C5 EFT span. This is allowed because the local truncation admits the already-frozen source-completed retarded convention without an additional nonlocal Green-function ambiguity.

If the local AS directions lie in the C5 span, record a scoped AS/C5 degeneracy. Keep the genuinely nonlocal AS sector BLOCKED. If a local residual survives, stress-test source completion, field redefinitions and Ward identities before any promotion.

No `ANSATZ-003`, Fisher or resource work yet.
