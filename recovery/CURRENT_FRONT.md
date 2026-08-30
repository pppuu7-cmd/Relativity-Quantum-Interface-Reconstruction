# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 095**.

> `docs/RECOVERY_GUIDE.md` and `docs/MASTER_TABLE.md` contain the mature framework but may lag the fast resource front. Read this pointer plus the listed recovery deltas before starting a new gate. Repository state, not chat history, is authoritative.

## Publication-track status

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–095 develop apparatus-rate closure, physical two-band likelihood, correlation/uncertainty corrections, seven-layer robust calibration, joint robust wall-clock certification, external multimode apparatus audit, tunable simultaneous `f,2f` envelopes, direct and interval-robust Toy009/Toy014 crossover, apparatus-characterization value-of-information, and primitive physical decision Jacobians.

RQIR remains separate from RTK/DSIR. No toy, Fisher, resource or detector result is an empirical new-physics claim.

## Mature inference backbone

Primary detector quantity:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Mandatory retained gates include:

- **NG-005:** exact gravitational null calibration cannot self-calibrate hidden source amplitude;
- **NG-006/007:** low-rank control degeneracies and low-frequency stability floors can survive arbitrarily high science exposure;
- **NG-023:** H-QND source metrology is not automatically ordered-response nondemolition;
- **NG-025/026:** locality belongs inside co-design; exact rank completion is not finite-noise/resource closure;
- exact hard constraints, centered covariance derivatives and full matrix PSD/cross-PSD Fisher are mandatory.

## Physical wall-clock backbone

Use

`T_sci = Z^2/R_beta`,

`T_cal = gamma sum_j 1/R_cal,j`,

`T_src = C_src/R_src`,

and duty multiplier

`m = 1/(1-d)`.

For the common `Z=5`, 90% multiplicative source-retention benchmark, `C_src=225`.

**NG-030:** robust branch dominance requires conservative nonoverlap, `T_i^upper < T_k^lower`.

Iteration 089 gives the exact Cartesian-interval certificate

`T_total^upper = [Z^2/R_beta^- + gamma sum_j 1/R_cal,j^- + C_src/R_src^-]/(1-d^+)`,

with the corresponding lower bound from upper rates and lower duty.

## Correlated simultaneous two-band science — Iterations 084–087

For raw band Fisher rates `r2,r4` and effective ordinary covariance correlation `rho`,

`R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`, `|rho|<1`.

- **RESOURCE-039:** `rho=0` recovers twice the ordinary harmonic mean.
- **NG-036:** marginal ASD/PSD values alone do not determine simultaneous `R_beta`; cross-PSD/full spectral matrix is required.
- **CORR-001:** for fixed weak band and `rho<0`, the partner-rate optimum occurs at `r_partner/r_weak=1/rho^2`; the old `4 r_weak` statement is only the independent/nonnegative-correlation ceiling/asymptote.
- **RESOURCE-040:** for box uncertainty, the exact lower science rate uses `rho_hi` and the four rate corners.
- **NG-037:** nominal anti-correlation is not robust resource credit unless its uncertainty upper bound remains sufficiently negative.

## Seven-layer physical calibration — Iteration 088

For each integrated same-time dual-probe calibration Fisher-rate block

`F_j=[[a_j,c_j],[c_j,b_j]]`,

use

`R_cal,j=lambda_min(F_j)`.

For PSD-safe independent entry uncertainty, concavity of `lambda_min` places the exact lower envelope at one of the eight box vertices.

With `R_cal,j^-`:

`H_cal^- = 7/sum_j(1/R_cal,j^-)`,

`T_cal^upper = gamma sum_j(1/R_cal,j^-)`.

Shot/repetition mapping:

`N_acc,j >= gamma/i_j^-`,

`N_try,j = gamma/(p_j^- i_j^-)`,

`R_cal,j^- = p_j^- i_j^- / t_cyc,j^+`.

**NG-038:** uncertainty boxes crossing the PSD boundary do not certify a positive robust calibration rate.

## Source-metrology robustness — Iteration 089

**NG-039:** if the source-metrology design is fixed before uncertain apparatus parameters are known, guaranteed throughput is

`max_design min_uncertainty R`,

