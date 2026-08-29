# RQIR Recovery Delta — Iteration 051

**Date:** 2026-08-29

## New constructive source-metrology protocol

A binary QND Ramsey ancilla can measure an optimized Fourier component of the Toy009 energy populations without resolving all five levels.

Controlled phase:

`U(phi)=exp[-i phi H otimes sigma_z/2]`.

Ancilla coherence:

`c(phi,alpha)=sum_i p_i(alpha) exp(-i phi E_i)`.

At ideal visibility, plus branch optimum:

- `phi*=2.418668`;
- `F_R^(alpha)=0.00389040938` per accepted copy;
- `41.42%` of projective energy-population Fisher;
- `~4.58%` of full Toy009 QFI.

**RQIR-PREP-003:** binary QND characteristic-function metrology is a viable simpler source-calibration channel in Toy009.

Current accepted plus-copy costs:

- Branch0: `~1170.86` Ramsey copies;
- best4 residual: `~12.87` Ramsey copies.

Transparent 100-Hz accepted-cycle boundaries:

- Branch0 vs best4: `t_R~18.23 s`;
- best4 vs best5: `t_R~22.12 min`.

Finite visibility makes these stricter:

- `V=.9`: Branch0/best4 `~14.18 s`;
- `V=.8`: `~10.83 s`;
- `V=.5`: `~3.93 s`.

RQIR-NG-024 remains: weak Ramsey phase also gives `F~phi^4` because trace and mean energy are exactly matched.

Use this protocol on independent/sacrificial source copies; RQIR-NG-023 still forbids assuming strong same-copy energy readout preserves ordered-response coherence.

## Files

- `analysis/qnd_ramsey_ancilla_metrology_iteration051.py`
- `docs/QND_RAMSEY_ANCILLA_SOURCE_METROLOGY.md`
- `research_log/2026-08-29_iteration_051_qnd_ramsey_ancilla_metrology.md`

## Next

Audit the physical realizability of the current Toy009 five-level source itself by reconstructing its Hamiltonian in the radius/probe eigenbasis. Determine whether a local multiwell/tight-binding implementation exists naturally or whether the present detector-aware source geometry requires dense/nonlocal couplings.
