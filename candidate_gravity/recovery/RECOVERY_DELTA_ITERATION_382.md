# RQIR Candidate Gravity — Recovery Delta Iteration 382

**Date:** 2026-09-04  
**Status:** RAW-VALID SCIENTIFIC AUTHORITY FOR ONE PRESELECTED CHANNEL / RESOURCE AUTHORITY FOR NEXT ARCHITECTURE  
**MODEL_READINESS: 24%**

## Authority

Iteration 382 validates one prospectively fixed cut-through-double-pole `Tr U2` channel with the Iteration-364 `channel_derivative` arithmetic used verbatim. It is scientific authority for this one channel and resource/runtime authority for choosing a smaller complete-48 architecture. It is **not** authority for the other 47 channels.

Freeze:

`PASS_U2_REPEATED_CUT_ONE_CHANNEL_PILOT__CONVERGED`

Validated Actions provenance:

- run `33816704205`
- job `100850328336`
- workflow head `7fb92f2bd6488ccf7b7a4aaf141bd913ad2aa46a`
- artifact `9916963796`, `iteration382-result`
- artifact digest `sha256:e4ce19e00d8b58f78407c68974f9baa326d8777a4cb84af9ec58ac42fc0ee143`
- scientific JSON SHA-256 `5fddd09cc07224063434e2abeef1c8d0a044cfcf88ee85cb9e825bb69b005648`
- exactly one top-level JSON object, sentinel `382`, `scientific_authority_pass=true`.

## Frozen parent contract

Iteration 382 does **not** change the Iteration-364 physics arithmetic. It imports `channel_derivative` verbatim and keeps:

- Iterations 359/362/363 parent authority;
- the same repeated-pole auxiliary-mass derivative identity and sign;
- `BASE_H=5e-6`, `HALF_H=2.5e-6`;
- low grid `6x12`, high grid `8x16`;
- half-phi-step cross-check;
- convergence threshold `2e-5`;
- cut-shell threshold `2e-10`;
- the same routing, physical numerator and normalization;
- no effective-action `+i/2` weight folded.

## Scientific result

Frozen global channel index `0`:

- `q^2=-1`
- route `1`, subterm `1`
- cut group pair `(0,2)`
- repeated group `2`
- other cut group `0`
- algebraic cut sign `+1`
- `D_s Tr U2 = -1.1437983592303379e-05`
- half-step value `-1.1437983587686573e-05`
- shifted-phi value `-1.1438001667849296e-05`
- scaled convergence error `8.280353369982061e-10 < 2e-5`
- maximum cut-shell absolute error `1.6132928326584306e-16 < 2e-10`
- minimum sampled uncut denominator `0.12097568457851282`
- status `CONVERGED`.

Runtime: `341.30850966599996 s`.

## Resource conclusion

Iterations 364 and 376 remain **operational cancellations**, not scientific FAIL and not zero. Iteration 382 demonstrates that the frozen arithmetic is viable when one channel is isolated. A complete-48 run may therefore be prospectively decomposed into much smaller fixed chunks while preserving all physics and numerical thresholds. The value of channel 0 must never be extrapolated to the other 47 channels.

## Scope boundary

No effective-action `+i/2` weight is folded here. No Source/Born subtraction, matched `K2`, comparator quotient, ANSATZ-003, Fisher or resource claim is authorized.

## Readiness

`MODEL_READINESS: 24%`. Change: `0 pp`; this closes a one-channel physical/resource prerequisite but not a full readiness rubric bucket.

## Exact next gate

Freeze a complete 48-index architecture with small prospectively fixed chunks and identical Iteration-364 arithmetic. Require exact index coverage, no overlap/gap, per-channel sentinel/status, and preserve the three distinct `q^2` buckets. Any nonconverged channel remains `BLOCKED`, never zero-filled.