not `min_uncertainty max_design R`, unless adaptive retuning and its cost are explicitly included.

## External apparatus audit — Iteration 090

Published multimode levitated platforms demonstrate simultaneous multimode readout/control and full spectral-covariance reconstruction, but the audited data do not yet provide one common RQIR-normalized apparatus with both required `f,2f` science bands, seven calibration Fisher blocks, source metrology and campaign duty.

- **APP-002:** published multimode capability is not yet a complete RQIR apparatus envelope.
- **NG-040:** do not concatenate best-in-class subsystem numbers from separate experiments as though they form one joint apparatus likelihood.

## Iteration 091 — tunable simultaneous f,2f apparatus envelope

Introduce one declared physical detector/calibration Fisher-throughput scale `R0`.

`r2^-=a2 R0`, `r4^-=a4 R0`,

`R_beta^-=s R0`,

`s = 4 a2 a4/(a2+a4+2 rho_+ sqrt(a2 a4))`.

For seven robust calibration layers write

`R_cal,j^-=k_j R0`.

Define

`A = Z^2/s + gamma sum_j 1/k_j`.

Then

`T_total^upper = m[A/R0 + C_src/R_src^-]`.

**RESOURCE-043:** for target cap `T_cap`, source throughput must first satisfy

`R_src^- > m C_src/T_cap`,

and above that floor

`R0_min = m A/[T_cap-m C_src/R_src^-]`.

**NG-041:** below the source-only rate floor no finite detector/calibration improvement can rescue the requested wall clock.

## Iteration 092 — direct physical Toy009/Toy014 crossover

For architecture `i`,

`A_i = Z^2/s_i + gamma_i sum_j 1/k_ij`,

`T_i = m_i[A_i/R0 + C_src/R_src,i]`.

Define

`Delta_D = m_14 A_14 - m_09 A_09`,

`Delta_S = C_src(m_14/R_src,14 - m_09/R_src,09)`.

Then

`T_14-T_09 = Delta_D/R0 + Delta_S`.

**RESOURCE-044:** a positive finite crossing is

`R0_cross = -Delta_D/Delta_S`.

**NG-042:** if `Delta_D>0` and `Delta_S>=0`, Toy014 cannot beat Toy009 at finite positive `R0` in the declared model.

**PREP-005:** on the common Ramsey apparatus and declared reset/visibility box, the optimized Toy014/Toy009 source-rate ratio remains above `1.39`; this is a finite numerical design-box result, not a theorem.

## Iteration 093 — exact robust physical crossover

Let each architecture have independent intervals

`A_i in [A_i^-,A_i^+]`, `R_src,i in [R_src,i^-,R_src,i^+]`, `d_i in [d_i^-,d_i^+]`.

Then

`T_i^upper=m_i^+[A_i^+/R0+C_src/R_src,i^-]`,

`T_i^lower=m_i^-[A_i^-/R0+C_src/R_src,i^+]`.

For robust Toy014 faster than Toy009 define

`D_14|09=m_14^+ A_14^+-m_09^- A_09^-`,

`S_14|09=C_src(m_14^+/R_src,14^- - m_09^-/R_src,09^+)`.

**RESOURCE-045:** `T_14^upper-T_09^lower=D_14|09/R0+S_14|09`; in the common `D>0,S<0` case Toy014 is robustly faster only for `R0>-D/S`.

**NG-043:** the reverse and forward robust boundaries need not coincide; an intermediate unresolved throughput band can exist in which neither architecture is an NG-030 winner.

**NG-044:** shared-kernel Pareto ratios `(q_s,q_c,q_p)` are not sufficient statistics for robust physical dominance.

Files:

- `analysis/robust_physical_crossover_iteration093.py`
- `docs/PAPER_III_ROBUST_PHYSICAL_CROSSOVER_ITERATION093.md`
- `research_log/2026-08-30_iteration_093_robust_physical_crossover.md`
- `recovery/RECOVERY_DELTA_ITERATION_093.md`

## Iteration 094 — crossover value-of-information

For any active robust boundary

`B=-D/S`,

**RESOURCE-046** gives the exact differential

`dB=-(1/S)dD+(D/S^2)dS`.

All active interval-endpoint sensitivities in `A_i`, `R_src,i`, and `d_i` are therefore analytic.

