# Candidate Gravity Recovery Delta — Iteration 405

Date: 2026-09-04

MODEL_READINESS: 24%

## Authority

Iteration 405 is now raw-validated scientific authority.

Freeze:

`PASS_U2_REPEATED_CUT_EXACT48_FAIL_CLOSED_ASSEMBLY`

Workflow run `33832181526` completed successfully. Raw artifact `9922054102`, digest `sha256:1dd9bbc6c863954059263171c5a160510ce3605bb416a46498c3453b48343729`, contains nonempty `iteration405_result.json`, `python_exit_code.txt=0`, and `iteration405_authority_audit.json` with `scientific_authority_pass=true`. Result SHA-256 frozen by the authority audit: `f766c6641fb9a89838784ae7572fa1f8459dd0260fd71007f8de93e727840cab`.

The fail-closed checks prove exactly 48 unique records, indices `0..47` once each, all CONVERGED, with 16 channels in each q2 bucket and the Iteration-392 topology-mask policy binding.

## Exact repeated-cut Tr U2 operator coordinate

- `q^2=-1`: `D_s TrU2_repeated_cut = +0.0006026660521292439`;
- `q^2=-0.34`: `D_s TrU2_repeated_cut = -0.0006500414994361118`;
- `q^2=-0.14`: `D_s TrU2_repeated_cut = -0.0015019714311265522`.

These raw exact-48 values supersede the earlier diagnostic 44+4 arithmetic quoted before the assembly artifact existed. The discrepancy is treated as a provenance correction, not a physics FAIL: only the raw fail-closed Iteration-405 assembly is authority.

No `+i/2` effective-action weight is folded here. Distinct q2 coordinates are not summed.

## Parallel Tr U1^2 state

Iteration 399 raw authority closes channel 5 / class 8 / `q^2=-0.14` as CONVERGED at `0.000119747535002548`. The exact remaining double-double blockers are `[2,4,11]`, all `BLOCKED_CONVERGENCE`; none may enter a q2 sum. Iteration 401 analytic-azimuth structure oracle remains independent and must not be duplicated.

## Readiness

MODEL_READINESS: 24%

Change: `0 pp`. A complete repeated-cut Tr U2 sector is now closed, but robust unique residual, parent ansatz, consistency/Ward closure, Fisher and experiment/resource buckets remain open.

## Exact next gate

Assemble complete `Tr U2` q2-by-q2 from Iteration 361 ordinary-simple zero + Iteration 366 repeated-family simple-simple + this exact Iteration-405 repeated-cut vector, still without `+i/2`.
