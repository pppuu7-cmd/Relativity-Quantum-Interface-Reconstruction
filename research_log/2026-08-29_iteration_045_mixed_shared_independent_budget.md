# RQIR Research Log — Iteration 045

**Date:** 2026-08-29  
**Target:** convert the Iteration-044 response-preserving same-copy Fisher cap into an explicit mixed D2 calibration schedule.

## Result

At ideal reciprocal-linear quantum efficiency, preserving at least 90% of unperturbed raw detector signal Fisher gives

`xi_shared<=0.7239817`, `I_shared<=0.5241495` per normalized mean row per accepted science copy.

Across the `1.180254e6` best-four covariance/science trajectories, this can credit at most

`~6.18630e5`

mean Fisher per row against the centered target

`gamma_mean=1.830265e6`.

Thus only `~33.8%` of the current mean target can be shared under this optimistic criterion; at least `~66.2%` (`~1.21164e6` Fisher per row) remains for independent/sacrificial mean-calibration preparations.

This is **RQIR-RESOURCE-019 — response-preserving shared-credit cap**.

## 100-Hz transparent benchmark

With `p=0.5`, `1 ms` dead/readout and same-time dual-probe parallelization, the best4 covariance/science floor is `~5.864 h`.

Optimistic mixed totals:

- independent `xi=1`: `~35.71 h`;
- `xi=2`: `~13.33 h`;
- `xi=3`: `~9.18 h`;
- `xi=5`: `~7.06 h`;
- `xi=10`: `~6.16 h`.

Compared with covariance + fully independent mean campaigns, shared weak monitoring saves about `15.24, 3.81, 1.69, 0.61, 0.15 h` respectively.

The main conclusion is not that sharing is useless, but that it cannot replace the independent mean-calibration layer while preserving the current response target in the reciprocal linear class.

## Efficiency

The shareable fraction scales linearly with shared-monitor efficiency in this proxy: `~33.8%*eta`.

## Files

- `analysis/d2_mixed_shared_independent_budget_iteration045.py`
- `docs/D2_MIXED_SHARED_INDEPENDENT_BUDGET.md`
- `recovery/RECOVERY_DELTA_ITERATION_045.md`

## Next gate

Propagate the backaction channel through the full hard-constrained D2 detector/nuisance Jacobian and solve the actual profiled `F_beta|theta` condition. The raw-signal 33.8% shared-credit result is an optimistic upper bound.