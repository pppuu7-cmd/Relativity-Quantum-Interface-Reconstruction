# 2026-09-03 — Iteration 306 Iteration305 failure-observability audit

MODEL_READINESS: 24%

The repository front at launch was Iteration 304 with an active Iteration305 triangle-cut process. Recent Actions exposed an additional direct-timelike Iteration305 run `33702862824` / job `100485680662` at head `11e593ea1ff3b3e49043e14fb4ee76c22fe1006d`; it failed specifically in the scientific reduction step, while validation and artifact upload were skipped.

Classification:

`FAIL_OPERATIONAL_ITERATION305_DIRECT_TRIANGLE_RUN_DROPS_SCIENTIFIC_DIAGNOSTICS_ON_THRESHOLD_FAILURE`.

The reducer computes all raw family scans, Laurent fits, scalar calibrations, quadrature/conjugacy diagnostics and the aggregate `passed` boolean, then constructs the result object. However, it executes `assert passed,result` before printing the JSON. Because the workflow uses `set -euo pipefail` and redirects stdout to `iteration305_result.json`, any failed scientific threshold causes the process to exit before the diagnostic JSON is emitted; validator and upload steps are then skipped. Therefore the failed run cannot be promoted to a scientific/consistency FAIL and cannot identify which frozen threshold failed.

This is an operational/reproducibility failure, not evidence against Candidate Gravity. No triangle Laurent coefficient, IR pole, finite normalized cut, or combined `e=1,c=2` coefficient is authoritative from run `33702862824`.

An independent Iteration305 run `33702724483` remains active and is not duplicated.

Readiness change: 0 percentage points. Comparator foundation remains `24/25`, robust unique residual `0/20`; the audit prevents a false negative claim but closes no readiness rubric block.

Guardrail: fail-closed scientific execution must still preserve a schema-valid diagnostic artifact with `scientific_gate_pass=false`; only authority promotion should fail. Raw metrics must survive both PASS and BLOCKED outcomes.

Next gate: consume the independent active Iteration305 artifact if it completes. If it does not yield schema-valid diagnostics, repair the direct reducer so JSON is emitted/uploaded before a final nonzero scientific gate status, rerun exactly once, and preserve the first violated frozen threshold without relaxing it.