To compare unlike coordinates, parameterize each current interval by a half-width contraction coordinate `eta`:

`x_-(eta)=c-eta h`, `x_+(eta)=c+eta h`.

For unresolved width `W=U-L`, define local decision leverage

`Lambda_x=(1/W) dW/deta_x` at `eta=1`.

**DESIGN-006:** prioritize characterization by reduction of the robust NG-043 decision band, not by raw percentage uncertainty.

**NG-045:** the largest raw fractional uncertainty need not be the highest-value measurement; source rates enter through `1/R_src`, duty through `m=(1-d)^-1`, and detector/calibration through `A/R0`.

**NG-046:** the leverage ranking is local to the declared uncertainty geometry and must be recomputed after substantial contraction; correlated primitive uncertainties require their joint uncertainty set rather than independent Cartesian boxes.

The Iteration-093 synthetic box is reproduced exactly. Its local leverage ordering is: Toy014 `R_src`, Toy009 `R_src`, Toy014 `A`, Toy014 duty, Toy009 duty, Toy009 `A`. This ranking is a regression example only, not an apparatus prediction.

Files:

- `analysis/crossover_value_of_information_iteration094.py`
- `docs/PAPER_III_CROSSOVER_VALUE_OF_INFORMATION_ITERATION094.md`
- `research_log/2026-08-30_iteration_094_crossover_value_of_information.md`
- `recovery/RECOVERY_DELTA_ITERATION_094.md`

## Iteration 095 — primitive physical decision Jacobian

The aggregate apparatus coefficient can now be differentiated directly with respect to measurable primitive inputs.

For two-band science,

`A_sci=Z^2[1/(4a2)+1/(4a4)+rho/(2 sqrt(a2 a4))]`.

**RESOURCE-047:** compose its exact `(a2,a4,rho)` gradient with RESOURCE-046's outer `dB/dA_i` to obtain local primitive crossover sensitivity.

For each calibration block `F_j=[[u,w],[w,v]]`, use `k_j=lambda_min(F_j)` and its exact matrix-entry gradient away from repeated eigenvalues. Since `A_cal=gamma sum_j 1/k_j`, equal fractional rate improvement gives

`dA=-(gamma/k_j)d ln k_j`.

**DESIGN-007:** characterize the slowest/largest-wall-clock calibration layer first under equal fractional improvement, not the block with the largest raw entry uncertainty.

Source metrology on a smooth fixed/unique-optimum branch is written

`R_src=p_E Omega_E q(V,Omega_E t_reset)`,

with exact primitive derivatives in preparation success, coupling, reset and visibility.

**NG-047:** under `rho<0`, increasing one raw band rate is not globally monotone useful; `dA/da2` changes sign at `a2/a4=1/rho^2`, reproducing CORR-001 locally.

**NG-048:** local primitive VOI derivatives do not apply at repeated calibration eigenvalues, PSD-boundary contact, worst-case uncertainty-corner changes or robust-boundary active-set changes; use exact finite contractions/subgradients/robust optimization there.

Files:

- `analysis/primitive_decision_jacobian_iteration095.py`
- `docs/PAPER_III_PRIMITIVE_DECISION_JACOBIAN_ITERATION095.md`
- `research_log/2026-08-30_iteration_095_primitive_decision_jacobian.md`
- `recovery/RECOVERY_DELTA_ITERATION_095.md`

## Immediate next gate — Paper III only

Construct one declared primitive uncertainty envelope for Toy009 and Toy014: source-specific `a2,a4,rho`, all seven `2x2` calibration Fisher blocks, source preparation/coupling/reset/visibility, and control duty. Evaluate the Iteration-095 Jacobian on the active robust branches and use finite contraction wherever NG-048 triggers. Identify the actual highest-value characterization measurement by reduction of the NG-043 unresolved band.

Do not start Toy015 unless the physical rate-space analysis identifies a genuinely source-dependent bottleneck that a new local source could plausibly improve.

## Discipline

Classical/stochastic/hybrid/full-QFT degeneracy, relativistic, gauge/conservation/causality/EFT/renormalization and experimental-measurability gates remain open unless explicitly closed elsewhere in the repository.
