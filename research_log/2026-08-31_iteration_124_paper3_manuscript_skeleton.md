# RQIR Research Log — Iteration 124

**Date:** 2026-08-31

## Question

Does Paper III now have a continuous claim/evidence chain suitable for manuscript drafting, or is there still a missing theoretical/resource bridge that must be solved first?

## Result

A manuscript-ready skeleton was built with eight central sections covering:

1. theoretical discriminant -> detector identifiability;
2. independent source-preparation metrology;
3. calibration Fisher -> shots/SNR/coherence/wall time;
4. transfer gain/phase and control recertification inside the likelihood;
5. non-double-counted campaign scheduling plus rank/span coverage;
6. Toy009/Toy014 detector-side robust rate interval;
7. final-significance `(u,v,z,delta)` architecture certificate;
8. experimental precedent and minimum apparatus closure vector.

Every section is tagged by claim class, core equation/result, figure/table target, literature comparator and explicit limitation. The checker enforces that the detector architecture section remains `PARAMETRIC+REGRESSION` rather than being promoted to an apparatus prediction, and that experimental precedent is not presented as validation of an RQIR signal.

The gap audit finds no missing abstract Fisher/resource link between the established stages. The remaining scientific gap for a **numerical apparatus verdict** is a compatible same-apparatus data vector: two-band PSD/cross-PSD/transduction, full transfer-reference Fisher, calibration-layer rates, covariance/backaction compatibility, geometry/additive SI controls, drift/recertification, source-metrology rate and duty.

### NG-082

Manuscript closure is not apparatus closure. A parametric end-to-end certificate must not be worded as a completed experimental forecast.

### DESIGN-020

Experimental characterization should target the full closure vector needed by `(u,v,z,delta)`, not isolated headline sensitivities whose improvement leaves another nuisance block unresolved.

## Reproducibility

Canonical checker:

`analysis/paper3_manuscript_skeleton_iteration124.py`.

Canonical manuscript architecture:

`docs/PAPER_III_MANUSCRIPT_SKELETON_ITERATION124.md`.

A duplicate preliminary checker created during the same iteration was removed so that Iteration 124 retains one canonical analysis authority.

## Readiness snapshot

Project-management estimates, not statistical quantities:

- Paper III scientific-content readiness: **96%**.
- Paper III submission readiness: **86%**.
- Repository readiness to begin a concrete Candidate-Gravity model: **85%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Next gate

Run the final Paper-III notation/dependency/reproducibility audit: canonicalize symbols, map every manuscript claim to exact repository evidence, identify stale formulas or label collisions, and produce the minimum figure/table generation command list. This is the last high-value gate before prose drafting, unless a RESOURCE-094-compatible apparatus dataset becomes available.
