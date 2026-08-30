# RQIR Iteration 072 — Toy012 Physical Resource Dominance / Rescue-Factor Gate

**Date:** 2026-08-30  
**Status:** architecture-pruning result under declared shared-kernel assumptions; no apparatus forecast and no new-physics claim.

## 1. Why Iteration 071 cannot be instantiated with old Toy012 gamma numbers

Iteration 071 requested an instantiation of the general D2 Fisher-rate wall-clock closure for Toy012. However, Iterations 062–063 had already shown that the original balanced Toy012 was optimized in an incomplete Euclidean detector metric. Its physical two-band D2 science Fisher and its spectral-tilt-profiled calibration burden are dramatically worse than the old normalized numbers.

Therefore the scientifically admissible Toy012 instantiation is first a **dominance/rescue-factor test**, not a nominal hours forecast.

The Iteration-071 resource closure is

`T_sci = Z^2/R_beta`,

`T_cal = gamma sum_j 1/R_cal,j`,

`T_src = C_prep/R_src`.

When two source designs share the same transfer/PSD/scheduling kernels up to their already-computed source-response/calibration/source-metrology factors, define time ratios relative to Toy009:

`q_s = T_sci,i/T_sci,009`,

`q_c = T_cal,i/T_cal,009`,

`q_p = T_src,i/T_src,009`.

Then, with

`x=T_cal,009/T_sci,009`, `y=T_src,009/T_sci,009`,

the projected auxiliary+science time is

`T_i/T_sci,009 = q_s + q_c x + q_p y`.

Toy009 itself is `1+x+y`.

## 2. Balanced Toy012 is componentwise dominated

Iteration 062 gives the exact physical equal-ASD D2 ratio

`S_eff,012bal/S_eff,009 = 1.9696285538e-8`.

Thus under a common science kernel

`q_s = 1/(1.9696285538e-8) = 5.0770994e7`.

Iteration 063 gives a conservative physical calibration-time factor

`q_c > 4.4e4`

(the executed 900-point scan is around `4.7e4`).

Independent zero-reset Ramsey source metrology remains a valid source-side calculation for the hidden direction:

- Toy009 rate coefficient `0.0025234392`;
- balanced Toy012 `0.002134292844`.

Hence under equal protocol-external acceptance/coupling/reset/visibility,

`q_p = 0.0025234392/0.002134292844 = 1.18233035`.

All three factors exceed unity:

`q_s >> 1`, `q_c >> 1`, `q_p > 1`.

Therefore for every `x>=0`, `y>=0`,

`q_s + q_c x + q_p y > 1+x+y`.

### RQIR-RESOURCE-034 — componentwise resource-dominance pruning

> If a candidate is slower than a baseline on every independently positive resource component of a declared wall-clock factorization, reallocating those resources cannot make the candidate optimal. The candidate may be rescued only by a source-specific transfer/PSD/scheduling change large enough to reverse at least one component ratio.

Balanced Toy012 is therefore removed from the physical D2 Pareto front **within the shared-kernel reference class**. Its exact-locality existence result remains retained.

## 3. Rescue factors quantify what NG-029 would require

RQIR-NG-029 warns that source-dependent detector kernels can invalidate fixed architecture ratios. Iteration 072 turns that warning into quantitative rescue requirements.

If a source-specific apparatus/kernel supplies additional Fisher-rate gains `g_s`, `g_c`, `g_p` relative to the shared-kernel factorization, the effective time ratios are schematically

`q_s/g_s`, `q_c/g_c`, `q_p/g_p`.

Balanced Toy012 therefore needs at least approximately

- **science:** `g_s > 5.08e7` just to match Toy009 science time;
- **calibration:** `g_c > 4.4e4` just to match the conservative Toy009 calibration time;
- **Ramsey source metrology:** `g_p > 1.1823` to match Toy009.

The first two are so large that a future claim that balanced Toy012 is experimentally preferred must explicitly exhibit the source-dependent detector/transduction mechanism producing those gains. They cannot be supplied by re-normalizing Fisher vectors.

## 4. High-response Toy012 is not strictly dominated, but its rescue region is extreme

The aggressive Toy012 point from Iteration 055 has

`S_eff,high/S_eff,009 = 1.2139856294e-4`,

so

`q_s = 8237.3298`.

Iteration 063 gives the conservative calibration lower bound

`q_c > 490`

(the physical scan is around `5.2e2`).

Its Ramsey rate coefficient is modestly **better** than Toy009:

`R_src,high/R_src,009 ~= 1.150503`,

so

`q_p ~= 0.869185`.

Thus this point cannot be rejected by componentwise dominance because it has one resource advantage: source metrology.

But to beat Toy009, even using the optimistic lower calibration factor `q_c=490`, it must satisfy

`8237.3298 + 490 x + 0.869185 y < 1+x+y`.

Therefore

`boxed{y > 62961.68 + 3738.10 x}`.

Even with `x=0`, Toy009 source metrology would need to consume more than about **62,962 Toy009 science times** before the high-response Toy012 Ramsey advantage could compensate its science penalty.

This is an algebraic resource boundary, not an assertion about any real apparatus.

## 5. What is now retained from Toy012

Balanced Toy012 remains valuable for the positive statement

`exact nearest-neighbour locality + rank-24 NP3 null + positive hidden states + ordered-response split`

is possible.

It is **not** retained as a competitive physical D2 architecture after the two-band detector correction.

The high-response Toy012 point is retained only as an extreme source-metrology-favouring Pareto direction, not as a practical baseline.

Toy013 remains the more interesting local branch because it trades a `23.65x` science penalty for a genuine `~8.11x` physical calibration advantage, producing a finite architecture crossover rather than componentwise failure.

## 6. Controls and caveat

This pruning comparison deliberately excludes source-specific control costs from the strict inequality. If control costs are common or Toy012 is no better, the conclusion only strengthens. If a future Toy012 apparatus claims a control advantage large enough to reverse the result, the necessary saving must be included explicitly in the Iteration-071 rate model.

Likewise, if source geometry changes detector transfer functions, PSDs, acceptance or coherence, the rescue gains above must be recomputed from explicit `R_beta`, `R_cal,j`, and `R_src`; this is exactly the discipline required by NG-029.

## 7. Reproducibility

Code:

`analysis/toy012_physical_resource_dominance_iteration072.py`

The script regression-checks the exact Iteration-062 science factors, the Ramsey source-time factors, strict balanced-Toy012 componentwise dominance, and the high-response `y(x)` rescue boundary.

## 8. Next gate

Build a common **physical local-source Pareto audit** for Toy011-response, Toy011-conditioning, Toy012-high and Toy013 using the three axes

1. physical spectral-tilt-profiled science time;
2. physical spectral-tilt-profiled calibration time;
3. independent Ramsey source-metrology time.

First identify dominated candidates without selecting an apparatus; then derive the lower-envelope regions in `(x,y)` for the surviving local sources. This separates the question “best local source” from the unrestricted Toy009 comparison.
