# RQIR Iteration 088 — Uncertainty-Safe Seven-Layer Matrix Calibration

**Date:** 2026-08-30  
**Status:** Paper-III resource/robustness gate; not an apparatus forecast and not a new-physics claim.

## 1. Purpose

Iteration 087 produced an exact interval-robust lower envelope for the two-band science Fisher rate. The next required step from `recovery/CURRENT_FRONT.md` is to propagate the same conservative logic through the seven same-time dual-probe calibration layers used by the mature D2 architecture.

The goal is to convert each uncertain `2x2` matrix Fisher block into:

1. a certified lower calibration Fisher rate `R_cal,j^-`;
2. a guaranteed accepted-cycle / expected-attempt budget;
3. a seven-layer harmonic throughput `H_cal^-`;
4. an upper calibration wall-clock bound suitable for NG-030.

This does not select a detector or insert an invented ASD.

## 2. Physical layer object

For calibration layer `j`, after integration over the declared acquisition window and full output PSD/cross-PSD, let the **Fisher-rate block** in the two row-normalized calibration coordinates be

`F_j = [[a_j,c_j],[c_j,b_j]]`.

For an ordinary positive-definite layer,

`lambda_min(F_j) = (a_j+b_j-sqrt((a_j-b_j)^2+4 c_j^2))/2`.

The robust scalar rate that guarantees information in every direction of that two-row layer is

`R_cal,j = lambda_min(F_j)`.

This is the uncertainty-safe version of the Iteration-069 matrix-PSD requirement. Marginal scalar SNR values alone are insufficient when `c_j` is not known to vanish.

## 3. RQIR-RESOURCE-041 — exact entry-box lower envelope for a PSD-safe layer

Suppose the integrated Fisher-rate entries have independent bounded uncertainty

`a in [a-,a+]`, `b in [b-,b+]`, `c in [c-,c+]`,

and the entire declared box is **PSD-safe**, i.e. every allowed matrix is positive definite.

The map

`F -> lambda_min(F)`

is concave on Hermitian/symmetric matrices. Therefore its minimum over a convex rectangular entry box is attained at an extreme point.

Hence

`boxed{R_cal,j^- = min lambda_min([[a,c],[c,b]])}`

over the eight vertices

`a in {a-,a+}`, `b in {b-,b+}`, `c in {c-,c+}`.

No Monte Carlo search is required for this uncertainty model.

The deterministic regression checks random PSD-safe boxes against 2000 random interior samples each.

## 4. Accepted cycles, attempts and coherence-time bridge

It is often more transparent to separate per-accepted-cycle information from event rate.

Let `I_j` be the per-accepted-cycle `2x2` Fisher block and let

`i_j^- = inf lambda_min(I_j)`.

If the layer must supply isotropic nuisance information `gamma`, then the accepted-cycle requirement is

`boxed{N_acc,j >= gamma/i_j^-}`.

If acceptance is bounded below by `p_j^-`, a sufficient worst-acceptance expected trial budget is

`boxed{N_try,j,required = gamma/(p_j^- i_j^-)}`.

For any true acceptance `p_j>=p_j^-`, the expected number of trials required to accumulate the target accepted information is no larger than this value. This is an expectation-level/Asimov resource conversion; a high-probability binomial completion guarantee would require a declared confidence level and is a separate scheduling layer.

If the cycle duration is bounded above by `t_cyc,j^+`, with the physical requirement

`t_cyc,j >= t_evol,j + t_read/reset,j`

and `t_evol,j` itself respecting the source coherence/evolution span, then

`R_cal,j^- = p_j^- i_j^- / t_cyc,j^+`

and

`boxed{T_cal,j^upper = gamma/R_cal,j^-}`.

Thus shot noise, acceptance, coherence span, read/reset overhead and matrix cross-noise now enter one explicit calibration-rate certificate.

## 5. Seven-layer aggregation

For independently scheduled layers,

`T_cal = gamma sum_{j=1}^7 1/R_cal,j`.

Since this expression is monotonically decreasing in every positive rate, independent lower bounds immediately give the conservative upper wall time

`boxed{T_cal^upper = gamma sum_j 1/R_cal,j^-}`.

Define

`H_cal = 7 / sum_j 1/R_cal,j`.

