# RQIR Candidate Gravity — Recovery Delta Iteration 329

Date: 2026-09-03

## Authoritative result

`PASS_COMMON_BACKGROUND_CLOSED_TRIAD_PHYSICAL_HN_FULL_CUBIC_ROUTING_CERTIFICATE`

Validated run `33737812923`, job `100592429867`, artifact `9886457281`, artifact digest `sha256:69b41c7c36aefe98c6e03523d97bbf2eaf639b9d3d831d8eb800bc6a9252bfe6`.

Scientific execution, sentinel/schema validation, upload and final scientific enforcement all passed.

## What changed

Iteration 327 showed that Iteration 326 could not itself be promoted as a common-background closed-triad numerator certificate because it rebound incoming `p` while loading historical H and N fixtures with different `qs/hs`.

Iteration 329 is a new gate version. It uses the Iteration-319 metric perturbations as one common background, replaces external momenta by the exact Iteration-322/324 closed triad, evaluates graviton H at each routed `p+Q`, and reconstructs ghost N from exactly the same `hs/qs/p` parent following Iteration 320. All `13` cubic sequences / `19` unique routed requests are covered with unchanged Iteration-326 thresholds.

The Iteration-327 negative result is retained as provenance and is not rewritten into a pass.

## Independent denominator result

Iteration 328 separately passes `PASS_TRIANGLE_TWO_ORIENTATIONS_ONE_SIGNED_AFFINE_INTEGRATION_FAMILY`: six triangle routes are two translation-only classes (`3+3`) but one denominator integration family after the valid loop reversal/translation quotient `p -> -p + C`. Numerator equivalence under this map is not yet certified.

Current structural family skeleton:

- singleton/tadpole-origin: `1`;
- bubble families: `3`;
- triangle integration families under signed-affine loop changes: `1`.

This skeleton is not a nonzero-cut certificate.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 328: `0 pp`. The common-background physical routing blocker closes, but no complete rubric bucket or robust comparator-subtracted residual closes.

## Exact next gate

Assemble the physical common-background cubic determinant integrand from Iteration-312 logdet weights + Iteration-324 shifted propagators + Iteration-329 routed H/N kernels. Canonically transform numerator polynomials into `1 singleton + 3 bubble + 1 signed-affine triangle` denominator families and validate the transformed representations at held-out loop momenta. Then classify scaleless/local/rational versus genuinely cut-capable origins before any DR/timelike-cut integration or Source/Born subtraction.

No `ANSATZ-003`, Fisher/resources, threshold weakening, zero-fill or blind heavy full-C5.
