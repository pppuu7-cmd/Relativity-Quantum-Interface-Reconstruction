# RQIR Candidate Gravity Recovery Delta — Iteration 306

Date: 2026-09-03

MODEL_READINESS: 24%

## Authority

Iteration 306 is authoritative only for the operational failure-observability audit of the failed direct Iteration305 triangle run. It does not supersede Iteration304 scientific cut authority and does not promote any Iteration305 triangle coefficient.

Freeze:

`FAIL_OPERATIONAL_ITERATION305_DIRECT_TRIANGLE_RUN_DROPS_SCIENTIFIC_DIAGNOSTICS_ON_THRESHOLD_FAILURE`

Failed execution provenance:

- run `33702862824`
- job `100485680662`
- head `11e593ea1ff3b3e49043e14fb4ee76c22fe1006d`
- reducer step: FAILURE
- validator step: SKIPPED
- upload step: SKIPPED

## Exact finding

The direct Iteration305 reducer computes raw epsilon scans, Laurent fits, scalar calibration, raised-triangle cancellation calibration, quadrature comparison, advanced/retarded conjugacy and a Boolean `passed`. It then builds a diagnostic result object but executes `assert passed,result` before printing JSON. The workflow redirects stdout to the scientific result file under `set -euo pipefail`.

Therefore any failed frozen threshold causes termination before the diagnostic JSON is preserved. This means the failed run cannot tell authority which scientific threshold failed and cannot be classified as a physics/consistency FAIL. It is an operational diagnostic-observability failure.

No triangle finite-cut coefficient, pole coefficient, or combined `e=1,c=2` cut may be imported from run `33702862824`.

## Independent active process

Run `33702724483` (`rqir-iteration305-timelike-tru1-visible-triangle-cut`) was still `in_progress` at this audit. Do not duplicate it.

## Guardrail

Fail-closed means no failed threshold may be promoted as PASS; it must not mean deleting the diagnostic evidence. Both PASS and scientific-BLOCKED paths must preserve a schema-valid artifact. The final job status may fail after upload if a frozen threshold is violated.

## Readiness

MODEL_READINESS: 24%

Change from previous assessment: `0 pp`. Comparator foundation remains `24/25`; robust unique residual remains `0/20`. This iteration protects scientific classification integrity but closes no rubric block.

## Exact next gate

Consume and schema-audit active run `33702724483` if it completes. If it fails without a usable artifact, repair the direct Iteration305 execution contract so diagnostic JSON is always emitted and uploaded before the final scientific gate exit; rerun once and classify the first actual violated frozen threshold without weakening any threshold.
