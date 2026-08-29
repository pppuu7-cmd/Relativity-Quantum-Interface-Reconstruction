# RQIR Recovery Delta — Iteration 053 / Toy011

**Date:** 2026-08-29

**Numbering:** Iteration 052 is the earlier QND Ramsey-ancilla Fisher-rate budget. Toy011 is Iteration 053.

## New source-locality result

Toy009 remains the operational/statistical baseline, but its literal spatial interpretation has a locality issue. In the sorted radius basis:

- about `64.46%` of off-diagonal Hamiltonian Frobenius power is beyond nearest neighbours;
- simply truncating those couplings changes `H` by relative Frobenius `~0.36893` and strongly shifts the spectrum.

**RQIR-NG-025 — post-hoc source-locality obstruction:** a detector-aware abstract source need not be a local spatial source. Locality must be imposed during source/inference co-design.

## Toy011 construction

Keep the Toy009 radii and exact spectrum `E=(1,2,3,4,6)`, but generate an exact nearest-neighbour Jacobi-chain Hamiltonian through Lanczos tridiagonalization of `diag(E)` from positive spectral weights. The radius operator is diagonal in the site basis.

A deterministic `12000`-trial scan (`seed=20260902`) jointly varies the local-chain spectral weights, second probe position and calibration phases.

### Response-oriented point — trial 6304

- exact rank `24/25`;
- `s_min~9.92249e-4`, condition `~4701.83`;
- positive hidden states, equality residual `<2e-16`;
- nonzero opposite ordered response;
- D1 two-band source proxy `~12.20%` of practical Toy009/Iteration011;
- D2 proxy `~15.58%`.

### Conditioning-oriented point — trial 3811

- `s_min~1.84219e-3`, condition `~2540.42`;
- D1 proxy `~5.42%` of Toy009;
- D2 proxy `~8.16%`.

## Positive conclusion

A finite NP3 mean/noise null with nonzero ordered-response split is compatible with an exactly local nearest-neighbour five-site Hamiltonian. The RQIR discriminator is therefore not intrinsically dependent on Toy009's dense radius-basis Hamiltonian.

**RQIR-DESIGN-002:** locality must be optimized jointly with calibration geometry and detector Fisher.

## Scope

Toy011 is not yet the preferred physical baseline because current local candidates lose substantial raw detector information. It must pass the centered hard-constrained `F_beta|theta` and physical-resource pipeline before promotion.

## Canonical files

- `analysis/toy011_local_nearest_neighbor_source.py` — implementation;
- `analysis/toy011_local_nearest_neighbor_source_iteration053.py` — canonical numbered entry point;
- `docs/TOY_MODEL_011_LOCAL_NEAREST_NEIGHBOR_SOURCE.md`;
- `research_log/2026-08-29_iteration_053_toy011_local_nearest_neighbor_source.md`.

## Next

Recompute centered hard-constrained D1/D2 statistical identifiability and source-metrology QFI for both Toy011 Pareto points. Report normalized nuisance geometry separately from the absolute detector-rate penalty. Do not reuse Toy009 source-QFI or energy-metrology numbers because the Toy011 hidden directions differ.
