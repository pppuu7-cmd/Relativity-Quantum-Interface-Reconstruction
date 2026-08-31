# RQIR Candidate Gravity — Iteration 197

**MODEL_READINESS: 24%**

## Goal
Complete the target-independent prospective v3 protocol after Iteration 196 showed structural rank but severe finite-noise conditioning.

## K2 design
The preregistered design searched only two global scales on the original six hard vectors: low in `{0.60,...,0.90}`, high in `{1.10,...,1.40}`, requiring `0.10<=x=q^2<=1.00`. The objective used only the supported hard comparator matrix `[x,...,x^6,x^2 exp(x)]` and minimized its column-normalized condition number, with raw condition number as tie-break. No candidate, soft2 or left-null information entered the design.

Selected scales: `0.80` and `1.40`.

Hard rank remains `7/7`. Raw condition number improves from v2 `2.0493466e7` to `6.3690956e6` (factor `3.2176`); column-normalized condition improves by factor `3.0705`; raw smallest singular value increases by factor `5.6670`.

Classification: conditioning improved but remains near-degenerate; this is not identifiability closure.

## Polarization freeze
Before any cubic comparator evaluation, a single geometry-only TT acceptance rule was frozen for all 12 v3 rows: `abs(hard raw TT norm)>=0.25`; partner polarization must keep constant sign and `min abs(raw norm)>=0.25` on 81 epsilon points in `[-0.01,0.01]`.

All 12 rows pass. Minimum partner margin is `0.8106158577`.

## Local C5 soft2 evaluation
Only after the geometry/polarization freeze, the exact leading cyclic `Riemann^3` soft2 coefficient was evaluated and the dimension-12 zero-K2 local basis formed as

`V4 = Riemann3_soft2 * {1,-x,x^2,-x^3}`.

Result:
- rank `4/12`;
- singular values `[6.1707923546,0.8674945113,0.1119400053,0.00594262129]`;
- condition number `1038.3957`;
- algebraic complement dimension `8` before blocked AS/C3 completion.

This preserves the structural local-C5 authority while moving the hard K2 block to a better-conditioned prospective protocol.

## Retained results
- `NUM-NG-011` — target-independent scale design improves supported hard K2 conditioning without candidate information.
- `PROTO-NG-005` — v3 polarization geometry frozen prospectively before cubic evaluation.
- `NUM-NG-012` — all 12 v3 rows pass geometric conditioning with minimum partner margin >0.81.
- `C5-NG-017` — v3 zero-K2 local dimension-12 curvature-cubic soft2 span remains rank 4.
- `REL-NG-012` — v3 leaves eight soft2 relation dimensions before blocked AS/C3 completion.
- `NG-FUNNEL-052` — conditioning design and polarization acceptance must both be frozen before cubic evaluation.

## Scope
AS remains `BLOCKED_AS_REALTIME_RELATION_COMPLETION`; C3 remains `BLOCKED_C3_CTP_ORDERED_COMPLETION`. These are not zero columns. No Candidate Gravity residual has been tested. `ANSATZ-003` is not created. Fisher/resources remain forbidden.
