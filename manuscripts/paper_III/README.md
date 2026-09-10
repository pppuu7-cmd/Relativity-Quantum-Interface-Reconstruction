# RQIR Paper III — final manuscript package

**Title:** *Relativity–Quantum Interface Reconstruction III: Resource Conversion, Apparatus-Level Identifiability, and Traceable Experimental Closure*

**Scientific authority:** RQIR Core v1.0 / Paper-III final scientific certificate, frozen 9 September 2026.

**Manuscript date:** 10 September 2026.

## Status

- Scientific/material readiness supporting Paper III: **100%**.
- Final article text: assembled from the frozen `main` authority rather than the earlier exploratory `paper-III` branch.
- Local preflight: RevTeX 4.2 compilation succeeds in two passes; 9 pages; no undefined citations/references; no overfull boxes after the self-containment revision.
- Journal-specific cover letter, portal metadata, and any journal-requested style conversion are intentionally separate from scientific readiness.

## Article scope

Paper III closes the third RQIR layer:

1. Paper I — calibration/source distinguishability;
2. Paper II — detector-facing statistical identifiability and nuisance geometry;
3. **Paper III — physical resource closure and experiment architecture;**
4. Paper IV — known-model comparator funnel under frozen RQIR v1.0;
5. Paper V — Candidate Gravity only if Paper IV warrants a genuinely new model.

The paper does not report an RQIR detection and does not select a microscopic gravity model.

## Main scientific content

The manuscript contains:

- the nuisance-profiled resource variational law and proofs of resource monotonicity, concavity, and data-only homogeneity;
- maximum-information/minimum-budget laws and marginal information-per-cost rule;
- the RQIR-II two-band continuation with a 16% information gain at fixed resource;
- a source-grounded three-pulse `87Rb` Raman atom-gravimeter binding;
- explicit frozen science/reference modulation geometry (`0.5 Hz` science, `1 Hz` reference, `1 micro-g` reference amplitude);
- source-traceable colored vibration covariance from the published Le Gouët et al. apparatus spectrum;
- the detector-facing probability likelihood `P=(1+C cos Phi)/2` with phase, drift, contrast, readout, scale, and finite-reference nuisances;
- a prospective traceable differential Raman-chirp reference;
- required negative controls and explicit failure domains;
- independent clean reproduction and provenance boundaries;
- a five-paper RQIR architecture figure, calibration/statistics crossover figure, frozen-result table, and claims/non-claims table.

## Canonical supporting authority

The manuscript is downstream of, and does not modify, the frozen scientific authority in:

- `docs/PAPER_III_FINAL_SCIENTIFIC_CERTIFICATE_2026-09-09.md`
- `docs/PAPER_III_SCIENTIFIC_MANIFEST_2026-09-09.json`
- `docs/RQIR7_PAPER_III_PROVENANCE_COMPATIBILITY_CERTIFICATE_2026-09-09.md`
- `docs/RQIR_CORE_V1_FREEZE_MANIFEST_2026-09-09.md`
- `.github/workflows/paper3_clean_reproduction.yml`

The seven authoritative apparatus-analysis scripts are listed in the scientific manifest.

## Build

From `manuscripts/paper_III`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The manuscript uses `revtex4-2`, TikZ, and PGFPlots.

## Frozen claim boundary

The positive article-facing claim is a **resource/design forecast**: in the declared Raman-gravimeter architecture, a modulated acceleration-like RQIR science amplitude can remain locally estimable after the declared physical colored-noise, detector, nuisance, and calibration treatment when a traceable acceleration-equivalent reference closes the common scale.

The manuscript must not be edited to claim:

- an observed RQIR departure;
- that the 2008 apparatus used the 2025 chirp-metrology implementation;
- that the digitized vibration spectrum is raw campaign data;
- that every apparatus nuisance is individually identifiable;
- that Paper III selects or validates a unique microscopic gravity model.
