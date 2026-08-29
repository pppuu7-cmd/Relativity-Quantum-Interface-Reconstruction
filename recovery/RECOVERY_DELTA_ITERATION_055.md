# RQIR Recovery Delta — Iteration 055

**Date:** 2026-08-30

Apply this after the current v2.6 recovery guide and Iterations 053–054.

## New retained item

**RQIR-RESOURCE-026 — source reset/preparation overhead is a first-class Fisher resource.**

For independent QND Ramsey source metrology use

`R_alpha(phi)=p_E F_alpha(phi,V)/(t_reset+phi/Omega_E)`.

Do not compare branches using Fisher per accepted copy alone.

Centered D2 physical source-metrology Fisher-rate thresholds:

- Branch0 ↔ best4: `2.1340355145e-4 s^-1`;
- best4 ↔ best5: `2.9312161645e-6 s^-1`.

Use total source-amplitude closure times

`T0=C0/R_alpha`,
`T4=T4_cov+C4/R_alpha`,
`T5=T5_cov`,

with `C0=4.55511`, `C4=0.05006143859980483`, `T4_cov=5.864018521 h`, `T5_cov=10.608109160 h`.

## Still mandatory

- NG-005 remains active: exact gravitational-null calibration does not self-calibrate hidden source amplitude.
- NG-023 remains active: QND w.r.t. source H is not ordered-response nondemolition.
- Keep source-metrology and detector Fisher coordinates consistent (`alpha`, not the old untransformed amplitude `a`).
- Keep centered covariance rows and exact hard trace+energy elimination.

## Reproduction

Run `analysis/qnd_ramsey_reset_visibility_surface_iteration055.py`.

## Next gate

Put Iteration-049 finite-resolution Gaussian QND pointer on the same wall-clock resource surface and compare it directly with Ramsey. Do not freeze an apparatus until the lower envelope is known.
