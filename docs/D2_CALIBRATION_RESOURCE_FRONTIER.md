# RQIR Iteration 027 — D2 Calibration / Preparation Resource Frontier

**Date:** 2026-08-29

## Scope

Iteration 026 showed that the three D2 calibration branches have genuinely different null structures. This iteration does **not** invent SI-time costs for them. Instead it computes the exact local Fisher Pareto frontier between calibration exposure and independent source-preparation Fisher for the common target

`F_{beta|theta} = 0.90`

on the same 23D hard trace+energy-constrained Toy009 source tangent space.

The branches are:

1. `NP3-null`: potential means + covariance rows;
2. `native-replace`: force-gradient means + covariance rows;
3. `augmented`: potential means + force-gradient means + covariance rows.

The corrected D2 baseline row weights are retained:

- `gamma_mean = 2.414e6`;
- `gamma_cov = 0.929e6`.

A common calibration multiplier `lambda` scales these benchmark Fisher weights. Independent source-preparation information is `C_a`. The Iteration-020 source-amplitude QFI is `F_Q(a=0.08)=13.2707` per ideal accepted copy.

## Core result: target-retention frontier

For each branch define `C_a^*(lambda)` as the minimum source-preparation Fisher needed to reach 90% detector-level profiled information.

### NP3-null

This branch retains the exact hidden amplitude obstruction. At `lambda=1` even formally infinite `C_a` falls infinitesimally below the 0.90 target because other nuisance directions remain at their benchmark calibration precision. The calibration multiplier required with asymptotically strong source metrology is

`lambda_min,strong-prep = 1.000239887`.

The frontier is extremely steep close to that threshold:

- `lambda=1.001`: `C_a^* ~= 1.2131e4`;
- `lambda=1.01`: `C_a^* ~= 953.04`;
- `lambda=1.05`: `C_a^* ~= 194.18`;
- `lambda=1.10`: `C_a^* ~= 101.37`;
- `lambda=1.20`: `C_a^* ~= 55.14`;
- `lambda=1.50`: `C_a^* ~= 27.45`;
- `lambda=2.00`: `C_a^* ~= 18.22`;
- `lambda -> infinity`: `C_a^* -> 9`, consistent with the ideal one-amplitude law `r/(1-r)=9` for `r=0.9` and normalized detector Fisher.

At `lambda=1.05`, `C_a^*=194.18` corresponds to about `14.63` ideal QFI-copy equivalents. At `lambda=2`, `18.22` corresponds to about `1.37` ideal-copy equivalents; physically, an integer-copy implementation would still require at least two accepted copies unless a continuous/metrological realization is used.

### Native-force replacement

The force-only replacement branch keeps a rotated exact null, so gravitational calibration alone still cannot reach 90% even for arbitrarily large exposure. However, its calibration geometry constrains the old hidden direction strongly enough that much less independent preparation Fisher is needed.

With asymptotically strong preparation metrology,

`lambda_min,strong-prep = 0.353369007`.

At the corrected benchmark `lambda=1`:

`C_a^* ~= 12.9694`,

which is about `0.977` ideal QFI-copy equivalents. This should be read as a Fisher-equivalent quantity, not as a claim that fewer than one physical copy can be measured.

The structural rotated-null obstruction remains: `C_a=0` saturates near `F_{beta|theta}~=0.0423` even as calibration exposure becomes arbitrarily large.

### Augmented potential + force calibration

The augmented branch closes the current 23D source tangent space locally. With asymptotically strong preparation metrology, only

`lambda_min,strong-prep = 0.171381513`

is needed to reach 90%.

At `lambda=1`:

`C_a^* ~= 11.7130`,

or about `0.883` ideal QFI-copy equivalents.

More importantly, this branch can trade calibration for preparation completely: at

`lambda ~= 4.89`

one reaches 90% with `C_a ~= 0`, reproducing Iteration 026.

## New resource principle

**RQIR-RESOURCE-007 — calibration/preparation Pareto boundary.**

A fixed target retention does not define a unique preparation budget or calibration budget. For a declared calibration observable set, the physically meaningful object is the branch-specific frontier

`C_a^*(lambda)`.

Comparing branches by one Fisher number at one arbitrary `gamma` can be misleading, especially near a nuisance threshold where `C_a^*(lambda)` can diverge sharply.

## Wall-clock conversion without hidden assumptions

The three branches must be converted to time with different physical calibration costs:

`T_null   = lambda (K_pot + K_cov) + C_a/R_P`,

`T_force  = lambda (K_force + K_cov) + C_a/R_P`,

`T_aug    = lambda (K_pot + K_force + K_cov) + C_a/R_P`.

Here:

- `K_pot` is the wall time needed to realize the `lambda=1` potential-mean Fisher rows;
- `K_force` is the wall time for the `lambda=1` force-gradient rows;
- `K_cov` is the covariance/noise calibration time;
- `R_P` is independent source-preparation Fisher per second.

These quantities are not interchangeable. In particular, the lower `lambda` required by the augmented branch does not automatically mean lower wall time because it contains twice as many mean-row families.

## Negative result / caution

There is no scientifically valid statement yet that one of the three D2 branches is globally cheaper. That ranking depends on the physical ratios `K_force/K_pot`, `K_cov/K_pot`, and `R_P K_pot`, together with timing/reference-control duty.

Therefore no SI-hour claim is made in this iteration.

## Reproducibility

Code: `analysis/d2_calibration_resource_frontier_iteration027.py`.

The script imports the exact Iteration-026 Fisher construction, computes `C_a^*(lambda)`, converts it to ideal QFI-copy equivalents, and includes regression guards on the headline thresholds.

## Next gate

Obtain or parameterize `K_pot`, `K_force`, and `K_cov` from the native D2 force-PSD/transduction model, then minimize the above wall-clock expressions along each exact Fisher frontier. This will produce a branch phase diagram showing when source metrology, force calibration, or complementary augmented calibration is the cheapest way to preserve detector information.
