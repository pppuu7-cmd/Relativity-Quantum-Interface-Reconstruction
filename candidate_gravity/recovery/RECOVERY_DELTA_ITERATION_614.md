# Recovery Delta — Iteration 614

**Date:** 2026-09-08  
**MODEL_READINESS:** 24%  
**Authority:** `PASS_ITER614_FROZEN_NATIVE_S_SCALAR_POLE_ROOT_AND_JACOBIAN_AUDIT__NON_RESIDUAL`

## Frozen basis

Iter613 prospectively froze `MSSC001-NATIVE-S-KIN-V1` before pole inspection. Iter614 changes none of its choices.

## New authority

Under `p0(s)=(sqrt(s),0,0,0)`, `s>0`, MSSC-001 `(+---)`, `m=0.7` and exact Iter368/588 mode vectors:

- `D_s^+`: no positive root;
- `D_s^-`: `s=0.09`, `2.89`;
- `D_a^+`: `s=1.241314274283428`;
- `D_a^-`: `s=0.09868572571657197`;
- `D_b^+`: `s=1.726971411425142`;
- `D_b^-`: `s=0.013028588574858`.

All six supported points are simple and distinct. Minimum root separation is `0.00868572571657195`.

Absolute Jacobians:

- `D_s^-(0.09)`: `2.333333333333333`;
- `D_s^-(2.89)`: `0.4117647058823529`;
- `D_a^+`: `0.6409796081665314`;
- `D_a^-`: `2.273306106119183`;
- `D_b^+`: `0.54342862858286`;
- `D_b^-`: `6.25657137141714`.

Therefore ordinary simple-root pullback is valid at all supported points:

`delta(D_A(s)) = sum_r delta(s-s_r)/|partial_s D_A(s_r)|`.

K1/K2 support: `5/6` routed terms. K1^3 support: `6/6` ordered chains. K3 remains local in this scalar-pole classification. All 13 source families remain retained; `zero_fill=false`.

## Convention warning

Source-sector q squares under `(+---)` are `(+1,+0.14,+0.34)`. They are not the Iter582 connection-sector q2 labels `(-1,-0.14,-0.34)` and must not be merged or summed.

## Still blocked

- MSSC-001 source numerator/routing-sign values at supported roots;
- treatment of any products after checking that only one retained routed denominator vanishes at each supported point;
- native Iter205 `Y/T_cut` sign/normalization binding to Iter582;
- Source/Born subtraction;
- comparator quotient and robust residual;
- `ANSATZ-003`, Fisher/resources.

## Exact next gate

Evaluate numerator/sign data on the six frozen simple-root points from the unchanged Iter594/605 object. Do not alter `MSSC001-NATIVE-S-KIN-V1` and do not promote `D_s^+` support absence into an amplitude zero statement.
