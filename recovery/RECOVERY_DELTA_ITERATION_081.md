# RQIR Recovery Delta — Iteration 081

**Date:** 2026-08-30

Paper III apparatus-completeness audit is now explicit.

New **RQIR-NG-032**: normalized Fisher/resource geometry does not determine absolute seconds. A common detector PSD normalization rescales detector/calibration Fisher rates and absolute time while leaving the dimensionless calibration ratio `x` invariant. A common scaling of all Fisher rates leaves `(x,y,d)` unchanged while rescaling total wall clock.

New **RQIR-APP-001**: minimum apparatus closure requires physical science transfer + full PSD/cross-PSD; seven calibration Jacobians + full matrix PSD/rates; source-metrology acceptance/coupling/visibility/reset/coherence; and low-frequency control/reference stability/duty, all with uncertainty intervals.

Existing `sigma_phi`, force-ASD and unit-transduction examples remain explicitly illustrative and cannot be promoted to apparatus forecasts.

Code: `analysis/apparatus_closure_identifiability_iteration081.py`.
Document: `docs/PAPER_III_APPARATUS_CLOSURE_IDENTIFIABILITY_ITERATION081.md`.

Next gate: construct a declared reference apparatus model from externally sourced/measured platform parameters, or retain a parameterized design envelope. Then compute `R_beta`, seven `R_cal,j`, `R_src`, `d` and NG-030 uncertainty-safe Toy009/Toy014 dominance.
