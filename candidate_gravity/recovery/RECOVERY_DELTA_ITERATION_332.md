# Recovery Delta — Iteration 332

**Date:** 2026-09-03  
**MODEL_READINESS:** 24%  
**Scientific status:** PASS within scoped timelike closed-triad numerator-family fixture.

## Validated provenance

- workflow: `rqir-iteration332-det-timelike-closed-triad-numerator-family-fixture`
- run: `33743302046`
- job: `100609965778`
- artifact: `9888598043` (`iteration332-result`)
- artifact digest: `sha256:8d8210b882bd4d5cba45be1e5c2efd89f9fee025d14e6d8c5f942e12c9f2c70c`
- scientific JSON SHA-256: `29a3e65146a03c8a0487c4a39d9b809ed985697fa0d5244ceca77e452aba7795`
- scientific exit code: `0`
- sentinel/schema audit: one top-level JSON object, iteration `332`, `scientific_authority_pass=true`.

## Authority

`PASS_TIMELIKE_CLOSED_TRIAD_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_FAMILY_FIXTURE`

The repaired run changes only NumPy-to-builtin JSON scalar serialization relative to the first failed operational attempt. It validates the exact rank-2 closed timelike triad
`q1=(1,0,0,0)`, `q2=(-0.4,0.1,0.1,0)`, `q3=(-0.6,-0.1,-0.1,0)` with
`q_i^2=(-1,-0.14,-0.34)` in signature `(-,+,+,+)`.

The already-frozen one-common-background physical H/N construction and shifted determinant routing reconstruct into `1 singleton + 3 bubble + 1 signed-affine triangle` canonical denominator families. Maximum held-out numerator reconstruction scaled error is `2.7755575615628914e-17`; maximum held-out denominator-map scaled error is `1.1102230246251565e-16`, both far below the unchanged `5e-10` threshold.

This is direct-timelike integrand-family authority only. It is not by itself a nonzero discontinuity certificate, not a comparator residual, and not authority for the full finite DR remainder.

## Next gate

Iteration 333 performs family-by-family direct-timelike cut-origin reduction. Bubble families are tested on exact massless two-line Cutkosky surfaces with deterministic angular convergence. Triangle two-line cuts are fail-closed: if the uncut denominator crosses the cut sphere, that channel is `BLOCKED` pending explicit causal `i0`/distributional treatment rather than zero-filled or silently principal-valued.

## Guardrails retained

- Iteration-297 evanescent/scheme warning remains binding for the full finite DR remainder.
- Source/Born subtraction remains forbidden until matched-observable pole/cut-origin classification is complete.
- `ANSATZ-003` remains uncreated.
- Fisher/resources remain forbidden.
- physical U2 remains independently BLOCKED; no zero-fill.
- no blind heavy full-C5 and no reopening of closed C5 `e=3`.

MODEL_READINESS: 24%
