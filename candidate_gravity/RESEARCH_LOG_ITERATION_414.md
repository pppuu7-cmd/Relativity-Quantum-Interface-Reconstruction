# Candidate Gravity Research Log — Iteration 414

Date: 2026-09-04

Repository source of truth was re-read first: `CURRENT_QG_FRONT.md`, `RECOVERY_DELTA_ITERATION_413.md`, `RESEARCH_LOG_ITERATION_413.md`, recent commits, and Actions. Physical/operator authority is Iteration 411; structural authority is Iteration 410; the exact unresolved double-double physical set is `[2]`. Iteration-413 run `33861440653` was still in progress and was not duplicated.

Iteration 414 freezes a prospective, non-promoting auxiliary-mass error predictor using only authoritative Iteration-411 values for index 2 / class 3 / `q^2=-1`: `D(5e-6)=-0.003560682203382001` and `D(2.5e-6)=-0.0036107242774472896`, whose scaled discrepancy is `5.0042074065288766e-05 > 2e-05`.

Under the explicit hypothesis that the central4 x central4 mixed-derivative error is leading-order truncation dominated, the error is `O(h^4)`, so a halving should reduce the pair discrepancy by about 16. The active Iteration-413 pair `2.5e-6 -> 1.25e-6` therefore has a prospectively frozen expected scaled discrepancy `3.127629629080548e-06`, below the unchanged `2e-05` physical gate. A Richardson diagnostic from Iteration 411 alone gives extrapolated mixed derivative `-0.003614060415718309` and estimated absolute error `3.336138271019251e-06` for the `2.5e-6` member.

These numbers are diagnostic predictions, not physical authority. No `D_s` is promoted and nothing is inserted into `Tr U1^2`. The purpose is to eliminate post-hoc interpretation freedom: if Iteration 413 does not show the predicted order-4 improvement, the next gate is dedicated auxiliary-mass derivative representation / cancellation-roundoff analysis, not threshold weakening or angular-grid escalation.

Reproducible code: `candidate_gravity/code/iteration414_channel2_mass_step_error_predictor.py`; result: `candidate_gravity/results/iteration414_channel2_mass_step_error_predictor.json`.

MODEL_READINESS: 24%

Change: 0 pp. This closes a methodological interpretation contract only; no stable readiness-rubric bucket is complete.