Then the exact robust harmonic throughput is

`boxed{H_cal^- = 7 / sum_j 1/R_cal,j^-}`

and

`boxed{T_cal^upper = 7 gamma/H_cal^-}`.

This is the uncertainty-safe completion of Iteration 080's calibration compression.

### Scope of exactness

The expression is exact for independent per-layer uncertainty sets that can attain their slow-rate extrema simultaneously. If one common apparatus parameter correlates several layers, inserting all individual minima remains conservative but may not be tight. A joint nuisance/uncertainty model should then replace the Cartesian product.

## 6. RQIR-NG-038 — non-PSD-safe error bars cannot certify a positive calibration rate

Independent error bars on `a,b,c` may describe matrix corners that are not positive semidefinite even though the central fitted Fisher matrix is physical.

In that case a naive entrywise box does **not** certify a positive `lambda_min` over its declared uncertainty set. One must either:

1. use a covariance-aware constrained uncertainty region that preserves PSD;
2. transform to a parameterization that is positive by construction (for example Cholesky/eigenvalue coordinates); or
3. report no positive robust layer-rate lower bound from those error bars.

A nominal positive-definite matrix is therefore not sufficient for NG-030 if its uncertainty representation crosses the PSD boundary.

This is a metrology/uncertainty statement, not a physical instability of the detector itself.

## 7. Transparent deterministic regression

`analysis/seven_layer_robust_calibration_iteration088.py` contains seven synthetic PSD-safe layer boxes solely to verify the algebra. They are **not apparatus measurements**.

The resulting layer rate lower bounds are approximately

- `301.6610 s^-1`;
- `378.6667 s^-1`;
- `358.8235 s^-1`;
- `290.5922 s^-1`;
- `324.3845 s^-1`;
- `346.5774 s^-1`;
- `349.6453 s^-1`.

Their robust harmonic throughput is

`H_cal^- = 333.1410685791254 s^-1`.

The script verifies identically that

`gamma sum_j 1/R_j^- = 7 gamma/H_cal^-`.

For illustration only, inserting the Iteration-074 physical-calibration normalization gives wall times of order

- Toy009 same-normalization `~9.51 h`;
- Toy014 `~33.14 h`;

for this **synthetic rate set**. These numbers are regression examples, not hardware forecasts; their only purpose is to show that the same uncertainty-safe rate vector can be propagated into branch-specific `gamma` costs.

## 8. Consequence for NG-030

The conservative architecture payload can now use

`T_sci^upper = Z^2/R_beta^-`,

`T_cal^upper = gamma sum_j 1/R_cal,j^-`,

`T_src^upper = C_prep/R_src^-`,

and largest allowed control/reference duty `d^+`:

`boxed{T_total^upper = [T_sci^upper+T_cal^upper+T_src^upper]/(1-d^+)}`.

For a lower wall-time bound use the corresponding fastest allowed rates and smallest duty, subject to any common correlated uncertainty model.

A robust Toy009/Toy014 claim still requires

`T_014^upper < T_009^lower`

or the reverse. If the intervals overlap, NG-030 labels the architecture decision unresolved.

## 9. What remains open

The rate algebra needed for the seven calibration layers is now closed under the declared interval model. Still missing for an apparatus-specific comparison are:

- measured/externally sourced two-band science transfer and full spectral matrix;
- the seven physical integrated calibration Fisher blocks and their uncertainty regions;
- independent source-metrology rate including acceptance, visibility, coupling, reset and coherence;
- timing/geometry/additive/gain reference duty and long-timescale stability;
- common uncertainty correlations across these blocks.

The next scientifically useful gate is therefore the **joint robust total-time certificate**: combine Iterations 087 and 088 with a bounded `R_src` and duty to derive a reusable NG-030 branch-comparison function before inserting external apparatus numbers.

## 10. Reproducibility

Run

`python analysis/seven_layer_robust_calibration_iteration088.py`.

The script verifies:

- the analytic `2x2` minimum eigenvalue;
- exact eight-corner lower envelopes for PSD-safe boxes;
- no random interior point below the corner bound;
- seven-layer harmonic-throughput identity;
- accepted-cycle/expected-attempt conversion;
- explicit failure of positive certification for a non-PSD-safe entry box.
