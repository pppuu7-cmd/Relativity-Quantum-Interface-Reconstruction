# RQIR Paper III — manuscript preflight

**Date:** 2026-09-10  
**Branch:** `paper-III-final`  
**Base:** frozen `main` / RQIR Core v1.0

## Decision

**ARTICLE TEXT / SCIENTIFIC PACKAGE: READY FOR EXTERNAL REVIEW.**

This status is narrower than a journal submission completion state. Journal-specific cover letter, classification codes, portal metadata, source-archive conventions, and any requested style conversion remain administrative packaging.

## Scientific consistency checks

- Paper III is downstream of the frozen 100% scientific/material authority and does not reopen Core v1.0 definitions.
- The manuscript preserves the five-paper architecture: I calibration, II statistical identifiability, III resource closure, IV known-model comparator funnel, V Candidate Gravity only if warranted.
- The central resource variational law, concavity/monotonicity/homogeneity result, budget law, marginal-value rule, two-band 16% result, and robust-allocation boundary are retained.
- The physical forecast is tied to the source-grounded `87Rb` Raman gravimeter apparatus/noise/detector family.
- The source/reference geometry is explicit in the article: science `0.5 Hz`, reference `1.0 Hz`, reference phase `0.37 rad`, nominal reference `1 micro-g`.
- `ng` and `micro-g` are explicitly defined as acceleration units, avoiding confusion with mass units.
- Physical colored covariance, detector-facing probability readout, reference calibration, nuisance profile, and failure controls are all represented.
- The prospective 2025 chirp-metrology authority is not presented as historical 2008 apparatus data.
- The coarse Fig.-8 digitization is explicitly not raw data.
- No experimental RQIR detection, quantized-gravity inference, or unique microscopic-model selection is claimed.

## Numerical authority checks

Article-facing numbers are taken from `docs/PAPER_III_SCIENTIFIC_MANIFEST_2026-09-09.json`, including:

- `11 mrad/shot -> 1.39247e-8 g @ 1 s`;
- Fig.-8 physical PSD `6.34856e-8 g @ 1 s` versus source `6.5e-8 g`;
- corrected scale `2.17592e-8 g @ 1 s` versus source `2e-8 g`;
- physical colored-noise forecast `5.72247 ng @ 60 s`, `1.85019 ng @ 600 s`;
- detector-facing forecast `5.72811 ng @ 60 s`, `1.851801 ng @ 600 s` for the 1% reference-prior check;
- `1 micro-g -> 25.1373191 Hz/s` differential chirp;
- conservative reference fraction `7.95629794e-5`;
- one-hour statistical uncertainty `0.746604 ng`;
- calibration/statistics crossover `9383.82 ng ~= 9.38 micro-g`.

## Reproducibility

The underlying scientific chain was independently reproduced by the frozen GitHub-hosted clean run (`workflow 34401786475`, `job 102635176796`). The manuscript does not substitute its LaTeX build for that scientific reproduction authority.

## Typesetting preflight

A two-pass local RevTeX 4.2 build was performed after the self-containment revision:

- output: **9 pages**;
- undefined references: **none**;
- undefined citations: **none**;
- overfull boxes: **none**;
- two vector figures and two article-facing tables render within the page area;
- selected pages were visually inspected after raster rendering.

## Remaining submission-administration items

These do not lower scientific readiness:

- choose the target journal and adapt class/options if needed;
- prepare target-journal cover letter;
- prepare portal metadata / subject classifications / keywords;
- export a journal-compliant source archive if required;
- perform final author-approved wording and bibliography proof before submission.
