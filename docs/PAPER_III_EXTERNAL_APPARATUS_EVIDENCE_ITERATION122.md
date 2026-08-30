# RQIR Iteration 122 — External Same-Apparatus Evidence Audit

**Date:** 2026-08-31  
**Status:** Paper-III external apparatus/literature gate. No apparatus forecast and no new-physics claim.

## 1. Purpose

Iteration 121 reduced the remaining detector-side uncertainty to physical Fisher-rate inputs. This iteration asks whether published levitated-optomechanics experiments already provide enough same-apparatus information to populate those inputs without inventing numbers.

The answer is mixed:

- several individual ingredients now exist experimentally;
- exact `f:2f` simultaneous mechanical-mode operation exists as a platform class by 2026;
- calibrated transfer/sensitivity spectra and cross-spectral multimode readout also exist;
- but the audited literature does **not** provide the complete RQIR same-apparatus Fisher input vector needed for a numerical robust `u`.

This is a literature-scope conclusion, not a claim that no unpublished/raw dataset could contain the missing information.

## 2. Audited experimental ingredients

### Pontin et al., Physical Review Research 5, 013013 (2023)

DOI `10.1103/PhysRevResearch.5.013013`.

The experiment measures two mechanical PSDs and their cross-correlation spectrum `S_xy(omega)` while controlling cavity-induced mode rotation. The published analysis reports 10-s traces at pressure `3e-3 mbar` for the relevant scans. It establishes that simultaneous two-mode spectral/cross-spectral acquisition and mode-orientation control are experimentally real.

It does not publish the RQIR exact `f:2f` force-calibrated four-real transfer Fisher matrix, the seven RQIR mean-layer rates, or the eight centered-covariance calibration rates.

### Fu et al., Optics and Lasers in Engineering 152, 106957 (2022)

DOI `10.1016/j.optlaseng.2022.106957`.

This work explicitly calibrates a levitated force-detection sensitivity spectrum using a harmonic Coulomb force and a measured transfer function. It reports a thermal-noise-limit force sensitivity `(4.39+-0.62)e-20 N/sqrt(Hz)` at `2.4e-6 mbar`, while measured off-resonance sensitivity is of order `1e-17 N/sqrt(Hz)` in the reported setup.

This is strong evidence that RQIR's insistence on measured transfer/spectral sensitivity rather than a single thermal-limit number is experimentally well motivated. The experiment is not the required simultaneous two-band/cross-PSD RQIR likelihood.

### Gosling et al., Physical Review Research 6, 013129 (2024)

DOI `10.1103/PhysRevResearch.6.013129`.

This experiment applies a directional stochastic force to a 3D-feedback-cooled levitated nanosphere and measures PSD/cross-correlation spectra. The published model contains separate susceptibilities and cross spectra, and the experiment reports effective feedback damping around `2.1 kHz` and `2.5 kHz` in the two transverse modes for a representative data set at `4e-3 mbar`.

The force-sensing discussion uses spectral integration blocks `T_b=3.3 ms`; the variance decreases as the number of blocks grows. The work also explicitly discusses detector/electronic noises, mode-dependent response, run-to-run variations and pressure-gauge uncertainty as calibration limitations.

This is directly relevant to RQIR's PSD/cross-PSD, finite-integration and calibration-drift requirements. It still does not provide the complete exact `f:2f` same-state Fisher matrix or the RQIR seven-plus-eight calibration Jacobian/rate library.

### Gosling et al., Review of Scientific Instruments 97, 013202 (2026)

DOI `10.1063/5.0292738`.

This work demonstrates stable 3D velocity feedback cooling with reduced cross-talk. The reported trap frequencies are approximately `35 kHz`, `137 kHz`, and `149 kHz`; the feedback transfer is implemented with digital band-pass filters whose center frequency, bandwidth, gain and phase are controlled. Mechanical cross-correlation spectra are used to diagnose cross-talk, and the improved electrode configuration reduces cross-talk by about an order of magnitude.

This is useful physical evidence for the control/transfer part of Paper III, but the frequencies are not an RQIR `f:2f` science pair and the paper does not report the required RQIR joint Fisher-rate matrices.

### Song et al., Nature Communications 17, 8852 (2026)

DOI `10.1038/s41467-026-75601-9`.

Published 14 July 2026. This experiment is especially relevant because it demonstrates simultaneous operation/measurement of a fundamental phonon-laser mode and its exact second harmonic.

The reported fundamental is `Omega_1/(2pi)=17.8 kHz`, while the second-harmonic mode is `2Omega_1/(2pi)=35.6 kHz`. The paper states that both modes are squeezed simultaneously in the same measurement; one representative protocol uses about 2500–3000 independent pulses with 5-ms spacing.

### RQIR-EXPERIMENT-001 — exact `f:2f` platform-class feasibility

> Exact fundamental/second-harmonic simultaneous mechanical operation is no longer merely a hypothetical apparatus assumption: a levitated optomechanical experiment has demonstrated it directly.

