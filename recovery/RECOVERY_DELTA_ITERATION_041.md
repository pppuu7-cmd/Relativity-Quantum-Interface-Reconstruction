# RQIR Recovery Delta — Iteration 041

**Date:** 2026-08-29

## New retained results

- **RQIR-NG-019 — non-QND shared-trajectory obstruction:** the 14 current D2 force-mean source operators cannot be treated as one disturbance-free multitime measurement. Of 91 pairs, only 7 commute; these are exactly the same-time dual-probe pairs. All 84 distinct-time pairs are noncommuting.
- `||[G0,H]||_F/||G0||_F ~=1.9056406`, `||[G1,H]||_F/||G1||_F ~=1.0586202`; the force observables are not QND under the Toy009 Hamiltonian.
- Best4 covariance rows `(0,1,3,7)` use six unique endpoints over four time layers; 13 of their 15 endpoint pairs are noncommuting.
- **RQIR-RESOURCE-016 — shared-Fisher credit rule:** reuse one accepted cycle across mean/covariance/control budgets only when one physical likelihood generates all score vectors and cross-Fisher including backaction/correlations.

## Optimistic shared-cycle requirements

If the Iteration-040 best4 covariance floor `N>1.180254e6` trajectories also supplied all current centered D2 mean/control information, required per-cycle standardized information would be:

- mean row: `I~1.550738`, `xi~1.245286`;
- timing: `I~0.0254117`, `xi~0.159410`;
- mean-offset reference: `I~155.07372`, `xi~12.45286`;
- covariance-offset reference: `I~49.99992`, `xi~7.07106`.

These are lower-bound targets only; no physical detector has yet been shown to achieve them jointly.

## Next

Use seven independent same-time dual-probe layers as the backaction-safe mean-calibration baseline, then compare against an explicit weak/continuous measurement model.
