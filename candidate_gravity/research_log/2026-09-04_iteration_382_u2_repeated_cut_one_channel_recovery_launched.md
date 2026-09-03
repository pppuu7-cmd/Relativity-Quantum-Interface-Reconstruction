# 2026-09-04 — Candidate Gravity Iteration 382

## Scope
Prospective one-channel recovery pilot for the 48 still-open physical timelike `Tr U2` cut-through-double-pole channels.

The factual repository front before this step remained validated through Iteration 378. Active Iterations 379/380/381 were checked and deliberately not duplicated.

## Scientific/resource decision
Cancelled Iterations 364 and 376 provide no scientific PASS/FAIL authority because their scientific steps ended before sentinel/schema/artifact. Iteration 376 used three 16-channel jobs and all three reached the fixed 30-minute timeout. The new recovery therefore narrows resource granularity before attempting another complete 48-channel architecture.

Iteration 382 selects only global channel index `0` in the already frozen Iteration-359/364 ordering. It imports Iteration-364 `channel_derivative` verbatim; no threshold, auxiliary-mass nodes, quadrature, sign, routing, numerator, normalization, q2 convention, or effective-action weight is changed.

Files added:
- `candidate_gravity/code/iteration382_u2_repeated_cut_one_channel_pilot.py`
- `.github/workflows/rqir-iteration382-u2-repeated-cut-one-channel-pilot.yml`

Run `33816704205`, job `100850328336`, head `7fb92f2bd6488ccf7b7a4aaf141bd913ad2aa46a` was launched. At this checkpoint its scientific step is still in progress; no raw artifact exists yet, so this log does **not** promote Iteration 382 to scientific authority.

## Classification
Current state: **ACTIVE / operationally unresolved**.

This is not a consistency FAIL, not an exact comparator identity, not regime-specific non-identifiability, not near-degeneracy, and not a novelty certificate. The other 47 channels remain open and unsupported values are never zero-filled.

MODEL_READINESS: 24%

Readiness change: `0 pp`. The resource architecture is safer and reproducible, but no readiness-rubric component closes before raw validation and complete physical-sector closure.

## Exact next gate
Validate the raw Iteration-382 artifact and sentinel. If channel 0 is `CONVERGED`, use its measured runtime only to prospectively freeze a smaller complete-48 chunk architecture with identical frozen arithmetic. If `BLOCKED_CONVERGENCE`, isolate only that channel with stronger angular/analytic treatment and leave thresholds unchanged.
