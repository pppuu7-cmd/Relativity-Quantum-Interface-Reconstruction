# RQIR Research Log — Iteration 014

**Date:** 2026-08-29  
**Topic:** correlated calibration covariance and slow drift  
**Labels:** `DRV`, `NUM`, `NEG`, `OPEN`

## Starting point

Iteration 013 replaced scalar calibration weight by heterogeneous mean/covariance Fisher allocation. The explicit next gate was non-diagonal calibration covariance and common-mode drift.

## Work performed

1. Reconstructed the current Iteration-011 Toy009 NP3 calibration and D1/D2 detector tangent models.
2. Replaced diagonal mean/covariance noise by class-wise compound-symmetry covariance blocks.
3. Re-optimized `gamma_mean,gamma_cov` at 90% retained detector information.
4. Finite-differenced the exact-null calibration operator with respect to second-probe position and global source phase/time.
5. Derived the first-order multiplicative-gain drift coupling analytically.

## Correlated covariance result

D1 optimized standardized cost relative to uncorrelated:

- rho=0.01: `0.998x`;
- rho=0.05: `0.991x`;
- rho=0.10: `0.986x`.

D2:

- rho=0.01: `1.019x`;
- rho=0.05: `1.191x`;
- rho=0.10: `2.129x`.

Therefore modest common-mode correlation is nearly harmless for D1 in this fixed-marginal covariance model, while D2 is substantially more sensitive.

## New rule

**RQIR-CAL-006 — correlation orientation principle.** Correlated calibration noise cannot be represented by one scalar penalty. Its effect is controlled by alignment of covariance eigendirections with detector-relevant nuisance tangents.

## Drift derivatives

For the exact-null source difference, row-normalized derivative-vector norms are approximately

- second-probe position: `2.91e-4`;
- common source phase/time: `2.56e-2`.

Timing drift is therefore the more important first-order control nuisance in this model.

At the Iteration-013 q=1 allocations, requiring drift residuals below 10% of per-row statistical calibration sigma gives:

- D1: `|delta tau| <~ 1.63e-2`;
- D2: `|delta tau| <~ 9.63e-3`.

Physical conversion `delta t=delta tau/(2 pi f_gap)` gives D1 approximately `26 us` at 100 Hz and D2 approximately `15 us` at 100 Hz; scale inversely with gap frequency.

## Gain-drift negative result / protection

For multiplicative calibration gain `mu=g A theta`, at the exact-null state `A theta0=0`, hence

`d mu / d g = A theta0 = 0`.

**RQIR-DRIFT-001:** purely multiplicative common gain drift is first-order suppressed in the exact-null difference channel. Geometry/time drift is not protected because it generates `(partial A) theta0`.

This is only a local first-order statement. Additive offsets and second-order gain-state coupling remain open.

## Files

- `analysis/correlated_calibration_drift_iteration014.py`
- `docs/CORRELATED_CALIBRATION_COVARIANCE_AND_DRIFT.md`

## Next gate

Promote drift from fixed covariance stress test to explicit low-rank nuisance/Fisher model with finite priors; add additive offsets and second-order gain-state coupling. Then map timing/phase stability to the D1 control clock and D2 sampling/PSD models before converting standardized resource costs to wall-clock seconds.
