# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 091**.

> `docs/RECOVERY_GUIDE.md` and `docs/MASTER_TABLE.md` contain the mature framework but may lag the fast resource front. Read this pointer plus the listed recovery deltas before starting a new gate. Repository state, not chat history, is authoritative.

## Publication-track status

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–091 develop apparatus-rate closure, physical two-band likelihood, correlation/uncertainty corrections, seven-layer robust calibration, joint robust wall-clock certification, external multimode apparatus audit, and now a parameterized tunable simultaneous `f,2f` apparatus envelope.

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

Files:

- `analysis/external_multimode_compatibility_iteration090.py`
- `docs/PAPER_III_EXTERNAL_MULTIMODE_APPARATUS_AUDIT_ITERATION090.md`
- `research_log/2026-08-30_iteration_090_external_multimode_apparatus_audit.md`
- `recovery/RECOVERY_DELTA_ITERATION_090.md`

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

### RQIR-RESOURCE-043

For target campaign cap `T_cap`, source throughput must first satisfy

`R_src^- > m C_src/T_cap`.

When this holds,

`R0_min = m A/[T_cap - m C_src/R_src^-]`.

This is the exact parameterized common-scale detector/calibration feasibility surface.

### RQIR-NG-041

If

`R_src^- <= m C_src/T_cap`,

no finite detector/calibration improvement can rescue the requested wall-clock cap. This is a physical-throughput extension of NG-005: existence of an independent source channel is not sufficient if its robust rate is too low.

Shot mapping:

`R0=p i0/t_cyc`,

so the apparatus must satisfy

`p i0/t_cyc >= R0_min`,

with `t_cyc` respecting the source coherence/evolution floor plus read/reset overhead.

Transparent normalized 7-day algebra check (`Z=5`, `C_src=225`, `d=5%`, `a2=a4=1`, `rho=0`, `k_j=1`):

- source floor `3.91604010025e-4 s^-1`;
- Toy009 `gamma_mean=1.830264703e6`: `A=1.2811865421e7`;
- Toy014 `gamma_mean=5.6776851e6`: `A=3.9743808200e7`;
- at `R_src=10x` source floor, `R0_min(009)=24.7761870 s^-1`, `R0_min(014)=76.8584428 s^-1`.

These are normalized design checks, not apparatus forecasts.

The historical shared-kernel Toy014/Toy009 regression is recovered exactly:

`y > 7.6895205385 + 7.5421347000 x`.

Files:

- `analysis/tunable_f2f_apparatus_envelope_iteration091.py`
- `docs/PAPER_III_TUNABLE_F2F_APPARATUS_ENVELOPE_ITERATION091.md`
- `research_log/2026-08-30_iteration_091_tunable_f2f_apparatus_envelope.md`
- `recovery/RECOVERY_DELTA_ITERATION_091.md`

## Immediate next gate — Paper III only

Translate Toy009/Toy014 dominance from the historical abstract `(x,y)` plane into source-specific physical `(R0,R_src,d)` rate space:

1. include Toy014 Ramsey reset/visibility dependence and its retained source-metrology advantage;
2. retain source-specific science coefficients `(a2,a4,rho)` and seven calibration coefficients `k_j` rather than assuming shared kernels;
3. derive robust crossover surfaces and identify whether Toy014 has a physically accessible winning region;
4. use that result to decide whether a Toy015 source search is justified.

Do not start Toy015 unless the rate-space analysis reveals a genuinely source-dependent bottleneck that a new source design can improve.

## Discipline

Classical/stochastic/hybrid/full-QFT degeneracy, relativistic, gauge/conservation/causality/EFT/renormalization and experimental-measurability gates remain open unless explicitly closed elsewhere in the repository.
