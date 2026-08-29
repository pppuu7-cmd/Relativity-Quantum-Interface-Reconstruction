# D2 Calibration-Branch Fisher Audit — Iteration 026

**Date:** 2026-08-29  
**Scope:** Toy009 / Iteration-011 source geometry, corrected hard trace+energy constraints, D2 detector branch.  
**Status:** detector/calibration consistency result only; no new-physics claim.

## Question

Iteration 025 showed that direct D2 force-gradient calibration detects the old Toy009 hidden direction. The next question is stricter: does detector-native force calibration actually remove the source-amplitude/profile degeneracy that produced RQIR-NG-005, or does it merely rotate the exact nullspace?

A rank comparison alone is insufficient. The hidden-state amplitude must be restored as an explicit nuisance in the same detector-level Fisher problem.

## Common hard-constrained model

Trace and energy are imposed exactly, leaving a 23-dimensional allowed source tangent space. Write local source perturbations as

`delta theta = alpha theta0 + Z_u u`,

where `alpha` is the fractional amplitude of the original hidden state and the 22 columns of `Z_u` span the remaining hard-constrained directions orthogonal to `theta0`.

The normalized D2 detector likelihood has

`d mu / d beta = s`,

`d mu / d alpha = s`,

so beta and source amplitude are detector-collinear before calibration/preparation information is added.

The comparison uses the corrected Iteration-015 D2 row weights

- `gamma_mean = 2.414e6`,
- `gamma_cov = 0.929e6`,

as a common local Fisher benchmark. These are not SI hardware rates.

## Three calibration branches

1. **NP3-null:** original 14 potential-mean rows + 8 covariance rows.
2. **Native-replace:** 14 force-gradient rows replace the 14 potential-mean rows; the 8 covariance rows remain.
3. **Augmented:** original 14 potential-mean rows + 14 force-gradient rows + 8 covariance rows.

All non-fixed rows are row-normalized exactly as in the preceding Toy009 resource layer.

## Exact-rank result

On the 23-dimensional hard trace+energy subspace:

- NP3-null rank = `22/23`;
- native-replace rank = `22/23`;
- augmented rank = `23/23`.

Thus replacing potential rows by force rows does **not** make the calibration complete. It destroys the old exact null but creates a new one-dimensional exact null.

For the native-replace null direction `n_F`:

- `|<n_F,n_old>| ~= 0.75451`;
- the D2 detector response of `n_F` is nonzero;
- its detector vector is aligned with the beta signal at `~0.97863` in cosine magnitude.

So the new null remains almost perfectly detector-relevant.

## Profiled Fisher result

Detector-only beta Fisher is normalized to one. With no independent preparation prior (`C_a=0`) at the corrected Iteration-015 row weights:

- NP3-null: `F_beta|theta ~ 0`;
- native-replace: `F_beta|theta ~ 0.03892`;
- augmented: `F_beta|theta ~ 0.65134`.

The key stress test is to increase all calibration weights while keeping `C_a=0`.

For native-replace, the profiled beta Fisher saturates near only

`F_beta|theta ~ 0.0423`

even when the calibration weights are increased by orders of magnitude. This is the signature of the new exact detector-relevant null.

For the augmented branch, no exact source null remains. Scaling the common calibration exposure by approximately

`lambda_cal ~= 4.89`

relative to the Iteration-015 D2 benchmark raises the calibration-only profiled information to

`F_beta|theta = 0.90`

without an independent preparation prior in this local Toy009 Fisher model.

At the unscaled benchmark, finite preparation information still helps. For native-replace, `C_a ~= 13` (in the present detector-Fisher-normalized fractional-amplitude coordinate) is enough to reach 90% retained information; the precise value is coordinate/rate dependent and must not be confused with the earlier `C_a=225` number quoted for detector SNR 5, where total detector Fisher was 25.

## New retained result

### RQIR-NG-010 — nullspace rotation under observable replacement

Replacing a calibration observable that detects the old hidden direction does not imply source identifiability. In current Toy009 D2, replacing NP3 potential means by detector-native force-gradient means rotates the one-dimensional exact null rather than removing it. The rotated null remains strongly aligned with the detector beta direction, so calibration exposure alone cannot recover the lost Fisher information.

This strengthens RQIR-NG-009: the correct object is the **joint nullspace of the actual calibration operator and detector transfer**, not whether a new row happens to project onto the old hidden vector.

### RQIR-CAL-009 — complementary-observable completion

For the current Toy009 geometry, retaining both potential-mean and force-gradient mean calibration rows closes the 23-dimensional hard-constrained source tangent space (`23/23`) and can, in principle, replace independent hidden-amplitude preparation information at sufficiently high calibration Fisher. This is a local finite-dimensional statement, not a claim of global tomography or experimental feasibility.

## Scientific interpretation

The D2 branch now separates cleanly:

- **null-preserving NP3:** requires independent source preparation metrology because the declared hidden amplitude remains calibration-invisible;
- **native-replace force calibration:** still requires independent information because a new detector-relevant exact null appears;
- **augmented potential+force calibration:** removes the exact source null locally, but costs more calibration channels/exposure and changes the declared calibration grade/protocol.

Therefore D2 resource accounting cannot be based on a single generic `gamma`. It must specify which physical observables are measured and whether they are replacements or complementary rows.

## Reproducibility

Code: `analysis/d2_calibration_branch_fisher_iteration026.py`.

Regression guards verify the native-replace hard-subspace rank, old/new null overlap, detector alignment, high-exposure Fisher saturation and the augmented 90%-retention exposure factor.

## Next gate

The next useful gate is to attach native physical Fisher rates to the **augmented** rows and compare the wall-clock cost of:

1. NP3-null + source-preparation QFI metrology;
2. native-replace + source metrology;
3. augmented potential+force calibration with reduced or zero source-metrology requirement.

The comparison must use the same D2 force PSD, duty cycle, timing/reference priors and corrected hard-constrained profile likelihood.