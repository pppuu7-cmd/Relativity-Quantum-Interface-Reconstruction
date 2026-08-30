# RQIR Recovery Delta — Iteration 091

**Date:** 2026-08-30  
**Authority:** append to `docs/RECOVERY_GUIDE.md` and `recovery/CURRENT_FRONT.md`; repository remains source of truth.

## New front

Iteration 091 builds the parameterized simultaneous tunable `f,2f` apparatus envelope requested by the Iteration-090 next gate. It does not instantiate a measured apparatus and does not change Paper I/II closure.

## Core parameterization

Use one declared physical detector/calibration throughput scale `R0`.

Science:

`r2^-=a2 R0`, `r4^-=a4 R0`,

`R_beta^-=s R0`,

`s=4 a2 a4/(a2+a4+2 rho_+ sqrt(a2 a4))`.

Seven calibration layers:

`R_cal,j^-=k_j R0`, `k_j>0`.

Define

`A=Z^2/s + gamma sum_j 1/k_j`.

With source requirement `C_src`, robust source rate `R_src^-`, upper duty `d^+`, and `m=1/(1-d^+)`:

`T_total^upper=m[A/R0 + C_src/R_src^-]`.

## RQIR-RESOURCE-043

For wall-clock cap `T_cap`, source throughput must first satisfy

`R_src^- > m C_src/T_cap`.

Then

`R0_min=m A/[T_cap-m C_src/R_src^-]`.

This is the exact common-scale detector/calibration feasibility surface.

## RQIR-NG-041

If

`R_src^- <= m C_src/T_cap`,

no finite detector/calibration improvement can satisfy the requested campaign cap. This is a physical throughput no-rescue boundary after NG-005 has already required an independent source channel.

## Shot mapping

For per-attempt information `i0`, acceptance `p`, and coherence/read/reset constrained cycle time `t_cyc`,

`R0=p i0/t_cyc`.

Therefore require

`p i0/t_cyc >= R0_min`.

The same `R0` scaling may be assigned to a calibration layer only when one declared likelihood physically implies `R_cal,j=k_j R0`; otherwise revert to the general Iteration-089 independent-rate certificate.

## Regression / transparent normalized slice

For `Z=5`, `C_src=225`, `T=7 days`, `d=5%`, `a2=a4=1`, `rho=0`, `k_j=1`:

- source floor `3.91604010025e-4 s^-1`;
- Toy009 `gamma_mean=1.830264703e6`: `A=1.2811865421e7`;
- Toy014 `gamma_mean=5.6776851e6`: `A=3.9743808200e7`;
- at `R_src=10x floor`, `R0_min(009)=24.7761870 s^-1`;
- `R0_min(014)=76.8584428 s^-1`.

These are normalized design checks only, not hardware forecasts.

The historical shared-kernel Toy014/Toy009 boundary is recovered:

`y > 7.6895205385 + 7.5421347000 x`.

## Reproduce

`python analysis/tunable_f2f_apparatus_envelope_iteration091.py`

## Next gate

Build the Toy009/Toy014 robust crossover directly in physical `(R0,R_src,d)` coordinates using source-specific science/calibration coefficients and Ramsey reset/visibility surfaces. Do not start Toy015 unless that analysis demonstrates a source-dependent bottleneck that a new source can improve.
