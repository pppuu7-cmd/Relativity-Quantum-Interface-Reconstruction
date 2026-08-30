# RQIR Iteration 085 — Correlated Dual-Band Fisher Closure

**Date:** 2026-08-30  
**Status:** Paper-III detector-rate refinement; not an apparatus forecast and not a new-physics claim.

## 1. Purpose

Iteration 084 closed the simultaneous two-band science rate assuming already-whitened independent band rates `r2,r4`. A real simultaneous D2/broadband detector can have nonzero cross-PSD between the two retained matched-filter channels. This iteration derives the exact local profiled Fisher rate in the presence of that correlation.

The goal is to make the next apparatus input explicit: measured/declared `S_F,2`, `S_F,4` and the cross-spectrum must enter before converting a detector into `R_beta`.

## 2. Two-channel local likelihood

After matched filtering/phase choice, represent the two real sufficient channel amplitudes by

`g=(g2,g4)`.

For one unit of live time, let the covariance be

`Sigma=[[s2,c],[c,s4]]`,

where

`c=rho sqrt(s2 s4)`, `|rho|<1`.

The common interface-amplitude score is

`g_beta=(g2,g4)`,

and the retained antisymmetric spectral-tilt nuisance score is

`g_q=(-g2,g4)`.

With `W=Sigma^-1`, the profiled Fisher rate is

`R_beta = g_beta^T W g_beta - (g_beta^T W g_q)^2/(g_q^T W g_q)`.

## 3. RQIR-RESOURCE-039 — exact correlated two-band rate

Direct algebra gives

`boxed{R_beta = 4 g2^2 g4^2 /(s4 g2^2 + 2 c g2 g4 + s2 g4^2)}`.

Define the raw single-band rates

`r2=g2^2/s2`, `r4=g4^2/s4`.

After absorbing channel sign/phase conventions into an effective matched-filter correlation `rho_eff`, the same result becomes

`boxed{R_beta = 4 r2 r4 /(r2+r4+2 rho_eff sqrt(r2 r4))}`.

For `rho_eff=0` this exactly reduces to Iteration 084:

`R_beta=4 r2 r4/(r2+r4)`.

Thus Iteration 084 is the zero-cross-PSD slice of the more general matrix likelihood rather than a separate approximation.

## 4. Balanced-band consequence

For `r2=r4=r`,

`boxed{R_beta = 2 r/(1+rho_eff)}`.

Therefore positive matched-filter correlation between the two same-sign science channels reduces the useful common-amplitude rate after profiling the antisymmetric tilt; negative correlation can improve it.

Examples relative to the independent value `2r`:

- `rho_eff=+0.5` -> `R_beta=1.3333 r`, a one-third loss relative to `2r`;
- `rho_eff=0` -> `R_beta=2r`;
- `rho_eff=-0.5` -> `R_beta=4r`.

The singular limits `|rho_eff|=1` are not ordinary covariance points and must be treated by an explicitly reduced likelihood, not by blindly inverting the matrix.

## 5. RQIR-NG-036 — cross-PSD cannot be omitted from a physical dual-band forecast

Two detectors with identical marginal band PSDs and identical signal amplitudes can have different `R_beta` solely because their cross-PSD differs.

Therefore quoting only `S_F,2` and `S_F,4` is insufficient for a simultaneous two-channel apparatus forecast whenever the two matched-filter outputs share technical, reference, feedback, readout or environmental noise.

A physical Paper-III rate certificate must use the full positive-definite matrix PSD/covariance on the retained channels or demonstrate that the cross term is negligible over the science likelihood.

## 6. NG-035 weak-band ceiling survives correlation

For any fixed finite `|rho_eff|<1`, hold `r2=r_w` and take `r4 -> infinity`. Then

`R_beta -> 4 r_w`.

Hence the Iteration-084 weak-band ceiling is unchanged by finite cross-correlation:

`boxed{R_beta <= 4 r_weak}` in the infinitely strong partner-band limit.

So a target `R_*` still requires

`r2>R_*/4`, `r4>R_*/4`.

Cross-PSD changes the finite-rate trade surface but does not permit a vanishing weak band to be rescued by the other band.

## 7. Inverse balanced specification with correlation

If a design aims for balanced raw band rates and target profiled rate `R_*`, then

`boxed{r >= (1+rho_eff) R_*/2}`.

For positive correlation this is stricter than the independent-band target; for negative correlation it is looser. This statement is only valid when the correlation is physically measured/declared and stable over the campaign.

At `Z=5`, using the Iteration-084 science-only targets:

- 1 day: `R_*=2.8935185e-4 s^-1`;
- 7 days: `R_*=4.1335979e-5 s^-1`;
- 30 days: `R_*=9.6450617e-6 s^-1`.

For example, a balanced detector with `rho_eff=+0.5` requires each raw band rate to be `0.75 R_*`, rather than `0.5 R_*` in the independent case.

## 8. Scope and limitations

This is a two-real-sufficient-channel local Gaussian result. A real complex Fourier/multiquadrature detector should first construct the full real covariance or complex spectral matrix and then reduce it to the declared matched-filter sufficient statistics. Frequency leakage, nonstationarity, cyclostationarity, nuisance-dependent covariance and uncertainty of the PSD estimate remain separate gates.

In particular, this result does not license use of a stationary matrix PSD for the source covariance channels already covered by NG-014/015. It applies to the detector-output science likelihood after its stationarity/matched-filter assumptions are justified.

## 9. Reproducibility

Run

`python analysis/correlated_dual_band_fisher_iteration085.py`.

The deterministic regression checks:

- Schur complement against the closed form over 1000 random positive-definite covariance cases;
- exact reduction to Iteration 084 at zero correlation;
- balanced-band law;
- correlation-independent weak-band ceiling;
- singular-covariance guard at `|rho|=1`.

## 10. Next gate

The apparatus closure vector is now sharper. For a simultaneous D2/broadband candidate, obtain one measured/declared two-band spectral matrix and transfer vector:

`{g2,g4, S_F,2, S_F,4, S_F,24}`

including finite acquisition windows and uncertainty intervals. Convert it through this matrix likelihood into `R_beta`. Then propagate the same spectral/noise model through all seven same-time calibration layers to obtain `R_cal,j`, followed by `R_src`, control duty and NG-030 robust Toy009/Toy014 comparison.
