# RQIR Research Log — Iteration 058

**Date:** 2026-08-30  
**Target:** compare finite-resolution Gaussian QND pointer and Ramsey ancilla source metrology on the same Toy012 reset-aware Fisher-rate target.

## Input from Iteration 057

At `y_ref=-4`, best four added force-covariance rows beat no-extra-force-covariance only if independent source metrology is slower than

`R_alpha~2.20253e-5 s^-1`

under the transparent covariance lower-bound comparison.

## Pointer result

Balanced Toy012 finite Gaussian energy pointer:

- projective energy Fisher ceiling `F_E^alpha~0.00629727`;
- zero-reset rate optimum `r~1.44273`;
- `max R/(p_E Gamma_E)~0.00425193`.

At `p_E=.5`, zero-reset threshold is

`Gamma_E~0.01036 s^-1`.

## Ramsey result

Balanced Toy012:

- zero-reset rate optimum `phi~1.57508`;
- `max R/(p_E Omega_E)~0.00213429`;
- per-copy Ramsey maximum `F_R,max~0.00349867`.

At `p_E=.5`, zero-reset rate threshold is

`Omega_E~0.02064 s^-1`.

The coupling normalizations are protocol-specific and must not be equated without a common hardware Hamiltonian.

## New retained result

**RQIR-RESOURCE-027 — per-copy Fisher imposes a hard reset ceiling.**

For any independent source-metrology protocol,

`R_alpha <= p_E F_max/t_reset`.

Therefore source reset/preparation alone can make a branch target impossible, regardless of measurement strength.

For Toy012, p=.5 and the current branch0/best4 target:

- Gaussian pointer reset ceiling `~142.96 s`;
- Ramsey reset ceiling `~79.42 s`.

Representative coupling thresholds:

- reset 1 s: pointer `Gamma~0.01057`, Ramsey `Omega~0.02091 s^-1`;
- reset 10 s: pointer `~0.01259`, Ramsey `~0.02373 s^-1`.

Record **RQIR-PREP-004**: fresh-copy throughput is an architecture variable, not a secondary overhead.

## Decision

Source-amplitude metrology is now sufficiently closed at the resource-model level. Move next to a total Toy012 D2 wall-clock budget including absolute detector signal, mean calibration, source metrology, timing/additive controls and science integration.

## Files

- `analysis/toy012_pointer_ramsey_reset_surface_iteration058.py`
- `docs/TOY012_POINTER_RAMSEY_RESET_SURFACE.md`
- `recovery/RECOVERY_DELTA_ITERATION_058.md`