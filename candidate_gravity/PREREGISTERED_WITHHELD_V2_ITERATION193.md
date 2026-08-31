# Candidate Gravity — Iteration 193: geometry-conditioned withheld v2

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**  
**Protocol:** `RQIR-WITHHELD-NULLSOFT-12-v2`

Following the v1 W05 numerical failure, a new protocol version is frozen before cubic comparator evaluation.

The twelve hard q-vectors are unchanged. Only polarization seed selection is repaired by one rule applied identically to every row:

- deterministic hard-seed stream starts at `193000+1000*row`;
- deterministic partner-seed stream starts at `193500+1000*row`;
- hard acceptance: `abs(raw TT norm)>=0.25`;
- partner acceptance: raw TT norm has constant sign and `min abs(norm)>=0.25` on an 81-point grid `epsilon in [-0.01,0.01]`;
- choose the first passing seed.

No comparator amplitude, left-null vector or candidate target enters the rule.

All twelve rows pass. The smallest partner margin is `0.6602965579`, well above the frozen `0.25` threshold.

Retain `PROTO-NG-003`, `NUM-NG-007`, `NG-FUNNEL-048`.

`MODEL_READINESS: 24%` — unchanged.
