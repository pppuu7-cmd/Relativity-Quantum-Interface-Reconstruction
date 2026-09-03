# RQIR Candidate Gravity Recovery Delta — Iteration 371

Date: 2026-09-04

MODEL_READINESS: 24%

## Validated authority

Iteration 371 raw artifact was downloaded and inspected independently of workflow conclusion.

- workflow: `rqir-iteration371-tru1sq-repeated-factor-cancellation`
- run: `33807185162`
- job: `100820348982`
- artifact: `9913397316`, `iteration371-result`
- artifact digest: `sha256:eb3702b2e830a57b3020ebd13c2f146e99bc9a24de2c2471f40fdd0dd18cf40a`
- raw scientific JSON SHA-256: `f887b859e687906d834398f9583ccd43ddb01deb33b846e3f1f8b676b3569283`
- authority-audit JSON SHA-256: `e2b63d4138d8df96284010067a453df886274ea8878e1dd5e1c156814c7c3550`
- workflow head: `62bd1e83ca6c752cb9235f520a6d723d953a2d51`

Freeze:

`PASS_TRU1SQ_REPEATED_FACTOR_PHYSICAL_CANCELLATION_CLASSIFICATION__SURVIVE_36__CANCEL_0__BLOCKED_0`

## Scientific result

Across the 21 physically distinct `Tr U1^2` families, the raw denominator census contains 36 multiplicity-two targets. Every one of these 36 targets passes the symmetric massless-shell stripped-numerator test as

`DOUBLE_POLE_NUMERATOR_SURVIVES`.

Counts:
- repeated-factor tests: `36`;
- physical double poles surviving: `36`;
- cancelled repeated factors: `0`;
- BLOCKED shell-limit cases: `0`.

Frozen shell-limit thresholds were not weakened:
- shell energy `E=0.73`;
- symmetric relative-energy steps `{2e-3,1e-3,5e-4}`;
- other-denominator separation `>=2e-2`;
- midpoint convergence `<=5e-2`;
- cancellation ratio `<=2e-2`;
- survival ratio `>=2e-1`.

Therefore apparent repeated denominator multiplicity in this sector is now physical double-pole authority rather than a raw-topology proxy. This result does not itself authorize any ordinary-simple Cutkosky substitution or normalized discontinuity integration.

## Anti-idle continuation

Iteration 372 was created and launched as the immediate next allowed topology gate. It enumerates all timelike two-line channels of the 21 distinct physical families and types each channel by exact pole multiplicities as `simple-simple`, `simple-double`, or `double-double`. No integration is performed.

- code commit: `54914cf6026b52c836958eac1eed33e9d703125b`
- workflow head: `16c262b221c5d02cb5a6c6129e4e1cb6fca96a3b`
- run: `33807434918`
- status at recovery write: `queued`

## Guardrails

All 21 physical families remain distinct from Iteration 370. Double poles may not be treated with ordinary-simple cut formulas. Unsupported remains BLOCKED, never zero-filled. No Source/Born subtraction, `ANSATZ-003`, Fisher/resources, or blind heavy full-C5.

## Exact next gate

Consume Iteration 372 raw artifact. Then split channels by singularity type. For simple-simple channels, certify numerator-on-shell regularity and all uncut-denominator separation before normalized integration. For simple-double/double-double channels, use the frozen auxiliary-mass derivative/distributional bridge generalized to the exact multiplicities and validate its kinematic prerequisites before integration.

Authoritative iteration: 371.
MODEL_READINESS: 24%
