# Candidate Gravity Research Log — Iteration 411

Date: 2026-09-04

Repository source of truth was re-read first: `CURRENT_QG_FRONT.md`, latest recovery, recent commits and current Actions state. Iteration 409 remained the latest validated physical/operator authority; Iteration 410 was the active structure-only recovery for unresolved double-double indices `[2,11]`.

Iteration 410 run `33847425175` completed successfully. Green workflow status was not treated as authority: both artifacts were downloaded and their scientific JSON plus authority-audit records were checked independently. Index 2 passed the frozen structure oracle with raw SHA-256 `dbaea9b9d015d6df7ab465c0748596462949eb682a8a2a662f88b5d667e8d2c7`; index 11 passed with raw SHA-256 `2ecfc9d9812a8258803e20e6e402df3c93dac2f0245bf61e390517839605693b`. Both are structure-only PASS and promote no physical D_s value.

With no already-running nonduplicative physical follow-up for those targets, Iteration 411 was created and launched. It specializes the already-frozen Iteration-407 analytic/spectral physical reduction separately to indices 2 and 11. The parent physical integrand, central4 x central4 mass stencil, `D_s=-sphere_mean[d_u d_v G]`, direct original-integrand held-out cross-check, `2e-5` physical convergence threshold and all structural thresholds are unchanged. Evaluator commit `1e01f7f4abf3ee00daafcf3580019a74ada9a670`; workflow/head commit `a50b25c408903112dc6962487b58478a7f34e3f3`; run `33851983789`.

The race-created repaired Iteration-408 run `33847487303` subsequently completed. Its green status was not used as authority: artifact `9929332270` with digest `sha256:d537f46afbadc538df9f87fe52d5659cb8d2a8657925c61c9ba32076099a9965` was downloaded and raw-inspected. `iteration408_result.json` SHA-256 is `d568406b391dc22e5a7d15330ff162b18f5abc43c4bfe8c2ef3fc868cccc6c5c`; it reports the structure-only PASS `PASS_TRU1SQ_BLOCKERS2_11_ANALYTIC_AZIMUTH_STRUCTURE_ORACLE`. This is consistent with, but operationally superseded by, the split Iteration-410 raw authority. It promotes no physical value and changes no blocker.

At the latest audit Iteration-411 run `33851983789` remains in progress. Jobs `100956624953` (index 2) and `100956624748` (index 11) are both still in the frozen physical analytic/spectral calculation step; raw authority audit and artifact upload are pending and no Iteration-411 artifact exists yet. Therefore no duplicate heavy run was launched.

MODEL_READINESS: 24%

Change: 0 pp. Exact next gate remains fail-closed raw validation of both Iteration-411 physical artifacts. Only converged raw-validated targets remove their corresponding physical blockers; any blocked target remains BLOCKED and is not zero-filled.
