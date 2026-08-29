# RQIR Physical Fisher Resource Budget

**Date:** 2026-08-29  
**Iteration:** 012  
**Status:** detector/source resource accounting; not a hardware forecast or new-physics claim.

## 1. Purpose

Previous noisy-identifiability work introduced two abstract Fisher resources:

- `C_a`: independent nongravitational information on the amplitude of the deliberately hidden source-state direction;
- `gamma`: row-normalized information strength assigned to the ordinary gravitational NP3 calibration matrix.

This note converts those quantities into repetitions, standardized single-shot sensitivity, elapsed measurement time, and coherence-time requirements. It also identifies a limitation of the scalar-`gamma` model: a real NP3 calibration does not consist of statistically identical rows.

The current source/calibration baseline is Iteration 011, not the older Toy010 covariance geometry.

## 2. Current baseline

Accepted Iteration-011 calibration:

- second probe `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- normalized `s_min = 1.9995404e-3`;
- exact rank `24/25`.

The 24 abstract rows decompose as:

- 1 trace/normalization constraint;
- 1 mean-energy constraint;
- 14 potential-mean rows;
- 8 symmetrized covariance/noise rows.

Thus only 22 rows are gravitational mean/covariance measurements in the natural physical interpretation. Trace normalization and source energy belong to source characterization, not to the same gravitational detector-noise model.

## 3. Updated scalar-gamma diagnostic

Rebuilding the local D1 four-quadrature Fisher model on the current Iteration-011 baseline gives, with source-amplitude calibration effectively perfect:

| retained detector-limited `F_beta` | scalar `gamma` |
|---:|---:|
| 50% | `~2.83e4` |
| 80% | `~6.85e5` |
| 90% | `~1.58e6` |
| 95% | `~3.38e6` |

The 90% requirement is somewhat heavier than the older Toy010 value even though the current `s_min` is comparable. This is expected: `1/s_min^2` is only a conditioning proxy; exact profiled Fisher also depends on how the weak calibration singular vectors align with the detector nuisance tangent.

### RQIR-CAL-004 — conditioning is not a sufficient resource proxy

Two calibrations with similar or better `s_min` can require different finite-noise calibration information because the detector couples differently to their weak singular directions.

Therefore final experiment design must optimize the full covariance-profiled Fisher matrix, not `s_min` alone.

## 4. Generic physical mapping

Let the detector-only information for the nominal interface amplitude be

`S_D = rho_D^2`,

where `rho_D` is the matched detector SNR for `beta=1`.

For any independent calibration observable `i`, define its single-shot Fisher information

`I_i^(1)`.

After `N_i` independent repetitions,

`I_i = N_i I_i^(1)`.

If a mean-like Gaussian observable has derivative `dmu/dtheta` and single-shot rms noise `sigma`, define

`xi_i = |dmu/dtheta|/sigma`,

so

`I_i^(1)=xi_i^2`

and

`N_i = I_i/xi_i^2`.

For a zero-mean Gaussian variance/covariance channel with variance `V(theta)`, the single-sample variance Fisher is instead

`I_V^(1) = 0.5 (d ln V/dtheta)^2`.

This distinction matters: covariance rows cannot in general be assigned the same shot cost as mean rows.

## 5. Independent source-preparation budget

The null-amplitude obstruction gave, after normalizing to detector information,

`C_a/S_D = r/(1-r)`

for retained detector fraction `r` when orthogonal nuisances are perfectly calibrated.

For an illustrative detector target `rho_D=5`, hence `S_D=25`:

| retained fraction | required physical `C_a` |
|---:|---:|
| 80% | 100 |
| 90% | 225 |
| 95% | 475 |

For 90% retention,

`N_prep = 225/xi_prep^2`.

Examples:

- `xi_prep=0.1`: `N_prep=22500`;
- `xi_prep=1`: `N_prep=225`;
- `xi_prep=10`: only a few independent preparations are needed in the local idealized model.

This shows an important asymmetry: if nongravitational source tomography can be made strongly sensitive per shot, verifying the hidden-state amplitude need not dominate the total resource budget. The ordinary gravitational nuisance calibration can be much more expensive.

## 6. Scalar-gamma shot-equivalent benchmark

The current 90% scalar diagnostic is

`gamma_90 ~= 1.58e6`.

At detector SNR 5, the corresponding row-normalized Fisher weight is

`gamma_90 S_D ~= 3.95e7`

per abstract normalized row.

If we use the 22 physically gravitational mean/covariance rows only and, purely for orientation, assign all of them the same standardized single-shot sensitivity `xi`, then

`N_row ~= 3.95e7/xi^2`

and

`N_grav,total ~= 22 N_row`.

Illustrative values:

| `xi` | shots/row | total 22-row shots | total time at 1 ms/shot | total time at 10 ms/shot |
|---:|---:|---:|---:|---:|
| 1 | `3.95e7` | `8.70e8` | `~10.1 days` | `~100.7 days` |
| 10 | `3.95e5` | `8.70e6` | `~2.42 h` | `~24.2 h` |
| 100 | `3.95e3` | `8.70e4` | `~87 s` | `~14.5 min` |

These are **not forecasts**. They demonstrate that the abstract gamma requirement cannot be judged experimentally until real single-shot sensitivities are assigned to each row.

## 7. Why one scalar gamma is physically insufficient

The old model used

`F_C = gamma A_norm^T A_norm`.

A physical model should instead use

`F_C = A^T Sigma_C^{-1} A`

or, for independent repeated settings,

`F_C = sum_i N_i I_i^(1) a_i a_i^T`,

with separate resources for different row classes.

At minimum the next covariance model must distinguish:

1. source normalization / trace;
2. source mean-energy metrology;
3. gravitational potential means;
4. gravitational symmetrized covariance/noise estimates;
5. correlations between repeated measurements when source preparation drifts.

A single `gamma` can remain a diagnostic condition-number stress test but must not be reported as an experimental repetition count.

## 8. Coherence-time mapping

The stored source phases are dimensionless `tau=Omega t`, where `Omega` is the basic angular gap scale. Therefore

`t = tau/(2 pi f_gap)`.

The largest accepted Iteration-011 phase is about `4.99085`, giving a minimum coherent evolution span, before detector interaction/dead time,

`T_coh >= 0.7943/f_gap`.

Examples:

- `f_gap=1 Hz`: `T_coh >= 0.794 s`;
- `f_gap=100 Hz`: `T_coh >= 7.94 ms`;
- `f_gap=1 kHz`: `T_coh >= 0.794 ms`.

Crucially, if calibration is performed with repeated independent state preparations, the source need not remain coherent for the *total* multi-hour/day calibration campaign. It must remain coherent over each individual preparation-evolution-readout cycle. Total calibration time instead imposes requirements on preparation reproducibility and long-term drift control.

### RQIR-RESOURCE-001 — coherence and repetition are different resources

For repeatable-source protocols, total Fisher can accumulate across independent preparations while coherence is required only within each shot. Long integration therefore converts a coherence requirement into a preparation-stability/drift requirement rather than demanding one source state survive for the entire experiment.

## 9. Main negative result of this iteration

A naive statement such as “`gamma=1.6e6` means 1.6 million measurements” is false.

`gamma` is an information ratio in a row-normalized artificial covariance model. Physical repetition counts scale as

`N_i = gamma S_D / I_i^(1)`

only for a row to which that same normalized information model applies. Mean and covariance rows generally have different `I_i^(1)`, and trace/energy rows belong to different metrology layers.

This correction prevents a potentially large experimental-resource misinterpretation.

## 10. Next gate

Replace scalar gamma by an explicit heterogeneous calibration covariance:

- D1: phase-readout variance, contrast loss, dead time and timing/control noise;
- D2: thermal force, displacement imprecision and backaction PSD;
- source layer: explicit preparation/tomography observable and drift covariance;
- mean and symmetrized-noise rows: separate per-shot Fisher laws.

Then optimize total wall-clock cost subject to a target profiled `F_beta|theta` retention, rather than optimizing `S_eff`, `s_min`, or scalar gamma separately.

## Reproducibility

See `analysis/physical_resource_budget_iteration012.py`.
