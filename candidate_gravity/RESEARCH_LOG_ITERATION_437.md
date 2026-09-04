# RQIR Candidate Gravity — Research Log Iteration 437

## Prospective gate freeze

Iteration 437 is allocated uniquely before its numerical result is inspected. It is authorized only because Iteration 436 raw-validly certified the complete frozen `N1` parent implementation.

The gate certifies the exact Iteration-270 formula

`Q1(M,x,p,h) = -Q0(p+k_x) @ N1(M,x,p,h) @ Q0(p)`

for `M=POS`, `x in {s,a,b}`, `p=P0=[0.7,-0.4,0.5,0.9]`, and unchanged `h=3e-5`.

`Q0` is evaluated from the exact parent definition `Q0(p)=inverse(N0(p))`, `N0(p)=norb([],[],p)`, using the same arbitrary-precision parent implementation certified in Iteration 436. This avoids substituting an unbound analytic shortcut at the shifted momenta.

## Frozen inputs

For every leg, both `Q0(P0)` and `Q0(P0+k_x)` are independently evaluated at 80 and 120 decimal digits. The leg momenta/polarizations and `P0` remain exactly those of Iteration 270.

## Prospectively frozen acceptance

- precision levels: 80 and 120 decimal digits;
- max componentwise scaled `Q0_80-Q0_120 <= 1e-40` over `P0` and all shifted `P0+k_x`;
- max componentwise scaled binary64 `Q0` vs 120-digit `Q0 <= 1e-12` at those same momenta;
- max componentwise scaled `Q1_80-Q1_120 <= 1e-40` over all legs;
- all 80/120-digit `Q0`, `N1`, and `Q1` values finite;
- binary64 `Q1` vs 120-digit `Q1` is classified against the unchanged `2e-5` physical reference tolerance:
  - `<=2e-5`: legacy Q1 reproduced within the physical tolerance;
  - `>2e-5`: legacy Q1 materially different, while the multiprecision Q1 closure may still be valid if all implementation-equivalence and cross-precision gates pass.

The `2e-5` comparison is diagnostic and cannot weaken downstream Iteration-424 thresholds.

## Authority scope

Q1 precision only at the frozen Iteration-270 representative kinematics. PASS does not certify `Q2`, `A_finite`, `Acoef`, `Asub`, 368/370, 379/374, 407, Iteration 424, or physical `D_s`.

## Readiness

`MODEL_READINESS = 24%` at launch. No readiness increase from Q1 alone.
