# RQIR Research Log — Iteration 059

**Date:** 2026-08-30

## Question

Can Toy009 timing/geometry/additive control priors be reused for the balanced Toy012 complementary D2 branch before constructing a total wall-clock budget?

## Result

No. The actual Toy012 relational/direct-force branch must be re-profiled.

Using the branch with 14 relational means + 14 force means and resource-relevant subsets of centered relational covariance, the 10%-per-row control allocation gives

- `sigma(delta y1) ~= 0.585485`;
- `sigma(delta y_ref) ~= 1.184282`;
- `sigma(delta tau) ~= 0.00260497`;
- at 100 Hz, `sigma_t ~= 4.14594 us`;
- relational/direct-force additive mean priors `~9.09585e-5`;
- covariance additive prior `~7.25572e-5`.

The timing target is materially tighter than Toy009's centered D2 value (`~9.19 us`).

Without independent control priors, the k4 branch retains only about `0.556, 0.659, 0.772, 0.804` detector Fisher at exposure scales `1,2,10,100`. Therefore exposure alone cannot reach the 0.90 target.

New retained result **RQIR-NG-027**: Toy012 retains a low-rank control-floor obstruction even after hard-rank completion and independent source-amplitude metrology.

With the declared 10% control priors, only a small global auxiliary-exposure correction is required: k4 `lambda~1.00237`, k5 `~1.00259`.

New retained design rule **RQIR-CAL-017**: independent reference channels are essential, but once they reach the required precision their additional normalized Fisher burden is small.

## Next

For total wall clock, stop treating all eight base relational covariance rows as a free/common constant. Enumerate their subsets and trade phase-referenced covariance trajectories against independent source-metrology Fisher.
