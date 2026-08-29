# RQIR Heterogeneous Calibration Fisher Allocation

**Date:** 2026-08-29  
**Iteration:** 013  
**Labels:** `DRV`, `NUM`, `NEG`, `OPEN`

## 1. Question

Iteration 012 showed that the scalar calibration strength `gamma` is not a physical shot count because the NP3 calibration rows are heterogeneous. This iteration replaces one common weight by separate Fisher allocations for:

- 14 gravitational potential-mean settings;
- 8 symmetrized covariance/noise settings.

Trace normalization and mean source-energy metrology are treated as separate, independently strong constraints rather than charged to the gravitational calibration shot budget.

The objective is to minimize a standardized shot-equivalent cost at fixed retained profiled detector information.

## 2. Physical Fisher form

For calibration row vectors `a_i`,

`F_C = sum_i I_i a_i a_i^T`,

where `I_i=N_i I_i^(1)` is the accumulated Fisher information in that measurement setting.

For the two gravitational row classes, define

`gamma_m` = information weight per normalized potential-mean row,

`gamma_c` = information weight per normalized covariance row.

Then

`F_C = F_trace+energy + gamma_m M_m + gamma_c M_c`,

with

`M_m=sum_mean a_i a_i^T`, `M_c=sum_cov a_i a_i^T`.

If single-shot Fisher informations are `q_m` and `q_c`, a standardized repetition cost is

`N_equiv = 14 gamma_m/q_m + 8 gamma_c/q_c`.

This is already more physical than scalar `gamma`, although `q_m,q_c` remain technology-dependent inputs.

## 3. Detector model

The current Iteration-011 balanced Toy009 NP3 geometry is retained. Detector information is built from the real/imaginary quadratures of the two selected harmonics and normalized so detector-only beta information is one.

Both branches are evaluated:

- D1 potential/matter-wave response;
- D2 gradient/force response.

The target is 90% retention of detector-only profiled information after the 24 orthogonal source-state nuisance directions are included.

## 4. Equal per-shot mean/covariance information

Set `q_c/q_m=1`.

### D1

Uniform gravitational-row weighting requires approximately

`gamma_m=gamma_c~1.54e6`.

Its standardized cost is about

`3.38e7` information-shot units.

Optimizing the two row classes gives approximately

`gamma_m~1.82e5`,

`gamma_c~3.49e5`,

with total standardized cost

`~5.35e6`.

Thus the same 90% profiled D1 information can be obtained in this toy covariance model with a cost reduction of approximately

**x6.3**

relative to uniform gravitational-row weighting.

### D2

Uniform weighting requires approximately

`gamma_m=gamma_c~2.14e6`,

with standardized cost `~4.72e7`.

A two-class optimized allocation gives approximately

`gamma_m~1.7e5`,

`gamma_c~1.0e6`,

with cost `~1.03e7`.

The reduction is approximately

**x4.6**.

The D2 optimum spends substantially more information on covariance rows than D1. This is a detector-branch dependence, not a universal property of the source.

## 5. Sensitivity to covariance-shot efficiency

Let `q=q_c/q_m`.

A deterministic logarithmic allocation scan gives the following representative 90%-retention results.

| branch | q | gamma_mean | gamma_cov | optimized standardized cost | gain vs uniform |
|---|---:|---:|---:|---:|---:|
| D1 | 0.1 | ~2.24e5 | ~3.00e5 | ~2.71e7 | ~5.3x |
| D1 | 1 | ~1.82e5 | ~3.49e5 | ~5.35e6 | ~6.3x |
| D1 | 10 | ~6.37e4 | ~1.43e6 | ~2.04e6 | ~11.2x |
| D2 | 0.1 | ~3.39e6 | ~4.03e5 | ~7.97e7 | ~2.5x |
| D2 | 1 | ~1.69e5 | ~9.96e5 | ~1.03e7 | ~4.6x |
| D2 | 10 | ~1.60e5 | ~1.11e6 | ~3.14e6 | ~10.1x |

Interpretation: the allocation shifts strongly when covariance estimation has a different single-shot Fisher efficiency from mean estimation. Therefore a calibration schedule optimized in abstract row-normalized units is not generally optimal in wall-clock time.

## 6. New result — RQIR-CAL-005

### Heterogeneous calibration allocation principle

At fixed detector likelihood and fixed calibration operator set, minimizing experimental resource cost requires allocating Fisher information by the downstream nuisance-projection leverage of each calibration class and by its per-shot information cost.

Equal precision on all calibration observables is generally not resource-optimal.

This is a finite-dimensional design result supported numerically here, not a universal theorem about all gravitational experiments.

## 7. Important negative result

There is no branch-independent optimal calibration schedule.

The D1 and D2 optima differ materially even for the same source and the same NP3 observable set. Therefore one cannot optimize source calibration before choosing the detector branch and declaring the measurement covariance.

This strengthens RQIR-DESIGN-001: the optimization endpoint must be detector-level profiled Fisher per physical resource, not source response, null survival, condition number, or row-normalized Fisher separately.

## 8. What remains unphysical

The present `q_m` and `q_c` are standardized placeholders. A hardware-facing forecast still requires:

- D1 phase-readout variance per shot, contrast loss and dead time;
- D2 force/displacement PSD and mechanical transfer;
- covariance-estimator Fisher information from the actual outcome distribution;
- shared drift/common-mode covariance between calibration settings;
- preparation success probability and reset time;
- independent source-amplitude metrology `C_a`;
- correlations between source preparation and detector calibration.

Thus the numerical gains above are resource-allocation diagnostics, not experimental forecasts.

## 9. Next gate

Introduce an explicit common-mode/drift nuisance and correlated calibration covariance. The immediate question is whether the apparent multi-fold allocation gain survives when repeated settings share a slowly varying amplitude/position/calibration drift. After that, map D1 and D2 to actual seconds using branch-specific per-shot/PSD laws.

## Reproducibility

Code: `analysis/heterogeneous_calibration_allocation_iteration013.py`.
