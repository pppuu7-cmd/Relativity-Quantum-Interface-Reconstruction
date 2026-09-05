# Recovery Delta — Iteration 450

**Date:** 2026-09-05  
**Authority type:** raw consumption of the collision-safe post-449 same-corner remaining-z MP stage; one-mass-node full-training-z numerical precision closure; non-promoting.

## Source of truth consumed

- run `33932061794`
- job `101212520875`
- artifact `9959560285` (`rqir-post449-same-corner-remaining-z-mp`)
- artifact digest `sha256:84509a60d16e660e52c7873261694249e1167f1d95d6a34bd5e91e4026199c54`
- scientific `result.json` SHA-256 `2467e807b8b5f1c8a93a83a1e5be2107d2c5ae3d8747bb2f5f586b16501d1c03`
- raw classification `PASS_SAME_CORNER_FULL_Z_SUPPORT_MP80_MP120__NON_PROMOTING`

The workflow conclusion was not used as scientific authority. The downloaded raw payload and authority audit were independently checked.

## Raw observations

Frozen mass node: `u=v=+5e-6`. Newly consumed z support: `{-0.43,+0.43}`. All 16 frozen phi nodes and radial Richardson nodes `{2e-3,1e-3,5e-4}` with both signs were evaluated by direct parent recomputation at 80 and 120 decimal digits.

- `32/32` newly evaluated output rows finite.
- max scaled 80↔120 discrepancy: `2.78393261527753298550080747733e-80 <= 1e-30`.
- max radial Richardson scaled error: `1.96385912050971757112266495724e-15`, below the unchanged inherited limit.

Combined with raw-consumed Iteration 449 z=`{-0.86,0,+0.86}`, all five frozen Iteration-407 training-z values `{-0.86,-0.43,0,+0.43,+0.86}` are now numerically precision-closed at this one mass coordinate. Under the already-frozen Iteration-449 denominator convention this is `80/2560 = 3.125%` of sample-generation provenance support. This percentage is not MODEL_READINESS and is not physical closure.

## Authority

No physical coordinate is promoted. Physical/operator authority remains Iteration 411. Physical blocker authority remains Iteration 421 with unresolved set `[2]`. Iteration 412 exact15, full `Tr U1^2`, full `D_s Gamma_{e=2}`, comparator-subtracted residual, ANSATZ-003 and Fisher/resources remain BLOCKED.

## Exact next gate

Retained Iteration-407 source uses `derivative_from_analytic(h)` with source-order nodes `[-2h,-h,+h,+2h]` on each axis; Iteration 379 fixes `BASE_H=5e-6`, `HALF_H=2.5e-6`. The first untested mass coordinate in the base-stencil source order is therefore `u=v=-1e-5`.

The next bounded, non-promoting gate is frozen to:
- index 2 / class 3 / `q^2=-1`;
- mass `u=v=-1e-5` only;
- all five training z values `{-0.86,-0.43,0,+0.43,+0.86}`;
- NPHI16;
- radial `{2e-3,1e-3,5e-4}`, both signs;
- direct parent recomputation at 80/120 digits;
- cross-precision `<=1e-30`;
- unchanged inherited radial threshold;
- exact row census `80` and all finite.

No threshold weakening, smaller physical mass step, angular escalation, binary-parent recast, zero fill or physical promotion is allowed.

**MODEL_READINESS: 24%**

Readiness change: 0 percentage points.
