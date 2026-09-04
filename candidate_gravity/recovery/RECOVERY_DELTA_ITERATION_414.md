# Candidate Gravity Recovery Delta — Iteration 414

Date: 2026-09-04

MODEL_READINESS: 24%

## Source-of-truth entry state

At run start, `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `RECOVERY_DELTA_ITERATION_413.md`, `candidate_gravity/RESEARCH_LOG_ITERATION_413.md`, recent commits, and current GitHub Actions state were re-read. The repository—not stale chat state—showed physical/operator authority at Iteration 411, structural authority at Iteration 410, exact unresolved double-double set `[2]`, and active Iteration-413 run `33861440653` for the sole remaining blocker. That run was still `in_progress`, so it was not duplicated and no result from it was assumed.

## Iteration 414 — prospective auxiliary-mass truncation predictor

A cheap, independent methodological analysis was frozen before Iteration 413 completes. It uses only raw-authoritative Iteration-411 mixed derivatives for index 2 / class 3 / `q^2=-1`:

- `D(h=5e-6) = -0.003560682203382001`;
- `D(h/2=2.5e-6) = -0.0036107242774472896`;
- observed scaled discrepancy `5.0042074065288766e-05 > 2e-05`.

The central4 first-derivative stencil has leading truncation order `O(h^4)`; applying it in both auxiliary-mass directions still gives a leading mixed-derivative discretization error of order `h^4` under the truncation-dominated hypothesis. Therefore one further halving should reduce the leading discrepancy by approximately `2^4=16`.

Prospectively frozen prediction for the active Iteration-413 pair `2.5e-6 -> 1.25e-6`:

- expected signed pair difference: `-3.127629629080548e-06`;
- expected scaled pair difference: `3.127629629080548e-06`;
- unchanged physical threshold: `2e-05`;
- therefore the pure leading-order truncation model predicts a numerical PASS.

A Richardson diagnostic using Iteration-411 values only gives

- extrapolated mixed derivative `-0.003614060415718309`;
- estimated absolute error of the `h=2.5e-6` member `3.336138271019251e-06`.

These are diagnostic predictions only. They are **not physical authority**, are not inserted into any `Tr U1^2` sum, and cannot close index 2.

## Scientific interpretation contract

The prediction is intentionally frozen before seeing Iteration-413 output.

- If Iteration 413 raw-validates as `CONVERGED`, consume its actual raw value, close only index 2, then execute the already-frozen Iteration-412 exact15 assembly.
- If Iteration 413 remains `BLOCKED_CONVERGENCE` and the discrepancy fails to decrease approximately as an order-4 truncation error, treat this as evidence that cancellation/roundoff or another auxiliary-mass derivative representation issue dominates; move to dedicated derivative-representation/error analysis without weakening thresholds.
- If Iteration 413 remains blocked while showing the expected order-4 decrease, preserve the blocker and quantify the remaining truncation error; do not use another blind angular-grid ladder.

No comparator/novelty/consistency claim is made here. This is a scoped prospective numerical-method diagnostic.

Reproducible code: `candidate_gravity/code/iteration414_channel2_mass_step_error_predictor.py`.
Result: `candidate_gravity/results/iteration414_channel2_mass_step_error_predictor.json`.
Code commit: `ab1992c20402005da0dd09a52ee025ecba1f59c0`.
Result commit: `636af414f1a28c15933458484d39549042641fc6`.

MODEL_READINESS: 24%

Change: `0 pp`. The iteration removes post-hoc freedom in interpreting the next mass-step result but closes no readiness-rubric bucket and promotes no physical coordinate.
