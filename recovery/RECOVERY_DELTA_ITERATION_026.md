# Recovery Delta — Iteration 026

**Date:** 2026-08-29

## New operational facts

Iteration 025 established that D2 force-gradient calibration sees the old Toy009 hidden direction. Iteration 026 shows this does **not** by itself restore identifiability.

Use exact trace+energy elimination. The allowed source tangent space is 23D. Restore the original hidden-state fractional amplitude as an explicit nuisance before profiling beta.

Three D2 calibration branches now exist:

1. `NP3-null`: original 14 potential means + 8 covariance rows. Hard-subspace rank `22/23`.
2. `native-replace`: 14 force-gradient means replace the 14 potential means, covariance rows retained. Hard-subspace rank `22/23`.
3. `augmented`: potential means + force-gradient means + covariance rows. Hard-subspace rank `23/23`.

For the native-replace branch, the new exact null overlaps the old hidden direction by `~0.75451` and its D2 detector vector aligns with the beta signal by `~0.97863`. Therefore high calibration exposure alone cannot solve the profile degeneracy; `F_beta|theta` saturates near `~0.0423` when `C_a=0`.

At corrected D2 benchmark row weights (`gamma_mean=2.414e6`, `gamma_cov=0.929e6`) and no preparation prior:

- NP3-null: `F_beta|theta ~ 0`;
- native-replace: `~0.03892`;
- augmented: `~0.65134`.

For augmented calibration, scaling all calibration weights by `~4.89` reaches `F_beta|theta=0.90` with `C_a=0` in the local Toy009 model.

## New labels

- **RQIR-NG-010:** observable replacement can rotate an exact null instead of removing it; check the new joint calibration-detector nullspace, not only projection on the old hidden vector.
- **RQIR-CAL-009:** complementary potential+force calibration closes the current 23D hard-constrained Toy009 source tangent space locally and can trade calibration Fisher against source-preparation Fisher.

## Do not do

- Do not claim native-force replacement solves RQIR-NG-005 merely because `G n_old != 0`.
- Do not merge replacement and augmented D2 protocols in one generic `gamma`.
- Do not interpret the `~4.89` exposure factor as an SI-time forecast before measurement-level Fisher rates for the added rows are supplied.

## Reproducibility

- `analysis/d2_calibration_branch_fisher_iteration026.py`
- `docs/D2_CALIBRATION_BRANCH_FISHER.md`
- `research_log/2026-08-29_iteration_026_d2_calibration_branch_fisher.md`

## Next gate

Compare wall-clock cost of NP3-null + source QFI metrology versus native-replace + source metrology versus augmented potential+force calibration, using common D2 force PSD, duty cycle, timing/reference priors and physical row transduction rates.