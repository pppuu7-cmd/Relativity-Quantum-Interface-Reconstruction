# RQIR post-482 stencil-sensitivity recovery delta

Date: 2026-09-06

**MODEL_READINESS:** 24% (unchanged)  
**Physical promotion:** none

The active heavy gate remains frozen Iteration-455 manifest rank 12 `(u,v)=(+1e-5,-1e-5)`, canonical run `33997856739`, job `101391409387`. Do not duplicate it. Raw-consume fail-closed only after completion and artifact upload.

## Exact sensitivity map

For each BASE or HALF central4 mixed-derivative assembly, the coefficient vector is

`c = (1/12, -2/3, +2/3, -1/12)`

and the 4x4 node weights are `W_ij=c_i c_j`. The absolute stencil-weight total is

`sum_ij |W_ij| = (sum_i |c_i|)^2 = 9/4`.

This defines a diagnostic stencil-L1 sensitivity coverage. It is not a probability, does not replace occurrence coverage, and cannot authorize support reordering.

### BASE

Ranks `0..11` are raw-certified. Their absolute BASE stencil weight is exactly `17/8`, i.e.

`(17/8)/(9/4) = 17/18 = 94.444444%`.

The full remaining BASE tail ranks `12..15` carries only `1/8`, i.e. `1/18 = 5.555556%` of absolute BASE stencil weight. Rank 12 itself carries `1/144`; if it passes, the diagnostic BASE sensitivity coverage becomes `307/324 = 94.753086%`.

### HALF

The only currently certified HALF nodes are the four exact BASE/HALF overlap coordinates, manifest ranks `5,6,9,10`, which are HALF local corners. Their combined absolute HALF weight is only `1/36`, so current HALF stencil-L1 sensitivity coverage is

`(1/36)/(9/4) = 1/81 = 1.234568%`.

The four HALF inner-inner nodes at manifest ranks `19,20,23,24` each carry absolute weight `4/9`; together they carry `16/9`, i.e.

`(16/9)/(9/4) = 64/81 = 79.012346%`

of the total absolute HALF stencil weight. These are therefore the main future sensitivity stress points, although the frozen source order must still be followed exactly and they may not be advanced ahead of ranks 12-18.

## Interpretation

The currently quoted `16/32 = 50%` occurrence-weighted support is a valid provenance/completion metric but is not a measure of assembled derivative sensitivity. BASE is already strongly covered in the stencil-weight sense; HALF is not. This asymmetry strengthens the retained rule that no physical conclusion may be drawn from early BASE completion and that independent BASE/HALF MP80/MP120 assembled closure must remain blocked until all 28 distinct support coordinates are locally certified.

Classification: `PASS_OCCURRENCE_COVERAGE_DISTINCT_FROM_ASSEMBLY_SENSITIVITY_COVERAGE__NON_PROMOTING`.

Guardrails retained: no source reordering, no UV-swap deduplication, no threshold weakening, no estimator change, no physical `D_s` promotion, no ANSATZ-003, no Fisher/resources.
