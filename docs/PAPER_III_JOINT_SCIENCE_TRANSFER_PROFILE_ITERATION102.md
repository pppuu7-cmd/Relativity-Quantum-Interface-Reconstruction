# RQIR Iteration 102 — Joint Science + Injected-Transfer Fisher Profile

**Date:** 2026-08-30  
**Status:** Paper-III detector/calibration Fisher-rate closure; exact local Gaussian result plus transparent balanced wall-clock slice. Not a hardware forecast and not a new-physics claim.

## 1. Purpose

Iteration 101 converted the missing temporal `f,2f` apparatus cut into explicit requirements for covariance certification and same-state two-tone transfer calibration. The next question is how those calibration resources enter the **science likelihood itself** and how much wall time should be assigned to science versus transfer calibration.

A key distinction appears:

- multiplicative transfer amplitude/phase errors enter the science **mean** and can be degenerate with `beta`;
- a covariance-only parameter such as `rho`, in an ordinary Gaussian location/covariance model, is Fisher-orthogonal to a mean parameter at first order.

Therefore these two uncertainty classes must not be treated as the same nuisance block.

## 2. General local transfer-profile formula

Let the science mean derivative for `beta` be a vector `s`. Let `D` map local transfer nuisance coordinates `g` into the mean, and let `W` be the science precision/Fisher metric after the declared science exposure and fixed covariance model.

An independent same-state injection campaign supplies transfer Fisher matrix `C`.

The joint mean-parameter Fisher is

`F = [[s^T W s, s^T W D], [D^T W s, D^T W D + C]]`.

Profiling the transfer coordinates gives

`boxed{F_beta|g = s^T W s - s^T W D (D^T W D + C)^-1 D^T W s}`.

### RQIR-RESOURCE-055 — injected-transfer Schur closure

This formula is the correct bridge from an injected calibration Fisher matrix to retained science Fisher. A transfer error bar should not be appended after the science calculation; its score geometry belongs inside the joint Fisher matrix.

## 3. RQIR-NG-056 — free per-band gains can erase common-amplitude science

For a two-band amplitude measurement at a nonzero fiducial signal, take two independent local fractional gains and `D=diag(s)`. Then the common amplitude direction lies inside the span of the gain columns.

If `C=0`,

`F_beta|g = 0`

(up to numerical precision) whenever the two gain directions span the signal vector.

Thus:

> **RQIR-NG-056:** an otherwise excellent two-band detector cannot identify a common science amplitude if each band has an unconstrained multiplicative transfer gain. Independent same-state transfer calibration, or a lower-dimensional physically constrained gain model, is structurally required.

This is a detector-transduction analogue of the broader RQIR lesson behind NG-005: extra science exposure cannot repair an exact nuisance collinearity.

## 4. Why `rho` is different in the ordinary Gaussian model

For a multivariate Gaussian likelihood with mean `mu(beta,g)` and covariance `Sigma(rho)`, the expected Fisher cross block between a pure mean parameter and a pure covariance parameter is zero:

`F_{beta,rho}=0`.

The reason is the vanishing third central moment of a Gaussian: the mean score is linear in the residual, while the covariance score is quadratic-minus-trace.

### RQIR-STAT-003 — Gaussian mean/covariance Fisher orthogonality

If `rho` enters only the covariance and the Gaussian covariance model is correct, `rho` should **not** be inserted into the same Schur subtraction as a multiplicative mean gain. Instead its uncertainty changes the value/robust lower envelope of the science Fisher metric `W(rho)` and carries a separate characterization-time cost from Iteration 101.

### RQIR-NG-057 — orthogonality is conditional

The orthogonality fails or becomes insufficient when:

- the covariance depends on `beta` or another science mean parameter;
- the likelihood is non-Gaussian;
- finite-window/cyclostationary processing couples mean and covariance estimators;
- transfer or whitening parameters jointly affect both mean and covariance;
- active robust corners switch.

In those cases use the full likelihood Fisher rather than importing the simple Gaussian block separation.

## 5. Exact balanced two-band slice

Consider two symmetric science bands with raw per-band rate `r`, ordinary covariance correlation `rho`, and separate science exposure `T_sci`.

Let a simultaneous two-tone calibration supply each fractional gain with Fisher rate `c` during calibration time `T_cal`, with a diagonal gain-prior block `C=c T_cal I` in the declared basis.

The exact profiled science Fisher is

`boxed{F_beta|g = 2 c r T_cal T_sci / [c T_cal(1+rho) + r T_sci]}`.

Define the perfect-transfer science rate

