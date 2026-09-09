# RQIR Papers I–V — strict repository-readiness audit

**Date:** 2026-09-09  
**Purpose:** estimate scientific/material readiness of the repository. This is not a probability of journal acceptance and is separate from journal-specific portal/submission administration.

## Canonical five-paper architecture

1. **Paper I** — operational hierarchy / ordered source information / finite discriminants.
2. **Paper II** — statistical identifiability / nuisance geometry.
3. **Paper III** — physical resource budgets / experiment architecture.
4. **Paper IV** — existing gravity and quantum-gravity frameworks through the common RQIR comparator funnel, ending in one of `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED`.
5. **Paper V** — a genuinely new RQIR-derived Candidate Gravity model only if Paper IV returns `NEW_REQUIRED`.

A `BLOCKED` comparator is not evidence for `NEW_REQUIRED`.

## Current headline table

| Paper | Current strict repository readiness | Status | Decisive reason |
|---|---:|---|---|
| I | **100% scientific material** | CLOSED for frozen scope | RQIR-THM-001/source-calibration layer is scientifically closed; remaining work is editorial/submission hardening rather than missing scientific content. |
| II | **100% scientific material** | CLOSED | detector-facing likelihood, nuisance profiling, whitening, rank-deficient tests and independent submission audit are closed; remaining actions are predominantly author/portal administration. |
| III | **100% scientific material — strengthened apparatus-specific scope** | CLOSED | physical same-apparatus scaling, source-traceable colored covariance, nonlinear detector likelihood, nuisance profiling, traceable chirp-reference metrology, provenance compatibility, independent clean reproduction and the final scientific manifest/certificate are all closed with explicit failure domains. |
| IV | **55%** | ACTIVE / prerequisite-blocked | comparator funnel and many framework audits exist, but the common physical observable/source-completion bridge and robust comparator-subtracted residual are still missing. |
| V | **0% article-authorized**; **24% conditional Candidate-Gravity groundwork** | CONDITIONAL / NOT AUTHORIZED | Paper IV has not returned `NEW_REQUIRED`. |

## Papers I–III collective status

**PAPERS I–III REPOSITORY SCIENTIFIC READINESS = 100%.**

This means the scientific/material layer needed to support the first three papers is now closed on the repository's strict scale. It does **not** mean every journal-specific formatting, cover-letter, author-metadata or submission-portal task is finished.

## Paper I

Repository scientific scope remains closed at Iteration 078. The CQG-targeted manuscript exists and the scientific material is sufficient for the paper. Remaining gaps such as publication polishing, final bibliography/priority normalization and package assembly are submission/editorial work rather than missing scientific content.

## Paper II

Paper II remains the most publication-mature branch. The repository contains the manuscript, vector figures, deterministic data regeneration, 10,000 randomized property tests, rank-deficient nuisance tests, correlated-covariance whitening, cover-letter material, manifest and checklist. Scientific material remains closed at 100%.

## Paper III — strengthened apparatus-specific closure

The strengthened 2026-09-09 programme closes the full chain below.

### Structural identifiability

- common multiplicative science-scale degeneracy is explicit;
- science-only and science+recoil negative controls fail absolute `theta` identifiability as required;
- a known/modulated acceleration-equivalent reference restores science-amplitude estimability;
- apparatus-only null directions are allowed only when theta-orthogonal;
- full correlated-covariance tests preserve the structural result.

### Physical same-apparatus and noise layer

- the physical model is tied to a published SYRTE `87Rb` Raman gravimeter with `2T=100 ms`, `4 Hz` cycle and measured `11 mrad/shot`;
- `k_eff T^2` reproduces the source's approximately `1.4e-8 g at 1 s` sensitivity scale;
- Cheinet sensitivity-function authority supplies the acceleration transfer geometry;
- an unfitted coarse source-traceable digitization of published Fig. 8 gives `6.34856e-8 g at 1 s` versus the source's `6.5e-8 g` vibration limit;
- factor-3 correction plus the independent `4 mrad/shot` budget gives `2.17592e-8 g at 1 s` versus the quoted typical `2e-8 g`;
- the continuous physical spectrum is propagated into sampled colored covariance;
- science estimability survives a five-fold stress of the problematic broad 2-Hz structure.

### Detector-facing likelihood

- the primitive detector observable is `P=(1+C cos Phi)/2` rather than reconstructed phase;
- source-grounded `sigma_P=3e-4` and an approximate effective `C~0.6` anchor are used;
- phase offset/drifts, contrast/drifts, readout gain/drift/offset and common scale are profiled simultaneously;
- the clean-run forecast gives `sigma_theta=5.72811 ng` at 60 s and `1.851801 ng` at 600 s for the 1% reference-prior check;
- the full detector likelihood reproduces the expected multiplicative calibration-floor law;
- static science, no-reference and unconstrained-reference negative controls remain failures.

