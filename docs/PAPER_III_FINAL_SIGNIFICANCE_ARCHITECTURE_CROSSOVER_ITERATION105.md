# RQIR Iteration 105 — Final-Significance Toy009/Toy014 Crossover in Compressed Physical Rates

**Date:** 2026-08-30  
**Status:** Paper-III physical architecture-decision theorem. Exact under the declared separable multiplicative source-amplitude model and multiplicative duty; regression slices are not apparatus forecasts.

## 1. Purpose

Iteration 104 removed the ambiguity between raw detector significance and final post-source-profile significance, and showed that source metrology should be optimized jointly with science rather than fixed at 90% retention unless that fraction happens to be rate-optimal.

The next useful step is to ask when Toy014's source-metrology advantage can compensate its detector/calibration disadvantage **for a final significance target**, after both resources are optimally scheduled.

## 2. Compressed physical rate pair

For architecture `i`, suppose the full Iteration-103 detector/transfer/seven-calibration campaign has already been optimized over its internal fractions, leaving an effective raw detector-side Fisher rate

`R_D,i`.

Let the independent source-amplitude metrology campaign supply rate

`R_A,i`.

In the separable local multiplicative-amplitude model, optimal joint science/source scheduling gives

`boxed{R_final,i = 1/[1/sqrt(R_D,i)+1/sqrt(R_A,i)]^2}`.

For final target `F_*=Z_final^2`, pre-duty wall clock is

`T_i=F_*/R_final,i`.

If a uniform control/reference duty fraction `d_i` multiplies all campaigns, the effective wall-clock rate is

`Q_i=(1-d_i) R_final,i`.

Then architecture ranking is simply `Q_i>Q_k`.

This compression is valid only after detector/transfer/calibration nuisance have been consistently absorbed into `R_D`. If source metrology changes the detector-optimal efficient direction, the complete RESOURCE-057 joint matrix problem must be solved instead of using this two-rate compression.

## 3. RQIR-RESOURCE-061 — exact final-significance rate-ratio law

Normalize Toy014 to Toy009 with

`u = R_D,14/R_D,09`,

`v = R_A,14/R_A,09`,

`z = R_A,09/R_D,09`,

`delta = (1-d_14)/(1-d_09)`.

Then

`boxed{Q_14/Q_09 = delta [(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2}`.

Toy014 is faster exactly when this ratio exceeds one.

Unlike the historical fixed `(x,y)` wall-clock boundary, this expression targets the **final profiled significance** and automatically uses the optimal science/source split.

The final target `Z` cancels from the architecture ratio in the local-linear regime; changing `Z` scales both campaign times by `Z^2` without changing which branch is faster.

## 4. Exact crossover in source-dominance coordinate

Let

`w=1/sqrt(z)`,

`A=1/sqrt(u)`,

`B=1/sqrt(v)`.

The equality `Q_14=Q_09` is

`sqrt(delta)(1+w)=A+B w`.

When a positive finite crossing exists,

`boxed{w_cross = [A-sqrt(delta)]/[sqrt(delta)-B]}`

and

`boxed{z_cross = 1/w_cross^2}`.

This is the direct final-significance replacement for the old statement that Toy014 wins only when the Toy009 baseline is sufficiently source-metrology dominated.

## 5. RQIR-DESIGN-012 — source dominance helps exactly according to relative rate ordering

Consider the square-root rate ratio as a function of

`w=1/sqrt(z)`.

Its derivative has a constant sign proportional to

`A-B = 1/sqrt(u)-1/sqrt(v)`.

Therefore:

- if `v>u`, decreasing `z` (making Toy009 more source dominated) monotonically favors Toy014;
- if `v<u`, source domination favors Toy009 instead;
- if `v=u`, the ranking is independent of `z` apart from duty.

This is a useful design diagnostic: a branch should only be called 'source-rescued' if its relative source-rate advantage is stronger than its relative detector-rate performance in the appropriate rate sense.

## 6. RQIR-NG-060 — no source-rescue claim from `q_p` alone

The source-rate ratio `v` by itself does not determine the final architecture winner.

A valid source-rescue claim requires, in the same normalization:

- `u`, the optimized detector+transfer+seven-calibration effective-rate ratio;
- `v`, the robust source-amplitude rate ratio;
- `z`, the baseline source/detector rate balance;
- relative duty `delta`.

Thus the mature Toy014 Ramsey advantage `v~1.49` does not by itself establish a winning region until `R_D,14/R_D,09` is obtained from a common physical apparatus certificate.

This is the final-significance analogue of NG-042/NG-044.

## 7. Repository regression slice — not an apparatus decision

Use only the retained **science-only shared-kernel** Toy014/Toy009 ratio

`u_reg = S_eff,014/S_eff,009 = 0.2830146574583767`

and the zero-reset Ramsey source-rate ratio

`v_reg = 1.4913343179877905`.

This does **not** include the full physical detector+seven-calibration RESOURCE-057 rate and is therefore regression-only.

For equal duty, the exact compressed crossover is

`boxed{z_cross ~= 0.04239396157}`.

Thus, in this limited science-only slice, Toy014 wins only when

`R_A,009/R_D,009 <~ 0.04239`,

i.e. the Toy009 baseline is strongly source-metrology limited.

This reproduces the qualitative content of the historical `y`-large rescue region in a final-significance rate coordinate.

If the illustrative duty values are

- `d_09=0.02`;
- `d_14=0.08`,

then

`delta=0.92/0.98`

and the same regression crossover tightens to

`z_cross ~= 0.02713545519`.

The extra Toy014 duty loss therefore requires an even more source-dominated baseline before its Ramsey advantage can compensate.

These values are algebraic regression slices, not experimental forecasts.

## 8. Relation to NG-030 robust dominance

Iteration 105 is a nominal/compressed exact law. A robust architecture claim still requires interval-safe nonoverlap.

For uncertain `(u,v,z,delta)`, do not rank architectures using central values only. Propagate the joint uncertainty or, preferably, return to RESOURCE-059 with the underlying scenario-specific Fisher-rate matrices.

The compressed law is most useful as:

1. a regression check;
2. a threshold surface for apparatus design;
3. a diagnostic showing which physical rate ratio must be measured next.

## 9. Consequence for Toy015

The present result does not justify Toy015.

The key missing number is now sharply exposed:

`R_D,14/R_D,09`

after full complex transfer calibration, seven physical calibration layers, covariance uncertainty and mandatory detector controls are optimized in the **same apparatus normalization**.

If that measured/derived `u` remains much smaller than the robust source-rate ratio `v`, a source-dominated winning region for Toy014 exists and can be quantified. If the residual limiting coordinate instead belongs to source geometry and can plausibly be improved, Toy015 becomes admissible.

Until then, another source search would be premature.

## 10. Reproducibility

Code:

`analysis/final_significance_architecture_crossover_iteration105.py`

The script verifies the rate compression, exact crossover, monotonic source-dominance direction, final-target `Z^2` scaling cancellation, the shared-kernel science-only regression crossing and a duty-shifted regression crossing.
