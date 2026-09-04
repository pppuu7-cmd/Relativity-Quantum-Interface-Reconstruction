# Candidate Gravity Recovery Delta — Iteration 391

Date: 2026-09-04

MODEL_READINESS: 24%

## Scope

Topology-only reclassification of the raw-preserved Iteration-388/384 U2 repeated-cut chunk indices 12-13. No physical integration was rerun. The exact Iteration-359 48-channel ordering and denominator-group topology were reconstructed and compared against the immutable raw Iteration-388 numerics.

## Raw Actions authority

- run: `33820559335`
- job: `100862111192`
- workflow head: `b88f0e22bdf26223e623ab6ebb6420c69fec04ac`
- code commit: `d828ef1f53c20f891c0816d9c405584cc0a68d94`
- artifact: `9918118094` (`iteration391-result`)
- artifact digest: `sha256:3e8ba2ff4f8b8696ff18e463d83b3e4686687fd6b7b27eaa70e0d9a8291743a4`
- raw result SHA-256: `ec9bced6138f631f6d426b69ec5f88cad22afe0e72623e0bac215176bf6bd839`
- source Iteration-388 raw Actions SHA-256: `5e7ab80c114f0c178adb4277cc65f161e7fa55a45d8e846c455042d14aa540dd`
- sentinel/authority audit: PASS.

## Result

`PASS_U2_CHUNK12_13_TOPOLOGY_AWARE_RECLASSIFICATION__BOTH_CONVERGED`

Index 12:
- q² = `-1`;
- denominator groups = 3;
- cut pair `[0,2]` leaves uncut group `[1]`;
- finite minimum uncut denominator `0.12097368457851282`;
- convergence error `3.9907266391548736e-10`;
- shell error `1.362778603343235e-16`;
- corrected status `CONVERGED`;
- `D_s TrU2 = -1.6409523141466878e-05`.

Index 13:
- q² = `-0.14`;
- denominator groups = exactly 2;
- cut pair `[0,1]` exhausts every denominator group;
- uncut group list is empty;
- therefore the raw `minimum_sampled_uncut_abs_denominator=+Infinity` is a correct empty-minimum sentinel, not a singularity;
- convergence error `4.824482827125998e-15`;
- shell error `9.042246118529107e-17`;
- corrected status `CONVERGED`;
- `D_s TrU2 = -0.0004977890941608628`.

The sole Iteration-384 defect was the wrapper requirement `isfinite(umin)`, which incorrectly rejected topologies with no uncut propagator. The physical Iteration-364 `channel_derivative`, grids, auxiliary-mass derivative, normalization and thresholds are unchanged.

## Consequence

Indices 12 and 13 may be merged as resolved CONVERGED records into the exact-48 U2 assembly. Iteration 390 applies the same topology-aware structural rule prospectively to the remaining failed/cancelled Iteration-384 chunks.

No effective-action weight is folded. No q² cross-summing. No Source/Born subtraction. No `ANSATZ-003`. No Fisher/resources.

MODEL_READINESS remains 24%.
