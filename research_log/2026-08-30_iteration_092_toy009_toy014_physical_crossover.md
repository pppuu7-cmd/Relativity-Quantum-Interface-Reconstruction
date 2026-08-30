# RQIR Research Log — Iteration 092

**Date:** 2026-08-30

## Goal

Continue from authoritative Iteration 091 and translate Toy009/Toy014 dominance from the historical abstract `(x,y)` plane into source-specific physical rate space, while explicitly retaining finite Ramsey reset/visibility and campaign duty.

## Result

For architecture `i`, define

`T_i = m_i[A_i/R0 + C_src/R_src,i]`, `m_i=1/(1-d_i)`.

Here

`A_i=Z^2/s_i + gamma_i sum_j 1/k_ij`

contains source-specific two-band science and seven-layer calibration coefficients.

Then

`T_14-T_09 = Delta_D/R0 + Delta_S`,

with

`Delta_D=m_14 A_14-m_09 A_09`,

`Delta_S=C_src(m_14/R_src,14-m_09/R_src,09)`.

A finite positive crossover is

`R0_cross=-Delta_D/Delta_S`.

**RQIR-RESOURCE-044:** this is the exact physical rate-space architecture crossover.

**RQIR-NG-042:** if Toy014 is worse in detector/calibration (`Delta_D>0`) and has no duty-adjusted source advantage (`Delta_S>=0`), no finite positive detector/calibration throughput can make it faster than Toy009.

## Reset/visibility source audit

Reconstructed Toy009/Toy014 hidden directions reproduce mature zero-reset Ramsey coefficients:

- Toy009 `0.0025234392`;
- Toy014 `0.00376329150`;
- ratio `1.49133432`.

For common Ramsey apparatus

`R_src=p_E Omega_E max_phi F_alpha(phi,V)/(Omega_E t_reset+phi)`.

A deterministic declared-box scan over `0.5<=V<=1` and dimensionless reset `0<=Omega_E t_reset<=1000` keeps `R_src,14/R_src,09 > 1.39` on the audited grid.

Representative ratios:

- `V=1,tau=0`: `1.49133`;
- `V=1,tau=1`: `1.57663`;
- `V=1,tau=10`: `1.90814`;
- `V=.9,tau=1`: `1.56795`;
- `V=.7,tau=10`: `2.09017`.

**RQIR-PREP-005:** Toy014's Ramsey source-metrology advantage survives the declared finite reset/visibility audit. This is a numerical design-box result, not a general theorem.

## Interpretation

Finite reset does not automatically erase the Toy014 source advantage and can strengthen it because the optimum shifts toward larger per-copy Fisher. However source advantage alone is insufficient: RESOURCE-044 requires the full detector/calibration coefficient and duty.

The historical boundary `y>7.6895+7.5421x` remains a shared-kernel regression slice of the generalized physical law.

## Files

- `analysis/toy009_toy014_physical_crossover_iteration092.py`
- `docs/PAPER_III_TOY009_TOY014_PHYSICAL_CROSSOVER_ITERATION092.md`
- `recovery/RECOVERY_DELTA_ITERATION_092.md`

## Next gate

Build conservative source-specific intervals for `A_009` and `A_014` from actual two-band science coefficients and all seven calibration-layer rate coefficients. Combine them with robust `R_src` and duty intervals and apply NG-030/RESOURCE-044. Do not begin Toy015 unless this rate-space calculation reveals a source-dependent bottleneck that a new local source could plausibly improve.
