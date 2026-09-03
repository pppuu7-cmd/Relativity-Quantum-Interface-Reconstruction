# Recovery Delta — Candidate Gravity Iteration 334

**Date:** 2026-09-03  
**MODEL_READINESS:** 24%  
**Status:** authoritative scoped BLOCKED result; not a Candidate Gravity consistency FAIL.

## Provenance

- workflow: `rqir-iteration334-det-triangle-q2minus1-highres-cut-resolution`
- run: `33748965082`
- job: `100627871946`
- artifact: `9891879802`
- artifact digest: `sha256:6cf1702b0a3733d9110d9316133037b327bf27de8cf9b9d7ba846d40d66718b8`
- scientific JSON SHA-256: `a01ec6eae6395edfd339b74ae0e43faed48aceff49cd3e06d4dac470595c5fe6`
- head: `adaf9e606d2503d016a8bbd9b82fceacb2067c5f`

## Result

The sole Iteration-333 `q^2=-1` signed-affine triangle channel remains
`BLOCKED_TRIANGLE_Q2_MINUS1_HIGHRES_DISCONTINUITY_RESOLUTION` under the unchanged normalized convergence threshold `2e-5`.

Deterministic Fibonacci-sphere means were:
- N=96: `0.00688185741457098`
- N=192: `0.006880603694626303`
- N=384: `0.006876461155359077`
- phase-shifted N=384: `0.006876204779348692`

The convergence-to-sample ratio is `2.2111065687680303e-4`, above the frozen threshold. The central-to-sample ratio is `0.36702862694482047`, so the channel is numerically substantial, but numerical nonzero authority is not promoted until convergence closes.

The uncut third denominator is analytically bounded away from zero on the cut sphere, exact affine range approximately `[0.11857864376269048, 0.40142135623730957]`; maximum cut-shell error was below `8.1e-17`. Therefore the blocker is quadrature convergence, not a causal/PV singularity.

## Guardrails retained

No threshold weakening; no numerator, parent dynamics, fixture, route or causal prescription change; unsupported remains BLOCKED; no `ANSATZ-003`; no Fisher/resources; no Source/Born subtraction; Iteration-297 finite-DR warning remains binding.

## Exact next gate

Use an independent stronger angular integration authority (tensor-product Gauss-Legendre in `z` with periodic azimuth quadrature and phase-shift cross-check), or derive an analytic angular integral. Do not recompute already-certified bubble or triangle channels.
