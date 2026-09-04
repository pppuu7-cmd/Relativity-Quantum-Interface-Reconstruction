# RECOVERY DELTA — ITERATION 436

**Status:** raw-consumed PASS; parent-precision closure, non-promoting.  
**Classification:** `PASS_ITER270_N1_80_120_DIGIT_CLOSURE__LEGACY_REPRODUCED__NON_PROMOTING`  
**MODEL_READINESS:** 24% (unchanged).

## Raw provenance

Run `33900713097`, job `101113864821`, artifact `9947511772`, artifact digest `sha256:3ebddf912b2e662dc884980c9b2578b1452ee5888dbdf3533307fe80ba76d8ad`; raw scientific JSON SHA-256 `154ab6654784f44967a43c5d84bc008544ce02260253724c0b9edd28aaeec5a2`.

## Frozen scientific object

The authoritative Iteration 436 object is the complete Iteration-270 parent chain

`geometry -> nhat -> y_down -> norb -> N1`

for `M=POS`, legs `s/a/b`, `P0=[0.7,-0.4,0.5,0.9]`, and the unchanged symmetric amplitude derivative step `h=3e-5`.

## Frozen acceptance and observed result

The contract was committed before the workflow result:

- required precision levels: 80 and 120 decimal digits;
- `max_scaled_abs[N1_80-N1_120] <= 1e-40`;
- every `norb(+h/-h)` binary64 endpoint had to reproduce the 120-digit port within `1e-12` scaled;
- all values finite;
- legacy `N1_binary64` vs `N1_120` classified against the unchanged `2e-5` physical reference tolerance.

Observed:

- max `N1_80` vs `N1_120` scaled discrepancy = `8.3327272424668097e-77`;
- max binary64 vs 120-digit `norb` endpoint discrepancy = `4.1643458019829987e-16`;
- max binary64 vs 120-digit `N1` discrepancy = `6.088515466627416e-12`;
- all values finite;
- legacy N1 is reproduced within `2e-5` by a margin of roughly `3.3e6`.

Per leg, binary64-vs-120-digit N1 scaled discrepancy is:

- `s`: `6.088515466627416e-12`;
- `a`: `4.596099727609572e-12`;
- `b`: `5.02312511827027e-12`.

## Scientific interpretation

Iteration 435 correctly identified severe cancellation amplification in selected raw components, especially the `s` leg, but Iteration 436 shows that this conditioning does **not** produce a material N1 numerical error at the frozen representative inputs. The complete N1 implementation is internally closed at 80/120 digits and the current binary64 N1 agrees far inside the unchanged physical reference tolerance.

This narrows the remaining precision diagnosis downstream. N1 is now certified only at this frozen scope; no physical `D_s` is promoted and Iteration 421 remains `BLOCKED_CONVERGENCE`.

## Exact next gate

Freeze and execute a separate `Q1=-Q0(p+k)@N1@Q0(p)` 80/120-digit closure using the certified N1 implementation and exact frozen Q1 momenta. `Q1` must independently certify its shifted `Q0` factors before any `Asub/Acoef/A_finite` closure.

## Guardrails

No change to `h`, momenta, polarizations, parent dynamics, routing, sign or normalization. No physical `D_s` promotion, no zero fill, no threshold weakening, no `ANSATZ003`, and no Fisher/resource claims.
