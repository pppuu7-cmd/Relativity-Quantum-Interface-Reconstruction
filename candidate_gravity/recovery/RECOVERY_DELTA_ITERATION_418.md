# Recovery Delta — Iteration 418

**Date:** 2026-09-04  
**MODEL_READINESS:** 24%  
**Latest physical/operator authority:** Iteration 411  
**Latest structural authority:** Iteration 410  
**Latest numerical-method diagnosis:** Iteration 415  

## Raw-consumed Iteration 413

Iteration 413 run `33861440653`, job `100986560018`, head/workflow commit `a8ecf715f49ca9a45fde149087359924ec856b36` completed successfully operationally. Scientific authority was determined from the raw artifact, not workflow colour.

Artifact `9934109783` (`iteration413-physical-index-2`), digest `sha256:a7166a6a9c52cee4b7f66550027e8cd0adf04627f43774c22a5fc2c215913887`; raw `iteration413_result.json` SHA-256 `9195de1f24c65bc85458a9bf5bd0f6173ca8b07011cb46f4ad81e5d3e087eef8`.

Target identity is double-double global index 2 / class 3 / `q^2=-1`. The frozen analytic/spectral structural and direct-integrand checks remain valid, but the physical auxiliary-mass derivative is `BLOCKED_CONVERGENCE`:

- previous Iteration-411 pair discrepancy: `5.0042074065288766e-05`;
- Iteration-413 refined pair discrepancy: `2.769196909034482e-04`;
- unchanged physical threshold: `2e-05`;
- diagnostic `D_s TrU1^2` at the Iteration-413 coarse member: `+0.003621190924267374` — NOT authority and NOT inserted into any sum;
- direct original-integrand cross-check remains approximately `2.06564e-09 < 2e-06`.

Thus the prospectively frozen Iteration-414 `O(h^4)` truncation prediction is falsified. The discrepancy grew rather than shrinking by approximately 16. Index 2 remains the sole physical double-double blocker. No zero fill, threshold weakening, or angular-grid escalation is permitted.

## Iteration 415 diagnosis

Repository result `candidate_gravity/results/iteration415_tru1sq_channel2_massstep_convergence_diagnosis.json`, commit `e5c43052b3ea869ea96aee21ee8f298ffd8ec18d`, classifies the observed behavior as `PASS_TRU1SQ_CHANNEL2_CONVERGENCE_DIAGNOSIS__ROUND_OFF_OR_CANCELLATION_SUSPECTED` with diagnostic-only authority. It records discrepancy ratio `5.533737154423608`, observed order `-2.4682571634198707`, expected `O(h^4)` ratio `0.0625`, and leaves physical index 2 BLOCKED.

## Iterations 416/417 operational note

The independent null-soft current re-audit workflows 416 and 417 ended workflow `failure`, but their science steps completed before the raw JSON audit failed with `JSONDecodeError: Extra data`. This is an output-wrapper/audit failure, not a scientific FAIL, and neither run reopens or supersedes existing operator authority. They are not the index-2 closure path.

## Anti-idle continuation — Iteration 418

With `queued=0` and `in_progress=0` after raw-consuming Iteration 413, the next scientifically allowed non-duplicate step was launched:

- code: `candidate_gravity/code/iteration418_tru1sq_channel2_mass_derivative_cancellation_audit.py`;
- code commit: `fe838c863d2f718a83a9ef7dabd26cbfcb71f2e5`;
- workflow: `.github/workflows/rqir-iteration418-tru1sq-channel2-mass-derivative-cancellation-audit.yml`;
- workflow/head commit: `33c839fb25daf1d51fd9375846d3bc3361b78c32`;
- run: `33866891471`.

Iteration 418 is diagnostic-only. It does not introduce a smaller `h`; it re-audits only the already-used `h={5e-6,2.5e-6,1.25e-6}` values, decomposes the frozen central4×central4 mixed derivative into its 16 weighted contributions, measures cancellation condition numbers, compares naive and compensated sums, and estimates binary64 roundoff amplification. The Iteration-407 analytic sphere representation, target identity, normalization/sign, structural checks, physical threshold `2e-5`, no-zero-fill rule and downstream guardrails remain frozen.

A PASS from Iteration 418 cannot by itself promote a physical coordinate. Its role is to decide whether the next representation must eliminate finite-difference cancellation through an algebraically equivalent analytic/high-precision auxiliary-mass mixed derivative. Index 2 remains BLOCKED until such a representation is independently stability-validated and cross-checked against the original integrand.

## Downstream state

Iteration 412 exact15 assembly remains fail-closed. Complete `Tr U1^2`, full `D_s Gamma_{e=2}`, comparator-subtracted residual, ANSATZ-003, Fisher/resources and Source/Born subtraction remain blocked.

`MODEL_READINESS: 24%`
