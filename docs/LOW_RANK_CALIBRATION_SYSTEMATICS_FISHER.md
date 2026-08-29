# RQIR Iteration 016 — Low-Rank Calibration Systematics Fisher

**Date:** 2026-08-29  
**Status:** first-order nuisance-identifiability result in corrected hard-constrained basis.

## 1. Model

Use the exact 22-dimensional source-nuisance basis from Iteration 015. Add four explicit calibration-systematics nuisance parameters:

1. `delta y` — second-probe position drift;
2. `delta tau` — common source phase/time drift;
3. `b_mean` — common additive offset on the 14 potential-mean rows;
4. `b_cov` — common additive offset on the 8 covariance/noise rows.

The calibration model is locally

`delta mu_C = A_c u + V z`,

where `u` is the 22D allowed source nuisance, `z=(delta y,delta tau,b_mean,b_cov)`, and `V` contains the corresponding four row-space derivative vectors.

Finite control knowledge enters through prior Fisher matrix `P_z`.

## 2. Structural result with no control priors

If all four systematic amplitudes are allowed to float without finite priors, the profiled detector information collapses to numerical zero for both D1 and D2.

Crucially, scaling all gravitational calibration weights by `2x`, `10x`, or `100x` does not restore information.

The reason is structural: additional shots determine only the combined row-space displacement `A_c u + V z`. If source nuisance directions can trade against unrestricted systematic directions inside the detector-relevant subspace, exposure alone does not separate them.

### RQIR-NG-006 — uncontrolled calibration-systematics degeneracy

For a detector parameter whose nuisance rejection relies on calibration `A_c u`, if an unrestricted systematic model `V z` overlaps the detector-relevant calibration image strongly enough, increasing calibration Fisher at fixed systematic model need not recover identifiability. Independent control/prior information on `z` is required.

Scope: local first-order finite-dimensional Toy009 likelihood. This is not a theorem about all experimental designs.

## 3. Finite control priors restore identifiability

A simple standardized control bundle was tested. Each systematic-induced calibration residual is constrained to approximately 10% of the statistical row uncertainty for the corrected q=1 Iteration-015 allocation.

### D1 corrected 90% allocation

Using approximately

- `gamma_mean = 1.72e6`,
- `gamma_cov = 0.94e6`,

the corresponding 10%-sigma prior widths are approximately

- `sigma(delta y) ~= 0.472` dimensionless geometry units;
- `sigma(delta tau) ~= 5.95e-3`;
- `sigma(b_mean) ~= 7.62e-5` row-normalized output units;
- `sigma(b_cov) ~= 1.03e-4` row-normalized output units.

The resulting profiled information is about

`F_beta ~= 0.89996`.

At `f_gap=100 Hz`, the phase/time prior corresponds to roughly `9.5 us`.

### D2 corrected 90% allocation

Using approximately

- `gamma_mean = 2.41e6`,
- `gamma_cov = 0.93e6`,

the 10%-sigma prior widths are approximately

- `sigma(delta y) ~= 0.399`;
- `sigma(delta tau) ~= 5.03e-3`;
- `sigma(b_mean) ~= 6.44e-5`;
- `sigma(b_cov) ~= 1.04e-4`.

The resulting profiled information is about

`F_beta ~= 0.89989`.

At `100 Hz`, the timing prior is about `8.0 us`.

These are standardized toy-model control requirements, not hardware specifications.

## 4. Resource/control trade

If both calibration information and matched control-prior information are doubled according to the same 10%-of-statistical-sigma rule, retained information rises to about `0.947` for both branches.

Thus there is a clean trade:

- more gravitational calibration shots alone do not cure unrestricted systematics;
- tighter independent control alone can restore identifiability;
- increasing calibration exposure and tightening control together improves the detector information.

This makes control metrology a first-class resource alongside source preparation, gravitational calibration, and detector exposure.

## 5. Important interpretation of geometry drift

Iteration 014 noted that `||v_y||` is much smaller than `||v_tau||`. Iteration 016 shows why derivative norm alone is not enough: with no prior, even the small geometry-drift column can destroy identifiability because the nuisance amplitude is unbounded and its row-space direction can align with a dangerous source nuisance.

Therefore drift importance must be judged by both

- derivative magnitude;
- orientation relative to detector-relevant nuisance directions;
- available prior/control precision.

## 6. Multiplicative gain

Pure common gain remains first-order suppressed at the exact null (`A theta0=0`). The leading gain-state contamination is bilinear, schematically

`delta mu_C ~ delta g * A delta theta`.

That term is second order in local perturbations and cannot be represented honestly as a new first-order Fisher column at the nominal exact-null point.

Therefore it is deferred to a nonlinear/bias robustness calculation rather than inserted artificially into the local Fisher matrix.

## 7. New design rule

### RQIR-CAL-007 — exposure cannot replace independent control for overlapping systematic directions

When calibration systematics occupy detector-relevant row-space directions, shot count and control prior are non-substitutable resources. Increasing exposure reduces statistical noise but does not identify an unrestricted systematic amplitude that is structurally degenerate with source nuisance.

## 8. Next gate

Perform a second-order bias/nonlinear likelihood audit for multiplicative gain-state coupling and timing nonlinearities. Then translate the finite `delta tau`, additive-offset and preparation priors into explicit D1 pulse-clock/reset requirements and D2 sampling/reference-channel requirements.

Reproducibility code: `analysis/low_rank_systematics_fisher_iteration016.py`.
