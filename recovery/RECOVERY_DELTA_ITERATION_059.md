# RQIR Recovery Delta — Iteration 059

**Date:** 2026-08-30

Apply after v2.8 / Iteration 058.

## Retained results

**RQIR-NG-027 — Toy012 control-floor obstruction**

On the balanced Toy012 complementary D2 branch, full hard rank plus independent source-amplitude metrology do not remove low-rank timing/geometry/additive degeneracies. Without independent control priors, increasing gravitational calibration exposure to `100x` still leaves `F_beta|theta~0.804` for the k4 relational-covariance branch.

**RQIR-CAL-017 — control existence dominates control overexposure**

For a conservative 10%-of-row-noise allocation, the Toy012 branch control targets are approximately

- `sigma(y1)=0.585485` dimensionless;
- `sigma(y_ref)=1.184282`;
- `sigma(delta_tau)=0.00260497`;
- at 100 Hz, `sigma_t=4.14594 us`;
- additive relational/force mean `9.09585e-5`;
- additive centered covariance `7.25572e-5`.

Once these independent references exist, only a small common auxiliary-exposure increase is needed to recover `F_beta|theta=0.90`:

- k4: `lambda~1.00237`;
- k5: `lambda~1.00259`.

Do not reuse the older Toy009 `9.19 us` D2 timing number for Toy012.

## Reproduction

Run `analysis/toy012_branchA_systematics_iteration059.py`.

## Next gate

Enumerate subsets of the **base relational covariance** rows. Iteration 057 varied added force covariance while keeping all eight relational covariance rows. For total wall-clock optimization that common overhead must now be exposed and traded against independent source metrology.
