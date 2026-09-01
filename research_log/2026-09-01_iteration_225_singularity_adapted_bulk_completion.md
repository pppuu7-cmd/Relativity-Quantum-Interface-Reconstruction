# Research log — RQIR Candidate Gravity Iteration 225

Date: 2026-09-01

MODEL_READINESS: 24%

Started from repository authority: `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_224.md`, the latest Iteration-224 research log, recent commits, and Actions state. No active GitHub Actions were present. The authoritative scientific front was Iteration 224.

Iteration 222's Born-fixed source-cut subtraction `R=-8 M_Born` was kept exactly unchanged. Iteration 223's local result that Born-subtracted collinear cap shells vanish as `delta^2` was retained. Iteration 224's global bulk number was not reused because its chart-dependent cap-mask sampling was classified `BLOCKED_NUMERICAL_BULK_HARD_REMAINDER`.

This iteration replaced only the numerical domain decomposition. The sphere was partitioned into exact spherical Voronoi cells around the two certified collinear directions. In each cell, the hard kernel was integrated in local polar coordinates with exact radial boundary `rho_max(phi)=atan2(1-cos(gamma), sin(gamma) cos(phi))`.

Two independent deterministic cubatures were then compared: Gauss-Legendre radial x midpoint azimuth and Gauss-Legendre radial x Gauss-Legendre azimuth.

Across five frozen scattering angles and both linear spin-2 polarizations, the worst order-32 relative disagreement is `2.584334806770234e-7`. The slowest rows are at `theta_ext=2.1`; order-40 stress tests reduce their disagreements to `6.045121421330798e-9` and `6.135670833005235e-9`.

A conservative relative numerical envelope of `3e-7` is therefore frozen for this comparator calculation. Classification: `PASS_NUMERICAL_GLOBAL_COMPLETION`. This resolves the Iteration-224 operational numerical blocker. It is not a consistency FAIL, exact comparator identity, near-degeneracy, regime-specific non-identifiability, or Candidate Gravity novelty.

Retain `NUM-NG-014`, `SRC-CUT-006`, `NG-FUNNEL-081`.

No `ANSATZ-003`. No Fisher/resources. No heavy Actions run was needed or duplicated.

MODEL_READINESS: 24%

Readiness change: +1 percentage point from 23%. The increase is confined to comparator foundation because a previously blocked comparator component, the finite global `MSSC-001` hard remainder, is now numerically completed. Unique residual discovery and all downstream candidate-specific rubric blocks remain zero.

Next gate: extract the source comparator's frozen regular+log/nonanalytic structure from the stable finite hard remainder and compare it with the distinct pure-graviton positive control without identifying the observables. AS/C3 remain BLOCKED and must not be zero-filled.
