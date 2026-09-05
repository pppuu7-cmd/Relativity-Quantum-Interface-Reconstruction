# Recovery Delta — Candidate Gravity Iteration 458

**Date:** 2026-09-05  
**Authority type:** exact central4×central4 precision-budget / promotion-barrier audit; non-promoting  
**Classification:** `PASS_MIXED_DERIVATIVE_PRECISION_BUDGET_FROZEN__NON_PROMOTING`

## Result
The authoritative Iteration-407 implementation forms BASE and HALF mixed auxiliary-mass derivatives separately using tensor-product fourth-order central first derivatives, with coefficients `[1/12,-2/3,+2/3,-1/12]/h`. BASE and HALF are compared by the frozen mass-step criterion; the retained physical quantity is `ds=-d_base`, not a Richardson extrapolation of the two levels.

The first-axis L1 coefficient sum is exactly `3/2`, so the mixed-derivative tensor L1 sum is `9/4`. Therefore the exact sample-error amplification norms are

- BASE `h=5e-6`: `9.0e10`;
- HALF `h=2.5e-6`: `3.6e11`.

A uniform absolute local MP discrepancy sufficient for an assembled absolute discrepancy `<=2e-6` would be `2.2222222222222222e-17` on BASE and `5.5555555555555555e-18` on HALF. Existing local gates instead use a scaled `<=1e-30` discrepancy. Thus local coordinate PASSes are necessary but are not, by logic alone, a derivative-level MP80/120 certificate unless actual sample scales / weighted errors are also propagated.

A prospective post-support contract is now frozen: after all 28 distinct `F(u,v)` coordinates are locally certified, assemble BASE and HALF independently at MP80 and MP120 from the same frozen 32 source occurrences and level-specific weights; require all finite and require each level's scaled MP80↔120 assembled discrepancy `<=2e-6`. Report the weighted error budget `sum |w_ij| |F80-F120|`. The separate BASE↔HALF frozen physical mass-step criterion remains `<=2e-5` and is not replaced.

No `F(u,v)` was evaluated. Active run `33946347229` was still in progress and was not duplicated. Physical index 2 was not promoted.

## Authority retained
Physical/operator authority remains Iteration 411. Physical blocker remains Iteration 421 for double-double index 2 / class 3 / `q^2=-1`. Latest completed numerical mass-support authority remains Iteration 456. Certified occurrence-weighted support coverage remains `4/32 = 12.5%`.

`ANSATZ-003`, exact15 promotion, Fisher/resources, and comparator residual remain blocked.

MODEL_READINESS: 24%

Change: **0 percentage points**. This iteration closes a genuine precision-promotion ambiguity but no stable readiness-rubric component.

## Next gate
Raw-consume run `33946347229` fail-closed at `u=-1e-5, v=+5e-6`. PASS permits only the next Iteration-455 distinct coordinate under unchanged conventions. After all 28 distinct coordinates are locally certified, execute the Iteration-458 assembly-level MP80/120 contract before Iteration-424 physical promotion.
