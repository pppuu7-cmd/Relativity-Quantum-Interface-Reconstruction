# RQIR Research Log — Iteration 085

**Date:** 2026-08-30

## Goal

Advance the active Paper-III apparatus gate after Iteration 084 by replacing the independent-band assumption with the full two-channel covariance needed for simultaneous broadband/two-mode readout.

## Result

For matched-filter science amplitudes `(g2,g4)`, covariance

`Sigma=[[s2,c],[c,s4]]`, `c=rho sqrt(s2 s4)`,

and antisymmetric spectral-tilt score `(-g2,g4)`, exact Schur profiling gives

`R_beta = 4 g2^2 g4^2 /(s4 g2^2 + 2 c g2 g4 + s2 g4^2)`.

Writing raw single-band rates `r2=g2^2/s2`, `r4=g4^2/s4` and absorbing sign/phase convention into `rho_eff`,

`R_beta = 4 r2 r4 /(r2+r4+2 rho_eff sqrt(r2 r4))`.

New **RQIR-RESOURCE-039:** Iteration 084 is the `rho_eff=0` slice of the full matrix likelihood.

New **RQIR-NG-036:** marginal PSDs alone do not determine simultaneous two-band `R_beta`; the cross-PSD/correlation is a first-class apparatus input whenever channels share technical/reference/feedback/environmental noise.

For balanced raw rates,

`R_beta=2r/(1+rho_eff)`.

The Iteration-084 weak-band ceiling survives all finite `|rho_eff|<1`:

`r_partner -> infinity => R_beta -> 4 r_weak`.

## Numerical regression

The deterministic 1000-case positive-definite covariance test found maximum absolute Schur-vs-closed-form discrepancy

`1.0644e-12`,

with exact independent-band, balanced-law and weak-band-limit regressions also passing to the declared tolerances.

## Decision

Do not accept a claimed simultaneous D2/broadband apparatus rate from only two ASD values. Require a full two-band spectral matrix (or a demonstrated negligible cross term), complex transfer/window information and uncertainty intervals before setting `R_beta`.

## Reproduce

`python analysis/correlated_dual_band_fisher_iteration085.py`

## Document

`docs/PAPER_III_CORRELATED_DUAL_BAND_FISHER_ITERATION085.md`