`R_s = 2r/(1+rho)`

and the effective common transfer-calibration rate

`R_c = 2c`.

Then the result becomes the transparent harmonic law

`boxed{1/F_beta|g = 1/(R_s T_sci) + 1/(R_c T_cal)}`.

This has the correct limits:

- `T_cal -> infinity`: `F -> R_s T_sci`;
- `T_sci -> infinity` at fixed calibration: `F -> R_c T_cal`;
- `T_cal -> 0`: `F -> 0`.

## 6. RQIR-RESOURCE-056 — optimal science/calibration wall-clock split

For a target Fisher `F_*=Z^2`, minimize

`T_total=T_sci+T_cal`

subject to the harmonic constraint above. The exact solution is

`boxed{T_sci/T_cal = sqrt(R_c/R_s)}`

and

`boxed{T_total^min = F_* [1/sqrt(R_s) + 1/sqrt(R_c)]^2}`.

Thus the slower information channel receives more time, but the optimum is not equal Fisher and not equal wall time unless the effective rates happen to match.

This is a two-resource analogue of the characterization water-filling logic from Iteration 097.

## 7. Calibration-speed penalty relative to perfect calibration

With infinitely fast transfer calibration the science-only time is

`T_ideal = F_*/R_s`.

The optimized finite-calibration penalty factor is

`P = T_total^min/T_ideal = [1 + sqrt(R_s/R_c)]^2`.

Therefore a desired maximum overhead `P_max>1` requires

`boxed{R_c/R_s >= 1/[sqrt(P_max)-1]^2}`.

Transparent thresholds:

- total time within 10% of perfect calibration (`P<=1.10`): `R_c/R_s >= 419.76`;
- within 25% (`P<=1.25`): `R_c/R_s >= 71.78`;
- within a factor 2 (`P<=2`): `R_c/R_s >= 5.828`.

These large ratios are not a claim that calibration is impossible. They quantify a simple fact: if calibration consumes separate campaign time and its uncertainty directly limits the science amplitude, making its *total wall-clock overhead* almost negligible requires it to accumulate Fisher much faster than science.

If transfer references can be acquired simultaneously with science without corrupting the weak-signal likelihood, the scheduling model changes and must be rebuilt with the shared likelihood/backaction rules rather than applying this separate-time result.

## 8. Consequence for Iteration 101 targets

Iteration 101 gave separate lower-bound specifications such as

- `rho_hi<=1/9` for 90% robust rate retention in the balanced nominal-zero-correlation slice;
- `N*SNR_inj^2>=1458.80` for a 5.13% common transfer-amplitude confidence bound at the same benchmark.

Iteration 102 shows how to use the **full transfer Fisher** more efficiently: rather than fixing an arbitrary gain-error target first, choose `T_cal` jointly with `T_sci` using RESOURCE-056 (or the general matrix formula), then check robust `rho`/drift/linearity constraints separately.

This prevents over-calibrating one nuisance while another resource dominates total wall time.

## 9. What is closed and what remains open

Closed:

- exact local Schur complement for transfer-gain calibration;
- structural no-go for unconstrained per-band gains;
- Gaussian mean/covariance orthogonality distinction;
- exact balanced correlated science + transfer-calibration Fisher;
- analytic optimal separate-time science/calibration split;
- calibration-rate thresholds for specified total-time overhead.

Open:

- source-specific complex transfer Jacobians for a real apparatus;
- full four-real-component `f,2f` transfer/covariance matrix rather than the balanced scalar slice;
- simultaneous-reference versus separate-reference scheduling;
- seven source/calibration layers in the same apparatus;
- source metrology and control duty;
- absolute Toy009/Toy014 NG-030 dominance.

## 10. Next admissible gate

Extend RESOURCE-055 to the **full complex four-real-component two-band likelihood** with:

1. complex gain amplitude/phase Fisher from dual-tone injection;
2. measured temporal covariance matrix and its uncertainty;
3. science spectral-tilt nuisance;
4. one shared calibration-time budget across both transfer bands and the seven calibration layers.

Then optimize total `T_sci+T_transfer+T_7cal` before adding `T_src` and duty. The resulting marginal-cost ranking will reveal whether detector calibration remains the active bottleneck or whether the frontier can finally return to source-specific design.

## 11. Reproducibility

Code:

`analysis/joint_science_transfer_profile_iteration102.py`

The script verifies the free-gain zero-Fisher gate, the general matrix formula, the exact balanced harmonic reduction, the analytic time optimum against a dense numerical scan, and the calibration-speed overhead thresholds.
