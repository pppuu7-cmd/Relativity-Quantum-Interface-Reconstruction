# Iteration 429 Recovery Delta

**Date:** 2026-09-04  
**MODEL_READINESS:** 24% (unchanged)  
**Authority:** implementation manifest; non-promoting  
**Raw-valid run:** 33887876664  
**Job:** 101072041025  
**Artifact:** 9942593929  
**Artifact digest:** `sha256:18b10e47179e4bcd464d02d7d63cb4fbfa2a087c3a88c37f84523f7044d82a5f`  
**Raw scientific JSON SHA-256:** `e45b004510953ddaa1de7f2be84bb9642bfe9cdc91987396b5fc1947c8e54da1`

## What was closed

The full fixed-mass `F(u,v)` dependency chain relevant to the authorized Iteration-424 high-precision fallback was bound fail-closed as

`407 -> 379 -> 374 -> 370 -> 368`.

The manifest verifies that a true 80/120-digit implementation cannot start at the final mass derivative only. The following lower layers must either be ported to arbitrary precision or separately certified:

1. kinematics and basis construction;
2. phi mean and degree-4 interpolation;
3. analytic affine moments;
4. radial stripped-limit Richardson evaluation;
5. traced numerator transport;
6. nested parent derivatives in Iteration 368;
7. the final frozen mass-node / cross-precision logic.

The current source contains explicit binary64 anchors including NumPy complex arrays and polynomial fitting in Iteration 407, NumPy trace/matrix operations in the routed numerator layer, and nested finite-difference derivative machinery in Iteration 368.

## Required implementation order

The next implementation should proceed deepest-first:

1. port/certify the Iteration-368/370 traced numerator primitives;
2. port the Iteration-379/374 radial stripped-limit wrapper while keeping frozen radial nodes and Richardson algebra;
3. port the Iteration-407 complete fixed-mass analytic/spectral `F` including polynomial solve and affine moments;
4. evaluate the Iteration-424 frozen mass nodes independently at 80 and 120 decimal digits under its pre-frozen fail-closed acceptance rules;
5. compare against the non-promoting Iteration-427 full-H factorized oracle.

Finite-difference truncation and arithmetic precision are distinct error sources. More digits do not by themselves cure truncation from the inherited derivative definitions.

## Current physical authority

- double-double index 2 remains **not promoted**;
- Iteration 421 remains raw-valid `BLOCKED_CONVERGENCE`;
- Iteration 412 exact15 remains blocked;
- Iteration 426 phi-resolution diagnostic is still independently running at this checkpoint;
- `MODEL_READINESS = 24%`.

## Guardrails

No threshold weakening, no smaller mass step, no numerator/routing/sign/normalization change, no zero fill, no `ANSATZ003`, and no Fisher/resource claims.
