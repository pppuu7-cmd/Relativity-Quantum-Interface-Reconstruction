# RQIR Paper III — final scientific certificate

**Date:** 2026-09-09  
**Status:** **100% scientific/material readiness for the strengthened apparatus-specific scope**  
**Manifest:** `docs/PAPER_III_SCIENTIFIC_MANIFEST_2026-09-09.json`

## Certified scope

Paper III is certified as an **apparatus-grounded resource/design paper** showing when an acceleration-like RQIR science amplitude is or is not identifiable in a realistic three-pulse `87Rb` Raman atom-gravimeter architecture after physical noise, detector and calibration nuisances are treated together.

This certificate does **not** claim an experimental discovery of an RQIR effect and does **not** claim that every numerical ingredient comes from one historical raw campaign.

## Independent clean reproduction authority

A dedicated clean-reproduction workflow was run on a fresh GitHub-hosted environment and completed successfully:

- workflow: `Paper III clean reproduction`;
- workflow run: `34401786475`;
- job: `102635176796`;
- conclusion: `success`;
- runner: Ubuntu 24.04.5 LTS, hosted `ubuntu-24.04` image;
- Python: `3.12.14`;
- freshly installed NumPy: `2.5.3`;
- freshly installed SciPy: `1.18.1`;
- PR head: `924dddb94681f5d28246f267394ea8e7c24d0b92`;
- checked-out PR merge commit: `0011039098424bdb66743d999f61f33c70b8e3ce`;
- base scientific/workflow commit: `edafefe06b115418e40454c3652e6d9fe1193c6b`.

Every tracked Paper-III audit completed with exit status zero, including the negative controls.

## Frozen computational chain

1. `analysis/atom_interferometer_calibration_hierarchy_audit.py`
2. `analysis/atom_interferometer_science_estimability_full_covariance_audit.py`
3. `analysis/atom_interferometer_reference_calibration_floor_audit.py`
4. `analysis/atom_gravimeter_same_apparatus_resource_closure_audit.py`
5. `analysis/atom_gravimeter_figure8_psd_covariance_audit.py`
6. `analysis/atom_gravimeter_detector_facing_probability_likelihood_audit.py`
7. `analysis/atom_gravimeter_chirp_reference_metrology_audit.py`
8. `docs/RQIR7_PAPER_III_PROVENANCE_COMPATIBILITY_CERTIFICATE_2026-09-09.md`

The exact clean-run numbers are frozen in `docs/PAPER_III_SCIENTIFIC_MANIFEST_2026-09-09.json` rather than being reconstructed manually in the manuscript.

## Frozen scientific result table

| Layer | Clean-run result | Decision |
|---|---|---|
| structural calibration hierarchy | known acceleration reference makes `theta` estimable; science-only and science+recoil do not | PASS with negative controls |
| full covariance | `theta` estimability survives correlated covariance through `rho <= 0.98`; unknown reference remains non-identifiable | PASS |
| abstract calibration floor | `sigma_theta^2 = A/N + calibration_floor^2` reproduced | PASS |
| same-apparatus scale | measured `11 mrad/shot -> 1.39247e-8 g @ 1 s` | reproduces source scale |
| physical Fig.-8 PSD | `6.34856e-8 g @ 1 s` versus source `6.5e-8 g` | PASS, 2.33% mismatch |
| corrected physical scale | `2.17592e-8 g @ 1 s` versus typical source `2e-8 g` | PASS, 8.80% mismatch |
| physical colored-noise science forecast | `sigma_theta = 5.72247 ng` at 60 s; `1.85019 ng` at 600 s | PASS |
| 2-Hz crosstalk stress | `x5 -> 9.31148 ng` at 60 s without loss of estimability | PASS |
| detector observable | `P=(1+C cos Phi)/2`, `sigma_P=3e-4`, effective `C~0.6` | source-grounded detector layer |
| nonlinear detector forecast | `5.72811 ng` at 60 s and `1.851801 ng` at 600 s for 1% reference prior | PASS |
| detector calibration law | full probability likelihood reproduces quadrature calibration floor | PASS |
| traceable chirp reference | `1 micro-g -> 25.1373191 Hz/s` differential chirp | PASS |
| conservative reference uncertainty | `7.95629794e-5 = 0.0079563%` | PASS |
| full-hour science forecast | `0.746604 ng`; 100% science duty in shot-coded chirp architecture | PASS |
| calibration/statistics crossover | `9383.82 ng ~= 9.38 micro-g` | explicit resource boundary |

