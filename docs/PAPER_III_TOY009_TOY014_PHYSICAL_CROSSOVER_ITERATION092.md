# RQIR Iteration 092 — Toy009/Toy014 Physical Rate-Space Crossover

**Date:** 2026-08-30  
**Status:** Paper-III physical architecture comparison; parameterized apparatus result, not a hardware forecast and not a new-physics claim.

## 1. Purpose

Iteration 091 converted one architecture into a physical `(R0,R_src,d)` feasibility surface. The next required step is to compare Toy009 and Toy014 directly without hiding source-specific science/calibration coefficients inside the old abstract `(x,y)` plane.

For architecture `i`, write

`T_i = m_i [A_i/R0 + C_src/R_src,i]`,

with

`m_i = 1/(1-d_i)`.

Here `A_i` is the full source-specific detector+calibration coefficient,

`A_i = Z^2/s_i + gamma_i sum_j 1/k_ij`,

where `s_i` contains the source-specific two-band science coefficients `(a2_i,a4_i,rho_i)` and each `k_ij` is a source-specific robust calibration coefficient. No equality of the Toy009 and Toy014 transfer kernels is required by the derivation.

## 2. Exact crossover law

The wall-clock difference is

`T_14 - T_09 = Delta_D/R0 + Delta_S`,

where

`Delta_D = m_14 A_14 - m_09 A_09`,

`Delta_S = C_src (m_14/R_src,14 - m_09/R_src,09)`.

Therefore, whenever a positive finite crossing exists,

`boxed{R0_cross = -Delta_D/Delta_S}`.

This is the direct physical rate-space replacement for the historical abstract crossover line.

### RQIR-RESOURCE-044 — physical architecture crossover

For any pair of fixed source-specific detector/calibration coefficients, robust source-metrology rates and duty factors, architecture dominance is decided by the sign of

`Delta_D/R0 + Delta_S`.

If `Delta_D>0` but `Delta_S<0`, Toy014 is more expensive in detector/calibration resources but better in duty-adjusted source metrology. It wins only for

`boxed{R0 > R0_cross}`.

This has a simple interpretation: once detector/calibration throughput is sufficiently high, their penalty becomes small enough that Toy014's source-metrology advantage can dominate total wall clock.

## 3. New impossibility condition

### RQIR-NG-042 — no source rescue without a duty-adjusted source advantage

If

`Delta_D>0`

and

`Delta_S>=0`,

then

`T_14-T_09>0`

for every finite positive `R0`. Thus Toy014 cannot beat Toy009 merely because it had a better zero-reset Ramsey coefficient in an earlier normalized comparison. The advantage must survive reset, visibility and duty in the actual physical rate.

Conversely, if `Delta_D<0` and `Delta_S<0`, Toy014 dominates at all positive `R0` in the declared model.

## 4. Reset/visibility-aware Ramsey source rates

For a common Ramsey source-metrology apparatus define

`tau_reset = Omega_E t_reset`.

For source `i`,

`R_src,i = p_E Omega_E max_phi [F_alpha,i(phi,V)/(tau_reset+phi)]`.

The common prefactor `p_E Omega_E` cancels in the Toy014/Toy009 source-rate ratio when both are evaluated on the same source-metrology apparatus.

The repository reconstruction reproduces the mature zero-reset values:

- Toy009: `max F/phi = 0.0025234392`;
- Toy014: `max F/phi = 0.00376329150`;
- ratio `R_src,14/R_src,09 = 1.49133432`.

A deterministic reset/visibility design-box audit was then performed for

- `0.5 <= V <= 1`;
- `0 <= tau_reset <= 1000`, with dense linear/logarithmic coverage.

Across the declared scan the Toy014/Toy009 optimized source-rate ratio remains above approximately `1.39`. Representative independently reproduced values include:

| visibility | `tau_reset` | `R_src,14/R_src,09` |
|---:|---:|---:|
| 1.0 | 0 | `1.49133` |
| 1.0 | 0.1 | `1.46992` |
| 1.0 | 1 | `1.57663` |
| 1.0 | 10 | `1.90814` |
| 1.0 | 100 | `1.92911` |
| 0.9 | 1 | `1.56795` |
| 0.7 | 10 | `2.09017` |

This is a finite declared-box numerical result, not a theorem for arbitrary visibility models or arbitrary source-metrology hardware.

### RQIR-PREP-005 — Toy014 Ramsey advantage survives the audited reset/visibility box

Within the common Ramsey model and declared `(V,tau_reset)` domain, finite reset and reduced visibility do not erase Toy014's source-metrology advantage over Toy009. Large reset can increase the ratio because the optimum shifts toward larger per-copy Fisher rather than Fisher-per-interaction-time.

This does **not** by itself prove Toy014 is faster overall; RESOURCE-044 still requires the detector/calibration penalty and duty to be included.

## 5. Relation to the historical `(x,y)` boundary

Under the old shared-kernel assumptions and equal duty, the detector/calibration terms reduce to the retained resource factors

`q_s=3.53338589945`,

`q_c=3.48482822888`,

while the zero-reset source-time factor is

`q_p=0.67054046`.

Then RESOURCE-044 reduces to the historical condition

`y > 7.6895 + 7.5421 x`.

Thus the old boundary is retained as a regression slice, not discarded. Iteration 092 generalizes it to physical source-specific rates and duty.

## 6. Scientific consequence

Toy014 now has a stronger status than at Iteration 074:

- its source-metrology advantage is not merely a zero-reset artifact over the audited Ramsey box;
- but it still has a large detector/calibration burden relative to Toy009;
- therefore the existence and size of its winning region depends on the actual source-specific `A_i`, `R_src,i` and duty values.

This means a Toy015 source search is still premature. The next highest-value gate is to construct conservative source-specific `A_009` and `A_014` intervals from the two-band science coefficients and the seven calibration layers, then apply RESOURCE-044/NG-030 directly.

## 7. Reproducibility

Code:

`analysis/toy009_toy014_physical_crossover_iteration092.py`

The script reconstructs Toy009/Toy014 hidden directions from repository machinery, reproduces the mature zero-reset Ramsey coefficients, scans the declared reset/visibility box, verifies the exact positive-rate crossover algebra, and tests NG-042 with an explicit counterexample.
