# RQIR Iteration 018 — Reference-Channel and Wall-Clock Resource Budget

**Date:** 2026-08-29  
**Status:** physical-resource translation on the corrected Iteration-015/016 basis.  
**Scope:** Toy009 + Iteration-011 balanced calibration; not a hardware forecast and not a new-physics claim.

## 1. Purpose

Iterations 015–017 corrected the nuisance Fisher calculation, derived first-order timing/additive control priors, and showed that common gain enters primarily through a gain×state product. This iteration translates those requirements into explicit reference-channel resources and introduces wall-clock Fisher rate as the next design objective.

The central distinction is now:

- information per accepted shot;
- coherent evolution time per shot;
- dead/reset time per shot;
- preparation success probability;
- reference/control Fisher rate;
- total profiled information per wall-clock second.

## 2. Clock-jitter mapping

The source phase is `tau = 2 pi f_gap t`. Therefore a dimensionless timing prior `sigma_tau` corresponds to

` sigma_t = sigma_tau / (2 pi f_gap) `.

Using the corrected Iteration-016 priors at `f_gap=100 Hz`:

- D1: `sigma_tau=5.95e-3` -> `sigma_t ~= 9.47 us`;
- D2: `sigma_tau=5.03e-3` -> `sigma_t ~= 8.01 us`.

For a white one-sided timing-jitter ASD `J_t` integrated over effective reference bandwidth `B_ref`,

` sigma_t^2 = J_t^2 B_ref `,

so

` J_t <= sigma_t / sqrt(B_ref) `.

Illustrative limits:

| branch | B=1 Hz | B=100 Hz | B=1 kHz |
|---|---:|---:|---:|
| D1 | 9.47 us/sqrtHz | 0.947 us/sqrtHz | 0.299 us/sqrtHz |
| D2 | 8.01 us/sqrtHz | 0.801 us/sqrtHz | 0.253 us/sqrtHz |

These values are bookkeeping translations of the current local prior, not specifications for a chosen clock architecture.

If `K` statistically independent timing-edge errors add in quadrature, then the per-edge RMS requirement is

` sigma_edge <= sigma_t/sqrt(K) `.

At 100 Hz, for `K=4` this gives about `4.73 us` D1 and `4.00 us` D2. Correlated clock errors do not receive this `sqrt(K)` relaxation and must be modeled as common-mode nuisances instead.

## 3. Coherent shot duration places a hard floor on cycle time

The largest accepted calibration phase is `tau_max=4.99085067`, so

`T_coh,min = tau_max/(2 pi f_gap)`.

At `100 Hz`:

`T_coh,min ~= 7.94 ms`.

Therefore any physical wall-clock estimate at 100 Hz must use a cycle time at least this long before adding preparation, readout and reset dead time. Earlier generic 1-ms/shot illustrations cannot be simultaneously interpreted as full-span shots at `f_gap=100 Hz`.

### RQIR-RESOURCE-002 — coherence floor must enter Fisher-rate accounting

A repetition budget cannot be converted to seconds by multiplying by an arbitrary nominal shot time below the required coherent evolution span.

## 4. Corrected calibration shot-equivalent scale

The corrected 90%-retention q=1 allocations are:

D1:
- `gamma_mean ~= 1.72199e6`;
- `gamma_cov ~= 0.938147e6`.

D2:
- `gamma_mean ~= 2.41445e6`;
- `gamma_cov ~= 0.929440e6`.

For detector SNR `rho_D=5`, `S_D=25`. If mean and covariance rows both have standardized per-shot sensitivity `xi`, the physical shot-equivalent count is

`N_C = S_D [14 gamma_mean/xi_mean^2 + 8 gamma_cov/xi_cov^2]`.

At `xi_mean=xi_cov=10`:

- D1: `N_C ~= 7.90e6` accepted-shot equivalents;
- D2: `N_C ~= 1.031e7`.

At `f_gap=100 Hz`, even with zero dead time and unit success probability, the coherence-span lower bounds are therefore approximately:

- D1: `17.4 h`;
- D2: `22.7 h`.

With `1 ms` extra dead time and `p_success=0.5`:

- D1: `~39.3 h`;
- D2: `~51.2 h`.

These are still standardized examples, because actual `xi_mean` and `xi_cov` are not yet tied to a hardware-specific D1/D2 noise model. Their role is to expose the scaling correctly.

## 5. Preparation/reset metrology

RQIR-NG-005 requires independent information on the hidden-state amplitude `a`. For detector information `S_D` and desired isolated preparation-retention fraction `r`,

