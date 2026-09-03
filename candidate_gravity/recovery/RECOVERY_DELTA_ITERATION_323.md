# Recovery Delta — Iteration 323

**Date:** 2026-09-03  
**MODEL_READINESS:** 24%

## Raw Actions authority

- Workflow: `rqir-iteration323-det-shifted-propagator-routing-audit`
- Run: `33723183698`
- Job: `100546443379`
- Artifact: `9880968545` (`iteration323-result`)
- Artifact digest: `sha256:ca32103428c403b615aec0b62ffc392d3b8dcba1cb71d3f236ef71223a2a3048`
- Scientific result SHA-256: `39101bb6ee6aaf49dca554474fa40fb260c6bfa8bc770f7767d8a49e80933880`
- Authority audit: one top-level JSON object, expected iteration `323`, `scientific_authority_pass=true`.

## Scientific result

Classification:
`PASS_SHIFTED_PROPAGATOR_ROUTING_AUDIT__ITERATION322_COEFFICIENT_REMAINS_LOCAL_ROUTING_FIXTURE`

The audit found:

- `single_K0_inverse_assignment=true`
- `A_uses_single_K0_inverse=true`
- `explicit_shifted_K0_inverse=false`
- pair and triple trace terms are present.

Therefore the Iteration-322 number is retained as a validated momentum-closed **local operator/routing fixture only**. It is not promoted to a physical loop-integrand determinant coefficient because the functional trace must contain successive free inverses evaluated at shifted loop momenta `K0^{-1}(p+Q)` between Fourier insertions.

## Consequence

`physical_denominator_routing_ready=false`. Denominator-family reduction and pole/cut-origin classification remain BLOCKED until explicit shifted propagator routing is implemented and validated. No Source/Born subtraction is allowed yet.

## Next gate

Implement an explicit ordered pair/triple functional-trace routing engine on the closed triad with cumulative momentum shifts and validate cyclic-routing equivalence. Physical numerator insertion kernels must subsequently be evaluated at their correct incoming momenta before any full determinant coefficient is promoted.

## Guardrails retained

- Preserve Iteration-322 numerical PASS but narrow its interpretation; do not alter prior thresholds.
- Unsupported kernels/coordinates are `BLOCKED`, never zero-filled.
- No `ANSATZ-003` before robust comparator-subtracted residual.
- No Fisher/resources before robust nonzero residual.
- No Source/Born subtraction before matched-observable pole/cut-origin classification.
- No blind heavy full-C5; do not reopen closed C5 `e=3`.

MODEL_READINESS: 24%
