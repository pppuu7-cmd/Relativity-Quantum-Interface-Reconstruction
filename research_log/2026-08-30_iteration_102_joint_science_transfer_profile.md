# RQIR Research Log — Iteration 102

**Date:** 2026-08-30

## Goal

Continue from Iteration 101 and put same-state injected transfer calibration inside the science Fisher, rather than treating transfer error bars as post-hoc tolerances. Derive the optimal science/calibration time split before reopening any source search.

## Main result — transfer-gain Schur closure

For science mean derivative `s`, science metric `W`, transfer nuisance map `D`, and independent injected-calibration Fisher `C`,

`F_beta|g = s^T W s - s^T W D (D^T W D + C)^-1 D^T W s`.

Registered as **RQIR-RESOURCE-055**.

## New structural no-go

With two free per-band multiplicative gains and no independent transfer calibration, the common science amplitude lies in the span of the gain nuisance columns and

`F_beta|g = 0`.

Registered as **RQIR-NG-056**. More science exposure cannot repair this exact transfer degeneracy.

## Covariance-parameter distinction

For an ordinary multivariate Gaussian with mean parameters separated from covariance parameters, the expected Fisher cross block between a mean parameter and covariance-only parameter `rho` is zero. Thus `rho` uncertainty belongs in the robust covariance envelope/characterization budget rather than being subtracted as if it were an ordinary multiplicative mean nuisance.

Registered as **RQIR-STAT-003**.

**RQIR-NG-057:** this orthogonality is conditional and can fail for beta-dependent covariance, non-Gaussian/cyclostationary likelihoods, shared transfer/whitening parameters, or robust active-set switches.

## Exact balanced two-band result

For symmetric raw band rate `r`, covariance correlation `rho`, science time `T_sci`, and simultaneous per-gain transfer-calibration rate `c` over calibration time `T_cal`,

`F_beta|g = 2 c r T_cal T_sci/[c T_cal(1+rho)+r T_sci]`.

Define

`R_s=2r/(1+rho)`, `R_c=2c`.

Then

`1/F = 1/(R_s T_sci)+1/(R_c T_cal)`.

For target `F_*=Z^2`, the minimum separate science+calibration wall time is

`T_total^min = F_* [1/sqrt(R_s)+1/sqrt(R_c)]^2`,

with

`T_sci/T_cal=sqrt(R_c/R_s)`.

Registered as **RQIR-RESOURCE-056**.

## Calibration-speed thresholds

Relative to perfect transfer calibration,

`P=[1+sqrt(R_s/R_c)]^2`.

Therefore:

- `P<=1.10` requires `R_c/R_s>=419.76`;
- `P<=1.25` requires `R_c/R_s>=71.78`;
- `P<=2` requires `R_c/R_s>=5.828`.

These thresholds apply to the declared separate-time balanced Gaussian slice; simultaneous non-invasive references require a different shared-likelihood schedule.

## Numerical validation

`analysis/joint_science_transfer_profile_iteration102.py` verifies:

- free-gain profiled Fisher is zero numerically;
- strong calibration recovers raw science Fisher;
- the matrix formula reduces exactly to the balanced closed form;
- the harmonic reciprocal-Fisher identity;
- the analytic wall-clock optimum against a dense numerical scan;
- the stated overhead thresholds.

## Files

- `analysis/joint_science_transfer_profile_iteration102.py`
- `docs/PAPER_III_JOINT_SCIENCE_TRANSFER_PROFILE_ITERATION102.md`
- `recovery/RECOVERY_DELTA_ITERATION_102.md`

## Next gate

Extend the transfer-profile calculation to the full four-real-component complex `f,2f` likelihood, including gain amplitude/phase, temporal covariance uncertainty, spectral tilt, and one shared transfer/seven-layer calibration budget. Optimize `T_sci+T_transfer+T_7cal`, then add source metrology and duty. Toy015 remains premature until that physical marginal-cost audit identifies a source-dependent bottleneck.
