# RQIR Recovery Delta — Iteration 025

**Date:** 2026-08-29

## Authority

Use this delta with `docs/RECOVERY_GUIDE.md` and Iteration-024 recovery delta. Repository state is authoritative.

## Critical new consistency result

The current Toy009 exact NP3 null is **not preserved** if the potential-mean calibration is physically replaced by direct D2 force/gradient mean rows.

Original calibration:

`A n = 0`, rank `24/25`.

For direct force-gradient rows `G` built from `dB/dy` at the same two probe positions and seven times:

- `max |G_i n| ~ 1.43036e-2`;
- RMS `~6.13671e-3`.

Appending these rows gives rank `25/25` and smallest singular value `~3.0014e-3`.

## New label

**RQIR-NG-009 — calibration-observable mismatch:** detector-native calibration observables may change or destroy the declared NP3 null. They cannot be assigned to the old calibration Fisher while retaining old hidden-amplitude assumptions.

## Interpretation

Iteration-022's D2 force-template Fisher formula remains a valid physical Fisher formula, but only for the actual force-calibration Jacobian. It does not automatically implement the existing NP3 potential-row calibration.

RQIR-NG-005 is conditional on `A n=0`. If force calibration has `G n != 0`, the hidden amplitude acquires gravitational calibration information and `F_beta|a` must be recomputed.

## Required branch split

Future D2 resource work must distinguish:

1. **D2 null-preserving calibration:** physically realize the declared NP3 potential/noise observables with an independent beta-blind transducer and retain the existing null analysis.
2. **D2 native-force calibration:** use force/gradient rows, rebuild calibration rank/nullspace and redo source optimization, source-amplitude Fisher, nuisance profiling and wall-clock optimization.

Do not compare D1/D2 SI wall time until this branch choice is explicit.

## Files

- `docs/D2_FORCE_CALIBRATION_NULL_AUDIT.md`
- `analysis/d2_force_calibration_null_audit_iteration025.py`
- `research_log/2026-08-29_iteration_025_d2_force_calibration_null_audit.md`

## Next target

Build both D2 calibration branches and evaluate exact/soft null geometry plus corrected detector-level `F_{beta|theta}`. Preserve RQIR-NUM-001 hard-constraint handling throughout.
