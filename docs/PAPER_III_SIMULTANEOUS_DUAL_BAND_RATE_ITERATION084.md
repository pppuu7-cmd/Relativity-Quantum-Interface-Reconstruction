# RQIR Iteration 084 — Simultaneous Dual-Band Fisher-Rate Closure

**Date:** 2026-08-30  
**Status:** Paper-III physical-rate closure for a simultaneous two-band detector; no apparatus forecast and no new-physics claim.

## 1. Motivation

Iteration 082 showed that a single narrow resonance with one quoted on-resonance force ASD cannot normalize the RQIR two-band likelihood. Iteration 083 showed that sequential retuning with independently unknown gains also fails unless each setting carries its own gain/relock reference Fisher.

The admissible next branch is therefore a detector that supplies both retained RQIR bands in one simultaneous likelihood: a broadband sensor or a genuinely simultaneous two-mode readout.

A literature check found experimental levitated platforms with simultaneous multi-mode detection and control, including the two-mode coherent-scattering experiment of Piotrowski et al. (*Nature Physics* 19, 1009–1013 (2023), DOI `10.1038/s41567-023-01956-1`), which reports COM modes near 224, 268 and 80 kHz and simultaneous two-mode ground-state cooling. This establishes that simultaneous multi-mode readout is experimentally real. It does **not** provide the required RQIR force PSD/cross-PSD at two science bands separated by an exact factor of two, so no absolute RQIR wall-clock number is inferred from it.

## 2. Two simultaneous band rates

Let the two retained science harmonics have independent whitened information rates

`r2 > 0`, `r4 > 0`.

For simultaneous live time `T`,

`P2 = r2 T`,

`P4 = r4 T`.

The mature spectral-tilt profile law is

`F_beta|tilt = 4 P2 P4/(P2+P4)`.

Therefore the profiled science Fisher remains linear in wall time:

`F_beta|tilt(T) = R_2band T`,

with

`boxed{R_2band = 4 r2 r4/(r2+r4)}`.

This is the physical Fisher-rate counterpart of Protocol 002C.

## 3. RQIR-RESOURCE-038 — simultaneous two-band throughput

The sufficient science-rate quantity for the current two-band/one-relative-tilt likelihood is

`boxed{R_2band = 4 r2 r4/(r2+r4)}`.

Equivalently, if

`H(r2,r4)=2 r2 r4/(r2+r4)`

is the ordinary harmonic mean of the two band rates, then

`R_2band = 2 H(r2,r4)`.

Consequences:

1. if `r2=r4=r`, then `R_2band=2r`, exactly equal to the raw total rate `r2+r4`; balanced whitened bands lose no common-amplitude information to the antisymmetric tilt nuisance;
2. if either band rate vanishes, `R_2band=0`;
3. if one band is arbitrarily stronger than the other, `R_2band -> 4 r_weak`; the weak band remains the bottleneck;
4. increasing only the already-strong band has rapidly diminishing value.

The factor `4 r_weak` in the strong-band limit does not mean the profiled rate exceeds the raw total information: when `r_strong >> r_weak`, the raw total is itself dominated by `r_strong`; the profile geometry discards almost all of that strong-band-only information and leaves a finite amount set by the weak band's ability to break the shape degeneracy.

## 4. Inverse partner-rate requirement

For a required profiled science rate `R_*`, fix one physical band rate `r2`. Solving

`4 r2 r4/(r2+r4) >= R_*`

gives

`boxed{r4 >= R_* r2/(4 r2 - R_*)}`

provided

`4 r2 > R_*`.

If

`4 r2 <= R_*`,

no finite improvement of the other band can reach the target.

### RQIR-NG-035 — single-band ceiling under a free relative spectral tilt

For fixed weak-band rate `r_w`, the maximum two-band profiled rate obtainable by making the other band arbitrarily good is

`boxed{R_2band < 4 r_w}`.

Hence an apparatus target `R_*` requires each science band individually to satisfy

`r_n > R_*/4`.

This is a genuine two-band feasibility floor. It cannot be repaired by unlimited sensitivity in only one band.

## 5. Force-domain normalization

For D2, once a physical force template and equivalent-force PSD are measured at each band, write schematically

`r_n = kappa_PSD |Delta F_n|^2/S_F,n^eq`.

`kappa_PSD` is kept explicit because the exact numerical factor depends on the one-sided/two-sided PSD and complex-quadrature convention used by the likelihood. The repository rule is to fix one convention and validate it against the time-domain likelihood before quoting absolute seconds.

The source-side force harmonics are

`Delta F_n = 2 alpha G m_s m_p G_n/L_0^2`

for the Newtonian reference channel, before any additional detector transfer/output coordinate conversion.

Thus a simultaneous two-band apparatus must supply at minimum

- measured/declared `S_F,2^eq` and `S_F,4^eq` in one convention;
- the two complex transfer functions and acquisition windows;
- any cross-PSD/cross-channel covariance if the modes share readout noise;
- the nuisance columns used to form the final `r2,r4` rather than raw unprofiled SNR alone.

## 6. Target science-rate examples

For science significance target `Z=5`, science-only acquisition satisfies

`T_sci = Z^2/R_2band`.

Therefore the required profiled rates are

- 1 day: `R_2band >= 2.8935185e-4 s^-1`;
- 7 days: `R_2band >= 4.1335979e-5 s^-1`;
- 30 days: `R_2band >= 9.6450617e-6 s^-1`.

If the two physical bands are balanced, each needs half that rate:

- 1 day: `r2=r4 >= 1.4467593e-4 s^-1`;
- 7 days: `>= 2.0667990e-5 s^-1`;
- 30 days: `>= 4.8225309e-6 s^-1`.

These are **science-only Fisher-rate specifications**, not total experiment requirements. Calibration, source metrology and duty remain separate terms in Iterations 077/080.

## 7. Relation to Iterations 077/080

For a simultaneous two-band apparatus, use

`R_beta = R_2band`

after all detector nuisance profiling that belongs inside the science likelihood.

Then the mature total-time certificate remains

`T_total = m [Z^2/R_beta + 7 gamma_mean/H_cal + C_prep/R_src]`.

This makes the role of measured two-band PSD explicit: it supplies the missing absolute `R_beta` scale identified by NG-032.

## 8. External-platform boundary

Current published levitated experiments demonstrate simultaneous multiple mechanical modes and tunable multimode interactions, but the searched literature did not provide one ready-made RQIR-compatible data set containing all of the following together:

1. two simultaneous calibrated force sensitivities at frequencies in exact `2:1` ratio;
2. transfer functions/acquisition windows at both bands;
3. cross-PSD or proof that the two band likelihoods are independent;
4. the seven RQIR calibration-layer Jacobians/rates;
5. independent source-metrology throughput and control duty.

Therefore this iteration retains a parameterized specification rather than fabricating an apparatus forecast.

## 9. Decision

The next apparatus search/design must optimize the **weaker physical band first** until both satisfy the NG-035 floor. Quoting a spectacular single-mode ASD is insufficient.

Once a platform supplies measured `r2,r4`, set `R_beta=R_2band`, then propagate the same apparatus PSD/cross-PSD through all seven calibration layers and source/control resources before applying NG-030 Toy009/Toy014 robust dominance.

## 10. Reproducibility

Run

`python analysis/simultaneous_dual_band_rate_iteration084.py`.

The script verifies time linearity, the balanced limit, the one-band obstruction, the strong-band ceiling, inverse partner-rate law and common PSD scaling.
