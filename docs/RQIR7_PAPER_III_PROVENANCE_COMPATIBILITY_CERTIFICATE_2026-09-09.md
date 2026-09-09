# RQIR7 — Paper III provenance / compatibility certificate

**Date:** 2026-09-09  
**Scope:** strengthened apparatus-specific Paper III resource/design forecast.

## Purpose

Certify that the Paper-III calculation does not silently combine incompatible raw datasets or treat transferable metrology authorities as if they were measurements from one historical campaign.

The scientific object certified here is an **apparatus-grounded resource/design forecast** for a compatible three-pulse Raman atom-gravimeter architecture. It is **not** a claim that an RQIR signal has been experimentally detected, and it is not a reconstruction of one raw historical SYRTE campaign.

## Authority graph

### A. Le Gouët et al. 2008 — baseline apparatus / noise / detector authority

Used for the common apparatus anchor:

- `87Rb` Raman atom gravimeter;
- `2T = 100 ms`;
- `4 Hz` repetition rate;
- approximately `10 us` Raman pulse scale;
- measured `11 mrad/shot` best phase noise;
- passive-platform vibration ASD in published Fig. 8;
- typical factor-3 vibration correction;
- independent non-vibration budget approximately `4 mrad/shot`;
- detector probability floor approximately `sigma_P = 3e-4` at high atom number;
- mid-fringe/post-correction operating constraints;
- simultaneous atom/seismometer transfer-function validation and controlled platform excitation.

These quantities form the **single physical baseline apparatus family** for the same-apparatus/noise/detector calculations.

The Fig.-8 PSD knots in the repository are an explicitly labelled coarse log-log digitization of the published passive-platform trace. They are not claimed to be raw samples.

### B. Cheinet et al. 2008 — sensitivity-function authority

Used for the three-pulse Raman sensitivity/transfer formalism, including the low-frequency acceleration response. This is a transferable theoretical/experimental transfer-function authority for the same class of Raman interferometer, not a second raw campaign whose data are merged with Le Gouët et al.

### C. Zhang et al. 2025 — absolute chirp-metrology authority

Used only to demonstrate a realizable, traceable way to measure Raman/microwave chirp rates with sub-mHz/s-class precision using calibrated time/frequency instrumentation synchronized to an atomic clock.

This source is **not** treated as evidence that the historical 2008 SYRTE apparatus possessed this metrology. It supplies a metrology capability for the proposed Paper-III experiment design.

### D. Hu et al. 2015 — DDS stability authority

Used only as an independent bound showing that direct-DDS chirp generation can have very small short-term instability. It is not used as the absolute reference-accuracy claim and contributes no raw atom-interferometer observations.

### E. BIPM CIPM Recommendation 2 (2015) — optical frequency standard

Used only to anchor the `87Rb` D2 optical frequency scale entering the representative `k_eff` calculation. It contributes no apparatus noise or detector data.

### F. RQIR-derived quantities

The following are calculations, not measurements:

- `k_eff T^2` resource scale;
- Fig.-8 PSD integration into sampled covariance;
- Fisher/null-space science estimability;
- nonlinear probability-likelihood propagation;
- detector nuisance stress tests;
- reference calibration-floor law;
- differential-chirp acceleration reference;
- one-hour resource forecasts and calibration/statistics crossover.

Every such quantity must be reproducible from tracked scripts and the source assumptions above.

## Compatibility rules

1. **No cross-source raw-data fusion.** No shot samples from one experiment are statistically concatenated with another experiment.
2. **One baseline apparatus family.** Noise, detector and cycle parameters used in the principal physical forecast come from the Le Gouët SYRTE Raman-gravimeter baseline unless explicitly labelled as a transferable design authority.
3. **Transfer-function theory is not raw data.** Cheinet sensitivity-function results are used to propagate physical noise; they are not treated as an independent realization of the same campaign.
4. **Chirp metrology is prospective design authority.** The Zhang/Hu chirp results establish how the proposed reference can be made traceable; they do not retrofit 2025 electronics/metrology into the 2008 dataset.
5. **Optical standard is scale authority only.** BIPM frequency uncertainty affects `k_eff`; it does not validate apparatus alignment, Raman detuning, or beam geometry.
6. **Mechanical shaker is no longer the absolute calibrator.** The 2008 platform-excitation result remains evidence that controlled transfer measurements are physically realizable, but the final reference architecture is the differential Raman-chirp reference.
7. **Digitized PSD is frozen as a source-traceable substitute.** In the absence of raw machine-readable campaign PSD/cross-PSD, the coarse Fig.-8 digitization is allowed only because it independently reproduces two published integrated noise scales and its limitation is explicit.
8. **Detector contrast anchor is approximate.** `C ~ 0.6` is inferred from published `sigma_P ~ 3e-4` and near-`1 mrad/shot` detector phase sensitivity; it is not claimed as a directly quoted raw contrast measurement.
9. **No experimental-detection claim.** All RQIR science amplitudes in the apparatus audits are forecast/test parameters, not observed departures from GR or quantum mechanics.

## Compatibility tests already passed

The repository has independent numerical checks that strongly constrain accidental source incompatibility:

- apparatus scale from `lambda`, `T` and `4 Hz` reproduces the quoted `1.4e-8 g at 1 s` short-term sensitivity;
- the unfitted coarse Fig.-8 spectrum predicts approximately `6.35e-8 g at 1 s` versus the source's `6.5e-8 g` vibration limit;
- applying the source's factor-3 rejection and independent `4 mrad/shot` budget gives approximately `2.18e-8 g at 1 s` versus the quoted typical `2e-8 g`;
- nonlinear detector propagation preserves the expected negative controls and finite-reference calibration law;
- the chirp-reference metrology uses the differential `~25 Hz/s` quantity rather than incorrectly normalizing sub-mHz/s metrology to the full `~25 MHz/s` gravity chirp.

## Frozen Paper-III scientific claim class

Paper III may claim:

> For a source-grounded, experimentally realizable three-pulse `87Rb` Raman atom-gravimeter design, RQIR acceleration-like science information can remain locally estimable after simultaneous physical colored-noise, phase, contrast, readout and calibration nuisance profiling, provided the science observable is modulated and an independently traceable acceleration-equivalent reference closes the absolute scale. The repository supplies explicit resource forecasts and failure domains.

Paper III may **not** claim:

- an experimental detection of an RQIR effect;
- that all inputs came from one historical raw dataset;
- that the 2008 apparatus was already calibrated by the 2025 chirp-metrology method;
- that the coarse Fig.-8 digitization is raw data;
- that every apparatus nuisance is individually identifiable.

## Decision

**MATCHED PROVENANCE / COMPATIBILITY GRAPH: PASS for a resource/design paper.**

This certificate freezes the allowed source composition and removes the earlier ambiguity about whether the strengthened Paper-III forecast mixed incompatible campaigns. Raw campaign data remain desirable but are no longer an undefined prerequisite: if unavailable, the source-traceable substitutes above are the frozen reproducible authorities, with their limitations carried into the manuscript.

The remaining repository-level gates to 100% scientific material are therefore:

1. independent clean deterministic reproduction of the complete Paper-III chain;
2. final article-facing scientific certificate / manifest / tables / failure-domain package bound to the clean run.
