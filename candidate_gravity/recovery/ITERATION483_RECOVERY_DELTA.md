# RQIR Candidate Gravity — Iteration 483 recovery delta

Date: 2026-09-06

**MODEL_READINESS:** 24% (unchanged)  
**Physical promotion:** none  
**Classification:** `PASS_OCCURRENCE_COVERAGE_DISTINCT_FROM_ASSEMBLY_SENSITIVITY_COVERAGE__NON_PROMOTING`

## Source-of-truth input

The active heavy gate remains frozen Iteration-455 manifest rank 12 `(u,v)=(+1e-5,-1e-5)`, canonical run `33997856739`, job `101391409387`. At this iteration it is still `in_progress` on `Run manifest-rank12 full-z MP stage`; raw authority audit and artifact upload are pending. It is therefore not scientific PASS and must not be duplicated.

The already committed diagnostic result `candidate_gravity/results/post482_stencil_sensitivity_weight_audit.json` (result commit `be4c7bf93b06f78859464bd626341383656ba788`) is now adopted as a non-promoting research authority update.

## Exact stencil-L1 sensitivity facts

For central4 coefficient vector `c=(1/12,-2/3,+2/3,-1/12)`, the 4x4 mixed-derivative node weights are `W_ij=c_i c_j`, and

`sum_ij |W_ij| = (sum_i |c_i|)^2 = 9/4`.

This is a diagnostic sensitivity metric only. It is not a probability, does not replace occurrence-weighted coverage, and does not authorize support reordering.

- BASE ranks `0..11` are raw-certified and carry absolute stencil weight `17/8`, i.e. `17/18 = 94.444444%` of BASE stencil-L1 sensitivity.
- Remaining BASE ranks `12..15` carry only `1/8 = 1/18 = 5.555556%` of BASE stencil-L1 sensitivity.
- Rank 12 itself carries absolute weight `1/144`; if raw-consumed PASS, BASE diagnostic sensitivity coverage becomes `307/324 = 94.753086%`.
- Current HALF certification is only the four exact BASE/HALF overlap corners at ranks `5,6,9,10`, absolute weight `1/36`, i.e. `1/81 = 1.234568%` of HALF stencil-L1 sensitivity.
- HALF ranks `19,20,23,24` are the four inner-inner nodes and together carry `16/9`, i.e. `64/81 = 79.012346%` of HALF absolute stencil weight. They remain future stress points but may not be advanced ahead of frozen ranks `12..18`.

## Interpretation

The current `16/32 = 50%` occurrence-weighted support is a valid completion/provenance metric but is not a measure of derivative sensitivity. BASE is already strongly covered in stencil-L1 weight while HALF is barely stress-tested. This strengthens, rather than relaxes, the frozen requirement that all 28 distinct support coordinates be locally certified before independent BASE/HALF MP80/MP120 assembled closure.

No threshold, estimator, source order, support identity, physical `D_s`, ansatz, Fisher gate, or resource gate changes.

## Active gate

Raw-consume rank 12 fail-closed after artifact upload. If and only if raw PASS, occurrence-weighted coverage advances from `16/32` to `17/32 = 53.125%`, and the next permitted heavy coordinate is frozen rank 13 `(u,v)=(+1e-5,-5e-6)`, multiplicity 1. If BLOCKED, localize the first failing `z/phi/radial` sample without threshold weakening or coordinate substitution.