### Traceable absolute reference metrology

The earlier mechanical/seismometer `~1%` proxy is superseded by a differential Raman-chirp reference.

For a Raman gravimeter,

`Delta Phi = (k_eff g - 2 pi alpha_nu) T^2`,

so a known differential chirp supplies an acceleration-equivalent reference in the same phase channel.

The final conservative design uses a differential chirp uncertainty of `2 mHz/s` directly on the small reference difference rather than incorrectly normalizing sub-mHz/s metrology to the full gravity chirp. The clean run gives:

- nominal gravity chirp: `25,137,319.1 Hz/s`;
- `1 micro-g` reference difference: `25.1373191 Hz/s`;
- conservative reference fraction: `7.95629794e-5 = 0.0079563%`;
- improvement over the old mechanical proxy: `133.806x`;
- full-hour science duty: `100%` because the reference can be shot-coded rather than consuming separate mechanical calibration blocks;
- one-hour statistical uncertainty: `0.746604 ng`;
- calibration/statistics crossover: `9383.82 ng ~= 9.38 micro-g`.

This is a transferable metrology architecture for the proposed resource/design experiment. The repository does not claim that the historical 2008 apparatus itself used the later chirp-metrology implementation.

### Provenance compatibility

`docs/RQIR7_PAPER_III_PROVENANCE_COMPATIBILITY_CERTIFICATE_2026-09-09.md` freezes the source graph:

- Le Gouët 2008 is the baseline apparatus/noise/detector family;
- Cheinet provides compatible sensitivity-function formalism, not a merged raw campaign;
- Zhang 2025 provides prospective absolute chirp-metrology capability;
- Hu 2015 provides DDS stability authority only;
- BIPM provides optical scale only;
- the Fig.-8 trace remains explicitly a coarse digitization rather than raw data;
- no raw observations from incompatible experiments are concatenated.

The lack of machine-readable historical raw campaign data is therefore carried as an explicit provenance limitation rather than an unresolved hidden input.

### Independent clean reproduction

A dedicated GitHub-hosted clean run completed successfully:

- workflow run `34401786475`;
- job `102635176796`;
- Ubuntu 24.04.5 LTS;
- Python `3.12.14`;
- fresh NumPy `2.5.3`;
- fresh SciPy `1.18.1`;
- checked-out PR merge commit `0011039098424bdb66743d999f61f33c70b8e3ce`;
- every tracked Paper-III computational step and provenance check concluded `success`.

This closes the independent clean-reproduction gate.

### Final article-facing scientific package

The final scientific claims, failure domains, environment identifiers and exact clean-run numbers are frozen in:

- `docs/PAPER_III_FINAL_SCIENTIFIC_CERTIFICATE_2026-09-09.md`;
- `docs/PAPER_III_SCIENTIFIC_MANIFEST_2026-09-09.json`.

No decisive scientific result now depends on an untracked notebook or undocumented manual calculation.

Therefore:

**PAPER III STRENGTHENED SCIENTIFIC/MATERIAL READINESS = 100%.**

## Paper IV

The repository contains substantial comparator material and a negative-results matrix spanning semiclassical, stochastic/postquantum, Gaussian/Källén–Lehmann, perturbative GR EFT, nonlocal/form-factor and asymptotic-safety directions. Later Candidate-Gravity work extends the audit chain through Iteration 675.

The live front remains prerequisite-blocked. Exact missing authorities are:

- **M1:** a concrete same-parent conserved detector/asymptotic observable geometry;
- **M2:** matched Source/Born/contact completion in that same observable;
- **M3:** a concrete nonzero robust comparator-subtracted residual;
- **M4:** actual `Tr U1` only if a future C5 route requires it.

Because M1-M3 are upstream of the terminal comparator decision, Paper IV cannot yet honestly choose `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, or `NEW_REQUIRED`. **55%** is retained.

## Paper V

Paper V remains unauthorized as a new-model paper until Paper IV returns `NEW_REQUIRED`. Candidate-Gravity groundwork remains **24%** and is not treated as Paper-V publication readiness.

## Program-level interpretation

The immediate first-three-paper scientific objective is now closed at **100%**. The broader RQIR programme is still incomplete because Paper IV remains at its physical comparator/residual bottleneck and Paper V is conditional. A conservative working programme/model readiness is now approximately **76%**; Candidate-Gravity groundwork remains **24%**.

## Next high-value action

For Papers I–III, research should now shift from opening new scientific gates to manuscript/submission hardening and consistency checks unless a reviewer-style audit reveals a real scientific defect. For the broader RQIR programme, the highest-value scientific front returns to Paper IV: obtain M1/M2 and construct the first defensible robust comparator-subtracted residual M3 before authorizing any new-gravity Paper V claim.
