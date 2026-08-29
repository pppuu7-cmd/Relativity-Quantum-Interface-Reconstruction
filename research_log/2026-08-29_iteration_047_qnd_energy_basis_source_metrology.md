# RQIR Research Log — Iteration 047

**Date:** 2026-08-29  
**Target:** test exact-QND/backaction-evading source observables as an escape from the reciprocal linear shared-monitoring obstruction.

## Result

Because the Toy009 Hamiltonian has nondegenerate spectrum, exact Hermitian QND observables are energy-diagonal. After exact trace+energy removal this leaves a three-dimensional hard QND sector.

For the centered finite-reference relational branch at `y_ref=-4`:

- hard rank without QND diagonal rows: `22/23`;
- with complete three-row diagonal QND basis: `23/23`.

This is **RQIR-CAL-016**: the current relational null is locally visible to the QND diagonal sector.

A simple projective energy-basis population measurement gives fractional-amplitude Fisher

- plus branch: `F_E^alpha~=0.00939188`;
- minus branch: `~0.00957913`;
- plus/minus pair: `~0.0189710`.

The plus-branch measurement extracts about `11.1%` of the full Toy009 QFI per accepted copy. This is **RQIR-PREP-002**.

For current best4 residual `C_alpha=0.05006144`, the ideal information cost is only

- `~5.33` accepted plus-branch copies, or
- `~2.64` plus/minus pair equivalents.

However, exact QND relative to `H` is not response-preserving on the same science copy. Complete projective energy dephasing leaves only `~0.29848` of the D2 response norm, with direction alignment `~0.82052`.

This is **RQIR-NG-023 — QND is not equivalent to ordered-response nondemolition**.

## Interpretation

Energy-basis metrology is promising as an **independent/sacrificial source-verification channel**, not as strong shared science monitoring. It is far simpler than the ideal `Delta0`-eigenbasis measurement and may make source metrology much cheaper than covariance completion.

## Files

- `analysis/qnd_energy_basis_source_metrology_iteration047.py`
- `docs/QND_ENERGY_BASIS_SOURCE_METROLOGY.md`
- `recovery/RECOVERY_DELTA_ITERATION_047.md`

## Next gate

Use the explicit energy-basis Fisher rate in the D2 branch phase diagram and determine when no-extra-force-covariance, best4, or best5 is actually cheapest.