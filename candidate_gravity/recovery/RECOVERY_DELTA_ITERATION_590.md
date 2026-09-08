# Recovery Delta — Iteration 590

Date: 2026-09-08

## Authoritative change
Iteration 590 closes a cubic source-response completeness audit upstream of the planned nonlinear Ward cancellation.

Canonical raw authority:
- run `34210666988`
- head `ffa700d898545048e1df7a81d0f5297e6ea0c818`
- artifact `10049640731`
- artifact digest `sha256:804cbbaf1008a579c368001f4081d85b09c42f2504bdb19c0e6a959016a1e840`
- result SHA256 `5ba0e9fc88b68b13d08d406829ebf4cc30e8ae85d8d92816f282d105a89d4d63`
- authority audit SHA256 `6fa94126f8ed2a3680352a4c477afbfbe871bbc21a379631db350b102b2cbce0`
- audit classification `PASS_RAW_AUTHORITY_AUDIT_ITER590_CUBIC_COMPLETENESS`
- failures `[]`

Machine consumption authority:
`candidate_gravity/results/iteration590_source_cubic_completeness_raw_consumption.json`
commit `4221cac06347927d3d4cd8a5717194cd5178115f`.

## Operational repair history
Initial run `34210212105` failed before scientific authority because persisted Iter589 result bytes no longer matched their raw artifact SHA. Diagnostic run `34210405875`, artifact `10049528601`, identified the drift. Byte-identical Iter589 raw authority was restored in commit `7217a6d0bb7fc6349497fd4dcf7af3fdcccff772`. The Iter590 formula and thresholds were not changed.

## Scientific result
For `G=K^-1`, the exact third mixed response is

`d_abc G = -G Kabc G + sum_6(G Ki G Kjk G) - sum_6(G Ki G Kj G Kk G)`.

Therefore the six Iter588/589 K1/K2 placements are a scoped subset, not automatically the full cubic source response.

On the exact Iter368/Iter588 fixture, both omitted families have nonzero support:
- local mixed third contact K3 is nonzero for all three singleton roles;
- six-permutation K1^3 chain sum is nonzero for all three singleton roles.

Classification:
`PASS_CUBIC_SOURCE_RESPONSE_COMPLETENESS_AUDIT__K1K2_ONLY_IS_SCOPED_NOT_FULL`.

## Binding interpretation
Do NOT perform or promote a K1/K2-only nonlinear Ward cancellation as the complete source response yet.

Open origin accounting:
- `K3_under_hard_channel_D_s = OPEN__LOCAL_ANALYTIC_PROJECTION_TO_BE_PROVED`
- `K1cubed_under_frozen_linked_T_cut = OPEN__MUST_NOT_BE_DROPPED_BY_1PI_LABEL_WITHOUT_PROTOCOL_AUTHORITY`
- `K1K2_only_as_complete_source_response = NOT_AUTHORIZED_YET`

Iteration 183 remains binding: physical matching uses the full source-completed cubic response, and internal repartitions are not observables. Old Born-fixed subtraction results from other on-shell cut observables may not be imported into this off-shell source response.

## Next permitted gate
First prove the hard-channel discontinuity status of the local K3 contact from the same MSSC-001 parent. Then independently classify K1^3 under the frozen linked `Y=(K2,S_soft2_full)` / `T_cut` protocol. Only after both are closed may the K1/K2 Ward block be called complete at the discontinuity level.

MODEL_READINESS stays 24%. `ANSATZ-003` and Fisher/resources remain forbidden. Source/Born subtraction remains not performed.
