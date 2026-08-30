# RQIR Research Log — Iteration 093

**Date:** 2026-08-30

## Goal

Continue from authoritative Iteration 092 and convert its fixed-parameter physical Toy009/Toy014 crossover into an exact NG-030 robust crossover under source-specific uncertainty in detector+calibration coefficient `A_i`, source-metrology rate `R_src,i`, and campaign duty `d_i`.

No closed Paper-I/II gate was reopened and no Toy015 search was started.

## Result

For architecture `i`,

`T_i=m_i[A_i/R0+C_src/R_src,i]`, `m_i=1/(1-d_i)`.

With independent intervals, exact time envelopes are

`T_i^upper=m_i^+[A_i^+/R0+C_src/R_src,i^-]`,

`T_i^lower=m_i^-[A_i^-/R0+C_src/R_src,i^+]`.

For robust Toy014-over-Toy009 dominance define

`D_14|09=m_14^+ A_14^+-m_09^- A_09^-`,

`S_14|09=C_src(m_14^+/R_src,14^- - m_09^-/R_src,09^+)`.

Then

`T_14^upper-T_09^lower=D_14|09/R0+S_14|09`.

**RQIR-RESOURCE-045:** the robust crossover is analytic. In the common rescue case `D>0,S<0`, Toy014 is certified faster only for

`R0>-D/S`.

The reverse Toy009 certificate is built independently from `T_09^upper-T_14^lower`.

## New negative results

**RQIR-NG-043:** the two robust boundaries generally differ, creating an `R0` interval in which neither branch satisfies NG-030 even if the nominal RESOURCE-044 comparison has a definite winner. The width of this unresolved band is therefore a characterization target.

**RQIR-NG-044:** the retained shared-kernel Pareto summary `(q_s,q_c,q_p)` is not sufficient for robust physical architecture dominance because it does not encode source-specific transfer/cross-PSD uncertainty, seven matrix calibration-rate intervals, source-metrology intervals and duty intervals.

## Regression

Synthetic-only test box with `C_src=225` gives

- Toy009 robust win: `R0 < 0.025237237237237236`;
- unresolved NG-030 band: `[0.025237237237237236,0.08006274509803925]`;
- Toy014 robust win: `R0 > 0.08006274509803925`.

The script checks all corner extrema and 10,000 deterministic random interior samples. These numbers are not hardware forecasts.

## Files

- `analysis/robust_physical_crossover_iteration093.py`
- `docs/PAPER_III_ROBUST_PHYSICAL_CROSSOVER_ITERATION093.md`
- `recovery/RECOVERY_DELTA_ITERATION_093.md`

## Next gate

Compute the sensitivity of the two robust crossover boundaries and unresolved-band width to each physical uncertainty coordinate (`A_i`, `R_src,i`, `d_i`). Use that to rank which apparatus characterization measurement has highest decision value before spending effort on a new Toy015 source search.
