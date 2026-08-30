# RQIR Iteration 095 — Primitive Physical Decision Jacobian

**Date:** 2026-08-30  
**Status:** Paper-III apparatus-characterization gate; analytic/local result, not a hardware forecast and not a new-physics claim.

## 1. Purpose

Iteration 094 ranked uncertainty only in the aggregate variables `A_i`, `R_src,i`, and duty. The next required step is to expose those aggregates back to measurable primitive inputs: the two science-band rates/correlation, each of the seven `2x2` calibration Fisher blocks, source-metrology throughput parameters, and controls.

This iteration derives the exact local chain rule needed for primitive-level value of information.

## 2. Science primitive Jacobian

With

`r2=a2 R0`, `r4=a4 R0`,

and effective ordinary covariance correlation `rho`, the two-band profiled science coefficient is

` s = 4 a2 a4/(a2+a4+2 rho sqrt(a2 a4)) `.

The science contribution to the physical coefficient `A` is

` A_sci = Z^2/s `,

or exactly

` A_sci = Z^2[1/(4a2)+1/(4a4)+rho/(2 sqrt(a2 a4))]. `

Therefore

`dA_sci/da2 = -Z^2/(4 a2^2) - Z^2 rho/(4 a2^(3/2) sqrt(a4))`,

`dA_sci/da4 = -Z^2/(4 a4^2) - Z^2 rho/(4 a4^(3/2) sqrt(a2))`,

`dA_sci/drho = Z^2/(2 sqrt(a2 a4))`.

### RQIR-RESOURCE-047 — primitive science decision Jacobian

Once the outer robust boundary derivative `dB/dA_i` from RESOURCE-046 is known, every local science primitive has exact crossover sensitivity

`dB/dx = (dB/dA_i)(dA_i/dx)`.

No additional Fisher inversion is required for this local characterization step.

## 3. Anti-correlation sign reversal survives at the apparatus-decision level

Factor the first derivative as

`dA_sci/da2 = -Z^2/(4 a2^2) [1 + rho sqrt(a2/a4)].`

For `rho>=0` it is negative: increasing a band rate improves the science budget.

For `rho<0`, the sign changes at

` a2/a4 = 1/rho^2. `

Above that point, increasing `a2` alone **increases** `A_sci`, i.e. worsens profiled science time. This is the differential form of CORR-001's finite partner-rate optimum.

### RQIR-NG-047 — raw single-band SNR is not a monotone characterization target under negative correlation

When `rho<0`, apparatus characterization or tuning must be scored through the profiled two-band likelihood. A larger marginal rate in one band is not automatically a better experiment after the anti-correlated nuisance geometry is included.

## 4. Seven calibration blocks: exact matrix-entry derivatives

For one normalized same-time dual-probe calibration block

`F_j=[[a,b],[c,b?]]`

use the symmetric notation

`F_j=[[u,w],[w,v]]`.

Its robust scalar rate coordinate is

`k_j=lambda_min(F_j)`

with

`lambda_- = (u+v-Delta)/2`,

`Delta=sqrt((u-v)^2+4w^2)`.

Away from a repeated eigenvalue (`Delta>0`),

`dlambda_-/du = [1-(u-v)/Delta]/2`,

`dlambda_-/dv = [1+(u-v)/Delta]/2`,

`dlambda_-/dw = -2w/Delta`.

Since

` A_cal = gamma sum_j 1/k_j, `

we have

` dA/dk_j = -gamma/k_j^2. `

For a fractional improvement `d ln k_j`,

` dA = -(gamma/k_j) d ln k_j. `

### RQIR-DESIGN-007 — calibration bottleneck characterization law

For equal fractional improvements in independently characterized calibration rates, the layer with the **smallest `k_j`** (largest `gamma/k_j` wall-clock contribution) gives the largest first-order reduction in `A`.

Thus calibration characterization should be prioritized by current wall-clock/Fisher contribution, not by the largest raw matrix-entry uncertainty.

