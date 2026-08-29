# RQIR Research Log — Iteration 031

**Date:** 2026-08-29  
**Target:** pass the finite-reference D2 relational-potential calibration from Iteration 030 through the corrected hard-constrained profiled Fisher without redefining the physical Toy009 source.

## Starting point

Iteration 030 established that D2 force integration measures `B(y)-B(y_ref)`, not absolute `B(y)`, and that the resulting calibration matrix remains rank `24/25` while its exact null rotates toward the original NP3 null as the reference is moved outward.

The missing question was whether the finite reference nevertheless self-calibrates the original hidden source amplitude well enough to restore beta identifiability.

## Method

- exact trace+energy elimination;
- fixed Toy009 hidden state from the original absolute-potential null;
- 22 orthogonal hard-constrained source nuisances;
- corrected D2 two-band detector response;
- relational mean and covariance rows rebuilt consistently for each `y_ref`;
- corrected D2 weights `gamma_mean=2.414e6`, `gamma_cov=0.929e6`;
- profiled `F_beta|theta`, not calibration rank alone.

## Result

Finite reference gives nonzero calibration Fisher on the old hidden amplitude but does not recover beta identifiability without source metrology.

Representative values:

- `y_ref=-5`: `I_amp~3.18167`, `F_beta(C_a=0)~8.1742e-5`, new-null detector alignment `~0.9999573`;
- `y_ref=-10`: `I_amp~0.671908`, `F_beta~1.2329e-5`, alignment `~0.9999936`;
- `y_ref=-100`: `I_amp~2.8486e-4`, `F_beta~1.2490e-8`, alignment `~0.999999993`.

The calibration exact null rotates into a nearby source direction that is almost perfectly aligned with the beta detector signal.

## New gate

**RQIR-NG-012 — relational-null substitution obstruction:** nonzero Fisher information about a previously hidden source amplitude does not imply nonzero profiled Fisher for beta when the full calibration operator retains another detector-aligned exact null.

Thus `I_cal(old amplitude)>0` is not a sufficient identifiability criterion.

## 90% preparation frontier at lambda=1

`C_a*` values:

- `y_ref=-4`: `15.48`;
- `-5`: `16.65`;
- `-7.5`: `19.36`;
- `-10`: `21.92`;
- `-20`: `31.59`;
- `-50`: `59.67`;
- `-100`: `106.20`.

With strong preparation metrology, the minimum calibration multiplier for 90% retention increases from `~0.464` at `y_ref=-4` to `~0.913` at `y_ref=-100`.

## Interpretation

Moving the reference outward simultaneously worsens native `q_pot` (Iteration 030) and drives the Fisher geometry back toward the original NP3 null, increasing source-metrology demand. The costs reinforce rather than cancel.

No new physics is claimed; this is a finite Toy009 inference/resource result.

## Files

- `analysis/d2_finite_reference_profiled_fisher_iteration031.py`
- `docs/D2_FINITE_REFERENCE_PROFILED_FISHER.md`
- `recovery/RECOVERY_DELTA_ITERATION_031.md`

## Next gate

Jointly minimize the normalized physical wall-clock objective over `(y_ref,lambda,C_a)` using heterogeneous finite-reference `q_pot,i`, then compare that optimized relational branch against native-force replacement and augmented calibration on the same corrected D2 Fisher basis.
