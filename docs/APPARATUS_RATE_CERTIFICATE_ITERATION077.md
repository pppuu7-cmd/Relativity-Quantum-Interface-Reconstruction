# RQIR Iteration 077 — Apparatus-Rate Certificate for Toy009/Toy013/Toy014

**Date:** 2026-08-30  
**Status:** resource/identifiability closure only; no apparatus forecast and no new-physics claim.

## 1. Purpose

Iterations 067–071 converted the old abstract preparation/calibration quantities into physical Fisher rates. Iterations 074–076 then left three relevant physical source branches (Toy009 global reference, Toy014 balanced exact-local branch, Toy013 calibration-specialized local branch) and added source-specific timing/control duty.

The remaining question is: what *minimal measured apparatus information* is sufficient to choose among these branches without inventing an absolute ASD?

## 2. Primitive measured inputs

For each source architecture `i`, measure or declare inside one fixed acquisition likelihood:

1. detector-level nuisance-profiled science Fisher rate `R_beta,i`;
2. the seven same-time dual-probe matrix calibration Fisher rates `R_cal,i,j` (`j=1..7`), each obtained from the full 2x2 PSD/cross-PSD block;
3. independent source-amplitude metrology rate `R_src,i`, including fresh-source preparation, reset/readout, acceptance and visibility/coherence losses;
4. timing/reference duty `d_i` (and any separately retained control duty), with `0<=d_i<1`.

No absolute detector ASD is needed *at the architecture-selection stage* once these rates have actually been measured/derived from the declared detector likelihood.

## 3. Compressed apparatus certificate

For fixed significance `Z` and retained multiplicative source-amplitude fraction `r`,

`C_prep = [r/(1-r)] Z^2`.

At the current `Z=5`, `r=0.90` target:

`C_prep = 225`.

Define

`T_sci,i = Z^2/R_beta,i`,

`T_cal,i = gamma_i sum_j 1/R_cal,i,j`,

`T_src,i = C_prep/R_src,i`.

Then

`x_i = T_cal,i/T_sci,i = gamma_i R_beta,i/Z^2 sum_j 1/R_cal,i,j`,

`y_i = T_src,i/T_sci,i = C_prep R_beta,i/(Z^2 R_src,i)`.

Including timing/reference duty as a payload multiplier,

`m_i = 1/(1-d_i)`,

and therefore

`boxed{T_total,i = m_i [Z^2/R_beta,i] [1+x_i+y_i]}`.

### RQIR-RESOURCE-036 — minimal apparatus-rate certificate

> After the full physical likelihood and nuisance profile are fixed, architecture selection among current RQIR branches requires only the compressed certificate `(R_beta, x, y, d)` per branch. The seven calibration rates remain mandatory audit inputs, but their wall-clock contribution compresses to `x` for branch selection.

This is stronger than the Iteration-071 closure because it identifies the exact sufficient resource coordinates for the present architecture decision.

## 4. General pairwise dominance test

Architecture `i` beats `k` iff

`[m_i/R_beta,i] [1+x_i+y_i] < [m_k/R_beta,k] [1+x_k+y_k]`.

Equivalently, defining the measured science-time ratio

`q_s(i/k)=R_beta,k/R_beta,i`,

one needs

`boxed{q_s(i/k) [m_i/m_k] [1+x_i+y_i] < 1+x_k+y_k}`.

This expression does not assume common PSD, common transduction, common bandwidth, common acceptance or common reset. Those effects have already entered the measured rates.

## 5. Regression to the retained shared-kernel projections

The general certificate must reproduce earlier special-case boundaries when the old shared-kernel resource ratios are deliberately inserted.

### Toy014 vs Toy009

Using Iteration-074

`(q_s,q_c,q_p)=(3.53338589945, 3.48482822888, 0.67054046)`,

the zero-control shared-kernel boundary is

`boxed{y > 7.6895205385 + 7.5421347000 x}`.

This exactly reproduces the retained Iteration-074 boundary before Iteration-076 duty correction.

### Toy013 vs Toy014

Using the retained Toy013 factors from Iterations 065–066 and Toy014 factors above gives

`boxed{x > 5.9842386660 + 98.2399220663 y}`

for Toy013 to beat Toy014 in the same shared-kernel projection.

These regressions are checks only; apparatus selection should use measured per-branch certificates, not assume the shared-kernel factors.

## 6. Which apparatus measurement matters most?

Let the no-duty payload be

`P=T_sci+T_cal+T_src`.

Define fractional wall-clock weights

`w_s=T_sci/P`,

`w_c=T_cal/P`,

`w_p=T_src/P`,

with `w_s+w_c+w_p=1`.

For small multiplicative rate errors,

`d ln P / d ln R_beta = -w_s`,

`d ln P / d ln R_src = -w_p`,

and for calibration row `j`,

`d ln P / d ln R_cal,j = -w_cal,j`.

Thus the resource model itself tells us where apparatus characterization effort has the highest leverage: measure most precisely the rate carrying the largest wall-clock weight. This avoids spending detector-development effort on a rate that is already subdominant in total time.

## 7. Robust branch selection under metrology uncertainty

A nominal crossing is not enough. Rate estimates and duty estimates have uncertainty.

For independent bounded uncertainties, define conservative total-time intervals by evaluating the candidate with slowest allowed rates / largest allowed duty for the upper bound and fastest rates / smallest duty for the lower bound.

### RQIR-NG-030 — uncertified near-boundary architecture choice

> If the conservative upper wall-clock bound of one architecture overlaps the lower bound of another, the repository must label the branch decision unresolved. A nominal central-value crossing is not a robust architecture result.

A sufficient robust dominance condition is

`T_i^upper < T_k^lower`.

The accompanying code implements this conservative interval test. A future apparatus model may replace independent bounds with a full correlated uncertainty model.

## 8. Consequence for the next search

The current source-design problem should not automatically launch Toy015. First obtain or derive the certificate `(R_beta,x,y,d)` for Toy009, Toy014 and Toy013 from a concrete detector/source-metrology model.

A new source search is scientifically justified if the certificate shows that total wall clock is dominated by a source-dependent component that source co-design can plausibly improve. If instead detector/control characterization dominates all branches similarly, improving the apparatus model is higher value than another abstract source search.

## 9. Reproducibility

Code:

`analysis/apparatus_certificate_iteration077.py`

The script verifies `C_prep=225`, the Toy014/Toy009 shared-kernel boundary, the Toy013/Toy014 boundary, and supplies a conservative uncertainty-certified dominance function.

## 10. Open gates

RQIR-NG-005 remains active: source amplitude requires independent metrology. NG-006/007 and detector-control floors remain active. Full classical/stochastic/hybrid/full-QFT degeneracy, gauge/conservation/causality/EFT and experimental-measurability gates remain open. No new physics is claimed.
