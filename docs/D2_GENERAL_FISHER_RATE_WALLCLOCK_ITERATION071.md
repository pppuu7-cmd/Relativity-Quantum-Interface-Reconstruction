# RQIR Iteration 071 — General D2 Fisher-Rate Wall-Clock Closure

**Date:** 2026-08-30  
**Status:** retained physical-resource formalization; not an apparatus forecast and not a new-physics claim.

## 1. Source-of-truth front

Iteration 070 supplied a controlled common-PSD/common-schedule reference likelihood and explicitly warned that absolute ASD cancellation is conditional. The next admissible step is therefore to remove that simplification while keeping the result parametric rather than inventing laboratory numbers.

The mature RQIR discipline remains unchanged: detector observability is quantified by profiled `F_beta|theta`; source amplitude is independently calibrated because of RQIR-NG-005; centered-noise and exact-constraint corrections remain mandatory; no toy result closes relativistic/full-QFT/classical/stochastic degeneracy gates.

## 2. General physical rates

Let the science matched-filter Fisher rate for beta after all detector-level profiling be

`R_beta = (p_sci/tau_sci) K_sci,profiled`,

where `K_sci,profiled` contains the physical transfer function, one-sided output/equivalent-force PSD, the D2 source direction and any coherence/visibility attenuation that belongs to the declared science likelihood.

For independent calibration layer `j`, define the worst relevant nuisance-direction Fisher rate

`R_cal,j = (p_j/tau_j) lambda_min[K_cal,j]`,

with

`K_cal,j = 4 Re int J_j^dag(f) S_j^-1(f) J_j(f) df`.

The full `2x2` same-time probe cross-spectrum is retained inside `S_j`; one must not replace it by a sum of scalar SNRs unless the cross terms are negligible.

For independent source metrology define

`R_src = p_src F_src/(t_reset+t_int+t_read)`

or the corresponding optimized continuous-rate expression for the chosen pointer/Ramsey protocol. Visibility and source coherence enter `F_src` or the transfer kernel explicitly.

## 3. Wall-clock closure

For target significance `Z`,

`T_sci = Z^2/R_beta`.

For seven independently acquired D2 mean-calibration layers with common normalized target `gamma_mean`,

`T_cal = gamma_mean sum_j 1/R_cal,j`.

For source-amplitude prior target `C_prep`,

`T_src = C_prep/R_src`.

Therefore the two resource ratios used in the Toy009/Toy013 architecture comparison become exactly

`x = T_cal/T_sci = gamma_mean R_beta/Z^2 sum_j 1/R_cal,j`,

`y = T_src/T_sci = C_prep R_beta/(Z^2 R_src)`.

This is **RQIR-RESOURCE-033 — general Fisher-rate wall-clock closure**. It removes the common-PSD/common-schedule assumption without requiring speculative detector parameters.

The total independent-campaign lower bound is

`T_total/T_sci = 1 + x + y + T_controls/T_sci`,

before any extra covariance campaign, source discard cost or backaction-driven duplication is added.

## 4. Source-preparation target becomes especially simple

For the local multiplicative science structure `mu_D ~ beta alpha_h s`, retaining a fraction `r` of the raw detector Fisher requires

`C_prep = [r/(1-r)] F_bb^raw`.

If the raw science exposure is itself chosen to reach `F_bb^raw=Z^2`, then

`C_prep = [r/(1-r)] Z^2`.

Hence

`boxed{y = [r/(1-r)] R_beta/R_src}`.

For the repeatedly used `r=0.90`,

`C_prep=225` at `Z=5`, and

`boxed{y = 9 R_beta/R_src}`.

This is useful because source-metrology feasibility can now be read directly as a **rate ratio** rather than as an abstract Fisher prior. To keep source metrology below 10% of science time one needs `R_src > 90 R_beta`; to keep it below science time one needs `R_src > 9 R_beta`.

These inequalities are hardware-independent once both rates are computed from explicit likelihoods.

## 5. Regression to Iteration 070

Under the Iteration-070 special assumptions — identical white force PSD, identical science/calibration cycle scheduling, seven equal calibration layers and symmetric two-probe correlation `rho` — the general formula reduces exactly to

`x = 296.184784604 (1+|rho|) r_F^2`

for Toy009 at `Z=5`.

The reproducibility script verifies the prefactor and the `rho=0,0.5,0.9` values from Iteration 070. Thus Iteration 071 is a strict generalization, not a replacement or duplicate calculation.

## 6. Coherence, dead time and shot noise

No separate ad-hoc penalty is needed if the likelihood is declared correctly:

- shot noise / colored detector noise enters `S(f)`;
- finite detector/source coherence enters the signal template or visibility factor;
- acceptance enters `p`;
- dead/read/reset times enter `tau`;
- cross-channel noise enters the matrix PSD;
- profile degeneracies enter `K_sci,profiled`, not a post-hoc SNR multiplier.

This is the physically safe route from `(C_a, gamma)` to repetitions and wall clock.

## 7. New negative guardrail

### RQIR-NG-029 — architecture ratios are not invariant under source-dependent transfer functions

The Toy013/Toy009 time ratios from Iteration 066 may be reused only when the detector transfer, PSD, scheduling and acceptance act on the two source designs through the same declared physical kernels up to the explicitly retained source-response factors. If source geometry changes the transfer function, bandwidth, coherence loss or detector coupling, the old `23.65x` science and calibration/source ratios must be recomputed from `R_beta`, `R_cal,j` and `R_src` for each source.

Thus a normalized source-response ratio is not by itself an apparatus-level wall-clock ratio.

## 8. Next admissible gate

The next highest-value step is to instantiate this general closure for the current leading locality-constrained Toy012 using its own D2 profiled source factor, seven mean-calibration layers, pointer/Ramsey source-metrology rates and the retained 100 Hz timing/coherence benchmark. The result should stay as a multidimensional physical surface unless a repository-backed detector PSD/transduction specification exists. Only after that should Toy012 be compared with Toy009 on one common apparatus budget.
