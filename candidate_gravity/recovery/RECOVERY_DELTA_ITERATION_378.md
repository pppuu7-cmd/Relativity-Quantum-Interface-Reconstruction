# Recovery Delta — Iteration 378

**Date:** 2026-09-04  
**MODEL_READINESS:** 24% (`+0 pp`)  
**Classification:** `PASS_TRU1SQ_SIMPLE_DOUBLE_ONE_CHANNEL_PILOT__CONVERGED`

## Scope
One prospectively selected physical simple-double `Tr U1^2` repeated-cut channel only. This gate validates the full physical auxiliary-mass derivative integration pipeline and measures runtime. It does **not** authorize extrapolating the pilot value to the other 35 simple-double channels.

## Raw validated result
- frozen selection rule: first simple-double channel in Iteration-372 order
- class: `2`
- `q^2=-0.34`
- multiplicities: `2 x 1`
- status: `CONVERGED`
- normalized operator coordinate: `D_s Tr U1^2 = -2.5401676390398016e-05`
- low-grid derivative: `-2.5401700122829485e-05`
- high-grid derivative: `-2.5401676390398016e-05`
- shifted-high derivative: `-2.540167994677779e-05`
- half-step derivative: `-2.5401674468932236e-05`
- scaled convergence error: `2.3732431469379806e-11` < frozen `2e-5`
- max radial Richardson scaled error: `1.4121990715230322e-16` < frozen `5e-4`
- max cut-shell error: `1.726049858596923e-16` < frozen `2e-10`
- minimum sampled uncut denominator: `0.2609889252677208` > frozen `1e-10`
- minimum Kallen function: `0.11559320009999997` > 0
- runtime: `1312.8183083709998 s` (~21.88 min)

The raw result SHA-256 independently recomputes to `637756f51e7ee0338a8d531edc5f1d2d58541ad803aa7c5dfd2026e2f9d33355`, exactly matching the authority audit.

## Provenance
- run: `33813604738`
- job: `100840748044`
- workflow head: `14255294b9b6d4dafd4ec0b769ccfd4318717ead`
- artifact: `9916310237`
- artifact digest: `sha256:eb426b188200236c07074b89b07f11cfefb4feaa74857b757bae73f478a8c62c`
- raw scientific JSON SHA-256: `637756f51e7ee0338a8d531edc5f1d2d58541ad803aa7c5dfd2026e2f9d33355`
- sentinel/schema: valid single top-level JSON; expected iteration `378`; `scientific_authority_pass=true`

## Consequence — prospectively frozen Iteration 381 architecture
Measured runtime authorizes scaling the **identical arithmetic** to all 36 simple-double channels in 12 fixed chunks of 3 channels each. Each chunk has a 90-minute job timeout. Physics, mass nodes, quadrature grids and convergence thresholds are unchanged from Iteration 378.

Iteration 381 code commit: `54b9529feea1826a4382ef9141a3750957a4ee88`.  
Iteration 381 workflow commit: `5ecb485240ffc39f4bd7b8950ec8963e7b06f92f`.  
Run: `33816213900` (queued at launch).

Full simple-double authority requires all 12 raw chunk artifacts, exactly 36 unique frozen indices with no gaps or overlaps, and later assembly preserving the three distinct `q^2` buckets. A chunk may return `BLOCKED_CONVERGENCE`; such a channel remains BLOCKED and is never zero-filled.

## Guardrails
Repeated poles are not ordinary simple cuts. Same `i0`. `D_s(simple-double)=+sphere_mean[d_mu G]`. No effective-action `-i/4` weight is folded yet. Distinct `q^2` coordinates are never summed. No threshold weakening. No source/Born subtraction. No `ANSATZ-003`. No Fisher/resources. No blind full-C5.

MODEL_READINESS: 24%
