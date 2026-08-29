# RQIR Iteration 036 — Centered-Likelihood Systematics Revalidation

**Date:** 2026-08-29  
**Scope:** Toy009/Iteration-011 D1/D2 control nuisance layer after Iteration-034 centered-noise correction.  
**Status:** corrected resource/control benchmark; no new-physics claim.

## 1. Purpose

Iteration 034 changed the preferred finite-noise covariance observable from raw symmetrized second moments to the derivative of the centered symmetrized noise kernel. That correction changed the normalized D1/D2 calibration row weights and therefore invalidated the old Iteration-016 numerical timing/additive priors as current centered-likelihood requirements.

This iteration reruns the same low-rank systematics logic on the corrected centered likelihood.

The four explicit calibration-systematics coordinates remain:

- second-probe position drift `delta y`;
- common source phase/time drift `delta tau`;
- common normalized mean offset `b_mean`;
- common normalized centered-covariance offset `b_cov`.

Trace and energy are still eliminated exactly.

## 2. Centered baseline used

Iteration-034 preferred normalized 90%-retention row weights:

### D1

`gamma_mean ~= 1.265715e6`,

`gamma_cov ~= 0.621783e6`.

### D2

`gamma_mean ~= 1.830265e6`,

`gamma_cov ~= 0.590127e6`.

The covariance drift vectors are recomputed from the **centered** covariance derivative rows, not reused from the old raw-second-moment model.

## 3. RQIR-NG-006 survives the correction

With all four control priors removed, the profiled detector Fisher remains numerically zero for both branches even when the gravitational calibration exposure is increased by factors

`1, 2, 10, 100`.

The residual numerical values remain at the `~1e-9` level or below.

Thus the central structural statement survives unchanged:

> More calibration exposure cannot cure a nuisance direction that is structurally degenerate with detector-relevant source variation when that control nuisance itself is unconstrained.

Iteration 034 therefore did not turn the old NG-006 into a numerical artifact.

## 4. Updated first-order control priors

Using the same conservative “10% of one-row statistical sigma” construction as Iteration 016, the centered-likelihood control bundle is:

### D1

- `sigma(delta y) ~= 0.550773` in the current dimensionless geometry coordinate;
- `sigma(delta tau) ~= 6.94360e-3`;
- at a 100-Hz gap, `sigma_t ~= 11.0511 us`;
- `sigma(b_mean) ~= 8.88857e-5`;
- `sigma(b_cov) ~= 1.26818e-4`.

The resulting profiled information is

`F_beta|theta ~= 0.899915`.

### D2

- `sigma(delta y) ~= 0.458019`;
- `sigma(delta tau) ~= 5.77425e-3`;
- at 100 Hz, `sigma_t ~= 9.19001 us`;
- `sigma(b_mean) ~= 7.39168e-5`;
- `sigma(b_cov) ~= 1.30175e-4`.

The resulting profiled information is

`F_beta|theta ~= 0.899893`.

These replace the old `9.47 us` D1 and `8.01 us` D2 timing numbers as the preferred first-order **centered-likelihood** benchmark.

The change is modest and in the less demanding direction, but it is conceptually important because the control coordinate now matches the actual RQIR centered-noise observable.

## 5. Updated raw centered-offset map

Undoing row normalization with the centered raw row norms gives the following one-sigma Toy-unit offset ranges.

### D1

Mean rows:

`3.396e-5` to `1.219e-4` raw mean units.

Centered covariance rows:

`7.750e-6` to `8.109e-5` raw centered-covariance units.

### D2

Mean rows:

`2.824e-5` to `1.014e-4` raw mean units.

Centered covariance rows:

`7.955e-6` to `8.323e-5` raw centered-covariance units.

As before, an SI tolerance still requires the physical row-specific readout Jacobian. RQIR-CAL-008 and RQIR-NG-008 remain unchanged.

## 6. Updated timing-reference benchmark

Retain the transparent Iteration-023 assumptions only as a benchmark:

- gap frequency `100 Hz`;
- event timing precision `10 us`;
- immediate reference target `sigma_ref=sigma_target/3`;
- acceptance `0.5`;
- dead time `1 ms`;
- coherent shot duration fixed by the current largest stored phase.

The centered timing targets imply reference blocks of approximately

- D1: `0.131812 s`;
- D2: `0.190604 s`.

These remain much shorter than long campaign durations. As before, white timing statistics are not the main long-run gate; colored/common-mode drift is.

## 7. Updated random-walk cadence illustration

With zero irreducible floor and the same

`<sigma^2> = sigma_ref^2 + D Delta/2`

benchmark:

### `D=100 us^2/h`

- D1 cadence: `~2.17114 h`;
- D2 cadence: `~1.50145 h`.

### `D=1000 us^2/h`

- D1 cadence: `~13.03 min`;
- D2 cadence: `~9.01 min`.

For equal diffusion coefficient,

`Delta_D2/Delta_D1 ~= 0.69155`.

The RQIR-NG-007 stability-floor obstruction remains unchanged: if the irreducible floor plus immediate reference variance already exceeds the required target variance, no cadence can repair the problem.

## 8. What remains open

This revalidation closes the first-order control-prior mismatch introduced by Iteration 034, but it does not yet redo every downstream nonlinear calculation.

Still to revalidate if needed for a final apparatus forecast:

- Iteration-017 second-order timing/gain bias at the new centered priors;
- a hardware-specific differential TDEV/phase-noise curve;
- physical SI additive/gain references for the centered covariance statistic.

These are not currently the dominant D2 covariance-rate gate.

## 9. Reproducibility

Code:

`analysis/centered_systematics_revalidation_iteration036.py`

The script recomputes centered drift vectors, verifies the 100x no-prior collapse, derives the updated D1/D2 priors, undoes row normalization, and re-evaluates the transparent colored-drift cadence benchmark.

## 10. Next gate

Return to the D2 covariance measurement problem from Iteration 035: construct a phase-referenced detector-output likelihood for the high-value covariance rows `(0,1,3,7)`, with imprecision/backaction and mean nuisances included in the same Fisher matrix. The centered timing priors above can then be inserted without reusing the obsolete raw-covariance control coordinates.
