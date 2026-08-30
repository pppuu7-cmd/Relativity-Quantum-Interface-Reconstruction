# RQIR Iteration 099 — Primitive Apparatus Characterization Certificate

**Date:** 2026-08-30  
**Status:** Paper-III apparatus-closure audit; no hardware forecast and no new-physics claim.

## 1. Purpose

Iterations 094–097 derived how uncertainty should be characterized and how finite characterization time should be allocated. Iteration 098 converted the independent source-amplitude Fisher requirement into real source-copy counts. The next required step is to state exactly which quantities must be supplied by one common apparatus before the Toy009/Toy014 robust architecture comparison is numerically meaningful.

The certificate deliberately separates:

1. repository-backed source/model quantities;
2. relative design ratios that are useful only as regression summaries;
3. apparatus-measured quantities that must share one physical normalization.

## 2. Repository-backed source/model entries already available

Toy009:

- zero-reset Ramsey rate-optimal phase `phi_009 ~= 1.09231`;
- zero-reset normalized rate coefficient `q_009=0.0025234392`;
- centered D2 `gamma_mean=1.830264703e6`;
- centered D2 `gamma_cov=5.901272925e5`;
- full source `F_Q^alpha=0.0849323916`;
- energy-population Fisher `F_E^alpha=0.0093918844`;
- 100-Hz maximum stored source-evolution benchmark `~7.94319 ms`.

Toy014:

- zero-reset Ramsey rate-optimal phase `phi_014=0.9264295097660072`;
- zero-reset normalized rate coefficient `q_014=0.0037632915041337926`;
- `gamma_mean~=5.6776851e6`;
- `gamma_cov~=2.7186736e6`;
- full source `F_Q^alpha~=0.1015944563`;
- energy-population Fisher `F_E^alpha~=0.01532342451`;
- 100-Hz maximum stored source-evolution benchmark `~6.81327 ms`.

The retained shared-kernel ratios `q_s,q_c,q_p` remain useful regression summaries but are not sufficient statistics for robust absolute apparatus dominance (NG-044).

## 3. Minimum primitive certificate

For each architecture `i in {009,014}`, the common-normalization detector/science layer must supply

`(a2_i, a4_i, rho_i)`

with uncertainties/covariances. These define

`s_i = 4 a2_i a4_i/(a2_i+a4_i+2 rho_i sqrt(a2_i a4_i))`.

The seven calibration layers must supply either their full physical `2x2` Fisher blocks or certified robust rates

`k_i1,...,k_i7`,

where each `k_ij=lambda_min(F_ij)` in the Iteration-088 convention.

With the already source-specific `gamma_i`, these give

`A_i = Z^2/s_i + gamma_i sum_j 1/k_ij`.

The same declared apparatus family must also supply the absolute detector/calibration throughput scale `R0`.

The source apparatus must supply

`(p_E, Omega_E, t_reset, V)`

with uncertainty/correlation, giving

`R_src,i = p_E Omega_E q_i(V,Omega_E t_reset)`.

Finally each architecture requires a control/duty interval `d_i` consistent with timing, geometry, additive/gain recertification and campaign scheduling.

For characterization-time optimization every active primitive additionally needs

`(uncertainty width/covariance, R_char, irreducible floor, characterization duty/cost)`.

## 4. RQIR-APP-003 — common-normalization certificate cut

A robust absolute RESOURCE-045 / NG-030 architecture decision is numerically closed only after the following dependency cuts are closed for both Toy009 and Toy014:

1. **science spectral cut:** `a2,a4,rho`;
2. **seven-layer calibration cut:** `k1...k7` or equivalent full Fisher blocks;
3. **absolute common detector scale:** `R0`;
4. **source-throughput cut:** `p_E,Omega_E,t_reset,V` or a directly measured robust `R_src` interval;
5. **control/duty cut:** `d`;
6. **characterization-cost cut** if RESOURCE-050 is to choose a physical measurement schedule: `R_char`, floors and correlations.

Closing only source-model quantities does not close an apparatus cut. Closing a subsystem in a different experiment does not close the common-normalization cut (NG-040).

## 5. Current certificate status

The current repository is rich in source/model information but deliberately incomplete in absolute apparatus information.

Current status:

- source-model Ramsey shape/coefficient: **available**;
- source Fisher target and accepted-copy budget: **available**;
- source-specific gamma values: **available**;
- relative Toy014/Toy009 science/calibration/source factors: **available as regression slices**;
- common-apparatus `a2,a4,rho`: **not yet measured/specified**;
- seven absolute physical `k_j` rates for both architectures: **not yet measured/specified**;
- common `R0`: **not yet measured/specified**;
- measured `p_E,Omega_E,t_reset,V` uncertainty envelopes in the same apparatus: **not yet supplied**;
- robust campaign duty/correlation envelope: **not yet supplied**;
- primitive `R_char` and systematic floors needed by RESOURCE-050: **not yet supplied**.

Therefore the present front remains **data-underdetermined, not algebra-underdetermined** for an absolute Toy009/Toy014 NG-030 winner.

## 6. RQIR-NG-052 — a complete source model does not imply a complete experiment certificate

Even when `q_i`, `gamma_i`, source QFI and coherence/evolution constraints are known exactly inside the toy model, an absolute wall-clock architecture decision cannot be inferred without a common detector/calibration normalization and physical source/control throughput.

This is stronger than merely saying that an ASD is missing: the missing object is a joint apparatus likelihood/certificate linking all required rates and their uncertainties.

No amount of re-optimizing the already-known source coefficients closes that missing experimental cut.

## 7. Consequence for Toy015

The current incompleteness does **not** justify another source search. The unresolved cuts are mostly apparatus-characterization cuts, not demonstrated source-geometry bottlenecks.

Toy015 remains inadmissible until the primitive certificate is populated enough for RESOURCE-050/RESOURCE-045 to show that the dominant residual wall-clock or decision uncertainty is genuinely source-dependent and plausibly improvable by source redesign.

## 8. Reproducibility

Run

`python analysis/primitive_certificate_iteration099.py`.

The script encodes the minimum certificate schema, keeps repository-backed source-model quantities separate from apparatus quantities, and fails the current absolute-decision readiness check until every required common-normalization cut is supplied (or replaced by an explicitly certified aggregate interval).
