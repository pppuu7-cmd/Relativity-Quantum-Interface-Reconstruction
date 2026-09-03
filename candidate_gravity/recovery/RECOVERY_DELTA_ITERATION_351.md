# Recovery Delta — Candidate Gravity Iteration 351

Date: 2026-09-03

## Scope

Rebuild the matched-timelike cubic U2 route census from all 30 raw Iteration-308 placements after Iteration 350 proved that the old singleton-soft `A1=0` pruning is not valid on the timelike fixture. This gate classifies exact structural zeros from the physical Iteration-348 A1/A2 provider only; it does not yet claim nonzero traced route products.

## Raw Actions authority

- run: `33782839444`
- job: `100740425386`
- artifact: `9904248985` (`iteration351-result`)
- artifact digest: `sha256:389c52fd492b74dd780d9c232ab6da0277624d35e94b6ba01d679e627967357b`
- scientific JSON SHA-256: `49f31685fc4c0b3e2b8ac5ca4e39cfb31a6cf241a85c958528d8ba272317c247`
- workflow head: `d8482cd0290d3955aaeb45b61fc4bfdc31443318`

Raw artifact and audit were inspected independently of workflow conclusion.

## Result

All six physical A components needed by the raw cubic placements are nonzero on the matched timelike fixture. Consequently:

- raw placements: `30`;
- structurally alive from exact physical A components: `30`;
- structurally killed by exact A zero: `0`.

Authority:

`PASS_U2_MATCHED_TIMELIKE_30_RAW_ROUTE_STRUCTURAL_CENSUS_WITH_PHYSICAL_A_COMPONENTS__FULL_PHYSICAL_ROUTE_PRODUCTS_NEXT`.

This does not establish that every full route trace is nonzero; only that no route may be discarded structurally using the former null-soft A1 zero.

## Next gate

Evaluate full physical matrix products and traces for all 30 routes with Iteration-348 A1/A2, Iteration-349 N/Y/Hinv, exact shifted incoming momentum, Iteration-345 functional transpose and `Hinv_VD=-K^-1`. Then canonicalize numerator/denominator families before any cut integration.

Iteration 352 has been launched for the full physical route-product gate.

MODEL_READINESS: 24%

Change from Iteration 350: `0 pp`.
