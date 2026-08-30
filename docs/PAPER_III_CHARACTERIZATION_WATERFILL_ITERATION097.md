# RQIR Iteration 097 — Optimal Characterization-Time Allocation

**Date:** 2026-08-30  
**Status:** Paper-III characterization-resource optimization; no apparatus forecast and no new-physics claim.

## 1. Purpose

Iteration 096 converted architecture decision leverage into value per physical characterization second.  A finite campaign should not repeatedly characterize only the currently best coordinate forever, because Fisher-limited uncertainty reduction has diminishing returns.

This iteration solves the finite-time allocation problem analytically in the locally smooth, independent, no-floor limit.

## 2. Local decision-width model

On a fixed active robust branch, linearize the unresolved-band width with respect to positive independent uncertainty scales `h_i`:

`W ~= W_const + sum_i c_i h_i`,

where

`c_i = partial W/partial h_i > 0`.

Let each characterization channel accumulate independent Fisher information

`I_i(t_i)=I_i0+R_i t_i`,

so

`h_i(t_i)=1/sqrt(I_i0+R_i t_i)`.

For a total characterization budget

`sum_i t_i = T_char`, `t_i>=0`,

the variable part of the robust decision width is

`Phi(t)=sum_i c_i / sqrt(I_i0+R_i t_i)`.

Each term is convex because

`d2Phi_i/dt_i2 = 3 c_i R_i^2/[4(I_i0+R_i t_i)^(5/2)] > 0`.

Therefore the KKT solution is the global optimum of the declared local model.

## 3. RQIR-RESOURCE-050 — characterization water-filling law

For every active channel the marginal decision-band shrink rate must be equal:

`c_i R_i/[2(I_i0+R_i t_i)^(3/2)] = lambda`.

Hence

`boxed{t_i(lambda) = max{0, [(c_i R_i/(2 lambda))^(2/3)-I_i0]/R_i}}`.

The unique `lambda>0` is chosen so that

`sum_i t_i(lambda)=T_char`.

This is a decision-weighted Fisher **water-filling** law.

A channel is inactive while its initial marginal value

`M_i0 = c_i R_i/(2 I_i0^(3/2))`

is below the current common active marginal `lambda`.

As the highest-value channels accumulate Fisher information their marginal values fall and additional channels enter the active set automatically.

## 4. Relation to Iteration 096

Because

`h_i=I_i^(-1/2)`

and

`Lambda_i=(c_i h_i)/W`,

the initial dimensionless marginal shrink rate is exactly

`(1/W) M_i0 = (1/2) Lambda_i R_i h_i^2 = Xi_i`.

Thus RESOURCE-050 is the finite-budget continuation of RESOURCE-048.

Iteration 096 tells which measurement receives the **next infinitesimal second**.  Iteration 097 tells how a finite campaign should redistribute time as uncertainties shrink.

## 5. RQIR-NG-050 — equal characterization time is generally suboptimal

Equal time, equal fractional interval contraction, and ranking by raw percent uncertainty are not generally optimal characterization policies.

They are optimal only in special symmetric cases where the relevant marginal decision values happen to agree.

For a real apparatus, characterization time should be allocated according to RESOURCE-050 or the corresponding joint/correlated robust optimization.

## 6. Deterministic regression using the Iteration-094 synthetic box

For regression only, take

- `W=1` and current `h_i=1`, so `c_i=Lambda_i`;
- equal characterization Fisher rates `R_i=1`;
- the six Iteration-094 aggregate uncertainty coordinates.

The exact water-filling schedule gives:

### Total normalized characterization time `T=0.1`

Only Toy014 `R_src` is active; essentially all `0.1` goes there.

### `T=1`

The optimal allocation is approximately

- Toy014 `R_src`: `0.59710`;
- Toy009 `R_src`: `0.40290`;
- all four other channels: zero.

### `T=3`

The active set expands to

- Toy014 `R_src`: `1.47494`;
- Toy009 `R_src`: `1.17401`;
- Toy014 `A`: `0.22649`;
- Toy014 duty: `0.12456`;
- Toy009 duty and `A`: zero.

All active channels have the same final marginal decision value to numerical precision.  The optimized objective is strictly smaller than equal-time allocation.

These allocations are regression-only and carry no hardware meaning because the Iteration-094 box and equal `R_i` are synthetic.

## 7. Systematic floors and nonsmooth gates

The analytic law above assumes independent no-floor Fisher accumulation on a fixed smooth branch.

For nonzero uncertainty floors, use the Iteration-096 floor-aware contraction law and solve the resource allocation piecewise/numerically.

For correlated parameter posteriors, replace independent scalar `I_i` by the joint Fisher/covariance update.

At calibration eigenvalue crossings, PSD-boundary contact, robust-corner switches, or Ramsey optimum active-set changes, NG-048 forbids blindly applying a single derivative; use finite contractions or robust optimization and recompute the active set.

## 8. Scientific consequence

The apparatus-characterization layer is now placed on the same resource footing as science, calibration and source metrology:

- science time is allocated by physical `R_beta`;
- source closure by `R_src`;
- calibration by seven matrix `R_cal,j`;
- characterization itself now has physical `R_char,i` and an optimal finite-time schedule.

What remains experimentally open is not the allocation algebra.  It is the declared primitive uncertainty/Fisher-rate envelope for one common Toy009/Toy014 apparatus.

## 9. Next gate

Construct the first declared primitive Toy009/Toy014 characterization table containing, for each active science/calibration/source/control primitive:

`central value, uncertainty, characterization Fisher rate, irreducible floor, correlations, and duty/cost`.

Use repository-backed source coefficients and externally measured or explicitly design-envelope apparatus quantities.  Then run RESOURCE-050 together with RESOURCE-045/NG-030 and identify a robust architecture or the residual unresolved region.

Do not begin Toy015 unless this physical schedule shows a genuinely source-dependent bottleneck.

## 10. Reproducibility

Run:

`python analysis/characterization_waterfill_iteration097.py`

The script verifies the KKT solution, staged active-set entry, equal final marginal values on active channels, and strict improvement over equal-time allocation in the synthetic regression.
