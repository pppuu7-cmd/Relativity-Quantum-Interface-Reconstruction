# RQIR Candidate Gravity Recovery Delta — Iteration 370

Date: 2026-09-04

MODEL_READINESS: 24%

## Validated authority

Iteration 370 raw artifact was independently downloaded and schema-audited.

- run `33806999857`
- job `100819748480`
- artifact `9913304080`, `iteration370-result`
- artifact digest `sha256:71135e2eca40651b78c83575d245356751488d387360e02e87084804b00f495f`
- raw scientific JSON SHA-256 `576b6fb43a634933cb0abb4f90fb09d2af71e5b0ea8402bdd2ee7de86a988005`
- authority-audit JSON SHA-256 `35ccb7989c9a86318809211a5be7e808b147e82f09b2ea52e5132772205792a9`
- workflow head `406f82d35b2199a956906635db64b3ddc43e0284`

Authority:
`PASS_TRU1SQ_PHYSICAL_NUMERATOR_TRANSPORT_TEST__0_OF_6_MULTIMEMBER_DENOMINATOR_PAIRS_EQUIVALENT`.

## Scientific result

All six denominator-only multi-member candidates from Iteration 369 fail the physical stripped-numerator transport test at three held-out loop momenta. Therefore none may be merged. The six best scaled transport errors are approximately `1.2202`, `1.4259`, `1.2565`, `1.0262`, `1.1598`, and `0.7230`, all vastly above the frozen `2e-4` threshold. Minimum held-out raw denominator magnitude is `0.019`, safely above the frozen `1e-5` floor.

Thus all **21 routed cyclic Tr U1^2 classes remain physically distinct numerator+denominator families** at this stage. This is a strong negative quotient result, not a Candidate Gravity consistency FAIL.

## Anti-idle continuation

Iteration 371 is now in progress and targets the remaining topology ambiguity: every apparent repeated raw denominator shift is approached on its massless shell using symmetric off-shell points. The full physical traced integrand is multiplied by the complete raw scalar denominator product, and the symmetric stripped-numerator limit is used to classify whether a repeated factor is cancelled, survives as a double pole, or remains explicitly BLOCKED.

- code commit `bbc44ce8f9d031104df9fe20eba637a73f3e621f`
- workflow head `62bd1e83ca6c752cb9235f520a6d723d953a2d51`
- run `33807185162`
- status at recovery write: `in_progress`

No Cutkosky integration is performed in Iteration 371.

## Guardrails

All 21 classes stay distinct unless a later stronger physical identity is proved. Apparent repeated shifts are not physical repeated poles until numerator cancellation is tested. BLOCKED is never zero-filled. No cut formula is applied to BLOCKED topology. No Source/Born subtraction, `ANSATZ-003`, Fisher/resources, or blind heavy full-C5.

## Exact next gate

Consume Iteration 371 raw artifact. Freeze only unblocked physical pole orders. Then classify timelike two-line cut support separately for the surviving simple/repeated families; any BLOCKED shell-limit cases require targeted analytic/higher-precision resolution before normalized discontinuity integration.

Authoritative iteration: 370.
MODEL_READINESS: 24%
