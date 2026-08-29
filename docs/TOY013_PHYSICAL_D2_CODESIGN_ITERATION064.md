# RQIR Iteration 064 — Toy013 Physical-D2 Co-design Gate

**Date:** 2026-08-30  
**Status:** reproducible search gate prepared; numerical winner not yet claimed.

Iteration 063 established that the Toy012 D2 calibration advantage was an artifact of optimizing in a Euclidean detector-vector metric and only later profiling the relative two-band spectral-tilt nuisance. RQIR-CAL-019 therefore requires detector nuisance directions to be present inside source/calibration co-design.

Iteration 064 implements the next admissible gate: Toy013 is searched only inside the exact nearest-neighbour Jacobi-chain manifold, with the physical two-band D2 metric

`S_eff = 4 |G2|^2 |G4|^2 / (|G2|^2 + |G4|^2)`

used at the cheap stage. Candidates with a collapsed harmonic are rejected explicitly by a band-balance floor. Conditioning enters only as a secondary score so a large null singular value cannot compensate loss of one detector band.

The expensive survivor audit imports the Iteration-063 full Fisher chain. Each candidate is normalized to unit beta Fisher *after* spectral-tilt profiling, then the centered NP3 mean/covariance calibration allocation is re-optimized while the spectral tilt remains a nuisance.

Exact retained checks for every reported survivor are:

- nearest-neighbour site Hamiltonian, with far-coupling norm < `2e-12`;
- positive hidden pair;
- exact calibration-null residual < `1e-12`;
- regression that tilt-only profiled beta Fisher equals one after normalization.

New design rule **RQIR-DESIGN-005**: a local source search must protect all detector bands that survive nuisance profiling; scalar raw response or Euclidean detector norm is not an admissible proxy when a detector nuisance can rotate away one band.

Reproducible code: `analysis/toy013_physical_d2_codesign_iteration064.py`.

No numerical Toy013 winner is recorded until that deterministic search has actually executed. This prevents an unevaluated candidate from entering the recovery/master chain as a scientific result.
