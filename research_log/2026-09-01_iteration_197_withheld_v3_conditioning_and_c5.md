# RQIR Candidate Gravity Research Log — Iteration 197

Date: 2026-09-01

## Goal
Improve finite-noise conditioning of the structurally rank-7 supported hard-K2 comparator without using candidate information, then prospectively freeze cubic geometry and re-evaluate the local zero-K2 C5 soft2 basis.

## Results
The target-independent two-scale design over the frozen base hard vectors selects scales `0.80` and `1.40` within `0.10<=q^2<=1.00`.

Hard K2 block `[x,...,x^6,x^2 exp(x)]`:
- rank `7/7`;
- raw condition number `6.3690956e6` versus v2 `2.0493466e7`;
- raw conditioning improvement factor `3.2176`;
- column-normalized improvement factor `3.0705`;
- raw smallest singular value gain `5.6670`.

A single geometry-only polarization rule was then frozen before cubic evaluation. All 12 v3 rows pass; minimum partner TT norm margin is `0.8106158577`.

After that freeze, the exact leading cyclic Riemann3 soft2 coefficient gives local C5 basis `Riemann3_soft2*{1,-x,x^2,-x^3}` with rank `4/12`, singular values `[6.1707923546,0.8674945113,0.1119400053,0.00594262129]`, and condition number `1038.3957`.

## Classification
✅ Structural hard rank remains intact and hard conditioning improves prospectively.

✅ v3 cubic geometry is valid and frozen before comparator cubic evaluation.

✅ Local C5 zero-K2 soft2 authority remains rank 4 on v3.

🟡 Hard K2 remains near-degenerate operationally; no Fisher/finite-noise identifiability claim is allowed.

🟡 AS is `BLOCKED_AS_REALTIME_RELATION_COMPLETION`, not zero.

🟡 C3 is `BLOCKED_C3_CTP_ORDERED_COMPLETION`, not zero.

❌ Candidate residual not tested; `ANSATZ-003` not created.

`MODEL_READINESS: 24%`

Readiness unchanged from 24%: the comparator protocol is more robust, but the remaining comparator-foundation point is still blocked by AS/C3 authority and unique residual remains 0/20.

## Next gate
Freeze a finite-noise conditioning acceptance criterion for the supported hard-K2 calibration on v3 using comparator-only scaling/uncertainty assumptions, without running Fisher or candidate forecasts. If the present `cond~6.37e6` fails that preregistered criterion, redesign the hard-node domain prospectively; otherwise retain v3 and return to closing AS/C3 relation authority rather than generating candidate targets.
