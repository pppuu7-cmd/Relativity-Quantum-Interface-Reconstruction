# RQIR Recovery Delta — Iteration 056

**Date:** 2026-08-30

Apply after canonical Iteration 055 / Toy012.

## New retained item

**RQIR-RESOURCE-026 — source reset/preparation overhead is a first-class Fisher resource.**

For independent QND Ramsey source metrology use

`R_alpha(phi)=p_E F_alpha(phi,V)/(t_reset+phi/Omega_E)`.

Do not compare branches using Fisher per accepted copy alone.

For the established centered Toy009 D2 source-amplitude closure comparison, physical source-metrology Fisher-rate thresholds are

- Branch0 ↔ best4: `2.1340355145e-4 s^-1`;
- best4 ↔ best5: `2.9312161645e-6 s^-1`.

Use total source-amplitude closure times

`T0=C0/R_alpha`,

`T4=T4_cov+C4/R_alpha`,

`T5=T5_cov`,

with `C0=4.55511`, `C4=0.05006143859980483`, `T4_cov=5.864018521 h`, `T5_cov=10.608109160 h`.

## Mandatory guards

- NG-005 remains active: exact gravitational-null calibration does not self-calibrate hidden source amplitude.
- NG-023 remains active: QND w.r.t. source H is not ordered-response nondemolition.
- Keep source-metrology and detector Fisher coordinates consistent (`alpha`).
- Keep centered covariance rows and exact hard trace+energy elimination.
- These branch-rate thresholds belong to the current Toy009 complementary D2 architecture; Toy012 must be re-profiled before reusing them numerically.

## Reproduction

Run `analysis/qnd_ramsey_reset_visibility_surface_iteration056.py`.

## Next gate

Put the finite-resolution Gaussian QND pointer on the same reset-aware wall-clock resource surface and compare it with Ramsey. In parallel, rebuild the complementary D2 branch on Toy012 before importing Toy009 branch thresholds into the local-source design.