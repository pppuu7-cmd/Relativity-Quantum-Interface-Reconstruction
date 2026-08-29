# RQIR Research Log — Iteration 052

**Date:** 2026-08-29  
**Target:** convert the QND Ramsey-ancilla source-metrology channel from Fisher/shot to Fisher/sec and map it onto the current D2 Branch0/best4/best5 decision thresholds.

## Result

Iteration 051's per-copy optimum (`phi~2.4187`) is not the wall-clock optimum.  With controlled phase `phi=Omega_E T` and negligible reset,

`R_E = p_E Omega_E F_alpha(phi)/phi`.

Optimizing `F_alpha(phi)/phi` gives

- `phi_rate ~= 1.092306912`;
- `F_alpha ~= 0.002756370099` per accepted plus-branch shot;
- `F/F_projective ~= 0.293484246`;
- `R_E/(p_E Omega_E) ~= 0.002523439217`.

This establishes **RQIR-RESOURCE-024**: Ramsey Fisher/copy and Fisher/time have different optimal phases.

Using Iteration 050's physical rate thresholds,

- Branch0/best4: `R_E=2.13404e-4 s^-1`;
- best4/best5: `R_E=2.93122e-6 s^-1`,

for `p_E=0.5` the required controlled phase rates are

- `Omega_04 ~= 0.16913742 s^-1`;
- `Omega_45 ~= 0.002323194 s^-1`.

At the Branch0/best4 boundary, the rate-optimal Ramsey interaction lasts only `~6.458 s` before reset/readout overhead.

## Meaning

The abstract source-preparation Fisher parameter has now been translated into a concrete ancilla-coupling requirement.  A future physical source implementation can be inserted through `(Omega_E, visibility, p_E, t_reset)` without redoing the Toy009/Toy010 hard-nuisance geometry.

This remains independent/sacrificial source metrology; NG-023 still forbids treating QND-with-H as automatically nondemolition for the ordered-response science copy.

## Files

- `analysis/qnd_ramsey_rate_budget_iteration052.py`
- `docs/QND_RAMSEY_RATE_BUDGET.md`
- `recovery/RECOVERY_DELTA_ITERATION_052.md`

## Next gate

Include finite visibility and fresh-copy reset explicitly in

`R_E = p_E F_alpha(phi,V)/(t_reset + phi/Omega_E)`

and derive the Branch0/best4 boundary surface in `(Omega_E,V,p_E,t_reset)`.