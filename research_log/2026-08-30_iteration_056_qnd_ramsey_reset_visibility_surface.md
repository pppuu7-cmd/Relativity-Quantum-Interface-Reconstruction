# RQIR Research Log — Iteration 056

**Date:** 2026-08-30

## Question

Can the independent QND Ramsey source-metrology channel required by NG-005 be converted from Fisher per accepted copy into a wall-clock rate that includes acceptance, visibility, interaction strength and fresh-source/reset overhead?

## Result

Yes. Define

`R_alpha(phi)=p_E F_alpha(phi,V)/(t_reset+phi/Omega_E)`.

Architecture comparison then depends only on the optimized physical rate. Using the established centered Toy009 D2 source-amplitude costs gives exact crossovers:

- Branch0/best4: `R_alpha=2.1340355145e-4 s^-1`;
- best4/best5: `R_alpha=2.9312161645e-6 s^-1`.

New retained result **RQIR-RESOURCE-026**: source reset/preparation overhead is a first-class Fisher resource. It changes the phase that maximizes Fisher per wall-clock time and can change the preferred D2 branch. Therefore source metrology cannot be summarized by a universal per-copy Fisher or one nominal cycle time.

Monotonic checks: increasing reset overhead does not improve the optimized rate; lowering visibility does not improve it.

## Interpretation discipline

This is a resource/inference result only. It does not alter NG-005, does not establish a realizable gravity experiment, and does not claim new physics. NG-023 remains active: energy-QND source metrology is assigned to independent/sacrificial copies until ordered-response nondemolition is demonstrated.

## Files

- `analysis/qnd_ramsey_reset_visibility_surface_iteration056.py`
- `docs/QND_RAMSEY_RESET_VISIBILITY_SURFACE_ITERATION056.md`
- `recovery/RECOVERY_DELTA_ITERATION_056.md`

## Next

Compare this Ramsey rate surface with the finite-resolution Gaussian QND pointer of Iteration 049 under the same reset/coupling accounting, then take the physical lower envelope before choosing the source-metrology architecture.