## Core positive claim

For the frozen apparatus/resource architecture, a **modulated acceleration-like RQIR science amplitude remains locally estimable** after simultaneous treatment of:

- physical colored vibration covariance;
- phase offset and phase drift;
- finite detector probability noise;
- contrast and contrast drift;
- readout gain, gain drift and offset;
- common multiplicative phase/acceleration scale;
- finite absolute reference uncertainty.

The result does not require every apparatus parameter to be individually identifiable. Apparatus-only null modes are allowed only when their overlap with the RQIR science direction is zero.

## Required negative controls

The repository also certifies the failure domain:

- static acceleration-like science with a free phase offset: **FAIL**;
- modulated science without an independently calibrated absolute reference: **FAIL**;
- unknown unconstrained reference amplitude: **FAIL**;
- recoil alone as replacement for absolute acceleration reference: **FAIL** for absolute `theta` identifiability.

These failures are part of the scientific result and prevent the positive result from being created by hidden regularization.

## Provenance boundary

The source-composition rules are frozen in `RQIR7_PAPER_III_PROVENANCE_COMPATIBILITY_CERTIFICATE_2026-09-09.md`:

- Le Gouët et al. 2008 supplies the baseline physical apparatus/noise/detector family;
- Cheinet et al. supplies compatible sensitivity-function/transfer formalism;
- Zhang et al. 2025 supplies transferable absolute chirp-metrology capability for the proposed design, not historical 2008 raw data;
- Hu et al. 2015 supplies DDS stability authority only;
- BIPM supplies the optical frequency scale only;
- the Fig.-8 curve is an explicitly labelled coarse source-traceable digitization, not raw data;
- no raw samples from different experiments are statistically concatenated.

The absence of raw machine-readable historical campaign data is therefore a documented provenance limitation, not an untracked scientific assumption.

## Article-facing claim boundary

Paper III **may** state that RQIR supplies a physically grounded experiment/resource architecture with explicit identifiability, nuisance, calibration and exposure requirements for a realistic Raman atom gravimeter.

Paper III **may not** state that:

- an RQIR departure has already been observed;
- the 2008 apparatus used the 2025 chirp-metrology implementation;
- the digitized Fig.-8 spectrum is raw campaign data;
- full apparatus parameter rank is necessary for science estimability;
- an unmeasured commanded chirp value is equivalent to certified metrology.

## Reproducibility and manifest gate

The clean CI result closes independent reproduction. The machine-readable manifest freezes:

- environment and commit identifiers;
- exact script list;
- exact numerical outputs used in the article-facing table;
- source/provenance boundaries;
- negative controls and failure domains;
- the meaning of `100%` readiness.

No decisive Paper-III scientific number now depends on an untracked notebook or an undocumented manual calculation.

## Final decision

**PAPER III STRENGTHENED SCIENTIFIC/MATERIAL READINESS: 100%.**

Papers I and II were already scientifically closed at 100% on the same repository-readiness scale. Therefore:

**PAPERS I–III REPOSITORY SCIENTIFIC READINESS = 100%.**

This statement concerns scientific/material readiness. Journal-specific copy-editing, final typesetting, cover letters, author metadata and portal submission remain a separate submission-administration layer and do not reopen the scientific gates certified here.
