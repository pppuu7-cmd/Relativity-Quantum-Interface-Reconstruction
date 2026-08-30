# RQIR Recovery Delta — Iteration 108

**Date:** 2026-08-30  
**Parent front:** Iteration 107.

## NUM-007 — exact timing overhead convention

When `T_cad` is an allowed informative/live interval and `T_ref` is a pure-dead reference block, define

`r=T_ref/T_cad`.

Then `r` is an overhead/live ratio, not total-wall duty. The exact identities are

`m_wall=1+r`,

`d_wall=r/(1+r)`,

`eta_live=1/(1+r)`.

The older `1/(1-r)` expression is only first-order accurate at small r.

## Corrected retained timing benchmarks

Toy009 centered D2 timing target: `~9.19001 us`.

Toy014 timing target: `~3.97715 us`.

Under the transparent common jitter/Brownian-drift model, Toy014 still has about a `24.91x` larger reference overhead than Toy009.

Exact wall-reference fractions:

- D=100 us^2/h: Toy014 `8.7751553e-4`, Toy009 `3.5261872e-5`;
- D=1000 us^2/h: Toy014 `8.7063953e-3`, Toy009 `3.5250685e-4`.

The qualitative low/moderate-drift conclusion is unchanged.

The old formal `r=1` point is exactly 50% total-wall reference time, not 100%. Exact 10% total-wall Toy014 timing-reference duty occurs at `D_tau~=1.26509e4 us^2/h` in the declared zero-floor benchmark.

## RESOURCE-066 — pure-dead control correction to detector ratio

For live detector ratio

`u_live=R_D,14^live/R_D,09^live`,

pure-dead timing references give

`u_wall=u_live (1+r09)/(1+r14)`.

Thus a final detector threshold `u_req` requires

`u_live > u_req (1+r14)/(1+r09)`.

Do not use this scalar correction for information-bearing reference blocks; use RESOURCE-064 constrained Fisher scheduling.

## Next gate

Create a Toy009/Toy014 control-cut status matrix. Timing is now parameterized. Geometry/additive/gain remain data-underdetermined in physical units because common transduction, drift spectra and reference Fisher rates are absent. Derive the minimum same-apparatus measurements needed to close those cuts; do not invent SI rates and do not start Toy015.

## Files

- `analysis/timing_overhead_convention_iteration108.py`
- `docs/PAPER_III_TIMING_OVERHEAD_CONVENTION_ITERATION108.md`
- `research_log/2026-08-30_iteration_108_timing_overhead_convention.md`
