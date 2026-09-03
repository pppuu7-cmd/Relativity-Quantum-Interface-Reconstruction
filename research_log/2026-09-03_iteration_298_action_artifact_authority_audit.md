# Research log — RQIR Candidate Gravity Iteration 298

**Date:** 2026-09-03  
**Entering authority:** Iteration 297  
**Scope:** authority audit of completed Iteration-296 direct-timelike `Tr U1` bubble DR Action.

## Result

The Iteration-296 workflow run `33693775575` completed with GitHub conclusion `success`, but its downloaded persisted result cannot be accepted as scientific authority.

`iteration296_result.json`:

- SHA-256: `99af1466a132d8c116b2ef5f8466fb67dbdd53e857e93a088ff53d4d577b3a7a`;
- bytes: `103185`;
- top-level JSON payloads after complete repeated decode: `3`;
- iteration sentinels: `[270, 273, 295]`;
- expected sentinel `296`: **absent**.

Hence:

`FAIL_OPERATIONAL_ITERATION296_ARTIFACT_MISSING_EXPECTED_FINAL_RESULT_SCHEMA`

The exact underlying Python termination cause is not inferred from this artifact. The authority decision does not require that inference: no expected final Iteration-296 result was persisted.

## Scientific meaning

This is operational/reproducibility FAIL only. It is not Candidate Gravity consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or a novelty statement. No Iteration-296 bubble DR numerical coefficient is promoted.

New guardrail:

`DO_NOT_ACCEPT_GREEN_ACTION_AS_SCIENTIFIC_PASS_WITHOUT_EXPECTED_ITERATION_SENTINEL_AND_SCHEMA_VALIDATION`

New operational blocker:

`BLOCKED_VALIDATED_TIMELIKE_TRU1_BUBBLE_DR_RESULT`

A fail-closed generic validator has been committed at `candidate_gravity/code/iteration298_validate_action_result.py`.

Iteration 297's independent evanescent/DR-continuation blocker remains unchanged and downstream of obtaining a valid result payload.

## Readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 297: **0 percentage points**. The audit blocks invalid evidence but does not close any model-readiness category.

## Next gate

Correct the bubble workflow so execution is fail-closed (`set -euo pipefail` or equivalent), the final JSON is written directly to a dedicated file, and a single expected-iteration sentinel is schema-validated before artifact upload. Only a validated rerun may enter scalar-calibration, retarded/advanced-conjugacy, epsilon-scan, Laurent-stability and discontinuity audits.

No ANSATZ-003. No Fisher/resources. No blind heavy full-C5 run.
