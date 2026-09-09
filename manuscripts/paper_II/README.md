# RQIR Paper II — Physical Review Research submission package

**Title:** *Relativity–Quantum Interface Reconstruction II: Statistical Identifiability, Nuisance Geometry, and Detectability in Detector-Facing Likelihoods*

**Author:** Aleksey Buyanov — Independent Researcher, Moscow, Russia — ORCID 0009-0001-2621-9305.

**Scientific status:** closed for the Paper-II scope defined by the RQIR series architecture and RQIR-STAT-001.

## What this manuscript closes

Paper I establishes exact source/calibration separation. Paper II asks whether the detector-facing target direction survives nuisance profiling and how independent calibration information changes local precision. The retained chain is

`Paper-I physical null direction -> detector response derivative -> covariance whitening -> nuisance profile -> prior-assisted profile -> finite-data staging`.

Paper III remains responsible for shots, PSD/SNR, coherence, wall-clock time, geometry and technology/resource conversion.

## Reproducibility

- historical certificate: `docs/PAPER_II_REFERENCE_LIKELIHOOD_CERTIFICATE_ITERATION079.md`
- historical regression script: `analysis/paper12_reference_regression_iteration079.py`
- independent submission audit: `analysis/paper_II_submission_audit_20260908.py`
- audit data: `manuscripts/paper_II/data/rqir_stat_001_submission_audit.json`
- exact public audit/data snapshot: `d0f6453721821fcaec4e9e24ea5e68185d90a5a2`
- fixed seeds: 20260830 (certificate), 20260908 (independent stress audit)

The submission audit reproduces all seven RQIR-STAT-001 regressions and adds 10,000 randomized property tests, intentionally rank-deficient nuisance matrices, a shared-versus-separate nuisance check, and correlated-covariance whitening checks.

## Figures and data

All five figures are vector LaTeX/TikZ/PGFPlots sources. The standalone submission-audit script regenerates the diagnostic curve/grid CSV files deterministically from the declared formulas and seeds.

## Build

The manuscript uses REVTeX 4.2 / APS formatting and embeds `thebibliography` so a minimal LaTeX installation can reproduce the PDF without BibTeX. `references.bib` is retained as a machine-readable convenience copy.

```bash
pdflatex main.tex
pdflatex main.tex
pdflatex main.tex
```

## Submission status

The manuscript contains no author or affiliation placeholders. The Paper-I citation is bound to Aleksey Buyanov, working manuscript v0.6, dated 8 September 2026. The Data Availability Statement is bound to exact public audit/data snapshot commit `d0f6453721821fcaec4e9e24ea5e68185d90a5a2`. APS-portal questions about funding, conflicts, related-submission status and optional referees remain author/admin actions rather than scientific manuscript work.
