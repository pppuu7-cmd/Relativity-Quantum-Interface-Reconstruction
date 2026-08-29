# RQIR Toy Model 011 — Local Nearest-Neighbor Source Embedding

**Date:** 2026-08-29  
**Iteration:** 053  
**Status:** finite-dimensional locality-constrained source construction; not a hardware implementation and not a new-physics claim.

> Numbering note: Iteration 052 is the earlier QND Ramsey-ancilla Fisher-rate budget. Toy011 was developed concurrently and is canonically assigned to Iteration 053.

## 1. Motivation

Toy009 is a valid operational finite-dimensional counterexample, but detector-aware optimization did not impose locality of the Hamiltonian in the physical radius/site basis. Toy011 asks whether the finite NP3 mean/noise null and ordered-response split survive when the source is required to have an exactly nearest-neighbour spatial Hamiltonian.

## 2. Locality audit of Toy009

Use the Toy009 radii

`(1.00000,1.60090,1.77911,2.60901,5.90724)`

as eigenvalues of the radius/site operator and transform the fixed spectrum Hamiltonian `H=diag(1,2,3,4,6)` to that basis.

The site-basis Hamiltonian is dense:

- `64.46%` of off-diagonal Frobenius power is beyond nearest neighbours;
- deleting all non-nearest-neighbour terms changes the full Hamiltonian by relative Frobenius `~0.36893`;
- the truncated spectrum becomes approximately `(1.335,2.817,3.430,3.984,4.434)` instead of `(1,2,3,4,6)`.

### RQIR-NG-025 — post-hoc source-locality obstruction

A detector-aware abstract source need not represent a local spatial Hamiltonian. Locality must be imposed during source optimization rather than obtained by truncating long-range couplings after the fact.

This does not invalidate Toy009 as an operational/statistical baseline; it limits a literal local-source interpretation.

## 3. Exact-spectrum local-chain construction

Toy011 keeps the same five radii and exact energy spectrum. Starting from a positive cyclic spectral-weight vector `q0`, Lanczos tridiagonalization of `diag(E)` produces an orthogonal basis `Q` for which

`H_site = Q^T diag(E) Q`

is exactly tridiagonal/nearest-neighbour, while the radius operator is diagonal in the site basis.

The Newtonian probes remain

`B(y)=Q diag(1/|r_i-y|) Q^T`.

Every scanned candidate therefore has simultaneously:

- exact spectrum `(1,2,3,4,6)`;
- diagonal five-site radius operator;
- exactly nearest-neighbour site Hamiltonian;
- the same finite NP3 observable family.

## 4. Joint local-source/calibration scan

A deterministic `12000`-trial scan with seed `20260902` varies:

- local-chain spectral weights `q0`;
- second probe location `y1`;
- six nonzero calibration phases.

Two Pareto-relevant candidates are retained.

### Response-oriented point — trial 6304

`q0≈(0.331914,0.631771,0.260908,0.317702,0.567178)`

`y1≈-5.8641521`

phases

`(0,3.27041685,3.75296867,0.63489295,2.05420608,5.27344622,4.02285984)`.

Results:

- exact rank `24/25`;
- `s_min≈9.92249e-4`;
- condition `≈4701.83`;
- positive hidden states;
- selected equality residual `<2e-16`;
- selected mean and centered noise equal while ordered response changes sign.

Representative harmonics:

- `H2≈-0.00551652-0.00091806i`;
- `H4≈+0.00226998-0.00269397i`;
- `G2≈-0.00788744-0.00161094i`;
- `G4≈+0.00378474-0.00449166i`.

Relative to practical Toy009/Iteration011 two-band source information, this point retains approximately:

- D1 `S_eff`: `12.20%`;
- D2 `S_eff`: `15.58%`.

### Conditioning-oriented point — trial 3811

`q0≈(0.151268,0.598236,0.201050,0.409645,0.641095)`

`y1≈-2.77703786`

phases

`(0,3.58229696,2.69261425,3.36881763,1.53334798,4.76982170,1.05761912)`.

Results:

- `s_min≈1.84219e-3`;
- condition `≈2540.42`, close to practical Toy009 (`~2313`);
- D1 `S_eff≈5.42%` of Toy009;
- D2 `S_eff≈8.16%` of Toy009;
- exact null, state positivity and ordered-response split remain intact.

## 5. Scientific result

Toy011 establishes the finite-dimensional existence result

`finite NP3 mean/noise equality + nonzero ordered-response split + exact nearest-neighbour spatial Hamiltonian`.

Thus the ordered-response discriminator is not intrinsically an artifact of Toy009's dense radius-basis Hamiltonian.

### RQIR-DESIGN-002 — locality belongs inside source/inference co-design

Locality is an active design constraint that competes with calibration conditioning and detector information. Physically meaningful optimization must therefore score locality, calibration geometry and detector Fisher together.

## 6. What remains open

Toy011 is **not** yet promoted over Toy009. The current local Pareto points retain substantially less raw D1/D2 information. The next gate must recompute:

1. centered hard-constrained `F_beta|theta`;
2. source-amplitude QFI and physically accessible energy/Ramsey metrology for the new hidden directions;
3. absolute D1/D2 detector-rate penalty and resulting wall time.

Normalized Fisher geometry and absolute detector sensitivity must be reported separately, because detector normalization can hide the locality-induced signal-rate penalty.

## 7. Reproducibility

- implementation: `analysis/toy011_local_nearest_neighbor_source.py`;
- canonical numbered entry point: `analysis/toy011_local_nearest_neighbor_source_iteration053.py`;
- research log: `research_log/2026-08-29_iteration_053_toy011_local_nearest_neighbor_source.md`;
- recovery delta: `recovery/RECOVERY_DELTA_ITERATION_053.md`.
