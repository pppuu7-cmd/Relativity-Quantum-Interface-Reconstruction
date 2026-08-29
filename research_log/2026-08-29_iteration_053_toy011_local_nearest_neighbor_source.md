# RQIR Research Log — Iteration 053 / Toy011

**Date:** 2026-08-29  
**Numbering note:** Iteration 052 is the earlier Ramsey ancilla Fisher-rate budget. Toy011 was discovered concurrently and is authoritatively assigned to Iteration 053.  
**Target:** test whether the Toy009 ordered-response discriminator fundamentally relies on a spatially nonlocal source Hamiltonian.

## Locality audit

In the Toy009 radius eigenbasis, the fixed `H=diag(1,2,3,4,6)` becomes dense. About

`64.46%`

of off-diagonal Frobenius power lies outside nearest-neighbor couplings. Naive nearest-neighbor truncation changes `H` by relative Frobenius `~0.369` and strongly shifts the spectrum.

This gives **RQIR-NG-025 — post-hoc source-locality obstruction**: locality must be imposed during source design, not by truncating a detector-optimized abstract source afterward.

## Toy011 construction

Keep the same five radii and exact spectrum, but generate an exact nearest-neighbor Jacobi-chain Hamiltonian by Lanczos tridiagonalization of `diag(E)` from a positive cyclic vector `q0`.

A deterministic 12000-trial scan (`seed=20260902`) jointly varies local-chain spectral weights, second probe location and calibration phases.

### Response-oriented local point — trial 6304

- `s_min~9.9225e-4`;
- condition `~4702`;
- exact rank `24/25`;
- positive states and equality residual `<2e-16`;
- opposite ordered response retained;
- D1 two-band source proxy `~12.2%` of current Toy009/Iteration011;
- D2 proxy `~15.6%`.

### Conditioning-oriented local point — trial 3811

- `s_min~1.8422e-3`;
- condition `~2540`, close to practical Toy009 (`~2313`);
- D1 proxy `~5.42%` of Toy009;
- D2 proxy `~8.16%`.

## Result

A genuinely local nearest-neighbor five-site source can retain the finite NP3 mean/noise null and nonzero ordered-response split. The discriminator therefore does not intrinsically depend on Toy009's dense source Hamiltonian.

Current local-source Pareto points pay a substantial detector-information penalty.

This gives **RQIR-DESIGN-002**: locality must be co-optimized with calibration and detector Fisher.

## Files

- implementation: `analysis/toy011_local_nearest_neighbor_source.py`;
- canonical iteration wrapper: `analysis/toy011_local_nearest_neighbor_source_iteration053.py`;
- `docs/TOY_MODEL_011_LOCAL_NEAREST_NEIGHBOR_SOURCE.md`;
- `recovery/RECOVERY_DELTA_ITERATION_053.md`.

## Next gate

Run Toy011 through the centered hard-constrained `F_beta|theta` / source-preparation pipeline. Decide whether its lower two-band source information is tolerable after profiling and physical resource conversion.