## 5. Calibration differentiability guard

At a repeated eigenvalue (`Delta=0`) `lambda_min` is not differentiable as an ordinary scalar function of the matrix entries. Likewise, if an uncertainty set approaches the PSD boundary, a local derivative cannot replace the exact robust vertex/PSD audit of Iteration 088.

### RQIR-NG-048 — local primitive VOI fails at active-set/eigenvalue singularities

Primitive derivative rankings are valid only inside a fixed smooth branch. Repeated eigenvalues, PSD-boundary contact, changes of the worst-case uncertainty corner, or changes of the active robust crossover require recomputation with finite contractions/subgradients or the exact uncertainty optimization.

This extends NG-046 from correlated uncertainty geometry to nonsmooth active-set changes.

## 6. Source-metrology primitive map

Write the optimized/fixed-design Ramsey-like source rate as

`R_src = p_E Omega_E q(V,tau)`,

`tau = Omega_E t_reset`,

where `q=F_alpha(phi,V)/(tau+phi)` evaluated at the declared protocol design. On a smooth branch (or at a unique interior optimum where the envelope theorem applies),

`dR/dp_E = Omega_E q = R/p_E`,

`dR/dV = p_E Omega_E q_V`,

`dR/dt_reset = p_E Omega_E^2 q_tau`,

`dR/dOmega_E = p_E[q + tau q_tau]`.

For optimized source metrology these derivatives are only valid while the same unique optimum/worst-case branch remains active. NG-039 still applies: a robust pre-declared design uses `max_design min_uncertainty`, not a hindsight `min max`.

The outer crossover derivative from Iteration 094 then gives

`dB/dx = (dB/dR_src)(dR_src/dx)`.

This directly turns preparation success, coupling, visibility and reset-time characterization into decision leverage.

## 7. Full primitive chain rule

For any active robust boundary

`B=-D/S`,

RESOURCE-046 gives

`dB=-(1/S)dD+(D/S^2)dS`.

Iteration 095 therefore supplies the missing inner Jacobian:

- science: `(a2,a4,rho) -> A_sci`;
- calibration: each matrix entry `-> lambda_min -> gamma/k_j`;
- source: `(p_E,Omega_E,t_reset,V) -> R_src`;
- controls: duty remains direct through `m=(1-d)^-1`.

The primitive measurement priority is the composition of these inner derivatives with the outer decision derivative, evaluated on the currently active uncertainty branch.

## 8. Deterministic numerical checks

`analysis/primitive_decision_jacobian_iteration095.py` verifies analytic derivatives against central finite differences.

Synthetic regression point for science:

`(a2,a4,rho)=(1.2,0.8,-0.3)` gives

- `dA/da2 = -2.74555789315`;
- `dA/da4 = -7.37354517306`;
- `dA/drho = 12.7577590770`.

Synthetic calibration block `(u,v,w)=(1.5,2.2,0.3)` gives

- `dlambda/du = 0.879628301183`;
- `dlambda/dv = 0.120371698817`;
- `dlambda/dw = -0.650791373456`.

For the synthetic seven-layer check with `gamma=2` and `k=(1.1,1.5,2,2.5,3,4,5)`, the slowest layer contributes `gamma/k=1.8181818`, the largest first-order calibration leverage under equal fractional rate improvement.

The anti-correlation sign-flip test with `rho=-0.5`, `a4=1` occurs exactly at `a2=4`, matching `a2/a4=1/rho^2`.

All examples are regression checks only.

## 9. Scientific consequence

The apparatus-characterization problem is now reducible to measurable primitives without inventing an absolute ASD. The next physically admissible step is not Toy015. It is to supply one declared source-specific primitive uncertainty envelope for Toy009 and Toy014, evaluate these Jacobians on its active robust corners, and rank the actual measurements by reduction of the NG-043 unresolved band.

If that exercise identifies a source-geometry bottleneck rather than a common detector/reference bottleneck, then a new local-source search becomes scientifically motivated.
