# RQIR Recovery Delta — Iteration 036

**Date:** 2026-08-29

## Centered-likelihood control revalidation

Iteration 034 invalidated the old raw-second-moment numerical control priors as the preferred RQIR centered-noise benchmark. Iteration 036 recomputes the low-rank timing/geometry/additive systematics on the corrected centered covariance likelihood.

## Structural result retained

**RQIR-NG-006 survives unchanged.**

With no independent control priors, both D1 and D2 `F_beta|theta` remain numerical zero even when centered gravitational calibration exposure is scaled to `100x`.

## Updated first-order centered control priors

D1:

- `sigma(delta tau)~6.94360e-3`;
- `sigma_t~11.0511 us` at 100 Hz;
- `sigma(b_mean)~8.88857e-5`;
- `sigma(b_cov)~1.26818e-4`;
- bundle restores `F_beta|theta~0.899915`.

D2:

- `sigma(delta tau)~5.77425e-3`;
- `sigma_t~9.19001 us`;
- `sigma(b_mean)~7.39168e-5`;
- `sigma(b_cov)~1.30175e-4`;
- bundle restores `F_beta|theta~0.899893`.

The old `9.47 us` D1 and `8.01 us` D2 numbers are retained only as raw-second-moment historical benchmarks.

## Updated raw centered-offset ranges

D1:

- mean `3.396e-5..1.219e-4`;
- centered covariance `7.750e-6..8.109e-5`.

D2:

- mean `2.824e-5..1.014e-4`;
- centered covariance `7.955e-6..8.323e-5`.

SI conversion still requires physical row transduction.

## Updated transparent timing-drift benchmark

With `sigma_event=10 us`, `sigma_ref=target/3`, acceptance `0.5`, current coherence floor and `1 ms` dead time:

- reference blocks: D1 `~0.131812 s`, D2 `~0.190604 s`;
- `D=100 us^2/h`: D1 `~2.17114 h`, D2 `~1.50145 h`;
- `D=1000 us^2/h`: D1 `~13.03 min`, D2 `~9.01 min`;
- equal-diffusion D2/D1 cadence ratio `~0.69155`.

RQIR-NG-007 remains valid.

## Reproducibility

- `analysis/centered_systematics_revalidation_iteration036.py`
- `docs/CENTERED_SYSTEMATICS_REVALIDATION.md`
- `research_log/2026-08-29_iteration_036_centered_systematics_revalidation.md`

## Next action

Proceed with the Iteration-035 phase-referenced covariance detector-output likelihood for high-value rows `(0,1,3,7)`, now using the centered timing/additive control coordinates above.
