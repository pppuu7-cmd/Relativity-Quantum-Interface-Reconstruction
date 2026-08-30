# RQIR Recovery Delta — Iteration 092

**Date:** 2026-08-30  
**Authoritative predecessor:** Iteration 091.

## New retained result

Toy009/Toy014 physical wall-clock comparison is now written directly in rate space.

For architecture `i`:

`T_i=m_i[A_i/R0+C_src/R_src,i]`,

`m_i=1/(1-d_i)`,

`A_i=Z^2/s_i + gamma_i sum_j 1/k_ij`.

The exact difference is

`T_14-T_09=Delta_D/R0+Delta_S`,

where

`Delta_D=m_14 A_14-m_09 A_09`,

`Delta_S=C_src(m_14/R_src,14-m_09/R_src,09)`.

If a positive finite crossing exists,

`R0_cross=-Delta_D/Delta_S`.

### RQIR-RESOURCE-044

This is the exact physical rate-space architecture crossover. If `Delta_D>0` and `Delta_S<0`, Toy014 wins only above `R0_cross`.

### RQIR-NG-042

If `Delta_D>0` and `Delta_S>=0`, Toy014 cannot beat Toy009 for any finite positive `R0` in the declared model. A historical zero-reset Ramsey advantage is not sufficient unless it survives reset/visibility/duty in the physical rate.

### RQIR-PREP-005

Using the repository Ramsey likelihood, the common-apparatus Toy014/Toy009 optimized source-rate ratio remains above `1.39` on the declared deterministic audit box

`0.5<=V<=1`, `0<=Omega_E t_reset<=1000`.

Zero-reset regression:

- Toy009 coefficient `0.0025234392`;
- Toy014 coefficient `0.00376329150`;
- ratio `1.49133432`.

This is a finite numerical design-box result, not a theorem beyond that Ramsey model/domain.

## Files

- `analysis/toy009_toy014_physical_crossover_iteration092.py`
- `docs/PAPER_III_TOY009_TOY014_PHYSICAL_CROSSOVER_ITERATION092.md`
- `research_log/2026-08-30_iteration_092_toy009_toy014_physical_crossover.md`

## Immediate next gate

Compute source-specific robust intervals for `A_009` and `A_014` using actual two-band science coefficients and all seven calibration rate blocks. Then combine with robust source-rate and duty intervals and apply NG-030 directly. Do not start Toy015 unless that calculation isolates a genuinely source-dependent physical bottleneck.
