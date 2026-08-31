# Candidate Gravity — Iteration 168: leading massless one-loop C5 TT shape

## Frozen perturbative statement

This iteration is restricted to the Iteration-166/167 eight-row timelike conserved-TT **linear** response block. The C5 comparison is frozen at EH tree plus renormalized local curvature-squared counterterms and the leading one-massless-loop nonlocal curvature-squared effective action,

\[
\Gamma_{1\ell}^{R^2}\supset\int\sqrt{-g}\,[a\,R\log(-\Box/\mu^2)R+b\,R_{\mu\nu}\log(-\Box/\mu^2)R^{\mu\nu}+c\,R_{\mu\nu\rho\sigma}\log(-\Box/\mu^2)R^{\mu\nu\rho\sigma}] .
\]

The local coefficients absorb renormalization-scheme dependence. The timelike discontinuity of the logarithm is independent of the arbitrary positive scale `mu` and of real local counterterms.

Literature basis: Codello & Jain, arXiv:1507.06308, construct the covariant gravitational EFT and its leading nonlocal curvature-squared quantum terms; Calmet, Capozziello & Pryer, EPJC 77 (2017) 589, describe the full second-curvature-order effective action including the three logarithmic structures. Donoghue & El-Menoufi, arXiv:1402.3252, emphasize that massless loops generate the relevant nonlocal logarithmic kernels.

## TT reduction

For the frozen normalized source/detector tensor and `k=(omega,0,0,0)`, the reproducible curvature calculation gives

- `R^(1)=0`;
- `Ricci^(1):Ricci^(1)=s^2/4`;
- `Riemann^(1):Riemann^(1)=s^2`;
- `Weyl^(1):Weyl^(1)=s^2/2`.

The maximum numerical deviations from these identities across all eight rows are respectively `0`, `1.67e-16`, `6.66e-16`, and `3.33e-16`.

Therefore every nonzero curvature-squared logarithmic term contributes a TT 1PI self-energy proportional to

\[
\Sigma_{TT}(s)\propto s^2\log(-s-i0\,\mathrm{sgn}\,\omega).
\]

The linear source response contains two EH propagators, `G0~1/s`, so

\[
\delta\chi^R_{TT}\sim G_0\Sigma_{TT}G_0\propto\log(-s-i0\,\mathrm{sgn}\,\omega).
\]

Hence its frequency-odd imaginary part is constant over all positive `s` rows. Different massless field content or graviton-loop coefficients change only the common coefficient at this frozen order.

## Rank/quotient certificate

The normalized curvature-log shape columns have rank

\[
\boxed{\operatorname{rank}=1}
\]

before profiling. After applying the Iteration-167 seven-dimensional constant-null quotient, the largest projected norm is

\[
\boxed{3.76\times10^{-16}}.
\]

Thus the **complete leading massless one-loop curvature-squared C5 TT absorptive span** is removed by the existing constant profile to machine precision.

Retain:

`C5-NG-005 — LEADING_MASSLESS_ONE_LOOP_TT_ABSORPTIVE_SPAN_IS_ONE_DIMENSIONAL_CONSTANT_SHAPE`.

`ABS-SHAPE-003 — ITERATION167_CONSTANT_QUOTIENT_REMOVES_COMPLETE_LEADING_MASSLESS_ONE_LOOP_CURVATURE_SQUARED_C5_TT_SECTOR`.

## Critical boundary

This is not a claim that the full quantum C5 absorptive response is constant. The following are explicitly **BLOCKED next-order shapes**, not zeros:

- two-loop massless self-energy;
- one-loop graphs containing higher-derivative EFT insertions;
- massive thresholds;
- nonlinear/post-Gaussian source-response completion.

Retain:

`NG-FUNNEL-028 — HIGHER_LOOP_AND_HIGHER_DERIVATIVE_LOOP_SHAPES_ARE_TRUNCATION_UNCERTAINTY_NOT_ZERO_COLUMNS`.

No Candidate Gravity residual is promoted. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden.
