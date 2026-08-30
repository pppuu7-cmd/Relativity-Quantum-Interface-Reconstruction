# RQIR Recovery Delta — Iteration 095

**Date:** 2026-08-30  
**Authority:** append to `docs/RECOVERY_GUIDE.md` / `recovery/CURRENT_FRONT.md` when restoring the active Paper-III front.

## New retained results

### RESOURCE-047 — primitive science decision Jacobian

For `r2=a2 R0`, `r4=a4 R0`,

`A_sci=Z^2/s=Z^2[1/(4a2)+1/(4a4)+rho/(2 sqrt(a2 a4))]`.

Derivatives:

`dA/da2=-Z^2/(4a2^2)-Z^2 rho/(4 a2^(3/2) sqrt(a4))`,

`dA/da4=-Z^2/(4a4^2)-Z^2 rho/(4 a4^(3/2) sqrt(a2))`,

`dA/drho=Z^2/(2 sqrt(a2 a4))`.

Compose with Iteration-094 `dB/dA_i` to obtain primitive crossover sensitivity.

### DESIGN-007 — calibration bottleneck characterization

For one normalized same-time dual-probe block `F_j=[[u,w],[w,v]]`,

`k_j=lambda_min(F_j)` and `A_cal=gamma sum_j 1/k_j`.

For equal fractional improvements,

`dA = -(gamma/k_j) d ln k_j`.

Therefore the layer with the smallest `k_j` / largest current `gamma/k_j` time contribution has the largest first-order characterization value.

### Source-metrology primitive derivatives

On a smooth fixed/unique-optimum branch write

`R_src=p_E Omega_E q(V,tau)`, `tau=Omega_E t_reset`.

Then

`dR/dp_E=Omega_E q`,

`dR/dV=p_E Omega_E q_V`,

`dR/dt_reset=p_E Omega_E^2 q_tau`,

`dR/dOmega_E=p_E(q+tau q_tau)`.

NG-039 remains mandatory for robust pre-declared designs.

## New guardrails

- **NG-047:** with `rho<0`, raw single-band rate is not a monotone experiment-quality coordinate. `dA/da2` changes sign at `a2/a4=1/rho^2`, the local form of CORR-001.
- **NG-048:** ordinary primitive VOI derivatives are invalid at repeated calibration eigenvalues, PSD-boundary contact, worst-case corner changes or robust-boundary active-set changes. Use exact finite contractions/subgradients/robust optimization there.

## Reproducibility

- `analysis/primitive_decision_jacobian_iteration095.py`
- `docs/PAPER_III_PRIMITIVE_DECISION_JACOBIAN_ITERATION095.md`
- `research_log/2026-08-30_iteration_095_primitive_decision_jacobian.md`

## Immediate next gate

Build a declared Toy009/Toy014 primitive uncertainty envelope and evaluate actual primitive-level decision leverage. Do not start Toy015 unless that exercise identifies a genuinely source-dependent bottleneck.
