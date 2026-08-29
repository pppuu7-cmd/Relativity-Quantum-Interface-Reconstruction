# RQIR Research Log — Iteration 027

**Date:** 2026-08-29
**Target:** D2 calibration/preparation resource frontier after Iteration 026.

## Starting point

Iteration 026 established three distinct D2 calibration branches on the exact trace+energy hard-constrained Toy009 tangent space: NP3-null, native-force replacement, and augmented potential+force. The next useful gate was not another rank test but a resource tradeoff at fixed detector-level profiled Fisher.

## Method

Reused `analysis/d2_calibration_branch_fisher_iteration026.py` without changing its source/calibration/detector geometry. For each branch and common calibration multiplier `lambda`, solved for the minimum independent source-preparation Fisher `C_a` satisfying

`F_{beta|theta} >= 0.90`.

Converted `C_a` to ideal accepted source-copy equivalents with Iteration-020 `F_Q=13.2707`.

No wall-clock hours were assigned because physical potential-row versus force-row Fisher rates remain branch dependent.

## Results

Strong-preparation minimum calibration multipliers:

- NP3-null: `lambda_min ~= 1.000239887`;
- native-replace: `lambda_min ~= 0.353369007`;
- augmented: `lambda_min ~= 0.171381513`.

At `lambda=1`:

- NP3-null lies infinitesimally below the 90% ceiling even as `C_a -> infinity`; small extra calibration is required.
- native-replace needs `C_a^* ~= 12.9694`.
- augmented needs `C_a^* ~= 11.7130`.

The NP3 frontier is sharply singular near its calibration threshold:

- `lambda=1.001`: `C_a^* ~= 1.2131e4`;
- `1.01`: `953.04`;
- `1.05`: `194.18`;
- `1.10`: `101.37`;
- `1.20`: `55.14`;
- `1.50`: `27.45`;
- `2.00`: `18.22`;
- asymptotically `C_a^* -> 9`.

The augmented branch reproduces the Iteration-026 no-preparation point at `lambda ~= 4.89`.

## New rule

**RQIR-RESOURCE-007:** preparation and calibration must be compared through the branch-specific Pareto frontier `C_a^*(lambda)` at a declared target detector retention. A single nominal `gamma` or a fixed `C_a` can hide a near-threshold divergence and is not a robust resource descriptor.

## Negative result

No branch can yet be called globally cheaper in SI time. The relevant wall-clock forms are

- `T_null=lambda(K_pot+K_cov)+C_a/R_P`;
- `T_force=lambda(K_force+K_cov)+C_a/R_P`;
- `T_aug=lambda(K_pot+K_force+K_cov)+C_a/R_P`.

The ordering depends on physical row Fisher rates and control duty. No hidden equal-rate assumption was introduced.

## Files

- `analysis/d2_calibration_resource_frontier_iteration027.py`
- `docs/D2_CALIBRATION_RESOURCE_FRONTIER.md`
- `recovery/RECOVERY_DELTA_ITERATION_027.md`

## Next gate

Build the dimensionless branch phase diagram in terms of `K_force/K_pot`, `K_cov/K_pot`, and preparation Fisher rate, then substitute experimentally justified D2 force-PSD/transduction inputs when available.
