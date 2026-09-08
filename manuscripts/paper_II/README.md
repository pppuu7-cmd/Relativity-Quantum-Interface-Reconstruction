# RQIR Article II - Physical Review Research manuscript

Working title:

**Relativity--Quantum Interface Reconstruction II: Nuisance-Profiled Statistical Identifiability in Calibration-Nullspace Observables**

Target journal: **Physical Review Research**.

## Scientific role in the series

Paper I establishes algebraic observability after detector-calibration null projection. Paper II asks the next question: whether the surviving target deformation is locally distinguishable from remaining physical/phenomenological nuisance directions, and whether the retained information is large enough to be experimentally useful.

The manuscript deliberately separates:

1. algebraic observability;
2. local statistical identifiability;
3. finite-data detectability.

## Current headline results

- Projection--Schur equivalence for nuisance-profiled Fisher information, including rank-deficient nuisance blocks through the Moore--Penrose pseudoinverse.
- Local first-order identifiability criterion: the whitened target tangent must have a component outside the nuisance tangent span.
- Monotonicity: enlarging the unconstrained nuisance tangent space cannot increase profiled information.
- Shared-vs-branch-specific theorem: fitting independent nuisance copies branch-by-branch is no more informative than a correctly shared nuisance fit.
- Signed/global RQIR benchmark: structurally identifiable but quantitatively extremely weak under the locked physical normalization.
- Positive/local RQIR benchmark: zero profiled Fisher information at the locked audit point after roundoff clipping; exposure alone cannot repair the local degeneracy.

## Build

The source is REVTeX 4.2 and uses the `prresearch` journal option.

```bash
pdflatex main.tex
```

The working source currently contains an inline bibliography so it also builds in minimal LaTeX environments. A `references.bib` file is retained alongside it for the final APS/BibTeX submission workflow.

## Pre-submission items still open

- Replace `Author Name` and institutional placeholders with final metadata.
- Give RQIR I its final bibliographic status (submitted/preprint/DOI) and update the self-citation.
- Re-run the historical Nim nonlinear-profile programs end-to-end in an environment with the required Nim runtime; the locked arithmetic is already regression guarded in Python.
- Archive the exact code/data snapshot (e.g. Zenodo or equivalent) and replace the Data Availability placeholder with a permanent link/identifier.
- Complete a final claim-to-artifact audit and journal copy edit.

The present PDF should therefore be treated as a **PRR-formatted working submission draft**, not yet as the final uploaded journal version.
