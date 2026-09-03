# RQIR Candidate Gravity — Recovery Delta Iteration 382

**Date:** 2026-09-04  
**Status:** ACTIVE / NOT YET SCIENTIFIC AUTHORITY  
**Previous validated authority:** Iteration 378  
**MODEL_READINESS: 24%**

## Purpose
Recover the still-open 48 physical timelike `Tr U2` cut-through-double-pole channels without treating operationally cancelled Iterations 364 or 376 as scientific results.

## Frozen parent contract
Iteration 382 does **not** change the Iteration-364 physics arithmetic. It imports `channel_derivative` verbatim and keeps:
- Iterations 359/362/363 parent authority;
- the same repeated-pole auxiliary-mass derivative identity and sign;
- `BASE_H=5e-6`, `HALF_H=2.5e-6`;
- low grid `6x12`, high grid `8x16`;
- half-phi-step cross-check;
- convergence threshold `2e-5`;
- cut-shell threshold `2e-10`;
- the same routing, physical numerator and normalization;
- no effective-action `+i/2` weight folded.

## Why the resource architecture changed
Iteration 364 was cancelled before sentinel/schema/artifact. Iteration 376 preserved the same arithmetic but used three fixed 16-channel jobs with a 30-minute timeout; all three jobs were cancelled during the scientific step at the timeout and produced no sentinel or artifact. Therefore neither attempt supplies scientific PASS/FAIL authority.

Iteration 382 prospectively selects exactly global channel index `0` from the frozen 48-channel ordering and evaluates that one channel only. This is a resource/pipeline pilot. Its eventual value can become authority only for that one preselected channel after raw artifact + sentinel validation; it can never close the other 47 channels by extrapolation.

## Reproducibility
Added:
- `candidate_gravity/code/iteration382_u2_repeated_cut_one_channel_pilot.py`
- `.github/workflows/rqir-iteration382-u2-repeated-cut-one-channel-pilot.yml`

Workflow run: `33816704205`, job `100850328336`, head `7fb92f2bd6488ccf7b7a4aaf141bd913ad2aa46a`.

At this recovery checkpoint the scientific step is still `in_progress`; sentinel/schema audit and artifact upload are pending. Therefore **Iteration 382 is not promoted to Candidate Gravity authority in this delta**.

## Classification discipline
- Iterations 364/376: **operational cancellation**, not scientific FAIL and not zero.
- Iteration 382 current state: **ACTIVE / operationally unresolved**, not PASS, FAIL, identity, non-identifiability, near-degeneracy, or novelty certificate.
- The other 47 `Tr U2` cut-through-double-pole channels remain open and cannot be zero-filled.

## Readiness
`MODEL_READINESS: 24%`

Change from previous assessment: `0 pp`. A safer resource-recovery experiment was launched, but no additional readiness-rubric component closes until a raw validated physical result is obtained and eventually the complete `Tr U2` coordinate is assembled.

## Exact next gate
Consume run `33816704205` only after raw artifact and sentinel/schema validation. If the preselected channel is `CONVERGED`, use measured runtime **only prospectively** to freeze a smaller complete-48 chunk architecture with identical arithmetic and unchanged thresholds. If it is `BLOCKED_CONVERGENCE`, isolate this channel with stronger angular/analytic treatment without weakening the frozen threshold.
