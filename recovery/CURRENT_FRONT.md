# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 093**.

> `docs/RECOVERY_GUIDE.md` and `docs/MASTER_TABLE.md` contain the mature framework but may lag the fast resource front. Read this pointer plus the listed recovery deltas before starting a new gate. Repository state, not chat history, is authoritative.

## Publication-track status

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–093 develop apparatus-rate closure, physical two-band likelihood, correlation/uncertainty corrections, seven-layer robust calibration, joint robust wall-clock certification, external multimode apparatus audit, a tunable simultaneous `f,2f` envelope, direct physical Toy009/Toy014 crossover, and now the exact interval-robust architecture crossover.

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

**RESOURCE-044:** whenever a positive finite crossing exists,

`R0_cross = -Delta_D/Delta_S`.

**NG-042:** if `Delta_D>0` and `Delta_S>=0`, Toy014 cannot beat Toy009 at any finite positive `R0` in the declared model.

**PREP-005:** on the common Ramsey apparatus and declared reset/visibility box, Toy014/Toy009 optimized source-rate ratio remains above `1.39`; this is a finite numerical design-box result.

The historical shared-kernel condition `y > 7.6895 + 7.5421 x` remains a regression slice of RESOURCE-044.

## Iteration 093 — exact robust physical crossover

Let each architecture have declared independent intervals

`A_i in [A_i^-,A_i^+]`,

`R_src,i in [R_src,i^-,R_src,i^+]`,

`d_i in [d_i^-,d_i^+]`.

Then

`T_i^upper=m_i^+[A_i^+/R0+C_src/R_src,i^-]`,

`T_i^lower=m_i^-[A_i^-/R0+C_src/R_src,i^+]`.

For robust Toy014 faster than Toy009 define

`D_14|09=m_14^+ A_14^+-m_09^- A_09^-`,

`S_14|09=C_src(m_14^+/R_src,14^- - m_09^-/R_src,09^+)`.

### RQIR-RESOURCE-045

`T_14^upper-T_09^lower=D_14|09/R0+S_14|09`.

Thus the NG-030 robust crossover is analytic. In the common rescue case `D>0,S<0`, Toy014 is robustly faster only for

`R0>-D/S`.

The reverse Toy009 certificate must be evaluated independently from `T_09^upper-T_14^lower`.

### RQIR-NG-043

The two robust crossover boundaries need not coincide. An intermediate throughput interval can exist in which neither architecture is robustly faster. A nominal RESOURCE-044 winner inside this interval is not an NG-030 winner. The width of this unresolved band is an apparatus-characterization target.

### RQIR-NG-044

The retained shared-kernel Pareto ratios `(q_s,q_c,q_p)` are not sufficient statistics for robust physical dominance because they do not encode source-specific transfer/cross-PSD uncertainty, all seven matrix calibration-rate intervals, robust source-metrology intervals and duty uncertainty.

Files:

- `analysis/robust_physical_crossover_iteration093.py`
- `docs/PAPER_III_ROBUST_PHYSICAL_CROSSOVER_ITERATION093.md`
- `research_log/2026-08-30_iteration_093_robust_physical_crossover.md`
- `recovery/RECOVERY_DELTA_ITERATION_093.md`

## Immediate next gate — Paper III only

Derive the sensitivity/value-of-information of the two robust crossover boundaries and the NG-043 unresolved-band width to uncertainty in `A_i`, `R_src,i` and `d_i`. Use it to prioritize which apparatus characterization measurement should be improved first.

Do not start Toy015 unless the physical rate-space analysis identifies a genuinely source-dependent bottleneck that a new local source could plausibly improve.

## Discipline

Classical/stochastic/hybrid/full-QFT degeneracy, relativistic, gauge/conservation/causality/EFT/renormalization and experimental-measurability gates remain open unless explicitly closed elsewhere in the repository.
