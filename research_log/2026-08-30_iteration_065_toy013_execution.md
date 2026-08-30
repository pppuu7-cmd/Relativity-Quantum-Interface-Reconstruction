# RQIR Research Log — Iteration 065

**Date:** 2026-08-30

## What was done

Executed the previously unrun Iteration-064 Toy013 deterministic search rather than duplicating any closed branch. The run used the repository-defined seed, 30k exact nearest-neighbour candidates, harmonic-balance and conditioning cuts, then the Iteration-063 spectral-tilt-profiled centered Fisher audit.

## Result

137/30000 candidates passed the cheap hard cuts; 120 were audited. The leading calibration-cost point is trial 29100.

Exact properties:

- `s_min=1.3291881226e-3`, condition `3527.2295`;
- harmonic balance `0.9047551404`;
- non-nearest coupling norm `3.42e-16`;
- hidden-state minima `0.1206413852`, `0.1200000000`;
- calibration-null residual `5.55e-17`;
- normalized tilt-profiled beta Fisher `1.0`.

Physical calibration metric:

- total weighted cost `3.5819942712e6`;
- `gamma_mean=1.2086865290e5`;
- `gamma_cov=2.3622914132e5`;
- cost ratio to Toy009 `0.1233011369`.

Counter-costs:

- `S_eff=2.4438110707e-5`, ratio to Toy009 `0.04228407350`;
- full `F_Q^alpha=0.08073047882` (~0.9505 Toy009);
- energy-population Fisher `4.54142493e-5` (~0.004835 Toy009);
- zero-reset Ramsey Fisher-rate coefficient `7.6258e-6` (~0.003022 Toy009).

## Interpretation

Retain **RQIR-DESIGN-006**: calibration geometry, absolute detector science signal, and independent source-metrology accessibility are separate resource axes. Trial 29100 is a calibration-optimal local Pareto point, not an overall baseline.

No new-physics claim. NG-005, NG-006, NG-023, NG-026 and all open consistency gates remain active.

## Next

Construct a common total wall-clock objective for Toy009/Toy011/Toy012/Toy013 including science exposure, calibration, independent source metrology, reset/dead time, coherence and controls. Promotion of Toy013 is forbidden until that gate is passed.
