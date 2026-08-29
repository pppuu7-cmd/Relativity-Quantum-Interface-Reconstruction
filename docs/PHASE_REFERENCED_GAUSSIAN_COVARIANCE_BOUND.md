# RQIR Iteration 037 — Phase-Referenced Gaussian Covariance Fisher Bound

**Date:** 2026-08-29  
**Scope:** D2 phase-referenced covariance resource gate after Iterations 034–036.  
**Status:** analytic detector-output/resource bound; not an apparatus forecast and not a new-physics claim.

## 1. Purpose

Iteration 035 established that the current Toy009 centered covariance rows are nonstationary and cannot be assigned a stationary scalar PSD rate without an explicit measurement model. The most conservative next model is therefore a repeated phase-referenced detector output

`y ~ N(mu, Sigma(alpha))`

per accepted cycle.

This iteration asks how much Fisher information one such Gaussian output can carry about the fractional hidden-source amplitude `alpha` if `alpha` enters only through the output covariance.

## 2. Affine covariance-only model

Take

`Sigma(alpha)=Sigma0+alpha Sigma1`

with `mu` independent of `alpha` in this calibration channel. Require the same local model to remain physically positive for the complete source-branch interval

`alpha in [-1,1]`.

Define the whitened covariance derivative

`A = Sigma0^(-1/2) Sigma1 Sigma0^(-1/2)`.

Positivity of `Sigma0 +/- Sigma1` implies every eigenvalue `lambda_k(A)` satisfies

`|lambda_k|<1`.

For one real Gaussian sample,

`I_alpha^(shot)=1/2 Tr[(Sigma0^-1 Sigma1)^2]`

and therefore

`I_alpha^(shot)=1/2 sum_k lambda_k^2 < m/2`,

where `m` is the dimension of the detector-output vector.

### RQIR-NG-016 — finite-dimensional affine covariance-only Fisher bound

> If a phase-referenced real Gaussian detector output has dimension `m`, the source coordinate enters only through an affine covariance, and the same affine model is required to remain positive for `alpha in [-1,1]`, then one accepted output sample carries strictly less than `m/2` Fisher information on `alpha`.

This bound already includes any **alpha-independent** detector imprecision or backaction added to `Sigma0`; such noise cannot increase the whitened derivative eigenvalues beyond the positivity limit.

The bound does **not** apply if the detector mean also contains useful alpha information, if diagonal variances/transfer/backaction depend non-affinely on alpha, if the physically allowed alpha interval is narrower, or if a non-Gaussian/collective measurement is used.

## 3. Important special cases

### Scalar variance row

For `m=1`, positivity on the full branch interval gives

`I_alpha^(shot)<1/2`.

### Bivariate covariance/cross-covariance row

For `m=2`,

`I_alpha^(shot)<1`.

The bound is tight in the limiting sense: a whitened derivative with eigenvalues close to `(+1,-1)` approaches one Fisher unit per accepted sample while maintaining positivity at the endpoints only in the strict interior.

## 4. Consequence for the Iteration-035 break-even

The coordinate-correct first-four covariance/preparation condition is

`I_cov^(shot) * (p_C eta_C)/(p_P eta_P) * (t_P/t_C) > 4.4502e4`.

For a minimal **bivariate** covariance-only readout, `I_cov^(shot)<1`. Therefore a necessary condition is

`(p_C eta_C)/(p_P eta_P) * (t_P/t_C) > 4.4502e4`.

At equal acceptance/information efficiency,

`t_P/t_C > 4.4502e4`.

Equivalently, transparent cycle-time ceilings are:

- if one source-metrology cycle takes `t_P=1 s`, covariance cycle must be faster than about `22.47 us`;
- `t_P=100 s` -> `t_C < 2.247 ms`;
- `t_P=10^4 s` -> `t_C < 0.2247 s`.

These are **necessary**, not sufficient, because realistic imprecision/backaction, nuisance profiling and nonideal extraction reduce the attainable Fisher below the positivity ceiling.

For the fifth covariance row, the current product is `~1.0012e6`; a bivariate affine covariance-only measurement would require an equal-efficiency cycle ratio exceeding roughly one million, making that row particularly hard to justify as a wall-clock substitute for source metrology.

## 5. Joint multi-output readout changes the accounting

If one accepted cycle yields an `m`-dimensional output vector containing several covariance channels simultaneously, the covariance-only bound becomes

`I_alpha^(shot)<m/2`.

For an `m=8` joint output the first-four resource product therefore gives only the necessary condition

`t_P/t_C > 1.11255e4`

at equal efficiency.

However, in that case the old resource expression

`T_cov = sum_i gamma_i/q_i`

is no longer the correct accounting object because the same shots contribute jointly to several covariance directions and the row estimates are correlated.

### RQIR-RESOURCE-013 — joint covariance Fisher accounting

> When one phase-referenced detector cycle supplies multiple covariance observables simultaneously, resource optimization must use the full matrix Fisher per cycle and its nuisance-profiled contribution. Independent row times may be summed only for genuinely separate measurement campaigns.

This is the natural extension of RQIR-CAL-012 from row selection to physical shared-shot acquisition.

## 6. Interpretation

The first-four covariance complementarity remains geometrically valuable, but a simple two-channel covariance-only detector cannot make it cheaper than independent source metrology unless covariance samples can be acquired tens of thousands of times faster (after efficiency factors) than source-metrology samples.

This does not rule out the complementary D2 branch. It redirects the design toward one of three possibilities:

1. a high-dimensional joint detector output that estimates several covariance directions per shot;
2. a channel where the same measurement also carries useful mean/response information rather than covariance-only information;
3. a non-Gaussian or explicitly quantum correlation measurement whose Fisher is not described by the affine Gaussian covariance-only bound.

## 7. Reproducibility

Code:

`analysis/phase_referenced_gaussian_covariance_bound_iteration037.py`

The script verifies the positivity/eigenvalue proof numerically, constructs a near-saturating bivariate example, checks scalar and multichannel bounds, and records the current first-four/fifth cycle-ratio thresholds.

## 8. Next gate

Build the **joint-output** D2 likelihood for the four high-value centered covariance rows `(0,1,3,7)` rather than treating their acquisition times as independent. Compute the matrix-valued `Sigma_,u`, include centered mean/timing/additive nuisances and detector imprecision/backaction, and compare the shared-shot profiled Fisher/time directly against coordinate-correct preparation metrology.
