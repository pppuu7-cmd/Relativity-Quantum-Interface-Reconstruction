# Candidate Gravity Research Log — Iteration 410

Date: 2026-09-04

Repository source of truth was read first: `CURRENT_QG_FRONT.md`, Iteration-409 recovery, the latest research log and recent commits. Latest validated authority was Iteration 409 with unresolved physical double-double indices `[2,11]`.

Iteration 408 run `33839449598` is now fail-closed classified as operational cancellation. Attempt 2 job `100928697231` was cancelled during the scientific step at the 45-minute resource boundary; raw authority audit was skipped. Artifact `9926539839` has digest `sha256:f7d8d24b3ed9ce6f9cb29f4d19daa5f714b08837bde253f1910c7443f2e1e67f` and contains a 0-byte `iteration408_result.json`. This is not structural FAIL, not PASS and not a zero result.

To avoid duplicating the timed-out two-target computation, Iteration 410 splits the exact same frozen structural oracle into one independent job for index 2 and one for index 11. The evaluator imports Iteration-408 structure arithmetic verbatim; only resource granularity changes. Structural thresholds remain `2e-11` for denominator affinity and `2e-6` for Fourier-tail, phase-mean and held-out polynomial tests. No D_s value can be promoted by this structure-only gate, and downstream physical convergence remains frozen at `2e-5`.

Evaluator commit `08f3fc070f1073bd8558b0ba0facaffb300f880b`; workflow launch commit `f642954f1a0ded452b801decdb8667f6dc23c4f0`; run `33847425175`. The run is active/not-yet-authoritative until both target artifacts are independently schema-audited.

MODEL_READINESS: 24%

Change: 0 pp. A real execution blocker has been isolated without changing physics or thresholds, but no new full readiness-rubric block has closed. Exact next gate is fail-closed raw validation of both Iteration-410 target artifacts, followed only on structural PASS by the already-frozen Iteration-407 physical reduction for the same index.
