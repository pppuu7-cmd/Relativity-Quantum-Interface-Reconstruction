# RQIR Research Log — Iteration 221

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Construction

Use only the pure-Einstein gauge-invariant `MSSC-001` two-scalar/two-graviton tree amplitudes on both sides of a scalar+graviton two-particle cut of gravitational Compton scattering.

The physical intermediate graviton sum uses plus/cross spin-2 polarizations.

## Checks

- transverse polarization-basis rotation changes the summed kernel by at most `3.96e-16` relative;
- incoming-graviton collinear log-log slope `-1.98791`;
- outgoing-graviton collinear slope `-1.98356`;
- antipodal directions remain finite.

Hence the connected source cut is gauge-safe at amplitude level but its phase-space integral is logarithmically IR divergent.

## Retained

`SRC-CUT-001`, `SRC-CUT-002`, `IR-NG-005`, `NG-FUNNEL-077`.

## Readiness

`MODEL_READINESS: 23%` — unchanged.

## Next gate

Factorize the two collinear residues against the complete scalar Compton Born amplitude. Do not fit residue coefficients from regulated angular integrals. If a universal Born-fixed relation exists, use it to define the next hard-remainder/inclusive gate.
