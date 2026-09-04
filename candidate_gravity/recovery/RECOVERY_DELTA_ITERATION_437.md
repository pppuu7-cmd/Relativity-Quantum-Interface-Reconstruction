# RECOVERY DELTA — ITERATION 437

**Status at allocation:** prospectively frozen; result not yet consumed.  
**Authority target:** Iteration-270 `Q1` 80/120-digit precision closure only.  
**Prerequisite:** raw-valid Iteration 436 `N1` precision closure PASS.  
**MODEL_READINESS:** 24% at launch.

## Frozen object

`Q1(M,x,P0,h) = -Q0(P0+k_x) @ N1(M,x,P0,h) @ Q0(P0)`

for `M=POS`, legs `s/a/b`, unchanged `h=3e-5` and exact Iteration-270 kinematics.

`Q0` is evaluated from the parent definition `inverse(norb([],[],p))` at `P0` and each exact shifted momentum `P0+k_x`.

## Frozen acceptance before result

- 80 and 120 decimal digits;
- `max_scaled(Q0_80-Q0_120) <= 1e-40`;
- `max_scaled(Q0_binary64-Q0_120) <= 1e-12`;
- `max_scaled(Q1_80-Q1_120) <= 1e-40`;
- all Q0/N1/Q1 values finite;
- legacy binary64 Q1 vs Q1_120 classified against `2e-5` without changing downstream thresholds.

PASS certifies only Q1 at this scope. `Asub/Acoef/A_finite` remains downstream.
