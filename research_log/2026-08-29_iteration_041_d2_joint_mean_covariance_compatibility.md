# RQIR Research Log — Iteration 041

**Date:** 2026-08-29  
**Target:** test whether one D2 trajectory can legitimately be credited with the 14 force-mean rows and best-four covariance information without an explicit backaction model.

## Confirmed operator structure

The current 14 force-mean operators are `G_k(t_j)` for two probes and seven stored phase settings.

Pairwise commutator audit:

- 91 total operator pairs;
- 7 commuting pairs;
- 84 noncommuting pairs.

The only commuting pairs are the same-time two-probe observables `G0(t_j), G1(t_j)`. Every distinct-time pair is noncommuting.

The force observables are also non-QND with respect to the source Hamiltonian:

- `||[G0,H]||/||G0|| ~= 1.9056406`;
- `||[G1,H]||/||G1|| ~= 1.0586202`.

This establishes **RQIR-NG-019 — non-QND shared-trajectory obstruction**: a classical multitime record cannot be credited as a disturbance-free simultaneous measurement of all source force observables without a declared weak/continuous/ancilla measurement dynamics including backaction.

## Best-four covariance endpoints

Rows `(0,1,3,7)` use six unique endpoints over four distinct time layers. Of the 15 endpoint pairs, only two same-time pairs commute; 13 cross-time pairs do not.

Thus the covariance graph itself probes noncommuting temporal source information.

## Optimistic shared-cycle budget

Using Iteration-040 best-four covariance floor `N_cov>1.180254e6` accepted trajectories, if those same trajectories could also supply all current centered D2 mean/control Fisher, the average per-cycle requirements would be:

- normalized mean row: `I~1.550738`, standardized sensitivity `~1.245286`;
- timing `delta tau`: `I~0.0254117`, sensitivity `~0.159410`;
- common mean-offset reference: `I~155.07372`, sensitivity `~12.45286`;
- common covariance-offset reference: `I~49.99992`, sensitivity `~7.07106`.

The mean requirement is moderate; the additive-reference requirements are not. These are optimistic lower-bound requirements because cross-information/backaction is ignored.

## New retained resource rule

**RQIR-RESOURCE-016 — shared-Fisher credit rule:** one trajectory can be reused across mean/covariance/control resource budgets only if one physical likelihood generates all score vectors and their cross-Fisher, including backaction and detector correlations.

## Files

- `analysis/d2_joint_mean_covariance_compatibility_iteration041.py`
- `docs/D2_JOINT_MEAN_COVARIANCE_COMPATIBILITY.md`
- `recovery/RECOVERY_DELTA_ITERATION_041.md`

## Next gate

Build an independent-preparation seven-time-layer D2 mean calibration budget as a backaction-safe baseline, then compare it against an explicit continuous weak-measurement trajectory model rather than assuming free multitime Fisher reuse.
