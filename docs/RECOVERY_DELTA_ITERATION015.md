# RQIR Recovery Delta — Iteration 015

**Date:** 2026-08-29  
**Applies after:** `docs/RECOVERY_GUIDE.md` v1.2

## Critical correction

Do not use the Iteration-013 heterogeneous q=1 optima or the Iteration-014 D2 correlated-covariance cost ratios as authoritative.

The old implementation used `1e12` trace/energy penalties followed by `np.linalg.pinv(..., rcond=1e-12)`. Under heterogeneous calibration weights this truncated real weak nuisance directions and overstated profiled `F_beta`.

Authoritative replacement: `docs/HARD_CONSTRAINT_FISHER_AUDIT.md` and `analysis/hard_constraint_fisher_audit_iteration015.py`.

### Corrected 90% q=1 allocation

- D1: `gamma_m~1.72e6`, `gamma_c~0.94e6`, standardized cost `~3.16e7`, uniform/optimal gain only `~1.07`.
- D2: `gamma_m~2.41e6`, `gamma_c~0.93e6`, standardized cost `~4.12e7`, uniform/optimal gain only `~1.14`.

Old points retain only about `0.572` (D1) and `0.481` (D2) under exact constraints.

### Corrected correlation stress test

For class-wise compound-symmetry rho=0.10, optimized cost ratios are approximately `0.90` (D1) and `0.91` (D2), not a D2 `2.13x` penalty.

### Corrected conservative timing scale

Using corrected allocations and the old 10%-of-statistical-sigma convention:

- D1 `|delta tau| <~5.96e-3` -> `~9.5 us` at 100 Hz;
- D2 `|delta tau| <~5.03e-3` -> `~8.0 us` at 100 Hz.

The derivative norms `||v_y||~2.91e-4`, `||v_tau||~2.56e-2` remain valid.

## New mandatory numerical rule

**RQIR-NUM-001:** declared exact constraints must be eliminated analytically by nullspace/basis reduction before Fisher profiling. Large artificial Fisher penalties must not be combined with thresholded pseudoinverses to stand in for exact constraints.

## Unchanged results

Toy009/Toy010 exact NP3 construction, positivity, equal selected mean/noise, nonzero opposite ordered response, RQIR-NG-005, source-preparation metrology requirement, Iteration-011 geometry, scalar uniform-gamma thresholds, coherence-vs-total-time distinction.

## Exact next step

Build the explicit finite-prior low-rank drift/additive-offset Fisher in the corrected 22D hard-constrained source-nuisance basis. Include timing, second-probe geometry, mean/covariance additive offsets, and only then second-order gain-state coupling.
