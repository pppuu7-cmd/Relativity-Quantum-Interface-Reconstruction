# RQIR Research Log — Iteration 222

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Question

Does the physical `MSSC-001` connected-source cut have a universal collinear residue fixed by the same complete Born amplitude?

## Frozen test

Five scattering angles, plus/cross external spin-2 states, local delta samples `[0.01,0.005,0.002,0.001,0.0005]`. No cap-integral fitting.

## Result

For both incoming and outgoing collinear directions,

`R = lim (1-cos delta) I_cut = -8 M_Born`

in the stripped source-amplitude normalization.

Worst cross-kinematic extrapolated error from `-8`: `3.15e-6`. Worst incoming/outgoing mismatch: `3.54e-6`.

## Retained

`SRC-CUT-003`, `IR-NG-006`, `NG-FUNNEL-078`.

## Readiness

`MODEL_READINESS: 23%` — unchanged.

## Next gate

Subtract the two Born-fixed collinear pole terms locally and verify that the remaining cut kernel is phase-space integrable. Only then attempt a regulator-independent hard-remainder integral.
