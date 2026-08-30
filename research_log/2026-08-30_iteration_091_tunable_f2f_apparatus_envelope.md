# RQIR Research Log — Iteration 091

**Date:** 2026-08-30

## Goal

Continue from the authoritative Iteration-090 front without fabricating a fixed apparatus from incompatible literature numbers. Build the parameterized tunable simultaneous `f,2f` design envelope requested by the current front, using the robust science/calibration/source/duty laws already closed in Iterations 087–089.

## Derivation

Introduce one physical detector/calibration throughput scale `R0` and write conservative science-band rates

`r2^-=a2 R0`, `r4^-=a4 R0`.

With worst allowed correlation `rho_+`, Iteration 087 gives

`R_beta^-=s R0`,

`s=4 a2 a4/(a2+a4+2 rho_+ sqrt(a2 a4))`.

Write the seven robust calibration rates in the same declared detector family as

`R_cal,j^-=k_j R0`.

Then define

`A=Z^2/s + gamma sum_j 1/k_j`.

The joint robust upper time becomes

`T_total^upper=m[A/R0 + C_src/R_src^-]`, `m=1/(1-d^+)`.

For a requested cap `T_cap`, absolute feasibility requires

`R_src^- > m C_src/T_cap`.

Above that source floor,

`R0_min=m A/[T_cap-m C_src/R_src^-]`.

## New retained results

**RQIR-RESOURCE-043:** exact parameterized `f,2f` apparatus feasibility surface in the common physical detector/calibration scale.

**RQIR-NG-041:** detector/calibration improvements cannot rescue a source-metrology channel whose robust throughput alone exhausts the requested wall-clock cap.

This is a physical-throughput extension of NG-005, not a replacement for it.

## Shot/resource mapping

If `R0=p i0/t_cyc`, then the design requirement becomes

`p i0/t_cyc >= R0_min`.

Thus the envelope directly exposes acceptance, shot information, coherence-constrained cycle time, read/reset overhead and seven-layer calibration burden.

## Deterministic numerical checks

For the transparent normalized slice `Z=5`, `C_src=225`, `T=7 days`, `d=5%`, `a2=a4=1`, `rho=0`, `k_j=1`:

- source feasibility floor `R_src=3.91604010025e-4 s^-1`;
- Toy009 `gamma_mean=1.830264703e6`: `A=1.2811865421e7`;
- Toy014 `gamma_mean=5.6776851e6`: `A=3.9743808200e7`;
- at `R_src=10x` the floor, `R0_min(009)=24.7761870 s^-1`;
- at the same normalized slice, `R0_min(014)=76.8584428 s^-1`.

These are scaling checks, not apparatus forecasts.

The old shared-kernel Toy014/Toy009 boundary is recovered exactly:

`y > 7.6895205385 + 7.5421347000 x`.

A deterministic 1000-point random regression checks that the analytic `R0_min` saturates `T_cap` to floating precision.

## Files

- `analysis/tunable_f2f_apparatus_envelope_iteration091.py`
- `docs/PAPER_III_TUNABLE_F2F_APPARATUS_ENVELOPE_ITERATION091.md`
- `recovery/RECOVERY_DELTA_ITERATION_091.md`

## Next gate

Translate the Toy009/Toy014 crossover from the historical abstract `(x,y)` plane into source-specific physical `(R0,R_src,d)` rate space, including Toy014 Ramsey reset/visibility advantage and source-specific science/calibration coefficients. Use that rate-space result to decide whether any Toy015 source search is scientifically justified.
