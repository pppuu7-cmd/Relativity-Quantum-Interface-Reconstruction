# RQIR Candidate Gravity Research Log — Iteration 197

Date: 2026-08-31

## Goal

Improve numerical conditioning of the already-proven rank-7 hard K2 comparator block without using any candidate information.

## Design

Deterministic scale grid on the same six base q-vectors:

- low scales `0.60..0.90` in steps of `0.05`;
- high scales `1.10..1.40` in steps of `0.05`;
- internal hard window `0.10 <= q^2 <= 1.00`;
- objective: minimum column-normalized condition number of `[x,...,x^6,x^2 exp(x)]`;
- tie-break: minimum raw condition number.

No candidate residual, soft2 amplitude or left-null used.

## Result

Best valid pair: `0.80 / 1.40`.

Selected q^2 range: `[0.184448,0.994896]`.

All partner legs remain spacelike on the frozen `epsilon in [-0.01,0.01]` grid, with partner q^2 range approximately `[0.179488,0.997136]`.

Compared with withheld-v2:

- raw condition improves from `2.04935e7` to `6.36910e6` (factor `3.2176`);
- column-normalized condition improves from `2.38767e7` to `7.77614e6` (factor `3.0705`);
- raw smallest singular value increases from `1.39038e-7` to `7.87933e-7` (factor `5.6670`).

Rank remains 7, as already guaranteed structurally by Iteration 196.

## Status

✅ v3 K2 geometry frozen before cubic/candidate evaluation.

✅ Conditioning materially improved.

🟡 Near-degeneracy remains; finite-noise identifiability not claimed.

🟡 v3 cubic polarization geometry: not yet frozen.

🟡 AS/C3: BLOCKED, not zero.

❌ Candidate residual: not tested.

❌ `ANSATZ-003`: not created.

`MODEL_READINESS: 24%`

Readiness unchanged: this is conditioning/protocol progress, not closure of a rubric component.

## Next gate

Freeze v3 polarization geometry by a uniform target-independent seed acceptance rule before any cubic C5/nonlocal evaluation on v3.
