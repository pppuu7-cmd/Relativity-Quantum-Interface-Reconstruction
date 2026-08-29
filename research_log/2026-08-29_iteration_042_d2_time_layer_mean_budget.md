# RQIR Research Log — Iteration 042

**Date:** 2026-08-29  
**Target:** convert the current centered D2 `gamma_mean` into a backaction-safe repetition/time budget using Iteration-041 operator compatibility.

## Scheduling model

The 14 force means split into seven commuting same-time dual-probe layers. Distinct phase layers use independent source preparations in the conservative strong-measurement branch.

For single accepted cycle row sensitivity `xi_mu`, each layer needs

`N_layer=gamma_mean/xi_mu^2`,

with current centered

`gamma_mean=1.830265e6`.

Parallel same-time dual-probe readout therefore needs `7 gamma_mean/xi_mu^2` accepted layer cycles; separate probe campaigns need twice that.

## Coherence-aware wall time

At 100 Hz, the seven stored phases require evolution times summing to

`0.0373396341 s`,

while the maximum layer requires

`7.94318794 ms`.

This gives **RQIR-RESOURCE-017 — phase-layer coherence accounting**: independent phase settings pay their own coherence/evolution time, so use `sum t_j`; do not use either `7*t_max` or one shared disturbance-free copy across noncommuting phases.

## 100-Hz benchmark

Ideal `p=1`, zero dead time, `xi_mu=1`:

- parallel dual-probe mean calibration: `18.9837 h`;
- sequential probes: `37.9675 h`;
- best4 covariance floor: `2.60416 h`.

Mean becomes no slower than covariance at

- `xi_mu>=2.69996` parallel;
- `xi_mu>=3.81832` sequential.

With `p=0.5`, `1 ms` dead/readout:

- covariance floor: `5.86402 h`;
- parallel mean at `xi=1`: `45.0852 h`;
- `xi=2`: `11.2713 h`;
- `xi=3`: `5.00946 h`;
- `xi=5`: `1.80341 h`;
- `xi=10`: `0.450852 h`.

Crossover: `xi_mu~2.77280` parallel or `3.92134` sequential.

## New design rule

**RQIR-CAL-015 — same-time dual-probe pairing:** the two probe-force observables at one phase commute and can be co-acquired in the present model; this is the maximal disturbance-free grouping of the 14 mean rows.

## Interpretation

The mean-resource target is now concrete: a future D2 apparatus model must deliver a per-accepted-layer row-standardized sensitivity of roughly `2.8` if mean calibration is to be no slower than the best4 covariance floor in the transparent 100-Hz benchmark. Physical SI transduction and readout integration are still open.

## Files

- `analysis/d2_time_layer_mean_budget_iteration042.py`
- `docs/D2_TIME_LAYER_MEAN_BUDGET.md`
- `recovery/RECOVERY_DELTA_ITERATION_042.md`

## Next gate

Build a minimal continuous weak-measurement/output model and quantify the information-backaction tradeoff needed to co-acquire mean and covariance information across noncommuting time layers.
