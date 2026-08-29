# Recovery Delta — Iteration 027

**Date:** 2026-08-29

## New operational facts

Iteration 027 converts the Iteration-026 D2 calibration-branch comparison into a fixed-retention resource frontier.

Target: `F_{beta|theta}=0.90` on the same exact trace+energy hard-constrained Toy009 tangent space.

For each branch define `C_a^*(lambda)` as the minimum independent source-preparation Fisher required when all branch calibration Fisher weights are multiplied by `lambda`.

Strong-preparation minimum calibration multipliers:

- NP3-null: `lambda_min=1.000239887`;
- native-force replacement: `lambda_min=0.353369007`;
- augmented potential+force: `lambda_min=0.171381513`.

At `lambda=1`:

- NP3-null remains just below the 90% ceiling even for `C_a -> infinity` because non-amplitude source nuisances are still fractionally under-calibrated;
- native-replace requires `C_a^*=12.9694`;
- augmented requires `C_a^*=11.7130`.

The NP3 frontier is singular near its calibration threshold. Representative values:

- `lambda=1.001 -> C_a^*~1.2131e4`;
- `1.01 -> 953.04`;
- `1.05 -> 194.18`;
- `1.10 -> 101.37`;
- `1.20 -> 55.14`;
- `1.50 -> 27.45`;
- `2.00 -> 18.22`;
- `lambda -> infinity -> C_a^* -> 9`.

With Iteration-020 `F_Q=13.2707`, ideal accepted-copy equivalents are `C_a/F_Q`; these are Fisher equivalents, not literal fractional physical copies.

The augmented branch can eliminate the independent preparation requirement at `lambda~4.89`, reproducing Iteration 026.

## New label

**RQIR-RESOURCE-007 — calibration/preparation Pareto boundary:** at fixed target detector retention, the correct resource object is the branch-specific function `C_a^*(lambda)`, not one arbitrary `gamma` and not one arbitrary fixed preparation prior.

## Wall-clock discipline

Do not rank the branches in SI time until the physical calibration rates are supplied. Use

- `T_null=lambda(K_pot+K_cov)+C_a/R_P`;
- `T_force=lambda(K_force+K_cov)+C_a/R_P`;
- `T_aug=lambda(K_pot+K_force+K_cov)+C_a/R_P`.

The augmented branch contains an extra mean-row family; lower required `lambda` does not automatically mean lower wall time.

## Reproducibility

- `analysis/d2_calibration_resource_frontier_iteration027.py`
- `docs/D2_CALIBRATION_RESOURCE_FRONTIER.md`
- `research_log/2026-08-29_iteration_027_d2_calibration_resource_frontier.md`

## Next gate

Construct a branch phase diagram versus `K_force/K_pot`, `K_cov/K_pot`, and physical preparation Fisher rate; then insert justified D2 force-PSD/transduction inputs and timing/reference duty.
