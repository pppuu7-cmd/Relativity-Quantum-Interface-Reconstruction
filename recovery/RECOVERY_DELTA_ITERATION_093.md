# Recovery Delta — RQIR Iteration 093

**Date:** 2026-08-30  
**Previous authoritative front:** Iteration 092  
**New front:** Iteration 093

## What changed

Iteration 093 combines the fixed-parameter Toy009/Toy014 physical crossover (Iteration 092) with the exact robust interval wall-clock certificate (Iteration 089).

For architecture `i`:

`T_i=m_i[A_i/R0+C_src/R_src,i]`, `m_i=1/(1-d_i)`.

With independent declared intervals:

`T_i^upper=m_i^+[A_i^+/R0+C_src/R_src,i^-]`,

`T_i^lower=m_i^-[A_i^-/R0+C_src/R_src,i^+]`.

For robust Toy014 faster than Toy009:

`D_14|09=m_14^+ A_14^+-m_09^- A_09^-`,

`S_14|09=C_src(m_14^+/R_src,14^- - m_09^-/R_src,09^+)`,

so

`T_14^upper-T_09^lower=D_14|09/R0+S_14|09`.

### RQIR-RESOURCE-045

The robust crossover is exact and analytic. For `D>0,S<0` the architecture is robustly faster only above

`R0_cross^rob=-D/S`.

Reverse dominance must be evaluated independently from the reverse upper/lower pair.

### RQIR-NG-043

The two robust crossover boundaries need not coincide. There may be an intermediate throughput band where neither architecture satisfies NG-030. A nominal RESOURCE-044 winner inside that band is not a robust winner.

### RQIR-NG-044

The old `(q_s,q_c,q_p)` resource ratios are not sufficient statistics for robust physical Toy009/Toy014 dominance. Full source-specific intervals in `A_i`, `R_src,i`, and `d_i` (or the uncompressed underlying science/calibration rates) are required.

## Reproducibility

Run:

`python analysis/robust_physical_crossover_iteration093.py`

Expected headline output:

- `PASS Iteration 093 robust physical crossover`;
- synthetic Toy009 robust-win threshold `0.025237237237237236`;
- synthetic Toy014 robust-win threshold `0.08006274509803925`.

The synthetic regression is not an apparatus forecast.

## Files to read after a chat reset

1. `recovery/CURRENT_FRONT.md`;
2. this delta;
3. `docs/PAPER_III_ROBUST_PHYSICAL_CROSSOVER_ITERATION093.md`;
4. Iteration-092 physical crossover;
5. Iteration-089 joint robust total-time certificate;
6. Iterations 087–088 for science/calibration uncertainty construction.

## Immediate next gate

Derive the decision-value/sensitivity of the unresolved NG-043 band to the individual uncertainty coordinates. Prioritize apparatus characterization before any Toy015 search.
