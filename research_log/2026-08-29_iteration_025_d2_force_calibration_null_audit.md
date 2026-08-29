# RQIR Research Log — Iteration 025

**Date:** 2026-08-29

## Target

Audit whether the D2 force-template calibration introduced parametrically in Iteration 022 can be treated as a physical implementation of the existing Toy009 NP3 potential-mean calibration without changing the nullspace.

## Work completed

1. Reconstructed the authoritative Toy009/Iteration-011 24x25 row-normalized calibration matrix.
2. Recovered its exact one-dimensional hidden direction `n` with `A n ~ 0`.
3. Constructed 14 direct Newtonian force/gradient mean rows using `dB/dy` at the same two probe positions and seven stored times.
4. Tested all force rows against `n`.
5. Appended the force rows to the original calibration matrix and recomputed rank/singular values.

## Numerical checks

Original NP3 matrix:

- shape `24x25`;
- rank `24`;
- smallest nonzero stored singular value `~1.9995404e-3`;
- `||A n|| < 1e-12`.

Direct force-gradient rows:

- max hidden-direction projection `~1.43036e-2`;
- RMS projection `~6.13671e-3`.

Augmented calibration:

- rank `25/25`;
- smallest singular value `~3.0014e-3`.

Therefore the old exact null does not survive detector-native force calibration.

## New retained result

**RQIR-NG-009 — calibration-observable mismatch:** a detector-native observable cannot be substituted for an NP3 calibration observable while silently retaining the old nullspace. In current Toy009, direct force-gradient mean calibration detects the hidden source direction and removes the exact one-dimensional null.

## Consequences

- RQIR-NG-005 remains valid for the declared exact-null calibration `A n=0`.
- If D2 force-gradient calibration is actually performed, gravitational calibration acquires information on the hidden amplitude and the Fisher problem must be rebuilt.
- Iteration-022 D2 force-template Fisher rate remains mathematically valid, but it belongs to the actual force-calibration Jacobian, not automatically to the existing NP3 potential-row Fisher.
- D2 physical resource accounting must branch into a null-preserving calibration protocol and a detector-native force calibration protocol.

## Scientific status

No new-physics claim. This is an internal detector/calibration consistency result inside G13.

## Files

- `analysis/d2_force_calibration_null_audit_iteration025.py`
- `docs/D2_FORCE_CALIBRATION_NULL_AUDIT.md`
- `recovery/RECOVERY_DELTA_ITERATION_025.md`

## Next gate

Construct both D2 calibration branches explicitly and recompute detector-level `F_{beta|theta}`, hidden-amplitude identifiability, nuisance/profile degeneracies and wall-clock resource cost before comparing D1 with D2.
