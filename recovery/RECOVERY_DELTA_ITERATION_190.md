# Recovery Delta — RQIR Iteration 190

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## New frozen protocol

`RQIR-WITHHELD-NULLSOFT-12-v1` adds twelve prospective rows generated only by scaling each of the six baseline hard vectors by `0.75` and `1.25`.

No candidate, target residual, or left-null weight was used.

- hard `q²` range: `[0.1621125,0.793125]`;
- partner `r²` over all soft steps: `[0.1574625,0.793]`;
- all hard legs remain spacelike;
- polarization seeds and soft steps are frozen in `results/preregistered_withheld_row_extension_iteration190.json`.

## Mandatory order

Comparator columns must be computed on these rows before any candidate is tested. Rows may not be retuned after seeing the comparator or candidate outcome.

Retain `PROTO-NG-001`, `NUM-NG-005`, `NG-FUNNEL-045`.
