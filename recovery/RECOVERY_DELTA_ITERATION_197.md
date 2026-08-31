# Recovery Delta — RQIR Candidate Gravity Iteration 197

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Authoritative result
Iteration 197 completes the prospective protocol `RQIR-WITHHELD-NULLSOFT-12-v3`.

The K2 design uses only the supported comparator family `[x,...,x^6,x^2 exp(x)]`, with global scales selected from preregistered grids and no candidate, soft2 or left-null information. Selected scales are `0.80` and `1.40`.

Hard K2:
- rank `7/7`;
- raw condition `6.3690956e6` versus v2 `2.0493466e7`;
- raw conditioning improvement factor `3.2176`;
- column-normalized improvement factor `3.0705`;
- raw smallest singular value gain `5.6670`.

A single geometry-only TT polarization acceptance rule was then frozen before cubic evaluation. All 12 v3 rows pass; minimum partner margin is `0.8106158577`.

Only after that freeze, the exact leading cyclic `Riemann^3` soft2 coefficient was evaluated. The local zero-K2 C5 basis

`V4 = Riemann3_soft2 * {1,-x,x^2,-x^3}`

remains rank `4/12`, with singular values `[6.1707923546,0.8674945113,0.1119400053,0.00594262129]` and condition number `1038.3957`.

## Classification
- hard conditioning: `IMPROVED_BUT_STILL_NEAR_DEGENERATE`;
- local C5 soft2: rank 4, supported comparator authority;
- AS: `BLOCKED_AS_REALTIME_RELATION_COMPLETION`, not zero;
- C3: `BLOCKED_C3_CTP_ORDERED_COMPLETION`, not zero;
- candidate residual: not tested;
- `ANSATZ-003`: NOT CREATED;
- Fisher/resources: FORBIDDEN.

## Retained results
`NUM-NG-011`, `PROTO-NG-005`, `NUM-NG-012`, `C5-NG-017`, `REL-NG-012`, `NG-FUNNEL-052`.

## Readiness
`MODEL_READINESS: 24%`

Unchanged from Iteration 196. Comparator protocol robustness improved, but AS/C3 still block the final comparator-foundation point and unique residual remains `0/20`.

## Authority files
- `analysis/withheld_v3_k2_conditioning_design_iteration197.py`
- `results/withheld_v3_k2_conditioning_design_iteration197.json`
- `analysis/withheld_v3_polarization_freeze_iteration197.py`
- `results/withheld_v3_polarization_freeze_iteration197.json`
- `analysis/withheld_v3_local_c5_soft2_iteration197.py`
- `results/withheld_v3_local_c5_soft2_iteration197.json`
- `candidate_gravity/WITHHELD_V3_CONDITIONING_AND_C5_ITERATION197.md`
- `research_log/2026-09-01_iteration_197_withheld_v3_conditioning_and_c5.md`

## Next gate
Freeze a comparator-only finite-noise conditioning acceptance criterion for v3 hard-K2 calibration. This is a conditioning gate, not Fisher. If v3 fails, redesign nodes prospectively without candidate information. If it passes, retain v3 and return to AS/C3 authority closure.
