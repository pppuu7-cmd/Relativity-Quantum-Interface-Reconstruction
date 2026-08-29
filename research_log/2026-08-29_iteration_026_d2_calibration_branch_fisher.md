# RQIR Research Log — Iteration 026

**Date:** 2026-08-29

## Target

Following RQIR-NG-009, compare the D2 null-preserving and detector-native calibration branches on one hard-constrained Fisher basis with the hidden-state amplitude restored as an explicit nuisance.

## Work completed

1. Reconstructed the authoritative Toy009 / Iteration-011 calibration and D2 detector transfer.
2. Eliminated trace+energy exactly, leaving a 23D allowed source tangent space.
3. Split that space into the original hidden-amplitude direction plus 22 orthogonal nuisance directions.
4. Compared three calibration operators: original NP3 rows, force-gradient rows replacing potential means, and an augmented potential+force operator.
5. Recomputed exact hard-subspace rank, rotated-null geometry and detector-level profiled `F_beta|theta`.
6. Added regression checks for rank, null overlap/alignment, high-exposure saturation and augmented calibration completion.

## Numerical results

Hard-subspace calibration rank:

- NP3-null: `22/23`;
- native-replace: `22/23`;
- augmented potential+force: `23/23`.

Native-replace new null:

- overlap with old hidden direction `~0.75451`;
- detector alignment with beta signal `~0.97863`.

At corrected D2 Iteration-015 row weights (`gamma_mean=2.414e6`, `gamma_cov=0.929e6`) and no preparation prior:

- NP3-null `F_beta|theta ~ 0`;
- native-replace `~0.03892`;
- augmented `~0.65134`.

Increasing native-replace calibration exposure by orders of magnitude does not cure the problem: `F_beta|theta` saturates near `~0.0423`, because an exact detector-relevant null remains.

The augmented branch has no exact source null. A common calibration-exposure scale of `~4.89` relative to the corrected D2 benchmark reaches `F_beta|theta=0.90` with `C_a=0` in this local Toy009 Fisher model.

## New retained results

**RQIR-NG-010 — nullspace rotation under observable replacement:** detecting the old hidden vector with a new calibration observable is insufficient. Replacing potential means by force-gradient means rotates the exact null rather than eliminating it; the rotated null remains detector relevant.

**RQIR-CAL-009 — complementary-observable completion:** in current Toy009, combining potential-mean and force-gradient calibration rows closes the 23D hard-constrained source tangent space locally and can trade calibration Fisher against independent source-preparation Fisher.

## Consequence

The D2 resource problem has at least three physically distinct protocols and must not use a generic calibration `gamma` without specifying the actual measured observables. In particular, native-force *replacement* is not equivalent to augmented force+potential calibration.

## Scientific status

No new-physics claim. Internal G13 identifiability/calibration result only.

## Files

- `analysis/d2_calibration_branch_fisher_iteration026.py`
- `docs/D2_CALIBRATION_BRANCH_FISHER.md`
- `recovery/RECOVERY_DELTA_ITERATION_026.md`

## Next gate

Attach measurement-level Fisher rates and wall-clock costs to the extra force and potential calibration rows, then optimize the trade between augmented calibration and independent source-preparation QFI metrology under the same D2 PSD/duty/reference assumptions.