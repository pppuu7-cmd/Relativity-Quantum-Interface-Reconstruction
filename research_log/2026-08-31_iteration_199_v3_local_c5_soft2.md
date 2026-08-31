# RQIR Candidate Gravity Research Log — Iteration 199

Date: 2026-08-31

## Goal

Evaluate the zero-K2 local C5 soft2 basis on the prospectively frozen v3 cubic geometry and compare its conditioning with v2.

## Result

v3 local C5 soft2 basis remains rank `4/12`.

- raw condition number: `4837.9565`;
- column-normalized condition number: `4587.3371`;
- complement dimension before AS/C3 completion: `8`.

Compared with v2, v3 soft2 conditioning is worse by factors `4.8399` raw and `8.1797` after column normalization, even though v3 hard K2 conditioning is better by factors about `3.22` raw and `3.07` column-normalized.

This establishes a hard-vs-soft conditioning tradeoff. v3 is not globally superior to v2.

## Status

✅ v3 hard K2: rank 7 and better conditioned than v2.

✅ v3 cubic geometry: prospectively frozen.

✅ v3 local C5 soft2: rank 4.

🟡 joint protocol design: tradeoff unresolved; requires multi-objective criterion.

🟡 AS/C3: BLOCKED, not zero.

❌ Candidate residual: not tested.

❌ `ANSATZ-003`: not created.

`MODEL_READINESS: 24%`

Readiness unchanged.

## Next gate

Freeze a target-independent multi-objective conditioning criterion for the full supported joint quotient and use it to compare/design prospective row sets. Do not use a candidate residual in the objective.
