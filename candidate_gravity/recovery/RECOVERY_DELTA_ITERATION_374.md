# Recovery Delta — Iteration 374

**Result consumed:** 2026-09-04  
**MODEL_READINESS:** 24% (`+0 pp`)  
**Classification:** `PASS_TRU1SQ_SIMPLE_SIMPLE_NORMALIZED_DISCONTINUITY__ALL_6_CONVERGED`

## Scope
Physical repository-normalized discontinuity for only the six Iteration-373 `REGULAR` simple-simple `Tr(U1^2)` channels. The reduced one-loop coefficient `-i/4` is not folded into these `Tr U1^2` coordinates.

## Validated result
All `6/6` channels are `CONVERGED`; `BLOCKED_CONVERGENCE=0`.

q2-resolved ordinary-simple sums:
- `q^2=-1.0`: `D_s TrU1sq_simple_simple = 6.253219881951187e-05 + 0 i`;
- `q^2=-0.34`: `D_s TrU1sq_simple_simple = 3.5044107116946374e-05 + 0 i`;
- `q^2=-0.14`: `D_s TrU1sq_simple_simple = 2.9297648005638963e-05 + 0 i`.

Each q2 bucket is `NONZERO`; distinct q2 coordinates remain separate.

Numerical controls:
- maximum scaled angular convergence error: `9.023987581011366e-10` < frozen `2e-5`;
- maximum radial Richardson scaled error: `3.1484214649442344e-17` < frozen `5e-4`;
- maximum cut-shell absolute error: `7.35968036186944e-17` < frozen `2e-10`;
- minimum sampled uncut absolute denominator: `0.12097829436145643` > frozen `1e-10`.

Normalization remains the Iteration-337 ordinary-simple bridge `D_s I = - sphere_mean`.

## Provenance
- run: `33812352303`
- job: `100836834321`
- workflow head: `cb2ddc7d838d0ba1844339d447445b3a8a613124`
- artifact: `9915759849`
- artifact digest: `sha256:2293a37961230bed7eaed2298fcfaddfcffb342c2e5579b29b9e73986b47450d`
- raw scientific JSON SHA-256: `ad84a0e59751171f906e0fbd9b868357e19b3cf8ce948970b3b529e134e84c3c`
- raw authority audit: one top-level JSON, expected iteration 374, `scientific_authority_pass=true`.

## Consequence
The ordinary-simple physical `Tr U1^2` sub-sector is closed. The remaining physical `Tr U1^2` work consists of the 36 simple-double and 15 double-double channels already methodically validated by Iteration 375 and kinematically certified by Iteration 377.

## Guardrails
No effective-action `-i/4` folding in this coordinate; repeated-pole channels excluded from this result; distinct q2 buckets never summed; no source/Born subtraction; no `ANSATZ-003`; no Fisher/resources; no blind full-C5.

MODEL_READINESS: 24%
