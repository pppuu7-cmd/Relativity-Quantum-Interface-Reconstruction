# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 092**.

> `docs/RECOVERY_GUIDE.md` and `docs/MASTER_TABLE.md` contain the mature framework but may lag the fast resource front. Read this pointer plus the listed recovery deltas before starting a new gate. Repository state, not chat history, is authoritative.

## Publication-track status

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–092 develop apparatus-rate closure, physical two-band likelihood, correlation/uncertainty corrections, seven-layer robust calibration, joint robust wall-clock certification, external multimode apparatus audit, a tunable simultaneous `f,2f` envelope, and now the direct physical Toy009/Toy014 rate-space crossover.

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

Conservative science rates:

`r2^-=a2 R0`, `r4^-=a4 R0`.

With worst allowed correlation `rho_+`,

`R_beta^-=s R0`,

`s = 4 a2 a4/(a2+a4+2 rho_+ sqrt(a2 a4))`.

For the seven robust calibration layers write

`R_cal,j^-=k_j R0`.

Define

`A = Z^2/s + gamma sum_j 1/k_j`.

Then

`T_total^upper = m[A/R0 + C_src/R_src^-]`, `m=1/(1-d^+)`.

**RESOURCE-043:** for target campaign cap `T_cap`, source throughput must first satisfy

`R_src^- > m C_src/T_cap`.

Above that source floor,

`R0_min = m A/[T_cap-m C_src/R_src^-]`.

**NG-041:** if `R_src^- <= m C_src/T_cap`, no finite detector/calibration improvement can rescue the requested wall-clock cap.

## Iteration 092 — direct physical Toy009/Toy014 crossover

For architecture `i`, retain its own source-specific science/calibration coefficient

`A_i = Z^2/s_i + gamma_i sum_j 1/k_ij`,

its own robust source-metrology rate `R_src,i`, and duty `d_i`:

`T_i = m_i[A_i/R0 + C_src/R_src,i]`, `m_i=1/(1-d_i)`.

Define

`Delta_D = m_14 A_14 - m_09 A_09`,

`Delta_S = C_src(m_14/R_src,14 - m_09/R_src,09)`.

Then

`T_14-T_09 = Delta_D/R0 + Delta_S`.

### RQIR-RESOURCE-044

Whenever a positive finite crossing exists,

`R0_cross = -Delta_D/Delta_S`.

If `Delta_D>0` and `Delta_S<0`, Toy014 wins only for `R0>R0_cross`: detector/calibration throughput must become sufficiently fast for Toy014's source-metrology advantage to dominate.

### RQIR-NG-042

If `Delta_D>0` and `Delta_S>=0`, Toy014 cannot beat Toy009 at any finite positive `R0` in the declared model. A zero-reset source advantage cannot be credited unless it survives reset/visibility/duty in the physical rate.

### RQIR-PREP-005

Using the repository Ramsey likelihood on a common source-metrology apparatus,

`R_src = p_E Omega_E max_phi F_alpha(phi,V)/(Omega_E t_reset+phi)`.

Zero-reset regression:

- Toy009 coefficient `0.0025234392`;
- Toy014 coefficient `0.00376329150`;
- Toy014/Toy009 rate ratio `1.49133432`.

A deterministic declared-box audit over `0.5<=V<=1` and `0<=Omega_E t_reset<=1000` keeps the optimized Toy014/Toy009 Ramsey source-rate ratio above `1.39` on the audited grid. Representative ratios include `1.57663` at `V=1,tau=1`, `1.90814` at `V=1,tau=10`, and `2.09017` at `V=.7,tau=10`.

This is a finite numerical design-box result, not a theorem beyond the stated Ramsey model/domain.

The historical shared-kernel condition

`y > 7.6895 + 7.5421 x`

remains a regression slice of RESOURCE-044.

Files:

- `analysis/toy009_toy014_physical_crossover_iteration092.py`
- `docs/PAPER_III_TOY009_TOY014_PHYSICAL_CROSSOVER_ITERATION092.md`
- `research_log/2026-08-30_iteration_092_toy009_toy014_physical_crossover.md`
- `recovery/RECOVERY_DELTA_ITERATION_092.md`

## Immediate next gate — Paper III only

Construct conservative source-specific intervals for `A_009` and `A_014` from the actual two-band science coefficients and all seven calibration-layer rate coefficients. Combine those intervals with robust `R_src` and duty intervals, then apply RESOURCE-044 and NG-030 directly.

Do not start Toy015 unless the resulting physical rate-space analysis identifies a genuinely source-dependent bottleneck that a new local source could plausibly improve.

## Discipline

Classical/stochastic/hybrid/full-QFT degeneracy, relativistic, gauge/conservation/causality/EFT/renormalization and experimental-measurability gates remain open unless explicitly closed elsewhere in the repository.