This removes one important platform-class feasibility concern from Iterations 082–084.

However, the Song experiment is a nonlinear thermomechanical phonon-laser/squeezing apparatus at roughly 20 mbar, not an RQIR force-calibrated dual-band sensor. The paper does not report a force-calibrated full `f:2f` PSD/cross-PSD Fisher matrix or the transfer/common-gain calibration quantities needed to compute `R_s` and `R_c` for Toy009/Toy014.

## 3. RQIR-NG-080 — componentwise literature cannot be spliced into one apparatus forecast

The audited papers provide complementary pieces:

- exact `f:2f` simultaneous mode operation;
- cross-spectral multimode readout;
- transfer-function calibration;
- force-sensitivity spectra;
- feedback gain/phase control;
- SI-traceable force-metrology methods in other levitated platforms.

But these pieces belong to different particles, pressures, traps, detectors, transfer functions and likelihoods.

Therefore:

> **RQIR-NG-080:** numbers from different experimental platforms must not be spliced together to manufacture a single Toy009/Toy014 apparatus certificate unless a declared transduction model proves the mapping and uncertainty propagation.

In particular, the `4.39e-20 N/sqrt(Hz)` thermal limit from one apparatus cannot be combined with the `17.8/35.6 kHz` harmonic pair of another apparatus and the cross-PSD of a third to claim an RQIR wall-clock time.

## 4. RQIR-RESOURCE-094 — minimum public dataset for a numerical detector certificate

A publication/raw-data release sufficient to collapse the current Paper-III detector interval must provide, under one declared apparatus state or a validated mapping between states:

1. simultaneous complex transfer vector/matrix at the two retained science frequencies;
2. full PSD/cross-PSD covariance in the same Fourier/window convention;
3. enough same-state reference data to compute the phase-profiled common-gain rate `R_c`;
4. seven same-time dual-probe mean-layer Fisher-rate matrices or their raw likelihood ingredients;
5. covariance-complement rate matrices for a physically allowed campaign cover, with backaction model if rows share source copies;
6. geometry/additive SI transduction and stability/reference information;
7. source-preparation/metrology throughput and acceptance/reset/visibility;
8. timing/control duty and drift/recertification data.

Only then is a numerical `u` defensible through RESOURCE-091/092.

## 5. What can be concluded now

Positive experimental conclusions:

- simultaneous multimode readout is established;
- cross-spectral force/noise sensing is established;
- measured transfer-function-based force calibration is established;
- active gain/phase feedback control with reduced cross-talk is established;
- exact `f:2f` fundamental/second-harmonic operation is experimentally established by 2026.

Negative/conditional conclusion:

- the audited public literature does not expose the complete one-apparatus RQIR likelihood/resource dataset required for a numerical Toy009/Toy014 detector comparison.

Hence the current parametric detector certificate is not a weakness to be filled by mixing unrelated sensitivity numbers; it is the scientifically correct boundary of what the public data support.

## 6. Consequence for Paper III

The external audit changes the interpretation of the remaining gap:

- the gap is **not** that a two-band or exact-harmonic levitated platform is obviously impossible;
- the gap is that the required combined calibration/cross-spectral/source/control **dataset has not been published in one compatible form** among the audited papers.

This supports presenting Paper III as an apparatus specification/certificate paper: it tells an experimental group exactly what must be measured to turn a promising platform into a falsifiable RQIR experiment.

## 7. Readiness snapshot after Iteration 122

Project-management estimates, not statistical quantities.

- **Repository readiness for writing Paper III — scientific content:** **95%**.
- **Paper III submission-ready state:** **78%**.
- **Repository readiness to begin a concrete Candidate-Gravity model:** **84%**.
- **Concrete Candidate-Gravity model itself:** **~10%**.

Paper III scientific readiness increases because the apparatus-class feasibility and public-data boundary have now been externally audited. Submission readiness increases more strongly because several key literature anchors for the experimental-resource section are now identified. Candidate-Gravity readiness is unchanged because no QG consistency gate or candidate dynamics was solved.

## 8. Next admissible gate

Paper III is now close to scientific closure. The highest-value next steps are:

1. perform a focused literature/novelty audit around Fisher-optimal calibration scheduling, cross-spectral force sensing and gravity-mediated quantum-interface experiments;
2. build a manuscript-ready claim/evidence table that separates theorem, deterministic toy regression, external experimental precedent and still-open apparatus input;
3. only pursue further detector numerics if a same-apparatus raw/public dataset actually supplies RESOURCE-094.

Candidate Gravity should remain separate until the reconstruction/article boundary is frozen and a concrete dynamics is introduced under QG-001…QG-010.

## 9. Reproducibility / evidence matrix

Run

`python analysis/external_apparatus_evidence_matrix_iteration122.py`.

The script records only the presence/absence of the RQIR-required public-data categories in the audited experimental papers; it deliberately contains no interpolated apparatus numbers.
