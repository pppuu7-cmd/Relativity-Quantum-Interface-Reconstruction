# RQIR Recovery Delta — Iteration 079

**Date:** 2026-08-30

Paper II scientific scope is closed for the current article architecture.

New retained **RQIR-STAT-001** regression certificate requires: Schur/projection agreement; nuisance-coordinate invariance; calibration monotonicity; exact NG-005 source-amplitude law; NG-006 exposure obstruction for aligned controls; two-band spectral-tilt identity; and the NUM-001 weak-nuisance threshold counterexample.

The explicit threshold counterexample has a nuisance score `(1e-8,0)` exactly aligned with science `(1,0)`: correct profiling gives `F_beta~0`, while deleting its `1e-16` Fisher entry with threshold `1e-12` falsely gives `F_beta=1`.

Code: `analysis/paper12_reference_regression_iteration079.py`.
Document: `docs/PAPER_II_REFERENCE_LIKELIHOOD_CERTIFICATE_ITERATION079.md`.

Physical shots/PSD/SNR/coherence/wall-clock conversion belongs to Paper III and must not be treated as an open Paper-II theorem.
