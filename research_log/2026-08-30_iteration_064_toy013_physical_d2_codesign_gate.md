# RQIR Research Log — Iteration 064

**Date:** 2026-08-30

## Result

Repository source-of-truth review found the active front at Iteration 063, not the older Iteration-060 wall-clock branch. Iteration 063 demoted Toy012 as a physical D2 baseline because spectral-tilt profiling increases its centered calibration cost by orders of magnitude relative to Toy009.

The next non-duplicative gate has therefore been implemented as a deterministic Toy013 search in `analysis/toy013_physical_d2_codesign_iteration064.py`.

The search uses exact nearest-neighbour Jacobi sources only. Cheap ranking uses the physical tilt-profiled two-band D2 information `S_eff`, an explicit harmonic-balance floor, and conditioning. The expensive survivor audit uses the full Iteration-063 spectral-tilt-profiled centered calibration Fisher.

Retained design rule **RQIR-DESIGN-005**: local source co-design must protect every detector band needed after nuisance profiling; neither scalar raw response nor Euclidean detector norm is sufficient when a nuisance direction can eliminate one band.

## Numerical status

No Toy013 winner is claimed in this iteration because the deterministic 30k-candidate / 120-survivor computation has not yet been executed in an available runtime. The repository now contains the reproducible gate and exact assertions required to promote a candidate safely once executed.

## Next

Execute Iteration 064, retain only exact-positive/local survivors, compare physical calibration cost to Toy009 and Toy011, then propagate the winning candidate into source-metrology and absolute wall-clock budgeting. Do not restore Toy012 as baseline unless it passes this physical detector metric.