# Candidate Gravity Research Log — Iteration 411

Date: 2026-09-04

Repository source of truth was re-read first: `CURRENT_QG_FRONT.md`, latest recovery, recent commits and current Actions state. Iteration 409 remained the latest validated physical/operator authority; Iteration 410 was the active structure-only recovery for unresolved double-double indices `[2,11]`.

Iteration 410 run `33847425175` completed successfully. Green workflow status was not treated as authority: both artifacts were downloaded and their scientific JSON plus authority-audit records were checked independently. Index 2 passed the frozen structure oracle with raw SHA-256 `dbaea9b9d015d6df7ab465c0748596462949eb682a8a2a662f88b5d667e8d2c7`; index 11 passed with raw SHA-256 `2ecfc9d9812a8258803e20e6e402df3c93dac2f0245bf61e390517839605693b`. Both are structure-only PASS and promote no physical D_s value.

With no already-running nonduplicative physical follow-up for those targets, Iteration 411 was created and launched. It specializes the already-frozen Iteration-407 analytic/spectral physical reduction separately to indices 2 and 11. The parent physical integrand, central4 x central4 mass stencil, `D_s=-sphere_mean[d_u d_v G]`, direct original-integrand held-out cross-check, `2e-5` physical convergence threshold and all structural thresholds are unchanged. Evaluator commit `1e01f7f4abf3ee00daafcf3580019a74ada9a670`; workflow/head commit `a50b25c408903112dc6962487b58478a7f34e3f3`; run `33851983789`.

The older repaired Iteration-408 structural run may remain in progress due to a race, but it is superseded operationally by the raw-validated Iteration 410 and cannot promote physical authority or substitute for Iteration 411.

MODEL_READINESS: 24%

Change: 0 pp. Exact next gate is fail-closed raw validation of both Iteration-411 physical artifacts. Only converged raw-validated targets remove their corresponding physical blockers; any blocked target remains BLOCKED and is not zero-filled.
