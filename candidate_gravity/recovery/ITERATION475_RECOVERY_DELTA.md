# Iteration 475 Recovery Delta

Date: 2026-09-05

## Authority retained
Physical/operator authority remains Iteration 411. Physical blocker authority remains Iteration 421 (`BLOCKED_CONVERGENCE`), exact unresolved physical set `[2]`. MODEL_READINESS remains 24%.

## New raw numerical authority
Canonical rank-9 run `33983416847`, job `101352576616`, artifact `9975782294`, artifact digest `sha256:a0e4d481dd4b34addf7a11316730dee3240e7843f12b586307f40608c08e15c5`, scientific JSON SHA-256 `533e5ab27c3631c25023e30ee70fecdb3bd845c18015cc6cf277ea42fd3ea8d8`.

At `u=+5e-6`, `v=-5e-6`, multiplicity 2: `80/80` finite; max scaled MP80↔MP120 `2.91451824771117558020302499753e-80 <= 1e-30`; max radial Richardson scaled error `2.55741734246055448980134948906e-15 <= 5e-4`. Classification `PASS_NEXT_MASS_NODE_FULL_Z_MP80_MP120__NON_PROMOTING`.

Certified occurrence-weighted precision coverage is now `15/32 = 46.875%`, i.e. `1200/2560` row occurrences. No physical promotion follows.

## Frozen-manifest correction
Iteration-455 distinct rank 10 `(+5e-6,+5e-6)`, multiplicity 2, is explicitly `CERTIFIED` in the frozen source-order manifest and was part of the initial certified baseline. It must not be recomputed as a new heavy gate. The stale prospective wording that rank-9 PASS permits rank 10 is superseded by the frozen manifest state.

The exact next untested coordinate is distinct rank 11: `u=+5e-6`, `v=+1e-5`, multiplicity 1. Launch only that coordinate under unchanged frozen conventions; raw-consume fail-closed.

`ANSATZ-003` remains uncreated. Comparator-subtracted residual and Fisher/resources remain BLOCKED.

MODEL_READINESS: 24%

Readiness change: 0 percentage points.
