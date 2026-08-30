# RQIR Iteration 094 — Robust Crossover Value-of-Information

**Date:** 2026-08-30  
**Status:** Paper-III decision/characterization gate; not a hardware forecast and not a new-physics claim.

## 1. Purpose

Iteration 093 showed that interval uncertainty can create a finite NG-043 throughput region in which neither Toy009 nor Toy014 is robustly faster. The next useful question is not to search a new source immediately, but to ask which apparatus uncertainty should be reduced first to shrink that unresolved region fastest.

For architecture `i`, retain

`T_i=m_i[A_i/R0+C_src/R_src,i]`, `m_i=1/(1-d_i)`.

For the robust statement `i` faster than `k`, define

`D_ik=m_i^+ A_i^+ - m_k^- A_k^-`,

`S_ik=C_src(m_i^+/R_i^- - m_k^-/R_k^+)`.

When a positive crossover exists,

`B_ik=-D_ik/S_ik`.

For Toy014-over-Toy009 call this upper boundary `U=B_14|09`; for Toy009-over-Toy014 call the reverse boundary `L=B_09|14`. The unresolved-band width is

`W=U-L`.

## 2. RQIR-RESOURCE-046 — analytic crossover sensitivity

For any active boundary `B=-D/S`,

`dB = -(1/S)dD + (D/S^2)dS`.

Therefore every interval-endpoint sensitivity is analytic.

For `B_ik`:

- `partial D/partial A_i^+ = m_i^+`;
- `partial D/partial A_k^- = -m_k^-`;
- `partial D/partial d_i^+ = A_i^+(m_i^+)^2`;
- `partial D/partial d_k^- = -A_k^-(m_k^-)^2`;
- `partial S/partial R_i^- = -C_src m_i^+/(R_i^-)^2`;
- `partial S/partial R_k^+ = +C_src m_k^-/(R_k^+)^2`;
- `partial S/partial d_i^+ = C_src (m_i^+)^2/R_i^-`;
- `partial S/partial d_k^- = -C_src (m_k^-)^2/R_k^+`.

This turns architecture characterization into a local value-of-information problem rather than a blind campaign to improve every subsystem equally.

## 3. Comparable characterization leverage

Raw derivatives have different units, so ranking `A`, `R_src` and `d` directly is misleading. For each uncertain interval `x in [x_-,x_+]`, define center `c`, half-width `h`, and contraction coordinate

`x_-(eta)=c-eta h`, `x_+(eta)=c+eta h`, `0<=eta<=1`.

`eta=1` is the current interval; `eta=0` is perfect characterization at the current midpoint.

Define the dimensionless local decision leverage

`Lambda_x = (1/W) dW/deta_x |_(eta=1)`.

A larger positive `Lambda_x` means reducing that interval width produces a larger first-order fractional reduction in the NG-043 unresolved band.

### RQIR-DESIGN-006 — characterize by decision leverage

Apparatus characterization should be prioritized by reduction of the robust decision interval, not by the largest raw fractional uncertainty or the easiest subsystem measurement.

## 4. Synthetic regression box

Use exactly the synthetic Iteration-093 box only as a regression test:

Toy009:

- `A=[1.0,1.1]`;
- `R_src=[1.0,1.1]`;
- `d=[0.02,0.04]`.

Toy014:

- `A=[3.3,3.8]`;
- `R_src=[1.4,1.6]`;
- `d=[0.03,0.06]`.

With `C_src=225`, Iteration 093 is reproduced:

- `L=0.025237237237237236`;
- `U=0.08006274509803925`;
- `W=0.05482550786080201`.

The analytic half-width-contraction derivatives are:

| interval | `dW/deta` | local leverage `Lambda` |
|---|---:|---:|
| Toy014 `R_src` | `0.02846048094` | `0.51911` |
| Toy009 `R_src` | `0.02343084635` | `0.42737` |
| Toy014 `A` | `0.00992863451` | `0.18110` |
| Toy014 `d` | `0.00871706182` | `0.15900` |
| Toy009 `d` | `0.00561589055` | `0.10243` |
| Toy009 `A` | `0.00193421656` | `0.03528` |

Thus, **for this synthetic box only**, source-metrology characterization has the highest decision value. This is not a universal ranking and is not an apparatus prediction.

A 50% contraction of just one interval gives unresolved-width reductions of approximately:

- Toy014 `R_src`: `22.27%`;
- Toy009 `R_src`: `19.78%`;
- Toy014 `A`: `9.05%`;
- Toy014 duty: `7.68%`;
- Toy009 duty: `5.03%`;
- Toy009 `A`: `1.76%`.

The finite reductions agree with the local leverage ordering.

## 5. New negative result — RQIR-NG-045

The parameter with the largest raw uncertainty is not necessarily the parameter with the largest architecture-decision value.

Reasons:

1. crossover sensitivity mixes detector/calibration and source terms through `B=-D/S`;
2. source-rate sensitivity scales as `1/R_src^2`;
3. duty sensitivity contains `m^2=(1-d)^-2` and can become strongly amplified at high duty loss;
4. the same interval can move both robust boundaries in different directions.

Therefore an uncertainty budget should not be ranked by percent error alone. The relevant metric is its effect on `U`, `L`, or `W`.

## 6. New guardrail — RQIR-NG-046

The derivative ranking is local to the declared uncertainty box and parameterization. It may change after a large characterization improvement, after correlations between interval inputs are introduced, or after the apparatus model changes.

Accordingly:

- use `Lambda_x` for the next measurement decision;
- recompute after a substantial interval contraction;
- for correlated posterior uncertainties, replace Cartesian endpoint derivatives by the actual joint uncertainty set rather than pretending independent boxes.

## 7. Consequence for the research programme

The next experimental-information target can now be selected quantitatively before Toy015 is attempted.

For a real Toy009/Toy014 apparatus envelope, supply actual uncertainty intervals for:

- source-specific two-band science/calibration coefficient `A_i`;
- robust source-metrology throughput `R_src,i`;
- campaign duty `d_i`.

Then compute `Lambda_x` and spend characterization effort on the largest decision leverage first.

Only if the resulting robust analysis shows that the dominant uncertainty or wall-clock penalty is intrinsically source-dependent does a Toy015 search become justified.

## 8. Reproducibility

Run

`python analysis/crossover_value_of_information_iteration094.py`.

The script verifies the analytic derivatives against finite differences and reproduces all Iteration-093 crossover boundaries before ranking the synthetic characterization levers.
