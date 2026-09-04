# RQIR Candidate Gravity — Research Log Iteration 431

## Question

Does the Iteration-430 nominal first precision-port stage `368/370` actually contain all numerical primitives that must be arbitrary-precision certified before the Iteration-424 fallback?

## Result

No. Source-level dependency audit establishes a hidden numerical parent boundary beneath Iteration 368.

Iteration 368 executes the prefix of `iteration270_vd_physical_b3_nonzero.py` and binds `ETA`, `Q0`, `Q1`, `Asub`, and `y_down`. Iteration 370 then executes the setup/block definitions from 368. The actual precision provenance therefore begins at

`270[Q0,Q1,Asub,y_down plus recursive numerical dependencies] -> 368/370`.

The relevant Iteration-270 layer is not symbolic-only. It contains NumPy floating/complex arrays, matrix inversions/determinants/norms and finite differences (`N1`, `N2`, `Acoef/Asub`). Consequently, arbitrary-precision arithmetic only around the Iteration-368/370 wrappers would leave a hidden binary64 numerical core and cannot be called a complete stage-1 precision certificate under Iterations 429/430 unless explicit retained-binary64 error bounds are proved.

## Scientific classification

`PASS_CHANNEL2_STAGE1_PARENT_PRECISION_BOUNDARY_CLOSURE__NON_PROMOTING`

This is a methodological/provenance PASS and a negative implementation finding against the shallower boundary assumption. It is not a Candidate-Gravity consistency FAIL, not an exact comparator identity, not regime-specific non-identifiability, not near-degeneracy, and not a novelty certificate. No physical coordinate is promoted.

## Frozen consequences

- Iteration-424 thresholds remain unchanged: `epsilon_mass <= 2e-5`, direct-original `<=2e-6`, tensor-(1,1) fit `<=2e-5`, `|D_s(80)-D_s(120)|<=2e-6`, finite outputs.
- Same dynamics, routing, numerator, sign, normalization, mass nodes and finite-difference definitions remain mandatory.
- No smaller `h`, threshold weakening, zero-fill, ANSATZ-003, Fisher, or resources are allowed.
- Exact15 remains blocked by physical index 2.

## Readiness

`MODEL_READINESS: 24%`

Change: **0 percentage points** from Iteration 430. The dependency boundary is now fail-closed, but no stable readiness-rubric block has been newly closed.

Rubric remains: comparator foundation `24/25`; unique residual `0/20`; frozen parent dynamics/ANSATZ `0/20`; consistency/positivity/Ward/causality `0/15`; identifiability/Fisher `0/10`; resource/experiment closure `0/10`.

## Next gate

Implement or quantitatively certify the Iteration-270 parent primitives `Q0/Q1/Asub/y_down` and recursive numerical operations at 80/120-digit provenance. After this inner closure passes, certify 368/370 and continue 379/374 -> 407 -> frozen Iteration-424 80/120 evaluation -> Iteration-427 oracle.
