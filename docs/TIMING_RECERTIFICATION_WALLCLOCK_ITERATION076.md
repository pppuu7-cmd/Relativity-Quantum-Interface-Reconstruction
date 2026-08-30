# RQIR Iteration 076 — Timing Recertification Duty / Control-Aware Wall Clock

**Date:** 2026-08-30  
**Status:** parametric control-resource closure; not an oscillator/apparatus forecast and not a new-physics claim.

## 1. Purpose

Iteration 075 found that Toy014 requires a source-specific timing tolerance

`sigma_t ~= 3.97715 us`

at 100 Hz and that unconstrained timing/geometry/additive nuisances still destroy the D2 discriminator. The remaining question is how periodic timing-reference recertification enters the Iteration-071 wall clock.

This iteration keeps the same transparent Brownian-diffusion benchmark used in earlier drift work:

- timing diffusion coefficient `D_tau` in `us^2/h`;
- single accepted timing-reference event uncertainty `sigma_event`;
- reference block targets `sigma_ref = sigma_target/3`;
- zero independent stability floor unless explicitly supplied.

## 2. Fourth-power timing law

Reference block time is

`T_ref = (t_cycle/p) (sigma_event/sigma_ref)^2`.

For Brownian timing diffusion, the allowed recertification interval is

`T_cad = 2 (sigma_target^2 - sigma_floor^2 - sigma_ref^2)/D_tau`.

With `sigma_ref=sigma_target/3` and zero floor,

`T_cad = (16/9) sigma_target^2/D_tau` hours.

Therefore the fractional reference duty

`d_tau = T_ref/T_cad`

scales as

`boxed{d_tau proportional to D_tau * sigma_event^2 * t_cycle / sigma_target^4}`.

### RQIR-RESOURCE-035 — timing recertification has a fourth-power tolerance penalty

> In the declared white-reference/Brownian-drift model, tightening the required timing tolerance increases recertification duty as `sigma_target^-4`. A modestly stricter timing tolerance can therefore become a large control-resource penalty even when a single reference block is short.

This scaling is conditional on the declared diffusion/reference model; other drift spectra require their own likelihood/cadence calculation.

## 3. Toy014 vs Toy009 reference duty

Using

- event jitter `10 us`;
- acceptance `p=0.5`;
- 1-ms dead/read time;
- zero stability floor;
- Toy014 target `3.97715 us`, cycle `~7.8133 ms`;
- Toy009 target `9.19001 us`, cycle `~8.9432 ms`,

we obtain:

| `D_tau [us^2/h]` | Toy014 duty | Toy009 duty | Toy014/Toy009 |
|---:|---:|---:|---:|
| 100 | `8.7829e-4` (`0.0878%`) | `3.5263e-5` | `~24.91` |
| 1000 | `8.7829e-3` (`0.878%`) | `3.5263e-4` | `~24.91` |

Thus Toy014's stricter timing tolerance costs roughly **25x more reference duty** than Toy009 under identical timing-reference/drift assumptions.

However, for these illustrative diffusion values the **absolute** Toy014 timing overhead is still below 1%. This is important: the stricter control requirement does not automatically erase Toy014's resource improvements over the older local sources.

## 4. Control-aware Toy014 vs Toy009 boundary

If periodic timing references occupy fraction `d` of total wall clock, payload time is multiplied by

`m=1/(1-d)`.

Using the Iteration-074 projected Toy014 resource vector

`(q_s,q_c,q_p)=(3.53339,3.48483,0.67054)`,

the no-control reference boundary was

`y > 7.6895 + 7.5421 x`.

Including the differential timing-reference duty gives approximately:

### `D_tau=100 us^2/h`

`boxed{y > 7.7118 + 7.5640 x}`.

### `D_tau=1000 us^2/h`

`boxed{y > 7.9178 + 7.7665 x}`.

So in this reference drift range the control correction shifts the architecture boundary only modestly, despite the large *relative* Toy014/Toy009 control-duty ratio.

## 5. When timing recertification becomes a first-order cost

Because duty is linear in `D_tau` in this model, Toy014 reaches

- `10%` reference duty at `D_tau ~= 1.14e4 us^2/h`;
- `100%` formal duty at `D_tau ~= 1.14e5 us^2/h`.

The latter marks failure of the simple cadence architecture, not a physically meaningful operating point.

A nonzero stability floor makes the situation worse: as

`sigma_floor^2 + sigma_ref^2 -> sigma_target^2`,

the cadence collapses and duty diverges, reproducing the logic of RQIR-NG-007.

## 6. Interpretation

Toy014 now has a more complete resource picture:

- exact nearest-neighbour locality and NP3 null;
- healthy physical two-band D2 signal;
- physical calibration factor `~3.48x` Toy009;
- Ramsey source-metrology rate `~1.49x` Toy009;
- systematics require independent control priors;
- timing control is stricter than Toy009 but does not dominate the transparent low/moderate-diffusion wall clock.

The largest remaining uncertainty is no longer an abstract Fisher normalization. It is the **actual detector transfer/PSD matrix and low-frequency timing/reference stability**.

## 7. Reproducibility

Code:

`analysis/timing_recertification_wallclock_iteration076.py`

The script verifies Toy014/Toy009 duties, the fourth-power scaling benchmark, the control-aware architecture boundaries, and the diffusion levels where reference duty reaches 10%/100%.

## 8. Next gate

The next scientifically useful step is to combine Toy014 and Toy013 with the full Iteration-071 source-specific rates and treat detector transfer and timing drift as explicit dimensionless ratios:

- `R_beta` science;
- seven `R_cal,j` matrix-Fisher calibration rates;
- `R_src` Ramsey/pointer source metrology;
- `d_ctrl(D_tau, sigma_event, floor)`.

Then identify which ratios would have to be measured in a real apparatus to decide Toy009 vs Toy014 vs Toy013, rather than introducing arbitrary ASD numbers.
