# RECOVERY DELTA — Iteration 628

Date: 2026-09-09

Classification:
`PASS_ITER628_RETARDED_INTERNAL_SCALAR_POLE_COEFFICIENTS__RAW_VALID__NON_RESIDUAL`.

Iteration 627 fixes the measured scalar probe to `G_phi^{ra}=G_R`, so every surviving internal scalar line is retarded. With the frozen source inverse denominator `D=m^2-r^2`, the induced prescription is

`D_ret = D - i0 sign(r0)`.

Therefore

`Disc_s[1/(D-i0 sign(r0))]/(2*pi*i)=sign(r0) delta(D)`,

and at each Iter614 simple root

`w_R = sign(r0) C_A / |partial_s D_A|`.

Using unchanged Iter615 numerators and Iter625 energy signs gives, in strict ascending-s order:

1. `D_b^-(0.013028588574858)`: `+0.00024912100468199333`;
2. `D_s^-(0.09)`: `+0.0007390333386357164`;
3. `D_a^-(0.09868572571657197)`: `-0.00019432750619153956`;
4. `D_a^+(1.241314274283428)`: `-0.0012850179378006798`;
5. `D_b^+(1.726971411425142)`: `+0.0007467205092433387`;
6. `D_s^-(2.89)`: `+0.0021373920072305223`.

Thus all five positive-energy roots have the opposite discontinuity sign from the historical common `K+i0` Iter615 weights, while the single negative-energy root `D_s^-(0.09)` retains the same sign. This relation is derived once from the frozen retarded propagator and is not a root-by-root hand flip.

All six roots remain supported; `D_s^+` remains `NO_POSITIVE_ROOT`, not amplitude zero. All 13 source families remain retained; `zero_fill=false`. Source/Born subtraction and native projection are `NOT_PERFORMED`. No Iter582 Candidate values were used.

Raw authority: Actions run `34285257942`, job `102259232746`, head `4acbf3dba5f88c51ffb52feca2db77b2ef40d6fc`, artifact `10079192751`, digest `sha256:353c4d1df3ca373b63da504ee411a3da0b9c4507eff8453931d5aafbc560497b`; independent artifact inspection: `PASS_RAW_AUTHORITY_AUDIT_ITER628_RETARDED_POLE_COEFFICIENTS`, `failures=[]`, root count 6, family count 13.

`N_native` remains `BLOCKED__ABSOLUTE_SOURCE_TO_NATIVE_PHASE_NORMALIZATION_NOT_YET_DERIVED_FROM_SAME_SK_FUNCTIONAL`.

MODEL_READINESS: 24%.
Readiness change: 0 percentage points.

Exact next gate: Iter629 must test, from the same doubled MSSC001+gravity functional and endpoint/Legendre conventions, whether a single common multiplicative source-to-native normalization exists at all. It must not fit `N_native` to Candidate values. If the open scalar response and native gravitational 1PI have inequivalent topology/combinatorics, record that as a structural BLOCKED result and replace the scalar-normalization bridge by the correct matched-observable/loop bridge.
