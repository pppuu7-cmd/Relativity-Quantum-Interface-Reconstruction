# RQIR Research Log — Iteration 118

**Date:** 2026-08-31

## Question

What is the actual calibration nuisance rank for Toy009/Toy014 after hard constraints, and are any of the seven mean layers or eight centered-covariance rows exactly redundant?

## Result

The hard-constrained source-nuisance basis has dimension `22`.

For both Toy009 and Toy014:

- `rank(A_m)=14` for the 14 mean rows;
- each of the seven same-time dual-probe mean layers contributes exactly `2` new directions;
- `rank(A_c)=8` for the centered-covariance rows;
- after the full mean span is present, each of the eight covariance rows contributes exactly `1` new direction;
- `rank([A_m;A_c])=22`.

Thus the current calibration requirement is full rank on the 22D nuisance space. Mean-only repetition cannot replace covariance calibration. A single four-real transfer setting can add at most four directions and therefore cannot replace the full eight-dimensional covariance complement of the mean span.

Conditioning diagnostics:

- Toy009 full calibration `s_min=0.00212667906656`, condition `~409.926`;
- Toy014 full calibration `s_min=0.00150105788788`, condition `~650.582`.

Labels:

- **RESOURCE-087:** full 22D calibration-span certificate.
- **NG-075:** no exact removable mean layer in the current span.
- **NG-076:** mean-only calibration cannot replace centered covariance.
- **RESOURCE-088:** at least two distinct four-real settings would be needed even dimensionally to replace all eight covariance-complement directions.

## Reproducibility

`analysis/toy009_toy014_calibration_span_iteration118.py` reconstructs both architectures and verifies all rank increments and singular-value regressions.

## Readiness snapshot

Project-management estimates, not statistical quantities:

- Paper III scientific-content readiness: **91%**.
- Paper III submission readiness: **72%**.
- Repository readiness to begin a concrete Candidate-Gravity model: **84%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Next gate

Use the stored covariance endpoint/backaction graph to determine which same-time calibration observables can actually share one physical acquisition. Then solve the minimum physical setting cover and feed it into RESOURCE-083 without double counting.
