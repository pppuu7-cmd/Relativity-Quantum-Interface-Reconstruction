# RQIR Research Log — Iteration 051

**Date:** 2026-08-29  
**Target:** test a concrete binary QND ancilla protocol for hidden-amplitude source metrology instead of full energy-level resolution.

## Result

For controlled phase

`U(phi)=exp[-i phi H otimes sigma_z/2]`,

the ancilla coherence is the energy-population characteristic function

`c(phi,alpha)=sum p_i(alpha) exp(-i phi E_i)`.

Optimizing the equatorial ancilla readout quadrature and `phi` gives, for the plus branch,

- `phi*=2.418668`;
- `F_R^(alpha)=0.00389040938` per accepted copy;
- `41.42%` of the projective energy-population Fisher;
- `~4.58%` of the full Toy009 QFI.

This is **RQIR-PREP-003 — binary QND characteristic-function metrology**.

Current plus-copy costs:

- Branch0 `C_alpha=4.55511`: `~1170.86` accepted Ramsey copies;
- best4 residual `C_alpha=0.05006144`: `~12.87` copies.

Transparent 100-Hz cycle-time phase boundaries:

- Branch0 vs best4: accepted Ramsey cycle `~18.23 s`;
- best4 vs best5: `~22.12 min`.

Visibility penalties after reoptimizing phase:

- `V=.9`: Branch0/best4 `~14.18 s`;
- `V=.8`: `~10.83 s`;
- `V=.5`: `~3.93 s`.

The weak-phase Fisher again begins as `O(phi^4)` because the hidden direction is exactly matched in trace and mean energy, confirming that RQIR-NG-024 is not specific to the Gaussian-pointer model.

## Files

- `analysis/qnd_ramsey_ancilla_metrology_iteration051.py`
- `docs/QND_RAMSEY_ANCILLA_SOURCE_METROLOGY.md`
- `recovery/RECOVERY_DELTA_ITERATION_051.md`

## Next gate

Map the five Toy009 levels to a minimal physical oscillator/internal-mode source and provide an explicit controlled-phase rate, ancilla visibility, acceptance and reset time. Compare its achieved energy-metrology Fisher rate with the Branch0/best4 boundary.
