# RQIR Research Log — Iteration 015: Hard-Constraint Fisher Audit

**Date:** 2026-08-29

## Trigger

Iteration 014's next gate required an explicit low-rank drift nuisance Fisher. While constructing it, the existing heterogeneous Fisher implementation was stress-tested for numerical-rank stability.

## Finding

Iterations 013-014 imposed trace/energy as `1e12` soft penalties and profiled with thresholded pseudoinverse. Under strongly heterogeneous `gamma_mean/gamma_cov`, the pseudoinverse silently truncated weak but detector-relevant nuisance directions.

This produced false profiled-information gains.

## Corrective method

Exact trace+energy constraints were eliminated analytically. In the 24-dimensional source-nuisance coordinates, the 2-row fixed-constraint matrix has rank 2. Its exact nullspace gives a 22-dimensional nuisance basis in which all subsequent Fisher matrices are well-conditioned enough to use ordinary solves without an arbitrary huge penalty.

## Numerical corrections

Old q=1 Iteration-013 points under exact constraints:

- D1 retained `F_beta ~=0.5724`, not 0.90;
- D2 retained `F_beta ~=0.4811`, not 0.90.

Corrected q=1 90%-retention optima:

- D1: `gamma_m ~=1.72e6`, `gamma_c ~=0.94e6`, cost `~=3.16e7`, only `~1.07x` cheaper than uniform;
- D2: `gamma_m ~=2.41e6`, `gamma_c ~=0.93e6`, cost `~=4.12e7`, only `~1.14x` cheaper than uniform.

The previously stated `6.3x` and `4.6x` savings are revoked.

Corrected compound-symmetry cost ratios at rho=0.10 are approximately:

- D1 `0.90`;
- D2 `0.91`.

Thus the previous D2 `~2.13x` cost increase is revoked. The general covariance-orientation lesson remains valid.

Drift derivative vectors themselves were unaffected. With corrected allocations, conservative 10%-sigma common-phase bounds become about `5.96e-3` (D1) and `5.03e-3` (D2), equivalent to about `9.5 us` and `8.0 us` at 100 Hz.

## New rule

**RQIR-NUM-001:** constraints declared exact must be analytically eliminated before Fisher profiling; do not emulate them with enormous penalties combined with thresholded pseudoinverses.

## Scope discipline

Unaffected: Toy009/Toy010 exact NP3 construction, positivity, equality residuals, ordered-response split, Iteration-011 geometry, RQIR-NG-005, independent preparation-metrology requirement, scalar uniform-gamma thresholds.

## Files

- `analysis/hard_constraint_fisher_audit_iteration015.py`
- `docs/HARD_CONSTRAINT_FISHER_AUDIT.md`
- this log

## Next gate

Construct the finite-prior low-rank timing/geometry/additive-offset Fisher in the corrected 22-dimensional hard-constrained nuisance basis. Do not reuse revoked Iteration-013/014 heterogeneous numerical optima.