`C_a = S_D r/(1-r)`.

At detector SNR 5:

| r | C_a | local sigma(a)=1/sqrt(C_a) |
|---:|---:|---:|
| 80% | 100 | 0.100 |
| 90% | 225 | 0.0667 |
| 95% | 475 | 0.0459 |

If one preparation-metrology shot has standardized sensitivity `xi_prep`,

`N_prep = C_a/xi_prep^2`.

Thus the 90% example needs 225 accepted shots for `xi_prep=1`, or 22500 for `xi_prep=0.1`. A non-unit preparation success probability multiplies the wall time by `1/p_success`.

The important interpretation is that shot-to-shot reset/repreparation quality must be measured, not merely assumed. If the reset variation changes the hidden amplitude, it belongs in the source-preparation covariance and cannot be absorbed into the gravitational calibration matrix because that direction is deliberately null there.

## 6. Wall-clock square-root allocation law

A fixed 90% source-metrology retention is not generally the wall-clock optimum.

Consider the two-resource limit with detector Fisher rate `R_D` and independent preparation-metrology rate `R_P`. Allocate total time `T` as `T_D=xT`, `T_P=(1-x)T`. Then

`S=R_D xT`, `C=R_P(1-x)T`,

and, after profiling only the preparation amplitude,

`F = S C/(S+C)`.

Maximizing `F/T` gives

`x_D = sqrt(R_P)/(sqrt(R_D)+sqrt(R_P))`,

`x_P = sqrt(R_D)/(sqrt(R_D)+sqrt(R_P))`,

and

`(F/T)_max = [sqrt(R_D R_P)/(sqrt(R_D)+sqrt(R_P))]^2`.

At this optimum the preparation-retention fraction is

`r_* = sqrt(R_P)/(sqrt(R_D)+sqrt(R_P))`.

### RQIR-RESOURCE-003 — square-root wall-clock allocation

In the two-resource local limit, optimal time allocation scales with square roots of Fisher rates, not with a fixed desired retention fraction.

A 90% preparation-retention fraction is wall-clock optimal only if

`R_P/R_D = [0.9/0.1]^2 = 81`.

Examples:

| R_P/R_D | optimal preparation retention |
|---:|---:|
| 1 | 50% |
| 4 | 66.7% |
| 9 | 75% |
| 81 | 90% |
| 100 | 90.9% |

Therefore the previous 80/90/95% tables are constraint benchmarks, not automatically optimal experimental schedules.

## 7. Gain-reference monitoring

Iteration 017 found a local posterior-scale RMS beta-bias coefficient

`bias/sigma_beta ~= 0.325 |delta g|`

for common gain×residual-source coupling.

If one allocates a local RMS bias budget `b sigma_beta`, then

` sigma_g <= b/0.325 `.

Illustrative reference requirements:

| allowed RMS bias | sigma_g max | equivalent gain-reference SNR `1/sigma_g` |
|---:|---:|---:|
| 0.1 sigma_beta | 0.308 | 3.25 |
| 0.01 sigma_beta | 0.0308 | 32.5 |
| 0.001 sigma_beta | 0.00308 | 325 |

This remains a **local posterior-scale** rule. It is not a global gain tolerance because the true nonlinear contamination is proportional to `delta g * delta theta`; larger residual source-state error requires proportionally stronger gain monitoring.

## 8. Main design consequences

1. The corrected calibration budget can imply many hours of wall time even at standardized per-shot sensitivity `xi=10`, because the coherent phase span already consumes about 7.94 ms per accepted shot at 100 Hz.
2. Dead time and preparation success enter multiplicatively in wall-clock cost and can easily erase modest Fisher-allocation improvements.
3. A fixed 90% nuisance-retention target is not a universal optimum; information rates determine the optimal split.
4. Clock/reference requirements should be expressed as PSD/bandwidth or common-mode nuisance priors, not only as a single timing RMS.
5. Reset/repreparation metrology and gravitational calibration are logically distinct resources because of RQIR-NG-005.

## 9. Next gate

Build branch-specific physical Fisher rates:

- D1: phase-shot variance, finite contrast, four-switch control, timing reference, preparation success, readout/reset dead time;
- D2: equivalent-force PSD, finite integration window, sampling reference and detector duty cycle;
- source metrology: explicit `R_P` rather than abstract `xi_prep`;
- then jointly optimize detector, preparation and calibration time fractions using full `F_beta|theta/T_wall` rather than the two-resource analytic limit.

## Reproducibility

See `analysis/reference_channel_wallclock_iteration018.py`.
